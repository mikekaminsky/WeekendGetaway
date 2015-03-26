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
* [ ] Improve use of dates throughout
* [x] Loop over legs in a segment (just in case there are multiple legs to a single flight)
* [ ] Collect duration by slice so it includes layover time and add to data model
* [ ] Use segment number to determine outbound vs. inbound on return trips and add to data model
* [ ] Refactor pullflights into object with simpler methods -- remove some amount of nesting if possible
* [ ] Set up payments for API use
* [ ] Loop over next 10 weekends
* [ ] Loop over top 100 airports
* [ ] Create ruby app to display data from JSON
  * Not sure how to organize data?
    * [datatables](https://www.datatables.net/) is an option -- can use Kayak-style metadata to describe multiple-leg information.
