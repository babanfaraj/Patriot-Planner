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
    return 0 < len(Student.query.filter_by(email=email,
                                           password=password).all())


def create_student(student_info, classes, study_preference):
    """Adds a student to the database with their classes and study preferences.
    :param student_info: The student's login information.
    :type student_info: Student
    :param classes: The list of classes a student has.
    :type classes: List[ClassTime]
    :param study_preference: The student's study preferences.
    :type study_preference: StudyTime
    :return:
    """
    db.session.add(student_info)
    for c in classes:
        db.session.add(c)
    db.session.add(study_preference)
    db.session.commit()

def path_to_gmaps_link(path):
    link = 'https://www.google.com/maps/dir'
    for loc in path:
        long, lat = loc.coords()
        link += '/' + str(lat) + ',+' + str(long)
    return link



if __name__ == '__main__':
    print(are_valid_credentials('cguerra5@masonlive.gmu.edu', 'password'))

