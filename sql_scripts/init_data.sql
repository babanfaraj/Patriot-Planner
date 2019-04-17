-- Inserts each building at Mason
-- VALUES format:
-- (building_name, is_study_location)
INSERT INTO building VALUES ('Johnson Center', TRUE);
INSERT INTO building VALUES ('Planetary Hall', TRUE);
INSERT INTO building VALUES ('Exploratory Hall', TRUE);
INSERT INTO building VALUES ('David King Hall', FALSE);
INSERT INTO building VALUES ('Sandy Creek Shuttle Stop', FALSE);
INSERT INTO building VALUES ('Southside Dining Hall', TRUE);
INSERT INTO building VALUES ('Tidewater', FALSE);
INSERT INTO building VALUES ('Enterprise Hall', TRUE);
INSERT INTO building VALUES ('Research Hall', TRUE);
INSERT INTO building VALUES ('Nguyen Engineering Building', TRUE);
INSERT INTO building VALUES ('Music/Theater Building', TRUE);
INSERT INTO building VALUES ('College Hall', TRUE);

-- Inserts all the locations (nodes) in the graph that represents the locations
-- a student can travel to.
-- VALUES format:
-- (location_name, longitude, latitude, building, is_parking_lot)
--
-- Also inserts all the paths (edges) that a student can take to get to each location
-- VALUES format:
-- (location1, location2, is_active)

-- Outline of the JC
INSERT INTO location VALUES ('JC1', 38.829980, -77.306815, 'Johnson Center', FALSE);
INSERT INTO location VALUES ('JC2', 38.830055, -77.306867, 'Johnson Center', FALSE);
INSERT INTO location VALUES ('JC3', 38.830641, -77.307253, 'Johnson Center', FALSE);
INSERT INTO location VALUES ('JC4', 38.830775, -77.307352, 'Johnson Center', FALSE);
INSERT INTO location VALUES ('JC5', 38.830458, -77.308149, 'Johnson Center', FALSE);
INSERT INTO location VALUES ('JC6', 38.830390, -77.308275, 'Johnson Center', FALSE);
INSERT INTO location VALUES ('JC7', 38.830375, -77.308287, 'Johnson Center', FALSE);
INSERT INTO location VALUES ('JC8', 38.829685, -77.307817, 'Johnson Center', FALSE);
INSERT INTO location VALUES ('JC9', 38.829369, -77.307018, 'Johnson Center', FALSE);
INSERT INTO location VALUES ('Rd1', 38.830338, -77.307052, NULL, FALSE);
INSERT INTO location VALUES ('Rd2', 38.829799, -77.306689, NULL, FALSE);
INSERT INTO location VALUES ('Rd3', 38.829569, -77.306530, NULL, FALSE);
INSERT INTO edge VALUES ('JC9', 'Rd3', TRUE);
INSERT INTO edge VALUES ('Rd3', 'Rd2', TRUE);
INSERT INTO edge VALUES ('Rd2', 'JC1', TRUE);
INSERT INTO edge VALUES ('JC1', 'JC2', TRUE);
INSERT INTO edge VALUES ('JC2', 'Rd1', TRUE);
INSERT INTO edge VALUES ('Rd1', 'JC3', TRUE);
INSERT INTO edge VALUES ('JC3', 'JC4', TRUE);
INSERT INTO edge VALUES ('JC4', 'JC5', TRUE);
INSERT INTO edge VALUES ('JC6', 'JC5', TRUE);
INSERT INTO edge VALUES ('JC6', 'JC7', TRUE);
INSERT INTO edge VALUES ('JC7', 'JC8', TRUE);

