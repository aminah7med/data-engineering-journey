# 17. Transactions and ACID

## Definition and purpose

A transaction groups multiple SQL statements into one logical unit of work. Transactions help maintain data correctness and consistency.

## Example

```sql
START TRANSACTION;

UPDATE inventory SET quantity = quantity - 1 WHERE product_id = 3;
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (1007, 3, 1, 299.99);

COMMIT;
```

If something fails before `COMMIT`, you can use `ROLLBACK`.

## ACID properties

- Atomicity: all or nothing
- Consistency: valid transitions only
- Isolation: concurrent transactions are separated
- Durability: committed data survives failures

## Common mistakes

- Forgetting a rollback when a workflow fails halfway
- Assuming a transaction is automatically committed in every context
- Not understanding isolation levels in concurrent systems

## Data Engineering use case

Transactions are essential when a pipeline needs to update multiple tables without leaving partial results. Data engineers must consider failure recovery and consistency when writing safe warehouse and operational updates.

## Interview questions

- What is the purpose of a transaction?
- What does ACID stand for?
- Why are transactions important in financial or inventory workflows?
