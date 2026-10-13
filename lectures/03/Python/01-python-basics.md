# Python Basics

> 📌 **Status: 🟡 In Progress**

## 📖 Overview

Python is a high-level, general-purpose programming language known for its readable syntax and large ecosystem of libraries.

It is widely used in automation, data analysis, backend development, machine learning, and data engineering.

This lecture covers programming language levels, compiler vs interpreter, Python syntax, indentation, and the main characteristics of Python.

## 🧠 Concepts

### 1. Programming Language Levels

Programming languages can be classified by how closely they communicate with computer hardware.

- **Low-level languages:** Close to hardware and machine instructions. They provide more direct control over system resources. Machine code and assembly language are examples.
- **High-level languages:** Designed to be easier for humans to read and write. Python and C++ are examples, although they differ in abstraction and execution models.

**Important notes:**
- High-level languages generally hide many hardware details.
- Low-level languages generally provide more direct hardware control.
- These classifications are broad; the distinction is not always absolute.
- SQL is a declarative query language. It describes the data result we want rather than specifying every step to produce it. It is sometimes described as very high-level, but that classification is not universal.

### 2. Compiler vs Interpreter

A **compiler** translates source code into another representation, often machine code, before the resulting program executes.

An **interpreter** executes program instructions through a runtime environment.

| Aspect | Compiled approach | Interpreted approach |
|---|---|---|
| Translation | Often happens before execution | Instructions may be processed during execution |
| Execution | Can run as native machine code | Depends on the interpreter or runtime |
| Performance | Often fast for CPU-intensive tasks | Depends on the implementation and workload |
| Example | C++ compiled to native machine code | Python executed by the CPython runtime |

**Important:** The distinction is not simply that a compiler translates the entire program while an interpreter executes it line by line.

In the standard CPython implementation, Python source code is compiled into bytecode, which is then executed by the Python virtual machine.

C++ is commonly compiled into native machine code. Its performance advantages depend on the workload, implementation, and compiler optimizations.

### 3. Python Is Dynamically Typed

Python is dynamically typed. You do not need to declare a variable's type before assigning a value.

```python
x = 10
print(type(x))  # <class 'int'>

x = "Python"
print(type(x))  # <class 'str'>
```

The name `x` first refers to an integer object and then refers to a string object.

**Key idea:** Types belong to objects, while variable names refer to objects.

Python is also strongly typed: it does not automatically allow every operation between incompatible types.

```python
age = 21
name = "Amin"

# print(age + name)  # TypeError
```

### 4. Python Indentation

Indentation defines code blocks in Python. Other languages, such as C++, commonly use curly braces `{}` to define blocks.

```python
age = 21

if age >= 18:
    print("Adult")
    print("Eligible by age")
```

Both `print()` statements belong to the `if` block because they have the same indentation level.

Incorrect indentation can cause an `IndentationError` or change the program's logic.

**Best practice:** Use four spaces per indentation level and remain consistent.

### 5. Colons and Semicolons

A colon `:` introduces a block after compound statements such as `if`, `for`, `while`, `def`, and `class`.

```python
if True:
    print("Hello")
```

A semicolon `;` is not required at the end of a Python statement.

```python
x = 10
y = 20
print(x + y)
```

Python allows semicolons to separate statements on the same line, but this is generally discouraged because it reduces readability.

### 6. Python's Main Characteristics

- **Readable syntax:** Python code is designed to be relatively easy to understand.
- **Dynamically typed:** Names do not require explicit type declarations.
- **General-purpose:** Python supports many different types of applications.
- **Large ecosystem:** Libraries and frameworks support data processing, automation, and more.
- **Cross-platform:** Python is available on major operating systems.
- **Interpreted execution model:** In common implementations such as CPython, bytecode is executed by a virtual machine.

## 💻 Syntax & Examples

### Example 1: Variables and Types

```python
name = "Amin"
age = 21
gpa = 2.8
is_student = True

print(name)
print(type(age))
print(type(gpa))
print(type(is_student))
```

### Example 2: Indentation and Conditions

```python
temperature = 30

if temperature > 25:
    print("The weather is hot")
    print("Consider drinking water")
else:
    print("The weather is moderate")
```

### Example 3: Python Statements

```python
first_number = 10
second_number = 5

result = first_number + second_number
print(result)
```

