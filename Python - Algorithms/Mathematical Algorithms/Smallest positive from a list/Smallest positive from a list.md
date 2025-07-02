# Python



## Solution 1

```python
def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.

    in_list_sorted=sorted(in_list)

    for i in in_list_sorted:
        if i > 0:
            print("Smallest positive is " + str(i))
            break
        else:
            print("No positive number"  )
```

### Output

```cmd
No positive number
No positive number
Smallest positive is 2
None
```

### Test cases

Test cases don't work because the code above prints various row on information. Is expected that only one value is return by the function.

```cmd
print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2
```

