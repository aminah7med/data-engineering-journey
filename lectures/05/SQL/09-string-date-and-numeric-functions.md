# 09. String, Date, and Numeric Functions

## Definition and purpose

SQL built-in functions transform values or calculate results inside a query. They are useful for cleaning text, extracting date parts, applying numeric rules, and handling missing values in analytics, staging, and pipeline validation.

Examples in this lesson target **MySQL 8.4** and the project's e-commerce schema, including `customers`, `orders`, `order_items`, and `products`.

## Scalar functions and aggregate functions

A **scalar function** takes one or more values from a row and returns a value for that row. For example, `UPPER(first_name)` produces an uppercase name for each customer.

An **aggregate function** summarizes values across multiple rows, usually producing one result for the input set or one result per `GROUP BY` group. `COUNT()`, `SUM()`, `AVG()`, `MIN()`, and `MAX()` are aggregate functions—not scalar functions. For details on their behavior and grouping, see [Aggregate Functions](04-aggregate-functions.md).

```sql
-- Scalar expression: one transformed value for each row
SELECT product_id, ROUND(unit_price, 0) AS rounded_price
FROM products;

-- Aggregate expressions: one summary per category
SELECT category, AVG(unit_price) AS average_price
FROM products
GROUP BY category;
```

## String functions

String functions transform or extract text. The following examples use customer names and product names from the schema:

```sql
SELECT
    customer_id,
    LOWER(email) AS normalized_email,
    UPPER(city) AS city_label,
    CONCAT(first_name, ' ', last_name) AS full_name,
    TRIM(product_name) AS cleaned_product_name,
    SUBSTRING(product_name, 1, 5) AS name_prefix
FROM customers
CROSS JOIN products;
```

This demonstrates valid functions, but the `CROSS JOIN` creates every customer/product combination and is usually not needed just to demonstrate text functions. In ordinary queries, apply functions to columns from the table being read:

```sql
SELECT
    customer_id,
    LOWER(email) AS normalized_email,
    UPPER(city) AS city_label,
    CONCAT(first_name, ' ', last_name) AS full_name
FROM customers;

SELECT
    product_id,
    TRIM(product_name) AS cleaned_product_name,
    SUBSTRING(product_name, 1, 5) AS name_prefix
FROM products;
```

- `LOWER()` and `UPPER()` change letter case.
- `CONCAT()` joins strings. In MySQL, if an argument is `NULL`, the result is `NULL`.
- `TRIM()` removes leading and trailing spaces by default.
- `SUBSTRING(string, start, length)` extracts characters; positions are one-based.

## Numeric functions

Numeric functions transform or classify numeric values:

```sql
SELECT
    product_id,
    unit_price,
    ROUND(unit_price, 1) AS price_to_one_decimal,
    ABS(unit_price - 20.00) AS distance_from_20,
    CEIL(unit_price) AS next_integer,
    FLOOR(unit_price) AS lower_integer
FROM products;
```

- `ROUND(number, decimals)` rounds to the requested number of decimal places.
- `ABS(number)` returns the non-negative magnitude.
- `CEIL(number)` (also spelled `CEILING(number)` in MySQL) returns the smallest integer greater than or equal to the value.
- `FLOOR(number)` returns the largest integer less than or equal to the value.

Rounding is a presentation or business rule, not a substitute for choosing an appropriate `DECIMAL` type and defining the required monetary precision.

## Date and time functions

The schema stores `orders.order_date` as `DATETIME`, `customers.signup_date` as `DATE`, and `products.created_at` as `DATETIME`:

```sql
SELECT
    order_id,
    order_date,
    DATE(order_date) AS order_day,
    YEAR(order_date) AS order_year,
    MONTH(order_date) AS order_month
FROM orders;
```

`DATE()` extracts the date part from a date-time value. `YEAR()` and `MONTH()` return numeric date parts.

```sql
SELECT
    CURRENT_DATE AS today,
    NOW() AS current_date_and_time;
```

`CURRENT_DATE` returns the current date; `NOW()` returns the current date and time. MySQL's current-time functions use the session time zone, so confirm time-zone settings when comparing values from distributed systems.

Use `DATE_ADD()` to calculate a date or time relative to another:

```sql
SELECT
    order_id,
    order_date,
    DATE_ADD(order_date, INTERVAL 7 DAY) AS follow_up_at
FROM orders;
```

For a date range, prefer a half-open range on the original column rather than wrapping the column in a function:

```sql
SELECT order_id, order_date, total_amount
FROM orders
WHERE order_date >= CURRENT_DATE - INTERVAL 30 DAY
  AND order_date < CURRENT_DATE + INTERVAL 1 DAY;
```

This example includes the last 30 days and today up to the start of tomorrow. Keeping the indexed column unmodified can allow an index range scan; verify with `EXPLAIN` for the actual query and data.

