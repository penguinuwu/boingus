# Backtracking - !!! Time Complexity Summary

Great question! Here's a comprehensive guide to **backtracking time complexities** for different problem types:

---

## **1. Subsets (Power Set)**
**Problem:** Generate all subsets of a set (no duplicates in input)

**Example:** `[1, 2, 3]` → `[[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]`

**Time Complexity: O(n · 2^n)**
- Number of subsets: **2^n** (each element: include or exclude)
- Each subset costs O(n) to copy
- Total: **O(n · 2^n)**

**Space:** O(n) recursion depth

---

## **2. Subsets II (with duplicates)**
**Problem:** Generate all unique subsets when input has duplicates

**Example:** `[1, 2, 2]` → `[[], [1], [2], [1,2], [2,2], [1,2,2]]`

**Time Complexity: O(n · 2^n)**
- Still generates at most 2^n subsets (duplicates are skipped)
- Sorting: O(n log n)
- Total: **O(n · 2^n)** (dominates sorting)

**Space:** O(n)

**Code pattern:**
```python
nums.sort()  # O(n log n)
if idx != start_idx and nums[idx] == nums[idx-1]:
    continue  # skip duplicates
```

---

## **3. Permutations**
**Problem:** Generate all orderings of n distinct elements

**Example:** `[1, 2, 3]` → 6 permutations

**Time Complexity: O(n · n!)**
- Number of permutations: **n!**
  - Level 1: n choices
  - Level 2: (n-1) choices
  - Level 3: (n-2) choices
  - Total: n × (n-1) × ... × 1 = **n!**
- Each permutation costs O(n) to copy
- Total: **O(n · n!)**

**Space:** O(n)

**Tree nodes:** 1 + n + n(n-1) + ... + n! ≈ **O(n!)**

---

## **4. Permutations II (with duplicates)**
**Problem:** Generate unique permutations when input has duplicates

**Example:** `[1, 1, 2]` → 3 unique permutations instead of 6

**Time Complexity: O(n · n!)**
- Worst case still explores n! paths (with pruning)
- Practically fewer due to duplicate skipping
- Still bounded by **O(n · n!)**

**Space:** O(n)

---

## **5. Combinations (choose k from n)**
**Problem:** Choose k elements from n elements

**Example:** `C(4, 2)` → `[[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]`

**Time Complexity: O(k · C(n, k))**
- Number of combinations: **C(n, k) = n! / (k! · (n-k)!)**
- Each combination costs O(k) to copy
- Total: **O(k · C(n, k))**

**Simplified bounds:**
- C(n, k) ≤ 2^n
- So also **O(k · 2^n)** upper bound

**Space:** O(k) recursion depth

---

## **6. Combination Sum (unlimited repetition, target)**
**Problem:** Find combinations that sum to target (reuse allowed)

**Example:** `candidates=[2,3,6,7], target=7` → `[[2,2,3], [7]]`

**Time Complexity: O(n^(t/m))**
- `t` = target value
- `m` = minimum candidate value
- `n` = number of candidates
- Max depth: t/m (using smallest number repeatedly)
- Each level branches up to n ways
- Total nodes: **O(n^(t/m))**

**Alternative notation:** O(n^t) where t relates to target

**Space:** O(t/m) recursion depth

---

## **7. Combination Sum II (no repetition, target)**
**Problem:** Find combinations that sum to target (each element used once)

**Example:** `candidates=[10,1,2,7,6,1,5], target=8`

**Time Complexity: O(2^n)**
- Each element: include or skip (binary choice)
- Generates subsets filtered by sum = target
- Total: **O(2^n)**

**With copy cost: O(n · 2^n)**

**Space:** O(n)

---

## **8. N-Queens**
**Problem:** Place n queens on n×n board (no attacks)

**Time Complexity: O(n!)**
- Row 1: n positions
- Row 2: < n positions (some attacked)
- Row 3: even fewer
- Roughly: **O(n!)** (actually tighter, but n! is common bound)

**More precise:** O(n!) but with heavy pruning

**Space:** O(n)

---

## **9. Sudoku Solver**
**Problem:** Fill 9×9 grid with constraints

**Time Complexity: O(9^m)**
- `m` = number of empty cells (up to 81)
- Each cell: try digits 1-9
- Worst case: **O(9^m)** ≈ **O(9^81)** (astronomical!)
- Heavy pruning in practice

**Space:** O(m) recursion depth

---

## **10. Word Search (2D grid)**
**Problem:** Find if word exists in grid

**Time Complexity: O(N · 4^L)**
- `N` = number of cells in grid
- `L` = length of word
- Try starting from each cell: O(N)
- From each cell, 4 directions, depth L: O(4^L)
- Total: **O(N · 4^L)**

**Space:** O(L) recursion depth

---

## **Summary Table:**

| Problem Type | Time Complexity | # Solutions | Key Factor |
|-------------|----------------|-------------|------------|
| Subsets | O(n · 2^n) | 2^n | Binary choice per element |
| Permutations | O(n · n!) | n! | All orderings |
| Combinations C(n,k) | O(k · C(n,k)) | C(n,k) | Choose k from n |
| Combination Sum (repeat) | O(n^(t/m)) | varies | Target-driven, repetition |
| Combination Sum II (no repeat) | O(2^n) | ≤ 2^n | Subset-like |
| N-Queens | O(n!) | varies | Constrained permutation |
| Sudoku | O(9^m) | 1 or 0 | Constraint satisfaction |

---

**General Pattern:**
- **Copy cost:** If you copy lists of size k, multiply by O(k)
- **Pruning:** Reduces practical runtime but usually doesn't change worst-case Big-O
- **Memoization:** Can dramatically reduce complexity (DP territory)

Hope this helps! 🚀
