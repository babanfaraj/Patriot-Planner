from python_src.models import Location, Student, Edge, ClassTime, StudyTime
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
    return Student.query.filter_by(email=email,
                                   password=password).first() is not None


def create_student(student_info, classes, study_preference):
    db.session.add(student_info)
    db.session.commit()
    for c in classes:
        db.session.add(c)
    db.session.add(study_preference)
    db.session.commit()


if __name__ == '__main__':
    StudyTime.print_all()
    Student.print_all()
    stud = None
    if Student.get('alam12@masonlive.gmu.edu') is None:
        stud = Student(email='alam12@masonlive.gmu.edu', password='password',
                       first_name='Albert', last_name='Lam')
    classes = [
        ClassTime(student_email='alam12@masonlive.gmu.edu', year='2018',
                  semester='spring', class_name='CS110',
                  building='Art Building', start_time='09:00:00',
                  end_time='10:15:00', week_days='MWF'),
        ClassTime(student_email='alam12@masonlive.gmu.edu', year='2018',
                  semester='spring', class_name='ECE301',
                  building='Merten Hall', start_time='12:00:00',
                  end_time='13:15:00', week_days='MW'),
        ClassTime(student_email='alam12@masonlive.gmu.edu', year='2018',
                  semester='spring', class_name='ECE301-001',
                  building='College Hall', start_time='03:00:00',
                  end_time='05:45:00', week_days='MW'),
        ClassTime(student_email='alam12@masonlive.gmu.edu', year='2018',
                  semester='spring', class_name='ECE301-202',
                  building='College Hall', start_time='03:00:00',
                  end_time='05:45:00', week_days='F'),
        ClassTime(student_email='alam12@masonlive.gmu.edu', year='2018',
                  semester='spring', class_name='CS112',
                  building='Art Building', start_time='09:00:00',
                  end_time='10:15:00', week_days='TR'),
        ClassTime(student_email='alam12@masonlive.gmu.edu', year='2018',
                  semester='spring', class_name='MATH201',
                  building='Art Building', start_time='2:00:00',
                  end_time='3:15:00', week_days='TR')]

    pref = StudyTime(student_email='alam12@masonlive.gmu.edu',
                     weekly_hours=5, min_cont_hours=0.75, max_cont_hours=2,
                     break_time_hours=0.5, earliest_time='10:00:00',
                     latest_time='23:59:00')

    create_student(stud, classes, pref)