## NULL-handling functions

`COALESCE(value1, value2, ...)` returns the first non-`NULL` argument. `NULLIF(value1, value2)` returns `NULL` when the two values are equal; otherwise, it returns `value1`.

```sql
SELECT
    customer_id,
    COALESCE(city, 'Unknown') AS city_for_report
FROM customers;
```

This replaces a missing city with a display value in the result; it does not update stored data.

```sql
SELECT
    order_id,
    total_amount / NULLIF(total_amount, 0) AS safe_ratio_example
FROM orders;
```

`NULLIF()` is often used to prevent division by zero. The expression above is syntactically valid but yields `1` for nonzero `total_amount`; a more typical use is to divide by a potentially zero count:

```sql
SELECT
    SUM(total_amount) / NULLIF(COUNT(*), 0) AS average_order_value
FROM orders
WHERE status = 'paid';
```

`COUNT(*)` cannot be zero in this aggregate query without `GROUP BY` (it returns one row with a count of zero), but the `NULLIF()` pattern is useful in grouped calculations or when the denominator is a computed value. `COALESCE()` and `NULLIF()` do not make `NULL` behave like an ordinary value; they explicitly handle it. For broader `NULL` and conditional-expression behavior, see [CASE and NULL Handling](08-case-and-null-handling.md).

## Function categories at a glance

| Category | Examples | Typical purpose |
|---|---|---|
| String scalar | `LOWER`, `UPPER`, `CONCAT`, `TRIM`, `SUBSTRING` | Normalize or extract text per row |
| Numeric scalar | `ROUND`, `ABS`, `CEIL`, `FLOOR` | Transform or compare numeric values per row |
| Date/time scalar | `DATE`, `YEAR`, `MONTH`, `CURRENT_DATE`, `NOW`, `DATE_ADD` | Extract parts or calculate dates and times |
| NULL handling | `COALESCE`, `NULLIF` | Choose fallback values or convert a sentinel case to `NULL` |
| Aggregate | `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` | Summarize values across rows |

## Built-in functions, user-defined functions, and stored procedures

Built-in functions such as `LOWER()` and `DATE_ADD()` are provided by MySQL. A **user-defined function (UDF)** is created or installed by a database user or extension to provide a reusable function not supplied as a built-in; it returns a value and can be used in expressions subject to MySQL's rules. A **stored procedure** is a separately invoked routine that can execute a sequence of SQL statements and may accept parameters and return result sets or output parameters. A procedure is not simply another scalar expression.

## Important notes and common mistakes

- MySQL functions and date arithmetic can differ from other SQL dialects; check the target database when porting queries.
- `CONCAT()` returns `NULL` if any argument is `NULL`. Use `COALESCE()` for an explicit fallback when that matches the business rule.
- `COALESCE()` returns the first non-`NULL` value; it does not treat empty strings or zero as missing.
- `NULLIF(a, b)` returns `NULL` only when `a` equals `b`; comparisons involving `NULL` are not true.
- `ROUND()` changes the result value, while display formatting is a separate concern. Avoid rounding intermediate financial calculations without a defined requirement.
- `CEIL()` and `FLOOR()` behave differently for negative values; test boundary cases when they affect business rules.
- Applying a function to a filtered/indexed column (for example, `DATE(order_date) = ...`) may prevent an efficient index range scan. Prefer a range predicate when possible.
- `CURRENT_DATE` and `NOW()` are evaluated according to MySQL's session time zone; align time zones and timestamp semantics in pipelines.
- Avoid implicit conversion between strings, dates, and numbers. Store and compare values using appropriate types.

## Data Engineering use case

A pipeline may normalize email casing with `LOWER()`, trim imported text with `TRIM()`, extract a reporting month with `YEAR()` and `MONTH()`, compute date windows with `DATE_ADD()`, and apply `COALESCE()` to create a clearly labeled reporting value for missing data. Aggregates such as `COUNT()` and `SUM()` can then validate row counts and totals; see [Aggregate Functions](04-aggregate-functions.md). Keep transformations explicit, preserve raw values when needed for auditability, and test nulls, empty strings, time zones, and numeric boundaries.

## Interview questions

- What is the difference between a scalar function and an aggregate function?
- Which of `COUNT()`, `SUM()`, `AVG()`, `MIN()`, and `MAX()` are aggregate functions?
- What does MySQL `CONCAT()` return if one input is `NULL`?
- How are `COALESCE()` and `NULLIF()` different?
- What is the difference between `CURRENT_DATE` and `NOW()`?
- Why might filtering with `DATE(order_date) = ...` be less efficient than a range predicate?
- How can `NULLIF()` help avoid division by zero?
- How does a stored procedure differ from a built-in or user-defined function?