-- Outline of Planetary Hall
INSERT INTO location VALUES ('PH1', 38.829886, -77.306481, 'Planetary Hall', FALSE);
INSERT INTO location VALUES ('PH2', 38.830111, -77.306419, 'Planetary Hall', FALSE);
INSERT INTO location VALUES ('PH3', 38.830486, -77.306091, 'Planetary Hall', FALSE);
INSERT INTO location VALUES ('PH4', 38.830518, -77.306023, 'Planetary Hall', FALSE);
INSERT INTO location VALUES ('EH1', 38.829412, -77.305384, 'Exploratory Hall', FALSE);
INSERT INTO location VALUES ('EH2', 38.829439, -77.305847, 'Exploratory Hall', FALSE);
INSERT INTO location VALUES ('EH3', 38.829537, -77.305910, 'Exploratory Hall', FALSE);
INSERT INTO location VALUES ('EH4', 38.829675, -77.305832, 'Exploratory Hall', FALSE);
INSERT INTO location VALUES ('DK1', 38.830147, -77.306658, 'David King Hall', FALSE);
INSERT INTO location VALUES ('SC1', 38.829318, -77.305309, 'Sandy Creek Shuttle Stop', FALSE);
INSERT INTO location VALUES ('Rd4', 38.830219, -77.306506, NULL, FALSE);
INSERT INTO location VALUES ('Rd5', 38.830389, -77.306325, NULL, FALSE);
INSERT INTO location VALUES ('Rd6', 38.830481, -77.305754, NULL, FALSE);
INSERT INTO location VALUES ('Rd7', 38.830127, -77.305529, NULL, FALSE);
INSERT INTO location VALUES ('Rd8', 38.830085, -77.305383, NULL, FALSE);
INSERT INTO location VALUES ('Rd9', 38.829890, -77.305237, NULL, FALSE);
INSERT INTO location VALUES ('Rd10', 38.829482, -77.304960, NULL, FALSE);
INSERT INTO location VALUES ('Rd11', 38.829489, -77.306017, NULL, FALSE);
INSERT INTO location VALUES ('Rd12', 38.829529, -77.306249, NULL, FALSE);
INSERT INTO location VALUES ('Rd13', 38.829585, -77.306289, NULL, FALSE);
INSERT INTO location VALUES ('Rd14', 38.829650, -77.306329, NULL, FALSE);
INSERT INTO edge VALUES ('PH1', 'DK1', TRUE);
INSERT INTO edge VALUES ('DK1', 'Rd4', TRUE);
INSERT INTO edge VALUES ('Rd4', 'PH2', TRUE);
INSERT INTO edge VALUES ('PH2', 'Rd5', TRUE);
INSERT INTO edge VALUES ('Rd5', 'PH3', TRUE);
INSERT INTO edge VALUES ('PH3', 'PH4', TRUE);
INSERT INTO edge VALUES ('PH4', 'Rd6', TRUE);
INSERT INTO edge VALUES ('Rd6', 'Rd7', TRUE);
INSERT INTO edge VALUES ('Rd7', 'Rd8', TRUE);
INSERT INTO edge VALUES ('Rd8', 'Rd9', TRUE);
INSERT INTO edge VALUES ('Rd9', 'Rd10', TRUE);
INSERT INTO edge VALUES ('Rd10', 'SC1', TRUE);
INSERT INTO edge VALUES ('SC1', 'EH1', TRUE);
INSERT INTO edge VALUES ('SC1', 'EH2', TRUE);
INSERT INTO edge VALUES ('EH2', 'EH3', TRUE);
INSERT INTO edge VALUES ('EH2', 'EH4', TRUE);
INSERT INTO edge VALUES ('EH3', 'EH4', TRUE);
INSERT INTO edge VALUES ('EH3', 'Rd11', TRUE);
INSERT INTO edge VALUES ('Rd11', 'Rd12', TRUE);
INSERT INTO edge VALUES ('Rd12', 'Rd13', TRUE);
INSERT INTO edge VALUES ('Rd13', 'Rd14', TRUE);
INSERT INTO edge VALUES ('Rd14', 'PH1', TRUE);

