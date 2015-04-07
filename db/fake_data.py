# Generate some fake data for database
from db.models import *
from db.Connection import *
import datetime

usercheck = raw_input('THIS WILL DESTROY YOUR DATABASE AND FILL IT WITH FAKE DATA. Type "yes" if you are sure you want to continue:')

if usercheck != 'yes':
  print("That was a close one! Don't do that again")
else:
  #Clear old data
  execfile("db/DBDestroy.py")

  date_time = datetime.datetime.now()

  session.add_all([
      Origin(origin = 'NYC'),
      Destination(destination = 'AUS'),
      Departure(departure_date = '2015-05-01'),
      ])

  for i in range(1, 7):

    newtrip = Trip(origin = 'NYC', destination = 'AUS', departure_date = '2015-05-0'+str(i), return_date = '2015-05-0'+str(i+2))

    newjourney = Journey(time_queried = date_time, price = 100.00, currency = 'USD')

    flight1 = Flight(duration = 60, outgoing = True)
    leg1 = Leg(carrier = "XX", flight_number = 102, origin = "NYC", destination = "AUS", departure_time = date_time + datetime.timedelta(hours=3),
        arrival_time = date_time + datetime.timedelta(hours=4), duration = 800)
    flight1.legs.append(leg1)


    flight2 = Flight(duration = 70, outgoing = False)
    leg2 = Leg(carrier = "XX", flight_number = 102, origin = "NYC", destination = "AUS", departure_time = date_time + datetime.timedelta(hours=3),
        arrival_time = date_time + datetime.timedelta(hours=4), duration = 800)
    flight2.legs.append(leg2)

    newjourney.flights.append(flight1)
    newjourney.flights.append(flight2)

    newtrip.journeys.append(newjourney)

    session.add_all([
        newtrip
        ])

    session.commit()

