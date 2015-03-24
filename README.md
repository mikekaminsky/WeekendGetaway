# WeekendGetaway
An application for finding cheap long-weekend flights

ToDo:
* [ ] Create general database connection class
*   [ ] Create local sqlite db for development
* [ ] Create setup method to create new DB with the following tables:
  * [ ] trips
  * [ ] flights
  * [ ] legs
* [ ] Create update method to add new trips, flights, and legs
* [ ] Create ruby app to display data from JSON
  * Not sure how to organize data?
    * [datatables](https://www.datatables.net/) is an option, but unclear how to display multiple legs.
    * Could custom right javascript for display (a la Kayak), but then sorting and filtering is a pain.
