# 10. MongoDB Data Modeling

> **MongoDB-specific:** MongoDB schema design is driven by access patterns; the same principles do not imply that every database should denormalize.

Start by writing the queries, expected cardinalities, update rates, and consistency requirements. Then decide what to embed and what to reference. A document is a good aggregate boundary when its fields are commonly read and changed together.

## Embedding

The sample embeds `items` in each order:

```javascript
db.orders.findOne(
  { order_id: "o-5001" },
  { _id: 0, order_id: 1, items: 1 }
)
```

This makes loading the order and its bounded line items straightforward and ensures the order's item list is updated atomically as one document. The trade-offs are document growth and product data duplication if item snapshots are stored.

## Referencing

The sample references customers and products using business identifiers: `orders.customer_id` and `orders.items.product_id`. These references avoid copying a complete customer or product document into every order. They require another lookup or aggregation `$lookup` to combine data, and a reference is not automatically enforced as a foreign-key constraint.

## Relationship patterns

- **One-to-one:** embed a small, always-used profile within a customer; reference a large or independently secured profile.
- **One-to-many:** embed a bounded list such as an order's items; reference unbounded events or independently managed children.
- **Many-to-many:** store references on one or both sides or use a separate relationship collection when membership changes or needs attributes.

## Decision checklist

| Consideration | Embedding tends to fit | Referencing tends to fit |
|---|---|---|
| Access | Parent and child read together | Independent reads or many access paths |
| Cardinality | Bounded | Large or unbounded |
| Updates | Shared lifecycle and atomic update | Independent, frequent updates |
| Duplication | Small or acceptable snapshots | Shared values must stay current |

MongoDB has a 16 MiB document limit. Excessive embedding can create oversized documents; excessive referencing can make common reads require multiple operations. There is no universal normalization rule—measure query patterns and write costs.

## Schema evolution

Optional fields make gradual changes possible but also create mixed versions. Validate required values, use explicit versioning when migrations need it, make readers tolerant during rollout, and backfill in bounded batches. Avoid silently interpreting missing fields as valid defaults unless that is the documented contract.
