-- Solution: Aggregation
SELECT status, COUNT(*) AS order_count
FROM orders
GROUP BY status;

SELECT customer_id, SUM(total_amount) AS total_revenue
FROM orders
GROUP BY customer_id
HAVING SUM(total_amount) > 0;

SELECT status,
       AVG(total_amount) AS average_order_value
FROM orders
WHERE status IN ('paid', 'shipped')
GROUP BY status;

SELECT is_active, COUNT(*) AS customer_count
FROM customers
GROUP BY is_active;

SELECT category, COUNT(*) AS product_count
FROM products
GROUP BY category;
