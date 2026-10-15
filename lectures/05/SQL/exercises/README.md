# SQL Exercises

This folder contains reproducible exercises based on a small e-commerce schema. The exercises are designed to be completed in order and to align with the SQL lesson sequence.

## Example database

The scripts in `setup/` create a dedicated MySQL database named `data_engineering_shop` and seed it with realistic sample data. The database is intentionally small enough to reason about by hand while still including edge cases such as missing relationships, null values, and duplicates.

## Run the setup

```bash
mysql -u root -p < exercises/setup/01-create-schema.sql
mysql -u root -p < exercises/setup/02-seed-data.sql
```

## Exercise roadmap

1. [01-basic-queries.sql](01-basic-queries.sql)
2. [02-filtering-and-sorting.sql](02-filtering-and-sorting.sql)
3. [03-aggregation.sql](03-aggregation.sql)
4. [04-joins.sql](04-joins.sql)
5. [05-subqueries-and-ctes.sql](05-subqueries-and-ctes.sql)
6. [06-window-functions.sql](06-window-functions.sql)
7. [07-data-cleaning.sql](07-data-cleaning.sql)
8. [08-data-engineering-scenarios.sql](08-data-engineering-scenarios.sql)

## How to use these exercises

- Read the short task description at the top.
- Complete each numbered question in sequence.
- Use the sample schema and `SELECT` statements to validate your work.
- Keep your query output and reasoning in a notes file if needed.

## Solutions

Answer scripts are available in the [solutions](solutions) directory.
