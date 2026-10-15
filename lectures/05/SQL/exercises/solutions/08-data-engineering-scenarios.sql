-- Solution: Data Engineering Scenarios
SELECT DISTINCT customer_id
FROM orders
WHERE status = 'paid'
INTERSECT
SELECT DISTINCT customer_id
FROM orders
WHERE status = 'pending';

SELECT order_id, customer_id, total_amount, status
FROM orders
WHERE total_amount > 1000
  AND status <> 'cancelled';

SELECT product_id, COUNT(*) AS order_count
FROM order_items
GROUP BY product_id
HAVING COUNT(*) > 1;

-- Here, the schema does not have a phone column. This query demonstrates the idea of a null-check for missing email values.
SELECT COUNT(*) AS missing_email_rows
FROM customers
WHERE email IS NULL;

SELECT order_id, customer_id, order_date, total_amount
FROM orders
WHERE order_date > '2024-03-15 00:00:00';
