# 🐍 Python Data Types

> 📌 **Status:** 🟡 In Progress  
> 🎯 **Focus:** Understanding how Python represents, stores, and works with different types of data.

---

## 📖 Overview

**Data Types** define the kind of value an object represents and determine which operations can be performed on it.

In Python, understanding data types is fundamental because almost every program involves manipulating different kinds of data.

As a future **Data Engineer**, understanding data types is especially important because real-world data comes in many forms:

- Text
- Numbers
- Boolean values
- Collections
- Missing values
- Structured records
- JSON objects
- Data loaded from databases
- Data received from APIs
- Data processed using Pandas and PySpark

This section covers Python's built-in data types, their behavior, type conversion, mutability, and their applications in Data Engineering.

---

## 🧠 Core Concepts

### 1. What Is a Data Type?

A **data type** describes the kind of value an object represents and determines the operations that can be performed on it.

```python
name = "Amin"
age = 21
height = 175.5
is_student = True

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>
```

The `type()` function returns the type of an object.

**Important:** Python is dynamically typed. Variable names do not require explicit type declarations, and the same name can refer to objects of different types at different times.

```python
x = 10
print(type(x))  # <class 'int'>

x = "10"
print(type(x))  # <class 'str'>

x = 10.0
print(type(x))  # <class 'float'>
```

The name `x` refers to a different object after each assignment.

### 2. Python's Built-in Data Types

Python provides several built-in data types.

| Category | Data Type | Example |
|---|---|---|
| Numeric | `int` | `age = 21` |
| Numeric | `float` | `price = 99.5` |
| Numeric | `complex` | `z = 2 + 3j` |
| Boolean | `bool` | `is_valid = True` |
| Text | `str` | `name = "Amin"` |
| Sequence | `list` | `numbers = [1, 2, 3]` |
| Sequence | `tuple` | `point = (10, 20)` |
| Sequence | `range` | `numbers = range(5)` |
| Set | `set` | `ids = {1, 2, 3}` |
| Set | `frozenset` | `ids = frozenset({1, 2, 3})` |
| Mapping | `dict` | `user = {"id": 1}` |
| Binary | `bytes` | `data = b"ABC"` |
| Binary | `bytearray` | `data = bytearray(b"ABC")` |
| Binary | `memoryview` | `view = memoryview(b"ABC")` |
| Special | `NoneType` | `result = None` |

The most frequently used types in beginner Python and Data Engineering are `int`, `float`, `bool`, `str`, `list`, `tuple`, `set`, `dict`, and `NoneType`.

### 3. Numeric Types

#### Integer (`int`)

Represents whole numbers without a decimal component.

```python
age = 21
quantity = 100
temperature = -5

print(type(age))  # <class 'int'>
```

Python integers can represent arbitrarily large integers, subject to available memory.

#### Float (`float`)

Represents floating-point numbers.

```python
price = 99.99
temperature = 36.5

print(type(price))  # <class 'float'>
```

Floating-point arithmetic can introduce small precision errors because many decimal fractions cannot be represented exactly in binary.

```python
print(0.1 + 0.2)
# 0.30000000000000004
```

For financial calculations requiring exact decimal arithmetic, Python's `decimal.Decimal` may be more appropriate than `float`.

#### Complex (`complex`)

Represents numbers with real and imaginary components.

```python
z = 2 + 3j

print(z.real)  # 2.0
print(z.imag)  # 3.0
```

Complex numbers are useful in scientific and mathematical applications but are less common in typical data pipelines.

### 4. Boolean (`bool`)

The Boolean type represents two logical values:

- `True`
- `False`

```python
is_valid = True
is_deleted = False

print(type(is_valid))  # <class 'bool'>
print(10 > 5)          # True
print(10 == 5)         # False
```

Boolean values are commonly used in conditions, validation rules, filtering, and quality checks.

**Important:** In Python, `bool` is a subclass of `int`, so `True` behaves like `1` and `False` behaves like `0` in numeric contexts. This is a language feature, but it is usually better to treat them as logical values in application code.

### 5. String (`str`)

A string represents text and is created using single, double, or triple quotes.

```python
name = "Amin"
city = 'Arish'
message = """Welcome to Python"""

print(type(name))  # <class 'str'>
```

Strings are **immutable**, which means their characters cannot be modified in place.

```python
name = "Python"

# name[0] = "J"  # TypeError

name = "J" + name[1:]
print(name)  # Jython
```

The final assignment creates a new string and binds the name `name` to it.

Common string operations:

