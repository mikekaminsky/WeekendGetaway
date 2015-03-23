# WeekendGetaway
An application for finding cheap long-weekend flights

1. Loop over [this list](https://www.world-airport-codes.com/world-top-30-airports.html) of airports
2. Loop over next 10 Weeknds (Friday-Monday trips)
3. Execute query against [QPX API](https://developers.google.com/qpx-express/v1/requests)
4. Save results:
  * date_queried
  * Dates of trip
  * from_airport
  * to_airport
  * flight_number_out
  * flight_number_back
  * total_price
5. Email results
  * Initially, just email 10 lowest prices with dates
  * After 1 month, look for price drops and send email with alerts for prices that are lower than historic median.

