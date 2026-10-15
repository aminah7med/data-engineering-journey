# 08. CASE and NULL Handling

## Definition and purpose

`CASE` creates conditional logic inside a query. `NULL` values represent missing or unknown data and require special handling in SQL.

## CASE example

```sql
SELECT order_id,
       CASE
           WHEN status = 'paid' THEN 'Completed'
           WHEN status = 'pending' THEN 'Awaiting payment'
           ELSE 'Other'
       END AS order_status_label
FROM orders;
```

## NULL behavior

`NULL` means ?unknown? or ?missing?, not zero. This affects:

- comparison: `column = NULL` is never true
- filtering: use `IS NULL` or `IS NOT NULL`
- aggregations: `SUM()` and `AVG()` ignore `NULL`
- concatenation: `NULL` often causes the result to become `NULL`

## Safe expression example

```sql
SELECT customer_id,
       COALESCE(email, 'missing_email') AS email_status
FROM customers;
```

`COALESCE` returns the first non-NULL value.

## Common mistakes

- Comparing `NULL` with `=`
- Assuming `NULL` behaves like an empty string
- Forgetting to use `COALESCE` when building reporting logic

## Data Engineering use case

Data engineers use `CASE` and `COALESCE` to standardize raw source data, map statuses, and prevent downstream pipeline failures when values are missing.

## Interview questions

- What is the difference between `NULL`, empty string, and zero?
- Why is `IS NULL` required instead of `= NULL`?
- How does `COALESCE` help in ETL logic?
