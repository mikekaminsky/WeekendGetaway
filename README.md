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
* [ ] Switch to using SQL Alchemy ORM for easier maintenance and migrations
* [ ] Use separate price and currency fields in model
* [ ] Deploy app to heroku
* [ ] Set up payments for API use
* [ ] Loop over next 10 weekends
* [ ] Loop over top 100 airports
