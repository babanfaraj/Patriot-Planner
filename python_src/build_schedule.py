from python_src.models import *
from python_src.db_connection import *


def build_schedule(email):
  cur_student = get_student(email)
  student_classes = cur_student.all_classes()
  print(Location.query.all())
  print("\n")
  print(student_classes)
  return email

build_schedule("hello")

