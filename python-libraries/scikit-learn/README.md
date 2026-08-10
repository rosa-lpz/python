### Introduction to Scikit-learn

**Scikit-learn** is a popular Python library used for **machine learning and data analysis**. It provides simple tools for building, training, testing, and evaluating machine learning models.

It is especially useful for beginners because it provides ready-to-use algorithms and works well with libraries such as **NumPy, Pandas, and Matplotlib**.

### What can you do with Scikit-learn?

You can use Scikit-learn for:

* **Classification** – predicting categories, such as spam/not spam.
* **Regression** – predicting numbers, such as house prices.
* **Clustering** – grouping similar data, such as customer segments.
* **Dimensionality reduction** – reducing the number of features in a dataset.
* **Data preprocessing** – scaling, encoding, and preparing data for ML models.
* **Model selection** – comparing different models and finding good parameters.
* **Model evaluation** – measuring how well a model performs.

### Common algorithms

Some important algorithms available in Scikit-learn include:

**Classification**

* Logistic Regression
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)
* K-Nearest Neighbors (KNN)

**Regression**

* Linear Regression
* Ridge Regression
* Lasso Regression
* Decision Tree Regressor
* Random Forest Regressor

**Clustering**

* K-Means
* DBSCAN
* Hierarchical Clustering

### Simple example

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(predictions)
```

The basic Scikit-learn workflow is:

**Data → Preprocess → Split → Train → Predict → Evaluate**

For your transition into **AI Engineering**, learning Scikit-learn well is useful because it teaches the fundamentals of machine learning that you'll later apply to more advanced AI and deep-learning systems.
