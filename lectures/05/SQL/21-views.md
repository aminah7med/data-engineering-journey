# 21. Views

## Definition and purpose

A **view** is a named SQL query that can be queried like a table. A standard view stores its definition, not a separate copy of the rows; when you query it, MySQL uses the view definition to produce the result.

Views are useful to:

- Reuse a query that would otherwise be repeated.
- Present a simpler, stable interface over several tables.
- Hide columns or rows that consumers do not need.
- Separate reporting logic from application queries.

Examples target **MySQL 8.4** and the learning schema in `data_engineering_shop`.

## Creating and querying a view

This view joins orders to customers and exposes a small reporting-friendly set of columns:

```sql
CREATE VIEW customer_order_details AS
SELECT
    o.order_id,
    o.customer_id,
    c.first_name,
    c.last_name,
    o.order_date,
    o.status,
    o.total_amount
FROM orders AS o
JOIN customers AS c
    ON c.customer_id = o.customer_id;
```

Query a view with ordinary `SELECT` syntax:

```sql
SELECT order_id, first_name, last_name, total_amount
FROM customer_order_details
WHERE status = 'paid'
ORDER BY order_date DESC;
```

The view is not a snapshot. The result reflects the underlying tables when the query runs. Filtering a view in an outer query is often convenient, but the optimizer determines how the query is executed.

## Replacing and dropping a view

MySQL 8.4 supports `CREATE OR REPLACE VIEW`. It creates the view if it does not exist or replaces its definition if it does:

```sql
CREATE OR REPLACE VIEW customer_order_details AS
SELECT
    o.order_id,
    o.customer_id,
    c.first_name,
    c.last_name,
    o.order_date,
    o.status,
    o.total_amount,
    o.shipping_city
FROM orders AS o
JOIN customers AS c
    ON c.customer_id = o.customer_id;
```

The example adds `shipping_city` to the view definition. Changing a view's columns can affect queries that depend on it, so coordinate changes with its consumers.

Remove a view definition with:

```sql
DROP VIEW IF EXISTS customer_order_details;
```

`DROP VIEW` removes the view, not the underlying `customers` or `orders` rows. `IF EXISTS` avoids an error when the view is already absent.

## Views, tables, and temporary tables

| Object | What it contains | Lifetime and refresh behavior |
|---|---|---|
| Ordinary table | Stored rows | Persists until changed or dropped |
| Standard view | A stored query definition | Persists as a database object; rows are derived from base tables when queried |
| Temporary table | Stored rows in a temporary table | Available only in the current session and removed when that session ends |

A view does not ordinarily cache its result. A temporary table stores rows you explicitly place in it and is useful for intermediate work within a session. An ordinary table stores persistent data. These objects have different storage, lifecycle, and update behavior.

## Standard views and materialized views

A **materialized view**, conceptually, stores the result of a query so it can be read without recomputing the full query each time. Because stored results can become stale, materialized views need a refresh or maintenance strategy.

**MySQL 8.4 does not provide native materialized views in the same manner as some other database systems.** A common alternative is a summary table populated and refreshed by a scheduled or incremental pipeline. That table must have an explicit strategy for updates, deletes, late-arriving data, and recovery; it is not automatically maintained as a materialized view would be in a system that supports one.

## Updatable views

Some simple views allow `INSERT`, `UPDATE`, or `DELETE` operations to affect rows in an underlying table. For example, this single-table view selects a subset of customer columns:

```sql
CREATE OR REPLACE VIEW active_customers AS
SELECT customer_id, first_name, last_name, email, is_active
FROM customers
WHERE is_active = 1
WITH CASCADED CHECK OPTION;
```

An update through this view modifies the base table:

```sql
UPDATE active_customers
SET email = 'updated@example.test'
WHERE customer_id = 1;
```

`WITH CASCADED CHECK OPTION` prevents inserts or updates through the view from creating rows that no longer satisfy the view's condition. The example is illustrative; it changes the customer's stored email if run.

Not every view is updatable. In MySQL, features such as `GROUP BY`, aggregate functions, `DISTINCT`, `UNION`, and certain joins or derived expressions can prevent updates or make them ambiguous. A view that combines orders and customers should generally be treated as a read interface, not as a direct editing interface. Check the MySQL documentation for the precise updatability rules.

## Security, abstraction, and maintainability

Views can provide a narrower interface by selecting only approved columns or rows. For example, a reporting view can omit customer email addresses. A view alone is not a complete security policy: configure account privileges carefully and test access using the intended account.

MySQL views can use `SQL SECURITY DEFINER` (the default) or `SQL SECURITY INVOKER`. With `DEFINER`, access checks for underlying objects use the view definer's privileges; with `INVOKER`, they use the querying account's privileges. Understand this setting before using views to expose data across privilege boundaries.

Views also create abstraction: consumers can query a stable name without repeating join logic. To keep them maintainable:

- Give the view and its columns clear, stable names.
- Select explicit columns instead of `SELECT *`, so schema changes do not silently alter the interface.
- Document the row grain and filters, especially for aggregates.
- Review dependent queries before changing or dropping a view.
- Measure query performance; a view can simplify SQL but does not inherently make it faster.

## Data Engineering use cases

- Expose a consistent, cleaned projection of source tables for downstream jobs.
- Centralize shared business logic, such as paid-order definitions or customer reporting fields.
- Restrict a consumer interface to the columns and rows required for a task.
- Build source views for extraction while keeping transformation logic readable.
- Use a maintained summary table—not a standard view—when a query result must be persisted and refreshed for performance.

Treat views as versioned interfaces when multiple pipelines or reports depend on them. Validate row counts, null behavior, permissions, and query plans after changes.

## Common mistakes

- Assuming a standard view stores or caches its result.
- Treating a view as a security boundary without checking grants and `SQL SECURITY`.
- Using `SELECT *` and unintentionally changing the view's exposed columns later.
- Assuming every view supports writes.
- Replacing a view without checking dependent queries or consumers.
- Expecting MySQL to refresh a materialized result automatically; MySQL 8.4 has no native materialized-view feature like some other systems.
- Assuming a view improves performance simply because it hides a complex query.

## Interview questions

- What is a view, and how does it differ from a table?
- Does a standard MySQL view store its result rows?
- What is the difference between a view and a temporary table?
- What does `CREATE OR REPLACE VIEW` do in MySQL?
- Does MySQL 8.4 provide native materialized views?
- When can a view be updatable, and what does `WITH CHECK OPTION` enforce?
- How can views support security, and what should be checked about `SQL SECURITY`?
- What are the risks of changing a view used by multiple reports or pipelines?
- When might a maintained summary table be more appropriate than a standard view?

## Official documentation

- [MySQL 8.4 `CREATE VIEW` statement](https://dev.mysql.com/doc/refman/8.4/en/create-view.html)
- [MySQL 8.4 `DROP VIEW` statement](https://dev.mysql.com/doc/refman/8.4/en/drop-view.html)
- [MySQL 8.4 view processing and algorithms](https://dev.mysql.com/doc/refman/8.4/en/view-algorithms.html)
