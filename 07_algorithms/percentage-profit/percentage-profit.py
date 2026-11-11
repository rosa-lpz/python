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

