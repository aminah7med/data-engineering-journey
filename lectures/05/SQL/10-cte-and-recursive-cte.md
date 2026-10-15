# 10. CTEs and Recursive CTEs

## Definition and purpose

A Common Table Expression (CTE) creates a named temporary result set that can be referenced in a query. Recursive CTEs can repeatedly generate rows and are useful for hierarchical data.

## Non-recursive CTE example

```sql
WITH recent_orders AS (
    SELECT order_id, customer_id, total_amount
    FROM orders
    WHERE order_date >= '2024-01-01'
)
SELECT customer_id, COUNT(*) AS order_count
FROM recent_orders
GROUP BY customer_id;
```

## Recursive CTE example

```sql
WITH RECURSIVE employee_hierarchy AS (
    SELECT employee_id, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT e.employee_id, e.manager_id, eh.level + 1
    FROM employees e
    JOIN employee_hierarchy eh ON e.manager_id = eh.employee_id
)
SELECT *
FROM employee_hierarchy;
```

## Why CTEs are useful

- They improve readability.
- They break complex logic into steps.
- They make repeated logic easier to manage.

## Common mistakes

- Overusing recursive CTEs when a join or aggregation would do the job
- Forgetting that recursion needs a base case
- Creating a CTE without considering query planner efficiency

## Data Engineering use case

A team may use a CTE to isolate filtering, produce a staging result, and then join that result to dimension tables. Recursive CTEs can model org charts or hierarchical product trees.

## Interview questions

- What is the difference between a derived table and a CTE?
- When would you use a recursive CTE?
- Why are CTEs useful in readable ETL logic?
