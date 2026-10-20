# 22. Database Normalization

## Definition and purpose

Database normalization is the process of organizing relational data into related tables so each fact is stored in an appropriate place and relationships are represented with keys. It helps reduce unnecessary duplication and prevents inconsistent changes. Normalization is a design tool, not a rule that every database must follow to the same degree.

Examples target **MySQL 8.4** and the course's e-commerce schema: `customers`, `orders`, `order_items`, and `products`.

## Why duplicate facts cause anomalies

Imagine storing order lines in one flat table that repeats customer and product details:

| order_id | order_date | customer_id | customer_name | customer_city | product_id | product_name | quantity |
|---:|---|---:|---|---|---:|---|---:|
| 501 | 2026-04-10 | 10 | Amal Nasser | Cairo | 7 | Travel Mug | 2 |
| 501 | 2026-04-10 | 10 | Amal Nasser | Cairo | 9 | Notebook | 1 |
| 502 | 2026-04-11 | 10 | Amal Nasser | Cairo | 7 | Travel Mug | 1 |

The customer's name and city repeat for every order line; product names repeat wherever a product is sold. If the same fact is stored in many rows, writes must keep every copy consistent.

This can create three common anomalies:

- **Update anomaly:** Amal moves to Alexandria. If only some of her repeated rows are updated, the table reports two different cities for the same customer.
- **Insertion anomaly:** A product is added to the catalog before it has been ordered. In this flat table, there is no order line on which to store it, unless unrelated order fields are made null or a fake order is inserted.
- **Deletion anomaly:** If the only row for a newly listed product is deleted with its order line, the product's catalog information is lost too.

Normalization separates facts with different lifecycles and links them using keys.

## Functional dependencies

A **functional dependency** describes which columns determine other columns. If every `customer_id` identifies exactly one customer name, write:

```text
customer_id -> customer_name, customer_city
```

This means that when `customer_id` is known, the name and city are determined by the current data rules. It does not mean the values never change; an update to the customer's city changes the fact associated with that ID.

For a row representing one product on one order:

```text
order_id, product_id -> quantity
order_id -> order_date, customer_id
product_id -> product_name, category
```

The first dependency uses the combination of order and product to identify a line in this simplified example. In the actual project schema, `order_item_id` is the primary key, and an order can contain multiple lines for a product; the line is therefore identified by `order_item_id` (or a suitable composite key such as `order_id` plus a line number).

## First Normal Form (1NF)

A table is in **First Normal Form (1NF)** when each row-column position holds one value from the column's intended domain and there are no repeating groups such as `product_1`, `product_2`, `product_3` or a comma-separated list of products in one cell. Each row should also be distinguishable by a key.

For example, do not store an order's products as `"7,9"` in one `product_ids` field. Store one row per order line:

| order_id | product_id | quantity |
|---:|---:|---:|
| 501 | 7 | 2 |
| 501 | 9 | 1 |

The values are atomic relative to this design: each row contains one product identifier and one quantity for that product. “Atomic” depends on the intended use; for example, storing a full address in one string may be unsuitable if the system must query or validate its components separately.

## Second Normal Form (2NF)

A table is in **Second Normal Form (2NF)** when it is in 1NF and every non-key column depends on the whole candidate key, not just part of a composite key. Partial dependencies are relevant when a candidate key contains multiple columns.

Consider order lines keyed by `(order_id, product_id)` with these columns:

```text
(order_id, product_id) -> quantity
order_id -> order_date, customer_id
product_id -> product_name, category
```

`order_date` depends only on `order_id`, and `product_name` depends only on `product_id`. These are **partial dependencies** on part of the composite key. Store the facts in separate tables:

```text
orders(order_id, customer_id, order_date, status, ...)
products(product_id, product_name, category, unit_price, ...)
order_items(order_item_id, order_id, product_id, quantity, unit_price, ...)
```

The actual course schema uses `order_item_id` as a surrogate primary key for each line. The order and product foreign keys still express the relationships. `order_items.unit_price` records the price charged on that order line; it is a historical transaction fact and can legitimately differ from the product's current catalog price.

If a table has only a single-column candidate key, it has no composite key with a proper subset, so partial dependency on part of that key does not arise. It can still have a transitive dependency and fail 3NF.

## Third Normal Form (3NF)

A table is in **Third Normal Form (3NF)** when it is in 2NF and non-key columns do not depend on other non-key columns instead of depending directly on the key. Informally, each non-key fact should describe the key, the whole key, and nothing but the key.

Suppose an order table repeats `customer_name` and `customer_city`:

