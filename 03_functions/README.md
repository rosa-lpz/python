# Function


In Python, function is a group of related statements that perform a specific task.

Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.

Furthermore, it avoids repetition and makes code reusable.

----

Python involves a function declaration `def` that takes one or more values, and a `return` that returns one or more values. Unlike some other languages, in Python you are not required to specify the data-type of the value your  function is going to return. 

**Note**: In Python every function returns a value. In case you do not specify a return value explicitly, Python will return `None` from that function.

## Reusing Code

Code reuse is a very important part of programming in any language. Increasing code size makes it harder to maintain. 

For a large programming project to be successful, it is essential to abide by the Don't Repeat Yourself, or DRY, principle. We've already looked at one way of doing this: by using loops. In this module, we will explore two more: functions and modules.

Bad, repetitive code is said to abide by the WET principle, which stands for Write Everything Twice, or We Enjoy Typing.



## Syntax of function

```python
def function_name(parameters):
	"""docstring"""
	statement(s)
```


Above shown is a function definition that consists of the following components.

1. Keyword `def` that marks the start of the function header.
2. A function name to uniquely identify the function. Function naming follows the same [rules of writing identifiers in Python](https://www.programiz.com/python-programming/keywords-identifier#rules).
3. Parameters (arguments) through which we pass values to a function. They are optional.
4. A colon (:) to mark the end of the function header.
5. Optional documentation string (docstring) to describe what the function does.
6. One or more valid python statements that make up the function body. Statements must have the same indentation level (usually 4 spaces).
7. An optional `return` statement to return a value from the function.



#### Example 1 - Basic function

````python
def func1():
    print("I am a function")
    
func1()
print(func1())
print(func1)
````



**Output**

```cmd
I am a function
I am a function
```



So in the first case, the function is being called directly, which executes the contents of the function, causing the print statement to print the string. So that's simple enough. In the second case, the function is also being called inside the print function, so the output is the same as in the first case, but then the outer print statement executes, and since our function doesn't return a value, Python evaluates the return value to be the Python constant of none, and then just prints the string representation of that.

In the last case, the function itself is not being executed at all since we're not including those little parentheses that would call the function. We're just printing the value of the function definition itself, which evaluates to this string that you see here.

# Function with inputs

* Parameter
  * Used inside the function to refer to it and to do things with it
* Argument
  * Actual value of the data


**Example 1**

```python
def greet(name):
	print(f"Hello {name}")

greet("Rob")

# Output
Hello Rob


# Parameter: "name"
# Argument: "Rob"
```


There are mainly four types of arguments. They are positional arguments, default arguments, keyword arguments, and arbitrary arguments.

## Positional arguments

The normal arguments that we define in user-defined functions are called positional arguments. All positional arguments are required while invoking the function.

```python
def my_function(a,b,c):
	#Do this with a
	#Then do this with b
	#Finally do this with c

# Calling the function
my_function(3,1,2)
	# Position of the arguments should match the parameters
my_function(c=3m,a=1,b=2)

```

## Default arguments

We can provide the value to the arguments in the function definition itself as default value. When the user didn’t pass the value, the function will consider the default value.

```python
>>> def add(a, b=3):
...     return a + b
...
>>> add(1, 2)
3
>>> add(1)
4
```

## Keyword arguments

To avoid the confusion using positional arguments we could use keyword arguments. In this, we can actually add each of the parameter names and an equal sign to say that.

```python
def my_function(a,b,c):
	#Do this with a
	#Then do this with b
	#Finally do this with c

# Calling the function
my_function(a=1,b=2, c=3)

# Calling the function with different order (do the same action)
my_function(c=3,a=1,b=2)

```


## Arbitrary arguments

We use arbitrary arguments to collect a bunch of values at a time when we don’t know the number of arguments that function will get. We _*_ and _**_ operators in the function definition to collect the arguments.

```python
>>> def add(*args):
...     return sum(args)
...
>>> add(1, 2, 3, 4, 5)
15
>>> def dict_args(**kwargs):
...     print(kwargs)
...
>>> dict_args(a='Geekflare', b='Geekflare Tools', c='Geekflare Online Compiler')
{'a': 'Geekflare', 'b': 'Geekflare Tools', 'c': 'Geekflare Online Compiler'}
```

# Types of Functions

Basically, we can divide functions into the following two types:

1. Built-in functions - Functions that are built into Python.

2. User-defined functions - Functions defined by the users themselves.



## How to call a function in python?

Once we have defined a function, we can call it from another function, program or even the Python prompt. To call a function we simply type the function name with appropriate parameters.

```python
>>> greet('Paul')
Hello, Paul. Good morning!
```

**Note:** Try running the above code in the Python program with the function definition to see the output.

```python
def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

greet('Paul')
```



# Docstrings

Docstrings (documentation strings) serve a similar purpose to comments, as they are designed to explain code. However, they are more specific and have a different syntax. They are created by putting a multiline string containing an explanation of the function below the function's first line.

In the above example, we have a docstring immediately below the function header. We generally use triple quotes so that docstring can extend up to multiple lines. This string is available to us as __doc__ attribute of the function.





###  Example1: Python function

-------------------------------------

```python
def greet(name):
	"""This function greets to
	the person passed in as
	parameter"""
	print("Hello, " + name + ". Good morning!")

greet('Paul')
```



In the above example, we have a docstring immediately below the function header. We generally use triple quotes so that docstring can extend up to multiple lines. This string is available to us as the `__doc__` attribute of the function.




###  Example 2: Python function

```python
def shout(word):
  """
  Print a word with an
  exclamation mark following it.
  """
  print(word + "!")
    
shout("spam")
```





###  Example 3: Python function

```python
def generador(*args):
  """Recibe n cantidad de número y regresa el número además de regresar True o False si el número es mayor a 5
  """
  for valor in args:
     yield valor, True if valor > 5 else False

documentacion = generador.__doc__


```



## Reference

* https://www.programiz.com/python-programming/docstrings





# * args and ** kwargs

## * args 

Python allows you to have functions with **varying numbers of arguments.**

Using * **args** as a function parameter enables you to pass an arbitrary number of arguments to that function. The arguments are then accessible as the tuple **args** in the body of the function.

```python
def function(named_arg, *args): #*arguments
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)
```

output

```cmd
1
(2, 3, 4, 5)
```

Note: The parameter ***args** must come after the named parameters to a function.

The name **args** is just a convention; you can choose to use another (example: * arguments).


### Example 1



```python
def my_min(x, y):
    if x < y:
        return x# Function


In Python, function is a group of related statements that perform a specific task.

Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.

Furthermore, it avoids repetition and makes code reusable.

----

Python involves a function declaration `def` that takes one or more values, and a `return` that returns one or more values. Unlike some other languages, in Python you are not required to specify the data-type of the value your  function is going to return. 

**Note**: In Python every function returns a value. In case you do not specify a return value explicitly, Python will return `None` from that function.

## Reusing Code

Code reuse is a very important part of programming in any language. Increasing code size makes it harder to maintain. 

For a large programming project to be successful, it is essential to abide by the Don't Repeat Yourself, or DRY, principle. We've already looked at one way of doing this: by using loops. In this module, we will explore two more: functions and modules.

Bad, repetitive code is said to abide by the WET principle, which stands for Write Everything Twice, or We Enjoy Typing.



## Syntax of function

```python
def function_name(parameters):
	"""docstring"""
	statement(s)
```


Above shown is a function definition that consists of the following components.

1. Keyword `def` that marks the start of the function header.
2. A function name to uniquely identify the function. Function naming follows the same [rules of writing identifiers in Python](https://www.programiz.com/python-programming/keywords-identifier#rules).
3. Parameters (arguments) through which we pass values to a function. They are optional.
4. A colon (:) to mark the end of the function header.
5. Optional documentation string (docstring) to describe what the function does.
6. One or more valid python statements that make up the function body. Statements must have the same indentation level (usually 4 spaces).
7. An optional `return` statement to return a value from the function.



#### Example 1 - Basic function

````python
def func1():
    print("I am a function")
    
func1()
print(func1())
print(func1)
````



**Output**

```cmd
I am a function
I am a function
```



So in the first case, the function is being called directly, which executes the contents of the function, causing the print statement to print the string. So that's simple enough. In the second case, the function is also being called inside the print function, so the output is the same as in the first case, but then the outer print statement executes, and since our function doesn't return a value, Python evaluates the return value to be the Python constant of none, and then just prints the string representation of that.

In the last case, the function itself is not being executed at all since we're not including those little parentheses that would call the function. We're just printing the value of the function definition itself, which evaluates to this string that you see here.

# Function with inputs

* Parameter
  * Used inside the function to refer to it and to do things with it
* Argument
  * Actual value of the data


**Example 1**

```python
def greet(name):
	print(f"Hello {name}")

greet("Rob")

# Output
Hello Rob


# Parameter: "name"
# Argument: "Rob"
```


There are mainly four types of arguments. They are positional arguments, default arguments, keyword arguments, and arbitrary arguments.

## Positional arguments

The normal arguments that we define in user-defined functions are called positional arguments. All positional arguments are required while invoking the function.

```python
def my_function(a,b,c):
	#Do this with a
	#Then do this with b
	#Finally do this with c

# Calling the function
my_function(3,1,2)
	# Position of the arguments should match the parameters
my_function(c=3m,a=1,b=2)

```

## Default arguments

We can provide the value to the arguments in the function definition itself as default value. When the user didn’t pass the value, the function will consider the default value.

```python
>>> def add(a, b=3):
...     return a + b
...
>>> add(1, 2)
3
>>> add(1)
4
```

## Keyword arguments

To avoid the confusion using positional arguments we could use keyword arguments. In this, we can actually add each of the parameter names and an equal sign to say that.

```python
def my_function(a,b,c):
	#Do this with a
	#Then do this with b
	#Finally do this with c

# Calling the function
my_function(a=1,b=2, c=3)

# Calling the function with different order (do the same action)
my_function(c=3,a=1,b=2)

```


## Arbitrary arguments

We use arbitrary arguments to collect a bunch of values at a time when we don’t know the number of arguments that function will get. We _*_ and _**_ operators in the function definition to collect the arguments.

```python
>>> def add(*args):
...     return sum(args)
...
>>> add(1, 2, 3, 4, 5)
15
>>> def dict_args(**kwargs):
...     print(kwargs)
...
>>> dict_args(a='Geekflare', b='Geekflare Tools', c='Geekflare Online Compiler')
{'a': 'Geekflare', 'b': 'Geekflare Tools', 'c': 'Geekflare Online Compiler'}
```

# Types of Functions

Basically, we can divide functions into the following two types:

1. Built-in functions - Functions that are built into Python.

2. User-defined functions - Functions defined by the users themselves.



## How to call a function in python?

Once we have defined a function, we can call it from another function, program or even the Python prompt. To call a function we simply type the function name with appropriate parameters.

```python
>>> greet('Paul')
Hello, Paul. Good morning!
```

**Note:** Try running the above code in the Python program with the function definition to see the output.

```python
def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

greet('Paul')
```



# Docstrings

Docstrings (documentation strings) serve a similar purpose to comments, as they are designed to explain code. However, they are more specific and have a different syntax. They are created by putting a multiline string containing an explanation of the function below the function's first line.

In the above example, we have a docstring immediately below the function header. We generally use triple quotes so that docstring can extend up to multiple lines. This string is available to us as __doc__ attribute of the function.





###  Example1: Python function

-------------------------------------

```python
def greet(name):
	"""This function greets to
	the person passed in as
	parameter"""
	print("Hello, " + name + ". Good morning!")

greet('Paul')
```



In the above example, we have a docstring immediately below the function header. We generally use triple quotes so that docstring can extend up to multiple lines. This string is available to us as the `__doc__` attribute of the function.




###  Example 2: Python function

```python
def shout(word):
  """
  Print a word with an
  exclamation mark following it.
  """
  print(word + "!")
    
shout("spam")
```





###  Example 3: Python function

```python
def generador(*args):
  """Recibe n cantidad de número y regresa el número además de regresar True o False si el número es mayor a 5
  """
  for valor in args:
     yield valor, True if valor > 5 else False

documentacion = generador.__doc__


```



## Reference

* https://www.programiz.com/python-programming/docstrings





# * args and ** kwargs

## * args 

Python allows you to have functions with **varying numbers of arguments.**

Using * **args** as a function parameter enables you to pass an arbitrary number of arguments to that function. The arguments are then accessible as the tuple **args** in the body of the function.

```python
def function(named_arg, *args): #*arguments
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)
```

output

```cmd
1
(2, 3, 4, 5)
```

Note: The parameter ***args** must come after the named parameters to a function.

The name **args** is just a convention; you can choose to use another (example: * arguments).


### Example 1



```python
def my_min(x, y):
    if x < y:
        return x
    else:
        return y

