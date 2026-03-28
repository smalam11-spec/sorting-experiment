# Sorting Algorithm Experiment Results

## 1. Summary of Results
* **Small/Medium Data (Size 2000):** Quick Sort consistently finished in under 0.01 seconds.
* **Large Data (Size 100,000):** Quick Sort took 0.2847s. Bubble Sort was skipped for this size because it would take significantly longer (likely several minutes).
* **Tricky Data:** Quick Sort handled "Flat Lists" (duplicates) extremely well (0.0002s) because of the way the middle pivot was chosen.

## 2. Analysis & Expectations
### Did the results match expectations?
**Yes.** As expected, Quick Sort ($O(n \log n)$) outperformed Bubble Sort ($O(n^2)$) in every category. 

### Key Observations:
1. **The "Almost Sorted" Case:** Quick Sort took 0.0123s, which was actually slower than the "Flat List." This happens because even small disorders require the algorithm to perform many recursions.
2. **Linked Structures vs Lists:** Sorting the Deque (Linked Structure) took 0.0021s. The extra time compared to a standard list is due to the overhead of converting the data structure.
3. **The Winner:** The "Python Built-in" (Timsort) was the fastest of all (0.0002s). This is because it is written in C and is highly optimized for real-world data.

## 3. Conclusion
Quick Sort is a highly efficient "Divide and Conquer" algorithm. While Bubble Sort is easy to write, it is not practical for any data size above a few hundred elements. For professional use, built-in library functions are superior.