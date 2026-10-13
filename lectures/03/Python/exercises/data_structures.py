```python
"""
Python Data Structures — Data Engineering Practice
===================================================

Topics:
1. Lists
2. Tuples
3. Sets
4. Dictionaries
5. Indexing and slicing
6. Mutability and references
7. Shallow and deep copies
8. Comprehensions
9. Sorting and searching
10. Stacks and queues
11. Frequency counting
12. Grouping records
13. Deduplication
14. Data transformation patterns
15. Time complexity
16. Data Engineering exercises

Run:
    python data_structures.py
"""

from collections import Counter, defaultdict, deque
from copy import copy, deepcopy
from heapq import nlargest
from itertools import islice
from time import perf_counter


# ============================================================
# 1. LISTS
# ============================================================

def lists_demo():
    print("\n=== LISTS ===")

    numbers = [10, 20, 30, 40, 50]

    print("Original:", numbers)
    print("First:", numbers[0])
    print("Last:", numbers[-1])
    print("Slice:", numbers[1:4])
    print("Every second element:", numbers[::2])
    print("Reversed:", numbers[::-1])

    # Add elements.
    numbers.append(60)
    numbers.extend([70, 80])
    numbers.insert(0, 5)

    print("After additions:", numbers)

    # Remove elements.
    numbers.remove(30)
    removed_value = numbers.pop()

    print("After remove:", numbers)
    print("Popped:", removed_value)

    # Search.
    print("Contains 40:", 40 in numbers)
    print("Index of 40:", numbers.index(40))
    print("Count of 20:", numbers.count(20))

    # Sort in place.
    values = [5, 2, 8, 1, 3]
    values.sort()

    print("Sorted in place:", values)

    # sorted() returns a new list.
    values = [5, 2, 8, 1, 3]
    sorted_values = sorted(values)

    print("Original:", values)
    print("Sorted copy:", sorted_values)

    # List comprehensions.
    squares = [number ** 2 for number in range(1, 6)]
    evens = [number for number in range(1, 11) if number % 2 == 0]

    print("Squares:", squares)
    print("Evens:", evens)


# ============================================================
# 2. TUPLES
# ============================================================

def tuples_demo():
    print("\n=== TUPLES ===")

    coordinates = (10, 20)
    database_config = ("localhost", 3306, "analytics")

    print(coordinates[0])
    print(database_config)

    # Unpacking.
    host, port, database_name = database_config

    print("Host:", host)
    print("Port:", port)
    print("Database:", database_name)

    # A tuple with one element requires a trailing comma.
    single_value = (10,)
    print(single_value, type(single_value))

    # Tuple structure is immutable.
    # coordinates[0] = 99  # TypeError

    # A tuple can contain mutable objects.
    nested = ([1, 2], [3, 4])
    nested[0].append(99)

    print("Tuple containing mutable lists:", nested)

    # Named fields can make records more readable.
    from collections import namedtuple

    Point = namedtuple("Point", ["x", "y"])
    point = Point(10, 20)

    print(point.x, point.y)


# ============================================================
# 3. SETS
# ============================================================

def sets_demo():
    print("\n=== SETS ===")

    values = [1, 2, 2, 3, 3, 3, 4]
    unique_values = set(values)

    print("Original:", values)
    print("Unique:", unique_values)

    # Membership.
    print(3 in unique_values)

    # Set operations.
    first = {1, 2, 3, 4}
    second = {3, 4, 5, 6}

    print("Union:", first | second)
    print("Intersection:", first & second)
    print("Difference:", first - second)
    print("Symmetric difference:", first ^ second)

    # Add and remove.
    first.add(10)
    first.discard(2)

    print("Updated set:", first)

    # discard() does not raise KeyError if the item is missing.
    first.discard(999)

    # Set elements must be hashable.
    # {[1, 2], [3, 4]}  # TypeError: lists are unhashable

    # Set iteration order is not guaranteed.
    # Sort explicitly if a predictable order is required.
    print("Sorted unique values:", sorted(unique_values))


# ============================================================
# 4. DICTIONARIES
# ============================================================

def dictionaries_demo():
    print("\n=== DICTIONARIES ===")

    employee = {
        "id": 101,
        "name": "Amin",
        "department": "Data Engineering",
        "salary": 15000,
    }

    print(employee["name"])
    print(employee.get("department"))
    print(employee.get("missing_key", "Not Found"))

    # Insert or update.
    employee["city"] = "Arish"
    employee["salary"] = 16000

    # Delete.
    removed_city = employee.pop("city")

    print("Removed city:", removed_city)

    # Iterate through keys and values.
    for key, value in employee.items():
        print(key, ":", value)

    # Merge dictionaries.
    first = {"a": 1, "b": 2}
    second = {"b": 99, "c": 3}

    merged = first | second

    print("Merged:", merged)
    # In a dictionary union, the right-hand value wins for duplicate keys.

    # Dictionary comprehension.
    squares = {
        number: number ** 2
        for number in range(1, 6)
    }

    print(squares)

    # Dictionary keys must be hashable.
    # A list cannot be used as a dictionary key.


# ============================================================
# 5. MUTABILITY AND REFERENCES
# ============================================================

def mutability_demo():
    print("\n=== MUTABILITY AND REFERENCES ===")

    original = [1, 2, 3]
    alias = original

    alias.append(4)

    print("Original:", original)
    print("Alias:", alias)
    print("Same object:", original is alias)

    # Rebinding one variable does not rebind the other.
    alias = [100, 200]

    print("Original after rebinding alias:", original)
    print("Alias after rebinding:", alias)

    # Shallow copy.
    nested_original = [[1, 2], [3, 4]]
    shallow_copy = nested_original.copy()

    shallow_copy[0].append(99)

    print("Nested original:", nested_original)
    print("Shallow copy:", shallow_copy)

    # Deep copy.
    nested_original = [[1, 2], [3, 4]]
    deep_copy = deepcopy(nested_original)

    deep_copy[0].append(99)

    print("Original after deep copy mutation:", nested_original)
    print("Deep copy:", deep_copy)


# ============================================================
# 6. COMPREHENSIONS
# ============================================================

def comprehensions_demo():
    print("\n=== COMPREHENSIONS ===")

    numbers = list(range(1, 11))

    squares = [number ** 2 for number in numbers]
    evens = [number for number in numbers if number % 2 == 0]

    square_map = {
        number: number ** 2
        for number in numbers
    }

    remainder_set = {
        number % 3
        for number in numbers
    }

    print("Squares:", squares)
    print("Evens:", evens)
    print("Square map:", square_map)
    print("Remainders:", remainder_set)

    # Nested list comprehension.
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    flattened = [
        value
        for row in matrix
        for value in row
    ]

    print("Flattened:", flattened)

    # Generator expression: produces values lazily.
    squared_generator = (
        number ** 2
        for number in numbers
    )

    print("Generator output:", list(squared_generator))


# ============================================================
# 7. COUNTER AND FREQUENCY COUNTING
# ============================================================

def counter_demo():
    print("\n=== COUNTER ===")

    statuses = [
        "completed",
        "pending",
        "completed",
        "failed",
        "completed",
        "pending",
    ]

    counts = Counter(statuses)

    print("Counts:", counts)
    print("Completed:", counts["completed"])
    print("Most common:", counts.most_common(2))

    words = ["python", "sql", "python", "spark", "sql", "python"]

    word_counts = Counter(words)

    print("Word counts:", word_counts)

    # Counter is useful for categorical summaries.
    # It does not replace explicit data validation.


# ============================================================
# 8. DEFAULTDICT
# ============================================================

def defaultdict_demo():
    print("\n=== DEFAULTDICT ===")

    grouped_values = defaultdict(list)

    grouped_values["A"].append(10)
    grouped_values["A"].append(20)
    grouped_values["B"].append(30)

    print(dict(grouped_values))

    grouped_totals = defaultdict(float)

    grouped_totals["A"] += 100.5
    grouped_totals["A"] += 200.0
    grouped_totals["B"] += 50.0

    print(dict(grouped_totals))


# ============================================================
# 9. QUEUES AND STACKS
# ============================================================

def queues_and_stacks_demo():
    print("\n=== QUEUES AND STACKS ===")

    # Stack: last in, first out.
    stack = []

    stack.append("task-1")
    stack.append("task-2")
    stack.append("task-3")

    print("Stack:", stack)
    print("Popped:", stack.pop())

    # Queue: first in, first out.
    queue = deque()

    queue.append("record-1")
    queue.append("record-2")
    queue.append("record-3")

    print("Queue:", queue)
    print("Processed:", queue.popleft())

    print("Remaining:", queue)

    # deque is generally more appropriate than list.pop(0)
    # for repeated queue operations at the front.


# ============================================================
# 10. SORTING
# ============================================================

def sorting_demo():
    print("\n=== SORTING ===")

    numbers = [5, 1, 9, 3, 7]

    print("Ascending:", sorted(numbers))
    print("Descending:", sorted(numbers, reverse=True))

    employees = [
        {"name": "Amin", "salary": 15000},
        {"name": "Khaled", "salary": 12000},
        {"name": "Ahmed", "salary": 18000},
    ]

    by_salary = sorted(
        employees,
        key=lambda employee: employee["salary"],
    )

    print("By salary:", by_salary)

    # Multi-key sorting.
    orders = [
        {"status": "pending", "amount": 100},
        {"status": "completed", "amount": 500},
        {"status": "completed", "amount": 200},
        {"status": "pending", "amount": 300},
    ]

    sorted_orders = sorted(
        orders,
        key=lambda order: (order["status"], order["amount"]),
    )

    print("Multi-key sorting:", sorted_orders)

    # Find the top 2 records without sorting every record.
    top_orders = nlargest(
        2,
        orders,
        key=lambda order: order["amount"],
    )

    print("Top 2 orders:", top_orders)


# ============================================================
# 11. SEARCHING
# ============================================================

def searching_demo():
    print("\n=== SEARCHING ===")

    numbers = [10, 20, 30, 40, 50]
    target = 30

    # Linear search.
    found_index = None

    for index, value in enumerate(numbers):
        if value == target:
            found_index = index
            break

    print("Linear search result:", found_index)

    # Membership in a set.
    number_set = set(numbers)

    print("Target in set:", target in number_set)

    # Binary search requires sorted input.
    def binary_search(sorted_values, target_value):
        left = 0
        right = len(sorted_values) - 1

        while left <= right:
            middle = (left + right) // 2

            if sorted_values[middle] == target_value:
                return middle

            if sorted_values[middle] < target_value:
                left = middle + 1
            else:
                right = middle - 1

        return -1

    print("Binary search:", binary_search(numbers, 40))
    print("Missing target:", binary_search(numbers, 99))


# ============================================================
# 12. GROUP RECORDS
# ============================================================

def grouping_demo():
    print("\n=== GROUPING RECORDS ===")

    orders = [
        {"order_id": 101, "status": "completed", "amount": 100},
        {"order_id": 102, "status": "pending", "amount": 200},
        {"order_id": 103, "status": "completed", "amount": 300},
        {"order_id": 104, "status": "failed", "amount": 50},
        {"order_id": 105, "status": "pending", "amount": 150},
    ]

    grouped_orders = defaultdict(list)

    for order in orders:
        grouped_orders[order["status"]].append(order)

    print("Grouped records:")

    for status, records in grouped_orders.items():
        print(status, records)

    # Aggregate amount by status.
    totals_by_status = defaultdict(float)

    for order in orders:
        totals_by_status[order["status"]] += order["amount"]

    print("Totals:", dict(totals_by_status))


# ============================================================
# 13. DEDUPLICATION
# ============================================================

def deduplication_demo():
    print("\n=== DEDUPLICATION ===")

    records = [
        {"order_id": 101, "amount": 100},
        {"order_id": 102, "amount": 200},
        {"order_id": 101, "amount": 100},
        {"order_id": 103, "amount": 300},
        {"order_id": 102, "amount": 250},
    ]

    seen_ids = set()
    unique_records = []
    duplicate_records = []

    for record in records:
        order_id = record["order_id"]

        if order_id in seen_ids:
            duplicate_records.append(record)
        else:
            seen_ids.add(order_id)
            unique_records.append(record)

    print("Unique records:", unique_records)
    print("Repeated keys:", duplicate_records)

    # IMPORTANT:
    # order_id 102 appears twice with different amounts.
    # The second record may be a legitimate update.
    # A business rule is required before choosing which record wins.


def deduplicate_exact_records(records):
    """
    Remove exact duplicate dictionaries while preserving order.

    Assumes each record contains hashable values.
    For nested or complex records, use a suitable canonical key.
    """
    seen = set()
    result = []

    for record in records:
        record_key = tuple(sorted(record.items()))

        if record_key not in seen:
            seen.add(record_key)
            result.append(record)

    return result


# ============================================================
# 14. MERGING RECORDS
# ============================================================

def merge_records_demo():
    print("\n=== MERGING RECORDS ===")

    customers = [
        {"customer_id": 1, "name": "Amin"},
        {"customer_id": 2, "name": "Khaled"},
        {"customer_id": 3, "name": "Ahmed"},
    ]

    orders = [
        {"order_id": 101, "customer_id": 1, "amount": 100},
        {"order_id": 102, "customer_id": 2, "amount": 200},
        {"order_id": 103, "customer_id": 1, "amount": 300},
    ]

    customers_by_id = {
        customer["customer_id"]: customer
        for customer in customers
    }

    enriched_orders = []

    for order in orders:
        customer = customers_by_id.get(order["customer_id"])

        enriched_orders.append({
            **order,
            "customer_name": (
                customer["name"] if customer else None
            ),
        })

    print("Enriched orders:", enriched_orders)


# ============================================================
# 15. CHUNKING A DATASET
# ============================================================

def chunked(iterable, chunk_size):
    """Yield lists containing up to chunk_size items."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    iterator = iter(iterable)

    while True:
        batch = list(islice(iterator, chunk_size))

        if not batch:
            break

        yield batch


def chunking_demo():
    print("\n=== CHUNKING ===")

    records = list(range(1, 12))

    for batch in chunked(records, 4):
        print("Processing batch:", batch)

    # Chunking is useful for bounded-memory processing.
    # This example starts from an in-memory list.
    # For large files, read incrementally instead of loading
    # the entire source into a list first.


# ============================================================
# 16. DATA QUALITY
# ============================================================

def data_quality_demo():
    print("\n=== DATA QUALITY ===")

    orders = [
        {"order_id": 101, "amount": 100, "status": "completed"},
        {"order_id": 102, "amount": -10, "status": "pending"},
        {"order_id": None, "amount": 200, "status": "completed"},
        {"order_id": 104, "amount": 300, "status": ""},
    ]

    valid_records = []
    invalid_records = []

    for order in orders:
        errors = []

        if order.get("order_id") is None:
            errors.append("Missing order_id")

        amount = order.get("amount")

        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            errors.append("Invalid amount")
        elif amount < 0:
            errors.append("Negative amount")

        if not isinstance(order.get("status"), str):
            errors.append("Invalid status type")
        elif not order["status"].strip():
            errors.append("Empty status")

        if errors:
            invalid_records.append({
                "record": order,
                "errors": errors,
            })
        else:
            valid_records.append(order)

    print("Valid:", valid_records)
    print("Invalid:", invalid_records)


# ============================================================
# 17. TIME COMPLEXITY EXPERIMENT
# ============================================================

def complexity_demo():
    print("\n=== COMPLEXITY EXPERIMENT ===")

    values = list(range(100_000))
    target = 99_999

    start = perf_counter()
    found_in_list = target in values
    list_duration = perf_counter() - start

    values_set = set(values)

    start = perf_counter()
    found_in_set = target in values_set
    set_duration = perf_counter() - start

    print("Found in list:", found_in_list)
    print("List membership seconds:", list_duration)

    print("Found in set:", found_in_set)
    print("Set membership seconds:", set_duration)

    # This is a small experiment, not a rigorous benchmark.
    # Results vary with hardware, Python version, and data.


# ============================================================
# 18. USEFUL DATA STRUCTURE PATTERNS
# ============================================================

def useful_patterns_demo():
    print("\n=== USEFUL PATTERNS ===")

    values = [10, 20, 30, 40]

    # First and last.
    print(values[0], values[-1])

    # Safe dictionary lookup.
    record = {"id": 101, "status": "completed"}
    print(record.get("amount", 0))

    # Stable uniqueness for hashable values.
    duplicated = [3, 1, 3, 2, 1, 4]
    stable_unique = list(dict.fromkeys(duplicated))

    print("Stable unique:", stable_unique)

    # Pair two sequences.
    names = ["Amin", "Khaled", "Ahmed"]
    scores = [90, 85, 88]

    print(dict(zip(names, scores)))

    # Group items by a key.
    words = ["apple", "ant", "banana", "berry", "avocado"]
    grouped_words = defaultdict(list)

    for word in words:
        grouped_words[word[0]].append(word)

    print(dict(grouped_words))


# ============================================================
# 19. MINI EXERCISES
# ============================================================

def exercise_1_second_largest(numbers):
    """Return the second-largest distinct number, or None."""
    unique_numbers = sorted(set(numbers))

    if len(unique_numbers) < 2:
        return None

    return unique_numbers[-2]


def exercise_2_frequency(values):
    """Return a frequency dictionary."""
    return dict(Counter(values))


def exercise_3_group_by_status(records):
    """Group records by status."""
    grouped = defaultdict(list)

    for record in records:
        status = record.get("status", "unknown")
        grouped[status].append(record)

    return dict(grouped)


def exercise_4_total_by_customer(orders):
    """Calculate total order amount per customer."""
    totals = defaultdict(float)

    for order in orders:
        customer_id = order["customer_id"]
        totals[customer_id] += order["amount"]

    return dict(totals)


def exercise_5_stable_deduplication(records, key_name):
    """Keep the first record for each business key."""
    seen = set()
    result = []

    for record in records:
        key = record.get(key_name)

        if key not in seen:
            seen.add(key)
            result.append(record)

    return result


def exercise_6_find_missing_ids(expected_ids, actual_ids):
    """Return expected IDs missing from the actual collection."""
    return set(expected_ids) - set(actual_ids)


def exercise_7_find_unexpected_ids(expected_ids, actual_ids):
    """Return IDs present in actual data but not in expected data."""
    return set(actual_ids) - set(expected_ids)


def exercises_demo():
    print("\n=== MINI EXERCISES ===")

    print("Second largest:", exercise_1_second_largest([5, 1, 9, 9, 3]))
    print("Frequency:", exercise_2_frequency(["a", "b", "a", "c"]))

    orders = [
        {"order_id": 101, "customer_id": 1, "amount": 100, "status": "completed"},
        {"order_id": 102, "customer_id": 2, "amount": 200, "status": "pending"},
        {"order_id": 103, "customer_id": 1, "amount": 300, "status": "completed"},
    ]

    print("Grouped:", exercise_3_group_by_status(orders))
    print("Customer totals:", exercise_4_total_by_customer(orders))

    print(
        "Missing IDs:",
        exercise_6_find_missing_ids(
            [101, 102, 103, 104],
            [101, 103],
        ),
    )

    print(
        "Unexpected IDs:",
        exercise_7_find_unexpected_ids(
            [101, 102, 103],
            [101, 103, 999],
        ),
    )


# ============================================================
# 20. RUN ALL DEMONSTRATIONS
# ============================================================

def main():
    demos = [
        lists_demo,
        tuples_demo,
        sets_demo,
        dictionaries_demo,
        mutability_demo,
        comprehensions_demo,
        counter_demo,
        defaultdict_demo,
        queues_and_stacks_demo,
        sorting_demo,
        searching_demo,
        grouping_demo,
        deduplication_demo,
        merge_records_demo,
        chunking_demo,
        data_quality_demo,
        complexity_demo,
        useful_patterns_demo,
        exercises_demo,
    ]

    for demo in demos:
        try:
            demo()
        except Exception as error:
            print(f"{demo.__name__} failed: {error}")


if __name__ == "__main__":
    main()


# ============================================================
# CHALLENGES — SOLVE THESE YOURSELF
# ============================================================
#
# 1. Find the second-largest distinct number without sorting.
#
# 2. Count how many times each customer appears.
#
# 3. Group orders by customer and calculate total revenue.
#
# 4. Identify duplicate order IDs and preserve the source records.
#
# 5. Find missing IDs between an expected list and an actual list.
#
# 6. Merge customers and orders using customer_id.
#
# 7. Return the five largest orders efficiently.
#
# 8. Implement a queue using collections.deque.
#
# 9. Explain why set membership is generally faster than list
#    membership for large collections.
#
# 10. Explain why average-case O(1) dictionary lookup is not
#     the same as a guarantee of O(1) in every possible case.
#
# 11. Process records in batches without creating a second full
#     copy of the dataset.
#
# 12. Design a deduplication strategy for repeated business keys
#     where records may contain conflicting values.
#
# 13. Explain the difference between exact duplicate records
#     and records that share a business key.
#
# 14. Write tests for every function in the mini exercises.
#
# 15. Discuss when a Python list, set, dictionary, or database
#     index is the appropriate choice.
#
# IMPORTANT:
# Data structure choice affects correctness, memory usage,
# performance, and maintainability. Always connect the choice
# to the actual workload and its requirements.
```