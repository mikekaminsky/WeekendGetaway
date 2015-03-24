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
#    flights.leg_id
#
#  legs
#    legs.id
#    legs.flight_id
#    legs.carrier
#    legs.flight_number
#    legs.origin
#    legs.departure_time
#    legs.destination
#    legs.arrival_time
#    legs.duration


class DBSetup(object):
    """
    Class to serve as a container for setting up the db for the flight data collector
    """
    def __init__(self, db_url = None, username = None, host = None):
        print "DBSetup object created"

        if db_url is None:
          db_url = 'postgres'
          print "Defaulting to local postgres"

        if username is None:
          username = os.environ['USER']
          print "Defaulting to local user " + username

        if host is None:
          host = 'localhost'
          print "Defaulting to localhost"

        self.db_url = db_url
        self.username = username
        self.host = host

    def DBDestroy(self):
        """
        Method to destroy existing database
        """
        con = psycopg2.connect(dbname=self.db_url, user=self.username, host=self.host)
        con.autocommit = True
        cur = con.cursor()
        cur.execute("DROP DATABASE IF EXISTS weekendgetaway;")
        con.commit()
        cur.close()
        con.close()

    def DBCreate(self):
        """
        Method for creating a new database
        """
        con = psycopg2.connect(dbname=self.db_url, user=self.username, host=self.host)
        con.autocommit = True
        cur = con.cursor()
        cur.execute(' CREATE DATABASE weekendgetaway; ')
        cur.execute(" SET timezone TO 'GMT' ;")
        cur.execute(' DROP TABLE IF EXISTS trips; ')
        cur.execute(' CREATE TABLE trips (id integer primary key, origin_city text, destination_city text, departure_date date, return_date date); ')
        cur.execute(' DROP TABLE IF EXISTS flights; ')
        cur.execute(' CREATE TABLE flights (id integer primary key, trip_id integer, time_queried timestamp, price numeric, leg_id integer); ')
        cur.execute(' DROP TABLE IF EXISTS legs; ')
        cur.execute(' CREATE TABLE legs (id integer primary key, flight_id integer, carrier text, flight_number integer, origin text, departure_time timestamp, destination text, arrival_time timestamp, duration integer); ')
        con.commit()
        cur.close()
        con.close()
