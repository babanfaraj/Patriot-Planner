-- Inserts each building at Mason
-- VALUES format:
-- (building_name, is_study_location)
INSERT INTO building VALUES ('Johnson Center', TRUE);
INSERT INTO building VALUES ('Planetary Hall', TRUE);

-- Inserts all the locations (nodes) in the graph that represents the locations
-- a student can travel to.
-- VALUES format:
-- (location_name, longitude, latitude, building, is_parking_lot)
INSERT INTO location VALUES ('Planetary Hall 1', 38.829881, -77.306483, 'Planetary Hall', FALSE);
INSERT INTO location VALUES ('Johnson Center 1', 38.829980, -77.306815, 'Johnson Center', FALSE);
INSERT INTO location VALUES ('Johnson Center 2', 38.830055, -77.306867, 'Johnson Center', FALSE);
INSERT INTO location VALUES ('Road 1', 38.830339, -77.307043, NULL, FALSE);
INSERT INTO location VALUES ('Road 2', 38.830422, -77.306859, NULL, FALSE);

-- Inserts all the paths (edges) that a student can take to get to each location
-- VALUES format:
-- (location1, location2, is_active)
INSERT INTO edge VALUES ('Johnson Center 1', 'Planetary Hall 1', TRUE);
INSERT INTO edge VALUES ('Johnson Center 1', 'Johnson Center 2', TRUE);
INSERT INTO edge VALUES ('Road 1', 'Johnson Center 2', TRUE);
INSERT INTO edge VALUES ('Road 1', 'Road 2', TRUE);

