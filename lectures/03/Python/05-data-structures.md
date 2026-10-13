# Data Structures

> 📌 **Status:** 🟡 In Progress

## 📖 Overview

**Data Structures** are ways of organizing and storing data so that it can be accessed, modified, and processed efficiently.

Python provides several built-in data structures, including:

- **Lists:** Ordered, mutable collections.
- **Tuples:** Ordered, immutable collections.
- **Sets:** Collections of unique, hashable elements.
- **Dictionaries:** Key-value mappings.

Choosing the appropriate data structure affects code readability, memory usage, and performance.

As a future **Data Engineer**, data structures are essential for processing records, removing duplicate values, grouping information, validating datasets, and transforming data before loading it into databases or distributed processing systems.

---

## 🧠 Concepts

### 1. Lists

A **list** is an ordered, mutable collection that allows duplicate values.

```python
numbers = [10, 20, 30, 20]

print(numbers)
print(numbers[0])  # 10
print(numbers[-1]) # 20
```

Key characteristics:

- Preserves element order.
- Supports indexing and slicing.
- Allows duplicate values.
- Can contain elements of different types.
- Supports adding, removing, and modifying elements.

#### Common List Methods

| Method | Purpose | Example |
|---|---|---|
| `append(x)` | Adds one element to the end | `numbers.append(40)` |
| `extend(iterable)` | Adds elements from an iterable | `numbers.extend([50, 60])` |
| `insert(i, x)` | Inserts an element at an index | `numbers.insert(0, 5)` |
| `remove(x)` | Removes the first matching value | `numbers.remove(20)` |
| `pop(i)` | Removes and returns an element | `numbers.pop()` |
| `sort()` | Sorts the list in place | `numbers.sort()` |
| `reverse()` | Reverses the list in place | `numbers.reverse()` |
| `index(x)` | Returns the first matching index | `numbers.index(30)` |
| `count(x)` | Counts occurrences of a value | `numbers.count(20)` |
| `copy()` | Creates a shallow copy | `other = numbers.copy()` |
| `clear()` | Removes all elements | `numbers.clear()` |

**Important:** Methods such as `append()`, `sort()`, and `reverse()` modify the existing list. They generally return `None`, rather than returning the modified list.

#### Adding and Modifying Elements

```python
numbers = [10, 20, 30]

numbers.append(40)
numbers[0] = 99

print(numbers)  # [99, 20, 30, 40]
```

#### List Mutability and Aliasing

Assignment does not automatically create a copy.

```python
numbers = [10, 20, 30]
other = numbers

other[0] = 99

print(numbers)  # [99, 20, 30]
print(other)    # [99, 20, 30]
```

Both names refer to the same list object.

To create a shallow copy:

```python
numbers = [10, 20, 30]
other = numbers.copy()

other[0] = 99

print(numbers)  # [10, 20, 30]
print(other)    # [99, 20, 30]
```

A shallow copy creates a new outer list, but nested mutable objects may still be shared.

### 2. Tuples

A **tuple** is an ordered collection whose element references cannot be reassigned after creation.

```python
coordinates = (10, 20)
record = ("Amin", 21, True)

print(coordinates[0])  # 10
print(record[1])       # 21
```

Key characteristics:

- Preserves order.
- Supports indexing and slicing.
- Allows duplicate values.
- Does not support reassignment of individual elements.
- Can contain different data types.

```python
coordinates = (10, 20)

# coordinates[0] = 50  # TypeError
```

A tuple is useful for representing a fixed group of values, such as coordinates or a record that should not have its elements reassigned.

**Important:** A tuple can contain a mutable object, such as a list. The tuple itself does not allow reassignment of its elements, but the contained list can still be modified.

```python
data = ([1, 2], 3)

data[0].append(99)

print(data)  # ([1, 2, 99], 3)
```

#### Creating a Single-Element Tuple

A comma is required:

