# 19. SQL for Data Engineering

## Definition and purpose

This lesson connects SQL fundamentals to the real work of Data Engineering: pipeline building, quality checks, and warehouse transformations.

## Common Data Engineering SQL tasks

- validating raw source data
- checking completeness with null analysis
- identifying duplicates and stale records
- summarizing daily or hourly business metrics
- building incremental loads with watermark logic
- testing idempotency and re-runnable pipelines
- creating staging and reporting views

## Example: data quality check

```sql
SELECT COUNT(*) AS total_rows,
       SUM(CASE WHEN email IS NULL THEN 1 ELSE 0 END) AS missing_emails
FROM customers;
```

## Example: incremental load pattern

```sql
SELECT *
FROM orders
WHERE order_date > '2024-03-01 00:00:00';
```

A pipeline may compare the newest timestamp seen previously to only fetch newer rows.

## Idempotency and upserts

A good Data Engineering workflow should be repeatable. Idempotency means re-running the same process does not create duplicate or conflicting results.

Common patterns:

- `INSERT ... ON DUPLICATE KEY UPDATE`
- merge-style logic in warehouse systems
- deduplication before final writes
- deterministic ordering and business keys

## Common mistakes

- Treating SQL as only a reporting language
- Ignoring data quality checks before transformations
- Assuming a repeated job is safe without idempotency controls

## Data Engineer use case

Data engineers use SQL in staging, validation, transformation, warehousing, and pipeline monitoring. The same logic that works in a notebook often needs to be made robust, testable, and repeatable.

## Interview questions

- What is idempotency in a data pipeline?
- Why are incremental loads important?
- How do you detect incomplete or inconsistent records in SQL?
