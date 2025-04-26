------------------- Notes on SQL Syntax --------------------

DROP DATABASE testdb;    --------- delete database
CREATE DATABASE company;    --------- create database

CREATE TABLE emp_details(    ------- create table
	indiv_id INTEGER,
	emp_fname VARCHAR(50),
	emp_lname VARCHAR(50),
    emp_dob DATE,
    emp_age INTEGER,
	emp_address VARCHAR(255),
	emp_phone INTEGER,
	emp_email VARCHAR(100),
    emp_nationality VARCHAR(100)	
);

TRUNCATE TABLE emp_details;    ------- to empty table

DROP TABLE emp_details;    -------- delete table

---# Constraints
-- 1. NOT NULL
-- 2. UNIQUE
-- 3. CHECK    ---- to check given condition
-- 4. DEFAULT
-- 5. PRIMARY KEY
-- 6. FOREIGN KEY

--- Create table with Constraints
CREATE TABLE emp_details( 
	indiv_id SERIAL PRIMARY KEY,
	emp_fname VARCHAR(50) NOT NULL,
	emp_lname VARCHAR(50),
	emp_dob DATE,
	emp_age INTEGER CHECK(emp_age >= 18 AND emp_age <= 65),
	emp_address VARCHAR(255),
	emp_phone INTEGER UNIQUE NOT NULL,
	emp_email VARCHAR(100) UNIQUE,
    emp_nationality VARCHAR(100) DEFAULT 'Unknown Nationality'
);

CREATE TABLE employees(
	emp_id SERIAL PRIMARY KEY, 
	emp_fname VARCHAR(50) NOT NULL,
	emp_lname VARCHAR(50),
	emp_department VARCHAR(100),
	emp_salary NUMERIC,
	joining_date DATE DEFAULT CURRENT_DATE,
	emp_phone INTEGER,
	emp_indiv_id INTEGER,

	FOREIGN KEY (emp_indiv_id) REFERENCES emp_details(indiv_id)    ------- this is the way to set foreign key
);

--- Another way to use constraint
CREATE TABLE emp_details(   
    indiv_id INTEGER,
    emp_fname VARCHAR(50) NOT NULL,
    emp_lname VARCHAR(50),
    emp_dob DATE,
    emp_age INTEGER,
    emp_address VARCHAR(255),                         
    emp_phone INTEGER,
    emp_email VARCHAR(100),
    emp_nationality VARCHAR(100),

    CONSTRAINT emp_details_emp_phone_unique UNIQUE(emp_phone),    -------- this is another way to set constraint
    CONSTRAINT emp_details_emp_age_check CHECK (emp_age >= 18),
    CONSTRAINT emp_details_emp_fname_emp_email_unique UNIQUE(emp_fname,emp_email)    --- set constraint on combination of both columns
);

--- # Referential Actions in PostgreSQL
-- 1. NO ACTION (default)    --- Rejects the DELETE or UPDATE if it breaks the foreign key constraint.
-- 2. RESTRICT    --- Like NO ACTION, but checks immediately (before any other triggers run).
-- 3. CASCADE    --- Automatically deletes or updates the referencing rows to match the change.
-- 4. SET NULL    --- Sets the foreign key column to NULL if the referenced row is deleted/updated.
-- 5. SET DEFAULT    --- Sets the foreign key column to its DEFAULT value.

--- Syntax Examples:
CREATE TABLE employees(
	emp_id SERIAL PRIMARY KEY, 
	emp_fname VARCHAR(50) NOT NULL,
	emp_lname VARCHAR(50),
	emp_department VARCHAR(100),
	emp_salary NUMERIC,
	joining_date DATE DEFAULT CURRENT_DATE,
	emp_phone INTEGER,
	emp_indiv_id INTEGER,

	CONSTRAINT employees_emp_indiv_id_fkey FOREIGN KEY (emp_indiv_id) REFERENCES emp_details(indiv_id)
	ON DELETE CASCADE
	ON UPDATE CASCADE    -------------- CASCADE
);

CREATE TABLE employees(
	emp_id SERIAL PRIMARY KEY, 
	emp_fname VARCHAR(50) NOT NULL,
	emp_lname VARCHAR(50),
	emp_department VARCHAR(100),
	emp_salary NUMERIC,
	joining_date DATE DEFAULT CURRENT_DATE,
	emp_phone INTEGER,
	emp_indiv_id INTEGER,

	CONSTRAINT employees_emp_indiv_id_fkey FOREIGN KEY (emp_indiv_id) REFERENCES emp_details(indiv_id)
	ON DELETE SET NULL
	ON UPDATE SET NULL    ---------------- SET NULL
);

CREATE TABLE employees(
	emp_id SERIAL PRIMARY KEY, 
	emp_fname VARCHAR(50) NOT NULL,
	emp_lname VARCHAR(50),
	emp_department VARCHAR(100),
	emp_salary NUMERIC,
	joining_date DATE DEFAULT CURRENT_DATE,
	emp_phone INTEGER,
	emp_indiv_id INTEGER DEFAULT 0,  -- default value is required for SET DEFAULT

	CONSTRAINT employees_emp_indiv_id_fkey FOREIGN KEY (emp_indiv_id) REFERENCES emp_details(indiv_id)
	ON DELETE SET DEFAULT
	ON UPDATE SET DEFAULT    ----------- SET DEFAULT
);

CREATE TABLE employees(
	emp_id SERIAL PRIMARY KEY, 
	emp_fname VARCHAR(50) NOT NULL,
	emp_lname VARCHAR(50),
	emp_department VARCHAR(100),
	emp_salary NUMERIC,
	joining_date DATE DEFAULT CURRENT_DATE,
	emp_phone INTEGER,
	emp_indiv_id INTEGER DEFAULT 0,

	CONSTRAINT employees_emp_indiv_id_fkey FOREIGN KEY (emp_indiv_id) REFERENCES emp_details(indiv_id)
	ON DELETE SET NULL
	ON UPDATE SET DEFAULT    ----------- Mix
);

--- # ALTER TABLE command
--- Some use cases are:
-- 1. Add new columns
-- 2. Delete existing columns
-- 3. Modify existing columns

