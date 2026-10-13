# Python for Data Engineering

> 📌 **Status:** 🟡 In Progress

## 📖 Overview

Python is one of the most widely used programming languages in Data Engineering because it provides a rich ecosystem of libraries for data ingestion, transformation, validation, automation, and pipeline orchestration.

Data Engineers use Python to build systems that collect data from different sources, transform it into reliable formats, load it into storage systems, and monitor the quality and execution of data pipelines.

Python does not replace SQL, databases, distributed processing frameworks, or orchestration tools. Instead, it connects these components and provides the programming logic needed to build and maintain data workflows.

This section focuses on applying Python fundamentals to practical Data Engineering tasks.

By the end of this section, you should understand how to:

- Read data from files and APIs.
- Process structured data using Python.
- Work with CSV and JSON.
- Connect Python applications to databases.
- Validate and clean incoming data.
- Handle errors and log pipeline execution.
- Organize reusable pipeline code.
- Understand when to use Python, SQL, or distributed processing tools.

---

## 🧠 Concepts

### 1. The Role of Python in Data Engineering

Python is commonly used throughout the data pipeline lifecycle.

A typical workflow looks like this:

```text
Data Sources
     |
     v
Ingestion
     |
     v
Validation
     |
     v
Transformation
     |
     v
Storage / Data Warehouse
     |
     v
Analytics and Reporting
```

Python can implement or coordinate many of these steps.

| Stage | Example Python Responsibility |
|---|---|
| Ingestion | Read files, call APIs, retrieve records |
| Validation | Check required fields, types, and constraints |
| Transformation | Clean, normalize, and enrich data |
| Loading | Write data to databases or storage systems |
| Monitoring | Log failures, record metrics, report quality issues |
| Orchestration | Implement tasks that tools such as Airflow can schedule |

Not every pipeline uses Python for every stage. For example, transformations may be executed directly in SQL, while Spark may be used for distributed processing.

### 2. Working with Structured Data

Data Engineers frequently work with records containing fields such as:

```python
order = {
    "order_id": 101,
    "customer_id": 25,
    "amount": 450.75,
    "status": "completed"
}
```

A list of dictionaries can represent multiple records:

```python
orders = [
    {"order_id": 101, "amount": 450.75},
    {"order_id": 102, "amount": 200.00},
    {"order_id": 103, "amount": 700.00}
]
```

This structure is useful for small datasets and API responses. For larger datasets, DataFrames, database operations, streaming systems, or distributed processing may be more appropriate.

### 3. File Formats: CSV and JSON

Data Engineers commonly exchange data through files.

**CSV** stores tabular data as rows and columns:

```csv
order_id,customer_id,amount
101,25,450.75
102,30,200.00
```

**JSON** represents structured data using objects and arrays:

```json
[
  {
    "order_id": 101,
    "customer_id": 25,
    "amount": 450.75
  },
  {
    "order_id": 102,
    "customer_id": 30,
    "amount": 200.00
  }
]
```

Python provides built-in modules for both formats:

- `csv` for CSV files.
- `json` for JSON serialization and deserialization.

Use CSV when working with straightforward tabular data. JSON is common in APIs and nested records.

For analytical data platforms, you may also encounter formats such as Parquet, which supports columnar storage and is commonly used in data lakes and distributed processing.

### 4. Data Ingestion

**Data ingestion** is the process of collecting data from a source and making it available to a target system.

Sources may include:

- Local files.
- REST APIs.
- Relational databases.
- Object storage.
- Message brokers.
- Application logs.

A simple ingestion process might:

1. Read a source.
2. Validate the incoming structure.
3. Record metadata about the extraction.
4. Store the raw data or pass it to the next stage.
5. Log success or failure.

A useful design principle is to distinguish the extraction process from the transformation process. This separation can make pipelines easier to debug, test, and rerun.

### 5. Data Transformation

**Data transformation** changes data into a format suitable for downstream use.

Common operations include:

- Converting data types.
- Normalizing strings.
- Handling missing values.
- Removing or identifying duplicates.
- Calculating derived columns.
- Standardizing timestamps.
- Applying business rules.

Example:

```python
raw_order = {
    "order_id": "101",
    "amount": "450.75",
    "status": " COMPLETED "
}

clean_order = {
    "order_id": int(raw_order["order_id"]),
    "amount": float(raw_order["amount"]),
    "status": raw_order["status"].strip().lower()
}

print(clean_order)
```

Output:

```text
{'order_id': 101, 'amount': 450.75, 'status': 'completed'}
```

In production systems, conversions should also handle invalid or missing values. The example above assumes the incoming values are valid.

### 6. Data Quality and Validation

