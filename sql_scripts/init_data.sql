-- Inserts each building at Mason
-- VALUES format:
-- (building_name, is_study_location)
INSERT INTO building VALUES ('Aquatic and Fitness Center', FALSE);
INSERT INTO building VALUES ('Art Building', TRUE);
INSERT INTO building VALUES ('College Hall', TRUE);
INSERT INTO building VALUES ('David King Hall', FALSE);
INSERT INTO building VALUES ('East Building', FALSE);
INSERT INTO building VALUES ('Enterprise Hall', TRUE);
INSERT INTO building VALUES ('Exploratory Hall', TRUE);
INSERT INTO building VALUES ('Fenwick Library', TRUE);
INSERT INTO building VALUES ('Innovation Hall', TRUE);
INSERT INTO building VALUES ('Johnson Center', TRUE);
INSERT INTO building VALUES ('Music/Theater Building', TRUE);
INSERT INTO building VALUES ('Merten Hall', TRUE);
INSERT INTO building VALUES ('Nguyen Engineering Building', TRUE);
INSERT INTO building VALUES ('Parking Lot C', FALSE);
INSERT INTO building VALUES ('Planetary Hall', TRUE);
INSERT INTO building VALUES ('Research Hall', TRUE);
INSERT INTO building VALUES ('Sandy Creek Shuttle Stop', FALSE);
INSERT INTO building VALUES ('Southside Dining Hall', TRUE);
INSERT INTO building VALUES ('The Hub', TRUE);
INSERT INTO building VALUES ('Tidewater', FALSE);

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
INSERT INTO edge VALUES ('DK1', 'Rd15', TRUE);
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
INSERT INTO location VALUES ('Rd100', 38.829189, -77.307464, NULL, FALSE);
INSERT INTO edge VALUES ('Rd100', 'JC9', TRUE);
INSERT INTO edge VALUES ('Rd100', 'MT1', TRUE);
INSERT INTO edge VALUES ('MT1', 'CH1', TRUE);

-- Nguyen Engineering Building Outline
INSERT INTO location VALUES ('ENG1', 38.827790, -77.305061, 'Nguyen Engineering Building', FALSE);
INSERT INTO location VALUES ('ENG2', 38.827332, -77.305030, 'Nguyen Engineering Building', FALSE);
INSERT INTO location VALUES ('ENG3', 38.827280, -77.304641, 'Nguyen Engineering Building', FALSE);
INSERT INTO location VALUES ('Rd61', 38.827594, -77.305871, NULL, FALSE);
INSERT INTO location VALUES ('Rd67', 38.827456, -77.306235, NULL, FALSE);
INSERT INTO location VALUES ('Rd68', 38.827402, -77.306101, NULL, FALSE);
INSERT INTO location VALUES ('Rd69', 38.827348, -77.305952, NULL, FALSE);
INSERT INTO location VALUES ('Rd70', 38.827193, -77.306204, NULL, FALSE);
INSERT INTO location VALUES ('Rd71', 38.827073, -77.305936, NULL, FALSE);
INSERT INTO location VALUES ('Rd72', 38.827053, -77.305694, NULL, FALSE);
INSERT INTO location VALUES ('Rd73', 38.826956, -77.305522, NULL, FALSE);
INSERT INTO location VALUES ('Rd74', 38.827047, -77.305424, NULL, FALSE);
INSERT INTO location VALUES ('Rd75', 38.827211, -77.305424, NULL, FALSE);
INSERT INTO location VALUES ('Rd76', 38.827340, -77.305287, NULL, FALSE);
INSERT INTO location VALUES ('Rd77', 38.827367, -77.305207, NULL, FALSE);
INSERT INTO location VALUES ('Rd78', 38.827150, -77.304981, NULL, FALSE);
INSERT INTO location VALUES ('Rd79', 38.827039, -77.304762, NULL, FALSE);
INSERT INTO location VALUES ('Rd80', 38.827149, -77.304638, NULL, FALSE);
INSERT INTO location VALUES ('Rd81', 38.827113, -77.304453, NULL, FALSE);
INSERT INTO location VALUES ('Rd82', 38.826965, -77.304391, NULL, FALSE);
INSERT INTO location VALUES ('Rd83', 38.827562, -77.304008, NULL, FALSE);
INSERT INTO location VALUES ('Rd84', 38.827694, -77.304375, NULL, FALSE);
INSERT INTO location VALUES ('Rd85', 38.827481, -77.304510, NULL, FALSE);
INSERT INTO location VALUES ('Rd86', 38.827674, -77.304859, NULL, FALSE);
INSERT INTO location VALUES ('Rd87', 38.827695, -77.304895, NULL, FALSE);
INSERT INTO edge VALUES ('Rd51', 'ENG1', TRUE);
INSERT INTO edge VALUES ('Rd51', 'Rd61', TRUE);
INSERT INTO edge VALUES ('Rd61', 'Rd67', TRUE);
INSERT INTO edge VALUES ('Rd67', 'Rd68', TRUE);
INSERT INTO edge VALUES ('Rd68', 'Rd69', TRUE);
INSERT INTO edge VALUES ('Rd68', 'Rd70', TRUE);
INSERT INTO edge VALUES ('Rd70', 'Rd71', TRUE);
INSERT INTO edge VALUES ('Rd71', 'Rd72', TRUE);
INSERT INTO edge VALUES ('Rd72', 'Rd73', TRUE);
INSERT INTO edge VALUES ('Rd73', 'Rd74', TRUE);
INSERT INTO edge VALUES ('Rd74', 'Rd75', TRUE);
INSERT INTO edge VALUES ('Rd75', 'Rd76', TRUE);
INSERT INTO edge VALUES ('Rd76', 'Rd77', TRUE);
INSERT INTO edge VALUES ('Rd77', 'ENG2', TRUE);
INSERT INTO edge VALUES ('ENG2', 'Rd78', TRUE);
INSERT INTO edge VALUES ('Rd78', 'Rd79', TRUE);
INSERT INTO edge VALUES ('Rd79', 'Rd80', TRUE);
INSERT INTO edge VALUES ('Rd80', 'Rd81', TRUE);
INSERT INTO edge VALUES ('Rd81', 'Rd82', TRUE);
INSERT INTO edge VALUES ('Rd82', 'Rd83', TRUE);
INSERT INTO edge VALUES ('Rd83', 'Rd84', TRUE);
INSERT INTO edge VALUES ('Rd84', 'Rd85', TRUE);
INSERT INTO edge VALUES ('Rd85', 'ENG3', TRUE);
INSERT INTO edge VALUES ('Rd85', 'Rd86', TRUE);
INSERT INTO edge VALUES ('Rd86', 'Rd87', TRUE);
INSERT INTO edge VALUES ('Rd87', 'ENG1', TRUE);

