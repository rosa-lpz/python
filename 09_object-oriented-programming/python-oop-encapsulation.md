# Python OOP - Encapsulation

Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single `_` or double `__`.

## Example 1: Data Encapsulation in Python

```python
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
```



**Output**

```
Selling Price: 900
Selling Price: 900
Selling Price: 1000
```



In the above program, we defined a Computer class.

We used `__init__()` method to store the maximum selling price of `Computer`. We tried to modify the price. However, we can't change it because Python treats the __maxprice as private attributes.

As shown, to change the value, we have to use a setter function i.e `setMaxPrice()` which takes price as a parameter.


# References

* https://www.programiz.com/python-programming/object-oriented-programming
* Udemy - 100 days of code

## YouTube
* Python's __init__ Method | 2MinutesPy: https://youtu.be/mYKGYr0xaXw

