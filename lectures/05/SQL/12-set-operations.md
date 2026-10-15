# 12. Set Operations

## Definition and purpose

Set operations combine results from multiple queries. They are useful when you want to compare or merge separate result sets with consistent columns.

## Common set operations

- `UNION`: combines distinct rows
- `UNION ALL`: combines all rows, including duplicates
- `INTERSECT`: returns rows present in both queries (not always available in MySQL)
- `EXCEPT`: returns rows only in the first result set (not always available in MySQL)

## Example

```sql
SELECT customer_id, first_name
FROM customers
WHERE region = 'North'
UNION ALL
SELECT customer_id, first_name
FROM customers
WHERE region = 'South';
```

## Important notes

- Column counts and types must align.
- `UNION` removes duplicates; `UNION ALL` does not.
- MySQL supports `UNION` and `UNION ALL`, but not all vendors support `INTERSECT` or `EXCEPT` in the same way.

## Common mistakes

- Forgetting that `UNION` removes duplicates
- Combining queries with mismatched column counts
- Using set operations when a `JOIN` or `CASE` would be clearer

## Data Engineering use case

Set operations are useful in data reconciliation, comparing two source extracts, or combining records from slightly different staging tables before transformation.

## Interview questions

- Why use `UNION ALL` instead of `UNION` when duplicates are expected?
- What needs to be the same across the queries used in a set operation?
- When would you compare query outputs with set logic rather than joins?
