#Execute.py
#Michael Kaminsky

import datetime
import PullFlights
import psycopg2
import os

execfile("secrets.py") # declares api_key variable

db_name = 'weekendgetaway'
username = os.environ['USER']
host = 'localhost'
db_password = ''


con = psycopg2.connect(dbname=db_name, user=username, host=host, password = db_password)

# Inputs
destination_list = ["AUS", "PHX", "LAX"]
origin_list = ["NYC"]

departure_dates = ["2015-05-01", "2015-05-08"]

# Generate return dates for our departure dates list
date_list = []
for date in departure_dates:
  return_date = str(datetime.datetime.strptime(date,"%Y-%m-%d").date() + datetime.timedelta(days = 3))
  date_pair = (date, return_date)
  date_list.append(date_pair)

pf = PullFlights.PullFlights(con, origin_list, destination_list, date_list, api_key)
pf.UpdateData()
