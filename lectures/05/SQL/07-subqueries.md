# 07. Subqueries

## Definition and purpose

A subquery is a `SELECT` statement nested inside another SQL statement. The inner query supplies a value, a set of values, or a temporary result that the outer query uses. Subqueries are useful when a question is naturally expressed in steps, such as “find customers whose total spending is above the average.”

Examples in this lesson target **MySQL 8.4** and the e-commerce schema used throughout this section: `customers`, `orders`, `order_items`, and `products`.

## Where subqueries can be used

### In `WHERE`

Use a subquery to filter rows based on a value or set returned by another query:

```sql
SELECT customer_id, first_name, last_name
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
    WHERE status = 'paid'
);
```

The inner query finds customer IDs with paid orders. The outer query returns those customers.

### In `SELECT`

A scalar subquery can calculate a value for each row in the outer result:

```sql
SELECT
    c.customer_id,
    c.first_name,
    (
        SELECT COUNT(*)
        FROM orders AS o
        WHERE o.customer_id = c.customer_id
    ) AS order_count
FROM customers AS c;
```

This correlated subquery counts each customer's orders. Because `orders.customer_id` is not unique, `COUNT(*)` is used to produce one scalar value for each customer.

### In `FROM`

A subquery in `FROM` is a derived table. It produces rows that the outer query can filter or combine:

```sql
SELECT customer_totals.customer_id, customer_totals.spent
FROM (
    SELECT customer_id, SUM(total_amount) AS spent
    FROM orders
    WHERE status IN ('paid', 'shipped')
    GROUP BY customer_id
) AS customer_totals
WHERE customer_totals.spent > 500;
```

In MySQL, a derived table must have an alias (`customer_totals` here). This example calculates totals first, then filters the result.

### In `HAVING`

Use a subquery in `HAVING` to compare an aggregate for each group with another result:

```sql
SELECT customer_id, AVG(total_amount) AS avg_order_amount
FROM orders
GROUP BY customer_id
HAVING AVG(total_amount) > (
    SELECT AVG(total_amount)
    FROM orders
);
```

This returns customers whose average order amount is above the overall average order amount. `HAVING` filters groups after aggregation; see [GROUP BY and HAVING](05-group-by-and-having.md) for the general clause behavior.

## Subquery types

These terms describe different aspects of a subquery. In particular, “correlated” describes whether the query depends on an outer row; it is not a separate return-size category.

### Scalar subquery

A scalar subquery returns one column and at most one row, so it can be used where one value is expected, such as an expression in `SELECT` or a comparison in `WHERE`.

```sql
SELECT product_id, product_name, unit_price
FROM products
WHERE unit_price > (
    SELECT AVG(unit_price)
    FROM products
);
```

In MySQL, a scalar subquery that returns no rows evaluates to `NULL`; one that returns more than one row raises an error. The inner `AVG()` returns one value for this query.

### Single-row subquery

A single-row subquery returns at most one row. It may return one column (and thus also be scalar) or several columns as a row value. A single-column result can be compared with operators such as `=`, `>`, or `<=`:

```sql
SELECT product_id, product_name
FROM products
WHERE unit_price = (
    SELECT MAX(unit_price)
    FROM products
);
```

The distinction is useful: “single-row” describes the number of rows, while “scalar” also requires exactly one column. A query expected to return one row must actually be constrained or aggregated to do so.

### Multi-row subquery

A multi-row subquery returns a set of values. Use it with `IN`, `NOT IN`, `ANY`, or `ALL`, rather than with a scalar comparison operator:

```sql
SELECT product_id, product_name
FROM products
WHERE product_id IN (
    SELECT oi.product_id
    FROM order_items AS oi
    JOIN orders AS o ON o.order_id = oi.order_id
    WHERE o.status = 'paid'
);
```

This returns products that appear in at least one paid order. The inner query can return multiple product IDs.

### Correlated subquery

A correlated subquery refers to a column from the outer query. Conceptually, its result depends on the current outer row:

```sql
SELECT c.customer_id, c.first_name, c.last_name
FROM customers AS c
WHERE EXISTS (
    SELECT 1
    FROM orders AS o
    WHERE o.customer_id = c.customer_id
      AND o.status = 'paid'
);
```

The reference to `c.customer_id` connects the inner query to each customer. Correlated subqueries can return a scalar, a row, or a set depending on their structure and use.

## `IN`, `EXISTS`, `NOT IN`, and `NOT EXISTS`

### `IN`

`IN` tests whether a value matches any value in a list or subquery result:

```sql
SELECT product_id, product_name
FROM products
WHERE product_id IN (
    SELECT product_id
    FROM order_items
    WHERE item_status = 'active'
);
```

This asks whether each product ID occurs among active order items.

### `EXISTS`

`EXISTS` tests whether the subquery returns at least one row. The selected expression is conventionally `1`; its value is not used:

```sql
SELECT c.customer_id, c.first_name, c.last_name
FROM customers AS c
WHERE EXISTS (
    SELECT 1
    FROM orders AS o
    WHERE o.customer_id = c.customer_id
);
```

This returns customers with at least one order. It does not multiply a customer row when several orders match.

### `NOT EXISTS`

`NOT EXISTS` finds rows for which there is no matching row:

```sql
SELECT c.customer_id, c.first_name, c.last_name
FROM customers AS c
WHERE NOT EXISTS (
    SELECT 1
    FROM orders AS o
    WHERE o.customer_id = c.customer_id
);
```

This is an anti-match query: it returns customers with no orders. It is commonly safer than `NOT IN` when the inner values may contain `NULL`.

