-- Solution: Filtering and Sorting
SELECT order_id, customer_id, total_amount, status
FROM orders
WHERE status = 'paid'
ORDER BY total_amount DESC;

SELECT customer_id, first_name, last_name, region
FROM customers
WHERE region IN ('West', 'East');

SELECT order_id, customer_id, total_amount
FROM orders
WHERE total_amount BETWEEN 100 AND 1000
ORDER BY total_amount DESC;

SELECT order_id, customer_id, order_date, total_amount
FROM orders
WHERE order_date >= '2024-03-01' AND order_date < '2024-04-01'
ORDER BY order_date DESC;

SELECT customer_id, first_name, last_name, email
FROM customers
WHERE email LIKE '%@example.com';
