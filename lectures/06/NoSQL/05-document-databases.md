# 05. Document Databases

A document database stores records as structured documents, usually with nested objects and arrays. In MongoDB, documents are BSON objects held in collections. BSON extends JSON's value types, including dates, binary values, and numeric types.

Example MongoDB document:

```javascript
{
  customer_id: 101,
  name: "Ahmed Hassan",
  address: { city: "Cairo", country: "Egypt" },
  tags: ["newsletter", "returning"]
}
```

Documents in one collection can have different optional fields, but applications still need an understood schema. Validation, tests, and version-aware transformations help control that flexibility.

## Querying documents

MongoDB provides the MongoDB Query API through drivers and `mongosh`. A query filter selects documents, and a projection controls which fields are returned:

```javascript
db.customers.find(
  { "address.city": "Cairo" },
  { _id: 0, customer_id: 1, name: 1 }
);
```

The API also supports update and delete operations and aggregation pipelines. These are MongoDB-specific query capabilities, not a query language shared by all document databases.

## Good fits

Document databases can fit application records whose fields naturally form a document and are commonly read together, such as content, product catalogs, or an order with its bounded line items. They can also accept semi-structured JSON-like records with optional fields. Use validation and deliberate modeling where data quality or downstream contracts require consistent fields. If the workload depends on extensive joins, strict relational constraints, or broad analytical scans, compare a relational or analytical platform rather than assuming a document store is a replacement.

## Modeling strengths and costs

Embedding fields that are read and updated together can reduce round trips. Arrays work well for bounded child collections, such as an order's line items. References are useful when related data is shared, independently updated, or unbounded. Denormalizing can improve reads but makes updates and consistency more complex.

MongoDB limits an individual BSON document to 16 MiB. Avoid unbounded arrays and huge documents; references or another data model may be more appropriate.

## Missing versus `null` (MongoDB-specific)

A missing field is absent from the document. A field whose value is `null` exists and has an explicit null value. In MongoDB, `{ coupon_code: null }` matches documents where `coupon_code` is either `null` or missing. To distinguish:

```javascript
db.orders.find({ coupon_code: { $exists: false } }); // absent
db.orders.find({ coupon_code: { $exists: true, $eq: null } }); // present and null
```

Query operators and null semantics should be verified against the [MongoDB query documentation](https://www.mongodb.com/docs/manual/tutorial/query-for-null-fields/).
