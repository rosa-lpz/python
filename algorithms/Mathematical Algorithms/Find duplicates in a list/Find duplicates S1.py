
def has_duplicates(lst):
    seen = set ()
    for x in lst:
        if x in seen:
            return True
        seen.add(x)
    return False



# Test 1
list1= [2,2,1,3,4,5]
print(has_duplicates(list1))