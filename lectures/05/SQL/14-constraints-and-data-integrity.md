# 14. Constraints and Data Integrity

## Definition and purpose

Constraints define business and database rules that keep data valid. They prevent bad records from entering tables and help maintain referential integrity.

## Common constraints

- `PRIMARY KEY`
- `FOREIGN KEY`
- `NOT NULL`
- `UNIQUE`
- `CHECK` (supported in MySQL 8.0+ with certain caveats)
- `DEFAULT`

## Example

```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    UNIQUE (product_name)
);
```

## Why constraints matter

Constraints reduce invalid data and make patterns easier to reason about. A system with weak constraints loses trust quickly, especially in operational and analytical pipelines.

## Common mistakes

- Using application code to enforce rules that belong in the database
- Creating duplicate records because a `UNIQUE` index is missing
- Ignoring the difference between logical validity and database validation

## Data Engineer use case

Data engineers often rely on constraints and data checks to catch invalid row values before a pipeline writes them downstream.

## Interview questions

- Why are constraints useful if application code already validates data?
- What is the difference between a uniqueness rule and a primary key?
- How do constraints help with data quality?
