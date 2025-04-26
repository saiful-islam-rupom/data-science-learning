-------------------------------------------- Practice ------------------------------------------------------

--###--- Tasks on smartphone dataset
-- Task1: Find the average battery capacity and the average primary rear camera resolution for all smartphones
        -- with a price greater than or equal to 100000
SELECT AVG(battery_capacity), AVG(primary_camera_rear) FROM smartphones  
    WHERE price >= 100000;

-- Task2: Find the average internal memory capacity of smartphones that have a refresh rate of 120 Hz or higher 
       -- and a front-facing camera resolution greater than or equal to 20 megapixels.
SELECT AVG(internal_memory) FROM smartphones  
    WHERE refresh_rate >= 120 AND primary_camera_front >= 20 ;

-- Task3: Find the number of smartphones with 5G capability
SELECT COUNT(*) FROM smartphones  
    WHERE has_5g = 'true' ;

----- tasks on sorting -----

-- Task4: Sort all the phones in descending order according to their total number of cameras 
SELECT model, (num_rear_cameras + num_front_cameras) AS total_cameras FROM smartphones
	ORDER BY total_cameras DESC NULLS LAST;

-- Task5: Sort data on the basis of ppi in decreasing order
SELECT model, SQRT((resolution_width*resolution_width) + (resolution_height*resolution_height))/screen_size AS ppi FROM smartphones
		ORDER BY ppi DESC

-- Task6: Find the phones with second largest battery
SELECT model, battery_capacity FROM smartphones
	ORDER BY battery_capacity DESC NULLS LAST
	LIMIT 1 OFFSET 1

-- Task7: Find the name and rating of the wrost rated apple phone
SELECT model, rating FROM smartphones
	WHERE brand_name = 'apple'
	ORDER BY rating ASC
	LIMIT 1;

-- Task8: Sort phones alphabetically and then on the basis of rating in descending order
SELECT brand_name, model, price FROM smartphones
	ORDER BY brand_name ASC , rating DESC

-- Task9: Sort phones alphabetically and then on the basis of price in ascending order
SELECT brand_name, model, price FROM smartphones
	ORDER BY brand_name ASC , price ASC

------ tasks on group by --------

-- Task10: Group smartphones by brand and get the count, average price, max rating, avg screen size and avg battery capacity
SELECT brand_name,
	COUNT(*) AS num_phones,
	AVG(price) AS avg_price,
	MAX(rating) AS max_rating,
	AVG(screen_size) AS avg_screen,
	AVG(battery_capacity) AS avg_battery FROM smartphones
	GROUP BY brand_name;

-- Task11: Group Smartphones by whether they have an NFC and get the average price and rating
SELECT has_nfc,
	AVG(price) AS avg_price,
	AVG(rating) AS avg_rating FROM smartphones    -- for both phones whether they have nfc or not
	GROUP BY has_nfc;

SELECT has_nfc,
	AVG(price) AS avg_price,
	AVG(rating) AS avg_rating FROM smartphones  -- for those phones only which has nfc
	WHERE has_nfc = 'true'
	GROUP BY has_nfc;

-- Task12: Group smartphones by the extended memory available and get the average price
SELECT extended_memory_available, AVG(price) AS avg_price FROM smartphones
	GROUP BY extended_memory_available;

-- Task13: Group smartphones by the brand and processor brand and get the count of models and the average primary camera resolution (rear)
SELECT brand_name, processor_brand,
	COUNT(model) AS num_model,
	AVG(primary_camera_rear) AS avg_primary_camera_rear FROM smartphones
	GROUP BY brand_name, processor_brand;

-- Task14:Find top 5 most costly phone brands
SELECT brand_name, ROUND(AVG(price)) AS costs FROM smartphones
	GROUP BY brand_name 
	ORDER BY costs DESC
	LIMIT 5;

-- Task15: Which brand makes the smallest screen smartphones
SELECT brand_name, MIN(screen_size) AS min_screen_size FROM smartphones
	GROUP BY brand_name 
	ORDER BY min_screen_size ASC
	LIMIT 1;

-- Task16: Avg price of 5g phones vs avg price of non 5g phones
SELECT has_5g, AVG(price) AS avg_price FROM smartphones
	GROUP BY has_5g;

