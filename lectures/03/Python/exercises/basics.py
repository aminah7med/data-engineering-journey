
"""
Python Fundamentals — Data Engineering Practice
================================================

Topics:
1. Variables and basic syntax
2. Built-in data types
3. Operators
4. Input and output
5. Conditions and loops
6. Functions and scope
7. Lambda functions
8. Error handling
9. File handling
10. CSV and JSON
11. Modules and imports
12. Object-oriented programming
13. Iterators and generators
14. Useful built-in functions
15. Data Engineering mini exercises

Run:
    python basics.py
"""

from pathlib import Path
import csv
import json
import logging
import math
import statistics
from datetime import datetime


# ============================================================
# 1. VARIABLES AND BASIC SYNTAX
# ============================================================

def variables_demo():
    print("\n=== VARIABLES ===")

    name = "Amin"
    age = 21
    height = 1.75
    is_learning_python = True

    print("Name:", name)
    print("Age:", age)
    print("Height:", height)
    print("Learning Python:", is_learning_python)

    # Python is dynamically typed.
    value = 100
    print(value, type(value))

    value = "Python"
    print(value, type(value))

    # Multiple assignment.
    x, y, z = 10, 20, 30
    print("Coordinates:", x, y, z)

    # Swap two variables.
    x, y = y, x
    print("After swapping:", x, y)

    # Constants are conventions, not enforced by Python.
    MAX_RETRIES = 3
    print("Max retries:", MAX_RETRIES)

    # Check the type of an object.
    print("Type of age:", type(age))
    print("Is age an integer?", isinstance(age, int))


# ============================================================
# 2. BUILT-IN DATA TYPES
# ============================================================

def data_types_demo():
    print("\n=== DATA TYPES ===")

    integer_value = 42
    float_value = 12.5
    complex_value = 2 + 3j
    boolean_value = True
    string_value = "Data Engineering"
    list_value = [1, 2, 3]
    tuple_value = (1, 2, 3)
    set_value = {1, 2, 3}
    dict_value = {"name": "Amin", "role": "Data Engineer"}
    none_value = None

    values = [
        integer_value,
        float_value,
        complex_value,
        boolean_value,
        string_value,
        list_value,
        tuple_value,
        set_value,
        dict_value,
        none_value,
    ]

    for value in values:
        print(value, "->", type(value).__name__)

    # Type conversion.
    print(int("100"))
    print(float("10.5"))
    print(str(500))
    print(bool(1))

    # int() truncates toward zero; it does not round.
    print(int(3.9))    # 3
    print(int(-3.9))   # -3

    # Common truthy and falsy values.
    print(bool(0))       # False
    print(bool(""))      # False
    print(bool([]))      # False
    print(bool(None))    # False
    print(bool("False")) # True: non-empty string

    # None checks.
    result = None

    if result is None:
        print("No result available")


# ============================================================
# 3. OPERATORS
# ============================================================

def operators_demo():
    print("\n=== OPERATORS ===")

    a = 17
    b = 5

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Floor division:", a // b)
    print("Remainder:", a % b)
    print("Power:", a ** b)

    # Comparison operators.
    print(a > b)
    print(a == b)
    print(a != b)

    # Logical operators.
    age = 21
    has_id = True

    print(age >= 18 and has_id)
    print(age < 18 or has_id)
    print(not has_id)

    # Membership.
    language = "Python"
    print("Py" in language)

    # Identity vs equality.
    first = [1, 2, 3]
    second = [1, 2, 3]

    print(first == second)  # True
    print(first is second)  # False

    # Augmented assignment.
    total = 10
    total += 5
    total *= 2
    print("Total:", total)


# ============================================================
# 4. STRINGS
# ============================================================

def strings_demo():
    print("\n=== STRINGS ===")

    text = "  Data Engineering with Python  "

    print(text.strip())
    print(text.lower())
    print(text.upper())
    print(text.title())
    print(text.replace("Python", "SQL"))
    print(text.strip().startswith("Data"))
    print(text.strip().endswith("Python"))

    # String indexing.
    language = "Python"

    print(language[0])
    print(language[-1])
    print(language[0:3])
    print(language[::-1])

    # f-strings.
    name = "Amin"
    score = 95.567

    print(f"Student: {name}")
    print(f"Score: {score:.2f}")

    # Splitting and joining.
    csv_line = "101,Amin,450.75"
    fields = csv_line.split(",")

    print(fields)
    print(" | ".join(fields))

    # Strings are immutable.
    # language[0] = "J"  # TypeError


