---
layout: default
title: Summary
parent: Machine Learning
mathjax: true
mermaid: true
---

<div class="mermaid">
classDiagram
      Machine Learning --|> Supervised
      Machine Learning --|> Unsupervised
      Supervised --|> Classification
      Supervised --|> Regression
      Unsupervised --|> Clustering
      Unsupervised --|> Association Rule Mining
</div>

### Machine Learning

- **Supervised** - Labels known
- **Unsupervised** - Labels and classed unknown
- **Classification** - Classify into discrete classes
- **Regression** - Find a continuous value
- **Clustering** - Grouping similar objects together
- **Association Rule Mining** - Finding patterns, mostly in streaming data

### Measuring Dispersion

- **Range** - Difference of largest and smallest value
- **Quartiles** - 3 values which divide the data into 4 parts
- **Inter quartile range** - Range of 4 quartiles separately
- **Five number summary of data** - [ *Min, Q<sub>1</sub>, Q<sub>2</sub>,
  Q<sub>3</sub>, Max* ]
- **Standard deviation** - Average of absolute deviation of all data-points from
  $$
  σ = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i-x̄)^2}
  $$
- **Variance** - Yet another measure of deviation, square of standard deviation
  σ<sup>2</sup>
- **Mean** - Average
- **Median** - Middle value(s) in sorted data
- **Mode** - Most frequent observation

### Statistics

- **Population** - All data-points under study in an statistical operation
- **Sample** - Small part of population to collect information

### Knowing the data

- **Attributes** - Properties that define a data point
  - **Nominal attributes** - Regarding names
  - **Binary attributes** - Meh
  - **Ordinal attributes** - Representing rank or order of data-points among
    themselves
  - **Numeric attributes** - Duh
  - **Interval scaled attributes** - Values are located at equal intervals and
    may be ranked
  - **Ratio scaled attributes** - When values are represented as comparison to
    other values
- **Reading box-plot**
  ![img](https://www.statisticshowto.com/wp-content/uploads/2009/08/boxplot4.png)
- **Properties of dataset**
  - Dimensionality - Number of attributes a dataset possesses
  - Sparsity - The degree of presence of null values in a dataset
  - Resolution -

### Measuring Performance

<table>
<thead>
  <tr>
      <th colspan="2" rowspan="2"><span><h3>Confusion Matrix</h3></span></th>
    <th colspan="2">Predicted Class</th>
  </tr>
  <tr>
    <th>True</th>
    <th>False</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">Actual Class</td>
    <td><span>True</span></td>
    <td>TP</td>
    <td>FN / Type 2</td>
  </tr>
  <tr>
    <td>False</td>
    <td>FP / Type 1</td>
    <td>TN</td>
  </tr>
</tbody>
</table>

- **Accuracy** - Overall correctness of classifier

  $$
  \frac{TP+TN}{TP+TN+FP+FN}
  $$

- **Error rate** - Misclassification rate

  $$
  \frac{FP+FN}{TP+TN+FP+FN}
  $$

- **True positive rate** - When "YES" was right

  $$
  \frac{TP}{TP+FN}
  $$

  $$
  \frac{TP}{Positives}
  $$

- **True negative rate / Specificity** - When "NO" was right

  $$
  \frac{TN}{TN+FP}
  $$

  $$
  \frac{TN}{Negatives}
  $$

- **False positive rate**

  $$
  \frac{FP}{TP+TN+FP+FN}
  $$

- **Precision** - How many times it was right when it said "YES"

  $$
  \frac{TP}{TP+FP}
  $$

  $$
  \frac{TP}{Yes_{predicted}}
  $$

- **Sensitivity**

  $$
  \frac{TP}{TP+FN}
  $$

- **Recall**

  $$
  \frac{TP}{TP+FN}
  $$

- **Prevalence** - How many times "_YES_" condition occurs in sample

  $$
  \frac{TP+FN}{TP+TN+FP+FN}
  $$

### Correlation

Degree of similarity between the values

- Direct method

$$
r(x,y) = \sqrt{\frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{\sum_{i=1}^{n}(x_i-\bar{x})^2\sum_{i=1}^{n}(y_i-\bar{y})^2}}
$$

- Shortcut method

$$
r(x,y) = \frac{\sum{x_iy_i-n\bar{x}\bar{y}}}{\sqrt{(\sum{x_i^2}-n\bar{x}^2)(\sum{y_i^2}-n\bar{y}^2)}}
$$

### Matthews' correlation coefficient

- Brian W. Matthews - 1975

It is used to measure the quality of binary class classification. It considers
the Confusion Matrix and provides a measure even if the classes are not balanced
in size.

$$
MCC = \frac{TP\times{TN}-FP\times{FN}}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}
$$

