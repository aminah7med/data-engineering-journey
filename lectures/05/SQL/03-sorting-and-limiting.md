# 03. Sorting and Limiting

## Definition and purpose

`ORDER BY` controls row ordering. `LIMIT` restricts the number of rows returned. These features are essential for readable outputs, top-N analysis, and pipeline checks.

## Syntax

```sql
SELECT column1, column2
FROM table_name
WHERE condition
ORDER BY column1 ASC, column2 DESC
LIMIT 10;
```

## Example

```sql
SELECT order_id, total_amount, order_date
FROM orders
WHERE status IN ('paid', 'shipped')
ORDER BY total_amount DESC
LIMIT 5;
```

This returns the five highest-value orders.

## Important notes

- `ORDER BY` is evaluated after the row set is built.
- `ASC` is default if omitted.
- `LIMIT` is often used with `ORDER BY` for ranking-style queries.
- MySQL allows `LIMIT OFFSET`, which is useful for pagination.

## Example with pagination

```sql
SELECT *
FROM orders
ORDER BY order_date DESC
LIMIT 20 OFFSET 40;
```

## Common mistakes

- Assuming rows are returned in insertion order without `ORDER BY`
- Using `LIMIT` without sorting when top values matter
- Mixing display ordering with data correctness

## Data Engineering use case

A data engineer might query the newest records or the most recent failures to validate a daily batch. Sorting and limiting also help reduce the amount of data examined during debugging.

## Interview question

- Why does `LIMIT` not guarantee the same rows across repeated runs unless the ordering is deterministic?
