# Control Flow

> 📌 **Status:** 🟡 In Progress

## 📖 Overview

**Control Flow** determines the order in which statements are executed in a program.

By default, Python executes statements sequentially, from top to bottom. Control flow statements allow a program to make decisions, repeat operations, and change its execution path based on conditions.

Control flow is essential in **Data Engineering** because pipelines often need to:

- Validate incoming records.
- Process multiple files or rows.
- Skip invalid records.
- Retry or stop operations based on conditions.
- Apply different transformations depending on the data.

This section covers conditional statements, loops, nested loops, loop control statements, and common control flow patterns.

---

## 🧠 Concepts

### 1. Sequential Execution

Sequential execution means that statements run in the order in which they appear.

```python
x = 10
y = 20

result = x + y
print(result)

print("Processing completed")
```

Python executes each statement before moving to the next one, unless a control flow statement changes that behavior.

### 2. Conditional Statements

Conditional statements execute code depending on whether a condition evaluates to `True` or `False`.

#### `if`

Executes a block when its condition is true.

```python
age = 21

if age >= 18:
    print("Adult")
```

#### `if-else`

Chooses between two execution paths.

```python
temperature = 30

if temperature > 25:
    print("Hot weather")
else:
    print("Moderate weather")
```

#### `if-elif-else`

Checks multiple conditions in order. The first condition that evaluates to `True` determines which branch executes.

```python
score = 85

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Very Good")
elif score >= 60:
    print("Pass")
else:
    print("Fail")
```

**Important:** Once a branch executes, the remaining branches in the same conditional chain are skipped.

### 3. Comparison Operators

Comparison operators compare values and produce a Boolean result.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `x == 10` |
| `!=` | Not equal to | `x != 10` |
| `>` | Greater than | `x > 10` |
| `<` | Less than | `x < 10` |
| `>=` | Greater than or equal to | `x >= 10` |
| `<=` | Less than or equal to | `x <= 10` |

Example:

```python
amount = 500

print(amount > 100)   # True
print(amount == 500)  # True
print(amount != 0)    # True
```

Do not confuse `=` with `==`:

- `=` assigns a value to a name.
- `==` compares two values.

### 4. Logical Operators

Logical operators combine or modify conditions.

| Operator | Meaning | Example |
|---|---|---|
| `and` | Both conditions must be true | `age >= 18 and age <= 60` |
| `or` | At least one condition must be true | `status == "active" or status == "pending"` |
| `not` | Reverses the truth value | `not is_valid` |

Example:

```python
age = 25
is_verified = True

if age >= 18 and is_verified:
    print("Access granted")
```

Python's `and` and `or` operators use short-circuit evaluation: the second operand may not be evaluated if the first operand determines the result.

### 5. Truthy and Falsy Values

Python conditions do not have to contain an explicit Boolean expression. Python evaluates the truth value of the object.

Common falsy values include:

- `False`
- `None`
- Numeric zero, such as `0` and `0.0`
- Empty strings, such as `""`
- Empty collections, such as `[]`, `{}`, and `set()`

Most other values are truthy.

```python
records = []

if records:
    print("Records found")
else:
    print("No records found")
```

Because `records` is empty, the `else` branch executes.

This pattern is useful when checking whether a collection contains any elements.

### 6. `for` Loops

A `for` loop iterates over the items of an iterable, such as a list, tuple, string, dictionary, or range.

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

The loop assigns each item to `number` and executes the loop body.

#### Using `range()`

`range()` generates a sequence of integers.

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

The stop value is excluded.

You can also specify a start and step:

```python
for i in range(2, 10, 2):
    print(i)
```

Output:

```text
2
4
6
8
```

#### Iterating Over a Dictionary

```python
order = {
    "order_id": 101,
    "amount": 250
}

for key, value in order.items():
    print(key, value)
```

Using `.items()` provides each dictionary key and its corresponding value.

### 7. `while` Loops

A `while` loop repeats as long as its condition remains true.

```python
count = 1

while count < 4:
    print(count)
    count += 1
```

Output:

```text
1
2
3
```

The variable `count` is updated on every iteration. When it reaches `4`, the condition becomes false and the loop stops.

**Important:** Make sure the condition can eventually become false, or use an intentional termination mechanism. Otherwise, the loop may run indefinitely.

### 8. Nested Loops

A nested loop is a loop inside another loop.

```python
for i in range(1, 3):
    for j in range(1, 4):
        print(i, j)
```

The inner loop completes its iterations for each iteration of the outer loop.

If the outer loop runs `m` times and the inner loop runs `n` times per outer iteration, the body executes `m × n` times.

For similarly sized inputs, nested loops may have \(O(n^2)\) time complexity.

However, nested loops are not automatically inefficient. Their performance depends on the amount of work performed, input size, and algorithm. Some tasks naturally require nested iteration.

### 9. `break`

