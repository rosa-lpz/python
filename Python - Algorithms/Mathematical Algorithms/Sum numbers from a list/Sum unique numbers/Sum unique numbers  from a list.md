# Sum unique numbers from a list

All unique numbers in a list are added together. If a number appears more than once in the list, it should not be included in the total.



**Examples**

```cmd
Example 1
Input: [1,1,2,3]
Output: 5
```



```cmd
Example 2
Input: [1,,2,3]
Output: 6
```





# Python

## Solution 1

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



```python
# instead of sum_unique, the sum of unique set elements was done:
sum=0
    for i in unique:
        sum+=i
    return sum

```





### Test Cases

#### Test 1

```python
list1=[1,1,2,3] # Output 5
sum(list1)
```

Output

```python
5
```



#### Test 2

```python
list2=[1,2,3] # Output 6
sum(list2)
```

Output

```python
6
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



### Test Cases

#### Test 1

```python
numbers1 = [1, 1, 2, 3] # Ouput 5
result1 = sum_unique_numbers(numbers)
print(result1)
```



#### Test 2

```python
numbers2 = [1, 2, 3] # Ouput 6
result2 = sum_unique_numbers(numbers)
print(result2)
```



#### Test 3

```python
numbers3 = [1, 2, 3, 2, 4, 5, 3, 6] # Output 16
result3 = sum_unique_numbers(numbers)
print(result3)
```





### Explanation

- The `count()` method is used on the list to check how many times each number appears.
- If the count of the number is exactly 1, it gets added to the `total_sum`.

In the example list `[1, 2, 3, 2, 4, 5, 3, 6]`, the numbers `1, 4, 5, 6` will be included in the sum, while `2` and `3` are excluded because they appear more than once.



## Solution 3



```python
def sum_unique_numbers(lst):
    # Create a set of numbers that appear more than once
    duplicates = {num for num in lst if lst.count(num) > 1}
    
    # Sum the numbers that are not in the duplicates set
    total_sum = sum(num for num in lst if num not in duplicates)
    
    return total_sum

```



### Test Cases

#### Test 1

```python
numbers1 = [1, 1, 2, 3] # Ouput 5
result1 = sum_unique_numbers(numbers)
print(result1)
```



#### Test 2

```python
numbers2 = [1, 2, 3] # Ouput 6
result2 = sum_unique_numbers(numbers)
print(result2)
```



#### Test 3

```python
numbers3 = [1, 2, 3, 2, 4, 5, 3, 6] # Output 16
result3 = sum_unique_numbers(numbers)
print(result3)
```





### Explanation

- **Creating the `duplicates` set**: This set is created by iterating over the list and including numbers that appear more than once.
- **Summing unique numbers**: The `sum()` function is used to add numbers that are **not** in the `duplicates` set.

For the list `[1, 2, 3, 2, 4, 5, 3, 6]`, the numbers `1, 4, 5, 6` will be included in the sum, while `2` and `3` are excluded because they appear more than once.





## Solution 3 v2 (with not set comprehensions)



```python
def sum_unique_numbers(lst):
    # Create an empty set to store duplicates
    duplicates = set()
    
    # Create an empty set to store numbers we've already seen
    seen = set()

    # Loop through the list to identify duplicates
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    # Sum the numbers that are not in the duplicates set
    total_sum = 0
    for num in lst:
        if num not in duplicates:
            total_sum += num
    
    return total_sum


```



### Test Cases

#### Test 1

```python
numbers1 = [1, 1, 2, 3] # Ouput 5
result1 = sum_unique_numbers(numbers)
print(result1)
```



#### Test 2

```python
numbers2 = [1, 2, 3] # Ouput 6
result2 = sum_unique_numbers(numbers)
print(result2)
```



#### Test 3

```python
numbers3 = [1, 2, 3, 2, 4, 5, 3, 6] # Output 16
result3 = sum_unique_numbers(numbers)
print(result3)
```





### Explanation

1. **`duplicates` set**: We initialize an empty set `duplicates` to store the numbers that appear more than once.

2. **`seen` set**: We use a `seen` set to track the numbers we've already encountered as we loop through the list.

3. **First loop**: We iterate through the list. If a number has already been encountered (i.e., it's in the `seen` set), it's added to the `duplicates` set. If it's the first time we encounter the number, it's added to the `seen` set.

4. ## **Second loop**: After identifying the duplicates, we iterate through the list again and sum only those numbers that are **not** in the `duplicates` set.