-- Outline of David King Hall
INSERT INTO location VALUES ('DK2', 38.830722, -77.307041, 'David King Hall', FALSE);
INSERT INTO location VALUES ('DK3', 38.830762, -77.306955, 'David King Hall', FALSE);
INSERT INTO location VALUES ('Rd15', 38.830419, -77.306845, NULL, FALSE);
INSERT INTO location VALUES ('Rd16', 38.830966, -77.306902, NULL, FALSE);
INSERT INTO location VALUES ('Rd17', 38.830912, -77.307042, NULL, FALSE);
INSERT INTO location VALUES ('Rd18', 38.830863, -77.307140, NULL, FALSE);
INSERT INTO location VALUES ('Rd19', 38.831007, -77.306807, NULL, FALSE);
INSERT INTO edge VALUES ('DK1', 'DK2', TRUE);
INSERT INTO edge VALUES ('Rd15', 'DK2', TRUE);
INSERT INTO edge VALUES ('DK2', 'DK3', TRUE);
INSERT INTO edge VALUES ('DK3', 'Rd16', TRUE);
INSERT INTO edge VALUES ('DK3', 'Rd17', TRUE);
INSERT INTO edge VALUES ('Rd16', 'Rd17', TRUE);
INSERT INTO edge VALUES ('Rd17', 'Rd18', TRUE);
INSERT INTO edge VALUES ('DK2', 'Rd18', TRUE);
INSERT INTO edge VALUES ('Rd16', 'Rd19', TRUE);

-- Southside Outline
INSERT INTO location VALUES ('SS1', 38.831474, -77.305712, 'Southside Dining Hall', FALSE);
INSERT INTO location VALUES ('Rd20', 38.831407, -77.305856, NULL, FALSE);
INSERT INTO location VALUES ('Rd21', 38.831023, -77.305567, NULL, FALSE);
INSERT INTO location VALUES ('Rd22', 38.831648, -77.305327, NULL, FALSE);
INSERT INTO location VALUES ('Rd23', 38.831669, -77.305277, NULL, FALSE);
INSERT INTO location VALUES ('Rd24', 38.831904, -77.305509, NULL, FALSE);
INSERT INTO location VALUES ('Rd25', 38.831776, -77.305841, NULL, FALSE);
INSERT INTO location VALUES ('Rd26', 38.831869, -77.305918, NULL, FALSE);
INSERT INTO location VALUES ('Rd27', 38.831790, -77.306131, NULL, FALSE);
INSERT INTO location VALUES ('Rd28', 38.831585, -77.305991, NULL, FALSE);
INSERT INTO edge VALUES ('Rd20', 'SS1', TRUE);
INSERT INTO edge VALUES ('Rd20', 'Rd21', TRUE);
INSERT INTO edge VALUES ('SS1', 'Rd22', TRUE);
INSERT INTO edge VALUES ('Rd22', 'Rd23', TRUE);
INSERT INTO edge VALUES ('Rd22', 'Rd24', TRUE);
INSERT INTO edge VALUES ('Rd24', 'Rd25', TRUE);
INSERT INTO edge VALUES ('Rd25', 'Rd26', TRUE);
INSERT INTO edge VALUES ('Rd26', 'Rd27', TRUE);
INSERT INTO edge VALUES ('Rd27', 'Rd28', TRUE);
INSERT INTO edge VALUES ('Rd28', 'Rd20', TRUE);

-- Enterprise Hall Outline
INSERT INTO location VALUES ('ENT1', 38.829246, -77.306053, 'Enterprise Hall', FALSE);
INSERT INTO location VALUES ('Rd40', 38.829326, -77.306111, NULL, FALSE);
INSERT INTO location VALUES ('Rd41', 38.828792, -77.305731, NULL, FALSE);
INSERT INTO location VALUES ('Rd42', 38.828646, -77.306090, NULL, FALSE);
INSERT INTO location VALUES ('Rd43', 38.828552, -77.306285, NULL, FALSE);
INSERT INTO location VALUES ('Rd44', 38.828743, -77.306637, NULL, FALSE);
INSERT INTO location VALUES ('Rd45', 38.828839, -77.306725, NULL, FALSE);
INSERT INTO location VALUES ('Rd46', 38.828945, -77.306741, NULL, FALSE);
INSERT INTO location VALUES ('Rd47', 38.829066, -77.306723, NULL, FALSE);
INSERT INTO location VALUES ('Rd48', 38.829302, -77.306697, NULL, FALSE);
INSERT INTO location VALUES ('Rd49', 38.829334, -77.306626, NULL, FALSE);
INSERT INTO location VALUES ('Rd50', 38.829380, -77.306377, NULL, FALSE);
INSERT INTO edge VALUES ('Rd40', 'ENT1', TRUE);
INSERT INTO edge VALUES ('ENT1', 'Rd41', TRUE);
INSERT INTO edge VALUES ('Rd41', 'Rd42', TRUE);
INSERT INTO edge VALUES ('Rd42', 'Rd43', TRUE);
INSERT INTO edge VALUES ('Rd43', 'Rd44', TRUE);
INSERT INTO edge VALUES ('Rd44', 'Rd45', TRUE);
INSERT INTO edge VALUES ('Rd45', 'Rd46', TRUE);
INSERT INTO edge VALUES ('Rd46', 'Rd47', TRUE);
INSERT INTO edge VALUES ('Rd47', 'Rd48', TRUE);
INSERT INTO edge VALUES ('Rd48', 'Rd49', TRUE);
INSERT INTO edge VALUES ('Rd49', 'Rd50', TRUE);
INSERT INTO edge VALUES ('Rd50', 'Rd40', TRUE);

