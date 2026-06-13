# Python Libraries for DSA (Data Structures & Algorithms)

Python provides powerful built-in libraries and modules for implementing Data Structures and Algorithms efficiently.

## Comparable To

- **C++** → STL (Standard Template Library)
- **Java** → Collections Framework
- **Python** → Built-in Libraries & Modules

## Why Learn Them?

- **Save Time** → Use pre-written and optimized code.
- Makes DSA questions easier and cleaner to solve.
- **Industry Standard** → Widely used in coding interviews and real-world software development.

---

# Built-in Functions & Common Operations

## 1. Sorting

### `sorted(iterable, key=None, reverse=False)`

Returns a new sorted list without modifying the original.

### Parameters

- `key` → Function used to determine sort order.
- `reverse=True` → Sort in descending order.

### Examples

```python
arr = [3, 1, 4, 1, 5]

sorted(arr)
# [1, 1, 3, 4, 5]

sorted(arr, reverse=True)
# [5, 4, 3, 1, 1]
```

#### Sort by Custom Key

```python
arr = [-3, 1, -4, 2, -1]

sorted(arr, key=lambda x: abs(x))
# [1, -1, 2, -3, -4]
```

#### Sort Strings by Length

```python
words = ["apple", "pie", "banana"]

sorted(words, key=len)
# ['pie', 'apple', 'banana']
```

### In-Place Sorting

```python
arr.sort()  # Modifies original list
```

---

## 2. Min / Max

### `min(iterable, key=None)`

Returns the minimum value.

### `max(iterable, key=None)`

Returns the maximum value.

### Examples

```python
min([3, 1, 4, 1, 5])
# 1

max([3, 1, 4, 1, 5])
# 5
```

#### Using a Custom Key

```python
arr = [-3, 1, -4, 2]

min(arr, key=abs)
# 1

max(arr, key=abs)
# -4
```

---

## 3. Sum / Product

### `sum(iterable, start=0)`

Returns the sum of all elements.

### Examples

```python
sum([1, 2, 3, 4])
# 10

sum([1, 2, 3], 10)
# 16
```

### Product of Elements

#### Using `math.prod()` (Python 3.8+)

```python
import math

math.prod([2, 3, 4])
# 24
```

#### Using `functools.reduce()`

```python
from functools import reduce

reduce(lambda x, y: x * y, [2, 3, 4])
# 24
```

---

## 4. Length / Count

### `len(iterable)`

Returns the number of elements.

### `count(value)`

Returns the number of occurrences of a value.

### Examples

```python
len([1, 2, 3])
# 3

len("hello")
# 5
```

```python
[1, 2, 2, 3].count(2)
# 2

"hello".count('l')
# 2
```

---

## 5. Any / All

### `any(iterable)`

Returns `True` if at least one element is truthy.

### `all(iterable)`

Returns `True` if all elements are truthy.

### Examples

```python
any([False, True, False])
# True

all([True, True, True])
# True

any([])
# False

all([])
# True
```

### DSA Usage

```python
nums = [2, 4, 6, 8]

all(x % 2 == 0 for x in nums)
# True
```

---

## 6. Enumerate

### `enumerate(iterable, start=0)`

Returns `(index, value)` pairs.

### Examples

```python
for i, val in enumerate([10, 20, 30]):
    print(i, val)

# 0 10
# 1 20
# 2 30
```

```python
list(enumerate(['a', 'b', 'c']))
# [(0, 'a'), (1, 'b'), (2, 'c')]
```

```python
list(enumerate(['a', 'b'], 1))
# [(1, 'a'), (2, 'b')]
```

### DSA Usage

- Avoid manual index tracking.
- Cleaner loops in DSA problems.

---

## 7. Zip

### `zip(*iterables)`

Combines multiple iterables element-wise.

### Examples

```python
list(zip([1, 2], [3, 4]))
# [(1, 3), (2, 4)]
```

```python
list(zip([1, 2, 3], [4, 5]))
# [(1, 4), (2, 5)]
```

```python
list(zip([1, 2], [3, 4], [5, 6]))
# [(1, 3, 5), (2, 4, 6)]
```

### Unzipping

```python
pairs = [(1, 3), (2, 4)]

a, b = zip(*pairs)

# a = (1, 2)
# b = (3, 4)
```

---

## 8. Reversed

### `reversed(iterable)`

Returns a reverse iterator.

### Examples

```python
list(reversed([1, 2, 3]))
# [3, 2, 1]
```

```python
"hello"[::-1]
# "olleh"
```

### Loop in Reverse Order

```python
for x in reversed([1, 2, 3]):
    print(x)

# 3
# 2
# 1
```

---

## 9. Range

### `range(stop)`

Generates numbers from `0` to `stop - 1`.

### `range(start, stop)`

Generates numbers from `start` to `stop - 1`.

### `range(start, stop, step)`

Generates numbers with a custom step size.

### Examples

```python
list(range(5))
# [0, 1, 2, 3, 4]
```

```python
list(range(1, 5))
# [1, 2, 3, 4]
```

```python
list(range(0, 10, 2))
# [0, 2, 4, 6, 8]
```

```python
list(range(5, 0, -1))
# [5, 4, 3, 2, 1]
```

---