- **Lazy Learners:** Store the training data and wait until the testing data
  appear. Take less time in training but more in prediction.

  Ex. KNN, Case Based Learning

- **Eager Learners:** Construct a classification model based on given training
  data, before receiving testing data.

### Regression

- Regression means stepping back towards the average/Finding strength of
  relationship between two variables

- **Regression analysis** - Modeling relation between one or more variables, the
  target label being continuous valued

- **Types of regression techniques**

  - Linear regression
  - Logistic regression
  - Polynomial regression
  - Lasso regression
  - Redge regression
  - Elastic regression
  - Stepwise regression

- **Linear regression using least squares method**

  - Calculate mean of X and Y values

  - Slope of the line for best fit:

$$
m = \frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{\sum_{i=1}^{n}(x_i-\bar{x})^2}
$$

- Calculate intercept as:

$$
c = \bar{y}-m\bar{x}
$$

- Use **m** and **c** to put up the line

- **Multiple linear regression**

  - When we formulate the X value as a tuple of values, so we predict a single
    value using a number of values

- **Non-linear regression**

  - When the data-points do not follow a straight line, we try moving to a
    higher degree and fit a curve

- **Logistic regression**

  - Making prediction for a binary dependent variable where linear relation
    between independent values is not required
  - In general, the output of a linear model is put into a sigmoid function that
    produces binary output
  - It makes use of probability of events in a bivariate environment to produce
    a binary output

- **Performance parameters for regression**

  - Correlation
  - Root Mean Square - Root of Mean of Square of Errors
  - Coefficient of determinant - The degree of correlation between X and Y
    values (How much the y value changed on change in X value)
  - Accuracy - Percentage of deviation of predicted target from actual values

### Dissimilarity in data

- **Numeric data**

  - Cosine similarity

    - A measure of the cosine between the two vectors in a multidimensional
      space

$$
\cos\theta=\frac{\vec{a}.\vec{b}}{\|\vec{a}\|\|\vec{b}\|} =
\frac{\sum_{1}^{n}a_ib_i}{\sqrt{\sum_{1}^{n}a_i^2}\sqrt{\sum_{1}^{n}b_i^2}}
$$

- Minkowski distance

  $$
  D = (\sum_{i = 1}^{n}\|X_i-Y_i\|^p)^{1/p}
  $$

  - for p = 1, D = _Manhattan distance_
  - for p = 2, D = _Euclidean distance_

- Pearson's correlation coefficient

  - A measure of correlation for both numeric as well as binary data

  - Ranges from -1 to 1

    $$
    corr(x,y)=\frac{covariance(x,y)}{\sigma(x)\times\sigma(y)}
    $$

$$
covariance = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})
$$

- **Binary data**

  - Use coefficients to determine similarity of binary attributes. Coefficient
    can range anywhere from 0 to 1 where 0 represents no similarity and 1
    represents complete similarity

  - Simple Matching Coefficient

    $$
    SMC = \frac{matching}{total}
    $$

    $$
    SMC = \frac{f_{11}+f_{00}}{f_{01}+f_{00}+f_{11}+f_{11}}
    $$

  - Jaccard coefficient

    $$
    J = \frac{f_{11}}{f_{01}+f_{10}+f_{11}}
    $$

### Naive Bayes classifier <sub><sub>Thomas Bayes - 1973</sub> </sub>

For n disjoint sets E<sub>1</sub>,E<sub>2</sub>,E<sub>3</sub>....E<sub>n</sub>

$$
P(\frac{E_i}{A})=\frac{P(E_i).P(\frac{A}{E_i})}{P(A)}
$$

- P(E<sub>1</sub>), P(E<sub>2</sub>)... are prior probabilities as they are
  provided beforehand

- P(A|E<sub>i</sub>) is the likelihood probability as it represents the
  likeliness of one event occurring after another

- P(E<sub>i</sub>|A) are posterior probabilities as they are determined after
  result of experiment

**Bayes Classification Method**

Used for class membership problem i.e. "_What is the probability of an item
belonging to a class_ ?". As per the Bayes' theorem, we assume that one class
does not affect the other. Since it is made to simplify the calculations, we
call it "_Naive_". The results are comparable to decision trees and Neural
Network classifiers in some cases.