```python
single = (10,)
not_a_tuple = (10)

print(type(single))      # <class 'tuple'>
print(type(not_a_tuple)) # <class 'int'>
```

### 3. Sets

A **set** is a mutable collection of unique, hashable elements.

```python
ids = {101, 102, 103, 101}

print(ids)  # Contains 101, 102, and 103 only
```

Key characteristics:

- Contains unique elements.
- Does not guarantee iteration order.
- Does not support positional indexing.
- Supports efficient membership checks in typical cases.
- Elements must be hashable.

#### Common Set Operations

```python
first = {1, 2, 3}
second = {3, 4, 5}

print(first | second)  # Union: {1, 2, 3, 4, 5}
print(first & second)  # Intersection: {3}
print(first - second)  # Difference: {1, 2}
print(first ^ second)  # Symmetric difference: {1, 2, 4, 5}
```

The order shown in set output is illustrative; do not rely on it.

#### Common Set Methods

| Method | Purpose |
|---|---|
| `add(x)` | Adds an element |
| `update(iterable)` | Adds elements from an iterable |
| `remove(x)` | Removes an element; raises `KeyError` if absent |
| `discard(x)` | Removes an element if present |
| `pop()` | Removes and returns an arbitrary element |
| `clear()` | Removes all elements |
| `issubset(other)` | Checks whether all elements are in another set |
| `issuperset(other)` | Checks whether the set contains all elements of another set |

Use `discard()` when an element may be absent and absence should not raise an error.

#### Removing Duplicates

```python
customer_ids = [101, 102, 101, 103, 102]

unique_ids = set(customer_ids)

print(unique_ids)
```

This removes duplicate values, but it does not preserve the original list order.

If order matters:

```python
unique_ids = list(dict.fromkeys(customer_ids))

print(unique_ids)  # [101, 102, 103]
```

**Data Engineering note:** Removing duplicate values is not the same as resolving duplicate records. If two records have the same `order_id` but conflicting amounts or timestamps, the pipeline needs an explicit rule to decide what to keep or how to merge them.

### 4. Dictionaries

A **dictionary** stores key-value pairs.

```python
order = {
    "order_id": 101,
    "amount": 250,
    "status": "paid"
}

print(order["order_id"])  # 101
print(order.get("amount")) # 250
```

Key characteristics:

- Keys are unique.
- Keys must be hashable.
- Values can have different types.
- Dictionaries are mutable.
- Insertion order is guaranteed in Python 3.7 and later.

#### Accessing Values

```python
order = {"order_id": 101, "amount": 250}

print(order["amount"])       # 250
print(order.get("customer")) # None
```

Using a missing key with square brackets raises `KeyError`. The `get()` method returns `None` by default when the key is absent, or a supplied default value.

```python
print(order.get("customer", "Unknown"))
```

#### Adding and Updating Values

```python
order["customer"] = "Amin"
order["amount"] = 300

print(order)
```

#### Removing Values

```python
order = {
    "order_id": 101,
    "amount": 250,
    "status": "paid"
}

status = order.pop("status")

print(status)  # paid
print(order)
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

Useful dictionary methods include:

- `keys()` — provides the dictionary's keys.
- `values()` — provides its values.
- `items()` — provides key-value pairs.
- `get()` — retrieves a value with a fallback.
- `update()` — adds or updates key-value pairs.
- `pop()` — removes a key and returns its value.

Dictionaries are useful for representing JSON objects, API responses, configuration settings, and individual data records.

### 5. Indexing

Indexing accesses an element by its position.

Python uses zero-based indexing for sequences such as lists and tuples.

```python
colors = ["red", "green", "blue"]

