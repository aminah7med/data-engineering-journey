# 18. Data Cleaning and Deduplication

## Definition and purpose

Data cleaning removes bad or inconsistent records; deduplication identifies repeated rows or repeated business keys. These are critical steps in Data Engineering because raw data is rarely perfectly clean.

## Example: duplicate detection

```sql
SELECT email, COUNT(*) AS duplicate_count
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;
```

## Example: duplication by recent history

```sql
SELECT customer_id, email, COUNT(*)
FROM customer_email_history
GROUP BY customer_id, email
HAVING COUNT(*) > 1;
```

## Deduplication strategy

A deterministic approach is often needed:

- choose a business key
- define a sorting rule to keep the most recent or most complete row
- use `ROW_NUMBER()` to rank duplicates
- delete or archive the extras

## Common mistakes

- Deleting duplicates without a stable deduplication rule
- Treating all missing values as the same kind of problem
- Ignoring source-specific differences in key logic

## Data Engineering use case

Data engineers regularly deduplicate customer records, event rows, and campaign data. A bad deduplication strategy causes inflated counts and incorrect downstream analytics.

## Interview questions

- Why is deduplication not only a SQL exercise, but also a business-rule exercise?
- What is a deterministic deduplication rule?
- How would you handle duplicate records in a pipeline without losing valid data?
