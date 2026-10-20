# 23. Stored Functions and Stored Procedures

## Definition and purpose

MySQL routines are named programs stored in a database. A **stored function** returns one value and can be used in an expression. A **stored procedure** is invoked with `CALL` and can perform a sequence of statements, return result sets, and use output parameters. They are not interchangeable.

Examples target **MySQL 8.4** and the course's `data_engineering_shop` schema, including `orders` and `order_items`.

## Built-in functions, stored functions, and procedures

- **Built-in functions**, such as `ROUND()` and `CURRENT_DATE`, are provided by MySQL and can be called in SQL expressions.
- A **stored function** is a SQL routine created with `CREATE FUNCTION`. It accepts parameters, returns one declared type, and can be used in expressions such as `SELECT`.
- A loadable **user-defined function (UDF)** extends MySQL with a function supplied by an installed component, typically written in C or C++. This is different from a stored SQL function.
- A **stored procedure** is created with `CREATE PROCEDURE` and invoked as a statement using `CALL`. It is suited to multi-step operations and can return output parameters or result sets.

## Creating and calling a stored function

This function calculates the price of one order-item unit after a percentage discount. It assumes the caller supplies a nonnegative price and a discount between 0 and 100:

```sql
DELIMITER //

CREATE FUNCTION discounted_unit_price(
    p_unit_price DECIMAL(10,2),
    p_discount_pct DECIMAL(5,2)
)
RETURNS DECIMAL(10,2)
DETERMINISTIC
NO SQL
BEGIN
    IF p_unit_price < 0 OR p_discount_pct < 0 OR p_discount_pct > 100 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Price must be nonnegative and discount must be between 0 and 100';
    END IF;

    RETURN ROUND(p_unit_price * (1 - p_discount_pct / 100), 2);
END//

DELIMITER ;
```

Call the function in a `SELECT` expression:

```sql
SELECT
    order_item_id,
    unit_price,
    discount_pct,
    discounted_unit_price(unit_price, discount_pct) AS net_unit_price
FROM order_items
WHERE item_status = 'active';
```

The function's parameters are input values. `RETURNS` declares the type of the single result, and `RETURN` supplies that result. The `IF ... THEN ... END IF` block demonstrates basic control flow; `SIGNAL` reports invalid inputs rather than silently returning a misleading value.

`DETERMINISTIC` means the function returns the same result for the same inputs. `NO SQL` declares that it does not read or write SQL data. Those declarations describe the routine and may matter for binary logging and server configuration; do not label a function deterministic or `NO SQL` unless that is true.

If either input is `NULL`, the comparisons do not evaluate to true and the arithmetic result is `NULL`; add explicit null validation if the business rule should reject null inputs.

Remove this routine definition with:

```sql
DROP FUNCTION IF EXISTS discounted_unit_price;
```

Dropping the function does not change rows in `order_items`.

## Creating and calling a stored procedure

This procedure counts orders for a customer. It accepts a customer ID through an `IN` parameter and returns the count through an `OUT` parameter:

```sql
DELIMITER //

CREATE PROCEDURE count_customer_orders(
    IN p_customer_id INT,
    OUT p_order_count BIGINT
)
READS SQL DATA
BEGIN
    SELECT COUNT(*)
    INTO p_order_count
    FROM orders
    WHERE customer_id = p_customer_id;
END//

DELIMITER ;
```

Call it with a session variable to receive the output:

```sql
CALL count_customer_orders(1, @order_count);
SELECT @order_count AS order_count;
```

Parameter modes:

- `IN` passes a value into the procedure. It is the default mode.
- `OUT` returns a value to the caller.
- `INOUT` passes an initial value in and returns its modified value.

`CALL` executes a procedure; it is not used to invoke a stored function. Remove the procedure definition with:

```sql
DROP PROCEDURE IF EXISTS count_customer_orders;
```

## The role of `DELIMITER`

In the MySQL command-line client, a semicolon normally ends the current input statement. A routine body contains internal semicolons, so the client would otherwise submit an incomplete `CREATE FUNCTION` or `CREATE PROCEDURE` statement.

`DELIMITER //` tells the **client** to treat `//` as the statement terminator while the routine is entered. `END//` finishes the complete `CREATE` statement; `DELIMITER ;` restores the usual terminator.

`DELIMITER` is a command interpreted by the MySQL command-line client. It is **not SQL sent to the MySQL server**. Other clients, drivers, and migration tools may have their own script parsing rules; follow their documentation rather than sending `DELIMITER` as a server statement.

