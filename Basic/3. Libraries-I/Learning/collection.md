# Collections Module – Specialized Data Structures

The `collections` module provides advanced container data types that are extremely useful in DSA.

## Main Components

* `deque` → Double-ended queue
* `Counter` → Frequency counter
* `defaultdict` → Dictionary with default values
* `OrderedDict` → Ordered dictionary with extra operations
* `namedtuple` → Lightweight immutable data structure

---

# 1. Deque (Double-Ended Queue)

A deque allows fast insertion and deletion from both ends in **O(1)** time.

### Import

```python
from collections import deque
```

### Methods

```python
d = deque([1, 2, 3])

d.append(4)
# deque([1, 2, 3, 4])

d.appendleft(0)
# deque([0, 1, 2, 3, 4])

d.pop()
# returns 4

d.popleft()
# returns 0

d.extend([5, 6])
# deque([1, 2, 3, 5, 6])

d.extendleft([-1, 0])
# deque([0, -1, 1, 2, 3])

d.rotate(2)
# Rotate 2 steps right

d.rotate(-1)
# Rotate 1 step left

len(d)
# Length

d[0]
# Access by index
```

### When to Use

* Queue implementation
* Stack implementation
* Sliding Window problems
* BFS Traversal
* Fast insert/delete at both ends

---

# 2. Counter (Frequency Counter)

Automatically counts occurrences of elements.

### Import

```python
from collections import Counter
```

### Methods

```python
c = Counter([1, 2, 2, 3, 3, 3])

c[2]
# 2

c[5]
# 0

c.most_common(2)
# [(3, 3), (2, 2)]

list(c.elements())
# [1, 2, 2, 3, 3, 3]

c.update([3, 4])
# Adds counts

c.subtract([2, 2])
# Subtracts counts
```

### Counter Operations

```python
c1 = Counter([1, 3, 3, 3, 3, 4])
c2 = Counter([3, 4, 4])

c1 + c2
# Counter({3: 5, 4: 3, 1: 1})

c1 - c2
# Counter({3: 3, 1: 1})

c1 & c2
# Intersection (min counts)

c1 | c2
# Union (max counts)
```

### When to Use

* Frequency counting
* Most common elements
* Anagram problems
* Character counting
* Frequency-based problems

---

# 3. defaultdict (Dictionary with Defaults)

A dictionary that automatically creates missing keys with a default value.

**Never raises `KeyError` for missing keys.**

### Import

```python
from collections import defaultdict
```

### Methods

#### Integer Default (`0`)

```python
dd = defaultdict(int)

dd['a']
# 0

dd['a'] += 1
# {'a': 1}
```

#### List Default (`[]`)

```python
dd_list = defaultdict(list)

dd_list['fruits'].append('apple')

dd_list['fruits']
# ['apple']
```

#### Set Default (`set()`)

```python
dd_set = defaultdict(set)

dd_set['nums'].add(1)

dd_set['nums']
# {1}
```

#### Custom Default

```python
dd_custom = defaultdict(lambda: "N/A")

dd_custom['missing']
# "N/A"
```

### When to Use

* Grouping elements
* Building graphs
* Avoiding KeyError checks
* Counting with auto-initialization

---

# 4. OrderedDict (Ordered Dictionary)

Dictionary that preserves insertion order and provides extra ordering operations.

> **Note:** Since Python 3.7+, normal dictionaries also preserve insertion order. `OrderedDict` is mainly useful for its additional methods.

### Import

```python
from collections import OrderedDict
```

### Methods

```python
od = OrderedDict([
    ('a', 1),
    ('b', 2),
    ('c', 3)
])

od['d'] = 4
```

#### Move Item to End

```python
od.move_to_end('a')
```

#### Move Item to Beginning

```python
od.move_to_end('c', last=False)
```

#### Remove Last Item

```python
od.popitem()
```

#### Remove First Item

```python
od.popitem(last=False)
```

### When to Use

* LRU Cache implementation
* Ordered dictionary requirements
* Front/back dictionary operations

---

# 5. namedtuple

Tuples with named fields.

* Immutable
* Lightweight
* Memory efficient

### Import

```python
from collections import namedtuple
```

### Methods

```python
Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)
```

#### Access by Name

```python
p.x
# 1

p.y
# 2
```

#### Access by Index

```python
p[0]
# 1

p[1]
# 2
```

#### Immutability

```python
p.x = 3
# ERROR! Cannot modify
```

### When to Use

* Lightweight data structures
* Returning multiple values
* Immutable records
* Dictionary keys
* Cleaner alternative to regular tuples

---
