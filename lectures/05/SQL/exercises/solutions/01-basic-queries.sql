-- Solution: Basic Queries
SELECT customer_id, first_name, last_name, email
FROM customers;

SELECT customer_id, first_name, last_name, email
FROM customers
WHERE is_active = 1 AND region = 'West';

SELECT order_id, customer_id, order_date, total_amount
FROM orders
ORDER BY order_date DESC
LIMIT 5;

SELECT customer_id, first_name, last_name, signup_date
FROM customers
WHERE signup_date > '2023-01-01';

SELECT COUNT(*) AS total_customers
FROM customers;
