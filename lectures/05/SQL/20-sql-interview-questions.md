# 20. SQL Interview Questions

This lesson is designed for review and interview preparation. It focuses on practical SQL thinking, not memorization alone.

## Typical question categories

- joins and relationship logic
- filtering and null behavior
- aggregation and grouping
- window functions
- deduplication
- transaction safety
- performance and index awareness

## Sample questions

### 1. Find customers with no orders

```sql
SELECT c.customer_id, c.first_name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

### 2. Find the top 3 customers by total revenue

```sql
SELECT c.customer_id, c.first_name, SUM(o.total_amount) AS total_revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name
ORDER BY total_revenue DESC
LIMIT 3;
```

### 3. Find duplicate emails

```sql
SELECT email, COUNT(*) AS row_count
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;
```

### 4. Find the latest order per customer

```sql
WITH ranked_orders AS (
    SELECT o.customer_id,
           o.order_id,
           o.order_date,
           ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY o.order_date DESC) AS rn
    FROM orders o
)
SELECT *
FROM ranked_orders
WHERE rn = 1;
```

## Interview tips

- Explain your reasoning, not just the final query.
- Clarify assumptions before writing complex SQL.
- Mention edge cases like missing values, duplicates, or partial relationships.
- Practice writing readable queries with aliases and clear logic.

## Data Engineering-specific focus

Interviewers often want to hear how you think about:

- null handling
- data quality concerns
- schema design
- idempotency and repeatability
- query performance
- safe updates and transactional workflows
