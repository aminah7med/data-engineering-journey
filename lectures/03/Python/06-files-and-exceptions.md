# Files & Exceptions

> 📌 **Status:** 🟡 In Progress

## 📖 Overview

**File Handling** allows Python programs to read data from files and write data to them.

**Exception Handling** allows programs to respond to runtime errors in a controlled way instead of terminating unexpectedly.

These concepts are essential in **Data Engineering**, where pipelines regularly read CSV and JSON files, process large datasets, write output files, and handle missing files, malformed records, permission problems, and other failures.

This section covers file operations, file modes, context managers, CSV and JSON processing, exceptions, and practical error-handling patterns.

---

## 🧠 Concepts

### 1. Opening a File

Python provides the built-in `open()` function to open a file.

```python
file = open("data.txt", "r")
```

The first argument is the file path, and the second argument specifies the mode.

Common file modes:

| Mode | Meaning |
|---|---|
| `"r"` | Read an existing file |
| `"w"` | Write to a file, replacing existing content |
| `"a"` | Append to the end of a file |
| `"x"` | Create a new file and fail if it already exists |
| `"b"` | Binary mode modifier |
| `"t"` | Text mode modifier; the default |
| `"r+"` | Read and write without initially truncating the file |

Modes can be combined, such as `"rb"` for reading binary data or `"w+"` for reading and writing while truncating the file initially.

**Important:** Opening a file in `"w"` mode can erase its existing contents.

### 2. Reading a File

Python provides several methods for reading file contents.

#### `read()`

Reads the entire remaining content as a string in text mode.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

For a very large file, reading everything into memory may be inefficient.

#### `readline()`

Reads one line at a time.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    line = file.readline()
    print(line)
```

#### Iterating Over a File

For text files, iteration is often a memory-efficient way to process lines.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip("\n"))
```

This processes one line at a time rather than loading the entire file into memory.

### 3. Writing to a File

Use `"w"` mode to write new content. Existing content is truncated when the file is opened successfully.

```python
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Data Engineering\n")
    file.write("Python File Handling\n")
```

The `write()` method returns the number of characters written in text mode.

### 4. Appending to a File

Use `"a"` mode to append content without initially replacing the existing contents.

```python
with open("logs.txt", "a", encoding="utf-8") as file:
    file.write("Pipeline execution completed\n")
```

Appending is useful for simple logs, but it does not automatically provide structured logging, concurrency safety, or reliable distributed log management.

### 5. The `with` Statement

The `with` statement uses a context manager to manage resources.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

When execution leaves the `with` block, the file is closed automatically, including when an exception occurs inside the block.

**Best practice:** Prefer `with open(...)` over manually opening and closing files.

### 6. File Paths

A file path identifies where a file is located.

```python
from pathlib import Path

file_path = Path("data") / "orders.csv"

print(file_path)
print(file_path.exists())
```

`pathlib.Path` provides a convenient, cross-platform way to work with file paths.

Relative paths are resolved relative to the process's current working directory, which may differ from the directory containing the Python script.

For this reason, production pipelines should make file locations explicit and avoid relying on an assumed working directory.

### 7. Working with CSV Files

CSV stands for **Comma-Separated Values**. It is a common format for tabular data.

Python's built-in `csv` module supports reading and writing CSV files.

#### Reading CSV Records

```python
import csv

with open("orders.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

`csv.DictReader` uses the header row as dictionary keys. Values are generally returned as strings unless additional conversion is performed.

For example, a CSV record might contain:

```csv
order_id,amount,status
101,250.50,paid
102,100.00,pending
```

The amount `"250.50"` initially arrives as text and may need validation and conversion.

#### Writing CSV Records

```python
import csv

orders = [
    {"order_id": 101, "amount": 250.50},
    {"order_id": 102, "amount": 100.00}
]

