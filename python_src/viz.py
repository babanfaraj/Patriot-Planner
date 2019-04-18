import matplotlib.pylab as plt

from python_src import db_connection as db_conn
from python_src.models import Edge


def visualize_map(path=None, label_nodes=True):
    """Displays a connected graph of the map"""
    edges = None
    if path is not None and len(path) > 1:
        edges = [[path[i - 1].location_name, path[i].location_name]
                 for i in range(1, len(path))]
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)

    graph = db_conn.get_graph(include_inactive_edges=True)
    for parent_node in graph.items():
        x1, y1 = parent_node[0].coords()

        # Color road nodes as black and path as blue
        if path is not None and parent_node[0] in path:
            ax1.plot(x1, y1, c='b', marker='s')
        elif parent_node[0].location_name[0:2] == 'Rd':
            ax1.plot(x1, y1, c='k', marker='o')
        else:
            ax1.plot(x1, y1, c='r', marker='o')

        # Add the node's label
        if label_nodes:
            label = '{}'.format(parent_node[0].location_name)
            ax1.annotate(label, (x1, y1))

        for child_node in parent_node[1]:
            x2, y2 = child_node.coords()

            # Color road nodes as black and path as blue
            if path is not None and child_node in path:
                ax1.plot(x1, y1, c='b', marker='s')
            elif child_node.location_name[0:2] == 'Rd':
                ax1.plot(x2, y2, c='k', marker='o')
            else:
                ax1.plot(x2, y2, c='r', marker='o')

            # Add the node's label
            if label_nodes:
                label = '{}'.format(child_node.location_name)
                ax1.annotate(label, (x2, y2))

            # Get the edge connecting the locations
            e = Edge.query.filter_by(location1=parent_node[0].location_name,
                                     location2=child_node.location_name).all()
            if len(e) == 0:
                e = Edge.query.filter_by(
                    location1=child_node.location_name,
                    location2=parent_node[0].location_name).all()

            # Plot active edges with green lines and inactive with red lines
            if e[0].is_active:
                p_loc = parent_node[0].location_name
                c_loc = child_node.location_name
                if (edges is not None and
                        ([p_loc, c_loc] in edges or [c_loc, p_loc] in edges)):
                    ax1.plot([x1, x2], [y1, y2], 'b-')
                else:
                    ax1.plot([x1, x2], [y1, y2], 'g-')
            else:
                ax1.plot([x1, x2], [y1, y2], 'r-')
    plt.show()

