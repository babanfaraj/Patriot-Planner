import matplotlib.pylab as plt

from python_src import db_connection as db_conn
from python_src.models import Edge


def visualize_map():
    """Displays a connected graph of the map"""
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    graph = db_conn.get_graph()
    for parent_node in graph.items():
        x1, y1 = parent_node[0].coords()
        label = '{} ({})'.format(parent_node[0].location_name,
                                 parent_node[0].building)
        ax1.annotate(label, (x1, y1))
        ax1.plot(x1, y1, 'ro')
        for child_node in parent_node[1]:
            x2, y2 = child_node.coords()
            ax1.plot(x2, y2, 'ro')
            label = '{} ({})'.format(child_node.location_name, child_node.building)
            ax1.annotate(label, (x2, y2))
            e = Edge.query.filter_by(location1=parent_node[0].location_name,
                                     location2=child_node.location_name).all()
            if len(e) == 0:
                e = Edge.query.filter_by(
                    location1=child_node.location_name,
                    location2=parent_node[0].location_name).all()
            # Plot active edges with green lines and inactive with red lines
            if e[0].is_active:
                ax1.plot([x1, x2], [y1, y2], 'g-')
            else:
                ax1.plot([x1, x2], [y1, y2], 'r-')
    plt.show()