```python
text = "  Data Engineering  "

print(text.strip())             # Remove surrounding whitespace
print(text.lower())             # Convert to lowercase
print(text.upper())             # Convert to uppercase
print(text.replace("Data", "Big Data"))
print("Data" in text)           # True
```

Strings are particularly important when processing CSV files, JSON payloads, API responses, log messages, and text columns in databases.

### 6. List (`list`)

A list is an ordered, mutable collection that allows duplicate values.

```python
numbers = [10, 20, 30, 20]

print(numbers[0])  # 10
print(numbers[-1]) # 20

numbers[1] = 99
numbers.append(40)

print(numbers)  # [10, 99, 30, 20, 40]
```

Key characteristics:

- Ordered collection.
- Mutable: elements can be changed.
- Allows duplicates.
- Can contain values of different types.
- Supports indexing and slicing.

Lists are useful for holding batches of records, intermediate processing results, and collections of values.

### 7. Tuple (`tuple`)

A tuple is an ordered, immutable collection.

```python
coordinates = (10, 20)
record = ("Amin", 21, True)

print(coordinates[0])  # 10
print(type(record))    # <class 'tuple'>
```

Unlike lists, tuple elements cannot be reassigned after the tuple is created.

```python
coordinates = (10, 20)

# coordinates[0] = 50  # TypeError
```

Tuples are useful for fixed groups of values, such as coordinates or records that should not have their elements reassigned.

**Important:** A tuple can contain a mutable object, such as a list. The tuple's element references cannot be reassigned, but the contained list may still be modified.

### 8. Set (`set`)

A set is a mutable collection of unique, hashable elements.

```python
ids = {101, 102, 103, 101}

print(ids)  # Contains 101, 102, and 103 only
```

Sets do not guarantee an iteration order, so do not rely on the order in which their elements are displayed.

Common operations:

```python
first = {1, 2, 3}
second = {3, 4, 5}

print(first | second)  # Union
print(first & second)  # Intersection
print(first - second)  # Difference
```

Sets are useful for membership checks and finding distinct values.

For example, a data pipeline can use a set to identify unique IDs in a batch. However, a set alone does not resolve conflicting duplicate records or preserve their full source data.

### 9. Dictionary (`dict`)

A dictionary stores data as key-value pairs.

```python
user = {
    "id": 101,
    "name": "Amin",
    "active": True
}

print(user["name"])  # Amin
print(user.get("email"))  # None
```

Key characteristics:

- Keys are unique.
- Keys must be hashable.
- Values can be of different types.
- Dictionaries are mutable.
- Insertion order is guaranteed in Python 3.7 and later.

You can add or update values:

```python
user["email"] = "amin@example.com"
user["active"] = False
```

Dictionaries are particularly useful for representing JSON objects, API responses, configuration settings, and individual records.

**Important:** `user["email"]` raises a `KeyError` if the key does not exist, while `user.get("email")` returns `None` by default.

### 10. None (`NoneType`)

`None` represents the absence of a value.

```python
result = None

print(result)        # None
print(type(result))  # <class 'NoneType'>
```

Use `is None` to check whether a value is `None`.

```python
if result is None:
    print("No result available")
```

`None` is not the same as `0`, `False`, or an empty string.

In Data Engineering, `None` may represent a missing field in Python data, but missing values can be represented differently in other systems. For example, SQL uses `NULL`, while Pandas and NumPy have their own missing-value conventions.

### 11. Mutable vs Immutable Types

Mutability describes whether an object can be modified after it is created.

| Mutable | Immutable |
|---|---|
| `list` | `int` |
| `dict` | `float` |
| `set` | `bool` |
| `bytearray` | `str` |
| | `tuple` |
| | `bytes` |
| | `frozenset` |

This table describes the objects themselves, not whether a variable name can be reassigned.

Example:

```python
numbers = [1, 2, 3]
other = numbers

other[0] = 99

print(numbers)  # [99, 2, 3]
print(other)    # [99, 2, 3]
```

Both names refer to the same list. Modifying the list through one name is visible through the other.

To create a shallow copy:

```python
numbers = [1, 2, 3]
other = numbers.copy()

other[0] = 99

print(numbers)  # [1, 2, 3]
print(other)    # [99, 2, 3]
```

A shallow copy creates a new outer collection, but nested mutable objects may still be shared.

### 12. Type Conversion (Casting)

Type conversion means converting a value from one type to another.

Common conversion functions include:

- `int()`
- `float()`
- `str()`
- `bool()`
- `list()`
- `tuple()`
- `set()`
- `dict()` — for compatible inputs.

Example:

