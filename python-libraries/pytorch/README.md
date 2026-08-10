### Introduction to PyTorch

**PyTorch** is an open-source Python framework used for **deep learning and artificial intelligence**. It is widely used to build and train neural networks and is especially popular in **AI research and modern machine learning**.

PyTorch allows you to work with **tensors**, build neural networks, train models, and use **GPUs** to speed up calculations.

### What can you do with PyTorch?

With PyTorch, you can:

* Build and train **neural networks**
* Work with **tensors** and large datasets
* Use **GPUs** for faster model training
* Build **deep learning models**
* Work with **images, text, audio, and other data**
* Create models for **classification and regression**
* Develop **Natural Language Processing (NLP)** applications
* Work with **Large Language Models (LLMs)**
* Experiment with new models for **AI research**

### Important PyTorch concepts

#### 1. Tensors

A tensor is PyTorch's main data structure. It is similar to a NumPy array but can also run efficiently on a GPU.

```python
import torch

x = torch.tensor([1, 2, 3, 4])

print(x)
```

You can also create a matrix:

```python
x = torch.tensor([
    [1, 2],
    [3, 4]
])

print(x)
```

#### 2. Neural Networks

PyTorch provides `torch.nn` for creating neural networks.

```python
import torch
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(2, 10),
    nn.ReLU(),
    nn.Linear(10, 1)
)

print(model)
```

Here:

* `Linear` → a fully connected layer
* `ReLU` → an activation function
* `10` → number of neurons in the hidden layer
* `1` → output neuron

#### 3. Training a Model

A typical PyTorch training process looks like:

**Data → Model → Prediction → Loss → Backpropagation → Update Weights**

For example:

```python
loss = criterion(predictions, y)

optimizer.zero_grad()
loss.backward()
optimizer.step()
```

* `loss` measures how wrong the model is.
* `backward()` calculates the gradients.
* `optimizer.step()` updates the model's weights.

### PyTorch vs Scikit-learn

| Scikit-learn                 | PyTorch                    |
| ---------------------------- | -------------------------- |
| Traditional machine learning | Deep learning              |
| Random Forest                | Neural Networks            |
| Logistic Regression          | CNNs                       |
| Decision Trees               | Transformers               |
| K-Means                      | LLMs                       |
| Easier for beginners         | More flexible              |
| Mostly CPU-based             | CPU and GPU                |
| Great for ML fundamentals    | Great for AI/deep learning |

### What should you learn first?

Since you want to transition from **Data Science into AI Engineering and Research**, I recommend learning PyTorch in this order:

**1. Python → 2. NumPy → 3. Tensors → 4. Neural Networks → 5. Training & Backpropagation → 6. CNNs → 7. NLP → 8. Transformers → 9. LLMs → 10. RAG**

This path will give you a strong foundation for **AI Engineering and AI Research**.
