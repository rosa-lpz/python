def highest_positive(in_list):
    # Sort the list in ascending order
    in_list_sorted = sorted(in_list)

    if in_list_sorted[-1] >0:
        return in_list_sorted[-1]
    else:
        return None


print(highest_positive([4, -6, 7, 2, -4, 10]))
# Ordered -6, -4, 2, 4, 7,10
# Correct output: 10

print(highest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# -.1,.2, 3, 5, 6,  7, 7
# Correct output: 7
