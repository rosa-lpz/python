# Percentage profit

- The function `calculate_percentage_profit()` accepts two parameters: `income` and `expenditure`.
- It checks whether the `expenditure` is zero, because division by zero is not allowed. If expenditure is zero, it returns an error message.
- It calculates the percentage profit using the formula and returns the result.
- Example Usage:

 

```python
# Function to calculate percentage profit
def calculate_percentage_profit(income, expenditure):
    # Check if expenditure is zero to avoid division by zero error
    if expenditure == 0:
        return "Expenditure cannot be zero."
    
    # Calculate percentage profit using the formula
    percentage_profit = ((income - expenditure) / expenditure) * 100
    
    return percentage_profit

# Example usage:
income = float(input("Enter the income: "))
expenditure = float(input("Enter the expenditure: "))

# Calculate and display the percentage profit
result = calculate_percentage_profit(income, expenditure)

print(f"Percentage Profit: {result:.2f}%")

```

**Input:**

```
Enter the income: 1500
Enter the expenditure: 1000
```

**Output**

```
Percentage Profit: 50.00%
```



