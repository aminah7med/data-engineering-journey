# Exercise Solutions Guide

Attempt the prompts first. These notes are reasoning hints and query patterns, not a replacement for validating output in `mongosh`. All examples target `nosql_learning` and the supplied sample.

## 01 — Document structures and modeling

- Customers contain scalar fields, a nested `address` document, and a `tags` array. Orders contain a `Date`-typed `order_date` after import and an `items` array of nested item documents. Products have nested `attributes`.
- Customer 101 has `loyalty_tier` absent; customer 103 has it present with `null`. Use `$exists: false` for absence and `{ $exists: true, $eq: null }` for explicit null.
- Customer 104 appears twice with distinct `_id` values (`c-104-a` and `c-104-b`); the business identifier is duplicated and should not be used as a unique key until resolved. The sample also has one missing customer ID and one explicitly null ID; inspect these separately because a group by business ID can collect both under a null group key.
- Embedding item purchase price/name snapshots can preserve the historical transaction. A product reference can locate current catalog details. Store both only when each serves a defined requirement.
- Keeping an unbounded order history inside a customer document risks growth and size limits and makes order filtering harder. Separate order documents fit independent order queries.

## 02 — MongoDB CRUD

Use a unique practice key, inspect any existing match, and check the result object:

```javascript
db.customers.insertOne({
  customer_id: 901,
  name: "Demo Customer",
  city: "Cairo"
});
db.customers.find({ customer_id: 901 });
db.customers.updateOne(
  { customer_id: 901 },
  { $set: { city: "Giza" } }
);
db.customers.deleteOne({ customer_id: 901 });
db.customers.find({ customer_id: 901 });
```

If using a different practice ID, substitute it consistently. Never run a delete with an empty filter.

## 03 — Aggregation pipeline

Order counts and revenue by status:

```javascript
db.orders.aggregate([
  {
    $group: {
      _id: "$status",
      order_count: { $sum: 1 },
      revenue: { $sum: "$total" }
    }
  },
  { $sort: { revenue: -1 } }
]);
```

Product units and gross item sales:

```javascript
db.orders.aggregate([
  { $unwind: "$items" },
  {
    $group: {
      _id: "$items.product_id",
      units_sold: { $sum: "$items.quantity" },
      gross_sales: {
        $sum: { $multiply: ["$items.quantity", "$items.unit_price"] }
      }
    }
  },
  { $sort: { gross_sales: -1 } }
]);
```

For line-item counts per order, either compute array size without unwinding:

```javascript
db.orders.aggregate([
  {
    $project: {
      _id: 0,
      order_id: 1,
      status: 1,
      line_item_count: { $size: "$items" }
    }
  }
]);
```

The stored order total can include discounts, tax, shipping, or rounding that is not represented in item prices, so it need not equal gross line-item sales.

## 04 — Data quality and duplicates

Find duplicate business identifiers:

```javascript
db.customers.aggregate([
  { $group: { _id: "$customer_id", count: { $sum: 1 } } },
  { $match: { count: { $gt: 1 } } }
]);
```

Missing vs explicit null:

```javascript
db.orders.find({ coupon_code: { $exists: false } });
db.orders.find({ coupon_code: { $exists: true, $eq: null } });
```

`{ coupon_code: null }` matches either case. The sample's `o-5002` has explicit null; `o-5003` and `o-5005` omit the field. For customers, `c-missing-id` omits `customer_id` while `c-null-id` explicitly sets it to null. Do not add a unique index on `customer_id` until duplicates and invalid IDs have been resolved under a documented rule. For order references, compare the distinct `customer_id` values to the customer set and item product IDs to the product set; flag unmatched records for quarantine or remediation rather than silently dropping them.
