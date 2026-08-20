# Find the numbers that sum a target

Given a list of numbers and a target number 

* Return true if there are two numbers A and B in the list suc that A + B = target
* Otherwise return false





# Python

## Solution 1 

```python
"""
Given a list of numbers and a target number 

* Return true if there are two numbers A and B in the list such that A + B = target
* Otherwise return false
"""

def find_target(lst,target):

    for i in lst:
        for j in lst:
            if (i+j == target):
               return True
    # Return false after the execution of all the loops       
    return False
        
    
    
# Test 1
lst_numbers=[1,2,3,4,5]
target_number=6

print(find_target(lst_numbers,target_number))
```





## Solution 2

```python
"""
Given a list of numbers and a target number 

* Return true if there are two numbers A and B in the list such that A + B = target
* Otherwise return false
"""

def find_target(lst,target):

    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] + lst[j] == target:
                return True

                
        return False
               
    
    # Return false after the execution of all the loops     
    return False
```