# ============================================================
# 5. INPUT AND OUTPUT
# ============================================================

def input_output_demo():
    print("\n=== INPUT AND OUTPUT ===")

    # input() returns a string.
    # Uncomment to experiment interactively:
    #
    # user_name = input("Enter your name: ")
    # user_age = int(input("Enter your age: "))
    # print(f"{user_name} is {user_age} years old.")

    amount = 450.75
    print(f"Amount: {amount:.2f}")

    # Avoid converting untrusted input without validation.
    raw_value = "123"

    try:
        number = int(raw_value)
        print("Converted number:", number)
    except ValueError:
        print("Invalid integer")


# ============================================================
# 6. CONDITIONS
# ============================================================

def conditions_demo():
    print("\n=== CONDITIONS ===")

    score = 85

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "Needs Improvement"

    print("Grade:", grade)

    amount = 500
    status = "completed"

    if amount > 0 and status == "completed":
        print("Valid completed transaction")

    # Conditional expression.
    label = "High Value" if amount >= 400 else "Regular Value"
    print(label)

    # Avoid overly complicated nested conditions.
    order = {
        "order_id": 101,
        "amount": 450,
        "status": "completed",
    }

    if order["status"] == "completed":
        if order["amount"] > 0:
            print("Order is eligible for processing")


# ============================================================
# 7. LOOPS
# ============================================================

def loops_demo():
    print("\n=== LOOPS ===")

    for number in range(1, 6):
        print(number)

    print("Even numbers:")
    for number in range(0, 11, 2):
        print(number)

    orders = [100, 250, 400]

    for index, amount in enumerate(orders, start=1):
        print(f"Order {index}: {amount}")

    # While loop.
    counter = 1

    while counter < 4:
        print("Counter:", counter)
        counter += 1

    # Break.
    for number in range(10):
        if number == 5:
            break
        print(number)

    # Continue.
    for number in range(5):
        if number == 2:
            continue
        print(number)

    # Loop else runs if the loop finishes without break.
    target = 7

    for number in [1, 3, 5]:
        if number == target:
            print("Found")
            break
    else:
        print("Target not found")

    # Avoid modifying a list while iterating over it.
    values = [1, 2, 3, 4, 5]
    even_values = [value for value in values if value % 2 == 0]

    print("Even values:", even_values)


# ============================================================
# 8. FUNCTIONS
# ============================================================

def calculate_total(prices):
    """Return the sum of a collection of prices."""
    return sum(prices)


def calculate_average(values):
    """Return the average, or None for an empty collection."""
    if not values:
        return None

    return sum(values) / len(values)


def normalize_text(value):
    """Strip whitespace and convert text to lowercase."""
    if not isinstance(value, str):
        raise TypeError("value must be a string")

    return value.strip().lower()


def calculate_discount(amount, discount_rate=0.10):
    """Return the discounted amount."""
    if amount < 0:
        raise ValueError("amount cannot be negative")

    if not 0 <= discount_rate <= 1:
        raise ValueError("discount_rate must be between 0 and 1")

    return amount * (1 - discount_rate)


def describe_person(name, age, **details):
    """Demonstrate keyword arguments."""
    return {
        "name": name,
        "age": age,
        "details": details,
    }


def functions_demo():
    print("\n=== FUNCTIONS ===")

    prices = [100, 200, 300]

    print("Total:", calculate_total(prices))
    print("Average:", calculate_average(prices))
    print("Empty average:", calculate_average([]))
    print("Normalized:", normalize_text("  COMPLETED "))
    print("Discounted:", calculate_discount(500, 0.20))

    person = describe_person(
        "Amin",
        21,
        role="Data Engineer",
        country="Egypt",
    )

    print(person)

    # Positional and keyword arguments.
    print(calculate_discount(amount=500, discount_rate=0.15))

    # Lambda function.
    square = lambda number: number ** 2
    print("Square:", square(5))

    # Higher-order functions.
    numbers = [1, 2, 3, 4, 5]

    print(list(map(lambda number: number * 2, numbers)))
    print(list(filter(lambda number: number > 2, numbers)))

    # Scope example.
    local_value = 10

    def inner_function():
        local_value = 20
        return local_value

    print("Outer:", local_value)
    print("Inner:", inner_function())