----------- Add new column ------------
ALTER TABLE emp_details
ADD COLUMN height_in_m NUMERIC,    
ADD COLUMN weight_in_kg NUMERIC;

-------- Modify existing column ---------
ALTER TABLE emp_details
ALTER COLUMN height_in_m SET NOT NULL,    -- Set Not null
ALTER COLUMN height_in_m TYPE INTEGER,    -- Set data type
ALTER COLUMN weight_in_kg TYPE INTEGER;

ALTER TABLE emp_details
ADD CONSTRAINT emp_details_height_in_m_check CHECK (height_in_m >= 1.72)    -- Add Constraint

DROP CONSTRAINT emp_details_height_in_m_check;    -- Delete Constraint

---------- Delete existing column ---------
ALTER TABLE emp_details
DROP COLUMN height_in_m,    
DROP COLUMN weight_in_kg;

----------- Rename table -------------
ALTER TABLE smartphones_cleaned_v6 RENAME TO smartphones;

---# INSERT data into table 

INSERT INTO emp_details 
    (emp_fname, emp_lname, emp_dob, emp_age, emp_address, emp_phone, emp_email, emp_nationality)  -- specifying the columns (all)
VALUES
    ('John', 'Doe', '1990-05-15', 34, '123 Main Street, NY', 1234567890, 'john.doe@example.com', 'American'),
    ('Jane', 'Smith', '1985-07-20', 39, '456 Elm Street, CA', 1234567891, 'jane.smith@example.com', 'Canadian'),
    ('Robert', 'Brown', '1992-11-03', 32, '789 Pine Avenue, TX', 1234567892, 'robert.brown@example.com', 'British'),
    ('Emily', 'Johnson', '1999-04-12', 25, '135 Oak Blvd, FL', 1234567893, NULL, 'Australian'),
    ('Michael', 'Williams', '1980-08-30', 44, '246 Cedar Rd, IL', 1234567894, 'michael.williams@example.com', NULL),
    ('Olivia', 'Jones', '1995-09-17', 29, '357 Maple Street, WA', 1234567895, 'olivia.jones@example.com', 'German'),
    ('David', 'Miller', '1988-12-01', 36, '468 Birch Lane, NV', 1234567896, NULL, 'Swedish'),
    ('Sophia', 'Taylor', '1997-02-23', 27, '579 Ash Dr, MA', 1234567897, 'sophia.taylor@example.com', 'Dutch'),
    ('Daniel', 'Anderson', '1975-06-11', 49, '680 Walnut Ave, OR', 1234567898, 'daniel.anderson@example.com', 'Finnish'),
    ('Ava', 'Thomas', '1982-10-07', 42, '791 Cherry Circle, GA', 1234567899, 'ava.thomas@example.com', 'Spanish');

INSERT INTO emp_details 
    (emp_fname, emp_phone, emp_nationality)  -- specifying the columns (not all)
VALUES
    ('Liam', 1234567800, 'Irish'),
    ('Noah', 1234567801, 'Norwegian'),
    ('Emma', 1234567802, 'Danish'),
    ('Mason', 1234567803, 'Italian'),
    ('Isabella', 1234567804, 'Greek');

INSERT INTO emp_details  -- without specifying the columns
VALUES
    (DEFAULT, 'John', 'Doe', '1990-05-15', 34, '123 Main Street, NY', 1234567890, 'john.doe@example.com', 'American'),
    (DEFAULT, 'Jane', 'Smith', '1985-07-20', 39, '456 Elm Street, CA', 1234567891, 'jane.smith@example.com', 'Canadian'),
    (DEFAULT, 'Robert', 'Brown', '1992-11-03', 32, '789 Pine Avenue, TX', 1234567892, 'robert.brown@example.com', 'British'),
    (DEFAULT, 'Emily', 'Johnson', '1999-04-12', 25, '135 Oak Blvd, FL', 1234567893, NULL, 'Australian'),
    (DEFAULT, 'Michael', 'Williams', '1980-08-30', 44, '246 Cedar Rd, IL', 1234567894, 'michael.williams@example.com', DEFAULT),
    (DEFAULT, 'Olivia', 'Jones', '1995-09-17', 29, '357 Maple Street, WA', 1234567895, 'olivia.jones@example.com', 'German'),
    (DEFAULT, 'David', 'Miller', '1988-12-01', 36, '468 Birch Lane, NV', 1234567896, NULL, 'Swedish'),
    (DEFAULT, 'Sophia', 'Taylor', '1997-02-23', 27, '579 Ash Dr, MA', 1234567897, 'sophia.taylor@example.com', 'Dutch'),
    (DEFAULT, 'Daniel', 'Anderson', '1975-06-11', 49, '680 Walnut Ave, OR', 1234567898, 'daniel.anderson@example.com', 'Finnish'),
    (DEFAULT, 'Ava', 'Thomas', '1982-10-07', 42, '791 Cherry Circle, GA', 1234567899, 'ava.thomas@example.com', 'Spanish');

---# Importing data from csv file to PostgreSQL using cmd

-- C:\Users\Acer> pip install csvkit
-- C:\Users\Acer> cd C:\Users\Acer\Downloads
-- C:\Users\Acer\Downloads>csvsql --db postgresql://postgres:admin@localhost/company --insert insurance_data.csv
--For chunk-- C:\Users\Acer\Downloads>csvsql --db postgresql://postgres:admin@localhost/company --insert smartphones_cleaned_v6.csv --chunk-size 2000
--For other type of encoding-- C:\Users\Acer\Downloads\qqq>csvsql --db postgresql://postgres:admin@localhost/test4db --insert --encoding latin1 movies.csv

---# For importing data from multiple csv file, use PowerShell

-- PS C:\Users\Acer> cd "C:\Users\Acer\Downloads\ddd"
-- PS C:\Users\Acer\Downloads\ddd> $files = Get-ChildItem -Filter *.csv
-- PS C:\Users\Acer\Downloads\ddd> foreach ($file in $files) {
-- >>     $tableName = $file.BaseName
-- >>     csvsql --db postgresql://postgres:admin@localhost/test1db --insert --tables $tableName --create $file.FullName
-- >> }

---# SELECT

---Select all columns
SELECT * FROM smartphones; -- retrive all columns from table called smartphones

