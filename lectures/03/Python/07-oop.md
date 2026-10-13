# Object-Oriented Programming (OOP)

> 📌 **Status:** 🟡 In Progress

## 📖 Overview

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code around objects, which combine data and behavior.

In Python, classes define the structure and behavior of objects. Objects can store information in attributes and provide operations through methods.

OOP helps organize complex applications into reusable, maintainable components.

As a future **Data Engineer**, OOP is useful when building data pipeline components, database clients, data validators, transformation classes, and reusable processing systems.

This section covers classes, objects, attributes, methods, constructors and initializers, special methods, inheritance, encapsulation, polymorphism, and composition.

---

## 🧠 Concepts

### 1. What Is a Class?

A **class** is a blueprint for creating objects. It defines the attributes and methods that its instances can have.

```python
class Employee:
    pass
```

The `class` keyword defines a class. The `pass` statement acts as a placeholder when no implementation is provided yet.

### 2. What Is an Object?

An **object** is an instance of a class.

```python
class Employee:
    pass

employee1 = Employee()
employee2 = Employee()

print(type(employee1))
print(employee1 is employee2)  # False
```

Both objects are instances of `Employee`, but they are distinct objects.

A class defines a type; an object is a particular instance of that type.

### 3. Attributes

Attributes store information associated with an object or class.

There are two common categories.

#### Instance Attributes

Instance attributes belong to individual objects.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee1 = Employee("Amin", 10000)
employee2 = Employee("Ahmed", 12000)

print(employee1.name)    # Amin
print(employee2.name)    # Ahmed
```

Each object has its own `name` and `salary`.

#### Class Attributes

Class attributes are defined on the class and are shared through the class unless an instance shadows the attribute with its own value.

```python
class Employee:
    company = "DataCorp"

    def __init__(self, name):
        self.name = name


employee1 = Employee("Amin")
employee2 = Employee("Ahmed")

print(employee1.company)
print(employee2.company)
```

Both instances access the class attribute `company`.

**Important:** Avoid using a mutable class attribute, such as a list, for data that should be independent for each instance.

### 4. Methods

A **method** is a function defined within a class and accessed through the class or its instances.

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"


employee = Employee("Amin")
print(employee.introduce())
```

The method `introduce()` uses the object's `name` attribute.

#### Function vs Method

A function is defined independently, while a method is associated with a class.

```python
def greet(name):
    return f"Hello, {name}"


class Employee:
    def greet(self):
        return "Hello from Employee"
```

Both are callable pieces of code, but the method is defined as part of a class.

### 5. The `self` Parameter

`self` refers to the current instance when an instance method is called.

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


employee = Employee("Amin")
print(employee.get_name())
```

When calling `employee.get_name()`, Python supplies the instance as the method's first argument.

`self` is a convention, not a reserved keyword, but using it is the standard Python practice.

### 6. `__init__()` and Object Initialization

`__init__()` initializes a newly created object. It is commonly used to set instance attributes.

```python
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department


employee = Employee("Amin", "Data Engineering")
```

When an instance is created, Python calls `__init__()` to initialize it.

**Technical distinction:** `__new__()` is responsible for creating the instance, while `__init__()` initializes the instance after it has been created.

In ordinary application code, you will usually define `__init__()` and rarely need to override `__new__()`.

### 7. Instance Methods, Class Methods, and Static Methods

Python supports different method types.

#### Instance Method

Receives the instance as its first argument, conventionally named `self`.

```python
class Pipeline:
    def __init__(self, name):
        self.name = name

    def run(self):
        return f"Running {self.name}"
```

#### Class Method

Uses `@classmethod` and receives the class as its first argument, conventionally named `cls`.

```python
class Pipeline:
    default_environment = "development"

    @classmethod
    def get_default_environment(cls):
        return cls.default_environment
```

Class methods are often used for operations related to the class itself or alternative constructors.

#### Static Method

Uses `@staticmethod` and does not automatically receive the instance or class as its first argument.

```python
class DataValidator:
    @staticmethod
    def is_positive(value):
        return value > 0
```

Static methods are useful for related utility operations that do not need instance or class state.

### 8. Dunder Methods

**Dunder** means *double underscore*. Dunder methods are special methods with names that begin and end with double underscores, such as `__init__` and `__str__`.

They let objects participate in Python language protocols.

#### `__str__()`

Defines a human-readable string representation.

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Employee: {self.name}"


employee = Employee("Amin")
print(employee)
```

