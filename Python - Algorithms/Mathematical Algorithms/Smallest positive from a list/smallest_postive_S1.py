def smallest_positive(in_list):
    # Sort the list in ascending order
    in_list_sorted = sorted(in_list)

    # Iterate through the sorted list to find the first positive number
    for i in in_list_sorted:
        if i > 0:
            return i  # Return the first positive number

    # If no positive numbers are found, return None
    return None


print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2