---Select specific columns / filtering columns
SELECT model, price, rating FROM smartphones 

--- Renaming column (temporary) -- AS - alias
SELECT os AS operating_sys, model, battery_capacity FROM smartphones 

--- Expression using columns
SELECT model,
	SQRT((resolution_width*resolution_width) + (resolution_height*resolution_height))/screen_size AS ppi 
	FROM smartphones

SELECT model, rating/10 AS rating_in_10 FROM smartphones  -- another one

--- constant
SELECT model, 'smartphone' AS type FROM smartphones    -- here 'smartphone' is constant and 'type' is a new temp-column

--- DISTINCT --- to fetch unique values
SELECT DISTINCT brand_name FROM smartphones    -- with single column
SELECT DISTINCT brand_name, processor_brand FROM smartphones  -- with combination(multiple column) --- this syntax will show data in separate column
SELECT DISTINCT (brand_name, processor_brand) FROM smartphones -- with combination(multiple column) --- this syntax will show data in single column

--- Filtering rows using WHERE clause
SELECT * FROM smartphones      
	WHERE brand_name = 'oppo'  --- here, fetch all the columns & rows, where brand_name is 'oppo'

SELECT * FROM smartphones
	WHERE price > 100000;  --- here, fetch all the columns & rows, where price is greater than 100000

SELECT model FROM smartphones  -- here shows only model column
	WHERE price > 100000;

SELECT model, price FROM smartphones  -- here shows both model and price column
	WHERE price > 100000;

--- AND
SELECT model, price FROM smartphones
	WHERE price >= 150000 AND price <= 200000;   --- smartphone's price between 150000 and 200000

SELECT model, price, rating FROM smartphones
	WHERE rating > 80 AND price < 25000;      --- smartphones with rating > 80 and price < 25000

SELECT * FROM smartphones
	WHERE rating > 80 AND price < 25000 AND processor_brand = 'snapdragon'; --- added another condition

SELECT * FROM smartphones
	WHERE brand_name = 'samsung' AND ram_capacity = 8;   --- find all samsung phones with ram > 8GB

--- BETWEEN
SELECT model, price FROM smartphones
	WHERE price BETWEEN 150000 AND 200000;    --- smartphone's price between 150000 and 200000

--- Query execution order:
-- FROM -> JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT -> DISTINCT -> ORDER BY

--- OR
SELECT * FROM smartphones       ----- find smartphones whose processor brand is exynos or bionic or tiger
	WHERE processor_brand = 'exynos'
		OR processor_brand = 'bionic'
		OR processor_brand = 'tiger';

--- IN
SELECT * FROM smartphones       ----- find smartphones whose processor brand is exynos or bionic or tiger
	WHERE processor_brand
		IN('exynos', 'bionic', 'tiger');

--- NOT IN ---- opposite to IN
SELECT * FROM smartphones      ------ find smartphones whose processor brands are not exynos, bionic and tiger
	WHERE processor_brand
		NOT IN('exynos', 'bionic', 'tiger');

--- # UPDATE --- permanent change
UPDATE smartphones
	SET processor_brand = 'dimensity'    ---- change the 'mediatek' processor brand name into 'dimensity'
	WHERE processor_brand = 'mediatek';

UPDATE emp_details
	SET emp_email = 'sophia123@hotmail.com', emp_nationality = 'Egyptian'  --- update in multiple column's data
	WHERE emp_fname = 'Sophia';

--- # DELETE --- permanent delete
DELETE FROM smartphones
	WHERE price > 400000;    --------- delete all the smartphone's data whose price are greater than 400000

DELETE FROM smartphones
	WHERE primary_camera_rear > 150 AND brand_name = 'samsung';   --- delete based on multiple condition

----## Some aggregate functions
---# MAX
SELECT MAX(price) FROM smartphones;  ---- only gives the value

SELECT * FROM smartphones     ----- get full details using subquery
WHERE price = (SELECT MAX(price) FROM smartphones);

SELECT MAX(price) FROM smartphones  --- find the samsung phone with highest price  --- this syntax only gives the values
WHERE brand_name = 'samsung';

SELECT * FROM smartphones    --- find the samsung phone with highest price  --- using subquery, this syntax gives full details
WHERE price = (SELECT MAX(price) FROM smartphones WHERE brand_name = 'samsung');

---# MIN
SELECT MIN(price) FROM smartphones;

---# AVG
SELECT AVG(rating) FROM smartphones  --- find the average rating of apple phone
WHERE brand_name = 'apple';

---# SUM
SELECT SUM(price) FROM smartphones   --- what would be the total cost if you want to buy all the 'poco' phones 
WHERE brand_name = 'poco';

---# COUNT
SELECT COUNT(brand_name) FROM smartphones   --- count the numbers of 'motorola' phones in the dataset
WHERE brand_name = 'motorola';

SELECT COUNT(*) FROM smartphones    --- same as above
WHERE brand_name = 'motorola';

---# COUNT(DISTINCT())  --- to count distinct values
SELECT COUNT(DISTINCT(brand_name)) FROM smartphones  --- find the number of distinct/unique phone brand names

---# STDDEV
SELECT STDDEV(screen_size) FROM smartphones   --- find out the standard deviation of screen_size of realme phone
WHERE brand_name = 'realme';

---# VAR_SAMP
SELECT VAR_SAMP(screen_size) FROM smartphones
WHERE brand_name = 'vivo';

---## Some scaler functions

---# ABS - make absolute -- means make positive
SELECT ABS (price - 100000) AS temp_price FROM smartphones;  --- make all the negative value to positive

---# ROUND --- 2.5-> 3 | 2.4-> 2
SELECT model,    
	ROUND(SQRT((resolution_width*resolution_width) + (resolution_height*resolution_height))/screen_size) AS ppi -- to make round figure
	FROM smartphones

SELECT model,
	ROUND(SQRT((resolution_width*resolution_width) + (resolution_height*resolution_height))/screen_size, 2) AS ppi -- round with two decimal places
	FROM smartphones

---# CEIL --- 2.1-> 3
SELECT model,
	CEIL(SQRT((resolution_width*resolution_width) + (resolution_height*resolution_height))/screen_size) AS ppi 
	FROM smartphones

