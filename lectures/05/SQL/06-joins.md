# 06. JOINs

## Definition and purpose

A `JOIN` combines rows from two or more tables using a relationship between their columns. In the e-commerce schema used in this course, `orders.customer_id` relates orders to customers, and `order_items.order_id` relates line items to orders. A join lets a query return columns from both sides of that relationship.

Examples target **MySQL 8.4** and the project's `customers`, `orders`, `order_items`, `products`, `employees`, and `departments` tables.

## Join conditions and aliases

The `ON` condition describes which rows match. Table aliases make multi-table queries shorter and clarify which table each column belongs to:

```sql
SELECT o.order_id, c.first_name, c.last_name, o.total_amount
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id;
```

Here, `o` is the alias for `orders`, and `c` is the alias for `customers`. Qualify columns with their table or alias whenever names could be ambiguous. Join keys should represent the same relationship and compatible values; matching on unrelated columns can produce plausible-looking but incorrect results.

The schema's primary and foreign keys describe expected relationships. One customer can have many orders, while each order refers to one customer. One order can have many order items, and each order item refers to one product. These cardinalities affect how many output rows a join produces.

## `INNER JOIN`

`INNER JOIN` returns only rows with a matching row on both sides:

```sql
SELECT o.order_id, c.customer_id, c.first_name, o.total_amount
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id
WHERE o.status = 'paid';
```

Each matching order appears with its customer. Customers without orders do not appear. Because the schema requires every order to reference a customer, the customer match should exist when foreign-key constraints are enforced.

## `LEFT JOIN`

`LEFT JOIN` preserves every row from the left table and adds matching right-side values. When no right-side row matches, its selected columns are `NULL`:

```sql
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(o.order_id) AS orders_placed
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name;
```

This includes customers with no orders. Use `COUNT(o.order_id)`, not `COUNT(*)`: an unmatched customer still contributes one null-extended output row, so `COUNT(*)` would count it as one.

To find customers with no orders, test a non-nullable right-side key:

```sql
SELECT c.customer_id, c.first_name, c.last_name
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

Be careful when filtering the right table. Putting `o.status = 'paid'` in the `WHERE` clause removes unmatched rows and makes the result behave like an inner join for that condition. To retain all customers while matching only paid orders, put the filter in `ON`:

```sql
SELECT c.customer_id, o.order_id, o.status
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id
   AND o.status = 'paid';
```

## `RIGHT JOIN`

`RIGHT JOIN` preserves every row from the right table and adds matching left-side values. Unmatched left-side columns become `NULL`:

```sql
SELECT d.department_name, e.employee_id, e.first_name, e.last_name
FROM employees AS e
RIGHT JOIN departments AS d
    ON e.department_id = d.department_id;
```

This keeps all departments, including departments with no assigned employees. A right join can usually be rewritten by swapping table order and using a `LEFT JOIN`, which many teams find easier to read:

```sql
SELECT d.department_name, e.employee_id, e.first_name, e.last_name
FROM departments AS d
LEFT JOIN employees AS e
    ON e.department_id = d.department_id;
```

## `FULL OUTER JOIN`

A full outer join preserves all rows from both sides: matching rows are combined, and nonmatching rows from either side are retained with `NULL` values for the missing side.

**MySQL 8.4 does not support the `FULL OUTER JOIN` syntax.** For tables with a unique match key, emulate it with a left join plus the right-only rows, combined using `UNION ALL`:

```sql
SELECT
    c.customer_id,
    c.first_name,
    o.order_id,
    o.status
FROM customers AS c
LEFT JOIN orders AS o
    ON o.customer_id = c.customer_id

UNION ALL

SELECT
    c.customer_id,
    c.first_name,
    o.order_id,
    o.status
FROM orders AS o
LEFT JOIN customers AS c
    ON c.customer_id = o.customer_id
WHERE c.customer_id IS NULL;
```

The second query contributes only orders without a matching customer, avoiding duplicates of matched rows. In the provided schema, the foreign key normally prevents such orphan orders; the pattern is still useful when validating unconstrained staging data. `UNION ALL` retains rows as produced and avoids the extra duplicate-removal work of `UNION`.

## Self joins

A self join joins a table to itself using different aliases. It is useful for relationships such as employee-to-manager:

```sql
SELECT
    employee.employee_id,
    employee.first_name AS employee_first_name,
    employee.last_name AS employee_last_name,
    manager.employee_id AS manager_id,
    manager.first_name AS manager_first_name,
    manager.last_name AS manager_last_name
FROM employees AS employee
LEFT JOIN employees AS manager
    ON employee.manager_id = manager.employee_id;