#### `__repr__()`

Defines a representation primarily intended for debugging and development.

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Employee(name={self.name!r})"


employee = Employee("Amin")
print(repr(employee))
```

#### Other Common Dunder Methods

| Method | Purpose |
|---|---|
| `__init__()` | Initializes an instance |
| `__new__()` | Creates an instance |
| `__str__()` | Provides a human-readable representation |
| `__repr__()` | Provides a developer-oriented representation |
| `__len__()` | Supports `len(object)` |
| `__eq__()` | Defines equality behavior |
| `__iter__()` | Supports iteration protocols |
| `__enter__()` | Supports entering a context manager |
| `__exit__()` | Supports exiting a context manager |

Do not define arbitrary dunder names casually. Special methods should follow the behavior expected by Python's corresponding protocols.

### 9. Encapsulation

**Encapsulation** means grouping data and behavior together while defining how internal state should be accessed or modified.

Python does not enforce traditional private access modifiers in the same way as some other languages, but it provides conventions and mechanisms to communicate intent.

#### Public Attributes

Public attributes can be accessed directly.

```python
class Employee:
    def __init__(self, name):
        self.name = name
```

#### Non-Public Attributes by Convention

A single leading underscore indicates that an attribute or method is intended for internal use.

```python
class Employee:
    def __init__(self, name):
        self._name = name
```

The underscore is a convention, not strict access control.

#### Name Mangling

A double leading underscore triggers name mangling, which helps avoid accidental name conflicts in subclasses.

```python
class Employee:
    def __init__(self, salary):
        self.__salary = salary
```

Name mangling is not a security mechanism and does not make the attribute truly inaccessible.

#### Properties

Properties allow controlled attribute access through methods.

```python
class Employee:
    def __init__(self, salary):
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")

        self._salary = value
```

Now, assigning an invalid salary raises a `ValueError`.

### 10. Inheritance

**Inheritance** allows a class to derive behavior and attributes from another class.

```python
class DataSource:
    def connect(self):
        return "Connecting to data source"


class MySQLSource(DataSource):
    def query(self):
        return "Executing MySQL query"


source = MySQLSource()

print(source.connect())
print(source.query())
```

`MySQLSource` inherits the `connect()` method from `DataSource` and defines its own `query()` method.

#### Method Overriding

A subclass can provide its own implementation of an inherited method.

```python
class DataSource:
    def connect(self):
        return "Generic connection"


class MySQLSource(DataSource):
    def connect(self):
        return "Connecting to MySQL"


source = MySQLSource()
print(source.connect())
```

The subclass implementation overrides the inherited method for instances of `MySQLSource`.

#### `super()`

`super()` allows a class to call implementations from its method resolution order, commonly to reuse parent-class initialization or behavior.

```python
class DataSource:
    def __init__(self, name):
        self.name = name


class MySQLSource(DataSource):
    def __init__(self, name, host):
        super().__init__(name)
        self.host = host


source = MySQLSource("Orders DB", "localhost")
print(source.name)
print(source.host)
```

### 11. Polymorphism

**Polymorphism** means that different object types can provide the same operation or interface while implementing it differently.

```python
class CSVExporter:
    def export(self):
        return "Exporting CSV"


class JSONExporter:
    def export(self):
        return "Exporting JSON"


def run_export(exporter):
    print(exporter.export())


run_export(CSVExporter())
run_export(JSONExporter())
```

The `run_export()` function works with both objects because each provides an `export()` method.

Python commonly uses duck typing: an object can be used when it supports the required behavior, without necessarily inheriting from a particular base class.

### 12. Abstraction

**Abstraction** exposes essential behavior while hiding implementation details.

Python's `abc` module supports abstract base classes.

```python
from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def extract(self):
        pass


class CSVSource(DataSource):
    def extract(self):
        return "Reading CSV data"
```

A concrete subclass must implement the abstract methods before it can be instantiated normally.

Abstraction is useful when multiple components must follow a common interface.

### 13. Composition

**Composition** means building a class using instances of other classes rather than relying entirely on inheritance.

```python
class DataValidator:
    def validate(self, records):
        return records


class Pipeline:
    def __init__(self, validator):
        self.validator = validator

    def run(self, records):
        return self.validator.validate(records)