print(my_min(8, 13, 4, 42, 120, 7))
```

**Explanation of the code**
This is a function called `my_min` that takes two arguments `x` and `y`. It then compares the two values using an `if` statement to determine which one is smaller. If `x` is smaller than `y`, the function returns `x`, otherwise it returns `y`. However, the function is called with more than two arguments which means it will raise a TypeError because it is expecting only two arguments.

**The a bug**
The code is not covering the requirement of taking any number of variables. It is only taking two variables and ignoring the rest of the arguments passed using * args. The output of the code will be 8, which is the smaller number between 8 and 13.

**Solution

In this version, `*args` allows the function to accept any number of arguments. The function then iterates over the arguments and finds the minimum value. If no arguments are provided, it raises a `ValueError` to indicate that at least one argument is required.

Now, when you call `my_min(8, 13, 4, 42, 120, 7)`, it will correctly return 4, which is the smallest number among the provided arguments.

```python
def my_min(*args):
    if not args:
        raise ValueError("At least one argument is required")

    min_value = args[0]
    for arg in args[1:]:
        if arg < min_value:
            min_value = arg
    return min_value# Function


In Python, function is a group of related statements that perform a specific task.

Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.

Furthermore, it avoids repetition and makes code reusable.

----

Python involves a function declaration `def` that takes one or more values, and a `return` that returns one or more values. Unlike some other languages, in Python you are not required to specify the data-type of the value your  function is going to return. 

