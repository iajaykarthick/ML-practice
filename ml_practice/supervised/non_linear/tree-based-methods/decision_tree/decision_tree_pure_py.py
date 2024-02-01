
# This is a pure python implementation of a decision tree classifier.
def unique_vals(rows, col):
    return set([row[col] for row in rows])


def class_counts(rows, class_index=-1):
    counts = {}
    
    for row in rows:
        label = row[class_index]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts


def is_numeric(value):
    return isinstance(value, int) or isinstance(value, float)


class Question:
    def __init__(self, column, value, header):
        self.column = column
        self.value = value
        self.header = header
        
    def match(self, example):
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value
        
    def __repr__(self):
        condition = "=="
        if is_numeric(self.value):
            condition = ">="
        return f"Is {self.header[self.column]} {condition} {str(self.value)}?"
    
    
def partition(rows, question):
    true_rows, false_rows = [], []
    
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows
    
    
    
def gini(rows):
    counts = class_counts(rows)
    impurity = 1
    for label in counts:
        prob_of_label = counts[label] / len(rows)
        impurity -= prob_of_label**2
    return impurity


def info_gain(left, right, current_uncertainity):
    p = len(left) / (len(left) + len(right))
    return current_uncertainity - (p * gini(left) + (1-p) * gini(right))


def find_best_split(rows, header):
    """Find the best question to ask by iterating over every feature / value and calculating the information gain."""
    best_gain = 0
    best_question = None
    current_uncertainity = gini(rows)
    n_features = len(rows[0]) - 1
    
    for col in range(n_features):
        values = set([row[col] for row in rows]) # Unique values in the column
        for val in values:
            question = Question(col, val, header)
            
            # try splitting the dataset
            true_rows, false_rows = partition(rows, question)
            
            # if it doesn't split the dataset, skip it
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue
            
            # calculate the information gain from this split
            gain = info_gain(true_rows, false_rows, current_uncertainity)
            
            if gain > best_gain:
                best_gain, best_question = gain, question
        
    return best_gain, best_question


class Leaf:
    def __init__(self, rows):       
        self.predictions = class_counts(rows)
        

class DecisionNode:
    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch
        

            
def build_tree(rows, header):
    print(f"Building tree... (len(rows) = {str(len(rows))}")
    
    # Try partitioning the dataset on each of the unique attributes, calculate the information gain, and return the question that produces the highest gain.
    gain, question = find_best_split(rows, header)
    
    # Base case: no further info gain; even the best info gain is 0, we can't split any further.
    # Since we can ask no further questions, we'll return a leaf.
    if gain == 0:
        print(f"Leaf node reached with {len(rows)} rows.")
        return Leaf(rows)
    
    # TODO: Negative gain? Even though find_best_split handles negative gain cases, should I check for precision errors?
    
    # If we reach here, we have found a useful feature / value to partition on.
    true_rows, false_rows = partition(rows, question)
    
    # Recursively build the true branch.
    print(f"Building true branch with {len(true_rows)} rows...")
    true_branch = build_tree(true_rows, header)
    
    # Recursively build the false branch.
    print(f"Building false branch with {len(false_rows)} rows...")
    false_branch = build_tree(false_rows, header)
    
    # Return a Question node.
    # This records the best feature / value to ask at this point, as well as the branches to follow depending on the answer.
    return DecisionNode(question, true_branch, false_branch)
    
    
    
    
def print_tree(node, spacing=""):
    """Prints the decision tree in an elegant format."""
    
    # Base case: if we have reached a leaf node
    if isinstance(node, Leaf):
        print(spacing + "Predict:", node.predictions)
        return
    
    # Print the question at this node
    print(spacing + str(node.question))
    
    # Print the branches
    print(spacing + '--> True:')
    print_tree(node.true_branch, spacing + "  ")
    
    print(spacing + '--> False:')
    print_tree(node.false_branch, spacing + "  ")



def classify(row, node):
    
    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        return node.predictions
    
    
    # Decide whether to follow the true-branch or the false-branch
    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)
    
    
    
def print_predictions(counts):
    total = sum(counts.values())
    probs = {}
    for label in counts.keys():
        probs[label] = str(int(counts[label]) * 100 / total) + "%"
        
    return probs