validator = DataValidator()
pipeline = Pipeline(validator)

print(pipeline.run([1, 2, 3]))
```

The `Pipeline` class uses a `DataValidator` object to perform validation.

Composition is often preferable when a class needs to collaborate with another component without being a specialized version of it.

---

## 💻 Syntax & Examples

### Example 1: Create a Data Pipeline Class

```python
class DataPipeline:
    def __init__(self, name):
        self.name = name

    def extract(self):
        return ["100", "200", "300"]

    def transform(self, records):
        return [int(record) for record in records]

    def run(self):
        raw_data = self.extract()
        transformed_data = self.transform(raw_data)

        return transformed_data


pipeline = DataPipeline("Orders Pipeline")

print(pipeline.name)
print(pipeline.run())
```

Output:

```text
Orders Pipeline
[100, 200, 300]
```

This example illustrates how a class can organize related pipeline operations. It is a simplified in-memory example, not a production ETL framework.

### Example 2: Validate Records with a Class

```python
class OrderValidator:
    def is_valid(self, order):
        if "order_id" not in order:
            return False

        amount = order.get("amount")

        if not isinstance(amount, (int, float)):
            return False

        if isinstance(amount, bool):
            return False

        return amount > 0


validator = OrderValidator()

print(validator.is_valid({
    "order_id": 101,
    "amount": 250
}))  # True

print(validator.is_valid({
    "order_id": 102,
    "amount": -10
}))  # False
```

This class encapsulates a simple validation rule. A production validator may return detailed issue objects instead of a Boolean.

### Example 3: Inheritance and Polymorphism

```python
class DataSource:
    def extract(self):
        raise NotImplementedError


class CSVSource(DataSource):
    def extract(self):
        return "Extracting from CSV"


class APISource(DataSource):
    def extract(self):
        return "Extracting from API"


sources = [CSVSource(), APISource()]

for source in sources:
    print(source.extract())
```

Each source implements the same operation differently, allowing the calling code to treat them uniformly.

---

## ⚠️ Common Mistakes

1. **Confusing a class with an object:** A class defines a type; an object is an instance of that type.
2. **Forgetting `self` in instance methods:** Instance methods normally receive the instance as their first parameter.
3. **Confusing `__init__()` with object creation:** `__new__()` creates the instance; `__init__()` initializes it.
4. **Using mutable class attributes for instance-specific data:** A shared list or dictionary can unintentionally be modified by multiple instances.
5. **Assuming a leading underscore enforces privacy:** It is a convention that communicates intended internal use.
6. **Treating name mangling as security:** Double-leading-underscore attributes are not secret or secure.
7. **Overusing inheritance:** Composition may be more appropriate when a class simply needs to use another component.
8. **Writing classes for every small operation:** A standalone function may be simpler when no object state or related behavior needs to be grouped.
9. **Defining arbitrary dunder methods:** Special methods should implement the relevant Python protocol correctly.
10. **Giving classes too many responsibilities:** Separate extraction, validation, transformation, and persistence when doing so improves clarity and testing.

---

## 👨‍💻 Data Engineering Connection

OOP can help organize data engineering systems into reusable components.

### 1. Data Sources

Different sources may expose a common extraction interface.

```python
class CSVSource:
    def extract(self):
        return "Read records from CSV"


class APISource:
    def extract(self):
        return "Fetch records from API"
