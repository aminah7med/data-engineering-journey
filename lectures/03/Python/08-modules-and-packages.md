# Modules & Packages

> 📌 **Status:** 🟡 In Progress

## 📖 Overview

**Modules and Packages** help organize Python code into reusable, maintainable components.

A **module** is typically a Python file (`.py`) containing code such as functions, classes, and variables. A **package** is a way to organize related modules under a common namespace, usually using directories.

As a future **Data Engineer**, understanding modules and packages is important for building projects with separate components for data ingestion, validation, transformation, database access, and pipeline orchestration.

This section covers importing modules, creating packages, using aliases, understanding import behavior, and organizing a Python project.

---

## 🧠 Concepts

### 1. What Is a Module?

A module is typically a Python source file that can be imported into another Python file.

For example, create a file named `math_operations.py`:

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

This module contains two reusable functions.

You can import and use them from another Python file.

```python
import math_operations

print(math_operations.add(10, 5))
print(math_operations.subtract(10, 5))
```

Output:

```text
15
5
```

The module name is usually derived from the filename without the `.py` extension.

**Important:** Avoid naming your own files after standard-library modules or installed packages, such as `json.py`, `csv.py`, or `logging.py`, because they can interfere with imports.

### 2. Importing Modules

Python provides several ways to import code.

#### Import the Entire Module

```python
import math

print(math.sqrt(25))
print(math.pi)
```

Using `module_name.member` makes it clear where a function or constant comes from.

#### Import Specific Members

```python
from math import sqrt, pi

print(sqrt(25))
print(pi)
```

This allows you to access the imported members directly.

#### Import with an Alias

```python
import pandas as pd
import numpy as np

print(pd.__name__)
print(np.__name__)
```

Aliases are common conventions for popular libraries.

#### Import a Module with an Alias

```python
import math as m

print(m.sqrt(36))
```

**Best practice:** Prefer explicit imports and avoid unnecessarily importing everything with `from module import *`, because wildcard imports can make it difficult to identify where names originate.

### 3. Built-in Modules vs Third-Party Modules

Python's modules come from different sources.

| Category | Description | Examples |
|---|---|---|
| Standard library | Included with Python | `math`, `json`, `csv`, `os`, `pathlib`, `logging` |
| Third-party packages | Installed separately | `pandas`, `numpy`, `requests`, `pyspark` |
| Project modules | Written as part of your project | `data_validator.py`, `transformations.py` |

The standard library does not usually need a separate package installation.

Third-party packages generally need to be installed into the Python environment used by your project.

### 4. What Is a Package?

A package organizes related Python modules into a directory structure.

Example:

```text
my_project/
├── main.py
└── data_utils/
    ├── __init__.py
    ├── cleaning.py
    └── validation.py
```

Here:

- `data_utils` is the package.
- `cleaning.py` and `validation.py` are modules.
- `__init__.py` can mark the directory as a regular package and may contain package initialization code.

Importing a function from a module:

```python
from data_utils.cleaning import clean_text
from data_utils.validation import validate_record
```

A directory without `__init__.py` can also function as a namespace package in supported circumstances. Therefore, `__init__.py` is common and useful, but it is not mandatory for every package.

### 5. The `__init__.py` File

The `__init__.py` file can initialize a package and define what is exposed through its namespace.

For example:

```text
data_utils/
├── __init__.py
├── cleaning.py
└── validation.py
```

The file `data_utils/__init__.py` might contain:

```python
from .cleaning import clean_text
from .validation import validate_record
```

Consumers can then write:

```python
from data_utils import clean_text, validate_record
```

This is an intentional public interface for the package.

**Important:** Do not place expensive operations, database connections, or pipeline execution directly in `__init__.py`. Importing a package should generally have minimal side effects.

### 6. Absolute and Relative Imports

An **absolute import** specifies a module using its package path.

```python
from data_utils.cleaning import clean_text
```

A **relative import** uses leading dots to refer to the current package hierarchy.

For example, inside `data_utils/validation.py`:

```python
from .cleaning import clean_text
```

One leading dot refers to the current package. Additional dots refer to parent package levels.

Relative imports are useful within packages, while absolute imports can make the source of a dependency clearer.

**Important:** Relative imports generally require the module to be imported as part of a package. Running a package module directly as a standalone script can cause import errors.

### 7. The `if __name__ == "__main__"` Pattern

Every Python module has a `__name__` attribute.

When a module is run as the top-level program, `__name__` is set to `"__main__"`. When it is imported under its module name, `__name__` usually contains that name.

This pattern allows a file to be both imported and executed directly.

```python
def main():
    print("Running the application")


if __name__ == "__main__":
    main()
```

When the file is executed directly, `main()` runs.

When the file is imported, the guarded block does not run.