-- Fenwick Library Outline
INSERT INTO location VALUES ('FL1', 38.831796, -77.307521, 'Fenwick Library', FALSE);
INSERT INTO location VALUES ('FL2', 38.832010, -77.307627, 'Fenwick Library', FALSE);
INSERT INTO location VALUES ('Rd56', 38.832628, -77.307986, NULL, FALSE);
INSERT INTO edge VALUES ('FL1', 'FL2', TRUE);
INSERT INTO edge VALUES ('FL2', 'Rd56', TRUE);

-- Merten Hall Outline
INSERT INTO location VALUES ('MH1', 38.834854, -77.307871, 'Merten Hall', FALSE);
INSERT INTO location VALUES ('Rd60', 38.834718, -77.307859, NULL, FALSE);
INSERT INTO edge VALUES ('Rd60', 'MH1', TRUE);

-- East Building Outline
INSERT INTO location VALUES ('EB1', 38.833107, -77.308039, 'East Building', FALSE);

-- Art Building Outline
INSERT INTO location VALUES ('AB1', 38.827739, -77.305939, 'Art Building', FALSE);
INSERT INTO location VALUES ('AB2', 38.828266, -77.306287, 'Art Building', FALSE);
INSERT INTO location VALUES ('Rd62', 38.828199, -77.306241, NULL, FALSE);
INSERT INTO location VALUES ('Rd63', 38.828494, -77.306438, NULL, FALSE);
INSERT INTO location VALUES ('Rd64', 38.828384, -77.306712, NULL, FALSE);
INSERT INTO edge VALUES ('AB1', 'Rd62', TRUE);
INSERT INTO edge VALUES ('Rd62', 'AB2', TRUE);
INSERT INTO edge VALUES ('AB2', 'Rd63', TRUE);
INSERT INTO edge VALUES ('Rd63', 'Rd64', TRUE);

-- Innovation Hall Outline
INSERT INTO location VALUES ('IN1', 38.828382, -77.307272, 'Innovation Hall', FALSE);
INSERT INTO location VALUES ('IN2', 38.828700, -77.307528, 'Innovation Hall', FALSE);
INSERT INTO location VALUES ('Rd65', 38.828699, -77.306731, NULL, FALSE);
INSERT INTO location VALUES ('Rd66', 38.828202, -77.307159, NULL, FALSE);
INSERT INTO edge VALUES ('Rd64', 'Rd65', TRUE);
INSERT INTO edge VALUES ('Rd64', 'Rd66', TRUE);
INSERT INTO edge VALUES ('Rd66', 'IN1', TRUE);

