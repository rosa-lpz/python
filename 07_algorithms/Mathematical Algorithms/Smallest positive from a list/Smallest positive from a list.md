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

