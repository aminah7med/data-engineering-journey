# 15. Keys and Relationships

## Definition and purpose

Keys define how tables relate to one another. They are essential for joining tables correctly and preserving data integrity.

## Key types

- Primary key: unique identifier for a row
- Foreign key: references another table?s primary key
- Candidate key: a possible unique key
- Surrogate key: generated technical identifier
- Natural/business key: values already meaningful to the business

## Example

```sql
CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

## Why this matters

A well-designed schema makes joins predictable and prevents orphan records. In Data Engineering, one must choose between business keys and surrogate keys depending on the use case.

## Common mistakes

- Treating every table as if it needs a generated key
- Forgetting to enforce foreign key relationships when they matter
- Mixing natural keys and surrogate keys in the same model without clear rules

## Data Engineering use case

A pipeline might use a business key to deduplicate incoming events while using a surrogate key for warehouse dimension tables. The trade-offs are important for idempotency and incremental loads.

## Interview questions

- What is the difference between a primary key and a foreign key?
- When would you choose a surrogate key over a natural key?
- What happens when a foreign key is broken?
