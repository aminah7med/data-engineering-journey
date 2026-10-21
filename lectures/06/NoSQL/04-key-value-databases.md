# 04. Key-Value Databases

A key-value database stores values addressed by keys. The value may be opaque to the database or have limited structure, depending on the product. The simplest access is “retrieve or update the value for this known key.”

```text
Key: session:9f31
Value: { "customer_id": 101, "expires_at": "2026-10-20T12:00:00Z" }
```

## Redis and key-value access

Redis is an example of a key-value database. Its primary command interface uses commands such as `SET` and `GET`; applications commonly access it with a client library, and developers can run commands interactively with `redis-cli`.

```text
SET session:9f31 "{\"customer_id\":101}" EX 3600
GET session:9f31
```

`SET` stores or replaces the value associated with a key; `GET` retrieves the value for that key. The optional `EX 3600` sets a 3,600-second expiration. Redis also supports data structures and additional interfaces, but it does not use SQL as its primary command interface. Its persistence, replication, expiration, and other behavior depend on configuration and the Redis version or deployment.

## Python dictionary analogy

A Python dictionary is a useful conceptual analogy because it maps keys to values:

```python
session = {"customer_id": 101}
sessions = {"session:9f31": session}
sessions["session:9f31"]  # lookup by key
sessions["session:9f31"] = {"customer_id": 101, "active": True}  # update
del sessions["session:9f31"]  # delete
```

This analogy explains key-based lookup, not database equivalence. A Python dictionary is an in-memory programming-language data structure; by itself, it does not provide database persistence, distribution across machines, replication, concurrent client access, or the operational controls of a database.

## Good fits

- Session state with expiration.
- Cache entries for frequently requested results.
- Small configuration values or feature flags addressed by known name.
- Fast lookups where access is naturally keyed.

## Trade-offs

A key-value model is not automatically a cache, and its persistence, durability, consistency, expiration, and replication behavior depend on the product and configuration. Queries by arbitrary fields or relationships may be inconvenient or require another index/search system. Key design also affects namespace collisions and distribution.

Use a key-value store when the dominant access is key-based and the operational guarantees fit. Use a document, relational, graph, or search-oriented system when the required query patterns demand richer structure or relationships.

## Redis compared with MongoDB and relational databases

Redis is commonly used for fast access by a known key, such as retrieving a cached result or session value. MongoDB stores BSON documents in collections and supports queries over document fields, nested values, and arrays. Relational databases store data in tables with defined relationships and are commonly queried with SQL, constraints, and joins. These models support different access patterns; Redis is not a drop-in replacement for either database when the application needs document queries, relational joins, or database-enforced relationships.

## Data Engineering context

A Data Engineer may encounter Redis as a low-latency cache in front of an operational database or API, reducing repeated reads for frequently requested reference data. A pipeline or service may also use it for short-lived state, deduplication keys, or rate-limiting counters, when Redis's configured persistence and consistency guarantees are appropriate. Redis is generally a serving or operational component in these workflows, not automatically the durable source of truth or an analytical warehouse. Expiration, invalidation, recovery, and stale-value behavior should be part of the design.

## E-commerce comparison

An application might cache a computed product summary under `product-summary:p-10`, with a time-to-live. The canonical product record could remain in MongoDB or a relational database. Cache invalidation, expiration, and stale data behavior must be designed rather than assumed.
