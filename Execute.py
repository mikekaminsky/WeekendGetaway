#Execute.py
#Michael Kaminsky

import datetime
execfile("secrets.py") # declares api_key variable

execfile("PullFlights.py")

db_url = 'weekendgetaway'
username = os.environ['USER']
host = 'localhost'
con = psycopg2.connect(dbname=db_url, user=username, host=host)
cur = con.cursor()

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


pf = PullFlights(cur, origin_list, destination_list, date_list)
pf.UpdateData()
