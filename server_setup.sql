-- Sets up the patriotplanner tables

CREATE TABLE locations (
    locationName VARCHAR(25),
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    isActive BOOLEAN NOT NULL,
    isStudyLocation BOOLEAN NOT NULL,
    isParkingLot BOOLEAN NOT NULL,
    PRIMARY KEY (locationName)
);

CREATE TABLE student (
    email VARCHAR(50),
    firstName VARCHAR(25) NOT NULL,
    lastName VARCHAR(25) NOT NULL,
    PRIMARY KEY (email)
);

CREATE TABLE edges (
    location1 VARCHAR(25),
    location2 VARCHAR(25),
    FOREIGN KEY (location1)
        REFERENCES locations(locationName),
    FOREIGN KEY (location2)
        REFERENCES locations(locationName),
    PRIMARY KEY (location1, location2)
);

CREATE TABLE restaurant (
    location VARCHAR(25),
    resturantName VARCHAR(25) NOT NULL,
    FOREIGN KEY (location)
        REFERENCES locations(locationName),
    PRIMARY KEY (location)
);

CREATE TABLE schedule (
    studentEmail VARCHAR(50),
    year CHAR(4),
    semester VARCHAR(7),
    className VARCHAR(25),
    location VARCHAR(25),
    startTime TIME NOT NULL,
    endTime TIME NOT NULL,
    weekDays VARCHAR(7),
    FOREIGN KEY (studentEmail)
        REFERENCES student(email),
    FOREIGN KEY (location)
        REFERENCES locations(locationName),
    PRIMARY KEY (studentEmail, year, semester, className)
);

CREATE TABLE studyTime (
    studentEmail VARCHAR(50),
    weeklyHours FLOAT NOT NULL,
    minContHours FLOAT NOT NULL,
    maxContHours FLOAT NOT NULL,
    FOREIGN KEY (studentEmail)
        REFERENCES student(email),
    PRIMARY KEY (studentEmail)
);

INSERT INTO student VALUES ('cguerra5@masonlive.gmu.edu', 'Carlos', 'Guerra');

