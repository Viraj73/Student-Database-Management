CREATE DATABASE IF NOT EXISTS student_manage;
USE student_manage;

CREATE TABLE IF NOT EXISTS Student_details (
    Roll_No INT PRIMARY KEY,
    Admission_Number INT,
    First_Name VARCHAR(50),
    Second_Name VARCHAR(50),
    Father_Name VARCHAR(50),
    Mother_Name VARCHAR(50),
    Gender VARCHAR(10),
    State VARCHAR(30),
    Enrollment_Date DATE
);

CREATE TABLE IF NOT EXISTS Marks (
    Roll_number INT,
    admission_number INT,
    Name VARCHAR(50),
    exam_name VARCHAR(30),
    Subject VARCHAR(30),
    marks_obtained INT
);