A pipeline should not assume that incoming data is correct.

Common data quality dimensions include:

- **Completeness:** Are required fields present?
- **Uniqueness:** Are duplicate records present where uniqueness is required?
- **Validity:** Do values follow expected rules?
- **Consistency:** Do related fields agree with each other?
- **Freshness:** Is the data sufficiently recent?
- **Accuracy:** Does the data correctly represent the real-world information it claims to describe?

Example validation:

```python
def validate_order(order):
    required_fields = ["order_id", "amount", "status"]

    for field in required_fields:
        if field not in order or order[field] is None:
            return False

    if order["amount"] < 0:
        return False

    return True
```

This is a basic example. A production validator should also verify data types, blank strings, business rules, and how invalid records are handled.

**Important:** A record that fails validation is not necessarily safe to discard. Depending on the business requirements, the pipeline may quarantine it, log the problem, send it for review, or stop processing.

### 7. Duplicate Detection and Deduplication

Duplicate records can lead to incorrect counts, inflated revenue, and inconsistent reports.

Suppose an incoming dataset contains:

```python
orders = [
    {"order_id": 101, "amount": 450},
    {"order_id": 102, "amount": 200},
    {"order_id": 101, "amount": 450}
]
```

If `order_id` is defined as the unique business key, the first and third records appear to be duplicates.

However, duplicate handling requires an explicit rule:

- Should the first record be retained?
- Should the latest record be retained?
- Should records be merged?
- Should conflicting records be quarantined?

Two records with the same key are not always identical. For example, one might represent an older order state and another a newer update.

The correct strategy depends on the source system, business key, event semantics, and ordering guarantees.

### 8. Working with APIs

Data Engineers often extract data from REST APIs.

Python's `requests` package is commonly used to send HTTP requests.

A typical API ingestion process must account for:

- HTTP status codes.
- Request timeouts.
- Authentication.
- Pagination.
- Rate limits.
- Transient failures.
- JSON parsing.
- Schema changes.

An API response may contain only one page of records. Therefore, fetching the first response does not necessarily mean the entire dataset has been extracted.

Production pipelines should also consider retries, incremental extraction, and how to avoid loading the same records repeatedly.

### 9. Database Connectivity

Python can interact with relational databases using database drivers and libraries such as SQLAlchemy.

Common tasks include:

- Executing parameterized SQL statements.
- Reading records.
- Inserting or updating records.
- Managing transactions.
- Handling database errors.
- Closing connections and releasing resources.

Use parameterized queries instead of building SQL statements by concatenating untrusted values.

For large loads, consider batching, bulk-loading features, and database-native transformations rather than inserting every record individually.

### 10. Logging and Error Handling

Pipelines need observable execution behavior.

Useful information to log includes:

- Pipeline or task name.
- Run identifier.
- Source and target.
- Number of records extracted.
- Number of records loaded.
- Number of rejected or duplicated records.
- Execution duration.
- Error details.

Python's `logging` module provides configurable logging levels, including `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.

Logging should help engineers understand failures without exposing passwords, access tokens, or sensitive data.

### 11. Batch Processing vs Streaming

**Batch processing** processes a collection of data at scheduled or defined intervals.

Example: process all orders received during the previous hour.

**Streaming processing** processes events continuously or in small increments as they arrive.

Example: process incoming transaction events as they are published to a message broker.

Python can be used in both approaches, but the architecture differs. A simple Python loop is not automatically a reliable streaming platform. Streaming systems often require event-time handling, checkpointing, delivery guarantees, and distributed coordination.

### 12. Python vs SQL vs Distributed Processing

Choosing the right tool is part of good Data Engineering.

| Tool | Best Fit |
|---|---|
| Python | Ingestion logic, APIs, orchestration code, validation, automation |
| SQL | Set-based transformations, joins, aggregations, relational data operations |
| Pandas | In-memory tabular processing for datasets that fit available resources |
| PySpark | Distributed processing of large datasets across a cluster |
| Airflow | Scheduling, dependency management, retries, and orchestration of workflows |

These tools are complementary.

For example, Python can extract data from an API, load it into a database, and trigger a workflow. SQL can then perform transformations inside the database.

Do not assume that moving all transformations into Python is better than using SQL. Consider data volume, memory, maintainability, performance, and where the data already resides.

---

## 💻 Syntax & Examples

### Example 1: Read a CSV File

```python
import csv

with open("orders.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

`csv.DictReader` represents each row as a dictionary using the CSV header names as keys.

By default, CSV values are strings. Convert them to the required types and validate them before applying calculations.

### Example 2: Read and Write JSON

```python
import json

