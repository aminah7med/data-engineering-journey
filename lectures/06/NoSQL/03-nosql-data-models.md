# 03. NoSQL Data Models

“NoSQL” groups several distinct models. Selecting a model around the application's access patterns is more important than selecting a product based on a broad category label.

| Model | Core representation | Typical fit | Common trade-off |
|---|---|---|---|
| Key-value | A key maps to an opaque value | Sessions, cache entries, feature flags | Queries are generally centered on known keys |
| Document | Self-contained records with nested fields and arrays | Product catalogs, content, order aggregates | Duplication and relationship management require design |
| Wide-column | Rows addressed by keys with flexible, grouped columns | Large event/time-series or write-heavy workloads | Query and partition design are crucial; arbitrary joins are not the focus |
| Graph | Nodes connected by typed, often attributed edges | Recommendations, identity, network paths | Traversals and graph operations can require specialized infrastructure |

Products sometimes combine features or use terminology differently. A product's actual partition, consistency, transaction, and query behavior matters more than its marketing category.

## Model from queries

List the required reads and writes before choosing the data shape. For each query, estimate how much data it fetches, whether it needs joins or traversals, what must be current, and how often each piece changes. A model that makes the common path simple can make another path harder.

For example, a customer profile can be a document containing a small address object, a key-value entry if it is accessed by an exact key, relational rows when address constraints and joins dominate, or graph nodes/edges if the important query is how customers are connected. These are not interchangeable designs.

## Trade-offs to document

- Read simplicity versus write amplification and duplicated values.
- Query flexibility versus predictable partition-local access.
- Stronger cross-record consistency versus availability and distribution choices.
- Operational familiarity and analytics integration.

The following lessons examine each model in turn, then use MongoDB for hands-on document work.
