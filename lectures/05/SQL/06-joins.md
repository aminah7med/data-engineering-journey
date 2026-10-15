# 06. JOINs

## Definition and purpose

A `JOIN` combines rows from two or more tables using a related column. This is one of the most important SQL concepts because most real-world data is modeled across multiple tables.

## Common JOIN types

- `INNER JOIN`: returns only matching rows
- `LEFT JOIN`: returns all rows from the left table and matching rows from the right table
- `RIGHT JOIN`: returns all rows from the right table
- `FULL OUTER JOIN`: not supported in MySQL in the same way as some other dialects

## Example

```sql
SELECT o.order_id, c.first_name, c.last_name, o.total_amount
FROM orders o
INNER JOIN customers c
  ON o.customer_id = c.customer_id;
```

## LEFT JOIN example

```sql
SELECT c.customer_id, c.first_name, COUNT(o.order_id) AS orders_placed
FROM customers c
LEFT JOIN orders o
  ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name;
```

This is useful for finding customers without orders because the `LEFT JOIN` preserves customers with no match in `orders`.

## Common mistakes

- Forgetting the join condition (`ON` clause)
- Using `INNER JOIN` when you need unmatched records
- Confusing join cardinality with row-count expectations
- Joining on columns with different types or meanings

## Data Engineering use case

Join logic is used constantly when building fact tables, customer dimensions, and analytical marts. A data engineer must know whether unmatched rows are expected or are a sign of missing data.

## Interview questions

- What is the difference between `INNER JOIN` and `LEFT JOIN`?
- How do you find rows that do not match in a join?
- Why can a join create duplicate rows if the relationship is not well-defined?