---# FLOOR --- 2.9-> 2
SELECT model,
	FLOOR(SQRT((resolution_width*resolution_width) + (resolution_height*resolution_height))/screen_size) AS ppi 
	FROM smartphones

--------------------------------

---# ORDER BY --- for sorting
SELECT model, screen_size FROM smartphones -- sort in descending order according to screen size for samsung phone
	WHERE brand_name = 'samsung'
	ORDER BY screen_size DESC;

SELECT model, (num_rear_cameras + num_front_cameras) AS total_cameras FROM smartphones
	ORDER BY total_cameras DESC NULLS LAST;  -- to list null value at the last

SELECT brand_name, model, price FROM smartphones
	ORDER BY brand_name ASC , price DESC   -- sort on the basis of multiple columns

---# LIMIT --- to limit output like head() in pandas
SELECT model, screen_size FROM smartphones
	WHERE brand_name = 'samsung'
	ORDER BY screen_size DESC
	LIMIT 5;   ------------------- to show only top 5 smasung phones

SELECT model, battery_capacity FROM smartphones
	ORDER BY battery_capacity DESC NULLS LAST
	LIMIT 3 OFFSET 2  --- LIMIT 3 means numbers of rows to show, OFFSET 2 means starting from position 2. (starting position -- 0,1,2,... like index position)

---# LIKE / ILIKE
SELECT * FROM employees WHERE fname LIKE 'J%' ;     --- start
SELECT * FROM employees WHERE fname LIKE '%e' ;     --- end
SELECT * FROM employees WHERE fname LIKE '%i%' ;     --- contains
SELECT * FROM employees WHERE fname LIKE '%aura%' ;     --- contains
SELECT * FROM employees WHERE fname ILIKE '%Aura%' ;     --- contains - (case insensitive)
SELECT * FROM employees WHERE fname LIKE '_m%' ;     --- second character
SELECT * FROM employees WHERE dept LIKE '__' ;     --- two characters

----# GROUP BY ------
SELECT brand_name, COUNT(*) FROM smartphones ---Group smartphones by brand and get the number of phones 
	GROUP BY brand_name;

SELECT brand_name, processor_brand,
	COUNT(model) AS num_model,
	AVG(primary_camera_rear) AS avg_primary_camera_rear FROM smartphones
	GROUP BY brand_name, processor_brand;    ----- group by on multiple columns

---# HAVING - when we use any condition/filtering on Group BY, we use HAVING instead of WHERE
SELECT brand_name, COUNT(*) AS num_phone, AVG(price) AS avg_cost FROM smartphones
	GROUP BY brand_name
	HAVING COUNT(*) > 20  -- HAVING do not recognize column aliases, so we need to use original expression
	ORDER BY avg_cost DESC

SELECT brand_name, AVG(price) AS avg_cost FROM smartphones
	GROUP BY brand_name
	HAVING COUNT(*) > 20
	ORDER BY avg_cost DESC 

SELECT brand_name, AVG(price) AS avg_cost FROM smartphones
	GROUP BY brand_name
	HAVING COUNT(brand_name) > 20  -- same as above one
	ORDER BY avg_cost DESC

--- # GROUP BY ROLLUP --- to get the total of group by sum with the output at last/first
SELECT p_name, SUM(price) from billing_info
	GROUP BY ROLLUP(p_name)   
	ORDER BY SUM(price);

--- # COALESCE --- to replace all NULLs in a column, and set the given value there
SELECT COALESCE(p_name, 'Total'),
	SUM(price) from billing_info
	GROUP BY ROLLUP(p_name)
	ORDER BY SUM(price);

---------- String functions-----------
-- CONCAT, CONCAT_WS
-- SUBSTR
-- LEFT, RIGHT
-- LENGTH
-- UPPER, LOWER
-- TRIM, LTRIM, RTRIM
-- REPLACE
-- POSITION
-- STRING_AGG

---# CONCAT
--Syntax: CONCAT (first_col, second_col)        
--Syntax: CONCAT (first_word, second_word, ...)
SELECT CONCAT('Water', 'mellon');     --- normal string
SELECT CONCAT(fname, lname) FROM employees;    --- columns
SELECT CONCAT(fname,' ', lname) FROM employees;    --- add separator/string

---# CONCAT_WS - concat with seperator
-- Syntax:   CONCAT_WS('sep' , first , second, ...)
SELECT CONCAT_WS('#', 'Thank', 'you', 'very', 'much'); 
SELECT CONCAT_WS('-', fname, lname) AS fullname FROM employees;

--- # SUBSTR
--Syntax: SUBSTR('string'/column, start, end)   --- start from 1 not 0
SELECT SUBSTR('Hello buddy!',1,4)   --- normal string
SELECT SUBSTR('Hello buddy!',7,12)
SELECT SUBSTR(name,1,3) FROM marks  --- on column

--- # REPLACE
-- Syntax: REPLACE('str'  ,  from_str  , to_str)
SELECT REPLACE('Hello buddy!',  'Hello',  'Hey');    --- normal string
SELECT REPLACE(dept,  'IT',   'Tech dept.') FROM employees;    --- for column's string

--- # REVERSE
SELECT REVERSE ('Hello');    --- normal string
SELECT REVERSE (fname) FROM employees;    --- for column's string

--- # LENGTH
SELECT LENGTH ('Hello World');     --- for normal string
SELECT LENGTH (fname) FROM employees;    ------ for column's string

SELECT * FROM employees WHERE LENGTH(fname) = 5;    --- used in a condition

--- # UPPER & LOWER
SELECT UPPER ('Hello World');   --- for normal string
SELECT UPPER (fname) FROM employees;    --- for column's string

SELECT LOWER ('Hello World');   --- for normal string
SELECT LOWER (fname) FROM employees;   --- for column's string

--- # LEFT & RIGHT --- similar as SUBSTR but more flexible
SELECT LEFT('Hello world', 4);  

SELECT RIGHT('Hello world', 5);   

--- # TRIM -- remove the extra spaces 
SELECT TRIM ('   Bangladesh    ');   
SELECT TRIM (name) FROM employees;

SELECT LENGTH (TRIM ('   Bangladesh  '));    ----- we can use a function in another function

--- # POSITION
SELECT POSITION('om' IN 'Thomas');   

