import webbrowser
import heapq

from python_src.models import Location, Building, Student
from python_src.viz import visualize_map


def display_path(url):
    webbrowser.open_new_tab(url)


def find_optimal_class_path(graph, classes, start_loc=None):
    """
    :param start_loc: A starting location.
    :param classes:
      A list of class locations in chronological order, Assume these classes all occur on the same day.
    """
    if classes is None or len(classes) < 2:
        return []

    # Lookup used to minimize the number of queries
    building_lookup = {c.class_name + c.start_time: Building.get(c.building) for c in classes}

    optimal_path = []
    if start_loc is not None:
        closest_pair = []
        min_dist = float('Inf')
        for end in building_lookup[classes[0].class_name + classes[0].start_time].entrances():
            dist = Location.dist(start_loc, end)
            if min_dist > dist:
                min_dist = dist
                closest_pair = [start_loc, end]
        optimal_path.append(get_best_path(graph, closest_pair[0], closest_pair[1])[0])

    # Get the optimal path from one class to the class immediately after
    # Checks multiple entrances for X class to find most optimal route
    for i in range(1, len(classes)):
        closest_pair = []
        min_dist = float('Inf')
        for start in building_lookup[classes[i - 1].class_name + classes[i - 1].start_time].entrances():
            for end in building_lookup[classes[i].class_name + classes[i].start_time].entrances():
                dist = Location.dist(start, end)
                if min_dist > dist:
                    min_dist = dist
                    closest_pair = [start, end]
        print(closest_pair)
        current_optimal_path = get_best_path(graph, closest_pair[0], closest_pair[1])
        optimal_path.append(current_optimal_path[0])
    return optimal_path


def get_best_path(graph, start_loc, end_loc):
    """ Uses A* search to find the best route from a start location to an end
    location
    :param graph: Graph contains location nodes
    :param start: Starting location node
    :param end:   End location node
    :return:      shortest_path
    """
    # Map each location name to its location object (to avoid database queries)
    loc_lookup = {l.location_name: l for l in graph.keys()}

    # Set the initial distances from the start node to each other node to inf
    dists = {l.location_name: float('Inf') for l in graph.keys()}
    dists[start_loc.location_name] = 0

    # A dictionary of each visited node's predecessor
    predecesors = {start_loc.location_name: None}

    # Initialize the min heap with the initial distances
    # For an actual distance, g, and a heuristic distance, h, each loc's
    # heap node is [h + g, g, loc.location_name]
    min_heap = []
    heapq.heappush(min_heap, [0, start_loc.location_name])
    visited = set()

    while min_heap is not None:
        cur_dist, cur_loc_name = heapq.heappop(min_heap)
        if cur_loc_name in visited:
            continue
        visited.add(cur_loc_name)

        # Exit if an end location has been hit
        if cur_loc_name == end_loc.location_name:
            shortest_path = [loc_lookup[cur_loc_name]]
            predecesor = predecesors[cur_loc_name]
            total_dist = dists[cur_loc_name]
            while predecesor is not None:
                shortest_path.insert(0, loc_lookup[predecesor])
                if loc_lookup[predecesor].building == start_loc.building:
                    break
                total_dist += dists[predecesor]
                predecesor = predecesors[predecesor]
            return shortest_path, total_dist

        # Insert/Update each neighbor
        cur_loc = loc_lookup[cur_loc_name]
        for neighbor_loc in graph[cur_loc]:
            neighbor_loc_name = neighbor_loc.location_name
            dist = dists[cur_loc_name] + Location.dist(cur_loc, neighbor_loc)
            if dist < dists[neighbor_loc_name]:
                dists[neighbor_loc_name] = dist

                heuristic_dist = Location.dist(neighbor_loc, end_loc)
                heapq.heappush(min_heap, [dist + heuristic_dist,
                                          neighbor_loc_name])
                predecesors[neighbor_loc_name] = cur_loc_name
    return [], 0


def path_to_gmaps_link(path):
    link = 'https://www.google.com/maps/dir'
    for loc in path:
        long, lat = loc.coords()
        link += '/' + str(lat) + ',+' + str(long)
    return link


if __name__ == '__main__':
    stud1 = Student.get('cguerra5@masonlive.gmu.edu')
    monday_classes = stud1.get_weekly_schedule(year=2019, semester='spring')[0]
    #find_optimal_class_path(monday_classes)
    optimal_class_path = find_optimal_class_path(monday_classes)
    '''
    for path in optimal_class_path:
        visualize_map(path=path)
       #display_path(path_to_gmaps_link(path))
    '''

