# NoSQL for Data Engineering

This section introduces the major NoSQL data models and uses MongoDB as a practical document-database example. NoSQL is not one database technology: key-value, document, wide-column, and graph databases make different trade-offs and solve different problems. No model is universally faster or better than a relational database; a good choice follows from access patterns, consistency requirements, workload, and operating constraints.

## Learning objectives

By the end of this section, you should be able to:

- Explain why NoSQL databases exist and compare their models with relational systems.
- Recognize key-value, document, wide-column, and graph workloads and their trade-offs.
- Use MongoDB documents, collections, BSON types, and CRUD operations with `mongosh`.
- Model related data with embedding or references based on query patterns and update needs.
- Build aggregation pipelines, select indexes, and reason about query performance.
- Explain replication, consistency, partitioning, sharding, and CAP without treating them as slogans.
- Apply document databases to semi-structured ingestion and data-quality workflows.

## Prerequisites

- Familiarity with JSON, basic programming data structures, and command-line use.
- Basic database concepts such as records, identifiers, and queries.
- A local MongoDB Community Server and MongoDB Shell (`mongosh`) for hands-on work. Conceptual lessons can be read without installing MongoDB.
- For relational concepts, see the [SQL learning path](../../05/SQL/README.md). This section does not repeat SQL fundamentals.

## Lesson roadmap

| # | Topic | Read |
|---:|---|---|
| 01 | NoSQL Fundamentals | [01-nosql-fundamentals.md](01-nosql-fundamentals.md) |
| 02 | Relational vs. NoSQL | [02-relational-vs-nosql.md](02-relational-vs-nosql.md) |
| 03 | NoSQL Data Models | [03-nosql-data-models.md](03-nosql-data-models.md) |
| 04 | Key-Value Databases | [04-key-value-databases.md](04-key-value-databases.md) |
| 05 | Document Databases | [05-document-databases.md](05-document-databases.md) |
| 06 | Wide-Column Databases | [06-wide-column-databases.md](06-wide-column-databases.md) |
| 07 | Graph Databases | [07-graph-databases.md](07-graph-databases.md) |
| 08 | MongoDB Fundamentals | [08-mongodb-fundamentals.md](08-mongodb-fundamentals.md) |
| 09 | MongoDB CRUD Operations | [09-mongodb-crud-operations.md](09-mongodb-crud-operations.md) |
| 10 | MongoDB Data Modeling | [10-mongodb-data-modeling.md](10-mongodb-data-modeling.md) |
| 11 | MongoDB Aggregation Pipeline | [11-mongodb-aggregation-pipeline.md](11-mongodb-aggregation-pipeline.md) |
| 12 | Indexing and Query Performance | [12-indexing-and-query-performance.md](12-indexing-and-query-performance.md) |
| 13 | Consistency and Replication | [13-consistency-and-replication.md](13-consistency-and-replication.md) |
| 14 | Partitioning and Sharding | [14-partitioning-and-sharding.md](14-partitioning-and-sharding.md) |
| 15 | NoSQL for Data Engineering | [15-nosql-for-data-engineering.md](15-nosql-for-data-engineering.md) |
| 16 | Interview Questions | [16-nosql-interview-questions.md](16-nosql-interview-questions.md) |

## MongoDB setup and sample data

Install MongoDB Community Server and `mongosh` using the [official installation guide](https://www.mongodb.com/docs/manual/installation/). Start the local server using the instructions for your operating system, then verify that the shell can connect:

```text
mongosh "mongodb://localhost:27017"
```

The sample uses the dedicated `nosql_learning` database. The import script refuses to insert into any of its three collections if a collection already contains documents; it does not drop collections or overwrite records. This makes repeat runs explicit and avoids destructive setup commands.

From the repository root, inspect the sample JSON and run:

```text
mongosh "mongodb://localhost:27017/nosql_learning" --file lectures/06/NoSQL/exercises/setup/import-sample-data.js
```

The script reads [sample-data.json](exercises/setup/sample-data.json), then inserts the `customers`, `orders`, and `products` arrays. Confirm the data in `mongosh`:

```javascript
use nosql_learning
db.customers.countDocuments()
db.orders.countDocuments()
db.products.countDocuments()
```

The sample intentionally includes one duplicate `customer_id` (`104`) for data-quality practice. Do not treat that business identifier as unique until it has been cleaned. MongoDB's `_id` values remain distinct.

## Exercises and solutions

- [Exercise guide and setup](exercises/README.md)
- [01 — Document structures and modeling](exercises/01-document-modeling.md)
- [02 — MongoDB CRUD](exercises/02-mongodb-crud.md)
- [03 — Aggregation pipeline](exercises/03-aggregation-pipeline.md)
- [04 — Data quality and duplicates](exercises/04-data-quality-and-duplicates.md)
- [Solutions guide](exercises/solutions/README.md)

Attempt each exercise before opening the corresponding solution notes. Each exercise references the supplied sample dataset; the solutions directory contains guidance rather than automatically executed scripts.

## Recommended study order

1. Read lessons 01–07 to understand the broader database landscape.
2. Import the sample data and read lessons 08–10 while inspecting documents.
3. Practice CRUD, then pipelines and indexes (lessons 09, 11, and 12).
4. Study consistency, replication, and sharding (lessons 13–14).
5. Apply the concepts to ingestion and quality checks in lesson 15.
6. Complete the exercises and use lesson 16 for interview review.

## Essential `mongosh` commands

```javascript
use nosql_learning
show collections
db.customers.find({ city: "Cairo" })
db.orders.find({ status: "paid" }).limit(5)
db.orders.aggregate([{ $group: { _id: "$status", count: { $sum: 1 } } }])
db.customers.getIndexes()
```

These are MongoDB Shell commands and MongoDB query/aggregation syntax; they are not SQL equivalents. Use the lesson examples for safe insert, update, and delete operations.

## Study checklist

- [ ] I can explain why NoSQL exists and why it describes multiple data models.
- [ ] I can compare relational and NoSQL design without claiming a universal winner.
- [ ] I can identify suitable key-value, document, wide-column, and graph workloads.
- [ ] I can explain MongoDB documents, collections, BSON, and CRUD behavior.
- [ ] I can choose embedding or referencing based on access and update patterns.
- [ ] I can distinguish a missing field from an explicit `null`.
- [ ] I can build and explain an aggregation pipeline.
- [ ] I can choose an index based on real query patterns and explain its write/storage cost.
- [ ] I can describe replication, consistency, CAP, partitioning, and sharding accurately.
- [ ] I can validate required fields, find duplicate business IDs, and explain downstream analytics options.
- [ ] I have completed the exercises and can explain my design decisions.

## Official documentation

- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [MongoDB Shell (`mongosh`)](https://www.mongodb.com/docs/mongodb-shell/)
- [MongoDB CRUD operations](https://www.mongodb.com/docs/manual/crud/)
- [MongoDB data modeling](https://www.mongodb.com/docs/manual/data-modeling/)
- [MongoDB aggregation](https://www.mongodb.com/docs/manual/aggregation/)
- [MongoDB indexes](https://www.mongodb.com/docs/manual/indexes/)
- [MongoDB replication](https://www.mongodb.com/docs/manual/replication/)
- [MongoDB sharding](https://www.mongodb.com/docs/manual/sharding/)
- [MongoDB import/export tools](https://www.mongodb.com/docs/database-tools/)

## Notes

- The example database is fictional and intended only for local practice.
- MongoDB-specific behavior is labeled as such. Syntax and guarantees differ among NoSQL products.
- Operational document databases and analytical warehouses/lakehouses have different workload goals; lesson 15 discusses a common pipeline boundary.