It determines an element belonging to a class if P(C<sub>i</sub>|X) >
P(C<sub>j</sub>|X), so we maximize P(C<sub>i</sub>|X). The class for which
P(C<sub>i</sub>|X) is maximized is called as _maximum posterior hypothesis_.

$$
P(C_i|X)=\frac{P(X|C_i)P(C_i)}{P(X)}
$$

---

### Support Vector Machine

Used for classification on both linear and non linear data, for classification
as well as numerical prediction. It uses non linear mapping for mapping data to
a higher dimension, where we search for a linear solution and is mapped back to
original dimension.

Procedure:

- Write the separating hyperplane as $w.x +b = 0$, where w is the weight vector.
- Write the equation as $w_0 + w_1x_1 + w_2x_2 + ... = 0$
- Find an equation such that for one class $w_0 + w_1x_1 + w_2x_2 + ... > 0$ and
  for another $w_0 + w_1x_1 + w_2x_2 + ... < 0$

### Principal Component Analysis

...

### K Nearest Neighbors

Classification based on analogy. Comparing a single test tuple with the training
tuples, similar to it. All training tuples are stored in an n-dimensional space.
Whenever testing tuple arrives, it is compared to the pattern in space. The
closeness to the tuples is defined in terms of euclidean distance or any other
suitable metrics. It is a lazy learning algorithm that creates a model once the
testing data arrives. It is _non parametric_, meaning we do not make assumptions
about underlying data.

- **Procedure:**

  - Divide data into k sets
  - Find mean to all sets
  - Minimize the distance of all points to all means iteratively until the
    points do not move

- **Pros:**

  - Easy to understand
  - No assumptions about data
  - Can both classify or calculate
  - Works easily on multi-class problems

- **Cons:**

  - Memory intensive
  - Sensitive to scale of data
  - Struggles with multi valued training data

**Modified KNN**

- Instead of making a distance based on majority, we make use of the weights,
  hence calculating weighted majority, so that outliers have less effect on the
  classification.

---

### Clustering

Differentiating points into groups based on similarity. Various clustering
methods are:

<table>
<thead>
  <tr>
    <th>Method</th>
    <th>Characteristics</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Partition method</td>
    <td>
    - Find mutually exclusive clusters of spherical shape<br>
    - Distance based<br>
    - Make use of mean/median or similar measures<br>
    - Effective use of small to medium sized data</td>
  </tr>
  <tr>
    <td>Hierarchical method</td>
    <td>
    - Multiple level decomposition<br>
    - Incorporate other techniques like microclustering
    </td>
  </tr>
  <tr>
    <td>Density based method</td>
    <td>
    - Can find arbitrary shaped clusters<br>
    - Low density regions seperate clusters<br>
    - Each point must have a minimum number of points within the neighborhood<br>
    - May filter outliers</td>
  </tr>
  <tr>
    <td>Grid based method</td>
    <td>
      - Use a multiresolution grid data structure<br>
      - Fast to process
    </td>
  </tr>
</tbody>
</table>

**Requirements for cluster analysis:**

- Scalability
- Ability to deal with arbitrary shape
- Domain knowledge
- Dealing with noisy data
- Insensitivity to input order
- Interpret-ability and usability

### Decision trees

A flowchart that represents flow of tests on training data and the outcome, leaf
nodes being the classes to predict.

**Example:** Should I go out or not

<div class="mermaid">
graph TD
    A[Weather] -->|Sunny|B(Humidity)
    B -->|High|E([No])
    B -->|Low|F([Yes])
    A -->|Cloudy|C([Yes])
    A -->|Rainy|D(Wind)
    D -->|Strong|G([No])
    D -->|Weak|H([yes])
</div>

Types of decision trees:

- Categorical variable decision tree
- Continuous variable decision tree

**Pruning** - Instead of making more splits, we converge sub-nodes of a tree to
make it less dense and less complex. It can be attained via both top-down or
bottom-up approach.

**Hold out method and random sub-sampling**

Given data is partitioned into 2 independent datasets. One set is used to train
data and other for testing. Random sub-sampling means the above process is
carried out k times and overall accuracy is the average of k operations.

**Cross validation**

Divide initial data into k mutually exclusive subsets called as "_Folds_".
Reserve one fold for testing and rest for training. Repeat the steps k times for
k folds, and get the average of the accuracy.

**Leave one out** is a special case for the k-fold cross validation where k is
the set to the number of initial tuples and one sample is left out at a time for
test.

In **stratified cross validation**, the folds are made such that the class
distribution is balanced among the folds.

### Ensemble methods

When a model is made out of composition of different models. Bagging and
Boosting are common ensemble methods.

