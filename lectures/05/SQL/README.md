# SQL for Data Engineering

This section is a practical SQL learning path for Data Engineering work. It focuses on relational thinking, query design, data quality, and the kinds of SQL patterns used in analytics pipelines, warehouse work, and operational data validation.

> Examples in this section target MySQL 8.4 unless otherwise stated.

## Learning objectives

By the end of this section, you should be able to:

- Explain what relational databases are and how SQL fits into modern Data Engineering workflows.
- Read and write queries using `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, and aggregate functions.
- Use `JOIN`s correctly to combine related data and explain differences between `INNER` and `LEFT` joins.
- Write subqueries and CTEs for modular logic.
- Handle `NULL`s, `CASE` expressions, and built-in functions with confidence.
- Use window functions for ranking, running totals, and segmentation.
- Create and modify database objects with DDL and DML.
- Understand constraints, keys, indexes, transactions, and ACID properties.
- Apply SQL to real Data Engineering tasks such as data quality checks, deduplication, and incremental loads.
- Prepare for technical interviews with scenario-based SQL questions.

## Prerequisites

Before you begin, make sure you have:

- A working SQL client or terminal for MySQL 8.4.
- MySQL Server installed locally or access to a MySQL-compatible environment.
- A basic understanding of tables, rows, and columns.
- A willingness to practice writing queries by hand and testing results.

## MySQL setup guidance

A simple local setup works well for this learning section:

```bash
mysql --version
mysql -u root -p
```

Then create a dedicated sample database:

```sql
CREATE DATABASE IF NOT EXISTS data_engineering_shop;
USE data_engineering_shop;
```

Use the scripts in `exercises/setup/` to create the schema and seed the data. The examples here assume the database is created and populated before you run the lesson queries.

## Lesson roadmap

| # | Topic | Read |
|---:|---|---|
| 01 | SQL Fundamentals | [01-sql-fundamentals.md](01-sql-fundamentals.md) |
| 02 | SELECT and Filtering | [02-select-and-filtering.md](02-select-and-filtering.md) |
| 03 | Sorting and Limiting | [03-sorting-and-limiting.md](03-sorting-and-limiting.md) |
| 04 | Aggregate Functions | [04-aggregate-functions.md](04-aggregate-functions.md) |
| 05 | GROUP BY and HAVING | [05-group-by-and-having.md](05-group-by-and-having.md) |
| 06 | JOINs | [06-joins.md](06-joins.md) |
| 07 | Subqueries | [07-subqueries.md](07-subqueries.md) |
| 08 | CASE and NULL Handling | [08-case-and-null-handling.md](08-case-and-null-handling.md) |
| 09 | String, Date, and Numeric Functions | [09-string-date-and-numeric-functions.md](09-string-date-and-numeric-functions.md) |
| 10 | CTEs and Recursive CTEs | [10-cte-and-recursive-cte.md](10-cte-and-recursive-cte.md) |
| 11 | Window Functions | [11-window-functions.md](11-window-functions.md) |
| 12 | Set Operations | [12-set-operations.md](12-set-operations.md) |
| 13 | DML and DDL | [13-dml-and-ddl.md](13-dml-and-ddl.md) |
| 14 | Constraints and Data Integrity | [14-constraints-and-data-integrity.md](14-constraints-and-data-integrity.md) |
| 15 | Keys and Relationships | [15-keys-and-relationships.md](15-keys-and-relationships.md) |
| 16 | Indexes and Query Performance | [16-indexes-and-query-performance.md](16-indexes-and-query-performance.md) |
| 17 | Transactions and ACID | [17-transactions-and-acid.md](17-transactions-and-acid.md) |
| 18 | Data Cleaning and Deduplication | [18-data-cleaning-and-deduplication.md](18-data-cleaning-and-deduplication.md) |
| 19 | SQL for Data Engineering | [19-sql-for-data-engineering.md](19-sql-for-data-engineering.md) |
| 20 | SQL Interview Questions | [20-sql-interview-questions.md](20-sql-interview-questions.md) |
| 21 | Views | [21-views.md](21-views.md) |

## Exercises and solutions

- [Exercises overview](exercises/README.md)
- [Setup scripts](exercises/setup/)
- [Solutions](solutions/)

## Example database setup

Run the setup scripts in order:

```bash
mysql -u root -p < exercises/setup/01-create-schema.sql
mysql -u root -p < exercises/setup/02-seed-data.sql
```

The example schema models a small e-commerce data platform with tables such as `customers`, `orders`, `order_items`, `products`, `employees`, and `departments`.

## Recommended study order

1. Start with fundamentals and query logic.
2. Move into filtering, sorting, and aggregation.
3. Practice joins and data relationships.
4. Learn subqueries, CTEs, and window functions.
5. Focus on NULL handling, data quality, and cleaning.
6. Finish with performance, transactions, and Data Engineering scenarios.
7. Use the interview questions as a rapid review before moving on.

## Essential SQL commands and concepts

```sql
SELECT column_name
FROM table_name
WHERE condition
ORDER BY column_name
LIMIT 10;

SELECT COUNT(*)
FROM orders
WHERE status = 'paid';

SELECT o.order_id, c.customer_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;
```

Core ideas you should be comfortable with:

- Relational tables and keys
- `SELECT` and filtering logic
- Aggregate functions and grouping
- `JOIN` types and relationship reasoning
- Subqueries and CTEs
- `NULL` behavior and `CASE` logic
- Window functions and ranking
- DDL, DML, transactions, and constraints
- Query tuning and index thinking

## Study checklist

- [ ] I can explain what SQL is and how it differs from programming languages.
- [ ] I can write basic `SELECT` statements with filters and sorting.
- [ ] I can explain `WHERE`, `GROUP BY`, and `HAVING` clearly.
- [ ] I can use `INNER JOIN` and `LEFT JOIN` correctly.
- [ ] I understand how `NULL` affects comparisons and aggregations.
- [ ] I know when to use subqueries versus CTEs.
- [ ] I can use window functions for ranking and running totals.
- [ ] I can create and alter tables safely.
- [ ] I understand transactions, ACID properties, and rollback behavior.
- [ ] I can detect duplicates and explain data quality checks for pipeline data.
- [ ] I can complete the exercises and explain my reasoning.

## Official documentation

- MySQL 8.4 Reference Manual: https://dev.mysql.com/doc/refman/8.4/en/
- SELECT statement: https://dev.mysql.com/doc/refman/8.4/en/select.html
- JOINs: https://dev.mysql.com/doc/refman/8.4/en/join.html
- Aggregate functions: https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html
- Window functions: https://dev.mysql.com/doc/refman/8.4/en/window-functions.html
- Transactions and ACID: https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-model.html

## Notes

- This section uses a realistic e-commerce schema to make SQL patterns easier to connect to business and Data Engineering tasks.
- The lessons are intentionally focused and practical, rather than attempting to cover every SQL dialect difference in full.
- MySQL-specific syntax is clearly labeled when it appears.
