number = 5
lst = [1, 2, 3, 4, 5]
lst_set = set(lst)  # Convert list to set
if number in lst_set:
    print("Number is in the list")
else:
    print("Number is not in the list")