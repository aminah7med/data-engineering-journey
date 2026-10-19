# 09. MongoDB CRUD Operations

> **MongoDB-specific:** run these examples in `mongosh` after importing the sample into `nosql_learning`.

CRUD means create, read, update, and delete. The examples use the sample's `customer_id: 101` record. MongoDB filters are document expressions; they are not interchangeable with SQL clauses.

## Create

```javascript
db.customers.insertOne({
  customer_id: 901,
  name: "Demo Customer",
  city: "Cairo"
});
```

`insertOne()` adds one document and generates `_id` if it is missing. This example creates a separate practice record; verify it with a read before continuing.

## Read

```javascript
db.customers.find({ city: "Cairo" });
db.customers.find(
  { customer_id: 101 },
  { _id: 0, customer_id: 1, name: 1, city: 1 }
);
```

`find()` returns a cursor for documents matching the filter. The second argument is a projection that limits returned fields.

## Update

```javascript
db.customers.updateOne(
  { customer_id: 101 },
  { $set: { city: "Alexandria" } }
);
```

`updateOne()` finds at most one match and applies `$set` to the selected field, leaving other fields unchanged. In this dataset, customer 101 is unique. Check `matchedCount` and `modifiedCount` from the result. If the filter could match duplicates, use a unique key or resolve data quality first.

## Delete

```javascript
db.customers.deleteOne({ customer_id: 901 });
```

`deleteOne()` removes at most one matching document. The preceding create step is its target. Check `deletedCount`; do not use an unfiltered delete in practice.

## More operators

```javascript
db.orders.find({ total: { $gte: 50 }, status: { $in: ["paid", "shipped"] } });
db.orders.updateOne(
  { order_id: "o-5001" },
  { $set: { status: "shipped" } }
);
```

MongoDB updates can change fields and arrays with operators such as `$inc`, `$push`, and `$pull`. Updates are atomic at the single-document level; multi-document transaction behavior has separate requirements and cost.