## When to use routines—and when not to

Stored functions can be useful for small, deterministic rules that need a consistent scalar expression in multiple queries. Stored procedures can be useful for database-side workflows that naturally involve several statements, parameterized operations, or a result set and output values.

Ordinary SQL is often better when a query, CTE, or view already expresses the transformation clearly. Keeping transformations in application or pipeline code may also make them easier to test, version, and deploy across database platforms. Avoid creating a routine solely to shorten a one-off query.

## Restrictions, error handling, and maintainability

- Stored functions are more restricted than procedures. In particular, they cannot perform transaction-control statements such as `COMMIT` or `ROLLBACK`, and cannot return result sets using a plain `SELECT` to the caller. They return a scalar value instead.
- Stored functions cannot use prepared statements for dynamic SQL or statements that explicitly or implicitly commit a transaction.
- Stored functions cannot modify tables in ways MySQL prohibits for functions, including modifying a table that is already being used by the statement that invoked the function. Do not use a function as a hidden side-effect mechanism.
- Procedures support broader procedural workflows, but that does not make them automatically safe or fast. Make transaction boundaries explicit and consider who owns the transaction.
- Use `DECLARE ... HANDLER` for expected SQL conditions when appropriate. If an exception should fail the operation, propagate it with `RESIGNAL` rather than swallowing it and reporting success. An `EXIT HANDLER FOR SQLEXCEPTION` can be used to clean up work, but only roll back a transaction the routine itself is responsible for.
- Give routines clear names, parameter types, and documented behavior. Keep source definitions in version control and deploy changes through a reviewed migration process.
- Routine creation and execution require appropriate privileges. Review `SQL SECURITY DEFINER` versus `SQL SECURITY INVOKER` and grant only necessary access, especially when routines expose protected data.
- Stored routines do not automatically improve performance. A scalar function called for every row can add overhead, and wrapping indexed columns in function calls can prevent efficient index use. Inspect query plans and test with representative data.
- Stored routines can create database-specific application logic, versioning dependencies, and debugging challenges. Consider these operational costs before moving logic into the server.

## Data Engineering use cases

- A stored function can centralize a small shared calculation, such as a validated line-price calculation used in multiple SQL queries.
- A stored procedure can run a parameterized database-side maintenance step and return counts or status values.
- Procedures may support controlled batch operations, but design transaction scope, retries, idempotency, and failure recovery explicitly.
- For multi-stage transformations, complex validation, or cross-platform pipelines, ordinary SQL scripts, CTEs, or orchestration code may be easier to test and monitor.

Record routine definitions in migrations, test both valid and invalid inputs, and monitor failures and execution time as part of the pipeline.

## Common mistakes

- Calling a stored procedure as if it were a scalar function, or trying to use a procedure in a `SELECT` expression.
- Omitting `RETURNS` or a `RETURN` value in a stored function.
- Treating `OUT` and `INOUT` parameters as ordinary input-only arguments.
- Forgetting that `DELIMITER` is a client command, not a SQL statement for the server.
- Declaring a function `DETERMINISTIC` or `NO SQL` when it reads changing table data or depends on session state.
- Hiding updates or other side effects inside a function.
- Catching every SQL exception and silently continuing with success-shaped output.
- Assuming a routine is faster or more portable than an ordinary query.

## Interview questions

- How does a built-in function differ from a stored function and a stored procedure?
- What are `IN`, `OUT`, and `INOUT` procedure parameters?
- What do `RETURNS` and `RETURN` do in a stored function?
- Why is `DELIMITER` used in the MySQL command-line client, and is it sent to the server?
- Why are stored functions restricted from transaction control and returning result sets?
- How should a procedure handle an error that must fail the operation?
- When would an ordinary SQL query or CTE be preferable to a stored routine?
- What performance and maintainability costs should be considered before adding routines?

## Official documentation

- [MySQL 8.4 `CREATE FUNCTION` statement](https://dev.mysql.com/doc/refman/8.4/en/create-procedure.html)
- [MySQL 8.4 `CREATE PROCEDURE` statement](https://dev.mysql.com/doc/refman/8.4/en/create-procedure.html)
- [MySQL 8.4 stored program restrictions](https://dev.mysql.com/doc/refman/8.4/en/stored-program-restrictions.html)
- [MySQL 8.4 stored program error handling](https://dev.mysql.com/doc/refman/8.4/en/condition-handling.html)
