# Exercise 01 — Document Structures and Modeling

Use the imported sample in `nosql_learning`. Do not modify data for this exercise.

1. Inspect one document in each of `customers`, `orders`, and `products`. Sketch the shape of each document and identify nested objects and arrays.
2. Find the customer document with `customer_id: 101`. Which fields are scalar, and which are arrays or embedded documents?
3. Find orders for customer 101 and list the product IDs and quantities in each order.
4. Identify a customer with `loyalty_tier` missing and one whose `loyalty_tier` is explicitly `null`. Explain the difference.
5. The sample repeats `customer_id: 104`. What makes the two documents distinguishable to MongoDB? Why is `customer_id` not a safe unique lookup yet?
6. Suppose an order is usually read together with all its items, but product names can change while historical orders must retain the purchased name and price. Propose which item fields to embed and which current product information to reference. Explain the snapshot trade-off.
7. Compare embedding a customer's entire order history with storing orders in a separate collection. Consider unbounded growth, common queries, and update patterns.

Suggested read-only starting queries:

```javascript
db.customers.find({ customer_id: 101 });
db.orders.find({ customer_id: 101 });
db.customers.find({ loyalty_tier: { $exists: false } });
db.customers.find({ loyalty_tier: { $exists: true, $eq: null } });
```
