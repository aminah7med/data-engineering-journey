# Functions

> 📌 **Status:** 🟡 In Progress

## 📖 Overview

A **function** is a reusable block of code designed to perform a specific task. Functions help organize programs, reduce code duplication, improve readability, and make testing easier.

In Python, functions can receive input values through parameters, perform operations, and return results.

Functions are essential in **Data Engineering** because pipelines often repeat operations such as validating records, transforming values, cleaning data, and processing batches.

This section covers defining and calling functions, parameters and arguments, return values, scope, default arguments, keyword arguments, and built-in functions.

---

## 🧠 Concepts

### 1. Defining and Calling Functions

Use the `def` keyword to define a function.

```python
def greet():
    print("Hello, Data Engineer!")
```

Defining a function does not execute its body. The function runs when it is called.

```python
greet()
```

Output:

```text
Hello, Data Engineer!
```

**Syntax:**

```python
def function_name():
    # Function body
    pass
```

- `def` starts a function definition.
- `function_name` identifies the function.
- Parentheses contain parameters, if any.
- The colon `:` introduces the function body.
- Indentation defines the function body.

### 2. Parameters vs Arguments

A **parameter** is a name specified in a function definition. An **argument** is a value supplied when calling the function.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Amin")
```

Here:
- `name` is the parameter.
- `"Amin"` is the argument.

A function can accept multiple parameters:

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

```text
30
```

### 3. The `return` Statement

The `return` statement sends a result back to the caller and immediately exits the current function.

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)  # 30
```

The returned value can be stored, passed to another function, or used in an expression.

#### `return` vs `print()`

- `print()` displays information.
- `return` provides a value to the code that called the function.

```python
def add_and_print(a, b):
    print(a + b)

def add_and_return(a, b):
    return a + b

x = add_and_print(2, 3)
y = add_and_return(2, 3)

print(x)  # None
print(y)  # 5
```

The first function prints `5` but does not explicitly return a value. Python therefore returns `None`.

**Best practice:** Use `return` when a function needs to produce a result for further processing. Use `print()` when displaying information is the intended behavior.

### 4. Functions Without an Explicit `return`

If execution reaches the end of a function without encountering a `return` statement, Python returns `None`.

```python
def log_message(message):
    print(message)

result = log_message("Processing started")
print(result)  # None
```

A function can also return early:

```python
def validate_amount(amount):
    if amount <= 0:
        return False

    return True
```

The first `return` stops the function immediately when the condition is satisfied.

### 5. Built-in Functions

Python provides built-in functions that are available without importing a module.

Common examples include:

| Function | Purpose | Example |
|---|---|---|
| `print()` | Display output | `print("Hello")` |
| `len()` | Get the length of a collection or sequence | `len([1, 2, 3])` |
| `type()` | Get an object's type | `type(10)` |
| `int()` | Convert to an integer when possible | `int("10")` |
| `float()` | Convert to a floating-point number | `float("2.5")` |
| `str()` | Convert to a string representation | `str(100)` |
| `sum()` | Add values in an iterable | `sum([1, 2, 3])` |
| `min()` | Find the minimum value | `min([3, 1, 2])` |
| `max()` | Find the maximum value | `max([3, 1, 2])` |
| `sorted()` | Return a new sorted list | `sorted([3, 1, 2])` |
| `range()` | Represent a sequence of integers | `range(5)` |
| `enumerate()` | Iterate with an index and value | `enumerate(["a", "b"])` |
| `zip()` | Iterate over multiple iterables together | `zip([1, 2], ["a", "b"])` |
| `isinstance()` | Check whether an object matches a type | `isinstance(10, int)` |

Example:

```python
numbers = [10, 20, 30]

print(len(numbers))   # 3
print(sum(numbers))   # 60
print(min(numbers))   # 10
print(max(numbers))   # 30
print(sorted(numbers, reverse=True))  # [30, 20, 10]
```

Built-in functions are different from functions you define yourself. They are part of Python's built-in namespace.

### 6. Default Parameters

A function parameter can have a default value. The default is used when the caller omits that argument.