print(colors[0])   # red
print(colors[1])   # green
print(colors[-1])  # blue
print(colors[-2])  # green
```

Positive indexes count from the beginning. Negative indexes count from the end.

Indexing a sequence outside its valid range raises `IndexError`.

### 6. Slicing

Slicing extracts a portion of a sequence.

**Syntax:**

```python
sequence[start:stop:step]
```

- `start`: The first index to include.
- `stop`: The index at which slicing stops, excluding that position.
- `step`: The increment between selected indexes.

```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])  # [1, 2, 3]
print(numbers[:3])   # [0, 1, 2]
print(numbers[3:])   # [3, 4, 5]
print(numbers[::2]) # [0, 2, 4]
print(numbers[::-1])# [5, 4, 3, 2, 1, 0]
```

Slicing is useful for selecting subsets of data or creating shallow copies of sequences.

```python
numbers = [1, 2, 3]
other = numbers[:]

other[0] = 99

print(numbers)  # [1, 2, 3]
print(other)    # [99, 2, 3]
```

For a list, slicing creates a shallow copy, not a fully independent copy of nested mutable objects.

### 7. Nested Data Structures

Data structures can contain other data structures.

```python
orders = [
    {"order_id": 101, "amount": 250},
    {"order_id": 102, "amount": 400},
    {"order_id": 103, "amount": 150}
]

print(orders[0]["order_id"])  # 101
```

Here:

- `orders` is a list.
- Each element is a dictionary.
- Each dictionary represents an order.

This pattern is common when processing JSON arrays containing objects.

### 8. Choosing the Right Data Structure

| Requirement | Suitable Structure | Reason |
|---|---|---|
| Maintain an ordered collection | `list` | Supports ordering, indexing, and modification |
| Represent a fixed group of values | `tuple` | Prevents reassignment of tuple elements |
| Track unique hashable values | `set` | Enforces uniqueness |
| Associate keys with values | `dict` | Provides key-based access |
| Preserve order while removing repeated hashable values | `dict` keys | Modern dictionaries preserve insertion order |

Choose based on the required behavior, not just personal preference.

### 9. Basic Time Complexity

Time complexity describes how the number of operations typically grows with input size.

| Operation | Typical Complexity |
|---|---|
| List indexing | \(O(1)\) |
| List append | Amortized \(O(1)\) |
| List search | \(O(n)\) |
| List insertion or deletion near the beginning | \(O(n)\) |
| Dictionary lookup | Average \(O(1)\) |
| Set membership check | Average \(O(1)\) |
| Sorting a list | Typically \(O(n \log n)\) |

These are typical complexity guarantees or average-case expectations, not universal timings. Actual performance depends on implementation, data, and operation.

---

## 💻 Syntax & Examples

### Example 1: Process Orders

```python
orders = [
    {"order_id": 101, "amount": 250},
    {"order_id": 102, "amount": 400},
    {"order_id": 103, "amount": 150}
]

total_amount = 0

for order in orders:
    total_amount += order["amount"]

print("Total amount:", total_amount)
```

Output:

```text
Total amount: 800
```

### Example 2: Find Unique Customer IDs

```python
customer_ids = [101, 102, 101, 103, 102, 104]

unique_ids = set(customer_ids)

print("Unique customers:", len(unique_ids))
```

Output:

```text
Unique customers: 4
```

This counts unique ID values, assuming the IDs use consistent representations. For example, the string `"101"` and integer `101` are different values.

### Example 3: Group Orders by Status

```python
orders = [
    {"order_id": 101, "status": "paid"},
    {"order_id": 102, "status": "pending"},
    {"order_id": 103, "status": "paid"}
]

orders_by_status = {}

for order in orders:
    status = order["status"]

    if status not in orders_by_status:
        orders_by_status[status] = []

    orders_by_status[status].append(order)

print(orders_by_status)
```

This example groups records into dictionary values containing lists of orders.

### Example 4: Work with Nested Data

```python
customers = {
    "customer_1": {
        "name": "Amin",
        "orders": [101, 102]
    },
    "customer_2": {
        "name": "Ahmed",
        "orders": [103]
    }
}

