-- Solution: Window Functions
SELECT customer_id,
       order_id,
       total_amount,
       ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY total_amount DESC) AS order_rank
FROM orders;

SELECT order_id,
       order_date,
       total_amount,
       SUM(total_amount) OVER (ORDER BY order_date) AS running_total
FROM orders;

WITH ranked_orders AS (
    SELECT customer_id,
           order_id,
           total_amount,
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn
    FROM orders
)
SELECT customer_id, order_id, total_amount
FROM ranked_orders
WHERE rn = 1;

SELECT customer_id,
       COUNT(*) AS order_count,
       RANK() OVER (ORDER BY COUNT(*) DESC) AS customer_rank
FROM orders
GROUP BY customer_id;

SELECT order_id,
       total_amount,
       AVG(total_amount) OVER () AS avg_order_total
FROM orders;
