-- Solution: Data Cleaning and Deduplication
SELECT COUNT(*) AS missing_email_customers
FROM customers
WHERE email IS NULL;

SELECT customer_id, email, COUNT(*) AS duplicate_count
FROM customer_email_history
WHERE email IS NOT NULL
GROUP BY customer_id, email
HAVING COUNT(*) > 1;

SELECT customer_id, first_name, last_name, city, region
FROM customers
WHERE city IS NULL OR region IS NULL;

SELECT customer_id,
       COALESCE(email, 'missing_email') AS normalized_email
FROM customers;

SELECT customer_id,
       first_name,
       last_name,
       email,
       region,
       CASE
           WHEN email IS NULL THEN 'missing_email'
           WHEN region IS NULL THEN 'missing_region'
           ELSE 'complete'
       END AS record_status
FROM customers;
