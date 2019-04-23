from python_src.models import Student
from python_src import db


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


def create_student(student_info, classes=None, study_preference=None):
    db.session.add(student_info)
    db.session.commit()
    if classes is not None:
        for c in classes:
            db.session.add(c)
    if study_preference is not None:
        db.session.add(study_preference)
    if study_preference is not None or classes is not None:
        db.session.commit()


