# Here's how to seed the database with an origin, a destination, and a date so that it can search for flights.
from db.models import *
from db.Connection import *

session.add_all([
    Origin(origin = 'NYC'),
    Destination(destination = 'AUS'),
    Departure(departure_date = '2015-05-01')
    ])

session.commit()

from sqlalchemy import text