---# STRING_AGG - concatenates values from multiple rows into a single string, with a separator
--Syntax: STRING_AGG(expression, delimiter)
SELECT course, STRING_AGG(name, ', ') AS enrolled_students FROM students
GROUP BY course;

STRING_AGG(name, ', ' ORDER BY name)   --- we can use ORDER BY inside STRING_AGG function
-----

---# CASE Expreesion/Statement -- like if,else condition
SELECT fname, salary, hire_date,
CASE
	WHEN salary >= 60000 THEN 'High'
	WHEN salary >= 50000 AND salary <60000 THEN 'Mid'
	ELSE 'Low'
END AS sal_cat
FROM employees;

--Task: Fetch the salary bonus according to employees salary, where bouns is 10% of their salary.
SELECT fname,salary,
CASE
	WHEN salary >0 THEN ROUND(salary*.10)
END AS bonus
FROM employees;

---# VIEW --- To save the query to view for later --- it will be stored as a table(view) ( not as normal table)
CREATE VIEW billing_info AS  --- here we save the query as 'billing_info' 
SELECT 
	c.cust_name,
	o.ord_date,
	p.p_name,
	p.price,
	oi.quantity,
	(oi.quantity*p.price) AS total_price
FROM order_items oi
	JOIN products p 
        ON oi.p_id=p.p_id
	JOIN orders o 
        ON o.ord_id=oi.ord_id
	JOIN customers c 
        ON o.cust_id=c.cust_id;

SELECT * FROM billing_info    --- now we can see the table(view) as like as normal table

----## Joins in tables ---
---# Types of join:
-- 1. CROSS JOIN - all possible combinations between two tables
-- 2. INNER JOIN/JOIN - only retrieve the common things  --- Most important
-- 3. LEFT JOIN - retrieve full left table + common things between two tables
-- 4. RIGHT JOIN - retrieve full right table + common things between two tables
-- 5. FULL OUTER JOIN - retrieve full left and full right table
-- 6. *Self join (special case) - when a table is joined with itself to compare or to find hierarchical or relational data within the same table.

---# CROSS JOIN
SELECT * FROM employees e -- there are 5 rows       --- so after the cross join it become (5*4)= 20 rows
CROSS JOIN departments d;  -- there are 4 rows  

SELECT e.emp_name, d.dept_name FROM employees e
CROSS JOIN departments d;

---# INNER JOIN/JOIN
SELECT * FROM employees e
INNER JOIN departments d 
	ON e.dept_id = d.dept_id;

---# LEFT JOIN
SELECT * FROM employees e
LEFT JOIN departments d 
	ON e.dept_id = d.dept_id;

SELECT * FROM students s   --- Find out HOD of the students considering year
LEFT JOIN class c 
	ON s.class_id = c.class_id AND s.enrollment_year = c.class_year;  --- on the basis of multiple columns

---# RIGHT JOIN
SELECT * FROM employees e
RIGHT JOIN departments d 
	ON e.dept_id = d.dept_id;

---# FULL OUTER JOIN
SELECT * FROM employees e
FULL OUTER JOIN departments d
	ON e.dept_id = d.dept_id;

---# *Self join - (special case)
SELECT t1.name, t2.name AS guardian FROM users t1
INNER JOIN users t2
	ON t1.emergency_contact = t2.user_id

----## Joining more than 2 tables
SELECT * FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id;

SELECT s.student_name, c.course_name FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id;

----## Filtering after joining - Find all the orders placed in pune
SELECT * FROM customers c
JOIN orders o
	ON c.user_id = o.user_id
WHERE c.city = 'Pune'

---# UNION -- join/append two same structure(column) table and remove duplicates
SELECT * FROM person1
UNION
SELECT * FROM person2

---# UNION ALL -- join/append two same structure(column) table and do not remove duplicates
SELECT * FROM person1
UNION ALL
SELECT * FROM person2

---# INTERSECT -- only keeps commons
SELECT * FROM person1
INTERSECT
SELECT * FROM person2

---# EXCEPT -- similar as set difference
SELECT * FROM person1
EXCEPT
SELECT * FROM person2

---------------

---## Subquery

-- Task: Find the movie with highest reating using subquery
SELECT * FROM movies
WHERE score = (SELECT MAX(score) FROM movies) --- here it is, now it can be used as a dynamic logic

---# Types of Subqueries:  
--		Based on:
--			1. The result it returns (3 Types)
--				1.1 Scaler subquery
--				1.2 Row subquery (single column)
--				1.3 Table subquery
--			2. Working (2 Types)
--				2.1 Independed subquery
--				2.2 Co-related subquery

------ Now solve some tasks using subquery ---------

----# Independent-scaler subquery

--Find the movie with highest profit (vs order by)
SELECT * FROM movies
WHERE (gross - budget) = (SELECT MAX(gross - budget) FROM movies)

--Find how many movies have a rating > the avg of all the movie ratings (Find the count of above average movies)
SELECT COUNT(*) FROM movies
WHERE score > (SELECT AVG(score) FROM movies)

--Find the highest rated movie of 2000
SELECT * FROM movies
WHERE year = 2000 AND score = (SELECT MAX(score) FROM movies
                               WHERE year = 2000)

--Find the highest rated movie among all movies whose number of votes are > the dataset avg votes
SELECT * FROM (SELECT * FROM movies
				WHERE votes > (SELECT AVG(votes) FROM movies))
WHERE votes = (SELECT MAX(votes) FROM (SELECT * FROM movies
										WHERE votes > (SELECT AVG(votes) FROM movies)))

---# Independent-row subquery(single column & multiple rows)

--Find all users who never ordered
SELECT * FROM (SELECT * FROM users u
				LEFT JOIN orders o
					ON u.user_id = o.user_id)
WHERE order_id IS NULL

--Find all the movies made by top 3 directors (in terms of total gross income)
SELECT * FROM movies
WHERE director IN (SELECT director FROM movies
					GROUP BY director
					ORDER BY SUM(gross) DESC NULLS LAST 
					LIMIT 3)

--Find all movies of all those actors whose filmography's avg rating > 8.5 -(take 25000 votes as cutoff for filtering actors)
SELECT * FROM movies
WHERE star IN (SELECT star  FROM movies
				WHERE votes > 25000
				GROUP BY star
				HAVING AVG(score) >8.5 )