-- Outline of Aquatic and Fitness Center
INSERT INTO location VALUES ('AFC1', 38.826672, -77.304375, 'Aquatic and Fitness Center', FALSE);
INSERT INTO location VALUES ('Rd90', 38.826695, -77.304861, NULL, FALSE);
INSERT INTO location VALUES ('Rd91', 38.826472, -77.304815, NULL, FALSE);
INSERT INTO location VALUES ('Rd92', 38.826386, -77.304960, NULL, FALSE);
INSERT INTO edge VALUES ('Rd90', 'Rd91', TRUE);
INSERT INTO edge VALUES ('Rd91', 'AFC1', TRUE);
INSERT INTO edge VALUES ('Rd91', 'Rd92', TRUE);

-- Outline of Parking Lot C
INSERT INTO location VALUES ('LC1', 38.825818, -77.305159, 'Parking Lot C', FALSE);

-- Outline of the Hub
INSERT INTO location VALUES ('H1', 38.830996, -77.305413, 'The Hub', FALSE);
INSERT INTO location VALUES ('H2', 38.830647, -77.305281, 'The Hub', FALSE);
INSERT INTO location VALUES ('H3', 38.830347, -77.304862, 'The Hub', FALSE);
INSERT INTO location VALUES ('H4', 38.830347, -77.304862, 'The Hub', FALSE);
INSERT INTO location VALUES ('Rd94', 38.830990, -77.305558, NULL, FALSE);
INSERT INTO location VALUES ('Rd95', 38.830828, -77.306008, NULL, FALSE);
INSERT INTO location VALUES ('Rd96', 38.830534, -77.305611, NULL, FALSE);
INSERT INTO location VALUES ('Rd97', 38.830444, -77.305248, NULL, FALSE);
INSERT INTO location VALUES ('Rd98',38.830169, -77.304725 , NULL, FALSE);
INSERT INTO edge VALUES ('H1', 'Rd94', TRUE);
INSERT INTO edge VALUES ('Rd94', 'Rd95', TRUE);
INSERT INTO edge VALUES ('Rd95', 'Rd6', TRUE);
INSERT INTO edge VALUES ('Rd6', 'Rd96', TRUE);
INSERT INTO edge VALUES ('Rd96', 'H2', TRUE);
INSERT INTO edge VALUES ('H2', 'Rd97', TRUE);
INSERT INTO edge VALUES ('Rd96', 'Rd97', TRUE);
INSERT INTO edge VALUES ('Rd97', 'H3', TRUE);
INSERT INTO edge VALUES ('H3', 'H4', TRUE);
INSERT INTO edge VALUES ('H4', 'Rd98', TRUE);

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
INSERT INTO location VALUES ('Rd57', 38.833483, -77.308028, NULL, FALSE);
INSERT INTO location VALUES ('Rd58', 38.833615, -77.308041, NULL, FALSE);
INSERT INTO location VALUES ('Rd59', 38.834140, -77.307970, NULL, FALSE);
INSERT INTO location VALUES ('Rd88', 38.826785, -77.304906, NULL, FALSE);
INSERT INTO location VALUES ('Rd89', 38.826738, -77.304876, NULL, FALSE);
INSERT INTO location VALUES ('Rd93', 38.825862, -77.305078, NULL, FALSE);
INSERT INTO location VALUES ('Rd99', 38.830019, -77.304969, NULL, FALSE);
INSERT INTO location VALUES ('Rd101', 38.829004, -77.307376, NULL, FALSE);
INSERT INTO location VALUES ('Rd102', 38.828860, -77.307379, NULL, FALSE);
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
INSERT INTO edge VALUES ('Rd33', 'FL1', TRUE);
INSERT INTO edge VALUES ('MT2', 'JC8', TRUE);
INSERT INTO edge VALUES ('Rd56', 'EB1', TRUE);
INSERT INTO edge VALUES ('EB1', 'Rd57', TRUE);
INSERT INTO edge VALUES ('Rd57', 'Rd58', TRUE);
INSERT INTO edge VALUES ('Rd58', 'Rd59', TRUE);
INSERT INTO edge VALUES ('Rd59', 'Rd60', TRUE);
INSERT INTO edge VALUES ('AB1', 'Rd61', TRUE);
INSERT INTO edge VALUES ('Rd43', 'Rd63', TRUE);
INSERT INTO edge VALUES ('Rd65', 'Rd44', TRUE);
INSERT INTO edge VALUES ('Rd78', 'Rd88', TRUE);
INSERT INTO edge VALUES ('Rd88', 'Rd89', TRUE);
INSERT INTO edge VALUES ('Rd89', 'Rd90', TRUE);
INSERT INTO edge VALUES ('Rd92', 'Rd93', TRUE);
INSERT INTO edge VALUES ('Rd93', 'LC1', TRUE);
INSERT INTO edge VALUES ('Rd94', 'Rd21', TRUE);
INSERT INTO edge VALUES ('Rd98', 'Rd99', TRUE);
INSERT INTO edge VALUES ('Rd99', 'Rd9', TRUE);
INSERT INTO edge VALUES ('Rd100', 'Rd101', TRUE);
INSERT INTO edge VALUES ('Rd101', 'Rd102', TRUE);
INSERT INTO edge VALUES ('Rd102', 'IN2', TRUE);

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
INSERT INTO student VALUES ('mmemon@masonlive.gmu.edu', 'Marvii', 'Memon', 'password');
INSERT INTO student VALUES ('bfaraj@masonlive.gmu.edu', 'Baban', 'Faraj', 'password');

