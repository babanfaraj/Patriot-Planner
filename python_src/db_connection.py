import pymysql
pymysql.install_as_MySQLdb()

from sqlalchemy import create_engine
from sqlalchemy import Column, Float, Boolean, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select


Base = declarative_base()


class Location(Base):
    __tablename__ = 'location'
    location_name = Column(String(25), primary_key=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    is_active = Column(Boolean, nullable=False)
    is_study_location = Column(Boolean, nullable=False)
    is_parking_lot = Column(Boolean, nullable=False)

    def __repr__(self):
        msg = 'Location({}, {}, {}, {}, {}, {})'
        return msg.format(self.location_name, self.latitude, self.longitude,
                          self.is_active, self.is_study_location,
                          self.is_parking_lot)


with open('db_login.txt') as f:
    db = f.readline().replace('\n', '')
    engine = create_engine(db)
    conn = engine.connect()
    location = Location()

    print(location)
    s = select([location])
    print(conn.execute(s))


