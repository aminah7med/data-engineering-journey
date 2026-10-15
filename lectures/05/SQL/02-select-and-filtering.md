# 02. SELECT and Filtering

## Definition and purpose

`SELECT` is the primary command for retrieving data. `WHERE` filters records based on a condition. Together they form the core of ad hoc analysis and operational validation in SQL.

## Syntax

```sql
SELECT column1, column2
FROM table_name
WHERE condition;
```

## Example

```sql
SELECT order_id, customer_id, status, total_amount
FROM orders
WHERE status = 'paid'
  AND total_amount >= 500;
```

This query returns paid orders worth at least 500.

## Operators commonly used in `WHERE`

- `=` equality
- `!=` or `<>` not equal
- `>`, `<`, `>=`, `<=`
- `IN` membership
- `BETWEEN` range
- `LIKE` pattern matching
- `IS NULL` and `IS NOT NULL`
- `AND`, `OR`, `NOT`

## Example with multiple filters

```sql
SELECT *
FROM customers
WHERE region = 'North'
  AND is_active = 1
  AND signup_date >= '2024-01-01';
```

## Pattern matching

```sql
SELECT first_name, last_name
FROM customers
WHERE email LIKE '%@example.com';
```

`LIKE` is useful for text-based filtering, but it can become slow on large unindexed text fields.

## Common mistakes

- Using `=` with `NULL` instead of `IS NULL`
- Forgetting parentheses around mixed `AND`/`OR` conditions
- Writing `LIKE` patterns without understanding `%` and `_`
- Filtering on computed values without testing business rules first

## Data Engineering use case

A warehouse pipeline often checks for stale customers or invalid statuses before loading them into a reporting table. Filtering logic is typically the first layer of validation.

## Interview questions

- Why does `NULL` not work with `=`?
- What is the difference between `IN` and `BETWEEN`?
- How do `AND` and `OR` affect evaluation order?
- When would you use `LIKE` versus exact equality?
