import matplotlib.pyplot as plt

from python_src import db_connection as db_conn
from python_src.models import Edge


def visualize_map(path=None, label_nodes=True):
    """Displays a connected graph of the map"""
    edges = None
    path_locs = None
    if path is not None:
        path_locs = [_.location_name for _ in path]
        if len(path) > 1:
            edges = [[path[i - 1].location_name, path[i].location_name]
                     for i in range(1, len(path))]
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    plotted_locs = set()
    plotted_edges = set()

    graph = db_conn.get_graph(include_inactive_edges=True)
    for parent_node, child_nodes in graph.items():
        x1, y1 = parent_node.coords()
        if parent_node.location_name not in plotted_locs:
            plot_location(ax1, parent_node, path_locs=path_locs, path=path,
                          label_nodes=label_nodes)
            plotted_locs.add(parent_node.location_name)

        for child_node in child_nodes:
            x2, y2 = child_node.coords()
            if child_node.location_name not in plotted_locs:
                plot_location(ax1, child_node, path_locs=path_locs, path=path,
                              label_nodes=label_nodes)
                plotted_locs.add(child_node.location_name)

            # Get the edge connecting the locations
            e = Edge.query.filter_by(location1=parent_node.location_name,
                                     location2=child_node.location_name).first()
            if e is None:
                e = Edge.query.filter_by(
                    location1=child_node.location_name,
                    location2=parent_node.location_name).first()

            # Plot active edges with green lines and inactive with red lines
            if e is not None and e.locations not in plotted_edges:
                if e.is_active:
                    p_loc = parent_node.location_name
                    c_loc = child_node.location_name
                    if (edges is not None and
                            ([p_loc, c_loc] in edges or [c_loc, p_loc] in edges)):
                        ax1.plot([x1, x2], [y1, y2], 'b-')
                    else:
                        ax1.plot([x1, x2], [y1, y2], 'g-')
                else:
                    ax1.plot([x1, x2], [y1, y2], 'r-')
                plotted_edges.add(e)
    plt.show()


def plot_location(ax, loc, path_locs=None, path=None, label_nodes=True):
    x, y = loc.coords()
    # Color road nodes as black and path as blue
    if path is not None and loc.location_name in path_locs:
        ax.plot(x, y, c='b', marker='s')
    elif loc.location_name[0:2] == 'Rd':
        ax.plot(x, y, c='k', marker='o')
    else:
        ax.plot(x, y, c='r', marker='o')

    # Add the node's label
    if label_nodes:
        label = '{}'.format(loc.location_name)
        ax.annotate(label, (x, y))


if __name__ == '__main__':
    visualize_map(path=None, label_nodes=True)

