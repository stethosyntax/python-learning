"""Python Libraries I Learning Module.

This module demonstrates commonly used Python built-in functions
and collections library utilities including:

- Built-in functions (len, sorted, min, max, sum, all, any)
- enumerate(), reversed(), and range()
- math module functions
- collections module:
    - deque
    - Counter
    - defaultdict
    - OrderedDict
    - namedtuple
- Custom classes

The script reads from input.txt and writes output to output.txt.
"""

import sys
import math
from collections import (
    OrderedDict,
    deque,
    Counter,
    defaultdict,
    namedtuple
)

sys.stdin = open('/Users/aruna/Desktop/Aruna/Career/Python-Learning/Basic/3. Libraries-I/Learning/input.txt', 'r')
sys.stdout = open('/Users/aruna/Desktop/Aruna/Career/Python-Learning/Basic/3. Libraries-I/Learning/output.txt', 'w')

# ============================================================================
# SECTION 1: STRING LENGTH OPERATIONS
# ============================================================================

print("\n" + "=" * 80)
print("1. STRING LENGTH OPERATIONS")
print("=" * 80 + "\n")

name = "Laura"

print(f"  Name: {name}")
print(f"  Built-in len(): {len(name)}")


def length_of_string(text):
    """Calculate the length of a string manually.

    Args:
        text (str): Input string.

    Returns:
        int: Number of characters in the string.
    """
    count = 0

    for _ in text:
        count += 1

    return count


print(f"  Custom length function: {length_of_string(name)}")

# ============================================================================
# SECTION 2: SORTING OPERATIONS
# ============================================================================

print("\n" + "=" * 80)
print("2. SORTING OPERATIONS")
print("=" * 80 + "\n")

print("2.1 Sorting Integer Lists")
print("-" * 80)

arr = [1, 5, 6, 7, 4]

print(f"  Original List: {arr}")
print(f"  Sorted Ascending: {sorted(arr)}")
print(f"  Sorted Descending: {sorted(arr, reverse=True)}")
print(f"  Original List After sorted(): {arr}")

arr.sort()

print(f"  After arr.sort(): {arr}")

arr.sort(reverse=True)

print(f"  After arr.sort(reverse=True): {arr}")

print("\n" + "-" * 80)
print("2.2 Sorting Using Absolute Values")
print("-" * 80)

arr = [-1, 5, -6, 7, 4]

print(f"  Original List: {arr}")
print(f"  Ascending: {sorted(arr)}")
print(f"  Descending: {sorted(arr, reverse=True)}")
print(f"  By Absolute Value: {sorted(arr, key=abs)}")
print(
    f"  By Absolute Value (Descending): "
    f"{sorted(arr, key=abs, reverse=True)}"
)

print(
    f"  Lambda Absolute Sort: "
    f"{sorted(arr, key=lambda x: abs(x))}"
)

print(
    f"  Lambda Absolute Sort (Descending): "
    f"{sorted(arr, key=lambda x: abs(x), reverse=True)}"
)

print("\n" + "-" * 80)
print("2.3 Sorting Strings")
print("-" * 80)

fruit_list = ["apple", "pineapple", "kiwi"]

print(f"  Original List: {fruit_list}")
print(f"  Alphabetical Order: {sorted(fruit_list)}")
print(f"  By Length: {sorted(fruit_list, key=len)}")
print(
    f"  By Length (Descending): "
    f"{sorted(fruit_list, key=len, reverse=True)}"
)

# ============================================================================
# SECTION 3: MINIMUM, MAXIMUM, AND SUM FUNCTIONS
# ============================================================================

print("\n" + "=" * 80)
print("3. MINIMUM, MAXIMUM, AND SUM FUNCTIONS")
print("=" * 80 + "\n")

print("3.1 Minimum and Maximum Values")
print("-" * 80)

arr = [-15, 6, 8, 7]

print(f"  List: {arr}")
print(f"  Minimum Value: {min(arr)}")
print(f"  Maximum Value: {max(arr)}")
print(f"  Maximum by Absolute Value: {max(arr, key=abs)}")

print("\n" + "-" * 80)
print("3.2 Sum Operations")
print("-" * 80)

arr = [15, 6, 8, 7]

print(f"  List: {arr}")
print(f"  Sum: {sum(arr)}")
print(f"  Sum with Start Value 10: {sum(arr, 10)}")
print(f"  Sum with Keyword Start=10: {sum(arr, start=10)}")

print("\n" + "-" * 80)
print("3.3 Math Module Functions")
print("-" * 80)

arr = [1, 2, 4]

print(f"  List: {arr}")
print(f"  math.fsum(): {math.fsum(arr)}")
print(f"  math.prod(): {math.prod(arr)}")
print(f"  Length: {len(arr)}")

