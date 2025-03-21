# Find the numbers that sum a target

* Given a list of numbers and a target number 

  * Return true if there are two numbers A and B in the list such that A + B = target
  * Otherwise return false



## Solution 1

```python
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
# Output: True
```



## Solution 2

```python
def find_target(lst,target):

    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] + lst[j] == target:
                return True

                
        return False
               
    
    # Return false after the execution of all the loops     
    return False
          
    
    
# Test 1
lst_numbers=[1,2,3,4,5]
target_number=6

print(find_target(lst_numbers,target_number))
# Output: True
```





# Sum unique numbers from a list

All unique numbers in a list are added together. If a number appears more than once in the list, it should not be included in the total.



## Solution 1

My Solution



```python
def sum_unique_numbers(lst):
    # Create set from lst
    unique=set()
    
    for i in lst: # [1,1,2,3]
        if i in unique:
            unique.remove(i)
        else:
            unique.add(i)
            

    sum_unique=sum(unique)
    return sum_unique
    


# Test 1
numbers1 = [1, 1, 2, 3] # Ouput 5
result1 = sum_unique_numbers(numbers1)
print(result1)

# Test 2
numbers2 = [1, 2, 3] # Ouput 6
result2 = sum_unique_numbers(numbers2)
print(result2)

# Test 3
numbers3 = [1, 2, 3, 2, 4, 5, 3, 6]
result3 = sum_unique_numbers(numbers3)
            

```





## Solution 2



```python
def sum_unique_numbers(lst):
    total_sum = 0
    # Iterate through the list
    for num in lst:
        # Count occurrences of each number in the list
        if lst.count(num) == 1:
            total_sum += num
    return total_sum
    
# Test 1
numbers1 = [1, 1, 2, 3] # Ouput 5
result1 = sum_unique_numbers(numbers1)
print(result1)

# Test 2
numbers2 = [1, 2, 3] # Ouput 6
result2 = sum_unique_numbers(numbers2)
print(result2)

# Test 3
numbers3 = [1, 2, 3, 2, 4, 5, 3, 6]
result3 = sum_unique_numbers(numbers3)
print(result3)

```



