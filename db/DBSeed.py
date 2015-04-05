from db.models import *
from db.Connection import *

session.add_all([
    Origin(origin = 'NYC'),
    Destination(destination = 'AUS'),
    Departure(departure_date = '2015-05-01')
    ])

session.commit()

from sqlalchemy import text