```

The pipeline can work with different source types through a consistent operation.

### 2. Data Validators

A validator class can encapsulate quality rules, configuration, and validation behavior.

Examples include:

- Required-field validation.
- Type validation.
- Duplicate-key detection.
- Range checks.
- Schema consistency checks.

For larger systems, separate rules into focused components to avoid creating one oversized validator class.

### 3. Pipeline Architecture

A pipeline can compose reusable components:

- Source reader.
- Data validator.
- Transformer.
- Destination writer.
- Quality issue logger.

Each component has a clear responsibility and can be tested independently.

### 4. Connection to Apache Airflow

Airflow uses Python to define workflows and tasks. OOP can organize reusable helpers or service clients called by those tasks.

However, defining a class does not automatically create an Airflow task. Airflow's operators, task definitions, scheduling, and dependencies remain responsible for orchestration.

### 5. Connection to DataPulse

DataPulse can use classes to represent pipeline components and quality checks.

For example:

- `CSVSource` reads input files.
- `OrderValidator` checks record quality.
- `DuplicateDetector` identifies repeated order IDs.
- `DataTransformer` normalizes valid records.
- `QualityIssueRepository` persists issue details.

The system should separate duplicate detection from duplicate resolution. A detector identifies conflicts; a resolution policy determines whether to keep the newest record, merge values, or quarantine conflicting records.

### 6. Testing and Maintainability

Classes and functions should be designed so that their behavior can be tested independently.

A validator should be testable without requiring a live database connection. A transformer should be testable using sample input records. Database access should be isolated where practical.

This reduces coupling and makes pipeline failures easier to diagnose.

---

## 🎯 Interview Questions

### Q1. What is OOP?

OOP is a programming paradigm that organizes code around objects containing data and behavior.

### Q2. What is the difference between a class and an object?

A class defines a type and its behavior. An object is an instance of that class.

### Q3. What is `self` in Python?

`self` is the conventional name for the first parameter of an instance method. It refers to the current instance.

### Q4. What is the difference between `__new__()` and `__init__()`?

`__new__()` creates an instance, while `__init__()` initializes the newly created instance.

### Q5. What are dunder methods?

They are special methods with double underscores at both ends of their names. They implement Python protocols, such as string representation, iteration, and object initialization.

### Q6. What is encapsulation?

Encapsulation groups data and behavior and defines how internal state should be accessed or modified. Python uses conventions, properties, and other techniques rather than strict private access modifiers.

### Q7. What is inheritance?

Inheritance allows a class to derive behavior and attributes from another class and optionally override inherited methods.

### Q8. What is polymorphism?

Polymorphism allows different object types to provide the same operation or interface with different implementations.

### Q9. What is abstraction?

Abstraction exposes essential behavior through a simplified interface while hiding implementation details. Python's abstract base classes can help enforce such interfaces.

### Q10. What is the difference between inheritance and composition?

Inheritance models a specialized type of another class. Composition builds a class using other objects that it delegates work to.

### Q11. When should you use a class instead of a function?

Use a class when related behavior and state need to be grouped into a reusable object. A function is often simpler for an independent operation that does not need persistent instance state.

### Q12. How can OOP help in Data Engineering?

It can organize source readers, validators, transformers, and destination writers into reusable components with clear responsibilities and testable interfaces.

---

## 📝 Practice

### Exercise 1: Create an Employee Class

Create an `Employee` class with:

- `name`
- `department`
- `salary`

Add a method called `introduce()` that returns a message containing the employee's name and department.

### Exercise 2: Implement a Data Validator

Create an `OrderValidator` class that checks whether an order contains a valid `order_id` and a positive numeric amount.

Reject Boolean values as amounts even though `bool` is a subclass of `int`.

### Exercise 3: Implement Inheritance

Create a base class called `DataSource` with an `extract()` method.

Create two subclasses:

- `CSVSource`
- `APISource`

Override `extract()` in each subclass to return a different message.

### Exercise 4: Demonstrate Polymorphism

Create a function called `run_extraction(source)` that calls the source's `extract()` method.

Test it with both `CSVSource` and `APISource` objects.

Explain why the function does not need separate branches for each class.

### Exercise 5: Use a Property

Create a class with an `amount` property that rejects negative values by raising `ValueError`.

Test the class with valid and invalid assignments.

### Exercise 6: Use Composition

Create a `Pipeline` class that receives a validator object through its constructor.

The pipeline should use the validator before transforming records.

Explain why this design may be easier to test than embedding every validation rule directly inside the pipeline class.

### Exercise 7: DataPulse Architecture

Design a small OOP architecture for DataPulse with separate components for:

1. Reading order records.
2. Validating required fields and types.
3. Detecting duplicate order IDs.
4. Resolving duplicates according to an explicit policy.
5. Logging data quality issues.
6. Writing accepted records to a destination.

Define the responsibility of each class and explain how the components communicate.

### Exercise 8: Interview Challenge

A developer creates one class that reads files, validates data, removes duplicates, transforms records, connects to MySQL, writes data, and generates reports.

Explain the maintainability and testing problems this design may create. Propose a design with smaller components and clear interfaces.

---

> **Next Step:** Practice classes, objects, methods, initialization, inheritance, and polymorphism. Keep the status as `🟡 In Progress` until you can implement the examples independently and explain when OOP is useful in a data pipeline.