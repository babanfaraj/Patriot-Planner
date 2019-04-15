from python_src import db


class Location(db.Model):
    __tablename__ = 'location'
    location_name = db.Column(db.String(25), primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    is_study_location = db.Column(db.Boolean, nullable=False)
    is_parking_lot = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        msg = 'Location({}, {}, {}, {}, {}, {})'
        return msg.format(self.location_name, self.latitude, self.longitude,
                          self.is_active, self.is_study_location,
                          self.is_parking_lot)

