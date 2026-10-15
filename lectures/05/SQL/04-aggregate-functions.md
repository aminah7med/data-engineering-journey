# 04. Aggregate Functions

## Definition and purpose

Aggregate functions summarize many rows into one result. They are central to business reporting, data quality analysis, and operational monitoring.

## Common aggregate functions

- `COUNT()` counts rows or non-NULL values
- `SUM()` adds numeric values
- `AVG()` returns the mean
- `MIN()` finds the lowest value
- `MAX()` finds the highest value

## Syntax

```sql
SELECT COUNT(*) AS total_orders,
       SUM(total_amount) AS revenue,
       AVG(total_amount) AS avg_order_value
FROM orders
WHERE status = 'paid';
```

## Example

```sql
SELECT COUNT(*) AS active_customers
FROM customers
WHERE is_active = 1;
```

## Important behavior

- `COUNT(*)` counts every row.
- `COUNT(column_name)` ignores `NULL` values in that column.
- `SUM()` ignores `NULL` values.
- `AVG()` is computed over non-NULL rows.

## Common mistakes

- Confusing `COUNT(*)` with `COUNT(column)`
- Applying aggregate functions without a `GROUP BY` when expecting row-by-row results
- Forgetting that `NULL`s can silently affect totals and averages

## Data Engineering use case

Aggregate functions are used to calculate daily revenue, stale record counts, duplicate counts, and pipeline success metrics.

## Interview questions

- What is the difference between `COUNT(*)` and `COUNT(column_name)`?
- Why does `AVG()` sometimes surprise you when `NULL`s exist?
- When would you use `SUM()` versus `COUNT()` in a dashboard?
