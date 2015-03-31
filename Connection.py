import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

execfile("secrets.py") # declares api_key variable
db_name = 'weekendgetaway'
username = os.environ['USER']
host = 'localhost'
db_password = ''

def create_url(dialect = "postgres", driver = "", username = "", password = "", host = "", port = "", database = ""):
    #dialect+driver://username:password@host:port/database
    if driver != "":
        driver = "+" + driver
    if host != "":
        host = "@" + host
    if port != "":
        port = ":" + port
    if password != "":
        password = ":" + password
    if database != "":
        database = "/" + database
    return dialect + driver + "://" + username + password + host + port + database

conn_url = create_url(username = username, password = db_password, host = host, database = db_name)
engine = create_engine(conn_url, echo = True)

Session = sessionmaker(bind=engine)
session = Session()