with open("output.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["order_id", "amount"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(orders)
```

The `newline=""` argument is recommended when opening CSV files for reading or writing with Python's `csv` module.

### 8. Working with JSON Files

JSON stands for **JavaScript Object Notation**. It is commonly used for API responses and structured data exchange.

Python's built-in `json` module supports JSON serialization and deserialization.

#### Reading JSON

```python
import json

with open("config.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)
```

`json.load()` reads JSON data from a file and converts it into corresponding Python objects.

Common mappings include:

| JSON Value | Python Type |
|---|---|
| Object | `dict` |
| Array | `list` |
| String | `str` |
| Number | `int` or `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

#### Writing JSON

```python
import json

order = {
    "order_id": 101,
    "amount": 250.50,
    "status": "paid"
}

with open("order.json", "w", encoding="utf-8") as file:
    json.dump(order, file, indent=4)
```

`json.dump()` writes a Python object to a file in JSON format.

**Important distinction:**

- `json.load()` reads JSON from a file-like object.
- `json.loads()` parses a JSON string.
- `json.dump()` writes JSON to a file-like object.
- `json.dumps()` converts a Python object into a JSON string.

### 9. What Is an Exception?

An **exception** is an event that interrupts the normal flow of execution when an error or other exceptional condition occurs.

Common exceptions include:

| Exception | Typical Cause |
|---|---|
| `FileNotFoundError` | A file does not exist at the specified path |
| `PermissionError` | The process lacks the required permissions |
| `IsADirectoryError` | A file operation is attempted on a directory where a file is expected |
| `ValueError` | A value is invalid for an operation |
| `TypeError` | An operation receives an incompatible type |
| `KeyError` | A dictionary key does not exist |
| `IndexError` | A sequence index is out of range |
| `ZeroDivisionError` | Division by zero |
| `JSONDecodeError` | JSON text is malformed |

Exceptions can be handled so the program can report errors, recover when appropriate, or fail in a controlled way.

### 10. `try` and `except`

Use `try` to place code that may raise an exception and `except` to handle specified exception types.

```python
try:
    number = int("abc")
except ValueError:
    print("The value must be a valid integer")
```

Only the matching exception is handled by this `except` block. Other exception types propagate unless another handler matches them.

### 11. Handling Multiple Exceptions

Different exception types may require different responses.

```python
try:
    with open("config.json", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("Configuration file was not found")
except PermissionError:
    print("Permission denied while reading the file")
```

Handle exceptions that you can meaningfully respond to. Avoid catching every exception without understanding what should happen next.

### 12. The `else` and `finally` Blocks

Python supports `else` and `finally` with exception handling.

- `else` runs when the `try` block completes without an exception handled by the associated `except` clauses.
- `finally` runs when control leaves the construct, whether an exception occurred or not, subject to process termination or other exceptional circumstances.

```python
try:
    number = int("100")
except ValueError:
    print("Invalid number")
else:
    print("Converted successfully:", number)
finally:
    print("Conversion attempt finished")
```

The `with` statement should generally be used for file cleanup because it already handles closing the file correctly.

### 13. Raising Exceptions

Use `raise` to signal that a condition is invalid.

```python
def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    return amount
```

This function rejects non-positive amounts instead of silently accepting them.

In production, validate input types as well if the function's contract requires numeric values.

### 14. Creating Custom Exceptions

Custom exceptions allow an application to represent domain-specific failures.

```python
class DataQualityError(Exception):
    """Raised when a data quality rule fails."""
    pass
```

Example:

```python
def validate_order(order):
    if "order_id" not in order:
        raise DataQualityError("Missing order_id")
```

Custom exceptions can make error handling clearer when a pipeline needs to distinguish data quality failures from infrastructure or programming errors.

---

## 💻 Syntax & Examples

### Example 1: Read a Text File Safely

```python
from pathlib import Path

file_path = Path("data.txt")

try:
    with file_path.open("r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip("\n"))
except FileNotFoundError:
    print(f"File not found: {file_path}")
except PermissionError:
    print(f"Permission denied: {file_path}")
```

This example handles two expected file-access problems. Other unexpected errors are not silently swallowed.

### Example 2: Read and Validate CSV Data

```python
import csv

def load_orders(file_path):
    orders = []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                order_id = int(row["order_id"])
                amount = float(row["amount"])
            except (ValueError, KeyError) as error:
                print(f"Invalid row: {row}. Reason: {error}")
                continue

            orders.append({
                "order_id": order_id,
                "amount": amount,
                "status": row.get("status")
            })

    return orders
```

This function converts selected fields and skips records with missing or invalid values.

In a production pipeline, consider returning structured validation issues rather than relying on `print()`. Also validate required headers before processing the rows.

### Example 3: Parse JSON Safely

```python
import json

def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("JSON file not found")
    except json.JSONDecodeError:
        print("The file contains invalid JSON")

    return None
```

This example returns `None` when a handled error occurs. In a production application, returning `None` can be ambiguous if `None` is also a legitimate result, so a structured result or a propagated exception may be more appropriate.

### Example 4: Process a File with a Controlled Failure

```python
def process_amount(value):
    try:
        amount = float(value)
    except (ValueError, TypeError) as error:
        raise ValueError(f"Invalid amount: {value!r}") from error

    if amount <= 0:
        raise ValueError("Amount must be positive")

    return amount
```

This example raises a clear exception and preserves the original conversion error as its cause when conversion fails.

---

## ⚠️ Common Mistakes

1. **Forgetting to close files:** Use a context manager with `with open(...)`.
2. **Using `"w"` when you intended to append:** `"w"` truncates the existing file.
3. **Reading a huge file with `read()` unnecessarily:** Iterate over lines or process batches when appropriate.
4. **Assuming CSV values are automatically numeric:** CSV readers usually return field values as strings.
5. **Confusing `json.load()` with `json.loads()`:** One reads from a file-like object; the other parses a string.
6. **Catching every exception with `except Exception` without a plan:** This can hide programming bugs and unexpected failures.
7. **Using a bare `except` unnecessarily:** It may catch exceptions that should normally propagate, including interruption-related exceptions.
8. **Ignoring invalid records silently:** Record the issue or apply a clearly defined rejection policy.
9. **Assuming `finally` prevents every possible failure:** Abrupt process termination or machine failure can prevent cleanup code from completing.
10. **Logging sensitive data:** Avoid writing passwords, API keys, personal information, or other secrets into logs.
11. **Assuming a relative path always points to the script's directory:** It normally depends on the current working directory.
12. **Using `print()` as the only production logging mechanism:** Use the `logging` module or an appropriate centralized logging system for operational pipelines.

---

## 👨‍💻 Data Engineering Connection

File handling and exception handling are essential for reliable ingestion pipelines.

### 1. Data Ingestion

A pipeline may read CSV exports, JSON API responses, configuration files, or text logs.

The ingestion stage should verify that the input exists, is readable, and has the expected format before downstream processing begins.

### 2. Data Validation and Quarantine

Invalid records should not necessarily cause the entire pipeline to fail.

A pipeline may:

- Accept valid records.
- Record invalid rows and their reasons.
- Quarantine malformed records.
- Stop processing when a critical structural or infrastructure failure occurs.

The right strategy depends on the business requirements and the severity of the failure.

### 3. Error Handling Strategy

Different failures need different responses.

| Failure | Possible Response |
|---|---|
| Optional input file missing | Skip it or report the absence |
| Required input file missing | Fail the task and report the error |
| Invalid individual record | Quarantine or reject the record |
| Database connection failure | Retry according to a defined policy |
| Invalid configuration | Stop early and report a configuration error |
| Malformed JSON payload | Reject or quarantine the payload |

Retries are useful for transient failures, but repeatedly retrying malformed data or invalid configuration does not normally solve the problem.

### 4. Logging

The built-in `logging` module supports structured operational logging levels such as `DEBUG`, `INFO`, `WARNING`, and `ERROR`.

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Pipeline started")
logging.warning("Invalid record detected")
logging.error("Pipeline failed")
```

In a production environment, configure handlers, formatting, log destinations, and sensitive-data controls appropriately.

### 5. Connection to Apache Airflow

Airflow tasks execute Python code and can fail when file access, parsing, validation, or database operations fail.

A task should generally raise an appropriate exception when it cannot complete its responsibility. Airflow can then mark the task as failed and apply configured retry behavior.

Do not catch an error, log it, and return success if the task actually failed.

### 6. Connection to DataPulse

In DataPulse, file and exception handling can support ingestion and data quality monitoring.

For example:

1. Read the incoming file.
2. Validate its format and required columns.
3. Parse each record.
4. Separate valid records from invalid records.
5. Record the issue type, source, timestamp, and status.
6. Load accepted records according to the pipeline's rules.
7. Fail the task when a critical error prevents safe processing.

A useful quality issue might contain:

```python
quality_issue = {
    "issue_type": "INVALID_DATA_TYPE",
    "source": "orders.csv",
    "field": "amount",
    "status": "open"
}
```

This dictionary is an illustrative in-memory structure. DataPulse should persist issues in its database if they need to remain available after the process exits.

---

## 🎯 Interview Questions

### Q1. How do you open a file safely in Python?

Use the `with` statement with `open()`. The context manager closes the file automatically when the block exits.

### Q2. What is the difference between `"w"` and `"a"`?

`"w"` opens a file for writing and truncates existing content. `"a"` opens it for appending.

### Q3. Why is reading a large file with `read()` potentially inefficient?

It loads the remaining file content into memory. Iteration or batch processing can reduce peak memory usage.

### Q4. What is the difference between `json.load()` and `json.loads()`?

`json.load()` reads JSON from a file-like object, while `json.loads()` parses JSON from a string.

### Q5. What is an exception?

An exception is an event that interrupts normal execution and can be handled or propagated by the program.

### Q6. What is the purpose of `try` and `except`?

They allow code that may fail to be executed within a protected block and let the program handle specified exception types.

### Q7. What is the difference between `else` and `finally` in exception handling?

`else` runs when the `try` block completes without an exception handled by the associated handlers. `finally` runs when control leaves the construct, regardless of whether an exception occurred in ordinary execution.

### Q8. Why should you avoid catching every exception indiscriminately?

It can hide programming errors and unexpected failures, making the pipeline appear successful when it has not completed correctly.

### Q9. How would you handle malformed records in a data pipeline?

Validate records, capture the failure reason, and apply an explicit policy to reject, quarantine, or correct the record when safe. Preserve enough context for debugging without logging sensitive information.

### Q10. When should a pipeline fail instead of skipping a record?

A pipeline should fail when an error prevents safe or correct execution, such as missing critical configuration, inaccessible required sources, or a broken schema contract. Record-level errors may be quarantined when the pipeline's requirements permit it.

### Q11. How does exception handling work with Airflow retries?

An unhandled task exception generally marks the task as failed, allowing Airflow's configured retry policy to apply. If the code catches the error and returns normally, Airflow may treat the task as successful.

### Q12. What is the purpose of a custom exception?

It represents an application-specific failure so that calling code can distinguish it from other types of errors and handle it appropriately.

---

## 📝 Practice

### Exercise 1: Read a Text File

Write a program that reads a text file line by line and prints each line without its trailing newline character.

Handle the case where the file does not exist.

### Exercise 2: Write and Append

1. Create a file called `output.txt`.
2. Write two lines to it.
3. Open it in append mode.
4. Add a third line.
5. Read the file and verify its contents.

Explain why using `"w"` for the second operation would be incorrect.

### Exercise 3: Read a CSV File

Given an `orders.csv` file with the columns `order_id`, `amount`, and `status`:

1. Read the records using `csv.DictReader`.
2. Convert `order_id` to an integer.
3. Convert `amount` to a numeric type.
4. Handle invalid records without silently discarding the reason.
5. Return the valid records.

### Exercise 4: Parse JSON

Write a function that reads a JSON file and handles:

- A missing file.
- Invalid JSON syntax.
- Successful parsing.

Explain whether your function should return `None`, return a structured error result, or raise an exception in each situation.

### Exercise 5: Exception Handling

Predict what happens in the following code:

```python
try:
    result = int("abc")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion succeeded")
finally:
    print("Operation finished")
```

Explain why each block does or does not execute.

### Exercise 6: Custom Exception

Create a custom exception called `DataQualityError`.

Write a function that raises this exception when an order is missing its required `order_id`.

### Exercise 7: DataPulse Scenario

A pipeline receives an hourly CSV file containing order records. Sometimes the file is missing, some rows contain invalid amounts, and some rows contain duplicate order IDs.

Design an error-handling strategy that distinguishes between:

1. Missing required input.
2. Invalid individual records.
3. Duplicate records.
4. Temporary infrastructure failures.
5. Unexpected programming errors.

Explain which errors should be logged, quarantined, retried, or cause the task to fail.

### Exercise 8: Interview Challenge

Explain why the following code can be dangerous in a production pipeline:

```python
try:
    process_data()
except Exception:
    print("Something went wrong")
```

Discuss how you would improve its exception handling, logging, and failure behavior.

---

> **Next Step:** Practice file operations, CSV and JSON processing, and exception handling. Keep the status as `🟡 In Progress` until you can solve the exercises and explain how your error-handling choices protect a data pipeline.