```python
def greet(name, message="Welcome"):
    print(f"{message}, {name}!")

greet("Amin")
greet("Amin", "Good morning")
```

Output:

```text
Welcome, Amin!
Good morning, Amin!
```

Parameters without default values must generally be supplied before parameters with default values in a function definition.

### 7. Positional and Keyword Arguments

**Positional arguments** are matched to parameters by their position.

```python
def describe_order(order_id, amount):
    print(order_id, amount)

describe_order(101, 250)
```

**Keyword arguments** identify parameters by name.

```python
describe_order(amount=250, order_id=101)
```

Keyword arguments can improve readability when a function accepts multiple parameters.

### 8. Variable Scope

Scope determines where a name can be accessed.

#### Local Scope

A variable created inside a function is normally local to that function.

```python
def calculate():
    result = 10 + 5
    return result

print(calculate())  # 15
```

The local variable `result` is not automatically available outside the function.

#### Global Scope

A name defined at the module level can generally be accessed inside functions.

```python
tax_rate = 0.14

def calculate_tax(amount):
    return amount * tax_rate

print(calculate_tax(100))
```

Functions can read the global `tax_rate`, but assigning to a global name inside a function requires additional care.

**Best practice:** Prefer passing dependencies as parameters and returning results instead of relying heavily on global variables.

### 9. Functions and Reusability

Functions let you define logic once and use it in multiple places.

Without a function:

```python
price1 = 100
total1 = price1 * 1.14

price2 = 200
total2 = price2 * 1.14
```

With a function:

```python
def calculate_total(price, tax_rate=0.14):
    return price * (1 + tax_rate)

total1 = calculate_total(100)
total2 = calculate_total(200)
```

The second version avoids repeating the calculation and makes the tax rate easier to manage.

### 10. Functions Should Have Clear Responsibilities

A function is easier to understand and test when it performs one clearly defined task.

```python
def is_valid_amount(amount):
    return amount > 0

def calculate_total(amount, tax_rate):
    return amount * (1 + tax_rate)
```

The first function validates a simple business rule. The second performs a calculation.

Separating responsibilities makes code easier to test, debug, and maintain.

### 11. Docstrings

A docstring describes what a function does. It is written as a string at the beginning of the function body.

```python
def calculate_total(amount, tax_rate):
    """Calculate the total amount including tax."""
    return amount * (1 + tax_rate)
```

Docstrings help developers understand a function's purpose, parameters, return value, and relevant assumptions.

### 12. Lambda Functions

A `lambda` expression creates a small anonymous function consisting of a single expression.

```python
square = lambda number: number ** 2

print(square(5))  # 25
```

For most named operations, a regular `def` function is clearer. Lambda functions are commonly used for short operations, such as sort keys.

```python
orders = [
    {"id": 1, "amount": 300},
    {"id": 2, "amount": 100},
    {"id": 3, "amount": 200}
]

sorted_orders = sorted(orders, key=lambda order: order["amount"])
```

This sorts the orders by their `amount`.

---

## 💻 Syntax & Examples

### Example 1: Validate an Order

```python
def is_valid_order(order):
    """Check whether an order has a positive amount."""
    return order["amount"] > 0


order = {
    "order_id": 101,
    "amount": 250
}

if is_valid_order(order):
    print("Order is valid")
else:
    print("Order is invalid")
```

This example separates validation logic from the code that uses the result.

In production, validate the record's structure and field types before accessing or comparing values.

### Example 2: Transform Data

```python
def normalize_customer_name(name):
    """Remove surrounding whitespace and normalize capitalization."""
    return name.strip().title()


raw_name = "  amin ahmed  "
clean_name = normalize_customer_name(raw_name)

print(clean_name)  # Amin Ahmed
```

The function can be reused wherever customer names need the same normalization rule.

### Example 3: Calculate a Summary

```python
def calculate_summary(amounts):
    """Return the count, total, and average of a list of amounts."""
    if not amounts:
        return {
            "count": 0,
            "total": 0,
            "average": None
        }

    total = sum(amounts)

    return {
        "count": len(amounts),
        "total": total,
        "average": total / len(amounts)
    }


amounts = [100, 200, 300]
summary = calculate_summary(amounts)

print(summary)
```

