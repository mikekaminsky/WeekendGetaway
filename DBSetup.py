from db.models import *
from Connection import *

Base.metadata.drop_all(engine) 
Base.metadata.create_all(engine) 
