# Problem: Max Points on a Straight Line
[Leetcode](https://leetcode.com/problems/max-points-on-a-line/)

**Given**: A set of points in a 2D plane.

**Objective**: Determine if all given points lie on a single straight line.

# Solution Approach Using PCA

The solution leverages Principal Component Analysis (PCA) to determine if all points lie on a straight line. The steps involved in the PCA-based method are as follows:

1. **Create the Feature Matrix**: Organize the points into a matrix where each row represents a point.

2. **Mean Center the Matrix**: Subtract the mean of each column (feature) from all entries in that column to center the data around the origin.

3. **Compute the Covariance Matrix and Perform Eigen Decomposition**: Calculate the covariance matrix of the centered data and then find its eigenvectors and eigenvalues.

4. **Sort Eigenvectors by Eigenvalues**: Sort the eigenvectors in descending order based on their corresponding eigenvalues, identifying the principal components.

5. **Project Data onto the First Principal Component (PC1)**: Use the eigenvector associated with the largest eigenvalue to project the data points onto this principal direction.

6. **Reconstruct the Data from the Projection**: Use the projection along PC1 to reconstruct the original data points.

7. **Compare the Reconstructed Data with the Original Data**: Check if the reconstructed data points are close to the original ones using `np.allclose`, indicating that all points lie on the same line.

## Python Implementation

```python
import numpy as np

def on_same_line(points):
    # Step 1: Create the feature matrix with type float
    X = np.array(points, dtype=float)
    
    # Step 2: Mean center the matrix
    X_centered = X - np.mean(X, axis=0)
    
    # Step 3: Find the covariance matrix, its eigenvectors, and eigenvalues
    covariance_matrix = np.cov(X_centered.T)
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    
    # Step 4: Sort eigenvectors by eigenvalues in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    pc1 = eigenvectors[:, sorted_indices[0]]
    
    # Step 5: Project the data onto PC1
    projection = X_centered.dot(pc1)
    
    # Step 6: Reconstruct from PC1
    reconstruction = np.outer(projection, pc1)
    reconstructed_X = reconstruction + np.mean(X, axis=0)
    
    # Step 7: Compare reconstructed_X with X using np.allclose
    return np.allclose(reconstructed_X, X)
```

Note: This approach, while not the most efficient for the specific problem of determining if points are on a straight line, provides a novel application of PCA to validate the geometric alignment of points in 2D space.