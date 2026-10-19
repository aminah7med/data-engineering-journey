# 12. Indexing and Query Performance

> **MongoDB-specific:** indexes are ordered data structures that help MongoDB locate matching documents and support some sort operations. A collection without a suitable index may require a collection scan.

## Start from a query

If the application often filters orders by customer and sorts by date, consider a compound index that follows the filter and sort pattern:

```javascript
db.orders.createIndex({ customer_id: 1, order_date: -1 });
db.orders.find({ customer_id: 101 }).sort({ order_date: -1 });
```

This is a candidate, not a universal prescription. Validate using representative data and `explain("executionStats")`:

```javascript
db.orders.find({ customer_id: 101 })
  .sort({ order_date: -1 })
  .explain("executionStats");
```

Review the plan, documents examined, keys examined, and returned result count. Index ordering matters for compound keys; a different query pattern can require a different index.

## Costs and cautions

Each additional index consumes storage and memory and must be maintained on writes. Too many indexes increase write latency and operational overhead. Indexes can also be unhelpful for low-selectivity filters or queries that return most of a collection. Create indexes for observed, important query patterns, then measure.

The sample's `customer_id: 104` is intentionally duplicated, so do not create a unique index on that field before resolving the duplicate. Unique indexes enforce a constraint and fail if existing documents violate it.

## Practical workflow

1. Capture the exact filter, sort, projection, and expected result size.
2. Check existing indexes with `db.orders.getIndexes()`.
3. Compare an explain plan before and after a candidate index.
4. Measure read and write behavior with realistic data.
5. Remove indexes only after confirming they're unused and assessing impact.