### `NOT IN` and `NULL`

`NOT IN` can produce surprising results if the subquery returns even one `NULL`. SQL comparisons with `NULL` are unknown, not true, so a `NOT IN` predicate may reject all rows rather than identify the expected non-matches.

For example, do not assume this reliably finds products never ordered if `order_items.product_id` can contain `NULL`:

```sql
SELECT p.product_id, p.product_name
FROM products AS p
WHERE p.product_id NOT IN (
    SELECT oi.product_id
    FROM order_items AS oi
);
```

The schema declares `order_items.product_id` as `NOT NULL`, but this pattern can become unsafe when used with a nullable source or changed schema. Prefer `NOT EXISTS` for a robust anti-match:

```sql
SELECT p.product_id, p.product_name
FROM products AS p
WHERE NOT EXISTS (
    SELECT 1
    FROM order_items AS oi
    WHERE oi.product_id = p.product_id
);
```

If `NOT IN` is intentional, explicitly exclude nulls from the inner query:

```sql
WHERE p.product_id NOT IN (
    SELECT oi.product_id
    FROM order_items AS oi
    WHERE oi.product_id IS NOT NULL
)
```

## Subqueries and `JOIN`s

A subquery expresses a value, set, or intermediate result; a `JOIN` combines rows from tables. Many tasks can be written either way, but the intended output matters.

Use a `JOIN` when columns from both tables are needed in the result:

```sql
SELECT o.order_id, c.first_name, c.last_name, o.total_amount
FROM orders AS o
JOIN customers AS c ON c.customer_id = o.customer_id;
```

Use `EXISTS` when the question is only whether a related row exists:

```sql
SELECT c.customer_id, c.first_name
FROM customers AS c
WHERE EXISTS (
    SELECT 1
    FROM orders AS o
    WHERE o.customer_id = c.customer_id
);
```

An equivalent inner join can return the same customer more than once if that customer has multiple orders. `DISTINCT` may remove duplicates, but `EXISTS` directly expresses the existence test and preserves one output row per customer.

Neither form is automatically faster. The optimizer may transform equivalent queries; compare actual plans and timings for the real data. For more on join types and row matching, see [JOINs](06-joins.md).

## Subqueries and CTEs

A common table expression (CTE), introduced with `WITH`, names a query result for use in the statement that follows. A derived table is a subquery in `FROM`; a CTE often makes multi-step logic easier to read:

```sql
WITH customer_totals AS (
    SELECT customer_id, SUM(total_amount) AS spent
    FROM orders
    WHERE status IN ('paid', 'shipped')
    GROUP BY customer_id
)
SELECT customer_id, spent
FROM customer_totals
WHERE spent > 500;
```

The same logic can be expressed as a derived table, as shown earlier. Prefer a subquery for a small, local condition or calculation. Prefer a CTE when naming a logical step improves clarity, when a result is reused in the statement, or when building a longer transformation. CTEs are not inherently faster: MySQL's optimizer determines how a query is executed. Recursive CTEs are a separate technique for hierarchical or iterative queries; see [CTEs and recursive CTEs](10-cte-and-recursive-cte.md).

## Common mistakes

- Using `=` with a subquery that can return multiple rows. Use `IN`, `EXISTS`, or a comparison such as `> ANY` when that matches the intended logic.
- Assuming a subquery returns one row without enforcing that with a unique condition or an aggregate.
- Using `NOT IN` when the result set may contain `NULL`; use `NOT EXISTS` or filter nulls explicitly.
- Forgetting the correlation condition, which can turn an intended per-customer check into an unrelated result.
- Returning columns from a subquery in a scalar context when more than one column is selected.
- Omitting the required alias for a derived table in MySQL.
- Rewriting a subquery as a `JOIN` without checking whether one-to-many matches will duplicate rows.
- Assuming the inner query is always executed once first. MySQL's optimizer may transform or reorder query operations.

## Performance considerations

- Correlated subqueries can be expensive when they require repeated work for many outer rows, but MySQL may decorrelate or otherwise optimize eligible queries.
- Use indexes that support the filtering and matching columns, such as `orders.customer_id` or `order_items.product_id`; see [Indexes and query performance](16-indexes-and-query-performance.md).
- Avoid selecting unnecessary columns, especially in large derived results.
- Compare alternatives with `EXPLAIN` (or `EXPLAIN ANALYZE` when appropriate) and representative data. Check rows examined and the chosen access paths instead of relying on syntax alone.
- A subquery, CTE, or join is not inherently the fastest form. Keep the clearest correct form, then measure.

## Data Engineering use cases

- Filter customers to those with qualifying orders, such as paid orders in a reporting period.
- Find products with no active order items as a catalog quality check.
- Compare a customer's aggregate with an overall benchmark to flag unusual spending.
- Build a derived per-customer or per-product result before loading a reporting table.
- Use `NOT EXISTS` to identify missing relationships, such as orders with no corresponding customer, when validating staged data.

In a pipeline, verify null behavior, duplicate handling, and expected row counts before using the query output as a load or quality-check result.

## Interview questions

- What is a subquery, and where can it appear in a `SELECT` statement?
- How does a scalar subquery differ from a single-row subquery?
- What makes a subquery correlated, and what performance concern can arise?
- When would you choose `EXISTS` instead of `IN`?
- Why can `NOT IN` behave unexpectedly when `NULL` is present?
- How can a `JOIN` produce duplicate rows when an `EXISTS` query does not?
- When might a CTE be clearer than a nested subquery?
- How would you investigate a slow correlated subquery in MySQL?
