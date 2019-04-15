import matplotlib.pylab as plt

from python_src import db_connection as db_conn


def visualize_map():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    graph = db_conn.get_graph()
    for parent_node in graph.items():
        x1, y1 = parent_node[0].coords()
        ax1.annotate(parent_node[0].location_name, (x1, y1))
        ax1.plot(x1, y1, 'ro')
        for child_node in parent_node[1]:
            x2, y2 = child_node.coords()
            ax1.plot(x2, y2, 'ro')
            ax1.annotate(child_node.location_name, (x2, y2))
            ax1.plot([x1, x2], [y1, y2], 'k-')
    plt.show()


def draw_line(ax, coords1, coords2):
    for i in range(1, 51):
        step = 1. / i



