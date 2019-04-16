import geopy.distance

from python_src import db


class Building(db.Model):
    __tablename__ = 'building'
    building_name = db.Column(db.String(50), primary_key=True)
    is_study_location = db.Column(db.Boolean, nullable=False)

    def entrances(self):
        return Location.query.filter_as(building=self.building_name).all()

    def restaurants(self):
        return Restaurant.query.filter_as(building=self.building_name).all()

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

    def __repr__(self):
        rep = ('Location(location_name={}, latitude={}, longitude={}, '
               + 'building = {}, is_parking_lot={})')
        return rep.format(self.location_name, self.latitude, self.longitude,
                          self.building, self.is_parking_lot)


class Student(db.Model):
    __tablename__ = 'student'
    email = db.Column(db.String(50), primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)

    def all_classes(self):
        """Returns all the classes associated with a student
        :rtype: List[ClassTime]
        """
        return ClassTime.query.filter_as(email=self.email).all()

    def add_class(self, class_name, year, semester, location, start_time, end_time,
                  week_days):
        db.session.add(
            ClassTime(student_email=self.email, class_name=class_name,
                      year=year, semester=semester, location=location,
                      start_time=start_time, end_time=end_time,
                      week_days=week_days))
        db.session.commit()

    def __repr__(self):
        # Don't print the user's password when __repr__ is called
        p = ''
        for _ in range(len(self.password)):
            p += '*'

        rep = 'Student(email={}, first_name={}, last_name={}, password={})'
        return rep.format(self.email, self.first_name, self.last_name, p)


class Edge(db.Model):
    __tablename__ = 'edge'
    location1 = db.Column(db.String(25), db.ForeignKey('location.location_name'),
                          primary_key=True)
    location2 = db.Column(db.String(25), db.ForeignKey('location.location_name'),
                          primary_key=True)
    is_active = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        rep = 'Edge(location1={}, location2={}, is_active={})'
        return rep.format(self.location1, self.location2, self.is_active)


class Restaurant(db.Model):
    __tablename__ = 'resturant'
    building = db.Column(db.String(25), db.ForeignKey('building.building_name'),
                         primary_key=True)
    restaurant_name = db.Column(db.String(25), primary_key=True)

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

    def __repr__(self):
        rep = ('Schedule(student_email={}, year={}, semester={}, '
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

    def __repr__(self):
        rep = ('StudyTime(student_email={}, weekly_hours={}, min_cont_hours={},'
               + ' max_cont_hours={})')
        return rep.format(self.student_email, self.weekly_hours,
                          self.min_cont_hours, self.max_cont_hours)