-- Research Hall Outline
INSERT INTO location VALUES ('RH1', 38.828202, -77.305266, 'Research Hall', FALSE);
INSERT INTO location VALUES ('RH2', 38.827917, -77.305007, 'Research Hall', FALSE);
INSERT INTO location VALUES ('RH3', 38.828312, -77.304929, 'Research Hall', FALSE);
INSERT INTO location VALUES ('Rd51', 38.827871, -77.305120, NULL, FALSE);
INSERT INTO location VALUES ('Rd52', 38.827991, -77.304837, NULL, FALSE);
INSERT INTO location VALUES ('Rd53', 38.828039, -77.304716, NULL, FALSE);
INSERT INTO location VALUES ('Rd54', 38.828956, -77.305350, NULL, FALSE);
INSERT INTO edge VALUES ('Rd41', 'RH1', TRUE);
INSERT INTO edge VALUES ('RH1', 'Rd51', TRUE);
INSERT INTO edge VALUES ('Rd51', 'RH2', TRUE);
INSERT INTO edge VALUES ('RH2', 'Rd52', TRUE);
INSERT INTO edge VALUES ('Rd52', 'Rd53', TRUE);
INSERT INTO edge VALUES ('Rd53', 'RH3', TRUE);
INSERT INTO edge VALUES ('RH3', 'Rd54', TRUE);
INSERT INTO edge VALUES ('Rd54', 'Rd41', TRUE);

-- Music and Theater Outline
INSERT INTO location VALUES ('MT1', 38.829063, -77.307811, 'Music/Theater Building', FALSE);
INSERT INTO location VALUES ('MT2', 38.829530, -77.308258, 'Music/Theater Building', FALSE);
INSERT INTO location VALUES ('CH1', 38.829043, -77.307856, 'College Hall', FALSE);
INSERT INTO edge VALUES ('JC9', 'MT1', TRUE);
INSERT INTO edge VALUES ('MT1', 'CH1', TRUE);

-- Nguyen Engineering Building
INSERT INTO location VALUES ('ENG1', 38.827790, -77.305061, 'Nguyen Engineering Building', FALSE);
INSERT INTO edge VALUES ('Rd51', 'ENG1', TRUE);

