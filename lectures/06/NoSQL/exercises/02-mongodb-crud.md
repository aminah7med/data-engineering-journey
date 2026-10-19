# Exercise 02 — MongoDB CRUD

Run in `mongosh` with `nosql_learning` selected. These operations use a separate practice customer and do not alter the supplied sample records.

1. Insert a customer with `customer_id: 901`, a fictional name, and `city: "Cairo"`.
2. Read the inserted customer by `customer_id`.
3. Update only that customer's city to `"Giza"` with `$set`; inspect the result counts.
4. Find all customers whose city is `"Cairo"`, projecting only `customer_id` and `name`.
5. Delete only the practice customer with `customer_id: 901`. Confirm the delete count and verify no matching practice document remains.
6. Explain why an unfiltered `deleteMany({})` is inappropriate here.

Use `insertOne`, `find`, `updateOne`, `deleteOne`, and check each operation's result before proceeding. If an old practice record with ID 901 exists, inspect it and choose a different unused practice ID rather than overwriting it.
