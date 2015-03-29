import os
import psycopg2

# data model
#
#  trips
#    trips.id
#    trips.origin_city
#    trips.destination_city
#    trips.departure_date
#    trips.return_date
#
#  flights
#    flights.id
#    flights.trip_id
#    flights.time_queried
#    flights.price
#
#  legs
#    legs.id
#    legs.flight_id
#    legs.slice
#    legs.carrier
#    legs.flight_number
#    legs.origin
#    legs.departure_time
#    legs.destination
#    legs.arrival_time
#    legs.duration
#    legs.slice_duration

class DBSetup(object):
    """
    Class to serve as a container for setting up the db for the flight data collector
    """
    def __init__(self, con = None):

        if con is None:
          print "Must provide a connection!"
          raise

        con.autocommit = True
        self.con = con
        print "DBSetup object created"

    def DBDestroy(self):
        """
        Method to destroy existing database
        """
        cur = self.con.cursor()
        cur.execute(' DROP TABLE IF EXISTS trips; ')
        cur.execute(' DROP TABLE IF EXISTS flights; ')
        cur.execute(' DROP TABLE IF EXISTS legs; ')
        self.con.commit()
        cur.close()

    def DBCreate(self):
        """
        Method for creating a new database
        """
        cur = self.con.cursor()
        cur.execute(" SET timezone TO 'GMT' ;")
        cur.execute(' CREATE TABLE trips (id serial primary key, origin_city text, destination_city text, departure_date date, return_date date); ')
        cur.execute(' CREATE TABLE flights (id serial primary key, trip_id integer, time_queried timestamp, price text); ')
        cur.execute(' CREATE TABLE legs (id serial primary key, flight_id integer, slice integer, carrier text, flight_number integer, origin text, departure_time timestamp, destination text, arrival_time timestamp, duration integer, slice_duration integer); ')
        self.con.commit()
        cur.close()