```

The `LEFT JOIN` keeps employees who have no manager, such as the top-level employee. Each alias represents a different role played by the same table.

## `CROSS JOIN`

A `CROSS JOIN` returns every combination of rows from its two inputs. If the first table has *m* rows and the second has *n*, the result has *m × n* rows:

```sql
SELECT d.department_name, p.category
FROM departments AS d
CROSS JOIN (
    SELECT DISTINCT category
    FROM products
) AS p;
```

This can produce a department-by-product-category grid, for example to prepare a reporting scaffold that includes combinations with no activity. A cross join is intentional only when all combinations are needed; forgetting a join condition can accidentally create the same kind of row explosion.

## Why joins can multiply rows

Joins return matching combinations, not automatically one row per entity. With the schema's one-to-many relationships, a customer with three orders produces three rows when joined to orders. Joining orders to `order_items` produces one row per line item. That is expected if the desired grain is one row per item.

Joining two independent one-to-many relationships at once can multiply combinations. For example, a customer with three orders and two email-history records may produce six rows when both child tables are joined through the customer. Aggregating after that join can overcount order totals or history records.

To investigate unexpected duplicates:

1. State the intended output grain (one row per customer, order, or item).
2. Check uniqueness and cardinality of the join keys on each side.
3. Count rows before and after each join; group by the intended key and inspect counts greater than one.
4. Check whether one-to-many tables are being combined independently.
5. Aggregate each child table to the required grain before joining, or use `EXISTS` if only existence matters.
6. Do not use `DISTINCT` as a default fix: it can hide a wrong join or remove legitimate repeated records.

For example, aggregate order totals before combining them with email history:

```sql
SELECT c.customer_id, c.first_name, order_totals.spent, email_counts.email_records
FROM customers AS c
LEFT JOIN (
    SELECT customer_id, SUM(total_amount) AS spent
    FROM orders
    GROUP BY customer_id
) AS order_totals
    ON order_totals.customer_id = c.customer_id
LEFT JOIN (
    SELECT customer_id, COUNT(*) AS email_records
    FROM customer_email_history
    GROUP BY customer_id
) AS email_counts
    ON email_counts.customer_id = c.customer_id;
```

Each derived result has at most one row per customer, preventing the two detail tables from multiplying each other.

## JOINs and subqueries

Use a join when the result needs columns from related tables or when combining row sets is the clearest expression. Use `EXISTS` when the question is whether a related row exists, without returning its columns:

```sql
SELECT c.customer_id, c.first_name
FROM customers AS c
WHERE EXISTS (
    SELECT 1
    FROM orders AS o
    WHERE o.customer_id = c.customer_id
      AND o.status = 'paid'
);
```

An inner join to `orders` could return a customer more than once when that customer has multiple paid orders. `EXISTS` preserves one output row per customer. A join can also be used when related values are needed, such as order status or totals.

Neither approach is universally faster; MySQL can optimize equivalent forms. Choose the form that expresses the intended result and verify performance with representative data. For subquery types and more examples, see [Subqueries](07-subqueries.md).

## Common mistakes

- Omitting or using the wrong `ON` condition.
- Joining columns with different meanings or incompatible types.
- Selecting an outer-joined table's columns in `WHERE` in a way that removes unmatched rows.
- Using `COUNT(*)` instead of counting a nullable-side key when counting matches after a `LEFT JOIN`.
- Assuming a join returns one row per left-side entity despite a one-to-many relationship.
- Joining multiple detail tables before aggregating, causing inflated counts or sums.
- Using `DISTINCT` to conceal unexplained row multiplication.
- Writing a `CROSS JOIN` unintentionally by omitting a join condition.

## Data Engineering use cases

- Join orders to customers and products when building transaction-level fact data.
- Use left joins to retain all dimension entities and identify missing facts or relationships.
- Join employee records to departments or managers for organizational reporting.
- Aggregate child records before joining to avoid double-counting metrics.
- Validate staged data by identifying unmatched keys before loading constrained production tables.

Always define the output grain and decide how unmatched records should be handled before building a pipeline transformation.

## Interview questions

- What rows does an `INNER JOIN` return, and how does that differ from a `LEFT JOIN`?
- How can a `RIGHT JOIN` be expressed as a `LEFT JOIN`?
- What does a `FULL OUTER JOIN` return, and how can you emulate it in MySQL 8.4?
- What is a self join? Give an example using employees and managers.
- What is the result size of a cross join?
- Why can a join return more rows than either input table?
- How would you find customers without orders?
- Why might `COUNT(*)` give a misleading result after a `LEFT JOIN`?
- When would you use `EXISTS` instead of a join?
- How would you investigate an unexpected increase in row counts in a data pipeline?
