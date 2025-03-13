def sum_unique_num(lst):
    # Create set from lst
    unique=set()
    
    for i in lst: # [1,1,2,3]
        if i in unique:
            unique.remove(i)
        else:
            unique.add(i)
            

    sum_unique=sum(unique)
    return sum_unique
    

list1=[1,1,2,3] # Output 5
print(sum_unique_num(list1))