Each statement is written on a separate line without a trailing semicolon.

## ⚠️ Common Mistakes

1. **Confusing dynamic typing with no types:** Python objects still have types; explicit variable type declarations are simply not required in ordinary assignments.
2. **Assuming a variable permanently belongs to one type:** A name can be rebound to an object of a different type.
3. **Using inconsistent indentation:** This may cause errors or change the structure of a program.
4. **Forgetting the colon:** Compound statements such as `if`, `for`, and `def` require a colon before their indented block.
5. **Adding unnecessary semicolons:** They are not needed at the end of ordinary Python statements.
6. **Assuming Python is never compiled:** CPython compiles source code to bytecode before executing it.
7. **Assuming C++ is always faster:** Performance depends on the workload and implementation. Python libraries may use optimized native code for computationally intensive operations.

## 👨‍💻 Data Engineering Connection

Python is a core tool in data engineering because it can connect systems, process data, automate workflows, and coordinate pipeline tasks.

### 1. Data Ingestion

Python can read data from files, APIs, and databases.

```python
import csv

with open("orders.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

This example reads CSV records as dictionaries. In production pipelines, large files may require streaming, batching, or distributed processing rather than loading everything into memory.

### 2. Data Transformation

Python can transform raw records before loading them into a destination.

```python
order = {
    "order_id": 101,
    "amount": 250
}

order["amount"] = float(order["amount"])

print(order)
```

This is a small example of type normalization during data processing.

### 3. Pipeline Orchestration

Tools such as Apache Airflow use Python to define workflows and tasks. Python can coordinate operations such as extracting data, validating records, transforming datasets, and loading results.

### 4. Performance Considerations

Python is convenient for pipeline logic, but ordinary Python loops may be inefficient for large CPU-intensive workloads.

Depending on the problem, data engineers may use:
- Pandas or NumPy for optimized data operations.
- PySpark for distributed data processing.
- SQL engines for database-side transformations.
- Native libraries when performance-critical operations require them.

**Key takeaway:** Choosing the right execution engine and processing strategy matters more than assuming one programming language is always faster.

## 🎯 Interview Questions

### Q1. What is Python?

Python is a high-level, general-purpose programming language with readable syntax and a large ecosystem. It is widely used in automation, data analysis, and data engineering.

### Q2. What is the difference between a compiler and an interpreter?

A compiler translates source code into another representation before execution, while an interpreter executes instructions through a runtime. Real implementations can combine both approaches.

### Q3. Is Python compiled or interpreted?

In CPython, Python source code is compiled into bytecode, which is executed by the Python virtual machine. Therefore, describing Python as purely interpreted is an oversimplification.

### Q4. What does dynamically typed mean?

It means variable names do not require explicit type declarations, and a name can refer to objects of different types at different times.

### Q5. Why is indentation important in Python?

Indentation defines code blocks and determines which statements belong to constructs such as conditions, loops, and functions.

### Q6. Why is Python commonly used in data engineering?

Python provides libraries and integrations for data ingestion, transformation, validation, automation, APIs, databases, and workflow orchestration.

### Q7. Is Python always slower than C++?

No absolute rule applies to every workload. C++ often performs better in CPU-intensive native execution, but Python applications can rely on optimized native libraries and distributed processing frameworks.

## 📝 Practice

### Exercise 1: Identify the Types

Predict the output before running the code.

```python
x = 100
print(type(x))

x = "100"
print(type(x))

x = 100.0
print(type(x))
```

### Exercise 2: Fix the Indentation

Identify and fix the syntax error.

```python
age = 20

if age >= 18:
print("Adult")
```

### Exercise 3: Understand Dynamic Typing

What will happen when this code runs? Explain why.

```python
value = 10
value = "Data Engineering"

print(value)
print(type(value))
```

### Exercise 4: Data Engineering Scenario

A pipeline receives an order amount as the string `"250.50"`.

1. What is the type of the original value?
2. Why might a data pipeline need to convert it to a numeric type?
3. Write Python code to convert it to `float` and print the result.

### Exercise 5: Interview Practice

Answer these questions in your own words without looking at the notes:

1. Why is Python considered a high-level language?
2. How does CPython execute Python code?
3. What role does indentation play in Python?
4. Why is Python useful in data engineering?
5. When might you choose SQL or PySpark instead of ordinary Python loops?