**Bagging** : This ensemble accounts for the majority votes given by the base
classifiers to produce the final result. Ex. Random forest

**Boosting** : Every base classifier is assigned a weight and its vote is
accounted for according to the weight. Ex. AdaBoost

### Apriori algorithm

Finding frequent item sets by combined candidate generation.Name of the
algorithm is Apriori because it uses prior knowledge of frequent itemset
properties. We apply an iterative approach or level-wise search where k-frequent
itemsets are used to find k+1 itemsets.

**Apriori Property :** All subsets of a frequent itemset must be
frequent(Apriori propertry). If an itemset is infrequent, all its supersets will
be infrequent.

### Neural Networks

Equivalent of biological neural system, just meant for use with computers.

**Model of a neuron :**

![perceptron node](https://wiki.pathmind.com/images/wiki/perceptron_node.png)

Every input has a _weight_ assigned to it that is passed to a computer function
and to the activation function that calculates the output. We may add bias to a
node to allow activation function to shift and fit on the data better.

The Σ produces an output as $w_1x_1+w_2x_2 + ... + w_nx_n$, which is then passed
to a non-linear function called _activation function_. Introducing non-linearity
is mandatory else the network may not learn at all over any number of layers.
Various functions used are:

- Sigmoid
- Signum
- Hyperbolic tangent
- Rectified Linear Unit (ReLU)

**Neural Net Architecture**

A network typically consists of an input layer having nodes depending upon the
input size, hidden layers and the output layer depending upon the number/type of
output to be produces.

![](https://www.pikpng.com/pngl/b/473-4732722_neural-network-png.png)

**Types of neural networks :**

- Single layer feed forward network - 2 layers (input and output)

- Multi layer feed forward network - Many layers between input and output

- Recurrent network - Contain feedback loops, which allow working on serialized
  data.

**Convolution Neural Networks :**

ANNs specialized to work on images. Other than fully connected layers, they
contain:

- **Convolution layer : ** Apply filters on the image kernel by kernel (kernel
  is a sub-matrix of pixels in the image).
- **Pooling layer : ** Reduce the spatial size of representation to reduce the
  amount of parameters in computation.
  - Average pooling (Find average in a kernel)
  - Min pooling (Find minimum in the kernel)
  - Max pooling (Find maximum in the kernel)

**Other terms related to Neural Networks :**

- **Back-propagation** : NN predicts some output that is compared to the real
  value. An error is calculated , and the error value is "back-propagated" into
  the network to adjust the weights to get better output.
- **Batch Size** : Portion of data worked upon at a time
- **Epoch** - Number of passes of the entire training dataset
- **Filter** : A matrix that is meant to spot specific features in an image.

**Layers in a neural network :**

- **Dense/Fully connected layer** - When all nodes in current layer are
  connected to all layers in previous nodes.
- **Convolution layer** - Applies filter to image
- **Pooling layer** - Gets important features from image
- **Dropout layer** - Randomly sets input units to 0 with a frequency of rate at
  each step during training time, which helps prevent overfitting.
- **Batch-norm layer** - Standardizes the inputs to a layer for each mini-batch.
  This has the effect of stabilizing the learning process and dramatically
  reducing the number of training epochs

# Classification

## data mining

- means digging deep into data that is in different forms to gain patterns
- and to gain knowledge on that pattern

### types

- predictive
  - classification
  - regression
  - time series analysis
  - prediction
- descriptive
- clustering
- summarization
- association rules
- sequence discovery

## classification

- data analysis task
- finding a model that distinguishes data classes and concepts
- problem os identifying to which od set of categories a new observation belongs
  to

### steps

- learning step
- classification step

### attributes

- represents features of an object
- binary
  - true or false
  - can be symmetric (both values are important), asymmetric (both values may
    not be important)
- nominal
  - more than two possible outcomes
  - ordinal - values order have sense
  - continuous - infinite no of values
  - discrete - finite no of values

## math

- classification is based on building a function
- taking input feature vector $X$ and
- predicting its outcome $Y$

## major types of classifiers

- Discriminative
  - it determines just one class for each row
  - it tries to model just by depending on the observed data
  - depends heavily on the quality of data rather than on distribution
  - e.g. `logistic regression`
- Generative
  - models the distribution of individual classes and tries to learn the model
    tha generates the data behind the scenes by estimating assumptions and
    distributions of the model
  - e.g. `naive bayes classifier`

## ML Classifiers

- decision trees
- bayesian classifiers
- neural networks
- k-nearest neighbor
- support vector machines
