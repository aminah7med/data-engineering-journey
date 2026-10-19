# 16. NoSQL Interview Questions

These model answers target internship and junior Data Engineering interviews. Adapt answers to the product and requirements in the question; avoid presenting general tendencies as universal guarantees.

## 1. What does NoSQL mean, and how does it differ from SQL?

**Model answer:** NoSQL is an umbrella for non-relational data models such as key-value, document, wide-column, and graph. SQL usually refers to a query language and commonly to relational database systems. The useful comparison is between concrete systems and requirements: relational tables and constraints may suit joins and multi-record integrity; a document store may suit nested aggregates accessed together. Neither is always faster or more scalable. I would compare data shape, query patterns, transaction scope, consistency, distribution, and operational cost.

## 2. Name the main NoSQL models and a suitable workload for each.

**Model answer:** Key-value fits session or cache lookups by known key. Document fits nested, evolving records such as product catalogs or order aggregates. Wide-column can fit distributed workloads with known partition-oriented access patterns, such as time-series by device and bucket. Graph fits queries that repeatedly traverse relationships, such as recommendations or fraud networks. Actual product capabilities vary, so I would validate guarantees and query needs.

## 3. What are MongoDB documents and collections?

**Model answer:** A MongoDB document is a BSON record of fields, nested objects, and arrays. A collection groups documents, typically for a common entity or access pattern. Each document has a unique `_id`; business identifiers such as `customer_id` are separate fields and are not unique unless constrained. Collections may have optional or varying fields, but a useful application schema and validation rules are still necessary.

## 4. When would you embed data versus reference it?

**Model answer:** I embed bounded data that is commonly read and updated with its parent, such as line items in an order. I reference data that is shared, independently updated, unbounded, or accessed along different paths. Embedding can reduce round trips and provide single-document atomicity, but can duplicate values and grow documents. References reduce duplication but require lookups and do not automatically enforce referential integrity. I decide from query and update patterns, cardinality, and consistency requirements.

## 5. Explain MongoDB CRUD with an example.

**Model answer:** In `mongosh`, `insertOne()` creates a document, `find()` reads matching documents, `updateOne()` applies an update operator such as `$set`, and `deleteOne()` removes one matching document. I use a selective, preferably unique filter for writes and inspect `matchedCount`, `modifiedCount`, or `deletedCount`. MongoDB query documents and operators are not SQL syntax.

```javascript
db.customers.insertOne({ customer_id: 901, name: "Demo", city: "Cairo" });
db.customers.find({ customer_id: 901 });
db.customers.updateOne({ customer_id: 901 }, { $set: { city: "Giza" } });
db.customers.deleteOne({ customer_id: 901 });
```

## 6. What is an aggregation pipeline?

**Model answer:** It is an ordered sequence of stages that processes documents. `$match` filters, `$project` reshapes, `$unwind` expands array elements, `$group` aggregates, `$sort` orders, and `$lookup` combines collections. Stage order and output grain matter: after unwinding items, a single order appears once per item, which can inflate order counts if not regrouped correctly.

## 7. How do indexes help, and what do they cost?

**Model answer:** An index can reduce the documents scanned for a filter and can support ordering. I create indexes for measured query patterns and validate with explain output. Indexes consume storage and memory and add work to writes. A low-selectivity filter or a query returning most documents may still scan many records. Compound index field order matters, and I avoid creating indexes speculatively.

## 8. What is replication? Does it replace backups?

**Model answer:** Replication maintains copies of data on multiple nodes and may support failover or read scaling. It does not replace backups: accidental deletes or corruption can replicate, and backups support recovery to an earlier point. In MongoDB, replica-set behavior is affected by elections, write concern, read concern, and read preference.

## 9. Explain consistency and the CAP theorem.

**Model answer:** Consistency describes which values reads can observe and depends on product guarantees and configuration. CAP addresses the choice during a network partition between availability—responding to requests—and strong single-copy consistency for those operations. It does not mean every system permanently picks only two properties, nor is “consistency” identical across all database terminology. I would explain the partition behavior and requested guarantees for the specific operation.

## 10. What is partitioning or sharding?

**Model answer:** Partitioning divides a dataset; sharding distributes partitions across servers. A well-chosen shard key can distribute load and allow targeted queries. A poor key may cause hotspots, uneven data, or scatter-gather queries. Sharding adds operational complexity and is not automatically necessary because a dataset is large; measure the capacity need and validate candidate keys.

## 11. How do you evolve a document schema safely?

**Model answer:** Treat the document shape as a versioned contract. Introduce changes compatibly, make readers handle the transition, validate new writes, backfill old records in controlled batches, monitor invalid shapes, and remove compatibility paths only after migration. Missing and explicit `null` have different meanings, so the contract should define each.

## 12. How would you identify duplicate customer identifiers?

**Model answer:** Group by the business key and retain groups with count greater than one, then inspect source records and decide the business resolution rule. I would distinguish missing and null IDs from actual duplicates, make ingestion idempotent using a stable event or source key, and add a unique constraint only after data is clean. The internal MongoDB `_id` is unique but does not itself prove `customer_id` uniqueness.

```javascript
db.customers.aggregate([
  { $group: { _id: "$customer_id", count: { $sum: 1 } } },
  { $match: { count: { $gt: 1 } } }
]);
```

## 13. Scenario: choose storage for orders and analytics.

**Question:** An application reads an order and its items together, but analysts need multi-year joins across customers, products, and order history. What would you propose?

**Model answer:** I would first quantify transactions, update patterns, and consistency requirements. MongoDB can be appropriate for the operational order aggregate, with bounded items embedded and customer/product references or item snapshots chosen intentionally. I would export validated data to a warehouse or lakehouse for long-range joins and broad scans, avoiding heavy analytics against the operational path. A relational database may be a better operational source if cross-entity transactions and constraints dominate.

## 14. Scenario: product values change after purchase.

**Question:** Should historical orders display the latest product price?

**Model answer:** Usually an order needs an immutable price snapshot captured at purchase time. The order item can store `product_id`, purchased `unit_price`, and perhaps the product name at that time. Referencing the current product document alone would lose historical meaning. This is a deliberate form of denormalization justified by audit and business semantics.

## 15. Scenario: a collection has optional and missing values.

**Question:** How do you tell “not supplied” from “explicitly empty”?

**Model answer:** Define the contract first. In MongoDB, a missing field is absent, whereas a field set to `null` is explicitly present with a null value. For example, `$exists: false` finds absent fields, while `{ field: { $exists: true, $eq: null } }` finds present-null fields. I would not collapse both cases without a documented rule.

## 16. How would you pick a database for a workload?

**Model answer:** I would document access patterns, data relationships, consistency/transaction needs, volume and growth, read/write profile, latency, query flexibility, operational skill, recovery, and downstream analytics. Then compare concrete systems using representative data and failure scenarios. I would choose the simplest system that meets requirements and revisit only when evidence shows a limitation.