---# Independent-table subquery(multiple columns & single/multiple rows)

--Find the most profitable movie of each year
SELECT * FROM movies
WHERE (year,(gross - budget)) IN (SELECT year, MAX(gross - budget) AS max_profit FROM movies
									GROUP BY year)


--Find the highest rated movie of each genre votes cutoff of 25000
SELECT * FROM movies
WHERE (genre,score) IN (SELECT genre, MAX(score) FROM movies
							WHERE votes > 25000
							GROUP BY genre)
	AND votes > 25000

---# Corelated subquery - here, inner query depended on outer query

--Find all the movies that have a rating higher than the average rating of movies in the same genre.
SELECT * FROM movies m1
WHERE score > (SELECT AVG(score) FROM movies m2 WHERE m2.genre = m1.genre)

--Find the favorite food of each customer.
WITH fav_food AS (      --- CTE  
    SELECT 
        o.user_id, 
        u.name, 
        f.f_name, 
        COUNT(*) AS frequency 
    FROM users u
    JOIN orders o ON u.user_id = o.user_id
    JOIN order_details od ON o.order_id = od.order_id
    JOIN food f ON od.f_id = f.f_id
    GROUP BY o.user_id, u.name, od.f_id, f.f_name
)
SELECT * FROM fav_food ff1
WHERE frequency = (SELECT MAX(frequency) FROM fav_food ff2 WHERE ff2.user_id = ff1.user_id)

---# Subquries can be used with:
--		1. SELECT (WHERE, SELECT, FROM, HAVING)
--		2. INSERT
--		3. UPDATE
--		4. DELETE

---# Usage with 'SELECT'
--Get the percentage of votes for each movie compared to the total number of votes.
SELECT name, (100*votes/(SELECT SUM(votes) FROM movies)) AS percentage FROM movies

--Display all movie names, genre, score and avg(score) of genre
SELECT name,genre,score,(SELECT AVG(score) FROM movies m2 WHERE m2.genre = m1.genre) AS avg_gs FROM movies m1

---# Usage with 'FROM'
--Display average rating of all the restaurants
SELECT r_name, AVG(restaurant_rating) AS avg_rr FROM (SELECT * FROM restaurants r
														LEFT JOIN orders o
														ON r.r_id = o.r_id)
GROUP BY r_name

---# Usage with 'WHERE' --- we did this in the different above tasks

---# Usage with 'HAVING'
--Find the genres having average score > average score of the all movies
SELECT genre, AVG(score) FROM movies
GROUP BY genre
HAVING AVG(score) > (SELECT AVG(score) FROM movies)

---# Usage with 'INSERT'
--Create a table called 'loyal_customers' with columns called user_id, name, total_orders, discount_money and insert data into the table of those users who ordered food more than 3 times
INSERT INTO loyal_customers(user_id, name, total_orders)
SELECT o.user_id, u.name, COUNT(o.user_id) AS total_orders  FROM orders o
JOIN users u
	ON o.user_id = u.user_id
GROUP BY o.user_id, u.name
HAVING COUNT(o.user_id) > 3

---# Usage with 'UPDATE'
--Populate the discount_money col of loyal_customer table using the orders table. Provide a 10% app money to all customers based on their total order value
UPDATE loyal_customers
SET discount_money = (SELECT SUM(o.amount) * 0.10 FROM orders o
 	 					 WHERE o.user_id = loyal_customers.user_id)

---# Usage with 'DELETE'
--Delete all the customers records who have never ordered
DELETE FROM users
WHERE user_id IN (SELECT user_id FROM users
					WHERE user_id NOT IN (SELECT DISTINCT(user_id) FROM orders))

------ Stored Routine --------
-- 1. Stored Procedure
-- 2. User Defined Function

---## Stored Procedure -- to save SQL query statement in a simple form for later use (like create a function and call)
--- # PROCEDURE
--Example: To update existing employee salary
CREATE OR REPLACE PROCEDURE update_emp_salary(p_emp_id INT, p_new_salary NUMERIC)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE employees                   --
    SET salary = p_new_salary          -- procedural code here
    WHERE emp_id = p_emp_id;           --
END;
$$;

CALL update_emp_salary(3, 80000)   --- to call the stored procedure and do operation

