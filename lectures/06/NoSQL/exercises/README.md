# NoSQL Exercises

Work in the dedicated `nosql_learning` database and use the supplied [sample dataset](setup/sample-data.json). Follow the setup instructions in the [NoSQL learning-path README](../README.md#mongodb-setup-and-sample-data) before starting. The import script refuses to write into any nonempty target collection and does not drop data.

## Exercises

1. [Document structures and modeling](01-document-modeling.md)
2. [MongoDB CRUD operations](02-mongodb-crud.md)
3. [Aggregation pipeline](03-aggregation-pipeline.md)
4. [Data quality and duplicates](04-data-quality-and-duplicates.md)

Exercises use MongoDB Shell (`mongosh`) syntax. They are practice prompts, not SQL. Use the separate [solutions guide](solutions/README.md) only after attempting the questions.

## Learning goals

- Inspect nested documents, arrays, optional fields, and explicit `null`.
- Compare embedding and referencing using actual access patterns.
- Practice reads and safely filtered writes.
- Build grouped and transformed results with pipeline stages.
- Identify duplicate business IDs and missing fields.

## Cleanup

No cleanup is required to complete the read-only exercises. Exercise 02 creates a `customer_id: 901` practice customer and then deletes only that matching record. Do not run broad deletion or database-drop commands. To reset sample data, first decide what existing practice records to preserve; do not use an automatic destructive reset.
