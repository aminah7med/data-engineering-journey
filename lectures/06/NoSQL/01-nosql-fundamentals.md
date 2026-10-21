# 01. NoSQL Fundamentals

## What does NoSQL mean?

NoSQL is an umbrella term for database systems whose data models and scaling approaches are not limited to the traditional relational-table model. It is often expanded as “not only SQL”: some products provide SQL-like interfaces, but a query language does not determine the underlying data model. NoSQL is not a single database technology.

Different models—key-value, document, wide-column, and graph—optimize for different shapes of data and access patterns. MongoDB, for example, is a document database; it should not be treated as representative of every NoSQL system.

## Why these systems exist

Applications handle structured data, semi-structured data, and sometimes unstructured data. Examples include relational records, JSON documents with optional fields, application logs, images or other files, and key-value data. NoSQL does not mean that all data is unstructured; the important question is which data model and access patterns fit the workload.

Applications also have varied requirements: flexible or evolving records, very high request volume, low-latency key lookups, large distributed datasets, or queries across highly connected entities. NoSQL databases provide different models for these needs. A flexible data model can allow records to have different fields, but it does not remove schema requirements: applications still need contracts for expected fields, types, and validation.

Relational databases remain excellent for structured data, joins, constraints, and transactions. SQL and NoSQL are complementary choices rather than mutually exclusive approaches: a relational database may fit transactional workflows, while a NoSQL database may better fit a specific document, key lookup, wide-column, or graph workload. Teams may use both for different parts of a system.

NoSQL systems became popular as internet applications grew and teams needed to distribute work and data across multiple machines. Distributed storage and horizontal scaling can help particular workloads, but they introduce operational complexity and do not eliminate the need for careful modeling, capacity planning, or consistency decisions. Choose a database according to its data model and access patterns, not because NoSQL is assumed to be universally better.

## Benefits and trade-offs

Potential benefits include flexible record shapes, modeling around common reads, and horizontal distribution for supported workloads. Trade-offs can include duplicated data, application-managed relationships, product-specific query languages, weaker or configurable consistency guarantees, and more complicated operations.

For example, JSON documents can preserve nested application data, logs can be ingested as semi-structured records, and a key-value store can serve values addressed by known keys. These are different workloads and may call for different database types; none implies that relational databases are unsuitable.

Schema flexibility does not mean “no schema.” Applications still depend on field names, types, required values, and invariants. Those expectations must be validated and evolved deliberately.

## Example

An e-commerce order can be represented as a document with an array of line items. That may make it convenient to retrieve an order and its purchased items together. It also duplicates product descriptions if snapshots are stored in every order, and it may not be suitable for every update or reporting workload.

```javascript
{
  order_id: "o-5001",
  customer_id: 101,
  items: [
    { product_id: "p-10", quantity: 2, unit_price: 19.99 }
  ],
  status: "paid"
}
```

This is MongoDB-style document data, not a claim that relational tables are inferior. See [relational vs. NoSQL](02-relational-vs-nosql.md) and [data models](03-nosql-data-models.md).

## When to consider NoSQL

Start with the access patterns and constraints, not a technology trend. Consider the data model, read/write ratio, transaction boundary, consistency needs, growth and distribution, operational skills, and reporting requirements. NoSQL is appropriate only when its model and trade-offs fit better than the alternatives.

## Check your understanding

- Why is “NoSQL database” not a precise model description?
- What costs can accompany flexible document shapes?
- What workload requirements would lead you to compare a document store with a relational database?
