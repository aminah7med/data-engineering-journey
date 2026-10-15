-- Solution: Subqueries and CTEs
SELECT customer_id, total_amount
FROM orders
WHERE total_amount > (
    SELECT AVG(total_amount)
    FROM orders
);

WITH customer_revenue AS (
    SELECT customer_id, SUM(total_amount) AS total_revenue
    FROM orders
    GROUP BY customer_id
)
SELECT customer_id, total_revenue
FROM customer_revenue
WHERE total_revenue > 1000;

SELECT o.order_id, o.customer_id, c.region
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.region = 'West';

SELECT customer_id, order_id, order_date
FROM orders o
WHERE o.order_date = (
    SELECT MAX(order_date)
    FROM orders o2
    WHERE o2.customer_id = o.customer_id
)
ORDER BY customer_id;

WITH customer_summary AS (
    SELECT customer_id,
           SUM(total_amount) AS revenue
    FROM orders
    GROUP BY customer_id
)
SELECT customer_id,
       revenue,
       CASE
           WHEN revenue >= 2000 THEN 'high'
           WHEN revenue >= 500 THEN 'medium'
           ELSE 'low'
       END AS revenue_band
FROM customer_summary;
