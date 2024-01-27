# Decision Tree Implementation

[Here](./decision_tree_basic_pure_py.ipynb) is the basic implementation of a decision tree classifier in Python.

## Key Features

- **Pure Python:** The implementation is written in pure Python without external libraries, making it easy to understand and modify.
- **Brute Force Approach:** The tree building process uses a brute force approach to find the best split at each node, exploring all possible splits based on information gain.
- **Recursive Structure:** The code employs recursion to create the tree structure, making it concise and elegant.

## Workflow

**1. Building the Tree:**

- **Recursive Function `build_tree(rows, header)`:**
  - Base Case:
    - If information gain is 0 (no further meaningful splits), create a `Leaf` node with majority class prediction.
  - Otherwise:
    - Find the best question to split the data using `find_best_split(rows, header)`.
    - Partition the data into true and false branches based on the question.
    - Recursively build subtrees for both branches.
    - Construct a `DecisionNode` with the question, true branch, and false branch.

**2. Making Predictions:**

- **Function `classify(row, node)`:**
  - Base Case:
    - If a `Leaf` node is reached, return its predictions.
  - Otherwise:
    - Evaluate the `Question` at the current node.
    - Recursively classify the row based on the answer (true or false branch).