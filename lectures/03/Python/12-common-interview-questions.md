# Interview Questions

> 📌 **Status:** 🟡 In Progress

## 📖 Overview

This document is a practical revision guide for Python interview preparation, with a focus on Data Engineering roles.

It covers Python fundamentals, data structures, functions, object-oriented programming, file handling, exceptions, modules, virtual environments, dependency management, and practical data pipeline scenarios.

The goal is not simply to memorize definitions. You should be able to:

- Explain Python concepts clearly.
- Write and debug small code examples.
- Compare alternative approaches.
- Analyze time and space complexity.
- Apply Python to data ingestion, transformation, validation, and loading.
- Explain how you would handle failures in a real data pipeline.

**Interview preparation strategy:**

1. Understand the concept.
2. Explain it in your own words.
3. Write a small example without assistance.
4. Discuss edge cases and trade-offs.
5. Connect the concept to a Data Engineering use case.

---

## 🧠 Concepts

### 1. Python Fundamentals

**Q1. What is Python?**

Python is a high-level, general-purpose programming language known for its readable syntax and extensive ecosystem of libraries.

It is widely used in automation, data processing, API integration, machine learning, and Data Engineering.

**Q2. Is Python compiled or interpreted?**

Python's execution model depends on the implementation. In CPython, source code is compiled into bytecode, which is then executed by the Python virtual machine.

Therefore, describing Python as simply "interpreted line by line" is an oversimplification.

**Q3. What is dynamic typing?**

Python is dynamically typed because variable names do not need explicit type declarations, and they can be rebound to objects of different types.

```python
value = 10
value = "hello"
```

The name `value` first refers to an integer object and then refers to a string object.

**Q4. What is the difference between mutable and immutable objects?**

Mutable objects can be changed after creation. Immutable objects cannot be changed after creation.

| Mutable | Immutable |
|---|---|
| `list` | `int` |
| `dict` | `float` |
| `set` | `bool` |
| | `str` |
| | `tuple` (the tuple structure itself) |

A tuple may contain a mutable object, such as a list. That nested object can still be modified.

**Q5. What is the difference between `==` and `is`?**

- `==` checks value equality.
- `is` checks object identity.

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True
print(a is b)  # False
```

Use `is None` when checking whether a value is `None`.

### 2. Data Structures

**Q6. What is the difference between a list and a tuple?**

A list is mutable, while a tuple's structure is immutable. Lists are suitable for collections that change; tuples are useful for fixed collections of values.

**Q7. What is the difference between a set and a list?**

A list preserves element order and allows duplicates. A set stores unique hashable elements and does not guarantee a meaningful iteration order.

Sets are useful for membership checks and removing duplicates when ordering is not required.

**Q8. How does a dictionary work?**

A dictionary stores key-value pairs and uses hashing to provide efficient average-case lookup, insertion, and deletion.

Dictionary keys must be hashable. In modern Python, dictionaries preserve insertion order.

**Q9. How would you remove duplicates from a list?**

If preserving the first occurrence of each hashable value is important:

```python
values = [1, 2, 1, 3, 2]

unique_values = list(dict.fromkeys(values))

print(unique_values)  # [1, 2, 3]
```

For records, first define which field or combination of fields determines duplication.

**Q10. What is the difference between shallow copy and deep copy?**

A shallow copy creates a new outer object but retains references to nested objects. A deep copy recursively copies nested objects, subject to the behavior of those objects.

```python
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0].append(99)

print(shallow)  # [[1, 2, 99], [3, 4]]
print(deep)    # [[1, 2], [3, 4]]
```

### 3. Functions

**Q11. What is the difference between `print()` and `return`?**

`print()` displays information. `return` sends a value back to the caller and ends the current function execution.

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)
```

**Q12. What are `*args` and `**kwargs`?**

- `*args` collects extra positional arguments into a tuple.
- `**kwargs` collects extra keyword arguments into a dictionary.

```python
def show_values(*args, **kwargs):
    print(args)
    print(kwargs)

show_values(10, 20, name="Amin")
```

**Q13. What is a lambda function?**

A lambda is a small anonymous function containing a single expression.

```python
square = lambda x: x * x

print(square(5))  # 25
```

Use a regular function when logic needs multiple statements, documentation, or clearer naming.

**Q14. What is a mutable default argument problem?**

Default arguments are evaluated when the function is defined, not every time it is called.

Problematic example:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

The same list can be reused across calls.

Safer version:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

### 4. Object-Oriented Programming

**Q15. What is the difference between a class and an object?**

A class defines a type and its behavior. An object is an instance of that class.

**Q16. What is `self`?**

`self` refers to the current instance in an instance method. It is a conventional parameter name, not a reserved keyword.

**Q17. What is the difference between `__init__` and `__new__`?**

`__new__` creates and returns an instance. `__init__` initializes an instance after it has been created.

