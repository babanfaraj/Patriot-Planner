from python_src.models import Location, Student, Edge


def get_graph():
    """Gets the graph of active paths on the mason campus
    :return:
    """
    adjacency_list = {l: [] for l in Location.query.all()}

    for e in Edge.query.all():
        if e.is_active:
            loc1 = Location.query.filter_by(location_name=e.location1).first()
            loc2 = Location.query.filter_by(location_name=e.location2).first()
            adjacency_list[loc1].append(loc2)
            adjacency_list[loc2].append(loc1)

    return adjacency_list

