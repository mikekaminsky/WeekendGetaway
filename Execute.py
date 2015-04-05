#Execute.py
#Michael Kaminsky

import datetime
import PullFlights
from db.Connection import *

# Inputs
#destination_list = ["AUS", "PHX", "LAX"]
destination_list = ["AUS"]
origin_list = ["NYC"]

#departure_dates = ["2015-05-01", "2015-05-08"]
departure_dates = ["2015-05-01"]

# Generate return dates for our departure dates list
date_list = []
for date in departure_dates:
  return_date = str(datetime.datetime.strptime(date,"%Y-%m-%d").date() + datetime.timedelta(days = 3))
  date_pair = (date, return_date)
  date_list.append(date_pair)

pf = PullFlights.PullFlights(session, origin_list, destination_list, date_list, api_key)
pf.UpdateData()
