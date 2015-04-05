from db.models import *
from db.Connection import *

Base.metadata.drop_all(engine) 
Base.metadata.create_all(engine) 
