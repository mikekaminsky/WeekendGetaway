#Execute.py
#Michael Kaminsky
import datetime
import PullFlights
from db.Connection import *
from db.models import *

# Inputs
origin_list = []
origin_query = session.query(Origin).distinct(Origin.origin)
for x in origin_query:
    origin_list.append(x.origin )

destination_list  = []
destination_query = session.query(Destination).distinct(Destination.destination)
for x in destination_query:
    destination_list.append(x.destination)

departure_dates   = []
departure_query = session.query(Departure).distinct(Departure.departure_date)
for x in departure_query:
    departure_dates.append(x.departure_date)

# Generate return dates for our departure dates list
date_list = []
for date in departure_dates:
    return_date = str(date + datetime.timedelta(days = 3))
    date_pair = (date, return_date)
    date_list.append(date_pair)

pf = PullFlights.PullFlights(session, origin_list, destination_list, date_list, api_key)
pf.UpdateData()
