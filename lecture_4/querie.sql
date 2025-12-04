-- 1. Create databases
-- Create database students
create table students
(
	id INTEGER PRIMARY KEY,
	full_name TEXT,
	birth_year INTEGER
);
-- Create database grades
create table grades
(
	id integer primary key,
	student_id integer references students(id),
	subject text,
	grade integer check (grade >= 1 and grade<=100)
);

-- 2. Insert data
-- Insert data in table students
insert into students (id, full_name, birth_year) values
(1, 'Alice Johnson', 2005),
(2, 'Brian Smith', 2004),
(3, 'Carla Reyes', 2006),
(4, 'Daniel Kim', 2005),
(5, 'Eva Thompson', 2003),
(6, 'Felix Nguyen', 2007),
(7, 'Grace Patel', 2005),
(8, 'Henry Lopez', 2004),
(9, 'Isabella Martinez', 2006);
-- Insert data in table grades
insert into grades (id, student_id, subject, grade)
values (1,1, 'Math', 88),
(2,1, 'English', 92),
(3,1, 'Science', 85),
(4,2, 'Math', 75),
(5,2, 'History', 83),
(6,2, 'English', 79),
(7,3, 'Science', 95),
(8,3, 'Math', 91),
(9,3, 'Art', 89),
(10,4, 'Math', 84),
(11,4, 'Science', 88),
(12,4, 'Physical Education', 93),
(13,5, 'English', 90),
(14,5, 'History', 85),
(15,5, 'Math', 88),
(16,6, 'Science', 72),
(17,6, 'Math', 78),
(18,6, 'English', 81),
(19,7, 'Art', 94),
(20,7, 'Science', 87),
(21,7, 'Math', 90),
(22,8, 'History', 77),
(23,8, 'Math', 83),
(24,8, 'Science', 80),
(25,9, 'English', 96),
(26,9, 'Math', 89),
(27,9, 'Art', 92);

-- Create indexse id table students on full_name 
create index students_full_name on students(full_name);

-- 3. Find all grades for a specific student (Alice Johnson).
select g.grade from grades as g
join students as s on s.id = g.student_id
where full_name ='Alice Johnson';

-- 4. Calculate the average grade per student.
select s.full_name,avg(grade) from grades as g
join students as s on s.id = g.student_id
group by s.full_name;

-- 5. List all students born after 2004.
select full_name from students where birth_year>2004;

-- 6. Create a query that lists all subjects and their average grades.
select subject, avg(grade) from grades group by subject;

-- 7. Find the top 3 students with the highest average grades
with s_with_g as (
select s.full_name as name,avg(grade) as avg_grade from grades as g
join students as s on s.id = g.student_id
group by s.full_name
order by avg_grade)
select name from s_with_g
limit 3;
-- 8. Show all students who have scored below 80 in any subject
select distinct s.full_name from grades as g
join students as s on s.id = g.student_id
where g.grade<80;





