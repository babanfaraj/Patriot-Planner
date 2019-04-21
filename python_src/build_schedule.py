from python_src.models import *
from python_src.db_connection import *
import datetime

#Returns all the study times for a given week
#First dimension of array indicates the day of the week
#Second dimension indicates study block in a given day
def build_schedule(email, semester, year):
  cur_student = Student.get(email)
  weekly_schedule = [[], [], [], [], []]
  if cur_student is None:
    print('No associated email')
    return 'No associated email'

  student_classes = cur_student.all_classes()
  filter_by_semester(student_classes, semester, year)
  set_classes(weekly_schedule, student_classes)

#  print(cur_student.study_preference())

  hours_left = cur_student.study_preference().weekly_hours
  min_cont_hours = cur_student.study_preference().min_cont_hours
  max_cont_hours = cur_student.study_preference().max_cont_hours
  break_time_hours = cur_student.study_preference().break_time_hours

  for i in range(5):
    weekly_schedule[i] = sorted(weekly_schedule[i], key=sort_key)

 # print(weekly_schedule)
  unavailable_times = find_unavailable_times(weekly_schedule)
 # print(unavailable_times)

  day = 0
  study_times = [[], [], [], [], []]
  available_times = [[], [], [], [], []]

  while hours_left > 0 and max_cont_hours >= min_cont_hours:
    if day == 5:
      day = 0
    available_times[day] = find_available_times(unavailable_times[day], max_cont_hours, break_time_hours)
    chosen_time = find_study_time(available_times[day], max_cont_hours)
    hours_left -= max_cont_hours
    unavailable_times[day].append(chosen_time)
    unavailable_times[day] = sorted(unavailable_times[day], key=sort_unavailable)
    study_times[day].append(chosen_time)
    day += 1

    no_availabity_days = 0
    for daily_available in available_times:
      if len(daily_available) == 0:
        no_availabity_days += 1

    if no_availabity_days == 5:
      max_cont_hours -= 5.0/60.0

  print(study_times)
  study_times_datetime = [[], [], [], [], []]
  day_num = 0
  for day in study_times:
    for session in day:
      start_hour = int(session[0])
      start_minute = round((session[0] - start_hour) * 60.0)
      end_hour = int(session[1])
      end_minute = round((session[1] - end_hour) * 60.0)
      start_time = datetime.time(start_hour, start_minute)
      end_time = datetime.time(end_hour, end_minute)
      study_times_datetime[day_num].append((start_time, end_time))
    day_num+=1

  print(study_times_datetime)
  return study_times_datetime

#Finds an individual study time
def find_study_time(daily_available, study_length):
  possible_time = []
  for available_time in daily_available:
    possible_time.append((available_time[0], available_time[0] + study_length))
    possible_time.append((available_time[1] - study_length, available_time[1]))
 # print(possible_time)
  best_study_time = possible_time[round((len(possible_time)-1)/2)]
  return best_study_time


#Finds all available times in a day
def find_available_times(daily_unavailable, ideal_hours, break_time_hours):
  daily_available = []
  # Corrects for break_time_hours adjustment that happens in code below. No need for break time between start and end of day
  daily_unavailable[0] = (0, daily_unavailable[0][1] - break_time_hours)
  daily_unavailable[len(daily_unavailable) - 1] = (daily_unavailable[len(daily_unavailable) - 1][0] + break_time_hours, 24)
  #

  for i in range(len(daily_unavailable)-1):
    #print(daily_unavailable[i])
    if (daily_unavailable[i+1][0] - daily_unavailable[i][1] - (break_time_hours * 2)) >= ideal_hours:
      daily_available.append((daily_unavailable[i][1] + break_time_hours, daily_unavailable[i+1][0] - break_time_hours))

  return daily_available

#finds all unavailable times in a week
def find_unavailable_times(weekly_schedule):
  unavailable_times = [[], [], [], [], []]
  i = 0
  for day in weekly_schedule:
    unavailable_times[i].append((0, 9))
    for _class in day:
      start_time = _class.start_time.hour + _class.start_time.minute/60.0
      end_time = _class.end_time.hour + _class.end_time.minute/60.0
      unavailable_times[i].append((start_time, end_time))
    unavailable_times[i].append((21, 24))
    i+=1

  return unavailable_times


#Key for sorting class time (Remove soon)
def sort_key(class_time):
  return class_time.start_time

#Sorts uavailable times
def sort_unavailable(daily_unavailable):
  return daily_unavailable[0]


#Removes all classes that are not curently being taken
def filter_by_semester(student_classes, semester, year):
  i = 0
  while i < len(student_classes):
    if student_classes[i].year != year or student_classes[i].semester != semester:
      del student_classes[i]
    else:
      i += 1

#Assign classes to days of the week
def set_classes(weekly_schedule, student_classes):
  for _class in student_classes:
    if "M" in _class.week_days:
      weekly_schedule[0].append(_class)
    if "T" in _class.week_days:
      weekly_schedule[1].append(_class)
    if "W" in _class.week_days:
      weekly_schedule[2].append(_class)
    if "R" in _class.week_days:
      weekly_schedule[3].append(_class)
    if "F" in _class.week_days:
      weekly_schedule[4].append(_class)


#build_schedule("cguerra5@masonlive.gmu.edu", "Spring", '2018')
