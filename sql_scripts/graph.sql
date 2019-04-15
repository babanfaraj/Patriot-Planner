-- Inserts all the locations (nodes) in the graph that represents the locations
-- a student can travel to. It also inserts all the paths (edges) that a
-- student can take to get to each location

INSERT INTO location VALUES ('Planetary Hall 1', 38.829881, -77.306483, TRUE, FALSE);
INSERT INTO location VALUES ('Johnson Center 1', 38.829980, -77.306815, TRUE, FALSE);
INSERT INTO location VALUES ('Johnson Center 2', 38.830055, -77.306867, TRUE, FALSE);
INSERT INTO location VALUES ('Road 1', 38.830339, -77.307043, FALSE, FALSE);
INSERT INTO location VALUES ('Road 2', 38.830422, -77.306859, FALSE, FALSE);

INSERT INTO edge VALUES ('Johnson Center 1', 'Planetary Hall 1', TRUE);
INSERT INTO edge VALUES ('Johnson Center 1', 'Johnson Center 2', TRUE);
INSERT INTO edge VALUES ('Road 1', 'Johnson Center 2', TRUE);
INSERT INTO edge VALUES ('Road 1', 'Road 2', TRUE);

