# 07. Graph Databases

Graph databases represent entities as nodes and relationships as edges. Nodes and edges can both carry properties. This model makes connected-data traversals a first-class operation.

```text
(Customer {customer_id: 101}) -[PURCHASED {order_id: "o-5001"}]-> (Product {product_id: "p-10"})
```

## Good fits

- Recommendations based on shared interests or purchases.
- Fraud investigations that follow networks of accounts, devices, or transactions.
- Access-control and dependency relationships.
- Social or organizational graphs.

The key question is whether the workload repeatedly traverses relationships, not just whether records are “connected” conceptually. A few fixed joins may be simpler and better served by relational tables.

## Trade-offs

Graph query languages, partitioning, traversal behavior, and transaction guarantees vary. Large graph distribution and high-degree nodes can be challenging. A graph model may be a specialized serving store alongside a relational or document source of record.
