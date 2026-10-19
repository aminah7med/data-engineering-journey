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