-- Inserts student class times into the class_time table
-- VALUES format:
-- (student_email, year, semester, class_name, building, start_time, end_time, week_days)
INSERT INTO class_time VALUES ('cguerra5@masonlive.gmu.edu', '2019', 'spring', 'CS321', 'Planetary Hall', '12:00:00', '13:15:00', 'MW');
INSERT INTO class_time VALUES ('cguerra5@masonlive.gmu.edu', '2019', 'spring', 'STAT350', 'Enterprise Hall', '15:00:00', '16:15:00', 'MW');
INSERT INTO class_time VALUES ('cguerra5@masonlive.gmu.edu', '2019', 'spring', 'OR442', 'Music/Theater Building', '13:30:00', '16:10:00', 'MW');
INSERT INTO class_time VALUES ('cguerra5@masonlive.gmu.edu', '2018', 'spring', 'PHYS260-001', 'Nguyen Engineering Building', '08:30:00', '09:20:00', 'MWF');
INSERT INTO class_time VALUES ('cguerra5@masonlive.gmu.edu', '2018', 'spring', 'PHYS260-302', 'Planetary Hall', '11:30:00', '12:20:00', 'F');
INSERT INTO class_time VALUES ('cguerra5@masonlive.gmu.edu', '2018', 'spring', 'PHYS261', 'Planetary Hall', '16:30:00', '19:10:00', 'W');
INSERT INTO class_time VALUES ('cguerra5@masonlive.gmu.edu', '2018', 'spring', 'CS367', 'Art Building', '12:00:00', '13:15:00', 'MW');
INSERT INTO class_time VALUES ('cguerra5@masonlive.gmu.edu', '2018', 'spring', 'MATH203', 'Innovation Hall', '10:30:00', '11:45:00', 'MW');
INSERT INTO class_time VALUES ('cguerra5@masonlive.gmu.edu', '2018', 'spring', 'CS330', 'Merten Hall', '15:00:00', '16:15:00', 'MW');
INSERT INTO class_time VALUES ('cguerra5@masonlive.gmu.edu', '2018', 'spring', 'REC101', 'Aquatic and Fitness Center', '17:00:00', '18:00:00', 'MW');

INSERT INTO class_time VALUES ('mmemon@masonlive.gmu.edu', '2019', 'spring', 'CS321', 'Planetary Hall', '12:00:00', '13:15:00', 'MW');
INSERT INTO class_time VALUES ('mmemon@masonlive.gmu.edu', '2019', 'spring', 'STAT350', 'Enterprise Hall', '15:00:00', '16:15:00', 'MW');
INSERT INTO class_time VALUES ('mmemon@masonlive.gmu.edu', '2019', 'spring', 'OR442', 'Music/Theater Building', '13:30:00', '16:10:00', 'MW');
INSERT INTO class_time VALUES ('mmemon@masonlive.gmu.edu', '2018', 'spring', 'PHYS260-001', 'Nguyen Engineering Building', '08:30:00', '09:20:00', 'MWF');
INSERT INTO class_time VALUES ('mmemon@masonlive.gmu.edu', '2018', 'spring', 'PHYS260-302', 'Planetary Hall', '11:30:00', '12:20:00', 'F');
INSERT INTO class_time VALUES ('mmemon@masonlive.gmu.edu', '2018', 'spring', 'PHYS261', 'Planetary Hall', '16:30:00', '19:10:00', 'W');
INSERT INTO class_time VALUES ('mmemon@masonlive.gmu.edu', '2018', 'spring', 'CS367', 'Art Building', '12:00:00', '13:15:00', 'MW');
INSERT INTO class_time VALUES ('mmemon@masonlive.gmu.edu', '2018', 'spring', 'MATH203', 'Innovation Hall', '10:30:00', '11:45:00', 'MW');
INSERT INTO class_time VALUES ('mmemon@masonlive.gmu.edu', '2018', 'spring', 'CS330', 'Merten Hall', '15:00:00', '16:15:00', 'MW');
INSERT INTO class_time VALUES ('mmemon@masonlive.gmu.edu', '2018', 'spring', 'REC101', 'Aquatic and Fitness Center', '17:00:00', '18:00:00', 'MW');

