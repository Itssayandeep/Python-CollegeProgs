# Define the tuple of monthly incomes
monthly_incomes = (
    ("January", 5000), ("February", 5500),
    ("March", 6000), ("April", 5800),
    ("May", 6200), ("June", 7000),
    ("July", 7500), ("August", 7300),
    ("September", 6800), ("October", 6500),
    ("November", 6000), ("December", 5500)
)

# Calculate the total income
total_income = sum(income for month, income in monthly_incomes)

# Function to print the report
def print_report(incomes):
    print(f"Total income: {total_income}\n")
    for i in range(0, len(incomes), 3):
        quarter_income = 0
        for month, income in incomes[i:i+3]:
            print(f"{month}: {income}")
            quarter_income += income
        print("-" * 20)
        print(f"Quarter: {quarter_income}\n")

# Print the report
print_report(monthly_incomes)