# ============================================================
# 9. COMPREHENSIONS
# ============================================================

def comprehensions_demo():
    print("\n=== COMPREHENSIONS ===")

    numbers = [1, 2, 3, 4, 5, 6]

    squares = [number ** 2 for number in numbers]
    evens = [number for number in numbers if number % 2 == 0]
    square_map = {number: number ** 2 for number in numbers}
    unique_remainders = {number % 3 for number in numbers}

    print("Squares:", squares)
    print("Evens:", evens)
    print("Square map:", square_map)
    print("Remainders:", unique_remainders)

    # Nested comprehension.
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6],
    ]

    flattened = [
        value
        for row in matrix
        for value in row
    ]

    print("Flattened:", flattened)


# ============================================================
# 10. USEFUL BUILT-IN FUNCTIONS
# ============================================================

def builtins_demo():
    print("\n=== BUILT-IN FUNCTIONS ===")

    values = [12, 5, 18, 7, 10]

    print("Length:", len(values))
    print("Minimum:", min(values))
    print("Maximum:", max(values))
    print("Sum:", sum(values))
    print("Sorted:", sorted(values))
    print("Reversed:", list(reversed(values)))
    print("Any:", any(value > 15 for value in values))
    print("All:", all(value > 0 for value in values))

    # zip combines corresponding values.
    names = ["Amin", "Khaled", "Ahmed"]
    scores = [90, 85, 88]

    for name, score in zip(names, scores):
        print(name, score)

    # enumerate provides index and value.
    for index, value in enumerate(values):
        print(index, value)

    # Sorting using a key.
    orders = [
        {"id": 101, "amount": 300},
        {"id": 102, "amount": 100},
        {"id": 103, "amount": 500},
    ]

    sorted_orders = sorted(
        orders,
        key=lambda order: order["amount"],
        reverse=True,
    )

    print("Sorted orders:", sorted_orders)


# ============================================================
# 11. EXCEPTIONS
# ============================================================

