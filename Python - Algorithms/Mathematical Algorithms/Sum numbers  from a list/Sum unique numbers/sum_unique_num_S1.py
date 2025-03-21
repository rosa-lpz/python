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
print(result3)