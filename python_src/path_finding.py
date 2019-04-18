from python_src.models import Location
from python_src.db_connection import get_graph
from python_src.db_connection import *
from python_src.viz import visualize_map


def find_optimal_class_path(start_loc, classes):
    """
    :param start_loc: A starting location.
    :param classes:
      A list of class locations in chronological order, Assume these classes all occur on the same day.
    """
    if classes is None or len(classes) == 0:
        return []

    # Gets the graph of gmu with location nodes and edges weighted by distance
    map = get_graph()

    optimal_path = list(get_best_path(map, start_loc, classes[0].building.entrances()))
    # Get the optimal path from one class to the class immediately after
    for i in range(1, len(classes)):
        optimal_path.append(get_best_path(map, classes[i - 1], classes[i]))
    return optimal_path


def get_best_path(graph, start, end):
    """
    :param graph: Graph contains location nodes
    :param start: Starting location node
    :param end:   End location node
    :return:      shortest_path
    """
    # Contains shortest distances from each node
    distance_dic = {}
    # Contains predecessors of each node
    predecessor_dic = {}
    locations_not_visited = graph
    infinity = float('Inf')
    shortest_path = []
    # Go through each node and set its distance to infinity
    for current_location in locations_not_visited:
        distance_dic[current_location] = infinity

    # Inserting shortest distance of starting location as 0 obv.
    distance_dic[start] = 0
    # Iterate through each node in graph
    while locations_not_visited:
        smallest_node = None
        # Gets smallest node of all other nodes from starting location
        for current_node in locations_not_visited:
            if smallest_node is None:
                smallest_node = current_node
            elif distance_dic[current_node] < distance_dic[smallest_node]:
                smallest_node = current_node
        # Check all child nodes of smallest node with its weights
        # If weight is less than what is stored in distance_dic
        #   Then update weight and predecessor
        for childNode in graph[smallest_node]:
            weight = Location.dist(smallest_node, childNode)
            if weight + distance_dic[smallest_node] < distance_dic[childNode]:
                distance_dic[childNode] = weight + distance_dic[smallest_node]
                predecessor_dic[childNode] = smallest_node
        locations_not_visited.pop(smallest_node)
    #print(distance_dic)
    current_node = end
    while current_node != start:
        shortest_path.insert(0, current_node)
        current_node = predecessor_dic[current_node]

    shortest_path.insert(0, start)
    return shortest_path


if __name__ == '__main__':
    graph = get_graph()
    start = None
    end = None
    # print(graph)
    for currentNode in graph.keys():
        if currentNode.location_name == "JC1":
            start = currentNode
            # print("Start: ", start)
        if currentNode.location_name == "MT1":
            end = currentNode
            # print("End: ", end)

    distance = Location.dist(start , end)
    # print("Distance from Start to End: ", distance)
    shortest_path = get_best_path(graph, start, end)
    # print("Shortest Path: ",shortest_path)
    stud1 = Student.get('cguerra5@masonlive.gmu.edu')
    stud1.study_preference()
    for currentclass in stud1.all_classes():
        print()
        print(currentclass)
        print()
    #optimal_class_path = find_optimal_class_path(start, stud1.all_classes())
    #print(optimal_class_path)
    visualize_map(path=shortest_path)

