#pullflights.py
#Michael Kaminsky

import json
import requests
import time
import re
import os
from db.models import *
from db.Connection import *
from sqlalchemy.orm.exc import NoResultFound

class PullFlights(object):
    """
    Class to serve as a container for the flight data collector
    """

    def __init__(self, 
                 session = None, 
                 origin_list = None, 
                 destination_list = None,
                 date_list = None, 
                 api_key = None
                 ):

        if session is None:
          print "You must provide a database session!"
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

        if api_key is None:
          print "You must provide an API key!"
          raise

        self.session = session
        self.origin_list = origin_list
        self.destination_list = destination_list
        self.date_list = date_list

        self.url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
        self.headers = {'content-type': 'application/json'}

        print "PullFlights object created"

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

                  # Check if row is already in the database
                  # If not, create a new object
                  try:
                    existing = self.session.query(Trip).filter_by(
                         origin = origin_city
                        ,destination = destination_city
                        ,departure_date = departure_date
                        ,return_date = return_date
                        ).one()
                    newtrip = existing
                  except NoResultFound:
                    newtrip = Trip(
                         origin = origin_city
                        ,destination = destination_city
                        ,departure_date =departure_date
                        ,return_date = return_date
                      )

                  response = requests.post(self.url, data=json.dumps(params), headers=self.headers)
                  date_time = time.strftime("%Y/%m/%d %H:%M:%S")
                  options = response.json()['trips']['tripOption']

                  # Begin looping through options
                  for option in options:
                      total_cost = re.sub('[^0-9\.]','',option['saleTotal'])
                      currency = re.sub('[\d\.]','',option['saleTotal'])
                      newjourney = Journey(time_queried = date_time, price = total_cost, currency = currency)
                      slicenum = 0
                      for eachslice in option['slice']: # Here is where we determine inbound vs. outbound slices.
                        outgoing = True if slicenum == 0 else False
                        newflight = Flight(duration = eachslice['duration'], outgoing = outgoing)
                        slicenum += 1
                        for segment in eachslice['segment']:
                            carrier = segment['flight']['carrier']
                            number = segment['flight']['number']
                            for leg in segment['leg']:
                                leg_origin = leg['origin']
                                leg_departure = leg['departureTime']
                                leg_destination = leg['destination']
                                leg_arrival = leg['arrivalTime']
                                leg_duration = leg['duration']
                                newleg = Leg(
                                     carrier = carrier
                                    ,flight_number = number
                                    ,origin = leg_origin
                                    ,destination = leg_destination
                                    ,departure_time = leg_departure
                                    ,arrival_time = leg_arrival
                                    ,duration = leg_duration
                                    )
                                newflight.legs.append(newleg)
                        newjourney.flights.append(newflight)
                      newtrip.journeys.append(newjourney)
                  session.add(newtrip)
                  self.session.commit()
