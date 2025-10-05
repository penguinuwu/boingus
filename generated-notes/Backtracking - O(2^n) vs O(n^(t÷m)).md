# Backtracking - O(2^n) vs O(n^(t/m))

Excellent question! This is a key insight for understanding backtracking complexity. Let me break it down:

---

## **Why Combination Sum II ≈ Subsets (both O(2^n))**

**Combination Sum II:**
- Each element can be used **at most once**
- For each element: **include it OR skip it** (binary choice)
- This is literally generating subsets, then filtering by `sum == target`
- Decision tree: binary at each step → **2^n possibilities**

**Subsets:**
- For each element: **include it OR skip it** (binary choice)
- Same binary decision tree → **2^n subsets**

**Key insight:** Combination Sum II is just "subsets with a filter". The structure is identical!

```python
# Combination Sum II - binary choices
for idx in range(start_idx, n):
    # Choice 1: Skip this element (move to next)
    # Choice 2: Include this element
    curr_list.append(nums[idx])
    backtrack(idx + 1, ...)  # Move to NEXT element (idx+1)
    curr_list.pop()
```

---

## **Why Combination Sum I is Different (O(n^(t/m)))**

**Combination Sum I:**
- Each element can be used **unlimited times**
- At each step: try **all n candidates** (not just skip/include)
- Can stay at same element multiple times
- Decision tree: n-way branching at each level!

```python
# Combination Sum I - n-way choices per level
for idx in range(start_idx, n):
    curr_list.append(candidates[idx])
    backtrack(idx, ...)  # Stay at SAME element (idx, not idx+1)
    curr_list.pop()
```

**Tree structure:**
```
Level 0: root
Level 1: n branches (try each candidate)
Level 2: each node branches n ways again
...
Max depth: t/m (until we hit target)

Total nodes: n^(t/m)
```

---

## **Visual Comparison**

### **Combination Sum II (No Repeat) - Binary Tree**
```
Array: [1, 2, 3], Target: 3

                    []
         /                      \
    skip 1                   include 1
       []                        [1]
     /    \                    /     \
  skip 2  +2              skip 2    +2
   []     [2]              [1]     [1,2]
  / \     / \              / \      / \
s/i 3  s/i 3            s/i 3   s/i 3
[] [3] [2] [2,3]      [1] [1,3] [1,2] [1,2,3]

Binary choices → 2^n leaves
```

### **Combination Sum I (Repeat Allowed) - N-ary Tree**
```
Array: [2, 3], Target: 7

                        []
                   /         \
              +2 (can reuse)  +3 (can reuse)
               [2]              [3]
            /      \          /     \
        +2  +3   +2  +3    +2  +3  +2  +3
       [2,2] [2,3] ...    [3,2] [3,3] ...
       
Each node has n children → n^depth branches
Max depth = t/m → n^(t/m) total
```

---

## **How to Memorize**

### **🔑 Key Question: "Can I reuse elements?"**

| Can Reuse? | Pattern | Complexity | Analogy |
|------------|---------|------------|---------|
| **NO** (each used once) | Binary choice per element | **O(2^n)** | Like subsets |
| **YES** (unlimited reuse) | n-way choice at each level | **O(n^depth)** | Like nested loops |

---

## **Mental Model**

### **Type 1: "Binary Choice Problems" → O(2^n)**
- **Structure:** Include/exclude each element once
- **Recursion:** `backtrack(idx + 1, ...)` (move to NEXT)
- **Examples:**
  - Subsets
  - Subsets II
  - Combination Sum II
  - Partition problems

**Pattern:**
```python
for idx in range(start_idx, n):
    # Decision: include nums[idx]
    curr_list.append(nums[idx])
    backtrack(idx + 1, ...)  # ← idx+1: move forward
    curr_list.pop()
    # (Decision to skip is implicit in the loop)
```

### **Type 2: "N-way Choice Problems" → O(n^depth)**
- **Structure:** At each step, try all n candidates
- **Recursion:** `backtrack(idx, ...)` (can STAY at same index)
- **Examples:**
  - Combination Sum (with repetition)
  - Coin Change (backtracking version)

**Pattern:**
```python
for idx in range(start_idx, n):
    curr_list.append(candidates[idx])
    backtrack(idx, ...)  # ← idx: can reuse same element
    curr_list.pop()
```

---

## **The "idx vs idx+1" Rule**

**This is the smoking gun!**

```python
# Combination Sum II (no repeat)
backtrack(idx + 1, ...)  # Next element → Binary tree → O(2^n)

# Combination Sum I (with repeat)
backtrack(idx, ...)      # Same element OK → N-ary tree → O(n^depth)
```

---

## **Quick Reference**

| Problem | Repeat? | Recursion Call | Tree Type | Complexity |
|---------|---------|---------------|-----------|------------|
| Subsets | - | `f(idx+1)` | Binary | O(2^n) |
| Subsets II | - | `f(idx+1)` | Binary | O(2^n) |
| Combination Sum II | ❌ | `f(idx+1)` | Binary | O(2^n) |
| Combination Sum I | ✅ | `f(idx)` | N-ary | O(n^(t/m)) |
| Permutations | - | tries all unused | Full tree | O(n!) |

---

## **Memorization Trick**

**"Plus one or not?"**
- **`idx + 1`** in recursion → "moving forward" → binary choices → **O(2^n)**
- **`idx`** in recursion → "staying put allowed" → n-way choices → **O(n^depth)**

**Story:** 
- Combination Sum II is like picking teammates: each person says YES or NO once → 2^n timelines
- Combination Sum I is like shopping: you can pick the same item multiple times → much more possibilities!

---

Hope this clarifies it! The key is recognizing whether elements can be reused, which determines if you're building a binary tree (2^n) or an n-ary tree (n^depth). 🎯