-- Task17: Group smartphones by the brand, and find the brand with the highest number of models that have both NFC and an IR blaster
SELECT brand_name, COUNT(model) AS num_model FROM smartphones
	WHERE has_nfc = 'true' AND has_ir_blaster = 'true'
	GROUP BY brand_name
	ORDER BY num_model DESC
	LIMIT 1;

-- Task18: Find all samsung 5g enabled smartphones and find out the avg price for NFC and Non-NFC phones
SELECT has_nfc, AVG(price) AS avg_price FROM smartphones
	WHERE brand_name = 'samsung' AND has_5g = 'true'
	GROUP BY has_nfc

-- Task19: Find the phone name, price of the costliest phone
SELECT model, price FROM smartphones
	WHERE price = (SELECT MAX(price) FROM smartphones)

-------- tasks on having ----------

-- Task20: Find the avg rating of smartphone brands which have more than 20 phones
SELECT brand_name, AVG(rating) AS avg_rating FROM smartphones
	GROUP BY brand_name
	HAVING COUNT(*) > 20
	
-- Task21: Find the top 3 brands with the highest avg ram that have a refresh rate of at least 90 Hz and fast charging available and don’t consider brands which have less than 10 phones
SELECT brand_name, AVG(ram_capacity) AS avg_ram FROM smartphones
	WHERE refresh_rate >= 90 AND fast_charging_available = 'true'
	GROUP BY brand_name
	HAVING COUNT(*) >= 10
	ORDER BY avg_ram DESC
	LIMIT 3;

-- Task22: Find the avg price of all the phone brands with avg rating > 70 and num_phones more than 10 among all 5g enabled phones
SELECT brand_name, AVG(rating) AS avg_rating FROM smartphones
	WHERE has_5g = 'true' 
	GROUP BY brand_name
	HAVING COUNT(*) > 10 AND AVG(rating) > 70


--### -- Tasks on insurance dataset

-- Task1. Show records of 'male' patient from 'southwest' region.
SELECT * FROM insurance
	WHERE gender = 'male' AND region = 'southwest'

-- Task2. Show all records having bmi in range 30 to 45 both inclusive.
SELECT * FROM insurance
	WHERE bmi BETWEEN 30 AND 45

-- Task3. Show minimum and maximum bloodpressure of diabetic patient who smokes. Make column names as MinBP and MaxBP respectively.
SELECT MIN(bloodpressure) AS minbp, MAX(bloodpressure) AS maxbp FROM insurance
	WHERE smoker = 'true'

-- Task4. Find no of unique patients who are not from southwest region.
SELECT COUNT(DISTINCT "PatientID") FROM insurance
	WHERE region NOT IN('southwest')

-- Task5. Total claim amount from male smoker.
SELECT SUM(claim) FROM insurance
	WHERE gender = 'male' AND smoker = 'true'

-- Task6. Select all records of south region.
SELECT * FROM insurance
	WHERE region IN ('southeast', 'southwest')

-- Task7. No of patient having normal blood pressure. Normal range[90-120]
SELECT COUNT(*) FROM insurance
	WHERE bloodpressure BETWEEN 90 AND 120

-- Task8. No of pateint below 17 years of age having normal blood pressure as per below formula -
    -- BP normal range = 80+(age in years × 2) to 100 + (age in years × 2)
SELECT COUNT(*) FROM insurance
	WHERE age < 17 AND bloodpressure BETWEEN (80+(age * 2)) AND (100 + (age * 2))

-- Task9. What is the average claim amount for non-smoking female patients who are diabetic?
SELECT AVG(claim) FROM insurance
	WHERE gender = 'female' AND smoker = 'false' AND diabetic = 'true'

-- Task10. Write a SQL query to update the claim amount for the patient with PatientID = 1234 to 5000.
UPDATE insurance
	SET "PatientID" = 5000
	WHERE "PatientID" = 1234

-- Task11. Write a SQL query to delete all records for patients who are smokers and have no children.
DELETE FROM insurance
	WHERE smoker = 'true' AND children = 0;


---###-- Tasks on ipl dataset

-- Task1: Find the top 5 batsman in IPL
SELECT batter, SUM(batsman_run) AS total_run FROM ipl
	GROUP BY batter
	ORDER BY total_run DESC
	LIMIT 5