print(customers["customer_1"]["name"])
print(customers["customer_1"]["orders"])
```

Nested dictionaries and lists can represent structured records, but deeply nested structures may become difficult to maintain. Consider defining clearer schemas or data models when complexity increases.

---

## ⚠️ Common Mistakes

1. **Confusing assignment with copying:** `other = numbers` creates an alias to the same list.
2. **Assuming `append()` returns the updated list:** It modifies the list in place and returns `None`.
3. **Assuming tuples make nested objects immutable:** Mutable elements inside tuples can still change.
4. **Expecting sets to preserve order:** Set iteration order is not guaranteed.
5. **Assuming a set solves every duplicate problem:** It removes duplicate elements but does not resolve conflicting records.
6. **Accessing a missing dictionary key without handling it:** This can raise `KeyError`.
7. **Forgetting that slicing excludes the stop index:** `numbers[1:4]` includes indexes 1, 2, and 3.
8. **Assuming slicing makes a deep copy:** Nested mutable objects can still be shared.
9. **Using a list when frequent membership checks dominate:** A set may be more appropriate for hashable values.
10. **Ignoring type consistency:** The string `"101"` and integer `101` are different values, which may affect joins and deduplication.

---

## 👨‍💻 Data Engineering Connection

Data structures are fundamental to handling data in memory before it is stored or processed by other systems.

### 1. API and JSON Processing

A JSON object typically becomes a Python dictionary, while a JSON array typically becomes a Python list.

```python
api_response = {
    "status": "success",
    "data": [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200}
    ]
}

records = api_response["data"]

for record in records:
    print(record["id"], record["amount"])
```

Understanding nested dictionaries and lists is important when extracting data from APIs.

### 2. Deduplication

A set can efficiently track IDs already encountered.

```python
seen_ids = set()
duplicates = []

for order in orders:
    order_id = order["order_id"]

    if order_id in seen_ids:
        duplicates.append(order_id)
    else:
        seen_ids.add(order_id)
```

This example detects repeated IDs in the order in which they are encountered. It does not merge records or decide which conflicting version is correct.

### 3. Data Aggregation

Dictionaries can accumulate metrics by category.

```python
orders = [
    {"status": "paid", "amount": 100},
    {"status": "pending", "amount": 50},
    {"status": "paid", "amount": 200}
]

totals = {}

for order in orders:
    status = order["status"]
    totals[status] = totals.get(status, 0) + order["amount"]