**Best practice:** Keep application startup logic inside a `main()` function and use this guard when appropriate.

### 8. Importing Is Not the Same as Installing

Importing makes a module's functionality available to your code.

Installing adds a package to a Python environment, usually using a package manager such as `pip`.

For example:

```bash
python -m pip install pandas
```

Then:

```python
import pandas as pd
```

The installation command and the import statement serve different purposes.

A package may already be installed in one environment but unavailable in another.

### 9. How Python Finds Modules

Python searches for modules using its import system, including entries in `sys.path`, built-in modules, and installed import mechanisms.

```python
import sys

for path in sys.path:
    print(path)
```

The exact search behavior depends on the module and the import system, but the current working directory or script-related paths are often important.

If Python cannot locate a module, it may raise:

```text
ModuleNotFoundError
```

Avoid solving import problems by adding arbitrary directories to `sys.path` without understanding the project structure. A proper package layout and installation configuration are usually more maintainable.

### 10. Avoiding Import Side Effects

When a module is imported, its top-level statements execute.

For example, this module has an undesirable side effect:

```python
# bad_module.py

print("Starting a pipeline...")
# A database connection or pipeline execution might occur here.
```

Importing `bad_module` prints the message immediately.

A better approach is to define functions and classes at module level and run the application explicitly.

```python
# pipeline.py

def run_pipeline():
    print("Starting a pipeline...")


if __name__ == "__main__":
    run_pipeline()
```

This makes modules easier to import, test, and reuse.

---

## 💻 Syntax & Examples

### Example 1: Create a Reusable Module

Project structure:

```text
project/
├── main.py
└── calculations.py
```

`calculations.py`:

```python
def calculate_total(amounts):
    return sum(amounts)


def calculate_average(amounts):
    if not amounts:
        return None

    return sum(amounts) / len(amounts)
```

`main.py`:

```python
from calculations import calculate_total, calculate_average

amounts = [100, 200, 300]

print(calculate_total(amounts))
print(calculate_average(amounts))
```

Output:

```text
600
200.0
```

This example separates calculation logic from application code.

### Example 2: Create a Package

Project structure:

```text
project/
├── main.py
└── data_utils/
    ├── __init__.py
    ├── cleaning.py
    └── validation.py
```

`data_utils/cleaning.py`:

```python
def clean_text(value):
    if value is None:
        return None

    return value.strip()
```

`data_utils/validation.py`:

```python
def is_positive_amount(value):
    if isinstance(value, bool):
        return False

    return isinstance(value, (int, float)) and value > 0
```

`main.py`:

```python
from data_utils.cleaning import clean_text
from data_utils.validation import is_positive_amount

print(clean_text("  Data Engineering  "))
print(is_positive_amount(250))
print(is_positive_amount(-10))
```

Output:

```text
Data Engineering
True
False
```

Run the program from the project directory:

```bash
python main.py
```

### Example 3: Create an Application Entry Point

`main.py`:

```python
def main():
    print("DataPulse application started")


if __name__ == "__main__":
    main()
```

This separates the application's entry point from code that may be imported elsewhere.

---

## ⚠️ Common Mistakes

1. **Confusing modules and packages:** A module is typically a Python file; a package organizes modules under a namespace.
2. **Confusing installation and importing:** Installing a package and importing it into Python are different operations.
3. **Naming files after standard-library modules:** A local `json.py` or `logging.py` can interfere with imports.
4. **Using wildcard imports unnecessarily:** `from module import *` can make code harder to understand and maintain.
5. **Running package modules directly when they rely on relative imports:** Prefer running the package entry point or using `python -m package.module` where appropriate.
6. **Executing code during import:** Top-level statements can run unexpectedly when another module imports the file.
7. **Ignoring the active Python environment:** A package installed in one environment may not be available in another.
8. **Creating circular imports:** Two modules that depend on each other can create initialization problems.
9. **Using arbitrary `sys.path` modifications:** This often hides a project-layout or packaging issue.
10. **Putting too much logic in `__init__.py`:** Keep package initialization lightweight and predictable.

---

## 👨‍💻 Data Engineering Connection

Modules and packages help turn a collection of scripts into a maintainable data engineering application.

### 1. Separation of Responsibilities

A data pipeline can be organized into modules such as:

- `extract.py` — retrieves source data.
- `validate.py` — checks schema and data quality.
- `transform.py` — cleans and transforms records.
- `load.py` — writes processed data to a destination.
- `logging_config.py` — configures logging.
- `config.py` — manages application configuration.

This structure makes each responsibility easier to understand and test.

### 2. Connection to DataPulse

A possible DataPulse package structure is:

