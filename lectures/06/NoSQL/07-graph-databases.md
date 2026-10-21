# 07. Graph Databases

Graph databases represent entities as **nodes** and connections between them as typed **relationships** (also called edges). Nodes and relationships can both have **properties**: key-value attributes that describe the entity or connection. Instead of primarily joining records through foreign keys, graph queries follow these explicit relationships, making connected-data traversal a first-class operation.

```text
(Customer {customer_id: 101}) -[PURCHASED {order_id: "o-5001"}]-> (Product {product_id: "p-10"})
```

Here `Customer` and `Product` are node labels, `PURCHASED` is the relationship type, and the values in braces are properties. The arrows indicate relationship direction.

## Querying graphs with Cypher

Neo4j is a graph database that supports Cypher, a declarative query language for matching nodes and relationships. A relationship-oriented query can find products purchased by a customer:

```cypher
MATCH (c:Customer {customer_id: 101})-[:PURCHASED]->(p:Product)
RETURN p;
```

Cypher can also express path traversals across multiple relationships. The exact labels, properties, and query performance depend on the graph model and indexes.

## Social graph example

A small social graph can represent people as nodes and friendships as relationships:

```text
(Person {id: 101}) -[:FRIEND]-> (Person {id: 202}) -[:FRIEND]-> (Person {id: 303})
```

This two-edge path connects person 101 to person 303 through person 202. A friend-of-a-friend query in Neo4j can find candidates connected by two `FRIEND` relationships and rank them by the number of mutual friends:

```cypher
MATCH (person:Person {id: 101})-[:FRIEND]-(mutual)-[:FRIEND]-(candidate:Person)
WHERE candidate <> person
  AND NOT (person)-[:FRIEND]-(candidate)
RETURN candidate, count(DISTINCT mutual) AS mutualFriends
ORDER BY mutualFriends DESC;
```

This is an example of a possible recommendation approach, not a guarantee that every social network uses Neo4j or any graph database. Production recommendation systems may combine graph features with ranking models, business rules, and other data stores.

## Good fits

- Social-network analysis, such as traversing connections or finding mutual relationships.
- Friend or product recommendations based on paths and shared relationships.
- Fraud investigations that follow networks of accounts, devices, or transactions to identify suspicious connections.
- Connected-data analysis, including access-control, dependency, and organizational relationships.

Graph databases are useful when relationships are central to the query—for example, when repeatedly exploring paths, neighbors, or multi-hop connections. The key question is whether the workload repeatedly traverses relationships, not just whether records are “connected” conceptually. A few fixed joins may be simpler and better served by relational tables.

## Trade-offs

Graph query languages, partitioning, traversal behavior, and transaction guarantees vary. Large graph distribution and high-degree nodes can be challenging. A graph model may be a specialized serving store alongside a relational or document source of record.
