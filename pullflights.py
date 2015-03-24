#pullflights.py
#Michael Kaminsky

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
#    flights.date_queried
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

import json
import requests
import pandas
import time

date_time = time.strftime("%Y/%m/%d %H:%M:%S")

#airport_list = ["ATL", "PEK", "LHR", "HND", "ORD"]

execfile("secrets.py") # declares api_key variable

departure_date = "2015-09-19"
return_date = "2015-09-21"
origin_city = "NYC"
destination_city = "MDE"


url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
headers = {'content-type': 'application/json'}

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




for option in options:
    total_cost = option['saleTotal']
    print total_cost
    for eachslice in option['slice']:
        for segment in eachslice['segment']:
            segment_travel_time = segment['duration']
            carrier = segment['flight']['carrier']
            number = segment['flight']['number']
            leg = segment['leg'][0] # it looks like there's only one leg per segment?!
            leg_origin = leg['origin']
            leg_departure = leg['departureTime']
            leg_destination = leg['destination']
            leg_arrival = leg['arrivalTime']
            leg_duration = leg['duration']
            print carrier + number + " " + leg_origin + " -> " + leg_destination + " " + str(leg_duration) + " minutes"


