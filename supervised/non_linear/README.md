## Linear separability

A dataset is linearly separable if and only if there exists a separating hyperplane:

- $\exists$ w such that:
  - $w_0 + \sum_{i=1}^{n} w_i x_i > 0$ if $x=\{x_1, \ldots, x_n\}$ is a positive example
  - $w_0 + \sum_{i=1}^{n} w_i x_i < 0$ if $x=\{x_1, \ldots, x_n\}$ is a negative example
  
  
  
The goal of learning in linear classifiers, including perceptron, support vector machines, and logistic regression, is to find appropriate values for the parameters $w_0$ and $w_i$ that best suit the characteristics of the given dataset. Specifically:

Perceptron and Support Vector Machines (SVMs): The objective is to find values for 
$w_0$ and $w_i$ that define a hyperplane separating different classes, and this separation is achieved by maximizing the margin or correctly classifying examples.

Logistic Regression: The objective is to find values for 
$w_0$ and $w_i$ that maximize the likelihood of the observed data. In logistic regression, these parameters are used to model the probability of an example belonging to a particular class.

**But some datasets are not linearly separable**
It's common for real-world datasets not to be perfectly linearly separable. This means you can't draw a straight line (or flat plane in higher dimensions) to perfectly divide the data points into distinct classes.
To handle such cases, we need techniques that can capture more complex decision boundaries.


## Addressing Non-Linearly separable data 
### Option 1: Non-Linear features
- This approach involves crafting new features from existing ones, using non-linear transformations.
- This can effectively increases the dimensionality of the data and potentially make it linearly separable in the new, higher-dimensional space.
#### Examples of Non-Linear Features:
- **Polynomial features**: Expanding the feature space by including the squared terms, interaction terms, or even higher-degree terms. For example, adding quadratic terms $(x_i^2)$ can create curved decision boundaries.
- **Kernel features**: Using functions like Gaussian Radial Basis Functions (RBF) or polynomial kernels to map data points into a higher-dimensional space where linear separation is more likely.
#### Classifier remains similar:
- Even though the features are non-linear, the actual classification model $(h_w(x))$ still maintains a linear form in terms of the parameters $(w)$.
This means we can still use linear classification algorithms like linear SVMs, logistic regression to learn the model.

#### Advantages
- **Easy to learn**: Linear models are generally easier to train and computationally efficient.
- **Transforms Data**: Non linear features can create more complex decision boundaries, making them suitable for wide range of problems.

#### Caution
- Using non-linear features can increase model complexity and the risk of overfitting. It's important to carefully select and tune the features to avoid these issues.


### Option 2: Non-Linear Classifier Models
- Instead of transforming the features, this approach employs classifiers that inherently non-linear in their parameters.
- Examples: **Decision Trees**, **Neural Networks**, **Support Vector Machines with Non-Linear Kernels (e.g., Gaussian RBF Kernel)**

#### Advantages:
- Generality: Can capture a wider range of complex decision boundaries and handle any type of non-linear separability.
- Model flexibility: Offers greater flexibility in representing intricate relationships between features and the target variable, potentially leading to higher accuracy for complex problems.
- No feature engineering (potentially): Depending on the chosen classifier, you might not need to manually craft non-linear features, simplifying the preprocessing stage.

#### Challenges:
- **Training difficulty**: Learning algorithms for non-linear classifiers often involve non-convex optimization, which can be computationally challenging and prone to getting stuck in local optima.
- **Overfitting risk**: Non-linear models can overfit the training data if not properly regularized.

Option 1: Non-Linear features with a linear model
Ideal for: Situations where ease of training and interpretability are prioritized.
Option 2: Fully Non-Linear Models
Ideal for: Situations where utmost flexibility and accuracy are crucial, even if it comes at the expense of harder training and reduced interpretability.

Choosing the optimal approach depends on the specific characteristics of your dataset, problem complexity, and desired trade-offs between simplicity, flexibility, and accuracy.