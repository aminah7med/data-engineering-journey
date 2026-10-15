# 11. Window Functions

## Definition and purpose

A window function calculates a value across a set of rows related to the current row without collapsing the output into a single group. This is useful for rankings, running totals, and comparisons within partitions.

## Example: ranking

```sql
SELECT order_id,
       customer_id,
       total_amount,
       ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY total_amount DESC) AS order_rank
FROM orders;
```

## Example: running total

```sql
SELECT order_id,
       order_date,
       total_amount,
       SUM(total_amount) OVER (ORDER BY order_date) AS running_total
FROM orders;
```

## Why it matters

Window functions allow analytics-style logic without losing row-level output. They are foundational in modern SQL for time series, segmentation, and trending analysis.

## Common mistakes

- Forgetting the `OVER (...)` clause
- Using a window function in a place where an aggregate is more appropriate
- Not understanding partitions and ordering inside the window

## Data Engineering use case

A data engineer may compute rolling revenue, rank product sales by region, or identify the latest record per customer while retaining the full dataset.

## Interview questions

- What is a window function?
- How is `ROW_NUMBER()` different from `RANK()`?
- Why are partitions important in window calculations?
