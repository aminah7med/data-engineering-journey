# Exercise 03 — Aggregation Pipeline

Use the orders and products collections in `nosql_learning`. Start with read-only pipelines.

1. Count orders by `status`.
2. Calculate total order revenue by `status`, sorted from highest revenue to lowest.
3. Unwind `items` and calculate units sold and gross item sales by `product_id`.
4. Join the product names to the item results with `$lookup`. What happens if a product reference does not match?
5. Compare the sum of `orders.total` for paid orders with the sum of item-level revenue for paid orders. Explain why totals might differ in a real system (discounts, tax, shipping, rounding).
6. Write a pipeline that returns one record per order with the order ID, status, and number of line items. Ensure the count is computed after unwinding and regrouping, or use an array-size expression.

Reminder: after `$unwind`, the grain is one row per order item, not one row per order. Use `$match`, `$unwind`, `$group`, `$lookup`, and `$sort` intentionally.
