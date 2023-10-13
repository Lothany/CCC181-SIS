DROP TABLE IF EXISTS colleges;
CREATE TABLE IF NOT EXISTS colleges (
    collegeCode VARCHAR(255) NOT NULL,
    collegeName VARCHAR(255) NOT NULL,
    PRIMARY KEY (collegeCode)
);