INSERT INTO class_time VALUES ('bfaraj@masonlive.gmu.edu', '2019', 'spring', 'CS321', 'Planetary Hall', '12:00:00', '13:15:00', 'MW');
INSERT INTO class_time VALUES ('bfaraj@masonlive.gmu.edu', '2019', 'spring', 'STAT350', 'Enterprise Hall', '15:00:00', '16:15:00', 'MW');
INSERT INTO class_time VALUES ('bfaraj@masonlive.gmu.edu', '2019', 'spring', 'OR442', 'Music/Theater Building', '13:30:00', '16:10:00', 'MW');
INSERT INTO class_time VALUES ('bfaraj@masonlive.gmu.edu', '2018', 'spring', 'PHYS260-001', 'Nguyen Engineering Building', '08:30:00', '09:20:00', 'MWF');
INSERT INTO class_time VALUES ('bfaraj@masonlive.gmu.edu', '2018', 'spring', 'PHYS260-302', 'Planetary Hall', '11:30:00', '12:20:00', 'F');
INSERT INTO class_time VALUES ('bfaraj@masonlive.gmu.edu', '2018', 'spring', 'PHYS261', 'Planetary Hall', '16:30:00', '19:10:00', 'W');
INSERT INTO class_time VALUES ('bfaraj@masonlive.gmu.edu', '2018', 'spring', 'CS367', 'Art Building', '12:00:00', '13:15:00', 'MW');
INSERT INTO class_time VALUES ('bfaraj@masonlive.gmu.edu', '2018', 'spring', 'MATH203', 'Innovation Hall', '10:30:00', '11:45:00', 'MW');
INSERT INTO class_time VALUES ('bfaraj@masonlive.gmu.edu', '2018', 'spring', 'CS330', 'Merten Hall', '15:00:00', '16:15:00', 'MW');
INSERT INTO class_time VALUES ('bfaraj@masonlive.gmu.edu', '2018', 'spring', 'REC101', 'Aquatic and Fitness Center', '17:00:00', '18:00:00', 'MW');

-- Inserts student study preferences into the study_time table
-- VALUES format:
-- (student_email, weekly_hours, min_cont_hours, max_cont_hours)
INSERT INTO study_time VALUES ('cguerra5@masonlive.gmu.edu', 8.0, 0.5, 1.0, 0.16666667, '09:00:00', '21:00:00');
INSERT INTO study_time VALUES ('mmemon@masonlive.gmu.edu', 8.0, 0.5, 1.0, 0.16666667, '09:00:00', '21:00:00');
INSERT INTO study_time VALUES ('bfaraj@masonlive.gmu.edu', 8.0, 0.5, 1.0, 0.16666667, '09:00:00', '21:00:00');

-- Inserts student study preferINSERT INTO class_time VALUES ('mmemon@masonlive.gmu.edu', '2018', 'spring', 'REC101', 'Aquatic and Fitness Center', '17:00:00', '18:00:00', 'MW');ences into the meal_time table
-- VALUES format:
-- (student_email, daily_meal_num, min_meal_hours, max_meal_hours, earliest_time, latest_time)
INSERT INTO meal_time VALUES ('cguerra5@masonlive.gmu.edu', 3, 0.25, 0.5, '08:00:00', '23:59:00');
INSERT INTO meal_time VALUES ('mmemon@masonlive.gmu.edu', 3, 0.25, 0.5, '08:00:00', '23:59:00');
INSERT INTO meal_time VALUES ('bfaraj@masonlive.gmu.edu', 3, 0.25, 0.5, '08:00:00', '23:59:00');

