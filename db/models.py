#models.py
from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy import UniqueConstraint

Base = declarative_base()

class Trip(Base):
    __tablename__ = 'trips'
    id = Column(Integer, primary_key=True)
    origin = Column(String)
    destination = Column(String)
    departure_date = Column(Date)
    return_date = Column(Date)

    __table_args__ = (UniqueConstraint('origin', 'destination', 'departure_date', 'return_date',  name='_trip_uc'),
                     )
class Journey(Base):
    __tablename__ = 'journeys'
    id = Column(Integer, primary_key=True)
    trip_id = Column(Integer, ForeignKey('trips.id'))
    time_queried = Column(DateTime)
    price = Column(Numeric)
    currency = Column(String)

    trip = relationship("Trip", backref=backref('journeys', lazy='dynamic', order_by=id))


class Flight(Base):
    __tablename__ = 'flights'
    id = Column(Integer, primary_key=True)
    journey_id = Column(Integer, ForeignKey('journeys.id'))
    duration = Column(Integer)
    outgoing = Column(Boolean)

    journey = relationship("Journey", backref=backref('flights', lazy='dynamic', order_by=id))


class Leg(Base):
    __tablename__ = 'legs'
    id = Column(Integer, primary_key=True)
    flight_id = Column(Integer, ForeignKey('flights.id'))
    carrier = Column(String)
    flight_number = Column(Integer)
    origin = Column(String)
    destination = Column(String)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    duration = Column(Integer)

    flight = relationship("Flight", backref=backref('legs', lazy='dynamic', order_by=id))