def safe_divide(a, b):
    """Divide two numbers and handle division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("Cannot divide by zero")
        return None


def exceptions_demo():
    print("\n=== EXCEPTIONS ===")

    print(safe_divide(10, 2))
    print(safe_divide(10, 0))

    raw_values = ["10", "20", "invalid", "40"]

    converted_values = []

    for raw_value in raw_values:
        try:
            converted_values.append(int(raw_value))
        except ValueError:
            logging.warning("Invalid integer encountered")

    print("Converted values:", converted_values)

    # try / except / else / finally.
    try:
        result = int("123")
    except ValueError:
        print("Conversion failed")
    else:
        print("Conversion succeeded:", result)
    finally:
        print("Conversion attempt finished")


# ============================================================
# 12. FILE HANDLING
# ============================================================

def file_handling_demo():
    print("\n=== FILE HANDLING ===")

    output_directory = Path("practice_output")
    output_directory.mkdir(exist_ok=True)

    text_file = output_directory / "example.txt"

    # Write.
    with text_file.open("w", encoding="utf-8") as file:
        file.write("Python for Data Engineering\n")
        file.write("File handling practice\n")

    # Read.
    with text_file.open("r", encoding="utf-8") as file:
        content = file.read()

    print(content)

    # Append.
    with text_file.open("a", encoding="utf-8") as file:
        file.write("Appended line\n")

    print("File exists:", text_file.exists())
    print("File size:", text_file.stat().st_size)


# ============================================================
# 13. CSV HANDLING
# ============================================================

def csv_demo():
    print("\n=== CSV HANDLING ===")

    output_directory = Path("practice_output")
    output_directory.mkdir(exist_ok=True)

    csv_path = output_directory / "orders.csv"

    orders = [
        {"order_id": 101, "amount": 450.75, "status": "completed"},
        {"order_id": 102, "amount": 200.00, "status": "pending"},
        {"order_id": 103, "amount": 700.50, "status": "completed"},
    ]

    fieldnames = ["order_id", "amount", "status"]

    with csv_path.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(orders)

    loaded_orders = []

    with csv_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["order_id"] = int(row["order_id"])
            row["amount"] = float(row["amount"])
            loaded_orders.append(row)

    print("Loaded orders:", loaded_orders)


# ============================================================
# 14. JSON HANDLING
# ============================================================

def json_demo():
    print("\n=== JSON HANDLING ===")

    output_directory = Path("practice_output")
    output_directory.mkdir(exist_ok=True)

    json_path = output_directory / "config.json"

    config = {
        "pipeline_name": "orders_pipeline",
        "source": "csv",
        "enabled": True,
        "retry_count": 3,
        "tags": ["python", "data-engineering"],
    }

    with json_path.open("w", encoding="utf-8") as file:
        json.dump(config, file, indent=2)

    with json_path.open("r", encoding="utf-8") as file:
        loaded_config = json.load(file)

    print(loaded_config)
    print("Pipeline:", loaded_config["pipeline_name"])


# ============================================================
# 15. DATE AND TIME
# ============================================================

def datetime_demo():
    print("\n=== DATE AND TIME ===")

    now = datetime.now()

    print("Current date and time:", now)
    print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))

    raw_date = "2026-10-13"

    parsed_date = datetime.strptime(raw_date, "%Y-%m-%d")

    print("Parsed date:", parsed_date)
    print("Year:", parsed_date.year)
    print("Month:", parsed_date.month)

    # In production pipelines, be explicit about time zones.
    # datetime.now() uses the system's local time.


# ============================================================
# 16. LOGGING
# ============================================================

def logging_demo():
    print("\n=== LOGGING ===")

    logger = logging.getLogger("python_practice")
    logger.setLevel(logging.INFO)

    logger.info("Pipeline started")
    logger.warning("Example warning")
    logger.error("Example error")

    # Avoid logging credentials or sensitive record contents.


# ============================================================
# 17. ITERATORS AND GENERATORS
# ============================================================

def generate_numbers(limit):
    """Yield numbers one at a time."""
    for number in range(limit):
        yield number


def iterators_generators_demo():
    print("\n=== ITERATORS AND GENERATORS ===")

    values = [10, 20, 30]
    iterator = iter(values)

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

    # Calling next(iterator) again raises StopIteration.

    for number in generate_numbers(5):
        print(number)

    # Generator expressions can avoid building an entire list.
    squares = (number ** 2 for number in range(5))

    print("Generator values:", list(squares))


# ============================================================
# 18. OBJECT-ORIENTED PROGRAMMING
# ============================================================

class Order:
    """Represent a simple customer order."""

    def __init__(self, order_id, amount, status="pending"):
        if amount < 0:
            raise ValueError("amount cannot be negative")

        self.order_id = order_id
        self.amount = amount
        self.status = status

    def complete(self):
        self.status = "completed"

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "amount": self.amount,
            "status": self.status,
        }

    def __repr__(self):
        return (
            f"Order(order_id={self.order_id}, "
            f"amount={self.amount}, status={self.status!r})"
        )


def oop_demo():
    print("\n=== OOP ===")

    order = Order(101, 450.75)

    print(order)

    order.complete()

    print(order.to_dict())


# ============================================================
# 19. SIMPLE DATA QUALITY CHECKS
# ============================================================

def validate_order(order):
    """
    Validate a basic order record.

    Returns:
        tuple[bool, str]:
            Validation result and reason.
    """

    required_fields = ["order_id", "amount", "status"]

    for field in required_fields:
        if field not in order or order[field] is None:
            return False, f"Missing required field: {field}"

    if not isinstance(order["order_id"], int):
        return False, "order_id must be an integer"

    if (
        isinstance(order["amount"], bool)
        or not isinstance(order["amount"], (int, float))
    ):
        return False, "amount must be numeric"

    if not math.isfinite(order["amount"]):
        return False, "amount must be finite"

    if order["amount"] < 0:
        return False, "amount cannot be negative"

    if not isinstance(order["status"], str):
        return False, "status must be a string"

    if not order["status"].strip():
        return False, "status cannot be blank"

    return True, "Valid"


def data_quality_demo():
    print("\n=== DATA QUALITY ===")

    orders = [
        {"order_id": 101, "amount": 450.75, "status": "completed"},
        {"order_id": 102, "amount": -20, "status": "pending"},
        {"order_id": 103, "amount": 200, "status": "completed"},
        {"order_id": 104, "amount": None, "status": "pending"},
    ]

    valid_orders = []
    invalid_orders = []

    for order in orders:
        is_valid, reason = validate_order(order)

        if is_valid:
            valid_orders.append(order)
        else:
            invalid_orders.append({
                "record": order,
                "reason": reason,
            })

    print("Valid records:", len(valid_orders))
    print("Invalid records:", len(invalid_orders))
    print("Invalid details:", invalid_orders)


# ============================================================
# 20. STATISTICS
# ============================================================

def statistics_demo():
    print("\n=== STATISTICS ===")

    values = [100, 200, 300, 400, 500]

    print("Mean:", statistics.mean(values))
    print("Median:", statistics.median(values))
    print("Minimum:", min(values))
    print("Maximum:", max(values))
    print("Total:", sum(values))


# ============================================================
# 21. MINI EXERCISES
# ============================================================

def exercise_1_sum_even_numbers(numbers):
    """Return the sum of even numbers."""
    return sum(number for number in numbers if number % 2 == 0)


def exercise_2_count_statuses(records):
    """Count records by status."""
    counts = {}

    for record in records:
        status = record.get("status", "unknown")
        counts[status] = counts.get(status, 0) + 1

    return counts


def exercise_3_find_max_order(orders):
    """Return the order with the highest amount, or None."""
    if not orders:
        return None

    return max(orders, key=lambda order: order["amount"])


def exercise_4_safe_integer(value):
    """Convert a value to an integer, returning None if invalid."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def exercise_5_remove_duplicate_ids(records):
    """
    Keep the first record for each order_id.

    This is a demonstration policy, not a universal
    deduplication strategy.
    """
    seen_ids = set()
    unique_records = []

    for record in records:
        order_id = record.get("order_id")

        if order_id not in seen_ids:
            seen_ids.add(order_id)
            unique_records.append(record)

    return unique_records


