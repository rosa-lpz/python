
# Access to list elements


There are various ways in which we can access the elements of a list.

## List Index

We can use the index operator `[]` to access an item in a list. In Python, indices start at 0. So, a list having 5 elements will have an index from 0 to 4.

Trying to access indexes other than these will raise an `IndexError`. The index must be an integer. We can't use float or other types, this will result in `TypeError`.

Nested lists are accessed using nested indexing.

### Example 1

```python
# List indexing
my_list = ['p','r','o','b','e']

# Output: p
print(my_list[0])

# Output: o
print(my_list[2])

# Output: e
print(my_list[4])

# Error! Only integer can be used for indexing
# my_list[4.0]

----------

# Nested List
n_list = ["Happy", [2,0,1,5]]

# Nested indexing

   # Output: a
print(n_list[0][1])    

  # Output: 5
print(n_list[1][3])


#Output
p
o
e
a
5
```
--------------------------------------------------------------
### Example 2
```python
# List indexing
months = ['January','February','March','April','May','June','July','August','September','Octuber','November','December']

 
print(months[0])
print(months[1])
print(months[7])


#Output
January
February
August
```

### Example 3 - don't work

```python
# List indexing
list_of_random_things = [1, 3.4, 'a string', True]

print(list_of_random_things[len(list_of_random_things)])
```

**Output**
```
IndexError                                Traceback (most recent call last)
<ipython-input-34-f88b03e5c60e> in <module>()
----> 1 lst[len(lst)]

IndexError: list index out of range
```


However, we can retrieve the last element by reducing the index by 1. Therefore, you can do the following:
```python
# List indexing
list_of_random_things = [1, 3.4, 'a string', True]

print(list_of_random_things[len(list_of_random_things) - 1])
```

**Output**
```
True
```
## Negative indexing

Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.

![[python-list-negindex.png]]

### Example 1

```python
# Negative indexing in lists
my_list = ['p','r','o','b','e']

# Output: e
print(my_list[-1])

# Output: p
print(my_list[-5])




#Output

e
p
```


### Example 2

```python
# List indexing
months = ['January','February','March','April','May','June','July','August','September','Octuber','November','December']

print(months[-1])


#Output
December
```

### Example 3
```python
# List indexing
list_of_random_things = [1, 3.4, 'a string', True]

print(list_of_random_things[-1])
print(list_of_random_things[-2])

# Output
True
a string
```

## References
* https://www.programiz.com/python-programming/list


# Slice and Dice with Lists 

We can access a range of items in a list by using the slicing operator (colon).

## Example 1

```python
my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])

# elements beginning to 4th
print(my_list[:-5])

# elements 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])




#Output
['o', 'g', 'r']
['p', 'r', 'o', 'g']
['a', 'm', 'i', 'z']
['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
```
--------------------------------------------------------------


Slicing can be best visualized by considering the index to be between the elements as shown below. So if we want to access a range, we need two index that will slice that portion from the list.



## Example 2

```python
# List indexing
months = ['January','February','March','April','May','June','July','August','September','Octuber','November','December']

q3 = months[6:9]
first_half = months[:6]
second_half = months[6:]
print(q3)
 


# Output
['July', 'August', 'September']
['January','February','March','April','May','June']
['July','August','September','Octuber','November','December']


```


Lists are very similar to strings:
* Both types support the len() function, indexing and slicing
```python

greeting= "Hello there"
months = ['January','February','March','April','May','June','July','August','September','Octuber','November','December']

print (len(greeting), len(months))


# Output
11 12
```




# REFERENCES

## Websites
* http://www.programiz.com/python-programming/list
* https://www.scholarhat.com/tutorial/python/list-in-python
* https://cs.stanford.edu/people/nick/py/python-list.html
* https://www.pythonhello.com/fundamentals/python-list-access
## Courses
* Udacity - [[AI Programming with Python]] 