```text
src/
└── datapulse/
    ├── __init__.py
    ├── ingestion/
    │   ├── __init__.py
    │   └── csv_reader.py
    ├── quality/
    │   ├── __init__.py
    │   ├── validation.py
    │   └── duplicate_detection.py
    ├── transformations/
    │   ├── __init__.py
    │   └── orders.py
    ├── storage/
    │   ├── __init__.py
    │   └── mysql_writer.py
    └── monitoring/
        ├── __init__.py
        └── issue_logger.py
```

This is an example of a possible layout, not a requirement to use exactly these directories.

Each module should have a focused responsibility. For example, `duplicate_detection.py` can identify repeated keys, while a separate component applies the chosen duplicate-resolution policy.

### 3. Testing

Modular code is easier to test independently.

For example:

- Test validation rules without connecting to MySQL.
- Test transformations with sample records.
- Test duplicate detection with controlled input.
- Test database writing separately using a test database or suitable mocks.

This reduces the number of moving parts involved in each test.

### 4. Apache Airflow Integration

Airflow DAG files can import reusable pipeline functions from project modules.

Instead of placing every transformation and database operation directly inside a DAG file, keep business logic in reusable modules and let the DAG define orchestration.

This makes the same business logic easier to test and reuse outside Airflow.

### 5. Dependency Management

Project modules may depend on third-party packages such as Pandas, SQLAlchemy, or PyMySQL.

Use an explicit dependency-management approach so that development, testing, and deployment environments can install compatible dependencies consistently.

Module organization and dependency management are related, but they solve different problems.

---

## 🎯 Interview Questions

### Q1. What is a Python module?

A module is typically a Python file containing reusable code, such as functions, classes, and variables, that can be imported by other code.

### Q2. What is the difference between a module and a package?

A module is typically a single Python file. A package organizes related modules under a common namespace, often using a directory structure.

### Q3. What is the purpose of `__init__.py`?

It can mark a regular package and execute package initialization code. It can also expose selected members as part of the package's public interface.

### Q4. What is the difference between `import module` and `from module import function`?

The first imports the module and accesses members through its namespace. The second imports a specific member directly into the current namespace.

### Q5. What does `if __name__ == "__main__"` do?

It runs a block only when the module is executed as the top-level program, rather than imported under its module name.

### Q6. What is the difference between installing and importing a package?

Installing makes package files available in a Python environment. Importing loads a module or package into the current Python process.

### Q7. What causes `ModuleNotFoundError`?

Python cannot find the requested module through its import system. Common causes include a missing installation, incorrect environment, or incorrect project layout.

### Q8. What is a circular import?

A circular import occurs when modules depend on each other, directly or indirectly. It can cause initialization problems when one module tries to access another before it has finished initializing.

### Q9. Why should a data engineering project use modules?

Modules separate responsibilities, improve reuse, make testing easier, and reduce duplication across ingestion, validation, transformation, and loading code.

### Q10. Why should pipeline logic be kept outside an Airflow DAG file when practical?

Keeping business logic in reusable modules makes it easier to test, maintain, and reuse independently of the orchestration framework.

---

## 📝 Practice

### Exercise 1: Create a Module

Create a file named `calculations.py` with functions to:

1. Calculate a total.
2. Calculate an average.
3. Return `None` when an average cannot be calculated because the input is empty.

Import these functions into `main.py` and test them.

### Exercise 2: Create a Package

Create a package named `data_utils` with:

- `cleaning.py`
- `validation.py`
- `__init__.py`

Implement one cleaning function and one validation function, then import and use them from `main.py`.

### Exercise 3: Use the Main Guard

Create a module containing a `main()` function and an `if __name__ == "__main__"` block.

Run it directly, then import it from another file. Explain which code executes in each case.

### Exercise 4: Diagnose an Import Error

A project contains a local file named `json.py`. Another file attempts to use Python's standard-library `json` module but fails unexpectedly.

Explain the likely cause and propose a fix.

### Exercise 5: Organize a Data Pipeline

Design a package containing separate modules for extraction, validation, transformation, and loading.

Write a simple entry point that calls the modules in the correct order.

### Exercise 6: DataPulse Architecture

Propose a module structure for DataPulse that supports:

1. Reading incoming order data.
2. Validating required fields and types.
3. Detecting duplicate IDs.
4. Resolving duplicates according to an explicit policy.
5. Logging quality issues.
6. Writing accepted records to MySQL.

Explain why each responsibility belongs in its chosen module.

### Exercise 7: Interview Challenge

A single Python file contains API requests, data cleaning, database queries, validation logic, and reporting.

Explain the problems this design may create and describe how you would split the application into modules and packages.

---

> **Next Step:** Practice importing functions, creating modules and packages, and using the main guard. Keep the status as `🟡 In Progress` until you can organize a small Python project independently.