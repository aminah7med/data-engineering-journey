# 15. NoSQL for Data Engineering

NoSQL databases can store application data, ingest JSON and event records, cache frequently accessed results, handle distributed high-volume workloads, and expose relationships between entities. Data Engineering work must preserve data meaning and quality at ingestion and plan how data will reach downstream analytical systems and data pipelines.

Different models support different jobs: a document database can store application records with nested fields; a key-value store can cache a result under a known key; a wide-column database can serve high-volume distributed access patterns designed around its partition keys; and a graph database can answer relationship and path queries. These are workload examples, not universal product guarantees.

## Ingest and validate JSON events

Suppose an application emits order events with an event ID, customer ID, timestamp, and nested items. A robust ingest step should parse JSON, validate required fields and types, record rejected or quarantined rows, and make retries idempotent where possible. It should not assume every event has the same optional fields.

MongoDB query examples against the practice collection:

```javascript
// Find orders where customer_id is missing.
db.orders.find({ customer_id: { $exists: false } });

// Find orders whose items field is absent or is not an array.
db.orders.find({
  $or: [
    { items: { $exists: false } },
    { items: { $not: { $type: "array" } } }
  ]
});
```

Validate type semantics for the MongoDB version in use. A query that finds missing fields is not a substitute for enforcing a contract at the ingestion boundary.

## Detect duplicate business identifiers

```javascript
db.customers.aggregate([
  { $group: { _id: "$customer_id", count: { $sum: 1 } } },
  { $match: { count: { $gt: 1 } } }
]);
```

This finds duplicated values, including `_id: null` for documents with a missing `customer_id`; follow up by distinguishing null/missing and inspecting the source records. The sample deliberately contains two customers with business ID 104. Resolve and document the business rule before applying a unique constraint.

## Transform and export

Aggregation pipelines can standardize fields, filter records, unwind arrays, compute metrics, and group data. For a bounded export:

```text
mongoexport --uri="mongodb://localhost:27017/nosql_learning" --collection=orders --out=orders.json --jsonArray
```

This writes an export file to the current directory; check the destination and avoid overwriting valuable files. For larger or recurring extracts, consider batching, change capture, or managed connectors only after defining consistency and recovery needs.

## Operational database vs. analytical platform

Operational NoSQL databases may serve application reads and writes with low latency and current state. Warehouses and lakehouses are optimized for historical analysis, larger scans, joins across domains, and governed analytical models. A pipeline may ingest JSON or change/event records from operational systems, validate and transform them, and land them in analytical storage for downstream reporting and analysis. Caching layers may reduce repeated reads but need deliberate expiration, invalidation, and stale-data handling.

Select each database according to the data model, access patterns, consistency requirements, operational needs, and workload. Consider transaction and recovery behavior, durability, partitioning, retention, monitoring, backup, and the team's ability to operate the product. A technology should not be selected solely because it is labeled NoSQL or distributed.

Initial exercises require only local MongoDB and `mongosh`; no streaming, orchestration, or cloud services are required.
