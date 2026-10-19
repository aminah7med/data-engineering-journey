# 04. Key-Value Databases

A key-value database stores values addressed by keys. The value may be opaque to the database or have limited structure, depending on the product. The simplest access is “retrieve or update the value for this known key.”

```text
Key: session:9f31
Value: { "customer_id": 101, "expires_at": "2026-10-20T12:00:00Z" }
```

## Good fits

- Session state with expiration.
- Cache entries for frequently requested results.
- Small configuration values or feature flags addressed by known name.
- Fast lookups where access is naturally keyed.

## Trade-offs

A key-value model is not automatically a cache, and its persistence, durability, consistency, expiration, and replication behavior depend on the product and configuration. Queries by arbitrary fields or relationships may be inconvenient or require another index/search system. Key design also affects namespace collisions and distribution.

Use a key-value store when the dominant access is key-based and the operational guarantees fit. Use a document, relational, graph, or search-oriented system when the required query patterns demand richer structure or relationships.

## E-commerce comparison

An application might cache a computed product summary under `product-summary:p-10`, with a time-to-live. The canonical product record could remain in MongoDB or a relational database. Cache invalidation, expiration, and stale data behavior must be designed rather than assumed.