**Q18. What are the four common OOP principles?**

- **Encapsulation:** Organizing data and behavior together and controlling access through an interface.
- **Abstraction:** Exposing essential behavior while hiding implementation details.
- **Inheritance:** Defining a class based on another class.
- **Polymorphism:** Allowing different object types to provide compatible behavior through a common interface.

**Q19. What is the difference between inheritance and composition?**

Inheritance models an "is-a" relationship. Composition models a "has-a" relationship, where one object uses or contains another object.

Composition is often preferable when a class needs functionality from another component without becoming a subtype of it.

### 5. Files, Exceptions, and Modules

**Q20. Why use a context manager when opening files?**

A context manager ensures that a resource is properly released when the block exits, including when an exception occurs.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

**Q21. What is the purpose of exception handling?**

Exception handling allows an application to respond to errors in a controlled way.

Use specific exceptions where possible. Avoid silently catching every exception without logging, recovery, or re-raising.

**Q22. What is the difference between a module and a package?**

A module is generally a Python file that provides reusable code. A package organizes modules under a package namespace, commonly using a directory structure.

**Q23. What does `if __name__ == "__main__":` do?**

It runs a block when the file is executed as the main program, rather than when it is imported as a module.

### 6. Virtual Environments and Dependencies

**Q24. What is a virtual environment?**

A virtual environment isolates a project's Python package installations and interpreter environment from other projects.

**Q25. What is pip?**

pip is a Python package installer used to install, upgrade, remove, and inspect packages.

**Q26. What is the purpose of `requirements.txt`?**

It records Python package requirements that can be installed with:

```bash
python -m pip install -r requirements.txt
```

**Q27. What is the difference between direct and transitive dependencies?**

A direct dependency is explicitly required by the project. A transitive dependency is required by another dependency.

**Q28. Why should you avoid committing `.venv/` to Git?**

It contains environment-specific files and can usually be recreated from the dependency specification and setup instructions.

---

## 💻 Syntax & Examples

### 1. Find the Output

**Question: What will this code print?**

```python
x = [1, 2, 3]
y = x

y.append(4)

print(x)
print(y)
```

**Answer:**

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

Both names refer to the same list object. The append operation modifies that shared object.

### 2. Predict the Loop Output

```python
for i in range(1, 5):
    if i == 3:
        continue
    print(i)
```

**Answer:**

```text
1
2
4
```

`continue` skips the remainder of the current iteration.

### 3. Find the Bug

```python
def calculate_total(prices):
    total = 0

    for price in prices:
        total + price

    return total
```

**Problem:** The code calculates `total + price` but never assigns the result back to `total`.

**Correct version:**

```python
def calculate_total(prices):
    total = 0

    for price in prices:
        total += price

    return total
```

### 4. Count Word Frequencies

```python
def count_words(words):
    frequencies = {}

    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


words = ["python", "sql", "python", "spark"]

print(count_words(words))
```

Output:

```text
{'python': 2, 'sql': 1, 'spark': 1}
```

This pattern is useful when counting categories, statuses, or event types.

### 5. Filter Invalid Records

```python
records = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": -20},
    {"id": 3, "amount": 50},
]

valid_records = [
    record
    for record in records
    if record["amount"] >= 0
]

print(valid_records)
```

Output:

```text
[
    {'id': 1, 'amount': 100},
    {'id': 3, 'amount': 50}
]
```

This is a simple validation example. In production, rejected records should usually be counted or logged, and the handling policy should be explicit.

### 6. Handle Invalid Numeric Data

```python
def parse_amount(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


print(parse_amount("120.5"))  # 120.5
print(parse_amount("invalid"))  # None
```

Returning `None` is one possible strategy. A real pipeline may instead quarantine the record or raise an error, depending on the requirements.

### 7. Complexity Question

```python
def find_duplicate(values):
    seen = set()

    for value in values:
        if value in seen:
            return value
        seen.add(value)

    return None
```

**Expected discussion:**

- Average time complexity: \(O(n)\).
- Auxiliary space complexity: \(O(n)\) in the worst case.
- Assumption: the values are hashable.
- The function returns the first duplicate encountered in traversal order, not necessarily the most frequent value.

---

## ⚠️ Common Mistakes

1. **Memorizing definitions without understanding them:** Interviewers may ask for a working example or an edge case.
2. **Confusing assignment with copying:** `b = a` creates another reference to the same object; it does not automatically copy it.
3. **Using `is` for value comparison:** Use `==` for equality and `is` for identity.
4. **Ignoring mutability:** Mutable default arguments can preserve state across calls.
5. **Confusing `print()` with `return`:** A function that only prints a value may return `None`.
6. **Catching every exception without a policy:** Handle expected failures specifically and preserve useful diagnostic information.
7. **Removing duplicates without a business rule:** Repeated keys may represent valid updates or conflicting records.
8. **Ignoring time and space complexity:** A correct solution may be inefficient for a large dataset.
9. **Using Python where SQL is more appropriate:** Database-native joins and aggregations can avoid unnecessary data transfer.
10. **Assuming all data fits in memory:** Large datasets may require chunking, streaming, database processing, or distributed frameworks.
11. **Logging sensitive information:** Avoid exposing passwords, tokens, or confidential records.
12. **Giving vague answers:** Explain the trade-off, the conditions under which your solution works, and its limitations.