The `break` statement immediately terminates the nearest enclosing loop.

```python
for number in range(10):
    if number == 5:
        break

    print(number)
```

Output:

```text
0
1
2
3
4
```

`break` is useful when a stopping condition has been reached or a required result has been found.

### 10. `continue`

The `continue` statement skips the rest of the current iteration and proceeds to the next iteration.

```python
for number in range(5):
    if number == 2:
        continue

    print(number)
```

Output:

```text
0
1
3
4
```

`continue` can be used to skip records that should not be processed further.

### 11. `pass`

The `pass` statement does nothing. It can serve as a placeholder when Python syntax requires a statement but the implementation is not ready.

```python
for record in []:
    pass
```

`pass` does not skip an iteration like `continue`, and it does not terminate a loop like `break`.

### 12. Loop `else`

Python allows a `for` or `while` loop to have an `else` block.

The `else` block executes when the loop finishes normally, but not when it is terminated by `break`.

```python
for number in range(3):
    if number == 5:
        break
else:
    print("Loop completed without break")
```

Output:

```text
Loop completed without break
```

This feature is useful in search operations when you want to distinguish between finding an item and finishing the search without finding it.

---

## 💻 Syntax & Examples

### Example 1: Validate an Order

```python
order = {
    "order_id": 101,
    "amount": 250,
    "status": "paid"
}

if order["amount"] <= 0:
    print("Invalid amount")
elif order["status"] == "paid":
    print("Order is ready for the next stage")
else:
    print("Order requires further processing")
```

This example demonstrates how conditions can select a processing path based on record values.

In production code, validate required fields and data types before accessing them directly.

### Example 2: Process Multiple Records

```python
orders = [
    {"order_id": 101, "amount": 250},
    {"order_id": 102, "amount": -10},
    {"order_id": 103, "amount": 500}
]

for order in orders:
    if order["amount"] <= 0:
        print("Invalid order:", order["order_id"])
        continue

    print("Processing order:", order["order_id"])
```

The loop processes each order and skips the remaining processing steps for records with invalid amounts.

### Example 3: Count Valid Records

```python
records = [
    {"id": 1, "valid": True},
    {"id": 2, "valid": False},
    {"id": 3, "valid": True},
    {"id": 4, "valid": True}
]

valid_count = 0

for record in records:
    if record["valid"]:
        valid_count += 1

print("Valid records:", valid_count)
```

Output:

```text
Valid records: 3
```

### Example 4: Search for a Record

```python
orders = [
    {"order_id": 101, "amount": 250},
    {"order_id": 102, "amount": 400},
    {"order_id": 103, "amount": 150}
]

target_id = 102

for order in orders:
    if order["order_id"] == target_id:
        print("Order found:", order)
        break
else:
    print("Order not found")
```

The `break` statement stops the loop after the matching order is found.

---

## ⚠️ Common Mistakes

1. **Using `=` instead of `==` in a comparison:** `=` assigns a value; `==` compares values.
2. **Forgetting the colon:** Conditional statements and loop headers require a colon.
3. **Incorrect indentation:** Indentation defines the body of each condition and loop.
4. **Creating an infinite `while` loop:** Ensure the loop's state changes or that an intentional stopping mechanism exists.
5. **Off-by-one errors with `range()`:** The stop value is excluded.
6. **Confusing `break` and `continue`:** `break` terminates the nearest loop; `continue` skips to the next iteration.
7. **Assuming `pass` skips an iteration:** It is a no-operation placeholder.
8. **Using nested loops without considering complexity:** Estimate how many times the inner body executes and whether a more efficient approach exists.
9. **Accessing missing dictionary keys:** Validate the record or use `.get()` when an absent key is an expected possibility.
10. **Assuming an `else` after a loop behaves like an `if-else`:** Loop `else` executes when the loop completes normally without `break`.

---

## 👨‍💻 Data Engineering Connection

Control flow is used throughout data ingestion, transformation, validation, and orchestration.

### 1. Data Validation

Conditions allow pipelines to check records before loading them into a destination.

```python
for record in records:
    if record.get("order_id") is None:
        print("Missing order ID")
        continue

    if record.get("amount", 0) <= 0:
        print("Invalid amount")
        continue

    print("Record passed these checks")
```

This is an illustrative example. Production pipelines should distinguish missing values from legitimate zero values and validate data types before performing numeric comparisons.

### 2. Filtering Records

Loops and conditions can select records that satisfy business rules.

```python
orders = [
    {"id": 1, "status": "paid"},
    {"id": 2, "status": "pending"},
    {"id": 3, "status": "paid"}
]

paid_orders = []

for order in orders:
    if order["status"] == "paid":
        paid_orders.append(order)

print(paid_orders)
```

For larger datasets, SQL, Pandas, or PySpark may be more appropriate than processing every record in a standard Python loop.

### 3. Retry Logic

