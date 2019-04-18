from python_src.models import Location, Student, Edge
from python_src import db


def get_graph(include_inactive_edges=False):
    """Gets the graph of active paths on the mason campus.
    :return: An adjacency list of the active paths.
    :rtype: dict(Location: List[Location])
    """
    adjacency_list = {l: [] for l in Location.query.all()}

    for e in Edge.query.all():
        if include_inactive_edges or e.is_active:
            loc1 = Location.query.filter_by(location_name=e.location1).first()
            loc2 = Location.query.filter_by(location_name=e.location2).first()
            adjacency_list[loc1].append(loc2)
            adjacency_list[loc2].append(loc1)

    return adjacency_list


def are_valid_credentials(email, password):
    """Determines if a user exists in the database.
    :param email: The email address of the student.
    :type email: str
    :param password: The password of the student.
    :type password: str
    :return: Whether or not the user exists.
    :rtype: bool
    """
    return 0 < len(Student.query.filter_as(email=email,
                                           password=password).all())


def create_student(student_info, classes, study_preference):
    db.session.add(student_info)
    for c in classes:
        db.session.add(c)
    db.session.add(study_preference)
    db.session.commit()

