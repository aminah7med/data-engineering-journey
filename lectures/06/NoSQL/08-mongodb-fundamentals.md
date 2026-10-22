# 08. MongoDB Fundamentals

> **MongoDB-specific:** examples in this section use MongoDB Shell (`mongosh`) and MongoDB operators.

MongoDB stores BSON documents in collections, which are grouped in databases. A document has a unique `_id` field; MongoDB creates an `ObjectId` if an insert omits it. The practice dataset uses readable string `_id` values for easier inspection and separate business identifiers such as `customer_id`.

```javascript
use nosql_learning
db.customers.findOne({ customer_id: 101 })
```

`use` selects a database in the shell; a database may not be physically created until data is written. `findOne()` returns one matching document or `null`.

## BSON and document structure

BSON is MongoDB's binary serialization format for storing and communicating documents. It supports JSON-like objects and arrays as well as additional types such as `ObjectId`, dates, and numeric types. JSON (JavaScript Object Notation) is a text-based data-interchange format; BSON is not JSON, though MongoDB documents have a similar structure and can be represented as JSON. The provided JSON file uses standard JSON strings for timestamps; the sample import script converts `order_date` strings into JavaScript `Date` values before insertion.

Collections can contain documents with optional fields. This does not remove the need for a schema contract. For example, downstream code may require `customer_id` to be an integer even if MongoDB permits some records to omit it.

## Parsing JSON before storage

Parsing converts JSON text into values a program can work with. For example, a backend can parse this JSON text:

```javascript
const jsonText = '{"customer_id": 101, "name": "Learner"}';
const document = JSON.parse(jsonText);
```

After parsing, `document` is a JavaScript object whose fields the backend can inspect. If the text is not valid JSON, parsing fails; successful parsing does not prove that the data is valid for the application.

Parsing, validation, and storage are separate steps:

- **Parsing** checks JSON syntax and converts the text into in-memory values.
- **Validation** checks whether those values meet the application's requirements, such as required fields, types, and business rules.
- **Storage** writes accepted data to a database. When a MongoDB driver inserts a JavaScript object, MongoDB stores it as a BSON document.

JSON is a text-based data-interchange format; BSON is MongoDB's binary document format. An application does not usually need to manually convert JSON text into BSON: the MongoDB driver serializes the validated object for the database.

## MongoDB query interface and basic operations

MongoDB's Query API is used through drivers and `mongosh`; it is not SQL. Common document operations include inserting a document with `insertOne()`, reading matching documents with `find()` or `findOne()`, changing fields with `updateOne()` and update operators such as `$set`, and removing a matching document with `deleteOne()`.

```javascript
db.customers.insertOne({ customer_id: 901, name: "Demo Customer" });
db.customers.findOne({ customer_id: 901 });
db.customers.updateOne(
  { customer_id: 901 },
  { $set: { city: "Cairo" } }
);
db.customers.deleteOne({ customer_id: 901 });
```

These commands illustrate create, read, update, and delete (CRUD). Run them only against the intended practice database; the [MongoDB CRUD lesson](09-mongodb-crud-operations.md) explains safe practice in more detail.

## Web application registration flow

JSON is commonly used to exchange signup data between a frontend and backend. REST describes an architectural style for designing APIs; it is not a data format or a database query language. A frontend might send a JSON request to a backend REST endpoint:

```text
Frontend → REST API → Validation → MongoDB → Response
```

For example, a signup form could send a `POST /api/registrations` request with a JSON body:

```json
{
  "email": "learner@example.com",
  "password": "user-provided-password",
  "display_name": "Learner"
}
```

Here, `email` and `password` are mandatory fields for the application, while `display_name` is optional. The backend parses the JSON request, checks that required fields are present and valid, validates field types and business rules, and rejects invalid input before writing to MongoDB. Parsing and validation are distinct: parsing makes the request available as program values, while validation determines whether those values may be accepted. It should hash the password using an appropriate password-hashing method rather than store the submitted password in plaintext.

After validation, the backend can insert a document into a `registrations` collection. On success, the API returns an appropriate success status and response, such as `201 Created`; invalid input can return `400 Bad Request`, and a duplicate email may return `409 Conflict`. Database or service failures should produce an appropriate error response without exposing sensitive implementation details.

Application-level validation handles request-specific rules and lets the API return useful client errors. MongoDB can also enforce database-level validation, such as required fields and BSON types, using collection schema validation. Database validation protects the stored data from invalid writes through other code paths, but it does not replace application validation or business logic. A unique index can enforce uniqueness for email values; checking for duplicates only in application code is not sufficient under concurrent requests.

The values and policies in this example are illustrative; actual signup rules depend on the application.

## Replica sets and read/write consistency

MongoDB replica sets maintain copies of data across nodes. Under normal operation, the **primary** accepts writes, while **secondary** nodes replicate the primary's oplog and can serve reads depending on the configured read preference. Replication is typically asynchronous, so a secondary may temporarily be behind the primary; this delay is called **replication lag**.

If the primary becomes unavailable, eligible voting members hold an **election** to select a new primary. During an election, writes may be unavailable for a time. After failover, a secondary may have replicated less recent data than the former primary, depending on timing and the acknowledged writes.

MongoDB's **write concern** controls the acknowledgement requested for a write—for example, whether it must be acknowledged by the primary alone or by a majority of voting members. Stronger acknowledgement can improve durability guarantees but may increase latency or cause writes to wait or fail when members are unavailable. **Read preference** controls which replica-set members may serve a read. Reading from secondaries can distribute read load, but can return stale data because of replication lag; reading from the primary is the default preference but should not be treated as a substitute for choosing appropriate write and read guarantees.

Read preference and write concern are separate controls: write concern describes the requested acknowledgement for writes, while read preference routes reads. Choose them according to the application's consistency, availability, and latency requirements. For more detail, see [Consistency and Replication](13-consistency-and-replication.md) and the [MongoDB replication documentation](https://www.mongodb.com/docs/manual/replication/).

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
