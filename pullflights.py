#pullflights.py
#Michael Kaminsky

import json
import requests
import time
import psycopg2
import os

# Constants
url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
headers = {'content-type': 'application/json'}

class PullFlights(object):
    """
    Class to serve as a container for the flight data collector
    """

    def __init__(self, 
                 cur = None, 
                 origin_list = None, 
                 destination_list = None,
                 date_list = None, 
                 ):
        print "PullFlights object created"

        if cur is None:
          print "You must provide a database connection!"
          raise

        if origin_list is None:
          print "You must provide a list of originating airports!"
          raise

        if destination_list is None:
          print "You must provide a list of destination airports!"
          raise

        if date_list is None:
          print "You must provide a list of date_tuples for leave and return!"
          raise

        self.cur = cur
        self.origin_list = origin_list
        self.destination_list = destination_list
        self.date_list = date_list

    def make_header(self, origin_city, destination_city, departure_date, return_date):
        """
        Method for making API request paramater
        """

        params = {
          "request": {
            "slice": [
              {
                "origin": origin_city,
                "destination": destination_city,
                "date": departure_date
              },
              {
                "origin": destination_city,
                "destination": origin_city,
                "date": return_date
              }
            ],
            "passengers": {
              "adultCount": 1
            },
          }
        }
        return params

    def UpdateData(self):
        for origin_city in self.origin_list:
            for destination_city in self.destination_list:

              if destination_city == origin_city:
                continue

              for date_tuple in self.date_list:
                  departure_date = date_tuple[0]
                  return_date    = date_tuple[1]

                  print origin_city + destination_city + departure_date + return_date

                  params = self.make_header(origin_city, destination_city, departure_date, return_date)

                  date_time = time.strftime("%Y/%m/%d %H:%M:%S")
                  response = requests.post(url, data=json.dumps(params), headers=headers)
                  options = response.json()['trips']['tripOption']

                  # Check if row is already in the database
                  # If not, add it
                  cur.execute("""
                          SELECT id 
                          FROM trips 
                          WHERE 
                              origin_city = (%s) 
                              AND destination_city = (%s) 
                              AND departure_date = (%s)
                              AND return_date = (%s)""", (origin_city, destination_city, departure_date, return_date))
                  cur_id_tuple = cur.fetchall()
                  if len(cur_id_tuple) != 0:
                      cur_id = cur_id_tuple[0][0]
                  else:
                      cur.execute("""
                          INSERT INTO trips (origin_city, destination_city, departure_date, return_date) 
                          VALUES (%s, %s, %s, %s)
                          RETURNING id""", (origin_city, destination_city, departure_date, return_date))
                      cur_id = cur.fetchall()
                      cur_id = cur_id[0][0]

                  # Begin looping through options
                  for option in options:
                      total_cost = option['saleTotal']
                      cur.execute("""
                          INSERT INTO flights (trip_id, time_queried, price) 
                          VALUES (%s, %s, %s) returning id
                          """, (cur_id, date_time, total_cost))
                      flight_id = cur.fetchall()
                      flight_id = flight_id[0][0]
                      slicenum = 0
                      for eachslice in option['slice']: # Here is where we determine inbound vs. outbound slices.
                          slice_duration = eachslice['duration']
                          slicenum += 1
                          for segment in eachslice['segment']:
                              segment_travel_time = segment['duration']
                              carrier = segment['flight']['carrier']
                              number = segment['flight']['number']
                              for leg in segment['leg']:
                                  leg_origin = leg['origin']
                                  leg_departure = leg['departureTime']
                                  leg_destination = leg['destination']
                                  leg_arrival = leg['arrivalTime']
                                  leg_duration = leg['duration']
                                  cur.execute("""
                                      INSERT INTO legs (slice, flight_id, carrier, flight_number, origin, departure_time, destination, arrival_time, duration, slice_duration) 
                                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                      RETURNING id""", (slicenum, flight_id, carrier, number, leg_origin, leg_departure, leg_destination, leg_arrival, leg_duration, slice_duration))
                                  con.commit()