with open("orders.json", mode="r", encoding="utf-8") as file:
    orders = json.load(file)

print(orders)

with open("processed_orders.json", mode="w", encoding="utf-8") as file:
    json.dump(orders, file, indent=2)
```

- `json.load()` reads JSON from a file.
- `json.loads()` parses a JSON string.
- `json.dump()` writes JSON to a file.
- `json.dumps()` converts a Python object into a JSON string.

The object must contain values that the JSON encoder can serialize, or a suitable custom serialization strategy must be provided.

### Example 3: Transform Records

```python
def transform_order(raw_order):
    return {
        "order_id": int(raw_order["order_id"]),
        "customer_id": int(raw_order["customer_id"]),
        "amount": float(raw_order["amount"]),
        "status": raw_order["status"].strip().lower()
    }


raw_order = {
    "order_id": "101",
    "customer_id": "25",
    "amount": "450.75",
    "status": " COMPLETED "
}

print(transform_order(raw_order))
```

The transformation function is reusable and easy to test.

It assumes all required fields exist and contain valid values. Production code should explicitly handle invalid inputs.

### Example 4: Detect Duplicate Business Keys

```python
orders = [
    {"order_id": 101, "amount": 450},
    {"order_id": 102, "amount": 200},
    {"order_id": 101, "amount": 450}
]

seen_order_ids = set()
unique_orders = []
duplicate_orders = []

for order in orders:
    order_id = order["order_id"]

    if order_id in seen_order_ids:
        duplicate_orders.append(order)
    else:
        seen_order_ids.add(order_id)
        unique_orders.append(order)

print("Unique records:", unique_orders)
print("Duplicate records:", duplicate_orders)
```

This example keeps the first record for each `order_id` and classifies later occurrences as duplicates.

It does not compare every field or resolve conflicting updates. Choose a deduplication rule that matches the business requirements.

### Example 5: Validate Records

```python
def validate_order(order):
    if order.get("order_id") is None:
        return False

    if order.get("amount") is None:
        return False

    if not isinstance(order["amount"], (int, float)):
        return False

    if order["amount"] < 0:
        return False

    return True


order = {
    "order_id": 101,
    "amount": 450.75,
    "status": "completed"
}

print(validate_order(order))
```

This validator checks a few basic conditions. Real pipelines usually need additional checks for missing fields, numeric edge cases, business rules, and duplicate keys.

### Example 6: Use Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def process_orders(orders):
    logging.info("Starting order processing")

    processed_count = 0

    for order in orders:
        if validate_order(order):
            processed_count += 1
        else:
            logging.warning(
                "Invalid order encountered"
            )

    logging.info(
        "Finished processing %s valid orders",
        processed_count
    )

    return processed_count
```

This example assumes `validate_order()` is defined earlier.

In production, use structured logs where appropriate, include a pipeline run identifier, and avoid logging sensitive record contents.

### Example 7: Handle Exceptions

```python
import logging

logging.basicConfig(level=logging.INFO)

def convert_amount(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        logging.warning("Invalid amount encountered")
        return None


print(convert_amount("450.75"))
print(convert_amount("invalid"))
```

Returning `None` is one possible invalid-value strategy. A production pipeline should define whether such records are rejected, quarantined, retried, or handled through another explicit policy.

### Example 8: Call a REST API

Install the package first:

```bash
python -m pip install requests
```

Example:

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    records = response.json()

    print("Records received:", len(records))

except requests.RequestException as error:
    print("API request failed:", error)
```

This example demonstrates a basic HTTP request. Production ingestion should also handle pagination, authentication, rate limits, retries, schema validation, and incremental extraction when required.

### Example 9: Load Data into a Database

A database driver or library is required. For example, SQLAlchemy can be installed with:

```bash
python -m pip install sqlalchemy
```

A simplified example using a SQLAlchemy engine:

```python
from sqlalchemy import create_engine, text

engine = create_engine(
    "sqlite:///pipeline.db"
)