**Note**: In Python every function returns a value. In case you do not specify a return value explicitly, Python will return `None` from that function.

## Reusing Code

Code reuse is a very important part of programming in any language. Increasing code size makes it harder to maintain. 

For a large programming project to be successful, it is essential to abide by the Don't Repeat Yourself, or DRY, principle. We've already looked at one way of doing this: by using loops. In this module, we will explore two more: functions and modules.

Bad, repetitive code is said to abide by the WET principle, which stands for Write Everything Twice, or We Enjoy Typing.



## Syntax of function

```python
def function_name(parameters):
	"""docstring"""
	statement(s)
```


Above shown is a function definition that consists of the following components.

1. Keyword `def` that marks the start of the function header.
2. A function name to uniquely identify the function. Function naming follows the same [rules of writing identifiers in Python](https://www.programiz.com/python-programming/keywords-identifier#rules).
3. Parameters (arguments) through which we pass values to a function. They are optional.
4. A colon (:) to mark the end of the function header.
5. Optional documentation string (docstring) to describe what the function does.
6. One or more valid python statements that make up the function body. Statements must have the same indentation level (usually 4 spaces).
7. An optional `return` statement to return a value from the function.



#### Example 1 - Basic function

````python
def func1():
    print("I am a function")
    
func1()
print(func1())
print(func1)
````



**Output**

```cmd
I am a function
I am a function
```



So in the first case, the function is being called directly, which executes the contents of the function, causing the print statement to print the string. So that's simple enough. In the second case, the function is also being called inside the print function, so the output is the same as in the first case, but then the outer print statement executes, and since our function doesn't return a value, Python evaluates the return value to be the Python constant of none, and then just prints the string representation of that.

In the last case, the function itself is not being executed at all since we're not including those little parentheses that would call the function. We're just printing the value of the function definition itself, which evaluates to this string that you see here.

# Function with inputs

* Parameter
  * Used inside the function to refer to it and to do things with it
* Argument
  * Actual value of the data


**Example 1**

```python
def greet(name):
	print(f"Hello {name}")

greet("Rob")

# Output
Hello Rob


# Parameter: "name"
# Argument: "Rob"
```


There are mainly four types of arguments. They are positional arguments, default arguments, keyword arguments, and arbitrary arguments.

## Positional arguments

The normal arguments that we define in user-defined functions are called positional arguments. All positional arguments are required while invoking the function.

```python
def my_function(a,b,c):
	#Do this with a
	#Then do this with b
	#Finally do this with c

# Calling the function
my_function(3,1,2)
	# Position of the arguments should match the parameters
my_function(c=3m,a=1,b=2)

```

## Default arguments

We can provide the value to the arguments in the function definition itself as default value. When the user didn’t pass the value, the function will consider the default value.

```python
>>> def add(a, b=3):
...     return a + b
...
>>> add(1, 2)
3
>>> add(1)
4
```

## Keyword arguments

To avoid the confusion using positional arguments we could use keyword arguments. In this, we can actually add each of the parameter names and an equal sign to say that.

```python
def my_function(a,b,c):
	#Do this with a
	#Then do this with b
	#Finally do this with c

# Calling the function
my_function(a=1,b=2, c=3)

# Calling the function with different order (do the same action)
my_function(c=3,a=1,b=2)

```


## Arbitrary arguments

We use arbitrary arguments to collect a bunch of values at a time when we don’t know the number of arguments that function will get. We _*_ and _**_ operators in the function definition to collect the arguments.

```python
>>> def add(*args):
...     return sum(args)
...
>>> add(1, 2, 3, 4, 5)
15
>>> def dict_args(**kwargs):
...     print(kwargs)
...
>>> dict_args(a='Geekflare', b='Geekflare Tools', c='Geekflare Online Compiler')
{'a': 'Geekflare', 'b': 'Geekflare Tools', 'c': 'Geekflare Online Compiler'}
```

# Types of Functions

Basically, we can divide functions into the following two types:

1. Built-in functions - Functions that are built into Python.

2. User-defined functions - Functions defined by the users themselves.



## How to call a function in python?

Once we have defined a function, we can call it from another function, program or even the Python prompt. To call a function we simply type the function name with appropriate parameters.

```python
>>> greet('Paul')
Hello, Paul. Good morning!
```

**Note:** Try running the above code in the Python program with the function definition to see the output.

```python
def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

greet('Paul')
```



# Docstrings

Docstrings (documentation strings) serve a similar purpose to comments, as they are designed to explain code. However, they are more specific and have a different syntax. They are created by putting a multiline string containing an explanation of the function below the function's first line.

In the above example, we have a docstring immediately below the function header. We generally use triple quotes so that docstring can extend up to multiple lines. This string is available to us as __doc__ attribute of the function.





###  Example1: Python function

-------------------------------------

```python
def greet(name):
	"""This function greets to
	the person passed in as
	parameter"""
	print("Hello, " + name + ". Good morning!")

greet('Paul')
```



In the above example, we have a docstring immediately below the function header. We generally use triple quotes so that docstring can extend up to multiple lines. This string is available to us as the `__doc__` attribute of the function.




###  Example 2: Python function

```python
def shout(word):
  """
  Print a word with an
  exclamation mark following it.
  """
  print(word + "!")
    
shout("spam")
```





###  Example 3: Python function

```python
def generador(*args):
  """Recibe n cantidad de número y regresa el número además de regresar True o False si el número es mayor a 5
  """
  for valor in args:
     yield valor, True if valor > 5 else False

documentacion = generador.__doc__


```



## Reference

* https://www.programiz.com/python-programming/docstrings





# * args and ** kwargs

## * args 

Python allows you to have functions with **varying numbers of arguments.**

Using * **args** as a function parameter enables you to pass an arbitrary number of arguments to that function. The arguments are then accessible as the tuple **args** in the body of the function.

```python
def function(named_arg, *args): #*arguments
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)
```

output

```cmd
1
(2, 3, 4, 5)
```

Note: The parameter ***args** must come after the named parameters to a function.

The name **args** is just a convention; you can choose to use another (example: * arguments).


### Example 1



```python
def my_min(x, y):
    if x < y:
        return x
    else:
        return y

print(my_min(8, 13, 4, 42, 120, 7))
```

**Explanation of the code**
This is a function called `my_min` that takes two arguments `x` and `y`. It then compares the two values using an `if` statement to determine which one is smaller. If `x` is smaller than `y`, the function returns `x`, otherwise it returns `y`. However, the function is called with more than two arguments which means it will raise a TypeError because it is expecting only two arguments.

**The a bug**
The code is not covering the requirement of taking any number of variables. It is only taking two variables and ignoring the rest of the arguments passed using * args. The output of the code will be 8, which is the smaller number between 8 and 13.

**Solution

In this version, `*args` allows the function to accept any number of arguments. The function then iterates over the arguments and finds the minimum value. If no arguments are provided, it raises a `ValueError` to indicate that at least one argument is required.

Now, when you call `my_min(8, 13, 4, 42, 120, 7)`, it will correctly return 4, which is the smallest number among the provided arguments.

```python
def my_min(*args):
    if not args:
        raise ValueError("At least one argument is required")

    min_value = args[0]
    for arg in args[1:]:
        if arg < min_value:
            min_value = arg
    return min_value

print(my_min(8, 13, 4, 42, 120, 7))

```

Output

```cmd
4
```



## * kwargs

** **kwargs** (standing for keyword arguments) allows you to handle named arguments that you have not defined in advance.

The keyword arguments return a **dictionary** in which the keys are the argument names, and the values are the argument values.

```python
def my_func(x, y=7, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)
```

Output

```cmd
2
3
(4, 5, 6)
{'a': 7, 'b': 8}
```




# Lambda

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax

```python
lambda _arguments_ : _expression_
```


Example

```python
x = lambda a : a + 10  
print(x(5))

# Output
# 15
```


# REFERENCES

## Websites

* https://www.programiz.com/python-programming/function
* https://www.sololearn.com/Play/Python
* https://www.w3schools.com/python/python_lambda.asp
* GeekFlare: 
  * https://geekflare.com/dev/top-python-interview-questions/



## Courses

* LinkedIn - Learning Python
  * https://www.linkedin.com/learning/learning-python/python-functions
* SoloLearn - Python intermediate
* Udacity - Data Structures and Algorithms Nanodegree

print(my_min(8, 13, 4, 42, 120, 7))

```

Output

```cmd
4
```



## * kwargs

** **kwargs** (standing for keyword arguments) allows you to handle named arguments that you have not defined in advance.

The keyword arguments return a **dictionary** in which the keys are the argument names, and the values are the argument values.

```python
def my_func(x, y=7, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)
```

Output

```cmd
2
3
(4, 5, 6)
{'a': 7, 'b': 8}
```




# Lambda

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax

```python
lambda _arguments_ : _expression_
```


Example

```python
x = lambda a : a + 10  
print(x(5))

# Output
# 15
```


# REFERENCES

## Websites

* https://www.programiz.com/python-programming/function
* https://www.sololearn.com/Play/Python
* https://www.w3schools.com/python/python_lambda.asp
* GeekFlare: 
  * https://geekflare.com/dev/top-python-interview-questions/



## Courses

* LinkedIn - Learning Python
  * https://www.linkedin.com/learning/learning-python/python-functions
* SoloLearn - Python intermediate
* Udacity - Data Structures and Algorithms Nanodegree
    else:
        return y

print(my_min(8, 13, 4, 42, 120, 7))
```

**Explanation of the code**
This is a function called `my_min` that takes two arguments `x` and `y`. It then compares the two values using an `if` statement to determine which one is smaller. If `x` is smaller than `y`, the function returns `x`, otherwise it returns `y`. However, the function is called with more than two arguments which means it will raise a TypeError because it is expecting only two arguments.

**The a bug**
The code is not covering the requirement of taking any number of variables. It is only taking two variables and ignoring the rest of the arguments passed using * args. The output of the code will be 8, which is the smaller number between 8 and 13.

**Solution

In this version, `*args` allows the function to accept any number of arguments. The function then iterates over the arguments and finds the minimum value. If no arguments are provided, it raises a `ValueError` to indicate that at least one argument is required.

Now, when you call `my_min(8, 13, 4, 42, 120, 7)`, it will correctly return 4, which is the smallest number among the provided arguments.

```python
def my_min(*args):
    if not args:
        raise ValueError("At least one argument is required")

    min_value = args[0]
    for arg in args[1:]:
        if arg < min_value:
            min_value = arg
    return min_value

print(my_min(8, 13, 4, 42, 120, 7))

```

Output

```cmd
4
```



## * kwargs

** **kwargs** (standing for keyword arguments) allows you to handle named arguments that you have not defined in advance.

The keyword arguments return a **dictionary** in which the keys are the argument names, and the values are the argument values.

```python
def my_func(x, y=7, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)
```

Output

```cmd
2
3
(4, 5, 6)
{'a': 7, 'b': 8}
```




# Lambda

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax

```python
lambda _arguments_ : _expression_
```


Example

```python
x = lambda a : a + 10  
print(x(5))

# Output
# 15
```


# REFERENCES

## Websites

* https://www.programiz.com/python-programming/function
* https://www.sololearn.com/Play/Python
* https://www.w3schools.com/python/python_lambda.asp
* GeekFlare: 
  * https://geekflare.com/dev/top-python-interview-questions/



## Courses

* LinkedIn - Learning Python
  * https://www.linkedin.com/learning/learning-python/python-functions
* SoloLearn - Python intermediate
* Udacity - Data Structures and Algorithms Nanodegree