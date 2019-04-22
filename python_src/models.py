import geopy.distance

from datetime import datetime
from python_src import db
from flask_login import UserMixin


class Student(db.Model, UserMixin):
    __tablename__ = 'student'
    email = db.Column(db.String(50), primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)

    def todays_schedule(self):
        today = datetime.today()
        year = str(today.year)

        if today.month in [1, 2, 3, 4, 5]:
            semester = 'spring'
        elif today.month in [8, 9, 10, 11, 12]:
            semester = 'fall'
        else:
            semester = 'summer'

        day = today.weekday()
        if day in [5, 6]:
            return []
        return self.get_weekly_schedule(year, semester)[day]

    def current_weekly_schedule(self):
        today = datetime.today()
        year = str(today.year)

        if today.month in [1, 2, 3, 4, 5]:
            semester = 'spring'
        elif today.month in [8, 9, 10, 11, 12]:
            semester = 'fall'
        else:
            semester = 'summer'

        return self.get_weekly_schedule(year, semester)

    def get_weekly_schedule(self, year, semester):
        """Gets the weekly
        :param year: The year of the class as a string.
        :type year: str
        :param semester: The semester of the class, either 'fall', 'spring', or
                         'summer'
        :type semester: str
        :return: A five element list where index 0 contains a list of classes
                 that occur on Monday, 1 a list of classes that occur on
                 Tuesday etc. Each list is sorted by start time.
        :rtype: List[List[ClassTime]]
        """
        classes = ClassTime.query.filter_by(student_email=self.email,
                                            semester=semester.lower(),
                                            year=year).all()

        # Initialize the list of classes for each weekday
        classes_by_day = [[] for _ in range(5)]
        if len(classes) == 0:
            return classes_by_day

        # Append each class to its corresponding weekday(s)
        days = {d: i for i, d in enumerate('MTWRF')}
        for c in classes:
            # Get the indices of the days a class occurs on
            class_days = []
            for week_day in c.week_days:
                class_days.append(days[week_day])

            # Add the class to each day it occurs on
            for day_idx in class_days:
                classes_by_day[day_idx].append(c)

        # Sort each list by start time
        for c in classes_by_day:
            c.sort(key=lambda _: _.start_time)

        return classes_by_day

    def update_password(self, new_password):
        self.password = new_password
        db.session.commit()

    def delete_class(self, year, semester, class_name):
        ClassTime.query.filter_by(
            student_email=self.email, year=year, semester=semester,
            class_name=class_name).delete()
        db.session.commit()

    def delete_all_classes(self):
        for c in self.all_classes():
            self.delete_class(year=c.year, semester=c.semester,
                              class_name=c.class_name)
        db.session.commit()

    def delete_study_preference(self):
        StudyTime.query.filter_by(student_email=self.email).delete()
        db.session.commit()

    def delete_meal_preference(self):
        MealTime.query.filter_by(student_email=self.email).delete()
        db.session.commit()

    def reset_account(self):
        self.delete_all_classes()
        self.delete_study_preference()
        self.delete_meal_preference()

    def all_classes(self):
        """Returns all the classes associated with a student
        :rtype: List[ClassTime]
        """
        return ClassTime.query.filter_by(student_email=self.email).all()

    def add_class(self, class_name, year, semester, building, start_time, end_time,
                  week_days):
        """Adds a class to a users account."""
        ClassTime.add(student_email=self.email, class_name=class_name,
                      year=year, semester=semester, building=building,
                      start_time=start_time, end_time=end_time,
                      week_days=week_days)

    def study_preference(self):
        """Returns a students study preference as a StudyTime object"""
        return StudyTime.get(self.email)

    def meal_preference(self):
        """Returns a students meal preference as a StudyTime object"""
        return MealTime.get(self.email)

    @staticmethod
    def get(student_email):
        """Gets the student table entry associated with an email"""
        return Student.query.filter_by(email=student_email).first()

    @staticmethod
    def print_all():
        """Prints every entry in the table"""
        header = '{:50} | {:25} | {:25} | {:25} |'
        print(header.format('email', 'first_name', 'last_name', 'password'))
        [print(_) for _ in Student.query.all()]

    def get_id(self):
        return self.email

    def __str__(self):
        # Don't print the user's password when __repr__ is called
        p = ''
        for _ in range(len(self.password)):
            p += '*'
        rep = '{:50} | {:25} | {:25} | {:25} |'
        return rep.format(self.email, self.first_name, self.last_name, p)

    def __repr__(self):
        # Don't print the user's password when __repr__ is called
        p = ''
        for _ in range(len(self.password)):
            p += '*'

        rep = 'Student(email={}, first_name={}, last_name={}, password={})'
        return rep.format(self.email, self.first_name, self.last_name, p)


