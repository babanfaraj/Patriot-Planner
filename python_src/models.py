import geopy.distance

from python_src import db


class Location(db.Model):
    __tablename__ = 'location'
    location_name = db.Column(db.String(25), primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    is_study_location = db.Column(db.Boolean, nullable=False)
    is_parking_lot = db.Column(db.Boolean, nullable=False)

    def coords(self):
        """Gets the coordinates of a location
        :return: A two tuple (longitude, latitude)
        """
        return self.longitude, self.latitude

    @staticmethod
    def dist(loc1, loc2, unit='ft'):
        """Gets the distance between two locations in feet.
        :param loc1: The initial location.
        :type loc1: Location
        :param loc2: The destination location.
        :type loc2: Location
        :return: The distance from loc1 to loc2 in feet.
        """
        if unit == 'ft':
            return geopy.distance.vincenty(loc1.coords(), loc2.coords()).ft

    def __repr__(self):
        rep = ('Location(location_name={}, latitude={}, longitude={}, '
               + 'is_active={}, is_study_location={}, is_parking_lot={})')
        return rep.format(self.location_name, self.latitude, self.longitude,
                          self.is_active, self.is_study_location,
                          self.is_parking_lot)


class Student(db.Model):
    __tablename__ = 'student'
    email = db.Column(db.String(50), primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)

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
        rep = 'Edge(location1={}, location2={})'
        return rep.format(self.location1, self.location2)