A `while` loop can implement basic retry logic, although production systems usually need retry limits, delays, error classification, and logging.

```python
attempt = 0
max_attempts = 3

while attempt < max_attempts:
    attempt += 1
    print("Attempt:", attempt)

    # Perform an operation and determine whether it succeeded.
```

This example demonstrates iteration only; it does not implement a real network request or retry policy.

### 4. Batch Processing

A `for` loop can process a collection of files or batches.

```python
files = ["orders_01.csv", "orders_02.csv", "orders_03.csv"]

for file_name in files:
    print("Processing:", file_name)
```

A production pipeline would also need to handle missing files, processing failures, and duplicate runs.

### 5. Connection to Apache Airflow

In Airflow, Python is used to define tasks and workflows. Conditions in task code can determine which processing path to take, while Airflow's own scheduling and branching features manage workflow execution.

**Important distinction:** A Python `if` statement controls logic inside the running code. It does not automatically control the scheduling or dependency graph of an Airflow DAG.

### 6. Connection to DataPulse

In the DataPulse project, control flow can determine how data quality issues are handled.

For example:

- If a record passes validation, continue processing.
- If a required field is missing, log the issue.
- If a duplicate is detected, apply the project's deduplication policy.
- If a critical processing step fails, report the failure and follow the defined recovery strategy.

A robust pipeline should make these decisions explicit, traceable, and testable.

---

## 🎯 Interview Questions

### Q1. What is control flow in Python?

Control flow determines the order in which statements execute, including conditional branches and repeated operations.

### Q2. What is the difference between `if`, `elif`, and `else`?

`if` checks the initial condition, `elif` checks additional conditions if earlier ones were false, and `else` handles the remaining case.

### Q3. What is the difference between a `for` loop and a `while` loop?

A `for` loop iterates over an iterable. A `while` loop repeats as long as its condition is true.

### Q4. What is the difference between `break` and `continue`?

`break` terminates the nearest enclosing loop, while `continue` skips the rest of the current iteration.

### Q5. What is an infinite loop?

An infinite loop continues without reaching a termination condition. It may be intentional, but it must have an appropriate stopping or interruption mechanism.

### Q6. What does `range(5)` produce?

It represents the integers `0`, `1`, `2`, `3`, and `4`. The stop value `5` is excluded.

### Q7. What is a nested loop?

A nested loop is a loop inside another loop. Its runtime depends on the number of iterations and the work performed in each iteration.

### Q8. When does a loop's `else` block execute?

It executes when the loop completes normally without being terminated by `break`.

### Q9. How is control flow used in a data pipeline?

It can validate records, select processing paths, skip invalid data, implement retry logic, and control how processing errors are handled.

### Q10. Why might you avoid ordinary Python loops for large datasets?

Processing records individually in Python can have substantial overhead. SQL engines, vectorized operations, or distributed frameworks such as PySpark may be more efficient for suitable workloads.

---

## 📝 Practice

### Exercise 1: Classify a Score

Write a program that classifies a score:

- `90` or higher: Excellent
- `75` to less than `90`: Very Good
- `60` to less than `75`: Pass
- Below `60`: Fail

Assume the score is between `0` and `100`. Consider how you would validate values outside that range.

### Exercise 2: Print Even Numbers

Use a `for` loop and `range()` to print all even numbers from `2` through `20`.

### Exercise 3: Understand a `while` Loop

Predict the output:

```python
x = 1

while x < 3:
    print(x)
    x += 1
```

Explain why the loop stops.

### Exercise 4: Use `break` and `continue`

Given the following code, predict the output:

```python
for number in range(1, 8):
    if number == 3:
        continue

    if number == 6:
        break

    print(number)
```

Explain which numbers are skipped and why the loop terminates.

### Exercise 5: Validate Orders

Given the following records:

```python
orders = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": -20},
    {"id": 3, "amount": 0},
    {"id": 4, "amount": 250}
]
```

Write a loop that prints valid orders with positive amounts and identifies invalid orders.

### Exercise 6: Search for a Customer

Given a list of customer dictionaries, search for a specific customer ID. Print the matching record and stop searching once it is found. If no match exists, print `"Customer not found"`.

### Exercise 7: Data Engineering Scenario

A pipeline receives records from an API. Some records have missing IDs, some have invalid amounts, and others are valid.

Design the control flow for the pipeline:

1. Check whether the ID exists.
2. Validate the amount.
3. Log invalid records.
4. Continue processing valid records.
5. Explain when a pipeline should skip one record versus stop the entire task.

### Exercise 8: Interview Challenge

Explain the difference between using nested loops to find duplicate IDs and using a set to track previously seen IDs. Discuss the expected time complexity and why the set-based approach is often more efficient for hashable IDs.

---

> **Next Step:** Complete the practice exercises and review the examples. Change the status to `✅ Completed` only after you can explain the main concepts and solve the exercises independently.