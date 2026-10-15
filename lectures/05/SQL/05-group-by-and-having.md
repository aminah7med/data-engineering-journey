# 05. GROUP BY and HAVING

## Definition and purpose

`GROUP BY` organizes rows into groups based on one or more columns. `HAVING` filters those groups after aggregation.

## Syntax

```sql
SELECT column_name, COUNT(*)
FROM table_name
WHERE condition
GROUP BY column_name
HAVING COUNT(*) > 1;
```

## Example

```sql
SELECT status, COUNT(*) AS order_count, SUM(total_amount) AS revenue
FROM orders
GROUP BY status;
```

This returns one row per status, with totals for each group.

## Why `HAVING` is needed

`WHERE` filters rows before aggregation. `HAVING` filters groups after aggregation has happened.

```sql
SELECT customer_id, COUNT(*) AS orders_placed
FROM orders
GROUP BY customer_id
HAVING COUNT(*) >= 2;
```

## Common mistakes

- Putting a filter on an aggregate in `WHERE` instead of `HAVING`
- Grouping by a field that is not logically part of the summary
- Forgetting that all non-aggregated selected columns must appear in `GROUP BY`

## Data Engineering use case

`GROUP BY` is used for KPI rollups, anomaly detection, and identifying categories that require follow-up. A pipeline quality check may group orders by status to see if too many are missing finalization.

## Interview questions

- What is the difference between `WHERE` and `HAVING`?
- Why do some SQL engines require all selected columns to be in `GROUP BY` or aggregated?
- When would you use `GROUP BY` with multiple columns?
