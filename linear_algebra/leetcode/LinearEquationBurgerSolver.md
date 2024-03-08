# Problem Statement

Given two integers `tomatoSlices` and `cheeseSlices`. The ingredients for different burgers are as follows:

- **Jumbo Burger**: 4 tomato slices and 1 cheese slice.
- **Small Burger**: 2 tomato slices and 1 cheese slice.

The goal is to return a list `[total_jumbo, total_small]` such that the number of remaining `tomatoSlices` equals 0 and the number of remaining `cheeseSlices` equals 0. If it is not possible to achieve this, return an empty list `[]`.

## Solution Approach

The problem can be modeled as a system of linear equations:

1. For the Jumbo and Small burgers, the total tomato slices used is `4*total_jumbo + 2*total_small = tomatoSlices`.
2. For the cheese slices, the total used is `total_jumbo + total_small = cheeseSlices`.

These equations can be represented in matrix form as:

```python
a = np.array([[4, 2], [1, 1]])
b = np.array([tomatoSlices, cheeseSlices])
```

Where a represents the coefficients of the system of equations, and b represents the right-hand side values derived from the input.

To solve this system, we can use the numpy.linalg.solve() method:

```python
import numpy as np

class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        a = np.array([[4, 2], [1, 1]])
        b = np.array([tomatoSlices, cheeseSlices])
        try:
            x = np.linalg.solve(a, b)
            # Check if the solution consists of non-negative integers
            if all(i.is_integer() and i >= 0 for i in x):
                return [int(x[0]), int(x[1])]
            else:
                return []  # Return an empty list if conditions are not met
        except np.linalg.LinAlgError:
            return []  # In case the system of equations is singular
```