---

## 👨‍💻 Data Engineering Connection

Python interviews for Data Engineering often move beyond language syntax to practical data-processing scenarios.

### 1. Data Ingestion

**Scenario:** You receive a CSV file containing one million orders. How would you read it?

A strong answer should mention:

- Checking the file structure and encoding.
- Validating required columns.
- Converting data types.
- Considering memory limitations.
- Processing in chunks if necessary.
- Recording the number of records read and rejected.

For larger workloads, consider database bulk loading or distributed processing rather than assuming a regular Python list is appropriate.

### 2. Deduplication

**Scenario:** An hourly pipeline receives multiple records with the same `order_id`. What would you do?

A strong answer should cover:

1. Defining the business key.
2. Distinguishing exact duplicates from conflicting updates.
3. Establishing a rule for retaining or merging records.
4. Recording duplicate counts and source information.
5. Making repeated processing safe.

A repeated ID alone does not prove that two records are identical or that one should always be discarded.

### 3. Handling Invalid Data

**Scenario:** An API returns an order with a missing amount.

Possible approaches include:

- Rejecting the record.
- Quarantining it for investigation.
- Applying a documented default if the business permits it.
- Failing the task if the field is essential to correctness.

The decision depends on the business impact and data contract. Avoid silently substituting a value without justification.

### 4. Pipeline Reliability

**Scenario:** A pipeline fails after loading some records. What should happen when it is retried?

A strong answer should discuss:

- Transactions where appropriate.
- Idempotent writes.
- Stable business keys.
- Upserts or controlled insert logic.
- Checkpoints or batch identifiers.
- Logging and recovery procedures.

The goal is to prevent retries from creating unintended duplicates or inconsistent results.

### 5. Choosing the Right Tool

**Scenario:** You need to join two large tables already stored in a relational database.

SQL may be the best choice because the database can perform the join without transferring all records into Python.

If the data is too large for one machine and requires distributed computation, Spark may be appropriate.

The choice should be based on data volume, system capabilities, performance, and operational complexity.

### 6. DataPulse Case Study

For the DataPulse project, be ready to explain how Python can support:

- Ingestion from a source.
- Required-field and type validation.
- Duplicate detection.
- Freshness monitoring.
- Recording data quality issues.
- Logging execution statistics.
- Writing validated records to a database.
- Testing retries and failure scenarios.

A strong design separates the pipeline into testable components and records enough metadata for another engineer to understand what happened during a run.

---

## 🎯 Interview Questions

Use these as your primary revision checklist. Try answering each question aloud before reading the expected points.

### Python Fundamentals

**Q1. What is the difference between mutable and immutable objects?**

Expected points: Whether the object can be changed after creation, examples, and implications for references and function arguments.

**Q2. Explain the difference between `==` and `is`.**

Expected points: Value equality versus object identity, with an example.

**Q3. What is the difference between a list, tuple, set, and dictionary?**

Expected points: Mutability, ordering, duplicates, access patterns, and common use cases.

**Q4. What is the difference between shallow and deep copying?**

Expected points: Whether nested objects remain shared or are recursively copied.

**Q5. What is the difference between `return` and `print()`?**

Expected points: Returning a value to the caller versus displaying output.

### Functions and OOP

**Q6. What are positional arguments, keyword arguments, `*args`, and `**kwargs`?**

Expected points: How arguments are passed and collected.

**Q7. What is a mutable default argument, and how do you avoid the problem?**

Expected points: Definition-time evaluation and the `None`-sentinel pattern.

**Q8. What is the difference between a class and an object?**

Expected points: A class defines behavior and structure; an object is an instance.

**Q9. What is the difference between `__new__` and `__init__`?**

Expected points: Object creation versus initialization.

**Q10. When would you prefer composition over inheritance?**

Expected points: Reusing behavior through collaboration rather than creating a subtype, and reducing unnecessary coupling.

### Files and Dependencies

**Q11. How would you process a CSV file safely?**

Expected points: Encoding, context managers, schema validation, type conversion, error handling, and memory usage.

**Q12. How do you handle exceptions in a pipeline?**

Expected points: Specific exceptions, logging, recovery policy, resource cleanup, and whether the task should fail.

**Q13. What is the difference between a module and a package?**

Expected points: Reusable Python files versus an organized package namespace.

