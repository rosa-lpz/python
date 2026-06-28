# Python OOP - Inheritance


Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).

### Example 1: Use of Inheritance in Python

```python
# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
```

In the above program, we created two classes i.e. Bird (parent class) and Penguin (child class). The child class inherits the functions of parent class. We can see this from the `swim()` method.

Again, the child class modified the behavior of the parent class. We can see this from the `whoisThis()` method. Furthermore, we extend the functions of the parent class, by creating a new `run()` method.

Additionally, we use the `super()` function inside the `__init__()` method. This allows us to run the `__init__()` method of the parent class inside the child class.


# Reference

* https://www.programiz.com/python-programming/object-oriented-programming
* Udemy - 100 days of code

## YouTube
* Python's __init__ Method | 2MinutesPy: https://youtu.be/mYKGYr0xaXw