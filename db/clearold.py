from db.models import *
from db.Connection import *
from sqlalchemy.orm.exc import NoResultFound
import datetime
from sqlalchemy import func

current_date = datetime.datetime.utcnow().date()


session.query(Journey).filter(func.DATE(Journey.time_queried) < current_date).delete(synchronize_session=False)

session.commit()
