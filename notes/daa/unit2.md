---
layout: default
title: Unit II
parent: Design and Analysis of Algorithms
mathjax: true
mermaid: true
---

# Unit II

- Sorting Algorithms Sorting 
  - Bubble sort, 
  - Insertion sort, 
  - selection sort, 
  - quick sort, 
  - randomized quick sort, 
  - merge sort, 
  - heap sort, 
  - counting sort, 
  - External sorting 
- Divide sorting algorithms into following types
  - online sort, 
  - stable sort, 
  - in place sort, 
  - Comparison of sorting algorithms on the basis of number of swaps, by number of comparisons, 
  - recursive or iterative nature, 
  - time and space complexity

## Sorting

- arranging in some order particular order is called sorting.

### Bubble sort

- it bubbles up one value at a time

**algo:**

```c
void bubble_sort(int *arr, int n){
  for(int i=0; i<n; i++){
    for(int j=0; j<n-1-i ; j++){
      if(arr[j] > arr[j+1]){
        // swap
        int temp=arr[j];
        arr[j]=arr[j+1];
        arr[j+1] =temp;
      }
    }
  }
}
```