print(totals)
```

Output:

```text
{'paid': 300, 'pending': 50}
```

This illustrates in-memory aggregation. For large datasets, SQL or distributed processing frameworks may be more appropriate.

### 4. Memory and Scalability

Lists and dictionaries store objects in memory. Keeping an entire large dataset in a Python collection can consume significant memory.

For larger workloads, consider:

- Reading data in batches.
- Streaming records where possible.
- Processing data with SQL engines.
- Using Pandas for suitable in-memory datasets.
- Using PySpark when distributed processing is needed.

The right choice depends on dataset size, available memory, processing requirements, and system architecture.

### 5. Connection to DataPulse

DataPulse can use data structures to support data quality checks:

- A **set** can track previously encountered `order_id` values.
- A **dictionary** can map each ID to a chosen record or processing state.
- A **list** can collect invalid records for reporting.
- A **dictionary** can represent a structured quality issue with its type, timestamp, source, and status.

For example:

```python
quality_issue = {
    "issue_type": "DUPLICATE_ORDER_ID",
    "order_id": 101,
    "source": "orders.csv",
    "status": "open"
}
```

This record describes an issue, but a production implementation should also capture the relevant context, apply a clear deduplication policy, and persist the issue in the database.

---

## 🎯 Interview Questions

### Q1. What is the difference between a list and a tuple?

Both are ordered collections. Lists are mutable, while tuple elements cannot be reassigned after creation.

### Q2. What is the difference between a list and a set?

Lists preserve order and allow duplicates. Sets contain unique, hashable elements and do not guarantee iteration order.

### Q3. What is the difference between a set and a dictionary?

A set stores unique elements. A dictionary stores key-value pairs with unique keys.

### Q4. Why is dictionary lookup typically \(O(1)\)?

Dictionaries use hash-based lookup. Average-case lookup is typically constant time, although collisions and implementation details can affect performance.

### Q5. Why can a set be useful for deduplication?

A set tracks unique hashable values and supports efficient membership checks in typical cases.

### Q6. What is the difference between `append()` and `extend()`?

`append()` adds one object to a list. `extend()` adds elements from an iterable individually.

### Q7. What is the difference between `remove()` and `pop()`?

`remove(value)` removes the first matching value. `pop(index)` removes and returns the element at an index, using the last element by default.

### Q8. What is the difference between a shallow copy and a deep copy?

A shallow copy creates a new outer collection but may share nested objects. A deep copy recursively copies nested objects where supported.

### Q9. How would you detect duplicate IDs in a large batch?

Maintain a set of previously seen IDs and check each incoming ID against it. For datasets too large for memory, use database constraints, SQL, distributed processing, or an external state store.

### Q10. Why might you choose a dictionary instead of a list?

A dictionary is appropriate when data must be retrieved by a key, such as finding a record by ID, rather than searching sequentially through a list.

### Q11. How do Python data structures relate to JSON?

JSON objects commonly map to Python dictionaries, and JSON arrays map to Python lists. Nested JSON data becomes nested dictionaries and lists.

### Q12. Does detecting a duplicate mean the pipeline has resolved it?

No. Detection identifies repeated keys or records. Resolution requires a business rule, such as keeping the newest record, retaining the first valid record, merging fields, or quarantining conflicting records.

---

## 📝 Practice

### Exercise 1: List Operations

Given:

```python
numbers = [10, 20, 30, 20, 40]
```

1. Print the first and last elements.
2. Print the slice containing `20, 30, 20`.
3. Add `50` to the end.
4. Remove the first occurrence of `20`.
5. Count how many times `20` appears.

### Exercise 2: Aliasing vs Copying

Predict the output:

```python
numbers = [1, 2, 3]
other = numbers
copy_of_numbers = numbers.copy()

other[0] = 99
copy_of_numbers[1] = 88

print(numbers)
print(other)
print(copy_of_numbers)
```

Explain which names refer to the same list.

### Exercise 3: Set Operations

Given:

```python
source_a = {1, 2, 3, 4}
source_b = {3, 4, 5, 6}
```

Calculate the union, intersection, difference, and symmetric difference.

Explain how these operations could compare IDs from two data sources.

### Exercise 4: Dictionary Operations

Given:

```python
order = {
    "order_id": 101,
    "amount": 250
}
```

1. Add a `status` field.
2. Update the amount.
3. Retrieve a potentially missing `customer_id` safely.
4. Iterate through all key-value pairs.
5. Remove the `status` field.

### Exercise 5: Group Orders

Given a list of order dictionaries, group them by status using a dictionary where each status maps to a list of orders.

### Exercise 6: Deduplicate IDs

Given:

```python
order_ids = [101, 102, 101, 103, 102, 104]
```

Produce a list of unique IDs while preserving their original order.

Explain why converting directly to a set does not guarantee the same order.

### Exercise 7: Data Engineering Scenario

Two data sources contain order records with overlapping IDs.

Design a solution that:

1. Identifies repeated order IDs.
2. Preserves the source of each record.
3. Detects conflicting amounts for the same ID.
4. Applies an explicit rule for choosing or merging records.
5. Logs unresolved conflicts.

Explain which data structures you would use and why.

### Exercise 8: Complexity Challenge

Explain the difference between these approaches for checking whether an ID exists in a collection:

- Searching a list.
- Checking membership in a set.
- Looking up a dictionary key.

Discuss typical time complexity and the memory trade-offs.

---

> **Next Step:** Practice lists, tuples, sets, dictionaries, indexing, slicing, and mutability. Keep the status as `🟡 In Progress` until you can solve the exercises and explain why you selected each data structure.