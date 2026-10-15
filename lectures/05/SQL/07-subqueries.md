# 07. Subqueries

## Definition and purpose

A subquery is a query nested inside another query. It can appear in `SELECT`, `FROM`, `WHERE`, or `HAVING` clauses and is useful when the logic is easier to express in stages.

## Example in `WHERE`

```sql
SELECT order_id, total_amount
FROM orders
WHERE customer_id IN (
    SELECT customer_id
    FROM customers
    WHERE region = 'West'
);
```

## Example in `FROM`

```sql
SELECT customer_id, avg_order_value
FROM (
    SELECT customer_id, AVG(total_amount) AS avg_order_value
    FROM orders
    GROUP BY customer_id
) x
WHERE avg_order_value > 1000;
```

## Important notes

- Subqueries can improve readability when logic is naturally nested.
- Correlated subqueries depend on the outer query row by row and may be slower.
- MySQL executes the inner query and then uses the value in the outer query.

## Common mistakes

- Using a subquery that returns multiple values in a scalar context
- Writing correlated subqueries without understanding performance impact
- Overusing nested queries when a join is clearer

## Data Engineering use case

A data engineer may use subqueries to filter a data set based on a business rule, such as ?orders for customers who placed at least one order last month?.

## Interview questions

- When is a subquery preferable to a join?
- What is a correlated subquery?
- Why can a subquery be less efficient than a well-designed join?