# ============================================================================
# SECTION 4: BOOLEAN AND COUNT OPERATIONS
# ============================================================================

print("\n" + "=" * 80)
print("4. BOOLEAN AND COUNT OPERATIONS")
print("=" * 80 + "\n")


print("4.1 all() and any()")
print("-" * 80)

arr = [True, False, True]

print(f"  Values: {arr}")
print(f"  all(): {all(arr)}")
print(f"  any(): {any(arr)}")

print("\n" + "-" * 80)
print("4.2 count()")
print("-" * 80)

arr = [1, 6, 1, 7]

print(f"  List: {arr}")
print(f"  Count of 1: {arr.count(1)}")
print(f"  Count of 6: {arr.count(6)}")


def count_elements_in_list(arr, element):
    """Count occurrences of an element in a list.

    Args:
        arr (list): Input list.
        element (Any): Element to count.

    Returns:
        int: Number of occurrences.
    """
    count = 0

    for value in arr:
        if value == element:
            count += 1

    return count


print(
    f"  Custom Count of 1: "
    f"{count_elements_in_list(arr, 1)}"
)

# ============================================================================
# SECTION 5: ENUMERATE, REVERSED, AND RANGE
# ============================================================================

print("\n" + "=" * 80)
print("5. ENUMERATE, REVERSED, AND RANGE FUNCTIONS")
print("=" * 80 + "\n")

print("5.1 enumerate() FUNCTION")
print("-" * 80)

arr = [5, 6, 1, 3]

print(f"  Original List: {arr}")
print(f"  Enumerated List (index-value pairs): {list(enumerate(arr))}")

print("\n  Iterating using enumerate:")
for index, value in enumerate(arr):
    print(f"    Index: {index}, Value: {value}")

print("\n" + "-" * 80)
print("5.2 reversed() FUNCTION")
print("-" * 80)

arr = [5, 6, 1, 3]

print(f"  Original List: {arr}")
print(f"  Reversed List: {list(reversed(arr))}")
print(f"  Original List (unchanged): {arr}")

print("\n" + "-" * 80)
print("5.3 range() FUNCTION")
print("-" * 80)

print(f"  range(5): {list(range(5))}")
print(f"  range(1, 6): {list(range(1, 6))}")
print(f"  range(0, 10, 2): {list(range(0, 10, 2))}")


# ============================================================================
# SECTION 6: COLLECTIONS MODULE - DEQUE
# ============================================================================

print("\n" + "=" * 80)
print("6. COLLECTIONS MODULE - DEQUE")
print("=" * 80 + "\n")

dq = deque([2, 3, 1])

print(f"  Initial Deque: {dq}")

dq.append(5)
print(f"  After append(5): {dq}")

dq.appendleft(7)
print(f"  After appendleft(7): {dq}")

dq.pop()
print(f"  After pop(): {dq}")

dq.popleft()
print(f"  After popleft(): {dq}")

dq.extend([10, "Raj"])
print(f"  After extend([10, 'Raj']): {dq}")

dq.extendleft([89, "Laura"])
print(f"  After extendleft([89, 'Laura']): {dq}")

dq.rotate(7)
print(f"  After rotate(7): {dq}")

dq.rotate(2)
print(f"  After rotate(2): {dq}")

print(f"  Final Deque Length: {len(dq)}")

# we use deque in stacks and queues because of its efficient append and pop operations from both ends. In a stack, we can use append() to push elements and pop() to pop elements from the right end. In a queue, we can use append() to enqueue elements at the right end and popleft() to dequeue elements from the left end.
# we use it in breadth-first search (BFS) algorithm because it allows us to efficiently add and remove elements from both ends of the queue, which is essential for the BFS algorithm to explore all neighbors of a node before moving on to the next level of nodes.
# we use it in fast operations on both ends of the list because it provides O(1) time complexity for append and pop operations from both ends, making it more efficient than a regular list for certain use cases where we need to frequently add or remove elements from both ends of the collection.

# ============================================================================
# SECTION 7: COLLECTIONS MODULE - COUNTER
# ============================================================================

print("\n" + "=" * 80)
print("7. COLLECTIONS MODULE - COUNTER")
print("=" * 80 + "\n")

arr = [1, 2, 2, 3, 2, 3, 3, 4]

counter = Counter(arr)

print(f"  List: {arr}")
print(f"  Counter Object: {counter}")
print(f"  Count of 4: {counter[4]}")
print(f"  Most Common (2): {counter.most_common(2)}")
print(f"  Most Common (1): {counter.most_common(1)}")

print("\n  Elements expanded:")
print(list(counter.elements()))

counter.update([7, 7, 3])
print(f"\n  After update([7, 7, 3]): {counter}")

