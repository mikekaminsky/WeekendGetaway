ALTER TABLE journeys
DROP CONSTRAINT journeys_trip_id_fkey,
ADD CONSTRAINT journeys_trip_id_fkey
   FOREIGN KEY (trip_id)
   REFERENCES trips(id)
   ON DELETE CASCADE;

ALTER TABLE flights
DROP CONSTRAINT flights_journey_id_fkey,
ADD CONSTRAINT flights_journey_id_fkey
   FOREIGN KEY (journey_id)
   REFERENCES journeys(id)
   ON DELETE CASCADE;

ALTER TABLE legs
DROP CONSTRAINT legs_flight_id_fkey,
ADD CONSTRAINT legs_flight_id_fkey
   FOREIGN KEY (flight_id)
   REFERENCES flights(id)
   ON DELETE CASCADE;
