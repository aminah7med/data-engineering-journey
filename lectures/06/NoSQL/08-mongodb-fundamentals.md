# 08. MongoDB Fundamentals

> **MongoDB-specific:** examples in this section use MongoDB Shell (`mongosh`) and MongoDB operators.

MongoDB stores BSON documents in collections, which are grouped in databases. A document has a unique `_id` field; MongoDB creates an `ObjectId` if an insert omits it. The practice dataset uses readable string `_id` values for easier inspection and separate business identifiers such as `customer_id`.

```javascript
use nosql_learning
db.customers.findOne({ customer_id: 101 })
```

`use` selects a database in the shell; a database may not be physically created until data is written. `findOne()` returns one matching document or `null`.

## BSON and document structure

BSON is MongoDB's binary serialization format. It supports JSON-like objects and arrays as well as additional types such as `ObjectId`, dates, and numeric types. The provided JSON file uses standard JSON strings for timestamps; the sample import script converts `order_date` strings into JavaScript `Date` values before insertion.

Collections can contain documents with optional fields. This does not remove the need for a schema contract. For example, downstream code may require `customer_id` to be an integer even if MongoDB permits some records to omit it.

## Inspect the practice collections

```javascript
show collections
db.customers.find({}, { _id: 0, customer_id: 1, name: 1, city: 1 })
db.orders.findOne({ order_id: "o-5001" })
db.products.find({ active: true })
```

Projection fields use `1` to include and `0` to exclude; except for `_id`, inclusion and exclusion projections should not be mixed. These examples are MongoDB query syntax, not SQL.

## Database and collection safety

All exercises target only `nosql_learning`. The provided import script refuses to insert if target collections are nonempty. It does not issue `dropDatabase()`, `drop()`, or mass-delete commands. Read a command's target and filter before running write operations.

Official references: [MongoDB document](https://www.mongodb.com/docs/manual/core/document/), [BSON types](https://www.mongodb.com/docs/manual/reference/bson-types/), [mongosh](https://www.mongodb.com/docs/mongodb-shell/).
