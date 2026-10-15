# 01. SQL Fundamentals

## Definition and purpose

SQL stands for Structured Query Language. It is the standard language used to query and manipulate relational data. In Data Engineering, SQL is used for validation, transformation, metrics, auditing, and reporting across warehouses and operational systems.

A relational database stores data in tables made up of rows and columns. Each table represents an entity, such as `customers`, `orders`, or `products`.

## Why it matters

Data engineers use SQL to:

- inspect data quality
- join datasets across systems
- aggregate business metrics
- debug pipeline behavior
- validate incremental loads
- define and maintain warehouse models

## Core concepts

- Table: a set of related records
- Row: one record in the table
- Column: one data field for that record
- Primary key: a unique identifier for a row
- Foreign key: a reference to a related row in another table
- Schema: the structure of a database or table

## Example

```sql
SELECT *
FROM customers;
```

This returns all rows and columns from the `customers` table. In a real database, a result set is usually filtered and limited before display.

```sql
SELECT customer_id, first_name, email
FROM customers
WHERE is_active = 1
LIMIT 10;
```

## Syntax and important rules

- `SELECT` lists the columns to return.
- `FROM` identifies the source table.
- `WHERE` filters rows.
- `LIMIT` restricts output size.
- SQL is case-insensitive for keywords, but table and column names are often case-sensitive depending on the database.

## Logical query processing order

A `SELECT` query does not execute in the same order a reader might expect. In MySQL, the logical order is roughly:

1. `FROM`
2. `WHERE`
3. `GROUP BY`
4. `HAVING`
5. `SELECT`
6. `ORDER BY`
7. `LIMIT`

This matters because the `SELECT` clause is computed after filtering and grouping, not before.

## Common mistakes

- Writing `SELECT` before understanding the table structure
- Forgetting that `WHERE` works before `SELECT` output is displayed
- Expecting row order without `ORDER BY`
- Assuming all databases treat `NULL` the same way

## When a Data Engineer would use it

A data engineer may use a simple query to inspect raw customer records, confirm whether a daily load inserted expected rows, or validate that a data quality rule is being met before moving data downstream.

## Interview questions

- What is the difference between a row and a column?
- What is a primary key and why is it important?
- How does a relational database differ from a flat file?
- Why is `ORDER BY` required if you want predictable output ordering?