class Building(db.Model):
    __tablename__ = 'building'
    building_name = db.Column(db.String(50), primary_key=True)
    is_study_location = db.Column(db.Boolean, nullable=False)

    def entrances(self):
        return Location.query.filter_by(building=self.building_name).all()

    def restaurants(self):
        return Restaurant.query.filter_by(building=self.building_name).all()

    @staticmethod
    def get(building_name):
        """Gets the building table entry associated with a building name"""
        return Building.query.filter_by(building_name=building_name).first()

    @staticmethod
    def print_all():
        """Prints every entry in the table"""
        header = '{:50} | {:20} | '
        print(header.format('building_name', 'is_study_location'))
        [print(_) for _ in Building.query.all()]

    def __str__(self):
        rep = '{:50} | {:20} | '
        return rep.format(self.building_name, self.is_study_location)

    def __repr__(self):
        return 'Building({})'.format(self.building_name)


class Location(db.Model):
    __tablename__ = 'location'
    location_name = db.Column(db.String(25), primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    building = db.Column(db.String(50), primary_key=True)
    is_parking_lot = db.Column(db.Boolean, nullable=False)

    def coords(self):
        """Gets the coordinates of a location
        :return: A two tuple (longitude, latitude)
        """
        return self.longitude, self.latitude

    @staticmethod
    def dist(loc1, loc2, unit='ft'):
        """Gets the distance between two locations in some unit.
        :param loc1: The initial location.
        :type loc1: Location
        :param loc2: The destination location.
        :type loc2: Location
        :param unit: The unit of measure either feet ('ft') or meters ('m'),
                     defaults to feet.
        :type unit: str
        :return: The distance from loc1 to loc2 in the unit.
        :raises: ValueError when an invalid unit is input
        """
        if unit == 'ft' or unit == 'feet':
            return geopy.distance.vincenty(loc1.coords(), loc2.coords()).ft
        if unit == 'm' or unit == 'meter':
            return geopy.distance.vincenty(loc1.coords(), loc2.coords()).m
        else:
            raise ValueError('The unit must be either \'m\' or \'ft\'')

    @staticmethod
    def get(location_name):
        """Gets the location table entry associated with a location name"""
        return Location.query.filter_by(location_name=location_name).first()

    def __repr__(self):
        rep = ('Location(location_name={}, latitude={}, longitude={}, '
               + 'building = {}, is_parking_lot={})')
        return rep.format(self.location_name, self.latitude, self.longitude,
                          self.building, self.is_parking_lot)


class Edge(db.Model):
    __tablename__ = 'edge'
    location1 = db.Column(db.String(25), db.ForeignKey('location.location_name'),
                          primary_key=True)
    location2 = db.Column(db.String(25), db.ForeignKey('location.location_name'),
                          primary_key=True)
    is_active = db.Column(db.Boolean, nullable=False)

    def dist(self):
        """Gets the distance of the edge"""
        return Location.dist(self.location1, self.location2)

    def locations(self):
        """Gets the distance of the edge"""
        return self.location1, self.location2

    @staticmethod
    def get(location1, location2):
        """Gets the edge associated with two locations"""
        return Edge.query.filter_by(location1=location1,
                                    location2=location2).first()

    def __repr__(self):
        rep = 'Edge(location1={}, location2={}, is_active={})'
        return rep.format(self.location1, self.location2, self.is_active)


class Restaurant(db.Model):
    __tablename__ = 'resturant'
    building = db.Column(db.String(25), db.ForeignKey('building.building_name'),
                         primary_key=True)
    restaurant_name = db.Column(db.String(25), primary_key=True)

    @staticmethod
    def get(building, restaurant_name):
        """Gets the edge associated with two locations"""
        return Restaurant.query.filter_by(building=building,
                                          restaurant_name=restaurant_name).first()

    def __repr__(self):
        rep = 'Restaurant(building={}, restaurant_name={})'
        return rep.format(self.location, self.restaurant_name)


class ClassTime(db.Model):
    __tablename__ = 'class_time'
    student_email = db.Column(db.String(50), db.ForeignKey('student.email'),
                              primary_key=True)
    year = db.Column(db.String(4), primary_key=True)
    semester = db.Column(db.String(7), primary_key=True)
    class_name = db.Column(db.String(25), primary_key=True)
    building = db.Column(db.String(25), db.ForeignKey('building.building_name'))
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    week_days = db.Column(db.String(7))

    @staticmethod
    def get(student_email, year, semester, class_name):
        """Gets the class_time table entry associated with an email and class
        information"""
        return ClassTime.query.filter_by(student_email=student_email,
                                         year=year,
                                         semester=semester,
                                         class_name=class_name).first()

    @staticmethod
    def add(student_email, year, semester, class_name, building, start_time,
            end_time, week_days):
        """Adds an entry to the ClassTime table"""
        db.session.add(
            ClassTime(student_email=student_email, year=year, semester=semester,
                      class_name=class_name, building=building,
                      start_time=start_time, end_time=end_time, week_days=week_days))
        db.session.commit()

    def __repr__(self):
        rep = ('ClassTime(student_email={}, year={}, semester={}, '
               + 'class_name={}, building={}, start_time={}, '
               + 'end_time={}, week_days={})')
        return rep.format(self.student_email, self.year, self.semester,
                          self.class_name, self.building, self.start_time,
                          self.end_time, self.week_days)


class StudyTime(db.Model):
    __tablename__ = 'study_time'
    student_email = db.Column(db.String(50), db.ForeignKey('student.email'),
                              primary_key=True)
    weekly_hours = db.Column(db.Float, nullable=False)
    min_cont_hours = db.Column(db.Float, nullable=False)
    max_cont_hours = db.Column(db.Float, nullable=False)
    break_time_hours = db.Column(db.Float, nullable=False)
    earliest_time = db.Column(db.Time, nullable=False)
    latest_time = db.Column(db.Time, nullable=False)

    @staticmethod
    def get(student_email):
        """Gets the study_time table entry associated with an email"""
        return StudyTime.query.filter_by(student_email=student_email).first()

    @staticmethod
    def print_all():
        """Prints every entry in the table"""
        header = '{:50} | {:15} | {:15} | {:15} | {:15} | {:15} | {:15} |'
        print(header.format('student_email', 'weekly_hours', 'min_cont_hours',
                            'max_cont_hours', 'break_time_hours',
                            'earliest_time', 'latest_time'))
        [print(_) for _ in StudyTime.query.all()]

    def __str__(self):
        rep = '{:50} | {:15} | {:15} | {:15} | {:16} |     {}    |     {}    |'
        return rep.format(self.student_email, self.weekly_hours,
                          self.min_cont_hours, self.max_cont_hours,
                          self.break_time_hours, self.earliest_time,
                          self.latest_time)

    def __repr__(self):
        rep = ('StudyTime(student_email={}, weekly_hours={}, min_cont_hours={},'
               + ' max_cont_hours={}, break_time_hours={}, earliest_time={},'
               + ' latest_time={})')
        return rep.format(self.student_email, self.weekly_hours,
                          self.min_cont_hours, self.max_cont_hours,
                          self.break_time_hours, self.earliest_time,
                          self.latest_time)


class MealTime(db.Model):
    __tablename__ = 'meal_time'
    student_email = db.Column(db.String(50), db.ForeignKey('student.email'),
                              primary_key=True)
    daily_meal_num = db.Column(db.Integer, nullable=False)
    min_meal_hours = db.Column(db.Float, nullable=False)
    max_meal_hours = db.Column(db.Float, nullable=False)
    earliest_time = db.Column(db.Time, nullable=False)
    latest_time = db.Column(db.Time, nullable=False)

    def __str__(self):
        rep = '{:50} | {:15} | {:15} | {:15} |     {}    |     {}    |'
        return rep.format(self.student_email, self.daily_meal_num,
                          self.min_meal_hours, self.max_meal_hours,
                          self.earliest_time, self.latest_time)

    def __repr__(self):
        rep = ('MealTime(student_email={}, daily_meal_num={},'
               + ' min_meal_hours={}, max_meal_hours={}, earliest_time={},'
               + ' latest_time={})')
        return rep.format(self.student_email, self.daily_meal_num,
                          self.min_meal_hours, self.max_meal_hours,
                          self.earliest_time, self.latest_time)


if __name__ == '__main__':
    carlos = Student.get('cguerra5@masonlive.gmu.edu')
    for d in carlos.get_weekly_schedule(year='2018', semester='spring'):
        print(d)
    carlos.update_password('new_password')
    if ClassTime.get(student_email=carlos.email, class_name='CS333',
                     year='2019', semester='Spring') is None:
        carlos.add_class(class_name='CS333', year='2019', semester='Spring',
                         start_time='09:00:00', end_time='10:15:00',
                         building='Merten Hall', week_days='MWF')

    print(carlos.todays_schedule())

