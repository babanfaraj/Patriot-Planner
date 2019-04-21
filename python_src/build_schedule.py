from python_src.models import *
from python_src.db_connection import *
from python_src.path_finding import get_best_path
import datetime
import math

"""
Returns all the study times for a given week
First dimension of array indicates the day of the week
Second dimension indicates study block in a given day
"""


def build_schedule(email, semester, year):
    cur_student = Student.get(email)
    #weekly_schedule = [[], [], [], [], []]
    if cur_student is None:
      print('No associated email')
      return 'No associated email'

    weekly_schedule = cur_student.get_weekly_schedule(year, semester)
   # print(weekly_schedule)
 #   student_classes = cur_student.all_classes()
    #filter_by_semester(student_classes, semester, year)
    #set_classes(weekly_schedule, student_classes)

 #   print(cur_student.study_preference())

    hours_left = cur_student.study_preference().weekly_hours
    min_cont_hours = cur_student.study_preference().min_cont_hours
    max_cont_hours = cur_student.study_preference().max_cont_hours
    break_time_hours = cur_student.study_preference().break_time_hours
    earliest_datetime = cur_student.study_preference().earliest_time
    latest_datetime = cur_student.study_preference().latest_time
    earliest_time = earliest_datetime.hour + earliest_datetime.minute/60.0
    latest_time = latest_datetime.hour + latest_datetime.minute/60.0
    earliest_time = 9.5
   #git  print(weekly_schedule)
    unavailable_times = find_unavailable_times(weekly_schedule, earliest_time, latest_time)

#    print(unavailable_times)

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

  #  print(study_times)
    study_times_datetime = [[], [], [], [], []]
    day_num = 0
    for _day in study_times:
      for session in _day:
        start_hour = int(session[0])
        start_minute = round((session[0] - start_hour) * 60.0)
        end_hour = int(session[1])
        end_minute = round((session[1] - end_hour) * 60.0)
        start_time = datetime.time(start_hour, start_minute)
        end_time = datetime.time(end_hour, end_minute)
        study_times_datetime[day_num].append((start_time, end_time))
      day_num+=1

    map_building_to_study_time(weekly_schedule, study_times)
 #   print(study_times_datetime)
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

def remove_overlapping_unavailable(unavailable_times):
    i = 0
    k = 0
    while i < len(unavailable_times):
      while k < len(unavailable_times[i])-1:
        if unavailable_times[i][k][1] > unavailable_times[i][k+1][1]:
          del unavailable_times[i][k+1]
        else:
          k+=1
      i+=1
    return unavailable_times



#finds all unavailable times in a week
def find_unavailable_times(weekly_schedule, earliest_time, latest_time):
    unavailable_times = [[], [], [], [], []]
    i = 0
    for day in weekly_schedule:
      unavailable_times[i].append((0, earliest_time))
      for _class in day:
        start_time = _class.start_time.hour + _class.start_time.minute/60.0
        end_time = _class.end_time.hour + _class.end_time.minute/60.0
        unavailable_times[i].append((start_time, end_time))
      unavailable_times[i].append((latest_time, 24))
      i+=1

    unavailable_times = remove_overlapping_unavailable(unavailable_times)
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


def map_building_to_study_time(weekly_schedule, study_times):
  #  print(weekly_schedule)
   # print(study_times)
    study_locations = [[], [], [], [], []]
    start_end_buildings = [[], [], [], [], []]
    for i in range(len(study_times)):
        for k in range(len(study_times[i])):
            start_end_buildings[i].append(find_classroom_before_after(weekly_schedule[i], study_times[i][k]))


   # print(start_end_buildings)
    for i in range(len(start_end_buildings)):
        for k in range(len(start_end_buildings[i])):
            if start_end_buildings[i][k][0].is_study_location:
                study_locations[i].append(start_end_buildings[i][k][0])
            elif start_end_buildings[i][k][1].is_study_location:
                study_locations[i].append(start_end_buildings[i][k][1])
            else:
                spot_on_path = find_study_spot_on_path(start_end_buildings[i][k][0], start_end_buildings[i][k][1])
                if spot_on_path[0]:
                    study_locations[i].append(spot_on_path[1])
                else:
                    bisect_path(start_end_buildings[i][k][0], start_end_buildings[i][k][1])

    print(study_locations)
    return 0


def bisect_path(start_building, end_building):
    start_locations = start_building.entrances()
    end_locations = end_building.entrances()
    graph = get_graph()

    min_path_weight = math.inf
    for i in range(len(start_locations)):
        for k in range(len(end_locations)):
            temp_path = get_best_path(graph, start_locations[i], end_locations[k])
            if temp_path[1] < min_path_weight:
                best_path = temp_path[0]

    middle_location = best_path[round(len(best_path)/2)]

    all_buildings = Building.query.all()
    for building in all_buildings

    print(middle_location)



def find_study_spot_on_path(start_building, end_building):
    start_locations = start_building.entrances()
    end_locations = end_building.entrances()
    graph = get_graph()
    for i in range(len(start_locations)):
        for k in range((len(end_locations))):
            path = get_best_path(graph, start_locations[i], end_locations[k])
            for l in range(len(path)):
                loc_building = Building.get(path[0][i].building)
                if loc_building and loc_building.is_study_location:
                    print(loc_building)
                    return True, loc_building
    return False, ''

def find_classroom_before_after(daily_schedule, single_study_time):
    all_buildings = Building.query.all()
    """If the user has no classes, they are placed in the JC"""
    #print(daily_schedule)
    if len(daily_schedule) == 0:
        return all_buildings[9], all_buildings[9]

    start_time = single_study_time[0]
    end_time = single_study_time[1]
   # print(start_time, end_time)
    class_start_times = []
    class_end_times = []
    for i in range(len(daily_schedule)):
        class_start_times.append(daily_schedule[i].start_time.hour + daily_schedule[i].start_time.minute /60.0)
        class_end_times.append(daily_schedule[i].end_time.hour + daily_schedule[i].end_time.minute / 60.0)

    if start_time > class_end_times[len(class_end_times)-1]:
        return Building.get(daily_schedule[len(daily_schedule)-1].building), Building.get(daily_schedule[len(daily_schedule) - 1].building)
    if end_time < class_start_times[0]:
        return Building.get(daily_schedule[0].building), Building.get(daily_schedule[0].building)

    class_before = Building.get(daily_schedule[find_closest_value(start_time, class_end_times)].building)
    class_after = Building.get(daily_schedule[find_closest_value(end_time, class_start_times)].building)
    #print(class_start_times)
    #print(class_end_times)
    #print(class_before, class_after)
    return class_before, class_after


def find_closest_value(value, _list):
    closest_distance = math.inf
    index = -1
    for i in range(len(_list)):
        if abs(value - _list[i]) < closest_distance:
            closest_distance = abs(value - _list[i])
            index = i
    return index
build_schedule("cguerra5@masonlive.gmu.edu", "spring", '2018')
