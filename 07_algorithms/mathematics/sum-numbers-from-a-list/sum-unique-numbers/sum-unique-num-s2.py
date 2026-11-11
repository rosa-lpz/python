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