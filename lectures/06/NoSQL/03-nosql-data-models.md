# 03. NoSQL Data Models

“NoSQL” groups several distinct models. Selecting a model around the application's access patterns is more important than selecting a product based on a broad category label.

| Model | Core representation | Example products | Typical fit | Common trade-off |
|---|---|---|---|---|
| Key-value | A key maps to an associated value, which may be opaque to the database | Redis | Sessions, cache entries, feature flags, and other known-key lookups | Queries are generally centered on known keys |
| Document | Self-contained records with nested fields and arrays; MongoDB stores JSON-like documents as BSON | MongoDB | Product catalogs, content, and order aggregates | Duplication and relationship management require design |
| Wide-column | Rows addressed by keys with flexible, grouped columns; exact terminology varies by product | Apache Cassandra, Apache HBase | High-volume distributed workloads with access patterns planned around partition and row keys | Query and partition design are crucial; arbitrary joins are not the focus |
| Graph | Nodes connected by typed, often attributed relationships | Neo4j | Relationship queries, path traversal, identity, and recommendation analysis | Traversals and graph operations can require specialized infrastructure |

Products sometimes combine features or use terminology differently. A product's actual partition, consistency, transaction, and query behavior matters more than its marketing category.

## Query languages and access methods

NoSQL databases do not share one query language. MongoDB's MongoDB Query API supports document filters, projections, updates, and aggregation pipelines. Redis is primarily accessed through commands such as `SET` and `GET`, commonly sent through `redis-cli` or a client library using Redis protocols. Cassandra uses Cassandra Query Language (CQL), a SQL-like language designed for its data model. HBase is accessed through client APIs (including Java APIs) and the HBase shell. Neo4j uses Cypher to query nodes, relationships, and paths. The language's resemblance to SQL does not mean the products have relational semantics or interchangeable query behavior.

## Model from queries

List the required reads and writes before choosing the data shape. For each query, estimate how much data it fetches, whether it needs joins or traversals, what must be current, and how often each piece changes. A model that makes the common path simple can make another path harder.

For example, a customer profile can be a document containing a small address object, a key-value entry if it is accessed by an exact key, relational rows when address constraints and joins dominate, or graph nodes/edges if the important query is how customers are connected. These are not interchangeable designs.

## Trade-offs to document

- Read simplicity versus write amplification and duplicated values.
- Query flexibility versus predictable partition-local access.
- Stronger cross-record consistency versus availability and distribution choices.
- Operational familiarity and analytics integration.

The following lessons examine each model in turn, then use MongoDB for hands-on document work.