Output:

```text
{'count': 3, 'total': 600, 'average': 200.0}
```

Returning a dictionary allows the caller to use each calculated metric independently.

### Example 4: Reuse a Function in a Loop

```python
def is_valid_amount(amount):
    return amount > 0


amounts = [100, -20, 0, 250]

for amount in amounts:
    if is_valid_amount(amount):
        print("Valid:", amount)
    else:
        print("Invalid:", amount)
```

The validation rule is defined once and reused for every amount.

---

## ⚠️ Common Mistakes

1. **Defining a function without calling it:** The body does not execute just because the function was defined.
2. **Confusing parameters and arguments:** Parameters appear in the definition; arguments are supplied when calling the function.
3. **Using `print()` instead of `return`:** Displaying a result does not automatically make it available to the caller.
4. **Forgetting to return a value:** A function without an explicit returned value produces `None`.
5. **Using local variables outside their scope:** Names defined locally are not normally available outside the function.
6. **Repeating logic instead of creating reusable functions:** This increases duplication and makes updates harder.
7. **Writing functions with too many responsibilities:** Complex functions are harder to understand and test.
8. **Using mutable default arguments carelessly:** Default values are evaluated once when the function is defined, not each time it is called.
9. **Assuming type hints enforce types automatically:** Python type hints primarily support documentation, static analysis, and development tools; they do not automatically validate all runtime inputs.
10. **Ignoring invalid input:** Functions used in data pipelines should define how invalid or unexpected values are handled.

### Mutable Default Argument Pitfall

Avoid this pattern:

```python
def add_record(record, records=[]):
    records.append(record)
    return records
```

The same list is reused across calls that omit `records`.

A safer pattern is:

```python
def add_record(record, records=None):
    if records is None:
        records = []

    records.append(record)
    return records
```

This creates a new list for each call that omits the argument.

---

## 👨‍💻 Data Engineering Connection

Functions are building blocks for modular and maintainable data pipelines.

### 1. Data Cleaning

A function can encapsulate a reusable cleaning rule.

```python
def clean_text(value):
    if value is None:
        return None

    return value.strip()
```

This example handles `None` explicitly before calling a string method.

In production, the function should also account for unexpected input types if they are possible.

### 2. Data Validation

```python
def validate_order(order):
    if "order_id" not in order:
        return False

    if "amount" not in order:
        return False

    if not isinstance(order["amount"], (int, float)):
        return False

    if isinstance(order["amount"], bool):
        return False

    return order["amount"] > 0
```

This function applies a simple validation policy. Real pipelines may need more detailed validation results, including error codes and explanations rather than a single Boolean.

### 3. ETL and ELT Pipelines

Functions can separate pipeline responsibilities:

- `extract_data()` — retrieves data from a source.
- `validate_data()` — checks records and schema rules.
- `transform_data()` — cleans or transforms values.
- `load_data()` — writes processed data to a destination.

These are conceptual function names, not built-in Python functions.

Separating these responsibilities improves testability and makes the pipeline easier to maintain.

### 4. Connection to Apache Airflow

Airflow workflows commonly use Python functions to define task logic.

A task might call a function that extracts records, validates the data, or writes results to a database. Airflow then manages scheduling, dependencies, retries, and task status.

The function's business logic and the orchestration framework have different responsibilities.

### 5. Connection to DataPulse

In the DataPulse project, reusable functions can implement data quality checks and transformations.

For example:

- `check_required_fields(record)`
- `detect_duplicate_orders(records)`
- `validate_order_amount(record)`
- `log_quality_issue(issue)`
- `normalize_order(record)`

Each function should have a clear contract: its expected inputs, output, side effects, and error behavior.

For duplicate handling, detection and resolution should be treated as separate responsibilities. Identifying duplicate `order_id` values does not automatically determine which record should be retained or how conflicting values should be reconciled.

### 6. Unit Testing

Functions with clear inputs and outputs are easier to test independently.

