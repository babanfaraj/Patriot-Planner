from python_src.models import Location, Building
from python_src.db_connection import get_graph
from python_src.db_connection import *
from python_src.viz import visualize_map
import webbrowser

def display_path(url):
    webbrowser.open_new_tab(url)

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

    # Checks multiple entrances for the first class to find most optimal route
    least_distance = 9999999
    optimal_path = []
    current_best_path = None
    #print("First Class: ", classes[0])
    # building_entrances = Building.get(classes[0].building).entrances()
    for current_end_location in  Building.get(classes[0].building).entrances():
        current_best_path = get_best_path(map, start, current_end_location)
        if current_best_path[1] < least_distance:
            least_distance = current_best_path[1]
    optimal_path.append(current_best_path[0])

    # Get the optimal path from one class to the class immediately after
    # Checks multiple entrances for X class to find most optimal route
    for i in range(1, len(classes)):
        least_distance = 99999999
        current_optimal_path = None
        # Iterate through all entrances
        for current_start_location in Building.get(classes[i-1].building).entrances():
            for current_end_location in Building.get(classes[i].building).entrances():
                map = get_graph()
                current_best_path = get_best_path(map, current_start_location, current_end_location)
                if current_best_path[1] < least_distance:
                    least_distance = current_best_path[1]
                    current_optimal_path = current_best_path
        print(current_optimal_path)
        optimal_path.append(current_optimal_path[0])
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

    current_node = end
    while current_node != start:
            shortest_path.insert(0, current_node)
            current_node = predecessor_dic[current_node]
    shortest_path.insert(0, start)
    return shortest_path, distance_dic[end]


def path_to_gmaps_link(path):
    link = 'https://www.google.com/maps/dir'
    for loc in path:
        long, lat = loc.coords()
        link += '/' + str(lat) + ',+' + str(long)
    return link


if __name__ == '__main__':
    graph = get_graph()
    start = None
    end = None
    # print(graph)
    for currentNode in graph.keys():
        if currentNode.location_name == "MH1":
            start = currentNode
            # print("Start: ", start)
        if currentNode.location_name == "AB1":
            end = currentNode
            # print("End: ", end)

    #shortest_path = get_best_path(graph, start, end)
    #print("Shortest Path: ",shortest_path[1])
    stud1 = Student.get('cguerra5@masonlive.gmu.edu')
    stud1.study_preference()
    weekly_classes = stud1.get_weekly_schedule(year=2019, semester='spring')
    optimal_class_path = find_optimal_class_path(start, stud1.all_classes())
    print(optimal_class_path)
    #for loc in shortest_path:
    #    print(loc.location_name)
    #visualize_map(path=optimal_class_path[0])
    url = "http://www.google.com/"
    webbrowser.open_new_tab(url)

    #for path in optimal_class_path:
        #visualize_map(path=path)
        #display_path(path_to_gmaps_link(path))

