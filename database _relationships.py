#students_id     students_name      course_id       course_name
#1               Job                 101            cs
#2               Paul                101            cs
#3               Freshier            102            it
#4               Jole                101            cs

#Primary key
#student_id INTEGER PRIMARY KEY


#foreign keys
#course_id INTEGER, FOREIGN KEY(course_id) REFERENCES Courses (course_id)

CREATE TABLES units(
    unit_id INTEGER PRIMARY KEY,
    unit_name TEXT NOT NULL,

);

CREATE TABLE enrollments(
    student_id INTEGER NOT NULL,
    unit_id INTEGER NOT NULL,

    PRIMARY KEY(student_id,unit_id),
)