counter.subtract([3, 3])
print(f"  After subtract([3, 3]): {counter}")


# Counter operations
c1 = Counter([1, 3, 2, 2, 2, 3, 3, 4])
c2 = Counter([3, 3, 1, 4, 5])

print("\n  Counter c1:", c1)
print("  Counter c2:", c2)

print("  Addition (c1 + c2):", c1 + c2)
print("  Subtraction (c1 - c2):", c1 - c2)
print("  Intersection (c1 & c2):", c1 & c2)
print("  Union (c1 | c2):", c1 | c2)

# Counter is used in various applications such as counting occurrences of elements in a list, finding the most common elements, and performing operations like addition, subtraction, intersection, and union on counts of elements. It is particularly useful in tasks like frequency analysis, data analysis, and natural language processing where counting occurrences of items is essential.

# ============================================================================
# SECTION 8: COLLECTIONS MODULE - DEFAULTDICT
# ============================================================================

print("\n" + "=" * 80)
print("8. COLLECTIONS MODULE - DEFAULTDICT")
print("=" * 80 + "\n")

dd = defaultdict(int)

print(f"  Defaultdict(int): {dd}")
print(f"  Missing key 'key1': {dd['key1']}")

dd[1] = "Laura"
dd["smith"] = "Raj"
dd["u"] = 99
dd["list"] = [1, 2, 3]

print(f"  After insertions: {dd}")
print(f"  Access 'list': {dd['list']}")

dd_set = defaultdict(set)

print("\n  Defaultdict(set):")
print(f"  Missing key: {dd_set['key1']}")

dd_set["Laura"] = [7, 8, 9]
print(f"  Laura initial value: {dd_set['Laura']}")

dd_set["Laura"].append(10)
print(f"  After append: {dd_set['Laura']}")

# ============================================================================
# SECTION 9: COLLECTIONS MODULE - ORDEREDDICT
# ============================================================================

print("\n" + "=" * 80)
print("9. COLLECTIONS MODULE - ORDEREDDICT")
print("=" * 80 + "\n")

od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])

print(f"  Initial OrderedDict: {od}")

print("  Key 'e' exists:", "e" in od)

od["e"] = 5
print(f"  After adding 'e': {od}")

od.move_to_end("b")
print(f"  After move_to_end('b'): {od}")

od.move_to_end("e", last=False)
print(f"  After move_to_end('e', first): {od}")

od.popitem()
print(f"  After popitem(): {od}")

od.popitem(last=False)
print(f"  After popitem(last=False): {od}")

print(f"  pop('c'): {od.pop('c')}")
print(f"  Final OrderedDict: {od}")

# wrong keys give KeyError in OrderedDict, while in defaultdict it gives default value. This is because OrderedDict does not have a default value for missing keys, while defaultdict does. In OrderedDict, if you try to access a key that does not exist, it raises a KeyError. In defaultdict, if you try to access a key that does not exist, it returns the default value specified when creating the defaultdict instead of raising an error.
# used in hashing and caching because of its ability to maintain the order of insertion, which can be important for certain applications where the order of elements matters. It is also used in situations where we need to ensure that the order of key-value pairs is preserved, such as when serializing data or when working with APIs that require ordered data.

# ============================================================================
# SECTION 10: NAMEDTUPLE
# ============================================================================

print("\n" + "=" * 80)
print("10. NAMEDTUPLE")
print("=" * 80 + "\n")

Point = namedtuple("Point", ["first", "second"])
NestedPoints = namedtuple("NestedPoints", ["first", "second"])

val = Point(7, 9)
print(f"  Point: {val}")
print(f"  First Value: {val.first}")

nested = NestedPoints(2, val)

print(f"  NestedPoints: {nested}")
print(f"  Inner Point: {nested.second}")
print(f"  Inner Value: {nested.second.second}")

# ============================================================================
# SECTION 11: CUSTOM CLASS
# ============================================================================

print("\n" + "=" * 80)
print("11. CUSTOM CLASS")
print("=" * 80 + "\n")


class Pair:
    """Store two related values.

    Attributes:
        first: First value.
        second: Second value.
    """

    def __init__(self, first, second):
        """Initialize Pair object.

        Args:
            first: First value.
            second: Second value.
        """
        self.first = first
        self.second = second


val = Pair(2, 9)
print(f"  Pair Object: ({val.first}, {val.second})")

val.first = 10
print(f"  After update: ({val.first}, {val.second})")

val2 = Pair(21, 89)
print(f"  Second Pair: ({val2.first}, {val2.second})")


# ============================================================================
# END OF MODULE
# ============================================================================

print("\n" + "=" * 80)
print("END OF LIBRARIES I MODULE")
print("=" * 80 + "\n")