-- Task2: Find the 2nd highest 6 hitter in IPL
SELECT batter, COUNT(batsman_run) AS sixers FROM ipl
	WHERE batsman_run = 6
	GROUP BY batter
	ORDER BY sixers DESC
	LIMIT 1 OFFSET 1

-- Task3: Find top 10 batsman with centuries in IPL
SELECT batter, COUNT(*) AS num_century
FROM (
    SELECT "ID", batter, SUM(batsman_run) AS total_run
    FROM ipl
    GROUP BY "ID", batter
    HAVING SUM(batsman_run) >= 100
) AS centuries
GROUP BY batter
ORDER BY num_century DESC
LIMIT 10;

-- Task4: Find the top 5 batsman with highest strike rate who have played a min of 1000 balls
SELECT batter,
	SUM(batsman_run) ,
	COUNT(batsman_run), 
	ROUND(SUM(batsman_run)/COUNT(batsman_run)*100,2) AS strike_rate FROM ipl
    GROUP BY batter
    HAVING COUNT(batsman_run) >= 1000
	ORDER BY strike_rate DESC
	LIMIT 5

-------# Tasks on joining ----- from Datasets_for_Joins folder

-- Task1: Find order_id , name , city by joining customers and orders
SELECT o.order_id, c.name, c.city FROM customers c
JOIN orders o
	ON c.user_id = o.user_id

-- Task2: Find order_id and product category by joining order_details and category
SELECT od.order_id, c.category FROM order_details od
JOIN category c
	ON od.category_id = c.category_id

-- Task3: Find all the orders placed in pune
SELECT * FROM customers c
JOIN orders o
	ON c.user_id = o.user_id
WHERE c.city = 'Pune'

-- Task4: Find all profitable orders
SELECT order_id, SUM(profit) AS total_profit FROM order_details
GROUP BY order_id
HAVING SUM(profit) > 0 ;

-- Task5: Find the customer who has placed max number of orders
SELECT c.name,COUNT(*) FROM customers c
JOIN orders o
	ON c.user_id = o.user_id
GROUP BY c.name 
ORDER BY COUNT(*) DESC
LIMIT 1

-- Task6: Which is the most profitable category(vertical)
SELECT c.vertical, SUM(od.profit) AS profits FROM order_details od
JOIN category c
	ON od.category_id = c.category_id
GROUP BY c.vertical 
ORDER BY profits DESC
LIMIT 1

-- Task7: Which are the top 5 most profitable states
SELECT c.state, SUM(od.profit) AS total_st_profit FROM customers c
JOIN orders o
	ON c.user_id = o.user_id
JOIN order_details od
	ON o.order_id = od.order_id
GROUP BY c.state 
ORDER BY total_st_profit DESC
LIMIT 5

-- Task8: Find all categories with profit higher than 2000
SELECT c.vertical, SUM(od.profit) AS profits FROM order_details od
JOIN category c
	ON od.category_id = c.category_id
GROUP BY c.vertical
HAVING SUM(od.profit) > 2000


--- ## Sleep Efficiency Dataset ----
--- ## For questions 1-5, you can find the dataset and details about it from [here](https://www.kaggle.com/datasets/equilibriumm/sleep-efficiency).

-- Task1: Find out the average sleep duration of top 15 male candidates who's sleep duration are equal to 7.5 or greater than 7.5.
SELECT AVG(sleep_duration) AS avg_sd FROM(
	SELECT *  FROM sleepef
	WHERE gender = 'Male' AND sleep_duration >= 7.5
	ORDER BY sleep_duration DESC
	LIMIT 15)

-- Task2: Show avg deep sleep time for both gender. Round result at 2 decimal places.
SELECT gender, AVG(deep_sleep_percentage)AS avg_deep_sleep_p, ROUND(AVG(sleep_duration*(deep_sleep_percentage/100)), 2) AS avd_deep_sleep_t FROM sleepef
	GROUP BY gender

-- Task3: Find out the lowest 10th to 30th light sleep percentage records where deep sleep percentage values are between 25 to 45. Display age, light sleep percentage and deep sleep percentage columns only.
SELECT age, light_sleep_percentage , deep_sleep_percentage FROM sleepef
	WHERE deep_sleep_percentage BETWEEN 25 AND 45
	ORDER BY light_sleep_percentage ASC
	LIMIT 21 OFFSET 9
