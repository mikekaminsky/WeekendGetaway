# WeekendGetaway
An application for finding cheap long-weekend flights

ToDo:
* [x] Create general database connection class
*   [x] Create local PostgreSQL db for development
* [x] Create setup method to create new DB with the following tables:
  * [x] trips
  * [x] flights
  * [x] legs
* [x] Create update method to add new trips, flights, and legs
* [x] Loop over legs in a segment (just in case there are multiple legs to a single flight)
* [x] Use segment number to determine outbound vs. inbound on return trips and add to data model
* [x] Collect duration by slice so it includes layover time and add to data model
* [x] Refactor pullflights into object with simpler methods -- remove some amount of nesting if possible
* [x] Create ruby app to display data from JSON
* [x] Switch to using SQL Alchemy ORM for easier maintenance and migrations
* [x] Split out slices into their own table
* [x] Use separate price and currency fields in model
* [x] Deploy app on heroku
* [x] Find better way of specifying database. Use [.env files](https://devcenter.heroku.com/articles/config-vars), use secrets.py, or see [this SO thread](http://stackoverflow.com/questions/5981508/share-database-between-2-apps-in-heroku) or [this Heroku post](https://blog.heroku.com/archives/2015/1/23/expanding_the_power_of_add_ons)
* [x] Use DB to manage which trips get queried
* [ ] Write script to dump data so Heroku doesn't drop the ban hammer.
* [ ] Load dump files into HDFS for future processing. See how to [article here](http://java.dzone.com/articles/how-set-multi-node-hadoop) and [amazon docs here](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-plan-file-systems.html) and this [hadoop wiki] (https://wiki.apache.org/hadoop/AmazonEC2). Put your hard hat on because this is some real devops shit.
* [ ] Try to figure out  a good system for doing migrations...[Try SQLAlchemy-Migrate](http://www.karoltomala.com/blog/?p=633) or [Alembic](http://alembic.readthedocs.org/en/latest/tutorial.html)
* [ ] Set up payments for API use
* [ ] Loop over next 10 weekends
* [ ] Loop over top 100 airports