with engine.begin() as connection:
    connection.execute(
        text("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY,
                amount REAL
            )
        """)
    )

    connection.execute(
        text("""
            INSERT INTO orders (order_id, amount)
            VALUES (:order_id, :amount)
        """),
        {"order_id": 101, "amount": 450.75}
    )
```

This example uses SQLite so it can run locally without a separate database server.

The `engine.begin()` context manages a transaction and commits on successful completion; an exception causes the transaction to be rolled back. Database-specific behavior may vary.

For MySQL or PostgreSQL, use the appropriate SQLAlchemy connection URL and install a compatible driver.

---

## ⚠️ Common Mistakes

1. **Using Python for every transformation:** SQL or database-native operations may be more efficient for relational workloads.
2. **Assuming CSV values have the correct data types:** CSV readers commonly return values as strings.
3. **Ignoring schema changes:** API responses and source files may add, remove, or change fields.
4. **Removing duplicates without defining the business key:** Duplicate detection must follow explicit business rules.
5. **Assuming repeated IDs always mean identical records:** They may represent updates, retries, or conflicting source events.
6. **Ignoring API pagination:** A single request may return only part of the available data.
7. **Using no request timeout:** Network calls can wait longer than expected.
8. **Retrying every failure indiscriminately:** Some errors are permanent and will not improve with retries.
9. **Building SQL through string concatenation:** Use parameterized queries to reduce SQL injection risk.
10. **Logging sensitive data:** Do not expose credentials, tokens, or confidential records.
11. **Processing huge files entirely in memory:** Consider chunked reads, database processing, or distributed frameworks.
12. **Ignoring transaction behavior:** Partial database writes can leave inconsistent results if failure handling is poorly designed.
13. **Treating `None` as a complete error-handling strategy:** Invalid records need an explicit downstream policy.
14. **Not testing transformations:** Small, deterministic functions are easier to test and debug than a single large pipeline function.

---

## 👨‍💻 Data Engineering Connection

### 1. Python in an ETL Pipeline

ETL stands for **Extract, Transform, Load**.

- **Extract:** Read data from an API, file, database, or another source.
- **Transform:** Validate, clean, normalize, deduplicate, and enrich the data.
- **Load:** Write the processed records to a destination.

Example architecture:

```text
REST API
   |
   v
Python Ingestion
   |
   v
Raw Storage
   |
   v
Validation and Transformation
   |
   v
MySQL / Data Warehouse
   |
   v
Analytics
```

The architecture depends on the project's requirements. Some systems use ELT instead, loading raw data first and transforming it inside the destination platform.

### 2. Python and SQL Work Together

Python is useful for connecting systems, handling files and APIs, and coordinating execution.

SQL is often better suited to relational joins, aggregations, and large set-based transformations that can be executed inside a database.

A practical Data Engineer chooses where each operation should run rather than forcing everything into one language.

### 3. Python and Airflow

Apache Airflow orchestrates workflows by scheduling tasks and managing their dependencies, retries, and execution history.

Python is used to define Airflow DAGs and task logic. The actual processing may happen in a database, Spark cluster, API service, or another system.

A task should ideally have a clear responsibility, well-defined inputs and outputs, and appropriate failure handling.

### 4. Python and Spark

Pandas is useful when data fits comfortably in the available memory of one machine.

PySpark is designed for distributed data processing and can work with datasets that exceed the practical limits of a single-machine Pandas workflow.

The right choice depends on data volume, processing requirements, available infrastructure, and operational complexity—not only the number of rows.

### 5. Python and Data Quality

For DataPulse, Python can implement data quality checks such as:

- Required-field validation.
- Duplicate-key detection.
- Type and format validation.
- Freshness checks.
- Record-count comparisons.
- Logging failed validations.

A useful pipeline records not only that a record failed, but also the reason, the source, the processing run, and the chosen resolution.

For example, an invalid record may be quarantined and logged instead of silently discarded. The appropriate behavior depends on the severity of the issue and the system's business requirements.

### 6. Idempotency and Reliable Pipelines

An operation is **idempotent** when repeating it produces the same intended final state as performing it once.

This matters because pipelines may be retried after network errors, process crashes, or partial failures.

For example, blindly inserting the same batch twice can duplicate records. A safer design might use stable business keys, database constraints, upserts, checkpoints, or batch identifiers.

The exact strategy depends on whether the source represents snapshots, updates, or individual events.

### 7. Testing Data Pipelines

A reliable pipeline should have tests for:

- Valid input records.
- Missing or malformed fields.
- Duplicate business keys.
- Empty datasets.
- Database failures.
- API errors.
- Repeated execution.
- Unexpected source schema changes.

Testing transformation functions independently helps isolate business logic from network and database failures.

---

## 🎯 Interview Questions

### Q1. Why is Python widely used in Data Engineering?

Python has a broad ecosystem of libraries and makes it practical to connect APIs, files, databases, processing frameworks, and orchestration tools.

### Q2. What is the difference between ETL and ELT?

ETL transforms data before loading it into the target system. ELT loads data first and performs transformations inside the target platform or processing environment.

### Q3. When would you use Python instead of SQL?

Python is useful for API integration, file processing, custom validation, automation, and orchestration. SQL is often preferable for relational joins, aggregations, and set-based transformations executed inside a database.

### Q4. How would you handle duplicate records in a pipeline?

First, define the business key and determine whether repeated records represent identical duplicates, retries, or legitimate updates. Then apply an explicit deduplication or merge policy and record relevant quality issues.

### Q5. How would you handle invalid data?

Validate records against defined rules, capture the failure reason, and apply a documented policy such as quarantine, rejection, correction, or controlled retry. Do not silently discard important records without a business-approved reason.

### Q6. How would you process a large CSV file?

Avoid loading the entire file into memory if it is too large. Depending on the workload, use chunked processing, streaming reads, database bulk-loading tools, or distributed processing frameworks.

### Q7. How do you handle API failures?

Use timeouts, inspect HTTP status codes, distinguish transient from permanent failures, apply bounded retries where appropriate, and log failures. Also handle authentication, rate limits, pagination, and partial extraction.

### Q8. What does idempotency mean in Data Engineering?

It means that repeating an operation produces the same intended final state rather than creating unintended duplicate or inconsistent results.

### Q9. Why is logging important in data pipelines?

Logs help engineers identify which tasks ran, what happened, how many records were processed, and why failures occurred. Logs should provide diagnostic information without exposing secrets.

### Q10. When would you choose Pandas over PySpark?

Pandas is often suitable for in-memory processing on a single machine. PySpark is appropriate when distributed execution is beneficial for data size or processing requirements. The decision should consider memory, performance, infrastructure, and complexity.

### Q11. What is the difference between data validation and data transformation?

Validation checks whether data satisfies defined rules. Transformation changes its representation or content. A pipeline often performs both, and some transformations may require validation before or after execution.

### Q12. How would you design a reliable ingestion pipeline?

Define the source and target, capture extraction metadata, validate the input, handle pagination and transient failures, make retries safe, track processed records, use appropriate transaction or checkpoint mechanisms, and test the pipeline's behavior under failure.

---

## 📝 Practice

### Exercise 1: Build a CSV Ingestion Script

Create an `orders.csv` file containing at least five records.

Write a Python script that:

1. Reads the CSV file.
2. Converts `order_id` to an integer.
3. Converts `amount` to a numeric type.
4. Validates required fields.
5. Separates valid and invalid records.
6. Writes valid records to a new file.
7. Logs how many records were processed.

### Exercise 2: Build a JSON Transformation

Create a JSON file containing nested customer and order information.

Write a script that:

1. Reads the JSON file.
2. Extracts the required fields.
3. Normalizes text values.
4. Converts data types.
5. Handles missing values.
6. Writes the transformed records to a new JSON file.

### Exercise 3: Implement Deduplication

Create a dataset with:

- Exact duplicate records.
- Repeated business keys with conflicting values.
- Unique records.

Implement a deduplication function and document the rule used for each case.

Do not automatically merge conflicting records without defining how the conflict should be resolved.

### Exercise 4: Build a Basic API Ingestion Script

Use a public test API to:

1. Send an HTTP request.
2. Set a timeout.
3. Check the response status.
4. Parse the JSON.
5. Validate the response structure.
6. Save the retrieved records.
7. Handle request errors.

For an advanced version, implement pagination and bounded retries.

### Exercise 5: Load Records into SQLite

Using SQLAlchemy:

1. Create a local SQLite database.
2. Define an `orders` table.
3. Insert validated records using parameterized SQL.
4. Read the inserted records.
5. Handle transaction failures.
6. Run the script more than once and observe whether duplicates occur.

Then modify the design to make repeated execution safe.

### Exercise 6: DataPulse Mini Pipeline

Build a small end-to-end pipeline:

```text
CSV Input
   |
   v
Extract
   |
   v
Validate
   |
   +------> Invalid Records / Quality Log
   |
   v
Transform
   |
   v
Deduplicate
   |
   v
Load into SQLite or MySQL
   |
   v
Execution Summary
```

Your pipeline should:

- Use reusable functions.
- Log processing statistics.
- Record validation failures.
- Apply a documented deduplication rule.
- Avoid exposing secrets.
- Handle exceptions.
- Include tests for normal and failure scenarios.

### Exercise 7: Interview Challenge

Explain how you would design a pipeline that receives orders every hour, detects duplicate records, handles invalid data, and loads the results into a database.

Your answer should address:

1. Data ingestion.
2. Data validation.
3. Deduplication rules.
4. Idempotent processing.
5. Database transactions.
6. Logging and monitoring.
7. Retry behavior.
8. Testing and data quality reporting.

---

> **Next Step:** Build the CSV ingestion script first. Then add validation, deduplication, and database loading as separate functions. Keep the status as `🟡 In Progress` until you can explain and implement the full workflow independently.