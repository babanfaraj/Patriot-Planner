-- Sets up the patriotplanner tables

CREATE TABLE building (
    building_name VARCHAR(50),
    is_study_location BOOLEAN NOT NULL,
    PRIMARY KEY (building_name)
);

CREATE TABLE location (
    location_name VARCHAR(25),
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    building VARCHAR(50),
    is_parking_lot BOOLEAN NOT NULL,
    FOREIGN KEY (building)
        REFERENCES building(building_name),
    PRIMARY KEY (location_name)
);

CREATE TABLE student (
    email VARCHAR(50),
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    password VARCHAR(25) NOT NULL,
    PRIMARY KEY (email)
);

CREATE TABLE edge (
    location1 VARCHAR(25),
    location2 VARCHAR(25),
    is_active BOOLEAN NOT NULL,
    FOREIGN KEY (location1)
        REFERENCES location(location_name),
    FOREIGN KEY (location2)
        REFERENCES location(location_name),
    PRIMARY KEY (location1, location2)
);

CREATE TABLE restaurant (
    building VARCHAR(50),
    restaurant_name VARCHAR(25),
    FOREIGN KEY (building)
        REFERENCES building(building_name),
    PRIMARY KEY (building, restaurant_name)
);

CREATE TABLE class_time (
    student_email VARCHAR(50),
    year CHAR(4),
    semester VARCHAR(7),
    class_name VARCHAR(25),
    building VARCHAR(50),
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    week_days VARCHAR(7),
    FOREIGN KEY (student_email)
        REFERENCES student(email),
    FOREIGN KEY (building)
        REFERENCES building(building_name),
    PRIMARY KEY (student_email, year, semester, class_name)
);

CREATE TABLE study_time (
    student_email VARCHAR(50),
    weekly_hours FLOAT NOT NULL,
    min_cont_hours FLOAT NOT NULL,
    max_cont_hours FLOAT NOT NULL,
    break_time_hours FLOAT NOT NULL,
    earliest_time TIME NOT NULL,
    latest_time TIME NOT NULL,

    FOREIGN KEY (student_email)
        REFERENCES student(email),
    PRIMARY KEY (student_email)
);

CREATE TABLE meal_time (
    student_email VARCHAR(50),
    daily_meal_num INTEGER NOT NULL,
    min_meal_hours FLOAT NOT NULL,
    max_meal_hours FLOAT NOT NULL,
    earliest_time TIME NOT NULL,
    latest_time TIME NOT NULL,

    FOREIGN KEY (student_email)
        REFERENCES student(email),
    PRIMARY KEY (student_email)
);

