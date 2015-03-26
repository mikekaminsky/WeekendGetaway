#pullflights.py
#Michael Kaminsky

import json
import requests
import time
import datetime
import psycopg2
import os

#Database
db_url = 'weekendgetaway'
username = os.environ['USER']
host = 'localhost'
con = psycopg2.connect(dbname=db_url, user=username, host=host)
cur = con.cursor()
execfile("secrets.py") # declares api_key variable

# Constants
url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
headers = {'content-type': 'application/json'}
#airport_list = ["ATL", "PEK", "LHR", "HND", "ORD"]
airport_list = ["ORD"]
origin_city = "NYC"
departure_date = "2015-03-27"
return_date = str(datetime.datetime.strptime(departure_date,"%Y-%m-%d").date() + datetime.timedelta(days = 3))

for destination_city in airport_list:
    print origin_city
    print destination_city

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

    date_time = time.strftime("%Y/%m/%d %H:%M:%S")
    response = requests.post(url, data=json.dumps(params), headers=headers)
    options = response.json()['trips']['tripOption']

    #Check if row is already in the database
    #If not, add it
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
