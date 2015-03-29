#NewDB.py
#Michael Kaminsky

import DBSetup
import psycopg2

execfile("secrets.py") # declares api_key variable

con = psycopg2.connect(dbname=db_name, user=username, host=host, password = db_password)

db = DBSetup.DBSetup(con)
db.DBDestroy()
db.DBCreate()