```text
order_id -> customer_id
customer_id -> customer_name, customer_city
```

Therefore, `order_id -> customer_name, customer_city` indirectly through `customer_id`. This is a **transitive dependency**. Keep customer details in `customers` and store the customer key in `orders`:

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    city VARCHAR(60) NULL
);

CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATETIME NOT NULL,
    status ENUM('pending', 'paid', 'shipped', 'cancelled') NOT NULL DEFAULT 'pending',
    total_amount DECIMAL(12,2) NOT NULL DEFAULT 0.00,
    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

These abbreviated definitions illustrate the relationship in the project's schema; the complete table definitions include additional columns. A query can recover the combined information with a join when needed:

```sql
SELECT
    o.order_id,
    o.order_date,
    c.customer_id,
    c.first_name,
    c.last_name,
    c.city
FROM orders AS o
JOIN customers AS c
    ON c.customer_id = o.customer_id;
```

## Primary keys and foreign keys

A **primary key** identifies a row in its table and must be unique and not `NULL`. A **foreign key** references a candidate key—commonly a primary key—in another table and can enforce that the referenced row exists.

In this schema:

- `customers.customer_id` identifies a customer.
- `orders.order_id` identifies an order; `orders.customer_id` references its customer.
- `products.product_id` identifies a product.
- `order_items.order_id` and `order_items.product_id` reference the related order and product.

These keys let tables store each entity's facts in one place while still supporting joins. A foreign key does not by itself make a relationship one-to-one; cardinality also depends on uniqueness and the data model. For more key concepts, see [Keys and Relationships](15-keys-and-relationships.md).

## Normalization and analytical modeling

Normalization is common in **OLTP** (online transaction processing) systems, where individual records are frequently inserted or updated and consistency of current entities matters. Splitting customer, order, product, and line-item facts reduces repeated updates and supports integrity constraints.

Analytical systems often use **denormalization**: deliberately storing repeated or pre-joined values to make common scans and reports simpler or faster. A star schema, for example, may have a central fact table joined to dimensions with descriptive attributes. This is not the same design goal as an OLTP schema. Analytical models still need clear grain, key behavior, history rules, and data-quality controls; denormalization should be intentional and measured.

## Denormalization

**Denormalization** deliberately duplicates or precomputes data—for example, storing a product name on an order line as a purchase-time snapshot, or building a summary table of daily sales. It can reduce joins or expensive recalculation for a known workload, but adds storage and a consistency or refresh burden.

The project's `order_items.unit_price` is an example of a value that should not necessarily be replaced by the current `products.unit_price`: the line price represents what was charged at purchase time. This is not accidental duplication if the historical price is part of the transaction record.

Before denormalizing, identify the query or business requirement, define which copy is authoritative, and decide how duplicated values are updated or refreshed.

## Common mistakes

- Treating normalization as “make every column a separate table.” Tables should represent meaningful entities and relationships.
- Calling a table normalized merely because it has a primary key; dependencies among non-key columns still matter.
- Confusing a functional dependency with a value that is permanently immutable.
- Applying 2NF without considering candidate keys and composite keys.
- Splitting a table without preserving relationships through appropriate primary and foreign keys.
- Removing purchase-time values such as line price because a current catalog value appears to duplicate them.
- Treating a denormalized warehouse model as automatically incorrect or as a replacement rule for OLTP design.
- Assuming normalization alone guarantees good performance; indexes, query patterns, constraints, and workload also matter.

## Data Engineering use cases

- Design normalized OLTP landing or application tables to reduce conflicting copies of customer and product attributes.
- Use primary and foreign keys to detect or prevent orphan orders and order lines.
- Normalize incoming records during staging when multiple source rows describe the same entity.
- Preserve transaction-time snapshots, such as price charged, while maintaining current product attributes separately.
- Build denormalized reporting facts or aggregates for analytics with explicit refresh and reconciliation checks.

For pipelines, document the grain and dependencies of each target table, test key uniqueness and referential integrity, and decide how late updates to source entities affect downstream snapshots.

## Interview questions

- What is database normalization, and which anomalies does it help prevent?
- Explain insertion, update, and deletion anomalies with an example.
- What does a functional dependency such as `customer_id -> customer_city` mean?
- What is the difference between a partial dependency and a transitive dependency?
- What requirements distinguish 1NF, 2NF, and 3NF?
- Why can a table with a single-column primary key still violate 3NF?
- How do primary and foreign keys support a normalized schema?
- Why might `order_items` store the price charged even when `products` also has a price?
- Why might an analytical warehouse intentionally denormalize data?
- How do OLTP and analytical modeling priorities differ?
