# Exercise 04 — Data Quality and Duplicates

Use only read-only checks against the practice collections.

1. Group customers by `customer_id` and return values appearing more than once. Inspect both duplicate documents.
2. Check for customers with a missing `customer_id`; separately check for a present `customer_id` whose value is `null`.
3. Find orders whose `coupon_code` is missing, then find orders whose `coupon_code` is explicitly `null`. Explain why a simple `{ coupon_code: null }` filter is not enough to distinguish them.
4. Check for orders missing `items`, and for orders whose `items` field is not an array.
5. Check for orders with no matching customer or an item whose `product_id` has no product match. Describe a validation approach without deleting records.
6. Propose an ingestion rule to prevent duplicate source events from creating repeated orders. Include an idempotency key or unique business constraint in the design.
7. Would you immediately create a unique index on `customers.customer_id`? Explain the precondition and remediation steps.

The sample deliberately contains two customers with `customer_id: 104`, one customer with a missing `customer_id`, another with `customer_id: null`, one order with `coupon_code: null`, and other orders where that field is missing.