```python
age_text = "21"
price_text = "99.5"

age = int(age_text)
price = float(price_text)

print(age + 1)      # 22
print(price + 0.5)  # 100.0
```

Invalid conversions can raise errors:

```python
# int("hello")  # ValueError
```

Conversion can also lose information:

```python
print(int(9.8))  # 9
```

`int()` truncates the fractional part of a floating-point number toward zero; it does not round to the nearest integer.

**Data Engineering note:** Validate incoming values before converting them, and handle invalid records according to the pipeline's error-handling policy.

### 13. Checking Types

Use `type()` to inspect an object's exact type.

```python
value = 100

print(type(value))  # <class 'int'>
```

Use `isinstance()` when checking whether an object belongs to a type or its subclasses.

```python
value = True

print(isinstance(value, bool))  # True
print(isinstance(value, int))   # True
```

Because `bool` is a subclass of `int`, `isinstance(True, int)` returns `True`.

If a pipeline requires an actual integer and must reject Boolean values, validate that explicitly:

```python
value = True

if type(value) is int:
    print("Valid integer")
else:
    print("Not an exact int type")
```

Choose validation rules based on the actual requirements of the data.

---

## 💻 Syntax & Examples

### Example 1: Inspect Different Types

```python
values = [
    100,
    99.5,
    "Python",
    True,
    [1, 2, 3],
    (1, 2),
    {1, 2, 3},
    {"id": 101},
    None
]

for value in values:
    print(value, type(value))
```

### Example 2: Convert API Data

API responses frequently represent values as strings or JSON values.

```python
record = {
    "order_id": "1001",
    "amount": "250.50",
    "is_paid": True
}

record["order_id"] = int(record["order_id"])
record["amount"] = float(record["amount"])

print(record)
```

In a production pipeline, add validation and error handling before assuming every record contains valid values.

### Example 3: Remove Duplicate Values

```python
customer_ids = [101, 102, 101, 103, 102]

unique_ids = set(customer_ids)

print(unique_ids)
```

A set removes duplicate values, but the output order is not guaranteed. If the original order must be preserved:

```python
unique_ids = list(dict.fromkeys(customer_ids))

print(unique_ids)  # [101, 102, 103]
```

These examples demonstrate in-memory deduplication. Real pipelines may require a defined business key, conflict-resolution rules, and persistent logging.

---

## ⚠️ Common Mistakes

1. **Confusing `"21"` with `21`:** The first is a string; the second is an integer.
2. **Assuming `float` is always exact:** Floating-point arithmetic can produce small precision errors.
3. **Assuming a tuple makes every contained object immutable:** A tuple can contain mutable lists or dictionaries.
4. **Assuming sets preserve insertion order:** Their iteration order is not guaranteed.
5. **Assuming assigning a list to another variable copies it:** `other = numbers` creates another reference to the same list.
6. **Assuming `int()` rounds a number:** It truncates the fractional part toward zero.
7. **Using dictionary indexing without checking a key:** A missing key can raise `KeyError`.
8. **Treating `None`, `False`, `0`, and `""` as equivalent:** They are different values with different meanings.
9. **Converting production data without validation:** Unexpected input may cause errors or incorrect results.
10. **Assuming Python types map directly to database types:** Type mapping depends on the database, connector, schema, and conversion rules.

---

## 👨‍💻 Data Engineering Connection

Understanding data types is essential for building reliable data pipelines.

### 1. Data Ingestion

Data arriving from CSV files, JSON documents, APIs, and databases may use different representations.

For example, a CSV field containing `"250.50"` is typically read as text by a basic CSV reader. The pipeline may need to validate and convert it before calculations.

### 2. Schema Enforcement

A data schema defines the expected fields and their types.

Example:

| Field | Expected Type | Example |
|---|---|---|
| `order_id` | Integer | `1001` |
| `amount` | Decimal | `250.50` |
| `customer_name` | String | `"Amin"` |
| `is_paid` | Boolean | `True` |

A pipeline should detect missing fields, invalid values, and unexpected types instead of silently assuming all records are valid.

For financial amounts, a decimal type may be preferable to a binary floating-point type.

### 3. Data Quality

Data type validation is part of data quality.

For example, a record with `"unknown"` in an `amount` field expected to be numeric should be flagged, rejected, or quarantined according to an explicit policy.

Possible quality checks include:

- Type validity.
- Required fields.
- Null or missing values.
- Valid ranges.
- Duplicate business keys.
- Schema consistency.

### 4. Python vs SQL Types

Python and SQL have different type systems.

For example:

