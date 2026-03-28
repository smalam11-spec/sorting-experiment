import time
import random
import sys

# Increase recursion depth for Quick Sort on very large or sorted lists
sys.setrecursionlimit(10000)

# PLAYER 1: BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# PLAYER 2: QUICK SORT
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# ---------------------------------------------------- PHASE 0: SMALL DATA (Required: 20, 30, 50) ---
# For small lists, we must sort many (10,000 times) to get a real time measurement.

small_size = 30
repeats = 10000
print(f"--- PHASE 0: SMALL DATA (Size: {small_size}, Repeated {repeats}x) ---")

start = time.time()
for _ in range(repeats):
    test_data = [random.randint(0, 100) for _ in range(small_size)]
    bubble_sort(test_data)
print(f"Bubble Sort (Total for 10k runs): {time.time() - start:.4f}s")

start = time.time()
for _ in range(repeats):
    test_data = [random.randint(0, 100) for _ in range(small_size)]
    quick_sort(test_data)
print(f"Quick Sort  (Total for 10k runs): {time.time() - start:.4f}s")


# ---------------------------------------------------- PHASE 1: THE ORIGINAL EXPERIMENT ---
print(f"\n--- PHASE 1: MEDIUM RANDOM DATA (Size: 2000) ---")
data = [random.randint(0, 10000) for _ in range(2000)]

# Time Bubble Sort
start = time.time()
bubble_sort(data.copy())
print(f"Bubble Sort: {time.time() - start:.4f} seconds")

# Time Quick Sort
start = time.time()
quick_sort(data.copy())
print(f"Quick Sort:  {time.time() - start:.4f} seconds")


# ---------------------------------------------------- PHASE 2: STRUCTURED DATA ---
size = 2000
data_sorted = list(range(size))
data_reverse = list(range(size, 0, -1))

print(f"\n--- PHASE 2: STRUCTURED DATA (Size: {size}) ---")

# Testing Quick Sort on Already Sorted Data
start = time.time()
quick_sort(data_sorted.copy())
print(f"Quick Sort (Already Sorted): {time.time() - start:.4f}s")

# Testing Quick Sort on Reverse Sorted Data
start = time.time()
quick_sort(data_reverse.copy())
print(f"Quick Sort (Reverse):        {time.time() - start:.4f}s")


# ---------------------------------------------------- PHASE 3: TRICKY DATA & STRINGS ---
print(f"\n--- PHASE 3: TRICKY DATA & STRINGS (Size: {size}) ---")

# 1. Almost Sorted (98% of the list is already in order)
data_almost = list(range(size))
for _ in range(int(size * 0.02)): 
    idx1, idx2 = random.randint(0, size-1), random.randint(0, size-1)
    data_almost[idx1], data_almost[idx2] = data_almost[idx2], data_almost[idx1]

# 2. Flat List (A long list with only 0s and 1s)
data_flat = [random.choice([0, 1]) for _ in range(size)]

# 3. String Data (Sorting words instead of numbers)
data_strings = ["apple", "zebra", "banana", "mango", "cherry"] * (size // 5)

# Testing on Almost Sorted
start = time.time()
quick_sort(data_almost.copy())
print(f"Quick Sort (Almost Sorted): {time.time() - start:.4f}s")

# Testing on Flat List (Duplicates)
start = time.time()
quick_sort(data_flat.copy())
print(f"Quick Sort (Flat List):      {time.time() - start:.4f}s")

# Testing on Strings
start = time.time()
quick_sort(data_strings.copy())
print(f"Quick Sort (Strings):        {time.time() - start:.4f}s")


# ---------------------------------------------------- PHASE 4: LARGE DATA (Quick Sort Only) ---
# Bubble Sort would take way too long here, so we only test Quick Sort.
large_size = 100000
print(f"\n--- PHASE 4: LARGE DATA (Size: {large_size}) ---")

large_data = [random.randint(0, 100000) for _ in range(large_size)]

start = time.time()
quick_sort(large_data)
print(f"Quick Sort (Large 100k): {time.time() - start:.4f}s")
import collections

# ---------------------------------------------------- PHASE 5: DIFFERENT DATA TYPES & TOOLS ---
print(f"\n--- PHASE 5: DATA TYPES & ALTERNATIVE TOOLS (Size: {size}) ---")

# 1. Testing on a Linked-List-like structure (deque)
data_deque = collections.deque(data.copy())
start = time.time()
# Note: Quick sort works on lists, so we convert it to show the overhead
sorted_deque = quick_sort(list(data_deque))
print(f"Quick Sort (on Deque/Linked Structure): {time.time() - start:.4f}s")

# 2. Testing Python's Built-in 'Stream-like' Sort (Timsort)
# This is what professional developers actually use!
start = time.time()
data_copy = data.copy()
data_copy.sort() # This is optimized C-code
print(f"Python Built-in (Optimized Stream):    {time.time() - start:.4f}s")