```python
def is_valid_amount(amount):
    return isinstance(amount, (int, float)) and not isinstance(amount, bool) and amount > 0


assert is_valid_amount(100) is True
assert is_valid_amount(-10) is False
assert is_valid_amount(0) is False
assert is_valid_amount(True) is False
```

These assertions demonstrate a simple validation contract. Larger projects should use a testing framework such as `pytest` to organize test cases and report failures.

---

## 🎯 Interview Questions

### Q1. What is a function in Python?

A function is a reusable block of code that performs a specific task. It can accept inputs, execute logic, and return a result.

### Q2. What is the difference between a parameter and an argument?

A parameter is a name defined in the function signature. An argument is the actual value supplied when calling the function.

### Q3. What is the difference between `return` and `print()`?

`return` sends a value back to the caller and exits the function. `print()` displays information and does not return that displayed value.

### Q4. What happens if a function has no `return` statement?

If the function finishes without returning a value, Python returns `None`.

### Q5. What are built-in functions?

They are functions provided by Python and available without importing a module, such as `len()`, `sum()`, `type()`, and `sorted()`.

### Q6. What is variable scope?

Scope determines where a name can be accessed. Variables defined inside a function are normally local to that function.

### Q7. What are default parameters?

They are parameters assigned default values in the function definition. The caller can omit those arguments and use the defaults.

### Q8. Why are mutable default arguments dangerous?

Default values are evaluated once when the function is defined. A mutable default, such as a list, can therefore retain changes across multiple calls.

### Q9. What is a lambda function?

A lambda expression creates a small anonymous function containing a single expression. It is useful for short operations, such as specifying a sorting key.

### Q10. Why are functions important in Data Engineering?

They encapsulate reusable operations for extraction, transformation, validation, loading, error handling, and testing. They help keep pipeline logic modular and maintainable.

### Q11. How would you test a data validation function?

Define expected behavior for valid, invalid, missing, and unexpected inputs, then write test cases that verify the returned results and any expected side effects.

### Q12. Should a function detect and resolve duplicates in the same step?

Not necessarily. Detection identifies duplicates, while resolution applies a defined business rule to select, merge, or reject records. Separating the responsibilities improves traceability and testing.

---

## 📝 Practice

### Exercise 1: Create a Greeting Function

Write a function named `greet` that accepts a name and returns a greeting message.

Example:

```python
print(greet("Amin"))
```

Expected output:

```text
Hello, Amin!
```

### Exercise 2: Calculate a Total

Write a function named `calculate_total` that accepts a price and a tax rate and returns the total price.

Test it with multiple values.

### Exercise 3: Return vs Print

Create two functions:

- One prints the sum of two numbers.
- One returns the sum of two numbers.

Call both functions and explain the difference between their results.

### Exercise 4: Validate an Order

Write a function that accepts an order dictionary and returns `True` if:

- The order contains an `order_id`.
- The amount is numeric but not Boolean.
- The amount is greater than zero.

Otherwise, return `False`.

### Exercise 5: Process a Batch

Write a function named `count_valid_orders` that accepts a list of orders and returns the number of orders with positive, valid numeric amounts.

Define how the function should handle missing fields and invalid values.

### Exercise 6: Fix the Mutable Default

Explain why the following function may produce unexpected results, then rewrite it safely.

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

### Exercise 7: Data Engineering Scenario

You are building a pipeline that receives thousands of order records.

Design separate functions for:

1. Checking required fields.
2. Validating data types.
3. Detecting duplicate order IDs.
4. Transforming valid records.
5. Logging data quality issues.

Explain what each function accepts, what it returns, and how invalid records should be handled.

### Exercise 8: Interview Challenge

Explain why this function is difficult to test and maintain, then suggest how to improve its design:

```python
def process_data(records):
    # Validate records
    # Remove duplicates
    # Transform values
    # Write to a database
    # Print a summary
    pass
```

Consider separating validation, deduplication, transformation, loading, and reporting into smaller functions.

---

> **Next Step:** Practice defining functions, passing arguments, returning values, and validating data. Keep the status as `🟡 In Progress` until you can explain the concepts and solve the exercises independently.