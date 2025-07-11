# Python OOP 

Python is a multi-paradigm programming language. It supports different programming approaches.

One of the popular approaches to solve a programming problem is by creating objects. This is known as Object-Oriented Programming (OOP).

An object has two characteristics:

- attributes
- behavior

Let's take an example:

A parrot is an object, as it has the following properties:

- name, age, color as attributes
- singing, dancing as behavior

The concept of OOP in Python focuses on creating reusable code. This concept is also known as DRY (Don't Repeat Yourself).

In Python, the concept of OOP follows some basic principles:

------



## Example

### Object

Waiter


#### Attributes

```python
is_holding_plate = True
tables_responsible = [4, 5, 6]
```



#### Methods (functions)

```python
def take_order(table, order):
    #takes order to chef

def take_payment(amount):
    #add money to restaurant
```







## Class

A class is a blueprint for the object.

We can think of class as a sketch of a parrot with labels. It contains all the details about the name, colors, size etc. Based on these descriptions, we can study about the parrot. Here, a parrot is an object.

The example for class of parrot can be :

```PYTHON
class Parrot:
    pass
```

Here, we use the `class` keyword to define an empty class Parrot. From class, we construct instances. An instance is a specific object created from a particular class.



## Object

An object (instance) is an instantiation of a class. When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.

The example for object of parrot class can be:

```python
obj = Parrot()
```

Here, obj is an object of class `Parrot`.

Suppose we have details of parrots. Now, we are going to show how to build the class and objects of parrots.



### Example 1: Creating Class and Object in Python

```python
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))
```



**Output**

```cmd
Blu is a bird
Woo is also a bird
Blu is 10 years old
Woo is 15 years old
```

In the above program, we created a class with the name Parrot. Then, we define attributes. The attributes are a characteristic of an object.

These attributes are defined inside the `__init__` method of the class. It is the initializer method that is first run as soon as the object is created.

Then, we create instances of the Parrot class. Here, **blu** and **woo** are references (value) to our new objects.

We can access the class attribute using `__class__.species`. Class attributes are the same for all instances of a class. Similarly, we access the instance attributes using `blu.name` and `blu.age`. However, instance attributes are different for every instance of a class.


### Example 2
```python
class Car:
	def __init__(self, seats):
	self.seats = seats


# 5 is set to define number of seats
my_car = Car(5)

# my_car=Car(5) can also be defined as
my_car.seats=5
```

## Methods

Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.

#### Example 1 : Creating Methods in Python

```python
class Parrot:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())
```

**Output**

```cmd
Blu sings 'Happy'
Blu is now dancing
```

In the above program, we define two methods i.e `sing()` and `dance()`. These are called instance methods because they are called on an instance object i.e `blu`.

#### Example 2 

```python
class Car:
	def enter_race_mode():
		self.seats = 2

# Call method
my_car.enter_race_mode()
```




------

## Key Points to Remember:

- Object-Oriented Programming makes the program easy to understand as well as efficient.
- Since the class is sharable, the code can be reused.
- Data is safe and secure with data abstraction.
- Polymorphism allows the same interface for different objects, so programmers can write efficient code.



# References

* https://www.programiz.com/python-programming/object-oriented-programming
* Udemy - 100 days of code

## YouTube
* Python's __init__ Method | 2MinutesPy: https://youtu.be/mYKGYr0xaXw