def practice_demo():
    print("\n=== MINI EXERCISES ===")

    print(exercise_1_sum_even_numbers([1, 2, 3, 4, 5, 6]))

    sample_orders = [
        {"order_id": 101, "amount": 100, "status": "completed"},
        {"order_id": 102, "amount": 200, "status": "pending"},
        {"order_id": 103, "amount": 300, "status": "completed"},
    ]

    print(exercise_2_count_statuses(sample_orders))
    print(exercise_3_find_max_order(sample_orders))
    print(exercise_4_safe_integer("123"))
    print(exercise_4_safe_integer("invalid"))
    print(exercise_5_remove_duplicate_ids(sample_orders))


# ============================================================
# 22. RUN ALL DEMONSTRATIONS
# ============================================================

def main():
    logging.basicConfig(
        level=logging.WARNING,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    demos = [
        variables_demo,
        data_types_demo,
        operators_demo,
        strings_demo,
        input_output_demo,
        conditions_demo,
        loops_demo,
        functions_demo,
        comprehensions_demo,
        builtins_demo,
        exceptions_demo,
        file_handling_demo,
        csv_demo,
        json_demo,
        datetime_demo,
        logging_demo,
        iterators_generators_demo,
        oop_demo,
        data_quality_demo,
        statistics_demo,
        practice_demo,
    ]

    for demo in demos:
        try:
            demo()
        except Exception as error:
            print(f"Demo {demo.__name__} failed: {error}")


if __name__ == "__main__":
    main()


# ============================================================
# CHALLENGES — SOLVE THESE WITHOUT LOOKING AT THE ANSWERS
# ============================================================
#
# 1. Write a function that returns the second-largest unique number.
#
# 2. Write a function that counts how many records have a
#    missing required field.
#
# 3. Read a CSV file and calculate total revenue.
#
# 4. Read JSON records and separate valid and invalid records.
#
# 5. Create an Order class with a method that applies a discount.
#
# 6. Write a function that retries a simulated operation a
#    maximum number of times. Do not retry permanent errors.
#
# 7. Create a generator that yields records in batches.
#
# 8. Write a function that calculates average order value and
#    handles an empty dataset.
#
# 9. Explain the time complexity of each solution.
#
# 10. Write unit tests for your validation functions.
#
# IMPORTANT:
# The examples above are for learning. Production pipelines need
# explicit error policies, tests, resource management, and
# appropriate logging.