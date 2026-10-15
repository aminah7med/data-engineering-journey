# 13. DML and DDL

## Definition and purpose

Data Definition Language (DDL) defines database objects such as tables and indexes. Data Manipulation Language (DML) changes rows inside those objects.

## DDL examples

```sql
CREATE TABLE audit_log (
    audit_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    table_name VARCHAR(100),
    event_time DATETIME DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE customers ADD COLUMN signup_source VARCHAR(50);
```

## DML examples

```sql
INSERT INTO customers (first_name, last_name, email, region, signup_date)
VALUES ('Nora', 'West', 'nora.west@example.com', 'West', '2024-04-20');

UPDATE customers
SET region = 'North'
WHERE customer_id = 5;

DELETE FROM customers
WHERE customer_id = 99;
```

## Important notes

- DDL changes the database structure.
- DML affects data within existing tables.
- Transactions are especially important for DML because partial updates can leave data inconsistent.

## Common mistakes

- Running destructive statements without a targeted filter
- Forgetting `WHERE` on an update or delete
- Forgetting to test the effect of schema changes before production use

## Data Engineering use case

Data engineers use DDL to create staging tables, add metadata columns, and manage warehouse schemas. DML is used for load patterns, history tracking, and controlled updates.

## Interview questions

- What is the difference between DDL and DML?
- Why is `UPDATE` and `DELETE` safety important in production systems?
- When would you use an `INSERT ... SELECT` pattern?
