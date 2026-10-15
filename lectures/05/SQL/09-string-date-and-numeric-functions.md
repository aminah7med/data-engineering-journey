# 09. String, Date, and Numeric Functions

## Definition and purpose

SQL provides built-in functions for cleaning and transforming text, dates, and numbers. These functions are widely used in analytics, staging, and pipeline validation.

## String functions

```sql
SELECT first_name,
       LOWER(first_name) AS lower_name,
       CONCAT(first_name, ' ', last_name) AS full_name
FROM customers;
```

## Date functions

```sql
SELECT order_id, order_date,
       DATE(order_date) AS order_day,
       MONTH(order_date) AS order_month
FROM orders;
```

## Numeric functions

```sql
SELECT ROUND(123.456, 2) AS rounded_value,
       ABS(-50) AS absolute_value;
```

## Important notes

- Date functions vary slightly across database systems.
- MySQL has strong built-in date and string support, which is useful for ETL work.
- Functions can also make query logic less readable if overused, so keep them clear and tested.

## Common mistakes

- Comparing date strings without converting types properly
- Returning unformatted dates when a business-friendly format is needed
- Forgetting that some functions are dialect-specific

## Data Engineering use case

A pipeline may clean customer names, standardize date strings into a common format, and round financial values before insertion into a warehouse.

## Interview questions

- What is the difference between a string function and a date function in SQL?
- Why is `CAST` or `CONVERT` sometimes required in data transformation logic?
- When should you prefer a SQL function over application-layer formatting?
