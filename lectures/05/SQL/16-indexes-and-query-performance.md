# 16. Indexes and Query Performance

## Definition and purpose

Indexes improve lookup speed by creating a sorted structure for a column or set of columns. They help reduce the cost of filtering, joining, and sorting but can also add write overhead.

## Example

```sql
CREATE INDEX idx_orders_customer_id ON orders (customer_id);
CREATE INDEX idx_orders_status_date ON orders (status, order_date);
```

## Why indexes matter

Without an index, MySQL may scan the full table. With an index, the database can locate or narrow relevant rows faster.

## Important concept: `EXPLAIN`

```sql
EXPLAIN SELECT *
FROM orders
WHERE status = 'paid';
```

`EXPLAIN` helps reveal whether MySQL is using an index and whether a table scan is likely.

## Common mistakes

- Indexing every column without measuring benefit
- Forgetting that data updates also require index maintenance
- Ignoring missing indexes on columns used in filters and joins

## Data Engineering use case

Performance investigation is part of data pipeline support. If a transformation or QA query is slow, understanding indexes and the execution plan is often the first step.

## Interview questions

- Why can indexes slow down writes?
- What does `EXPLAIN` tell you?
- When is an index more valuable than a broad scan?