**Q14. Why use a virtual environment?**

Expected points: Package isolation, reduced dependency conflicts, and reproducible setup.

**Q15. What is the difference between `pip list` and `pip freeze`?**

Expected points: Human-readable package listing versus requirements-style output of installed versions.

### Data Engineering Scenarios

**Q16. How would you process a dataset that does not fit into memory?**

Expected points: Chunked reads, streaming, database processing, columnar formats, or distributed frameworks.

**Q17. How would you identify duplicate records?**

Expected points: Business keys, uniqueness rules, exact versus conflicting duplicates, and an explicit resolution policy.

**Q18. How would you make a data pipeline idempotent?**

Expected points: Stable keys, upserts, uniqueness constraints, transaction design, checkpoints, and safe retry behavior.

**Q19. When would you use Python instead of SQL?**

Expected points: Python for APIs, file handling, custom logic, and orchestration; SQL for relational and set-based operations. Explain that both are often used together.

**Q20. How would you investigate a pipeline that runs successfully but loads incorrect data?**

Expected points: Source validation, transformation tests, row counts, schema checks, duplicate analysis, logs, target verification, and comparison with expected business rules.

**Q21. How would you handle a source API that occasionally returns errors?**

Expected points: Timeouts, status-code handling, bounded retries for transient errors, rate limits, pagination, and monitoring.

**Q22. How would you monitor data freshness?**

Expected points: Source timestamps, ingestion timestamps, expected arrival frequency, a defined freshness threshold, and alerts when the threshold is exceeded.

**Q23. How would you test a data transformation function?**

Expected points: Unit tests, valid and invalid inputs, boundary conditions, expected outputs, and tests for missing values or duplicates.

**Q24. How would you explain a technical decision to a non-technical stakeholder?**

Expected points: Business impact, risk, trade-offs, reliability, and measurable outcomes rather than unnecessary implementation details.

---

## 📝 Practice

### Exercise 1: Python Fundamentals Assessment

Write a program that:

1. Accepts a list of numbers.
2. Removes duplicate values while preserving their first-occurrence order.
3. Calculates the sum and average.
4. Handles an empty input.
5. Returns the results from a function.

Explain the time and space complexity of your solution.

### Exercise 2: Record Validation

Given:

```python
orders = [
    {"order_id": 101, "amount": 250.0},
    {"order_id": 102, "amount": -10.0},
    {"order_id": None, "amount": 100.0},
    {"order_id": 104, "amount": 75.0},
]
```

Write a function that separates valid records from invalid records and provides a reason for each rejection.

Do not discard invalid records silently.

### Exercise 3: Deduplication Design

Create a dataset containing:

- Exact duplicate records.
- Repeated IDs with different amounts.
- A legitimate update to an existing order.

Design a deduplication strategy and explain why your chosen rule is appropriate.

### Exercise 4: File Processing

Write a script that reads a CSV file, validates its schema, converts values to the expected types, and writes valid and invalid records to separate outputs.

Include logging and exception handling.

### Exercise 5: Data Pipeline Design

Design a pipeline that extracts data from an API and loads it into a relational database.

Explain:

1. How you would handle pagination.
2. How you would validate the response.
3. How you would manage retries.
4. How you would avoid duplicate loads.
5. How you would track execution.
6. How you would test failures.

### Exercise 6: Mock Interview

Answer the following questions aloud without reading the notes:

1. Explain dynamic typing in Python.
2. Compare lists, tuples, sets, and dictionaries.
3. Explain shallow copying with an example.
4. Describe how you would process a large CSV.
5. Explain idempotency in data pipelines.
6. Compare Python transformations with SQL transformations.
7. Explain how you would handle conflicting duplicate records.
8. Describe how you would investigate incorrect data in a successful pipeline run.

For each answer, aim to provide a definition, a concrete example, and a trade-off or limitation.

### Exercise 7: Self-Assessment

Mark each skill only after you can demonstrate it independently.

- [ ] Explain Python fundamentals without memorized definitions.
- [ ] Select an appropriate data structure for a given problem.
- [ ] Write reusable functions with predictable behavior.
- [ ] Handle files and exceptions safely.
- [ ] Create and recreate a virtual environment.
- [ ] Manage dependencies using pip.
- [ ] Validate and transform records.
- [ ] Detect duplicates using a defined business key.
- [ ] Explain time and space complexity.
- [ ] Design safe retries and idempotent data loads.
- [ ] Explain when to use Python, SQL, or Spark.
- [ ] Debug a pipeline using logs, tests, and data quality checks.

---

> **Next Step:** Use this document as a revision guide, not a memorization sheet. Practice writing code, explain your decisions aloud, and connect each Python concept to a realistic data pipeline scenario. Keep the status as `🟡 In Progress` until you can answer the core questions and complete the practical exercises independently.