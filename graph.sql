-- Inserts all the locations (nodes) in the graph that represents the locations
-- a student can travel to. It also inserts all the paths (edges) that a
-- student can take to get to each location

INSERT INTO locations VALUES ('Planetary Hall 1', 38.829881, -77.306483, TRUE, TRUE, FALSE);
INSERT INTO locations VALUES ('Johnson Center 1', 38.829980, -77.306815, TRUE, TRUE, FALSE);
INSERT INTO locations VALUES ('Johnson Center 2', 38.830055, -77.306867, TRUE, TRUE, FALSE);
INSERT INTO locations VALUES ('Road 1', 38.830339, -77.307043, TRUE, FALSE, FALSE);
INSERT INTO locations VALUES ('Road 2', 38.830422, -77.306859, TRUE, FALSE, FALSE);

INSERT INTO edges VALUES ('Johnson Center 1', 'Planetary Hall 1');
INSERT INTO edges VALUES ('Johnson Center 1', 'Johnson Center 2');
INSERT INTO edges VALUES ('Road 1', 'Johnson Center 2');
INSERT INTO edges VALUES ('Road 1', 'Road 2');