- Python `int` may map to different SQL integer types depending on the database and connector.
- Python `float` may map to a floating-point SQL type.
- Python `None` commonly maps to SQL `NULL` through database drivers.
- Python `str` may map to SQL `VARCHAR`, `TEXT`, or another character type.

Always check the target database schema and connector behavior.

### 5. Pandas and PySpark

Data types also affect data processing libraries.

- **Pandas:** Uses types such as `int64`, `float64`, `object`, `string`, and nullable types. Missing-value behavior depends on the dtype.
- **PySpark:** Uses a defined schema with types such as `IntegerType`, `LongType`, `StringType`, `BooleanType`, and `DecimalType`.

Explicit schemas and deliberate conversions can improve data quality, reduce ambiguity, and make pipelines more predictable.

### 6. Connection to DataPulse

In the DataPulse project, data type validation can be one of the data quality checks.

For example, if `order_id` is expected to be an integer but arrives as an invalid string, DataPulse could record:

- **Issue type:** `INVALID_DATA_TYPE`
- **Affected field:** `order_id`
- **Expected type:** Integer
- **Actual value:** The received value
- **Status:** Open, resolved, or another defined status
- **Timestamp:** When the issue was detected
- **Source:** The originating file, API, or dataset

This makes the issue traceable instead of silently allowing bad data into downstream transformations.

---

## 🎯 Interview Questions

### Q1. What are data types in Python?

Data types identify the kind of object a value represents and determine which operations are supported.

### Q2. What is the difference between `int` and `float`?

`int` represents integers, while `float` represents floating-point numbers that can include fractional values.

### Q3. What is the difference between a list and a tuple?

Both are ordered collections, but lists are mutable and tuples are immutable with respect to their element references.

### Q4. What is the difference between a set and a list?

Lists preserve order and allow duplicates. Sets contain unique, hashable elements and do not guarantee iteration order.

### Q5. What is the difference between `None` and `False`?

`None` represents the absence of a value, while `False` is a Boolean value representing a negative logical result.

### Q6. What is type conversion?

Type conversion transforms a value from one type to another, such as converting `"21"` to the integer `21`.

### Q7. What is the difference between `type()` and `isinstance()`?

`type()` returns an object's type. `isinstance()` checks whether an object is an instance of a specified type or one of its subclasses.

### Q8. Why does `other = numbers` not copy a list?

Assignment binds another name to the same list object. Mutating the list through either name affects the shared object.

### Q9. Why are data types important in Data Engineering?

They help enforce schemas, validate incoming data, prevent invalid transformations, and maintain consistency across files, APIs, databases, and processing frameworks.

### Q10. How would you handle an invalid numeric value received from an API?

Validate the value, attempt conversion using appropriate error handling, and apply a defined policy such as logging, quarantining, rejecting, or correcting the record when justified.

---

## 📝 Practice

### Exercise 1: Identify the Types

Predict the output before running the code.

```python
x = 10
y = "10"
z = 10.0
flag = True

print(type(x))
print(type(y))
print(type(z))
print(type(flag))
```

### Exercise 2: Type Conversion

Convert the following values to the appropriate types:

```python
age = "21"
price = "150.75"
```

Requirements:

1. Convert `age` to an integer.
2. Convert `price` to a float.
3. Print the sum of `age` and `price`.

### Exercise 3: Mutable vs Immutable

Predict the output and explain why.

```python
numbers = [1, 2, 3]
other = numbers

other[0] = 99

print(numbers)
print(other)
```

### Exercise 4: Dictionary Validation

Given the following record:

```python
order = {
    "order_id": "1001",
    "amount": "250.50",
    "is_paid": True
}
```

Requirements:

1. Convert `order_id` to an integer.
2. Convert `amount` to a numeric type.
3. Verify that `is_paid` is a Boolean.
4. Explain how you would handle an invalid value.

### Exercise 5: Data Quality Scenario

A pipeline expects the following record:

```python
order = {
    "order_id": "ABC",
    "amount": "unknown",
    "is_paid": "yes"
}
```

Identify the data quality issues and propose a validation policy for each field.

### Exercise 6: Interview Challenge

Explain the difference between these two operations:

```python
numbers = [1, 2, 3]
other = numbers
```

and

```python
numbers = [1, 2, 3]
other = numbers.copy()
```

Include an example showing how modifying `other` affects `numbers` in each case.

---

> **Next Step:** After completing this lecture, practice these concepts using Python exercises, then continue to control flow and data structures. Keep the status as `🟡 In Progress` until the material and practice exercises have been reviewed.