-- Another Example: To add employee in the table
CREATE OR REPLACE PROCEDURE add_employee(
    p_fname VARCHAR,
    p_lname VARCHAR,
    p_email VARCHAR,
    p_dept VARCHAR,
    p_salary NUMERIC,
	p_hire_date DATE
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO employees (fname, lname, email, dept, salary, hire_date)
    VALUES (p_fname, p_lname, p_email, p_dept, p_salary, p_hire_date);
END;
$$;

CALL add_employee('Nitol','Siddique','nitol123@gmail.com','Management', 77000, '2025-01-11')

---## User Defined Function --- similar as Stored procedure but little different
---# FUNCTION
-- Example: Create a function to find maximum salary paying employee in any dept
CREATE OR REPLACE FUNCTION dept_max_sal_emp(dept_name VARCHAR)   
RETURNS TABLE(emp_id INT, fname VARCHAR, salary NUMERIC)
AS $$
BEGIN
  RETURN QUERY
  SELECT e.emp_id, e.fname, e.salary FROM employees e
  WHERE e.dept = dept_name AND e.salary = (SELECT MAX(emp.salary) FROM employees emp
                                           WHERE emp.dept = dept_name);
END;
$$ LANGUAGE plpgsql;

SELECT * FROM dept_max_sal_emp('HR');  --- calling the function

---# CTE - Common Table Expression ---
--Example: Fetch the employees who get more than average salaries in their particular department
WITH dept_avg_sal AS (SELECT dept, AVG(salary) AS avg_salary FROM employees
                 GROUP BY dept)
 -- Main query referencing the CTE
SELECT e.emp_id, e.fname, e.dept, e.salary, da.avg_salary
FROM employees e
JOIN dept_avg_sal da
    ON e.dept = da.dept
WHERE
    e.salary > da.avg_salary;

---# TRIGGER ---
-- It is a special procedures in a database that automatically execute predefined actions in response to certain events on a table or view.
--Syntax:
CREATE OR REPLACE FUNCTION trigger_function_name()   --- create function for trigger
RETURNS TRIGGER AS $$
BEGIN
    -- Trigger logic here
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_name    --- this is the main syntax for TRIGGER
{ BEFORE | AFTER | INSTEAD OF } { INSERT | UPDATE | DELETE | TRUNCATE }
ON table_name
FOR EACH { ROW | STATEMENT }
EXECUTE FUNCTION trigger_function_name();

-- Example: create a trigger that will convert negative value into '0' if we insert/update any negative value in salary in employees table
CREATE OR REPLACE FUNCTION check_salary()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.salary < 0 THEN NEW.salary = 0;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER before_update_salary
BEFORE UPDATE ON employees
FOR EACH ROW
EXECUTE FUNCTION check_salary();

-------## Window Functions--------

--- #Some frame secifications
--1. ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW: means that the frame includes all rows from the beginning of the partition up to and including the current row.
--2. ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING: the frame includes the current row and the row immediately before and after it.
--3. ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING: the frame includes all rows in the partition.
--4. ROWS BETWEEN 3 PRECEDING AND 2 FOLLOWING: the frame includes the current row and the three rows before it and the two rows after it.

---# Usage with Aggregate functions
SELECT AVG(marks) OVER() FROM marks  --- give multiple rows of average marks

SELECT *, AVG(marks) OVER() FROM marks --- give multiple rows of average marks with 'all'

SELECT *, AVG(marks) OVER(PARTITION BY branch) FROM marks -- now it works like group by on the basis of branch but gives the average of marks according to the branch to every row
ORDER BY student_id -- to get rid from self ordering

SELECT *, 
MIN(marks) OVER(),  -- gives min marks in every row
MAX(marks) OVER(),
MIN(marks) OVER(PARTITION BY branch) AS min_br, -- gives min marks in every row according to their branch
MAX(marks) OVER(PARTITION BY branch) AS max_br
FROM marks

--Find all the students who have marks higher than the average marks of their respective branch
SELECT * FROM(SELECT *, 
				AVG(marks) OVER(PARTITION BY branch) AS avg_br
				FROM marks) t
WHERE t.marks > t.avg_br

----# RANK/DENSE_RANK/ROW_NUMBER -- Window functions

---# RANK - [1,1,3]
SELECT *, 
RANK() OVER(ORDER BY marks DESC) FROM marks  -- ranking students according to their marks

SELECT *, 
RANK() OVER(PARTITION BY branch ORDER BY marks DESC) FROM marks --ranking students according to their marks on the basis of their respective branch

---# DENSE_RANK -- same as RANK , just only [1,1,2]
SELECT *, 
DENSE_RANK() OVER(PARTITION BY branch ORDER BY marks DESC) FROM marks --ranking students according to their marks on the basis of their respective branch

SELECT * FROM (SELECT "BattingTeam", batter, -- Find and rank the top 5 batsman of each ipl team according to their total runs
				SUM(batsman_run) AS total_run,
				DENSE_RANK() OVER(PARTITION BY "BattingTeam" ORDER BY SUM(batsman_run) DESC ) AS rank_in_team FROM ipl
				GROUP BY "BattingTeam", batter) t
WHERE t.rank_in_team < 6
ORDER BY T."BattingTeam", rank_in_team

---# ROW_NUMBER -- Assigns row number for every rows
SELECT *, 
ROW_NUMBER() OVER()  -- assign row number to all rows in the table
FROM marks

SELECT *, 
ROW_NUMBER() OVER(PARTITION BY branch) -- assign row number to all rows according to their respective branch
FROM marks

SELECT *, 
CONCAT(branch, '-', ROW_NUMBER() OVER(PARTITION BY branch)) AS roll -- assigning a column called 'roll' where roll like this: CSE-1
FROM marks
------
-- Find out the top 2 customers of every month who spent most amount of money
SELECT * FROM(SELECT 
			  user_id, 
			  TO_CHAR(date, 'FMMonth') AS month_name,
			  EXTRACT(MONTH FROM date) AS month_number,
			  SUM(amount) AS amount,
			  RANK() OVER(PARTITION BY TO_CHAR(date, 'FMMonth') ORDER BY SUM(amount) DESC) AS rank
		      FROM orders
		      GROUP BY user_id, month_number, month_name
		      ORDER BY month_number) t
WHERE t.rank < 3
ORDER BY t.month_number ASC, t.rank ASC

---## FIRST_VALUE/LAST_VALUE/NTH_VALUE -- Window functions
---## There may be issues occur related to 'frame' when we use these function
------To git rid from the issues, we use- 'ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING' clause

---# FIRST_VALUE
SELECT *, 
FIRST_VALUE(name) OVER( ORDER BY marks DESC  -- assign the topper name with every rows
			            ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
FROM marks

SELECT *, 
FIRST_VALUE(name) OVER(PARTITION BY branch ORDER BY marks DESC -- assign the topper name with every rows according to their respective branch
			            ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
FROM marks

---# LAST_VALUE
SELECT *, 
LAST_VALUE(name) OVER(ORDER BY marks DESC -- assign the Lowest scorer name with every rows
					   ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) 
FROM marks

---# NTH_VALUE(column,n)
SELECT *, 
NTH_VALUE(name,5) OVER(ORDER BY marks DESC -- assign the 5th topper name with every rows
					   ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) 
FROM marks

SELECT *, 
NTH_VALUE(name,2) OVER(ORDER BY marks ASC -- assign the 2nd lowest scorer name with every rows
					   ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) 
FROM marks
------

-- Find toppers of thier respective branch
SELECT name, branch, marks 
FROM (
    SELECT *, 
        FIRST_VALUE(name) OVER(PARTITION BY branch ORDER BY marks DESC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS topper_name,
        FIRST_VALUE(marks) OVER(PARTITION BY branch ORDER BY marks DESC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS topper_marks
    FROM marks
) t
WHERE t.name = t.topper_name AND t.marks = t.topper_marks;

---## LEAD/LAG Window functions

---# LEAD -- assign a leading column
SELECT *, 
	LEAD(marks) OVER(ORDER BY student_id)
FROM marks

---# LAG -- assign a lagging column 
SELECT *, 
	LAG(marks) OVER(ORDER BY student_id)
FROM marks

SELECT *, 
	LAG(youtube_views,7) OVER(ORDER BY EXTRACT(YEAR FROM date), TO_CHAR(date, 'Month')) -- lag down to 7 rows
FROM youtube

---

--Find the Month-on-Month revenue growth of Zomato
SELECT 
    TO_CHAR(date, 'Month') AS month_name,
    SUM(amount) AS total_amount,
    SUM(amount) - LAG(SUM(amount)) OVER (ORDER BY EXTRACT(MONTH FROM date)) AS growth
FROM orders
GROUP BY EXTRACT(MONTH FROM date), TO_CHAR(date, 'Month')
ORDER BY EXTRACT(MONTH FROM date);

---# Cumulative sum & Cumulative average
-- Find out the V Kohli's carrier runs and average carrier runs after 50th match and 100th match
SELECT * FROM (SELECT ROW_NUMBER() OVER(ORDER BY "ID") AS match_no,
				SUM(batsman_run) AS total_runs,
				SUM(SUM(batsman_run)) OVER(ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS carrier_runs, -- cumulative sum
				AVG(SUM(batsman_run)) OVER(ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS avg_carrier_runs -- cumulative average
				FROM ipl
				WHERE batter = 'V Kohli'
				GROUP BY "ID")
WHERE match_no = 50 OR match_no = 100

SELECT * FROM (SELECT ROW_NUMBER() OVER(ORDER BY "ID") AS match_no, -- alternatively
				SUM(batsman_run) AS total_runs,
				SUM(SUM(batsman_run)) OVER w AS carrier_runs, -- from here 
				AVG(SUM(batsman_run)) OVER w AS avg_carrier_runs -- from here
				FROM ipl
				WHERE batter = 'V Kohli'
				GROUP BY "ID"
				WINDOW w AS (ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)) -- here set the over clause to get rid from repeatative work
WHERE match_no = 50 OR match_no = 100

---# Running average/Rolling average
--Find V Kohli's 10 matches running average in his entire carrier --- to find out V Kohli's form 
SELECT * FROM (SELECT ROW_NUMBER() OVER(ORDER BY "ID") AS match_no,
				SUM(batsman_run) AS total_runs,
				SUM(SUM(batsman_run)) OVER(ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS carrier_runs, -- cumulative sum
				AVG(SUM(batsman_run)) OVER(ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS avg_carrier_runs, -- cumulative average
				AVG(SUM(batsman_run)) OVER(ROWS BETWEEN 9 PRECEDING AND CURRENT ROW) AS avg_runs_last_10_matches -- running/rolling average
				FROM ipl
				WHERE batter = 'V Kohli'
				GROUP BY "ID")

---# Percent of total
--Find out the percent of total sales for each food in a particular restaurant(dominos)
SELECT f_name,(total_amount/SUM(total_amount) OVER ())*100 AS percent_of_total
	  FROM(SELECT f_name, SUM(amount) AS total_amount FROM orders o
	  JOIN order_details od
	  ON o.order_id = od.order_id
	  JOIN restaurants r
	  ON o.r_id = r.r_id
	  JOIN food f
	  ON od.f_id = f.f_id
      WHERE r_name = 'dominos'
	  GROUP BY f_name)

---# Percent change 
-- percent change = ((new value - old value)/old value)*100
SELECT EXTRACT(YEAR FROM date) AS year,
TO_CHAR(date, 'Month') AS month,
SUM(youtube_views) total_views,
((SUM(youtube_views)- LAG(SUM(youtube_views)) OVER(ORDER BY EXTRACT(YEAR FROM date), TO_CHAR(date, 'Month')))/LAG(SUM(youtube_views)) OVER(ORDER BY EXTRACT(YEAR FROM date), TO_CHAR(date, 'Month')))*100 AS percentage_change
FROM youtube
GROUP BY year, month
ORDER BY year, month

---# Percentile & Quantile(n number of equal intervals)
--Find the median marks of all the students
SELECT *,
  (SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY marks) -- Discrete percentile value; eg. [1,2,3,4,4,5] median of disc. percentile = 3 or 4
   FROM marks) AS median_marks
FROM marks
----
SELECT *,
  (SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY marks) -- Continuous percentile value; eg. [1,2,3,4,4,5] median of cont. percentile = (3+4)/2= 3.5
   FROM marks) AS median_marks
FROM marks

--Find branch wise median of students marks
SELECT *,
  (SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY marks)
   FROM marks m2 
   WHERE m2.branch = m1.branch) AS median_marks
FROM marks m1

---# Removing outliers - using quartile and inter-quartile
SELECT * FROM (SELECT *,
              (SELECT PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY marks) FROM marks) AS q1,
              (SELECT PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY marks) FROM marks) AS q3
	           FROM marks) 
WHERE marks > (q1 - (1.5*(q3-q1))) AND marks < (q3 + (1.5*(q3-q1))) -- here we remove minimum - <<have confusion>>
ORDER BY student_id

---# Segmentation - using NTILE
SELECT *,
	NTILE(3) OVER(ORDER BY marks DESC) AS buckets
FROM marks

--Seperate the phone type in three categories(premium, moderate, affordable) according to their prices
SELECT *,
CASE     -- case statement - like if,else condition
	WHEN bucket = 1 THEN 'premium'
	WHEN bucket = 2 THEN 'moderate'
	WHEN bucket = 3 THEN 'affordable'
END AS phone_type
FROM(SELECT brand_name, model , price,
	 NTILE(3) OVER(ORDER BY price DESC) AS bucket
	 FROM smartphones)

---# Cumulative distribution
--Find out the percentile score of students
SELECT *,
CUME_DIST() OVER(ORDER BY marks) AS percentile_score
FROM marks

---# Partition by multiple columns
--Rank the match(ID) between batter and bowler on the basis of batter's total runs against the bowler on that particular match
SELECT "ID",
batter,
bowler,
SUM(batsman_run) AS total_runs_against_bowler,
DENSE_RANK() OVER(PARTITION BY batter, bowler ORDER BY SUM(batsman_run) DESC) AS rank
FROM ipl
GROUP BY "ID",batter, bowler


