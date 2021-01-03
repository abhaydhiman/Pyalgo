# Count minimum steps to get the given desired array

## Consider an array with n elements and value of all the elements is zero. We can perform following operations on the array

1. Incremental operations:Choose 1 element from the array and increment its value by 1.
2. Doubling operation: Double the values of all the elements of array.

## We are given desired array target[] containing n elements. Compute and return the smallest possible number of the operations needed to change the array from all zeros to desired array

```txt
Examples:

Input: target[] = {2, 3}
Output: 4
To get the target array from {0, 0}, we 
first increment both elements by 1 (2 
operations), then double the array (1 
operation). Finally increment second
element (1 more operation)

Input: target[] = {2, 1}
Output: 3
One of the optimal solution is to apply the 
incremental operation 2 times to first and 
once on second element.
```

https://www.geeksforgeeks.org/count-minimum-steps-get-given-desired-array/