-- Building connections
INSERT INTO location VALUES ('Rd29', 38.831558, -77.306129, NULL, FALSE);
INSERT INTO location VALUES ('Rd30', 38.831612, -77.306496, NULL, FALSE);
INSERT INTO location VALUES ('Rd31', 38.831608, -77.306606, NULL, FALSE);
INSERT INTO location VALUES ('Rd32', 38.831493, -77.307062, NULL, FALSE);
INSERT INTO location VALUES ('Rd33', 38.831434, -77.307283, NULL, FALSE);
INSERT INTO location VALUES ('Rd34', 38.831183, -77.307232, NULL, FALSE);
INSERT INTO location VALUES ('Rd35', 38.831069, -77.307262, NULL, FALSE);
INSERT INTO location VALUES ('Rd36', 38.830952, -77.307465, NULL, FALSE);
INSERT INTO location VALUES ('Rd37', 38.830878, -77.307437, NULL, FALSE);
INSERT INTO location VALUES ('Rd38', 38.829441, -77.305993, NULL, FALSE);
INSERT INTO location VALUES ('Rd39', 38.829380, -77.306146, NULL, FALSE);
INSERT INTO location VALUES ('Rd55', 38.829241, -77.306937, NULL, FALSE);
INSERT INTO edge VALUES ('Rd14', 'Rd3', TRUE);
INSERT INTO edge VALUES ('PH1', 'Rd2', TRUE);
INSERT INTO edge VALUES ('PH1', 'JC1', TRUE);
INSERT INTO edge VALUES ('JC2', 'DK1', TRUE);
INSERT INTO edge VALUES ('JC1', 'DK1', TRUE);
INSERT INTO edge VALUES ('Rd15', 'Rd1', TRUE);
INSERT INTO edge VALUES ('JC3', 'DK2', TRUE);
INSERT INTO edge VALUES ('Rd19', 'Rd20', TRUE);
INSERT INTO edge VALUES ('Rd28', 'Rd29', TRUE);
INSERT INTO edge VALUES ('Rd29', 'Rd30', TRUE);
INSERT INTO edge VALUES ('Rd30', 'Rd31', TRUE);
INSERT INTO edge VALUES ('Rd31', 'Rd32', TRUE);
INSERT INTO edge VALUES ('Rd32', 'Rd33', TRUE);
INSERT INTO edge VALUES ('Rd33', 'Rd34', TRUE);
INSERT INTO edge VALUES ('Rd34', 'Rd35', TRUE);
INSERT INTO edge VALUES ('Rd35', 'Rd36', TRUE);
INSERT INTO edge VALUES ('Rd36', 'Rd37', TRUE);
INSERT INTO edge VALUES ('Rd37', 'JC4', TRUE);
INSERT INTO edge VALUES ('Rd11', 'Rd38', TRUE);
INSERT INTO edge VALUES ('Rd38', 'Rd39', TRUE);
INSERT INTO edge VALUES ('Rd12', 'Rd39', TRUE);
INSERT INTO edge VALUES ('Rd39', 'Rd40', TRUE);
INSERT INTO edge VALUES ('Rd38', 'Rd40', TRUE);
INSERT INTO edge VALUES ('Rd50', 'Rd12', FALSE);
INSERT INTO edge VALUES ('Rd55', 'Rd47', TRUE);
INSERT INTO edge VALUES ('Rd55', 'Rd48', TRUE);
INSERT INTO edge VALUES ('Rd55', 'JC9', TRUE);
INSERT INTO edge VALUES ('MT2', 'JC8', TRUE);

-- Inserts all the restaurants into the restaurant table
-- VALUES format:
-- (building, restaurant_name)
INSERT INTO restaurant VALUES ('Southside Dining Hall', 'Southside Dining Hall');
INSERT INTO restaurant VALUES ('Johnson Center', 'Panera Bread');
INSERT INTO restaurant VALUES ('Johnson Center', 'Chipotle');

-- Inserts students into the student table
-- VALUES format:
-- (email, first_name, last_name, password)
INSERT INTO student VALUES ('cguerra5@masonlive.gmu.edu', 'Carlos', 'Guerra', 'password');

-- Inserts student class times into the class_time table
-- VALUES format:
-- (student_email, year, semester, class_name, building, start_time, end_time, week_days)
INSERT INTO class_time VALUES ('cguerra5@masonlive.gmu.edu', '2019', 'Spring', 'CS321', 'Planetary Hall', '12:00:00', '13:15:00', 'MW');
INSERT INTO class_time VALUES ('cguerra5@masonlive.gmu.edu', '2019', 'Spring', 'STAT350', 'Enterprise Hall', '15:00:00', '16:15:00', 'MW');
INSERT INTO class_time VALUES ('cguerra5@masonlive.gmu.edu', '2019', 'Spring', 'OR442', 'Music/Theater Building', '13:30:00', '16:10:00', 'MW');

-- Inserts student study preferences into the study_time table
-- VALUES format:
-- (student_email, weekly_hours, min_cont_hours, max_cont_hours)
INSERT INTO study_time VALUES ('cguerra5@masonlive.gmu.edu', 8.0, 0.5, 1.0, 0.16666667);

