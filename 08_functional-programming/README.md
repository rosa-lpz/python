# Functional Programming

Functional programming is a style of programming that (as the name suggests) is based around functions. 

In computer science, functional programming is a programming paradigm where programs are constructed by applying and composing functions. It is a declarative programming paradigm in which function definitions are trees of expressions that map values to other values, rather than a sequence of imperative statements which update the running state of the program.

* Declarative programming:
  * In computer science, declarative programming is a programming paradigm—a style of building the structure and elements of computer programs—that expresses the logic of a computation without describing its control flow.



Functional programming languages are specially designed to handle symbolic computation and list processing applications. Functional programming is based on mathematical functions. Some of the popular functional programming languages include: Lisp, Python, Erlang, Haskell, Clojure, etc.

Functional programming languages are categorized into two groups, i.e. −

- **Pure Functional Languages** − These types of functional languages support only the functional paradigms. For example − Haskell.
- **Impure Functional Languages** − These types of functional languages support the functional paradigms and imperative style programming. For example − LISP.



## Functional Programming – Characteristics

The most prominent characteristics of functional programming are as follows −

- Functional programming languages are designed on the concept of mathematical functions that use conditional expressions and recursion to perform computation.
- Functional programming supports **higher-order functions** and **lazy evaluation** features.
- Functional programming languages don’t support flow Controls like loop statements and conditional statements like If-Else and Switch Statements. They directly use the functions and functional calls.
- Like OOP, functional programming languages support popular concepts such as Abstraction, Encapsulation, Inheritance, and Polymorphism.



## Functional Programming – Advantages

Functional programming offers the following advantages −

- **Bugs-Free Code** − Functional programming does not support **state**, so there are no side-effect results and we can write error-free codes.
- **Efficient Parallel Programming** − Functional programming languages have NO Mutable state, so there are no state-change issues. One can program "Functions" to work parallel as "instructions". Such codes support easy reusability and testability.
- **Efficiency** − Functional programs consist of independent units that can run concurrently. As a result, such programs are more efficient.
- **Supports Nested Functions** − Functional programming supports Nested Functions.
- **Lazy Evaluation** − Functional programming supports Lazy Functional Constructs like Lazy Lists, Lazy Maps, etc.

As a downside, functional programming requires a large memory space. As it does not have state, you need to create new objects every time to perform actions.

Functional Programming is used in situations where we have to perform lots of different operations on the same set of data.

- Lisp is used for artificial intelligence applications like Machine learning, language processing, Modeling of speech and vision, etc.
- Embedded Lisp interpreters add programmability to some systems like Emacs.



## Functional Programming vs. Object-oriented Programming

The following table highlights the major differences between functional programming and object-oriented programming −

|                    Functional Programming                    |                             OOP                              |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                     Uses Immutable data.                     |                      Uses Mutable data.                      |
|            Follows Declarative Programming Model.            |            Follows Imperative Programming Model.             |
|              Focus is on: “What you are doing”               |               Focus is on “How you are doing”                |
|                Supports Parallel Programming                 |            Not suitable for Parallel Programming             |
|              Its functions have no-side effects              |        Its methods can produce serious side effects.         |
| Flow Control is done using function calls & function calls with recursion | Flow control is done using loops and conditional statements. |
|   It uses "Recursion" concept to iterate Collection Data.    | It uses "Loop" concept to iterate Collection Data. For example: For-each loop in Java |
|      Execution order of statements is not so important.      |       Execution order of statements is very important.       |
| Supports both "Abstraction over Data" and "Abstraction over Behavior". |            Supports only "Abstraction over Data".            |





## Efficiency of a Program Code

The efficiency of a programming code is directly proportional to the algorithmic efficiency and the execution speed. Good efficiency ensures higher performance.

The factors that affect the efficiency of a program includes −

- The speed of the machine
- Compiler speed
- Operating system
- Choosing right Programming language
- The way of data in a program is organized
- Algorithm used to solve the problem

The efficiency of a programming language can be improved by performing the following tasks −

- By removing unnecessary code or the code that goes to redundant processing.
- By making use of optimal memory and nonvolatile storage
- By making the use of reusable components wherever applicable.
- By making the use of error & exception handling at all layers of program.
- By creating programming code that ensures data integrity and consistency.
- By developing the program code that's compliant with the design logic and flow.

An efficient programming code can reduce resource consumption and completion time as much as possible with minimum risk to the operating environment.



----

## Example



A key part of functional programming is higher-order functions. We have seen this idea briefly in the previous lesson on functions as objects. Higher-order functions take other functions as arguments, or return them as results.

Example:

```python
def apply_twice(func, arg):
   return func(func(arg))

def add_five(x):
   return x + 5

print(apply_twice(add_five, 10))
```





Result: 20



**Reference:** 

* Wikipedia
* Sololearn
* Tutorialspoint: https://www.tutorialspoint.com/functional_programming/functional_programming_introduction.htm







# Pure functions

Functional programming seeks to use **pure functions**. Pure functions have no side effects, and return a value that depends **only** on their arguments.

This is how functions in math work: for example, the **cos(x)** will, for the same value of **x**, always return the same result.



**Using pure functions has both advantages and disadvantages.** 

Pure functions are:

* easier to reason about and test.
* more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the next time the function of that input is needed, reducing the number of times the function is called. This is called **memoization**.
* easier to run in parallel.



Below are examples of pure and impure functions.



**Pure function:**

```PY
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)PYCopy
```



**Impure function:**

```PY
some_list = []

def impure(arg):
  some_list.append(arg)
```





# Lambdas

Creating a function normally (using **def**) assigns it to a variable with its name automatically. 

Python allows us to create functions on-the-fly, provided that they are created using **lambda** syntax. 

This approach is most commonly used when passing a simple function as an argument to another function. The syntax is shown in the next example and consists of the **lambda** keyword followed by a list of arguments, a colon, and the expression to evaluate and return. 

**Example**

```python
def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)
```



## **Lambda functions aren't as powerful as named functions.** 

They can only do things that require a single expression -- usually equivalent to a single line of code.



**Example** 1

```python
#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))
Click to run
```

In the code above, we created an anonymous function on the fly and called it with an argument.



**Example** 2

Lambda function that returns the square of its argument, and call it for the number 8

```python
a = (lambda x; x*x) (8)
```



# Decorators

Decorators provide a way to modify functions using other functions. 

This is ideal when you need to extend the functionality of functions that you don't want to modify.

```python
def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

decorated = decor(print_text)
decorated()
```



We defined a function named decor that has a single parameter func. Inside decor, we defined a nested function named wrap. The wrap function will print a string, then call func(), and print another string. The decor function returns the wrap function as its result.

We could say that the variable decorated is a decorated version of print_text -- it's print_text plus something.

In fact, if we wrote a useful decorator we might want to replace print_text with the decorated version altogether so we always got our "plus something" version of print_text.

This is done by re-assigning the variable that contains our function:

```python
print_text = decor(print_text)
print_text()
```





## Recursion



# References

* Solo learn - Python intermediate
* Wikipedia
  * Functional programming: https://en.wikipedia.org/wiki/Functional_programming
  * Declarative programming: https://en.wikipedia.org/wiki/Declarative_programming 
* Tutorialspoint
  * https://www.tutorialspoint.com/functional_programming/functional_programming_introduction.htm