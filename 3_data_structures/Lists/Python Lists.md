# Content
- [[Python Lists - Creation]]
- [[Python Lists - Access elements]]
- [[Python Lists - Edition]]
- [[Python Lists - Join]]
- [[Python Lists - Loops]]
- [[Python Lists - Methods]]
- [[Python Lists - Operations]]

List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible. All the items in a list do not need to be of the same type.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are [Tuple](https://www.w3schools.com/python/python_tuples.asp), [Set](https://www.w3schools.com/python/python_sets.asp), and [Dictionary](https://www.w3schools.com/python/python_dictionaries.asp), all with different qualities and usage.

Declaring a list is pretty straight forward. Items separated by commas are enclosed within brackets [ ].

-------------------------------------
```python
a = [1, 2.2, 'python']
```
-------------------------------------
We can use the slicing operator [ ] to extract an item or a range of items from a list. Index starts form 0 in Python.



## List Items

List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index `[0]`, the second item has index `[1]` etc.



### Example 1

-------------------------------------
```python
a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])
```



**Output**

```cmd
a[2] =  15
a[0:3] =  [5, 10, 15]
a[5:] =  [30, 35, 40]
```



### Example 2

-------------------------------------

```python
Participants = ['John', 'Leila', 'Gregory', 'Cate']


print (Participants[1])

print (Participants[-2])

```



**Output**

```cmd
Leila
Gregory
```




# Characteristics of Lists
## Ordered

When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

**Note:** There are some [list methods](https://www.w3schools.com/python/python_lists_methods.asp) that will change the order, but in general: the order of the items will not change.



-------------------------------------

```python
>>> a = [1,2,3]
>>> a[2]=4
>>> a
[1, 2, 4]
```

-------------------------------------





## Changeable

The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.



### Example 1

-------------------------------------

```python
Participants = ['John', 'Leila', 'Gregory', 'Cate']

Participants[3] ='Maria'
print (Participants[3])



```



**Output**

```cmd
'John', 'Leila', 'Gregory', 'Maria'
```



------

## Allow Duplicates

Since lists are indexed, lists can have items with the same value:

```python
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
```



# Python List Operations
Basic list operations in Python include performing basic arithmetic on the numbers contained within a list, accessing elements of an existing list, replacing elements of a list, rearranging elements of a list, concatenating multiple lists together, and duplicating specific entries in a list.

|   |   |   |
|---|---|---|
|**Python Expression**|**Results**|**Description**|
|len([1, 2, 3])|3|Length|
|[1, 2, 3] + [4, 5, 6]|[1, 2, 3, 4, 5, 6]|Concatenation|
|['Hi!'] * 4|['Hi!', 'Hi!', 'Hi!', 'Hi!']|Repetition|
|3 in [1, 2, 3]|True|Membership|
|for x in [1, 2, 3]: print x,|1 2 3|Iteration|


```python
# Creating a List with 
# the use of multiple values 
List = ["Geeks", "For", "Geeks"] 
print("\nList containing multiple values: ") 
print(List)

# Creating a Multi-Dimensional List 
# (By Nesting a list inside a List) 
List2 = [['Geeks', 'For'], ['Geeks']] 
print("\nMulti-Dimensional List: ") 
print(List2) 

# accessing a element from the 
# list using index number 
print("Accessing element from the list") 
print(List[0]) 
print(List[2]) 

# accessing a element using 
# negative indexing 
print("Accessing element using negative indexing") 
	
# print the last element of list 
print(List[-1]) 
	
# print the third last element of list 
print(List[-3])
```


# References

* https://www.w3schools.com/python/python_lists.asp
* https://www.programiz.com/python-programming/variables-datatypes
* https://www.tutorialspoint.com/python/python_lists.htm