# 02. Relational vs. NoSQL

Relational databases organize data into tables with declared columns, keys, constraints, and relationships. SQL is a standardized family of query languages for these systems. NoSQL includes multiple models; a document database such as MongoDB stores BSON documents in collections. Neither label alone specifies a system's consistency, transaction, or scale characteristics.

| Concern | Relational approach | NoSQL approach |
|---|---|---|
| Data shape | Tables with defined columns and relations | Depends on model: documents, key-value pairs, wide rows, or graph edges |
| Relationships | Commonly expressed with keys and joins | May use embedded data, references, denormalization, or traversals |
| Schema | Often database-enforced; schema changes are explicit | May allow varying record shapes; application validation is still needed |
| Transactions | Strong multi-row transactions are common | Varies by product; MongoDB supports multi-document transactions, with operational costs |
| Scaling | Often scaled vertically; distributed options also exist | Many products support horizontal distribution; it is not automatic or free |
| Querying | SQL supports expressive joins and analytics | Query language and capabilities vary by product/model |

The table describes common tendencies, not universal guarantees. Relational systems can scale horizontally, and NoSQL systems can support transactions and schemas. Compare actual products and workload requirements.

SQL is a mature, broadly shared language for relational databases, while NoSQL has no single query language. The interface depends on the product and model: MongoDB uses its Query API, Redis primarily uses commands such as `SET` and `GET`, Cassandra provides CQL, HBase provides APIs and shell commands, and Neo4j uses Cypher. A system may also expose client libraries or additional interfaces. Do not assume that choosing NoSQL means giving up SQL everywhere, or that every NoSQL product has the same query capabilities.

## Choosing based on workload

Choose relational storage when correctness depends on constraints across related records, flexible joins, multi-entity transactions, or mature SQL analytics are central. Consider NoSQL when a particular model directly supports important access patterns—for example, retrieving a nested aggregate as one document or serving a high-volume key lookup.

Teams often use both. A transactional application can use a document store while publishing validated data to a warehouse or lakehouse for historical, cross-domain analysis.

## Do not translate syntax mechanically

SQL:

```sql
SELECT customer_id
FROM orders
WHERE status = 'paid';
```

MongoDB Shell (`mongosh`):

```javascript
db.orders.find(
  { status: "paid" },
  { _id: 0, customer_id: 1 }
);
```

The intent is similar, but syntax, null/missing-field semantics, operators, and query-planning behavior differ. For SQL fundamentals, use the [SQL learning path](../../05/SQL/README.md).

## Decision checklist

For each candidate system, ask:

1. What are the dominant reads and writes?
2. Which records must change atomically?
3. Which fields and relationships must be constrained?
4. What consistency and availability are required during failures?
5. What is the expected data volume and distribution?
6. How will the data be operated, backed up, and analyzed?

NoSQL is not inherently faster or more scalable; its fit depends on the model, access patterns, consistency requirements, and operations.
