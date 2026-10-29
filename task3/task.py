# Multi-Currency Travel Budget Analysis

print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")

budget = float(input("Enter planned travel budget in INR: Rs. "))
n = int(input("Enter number of expense categories: "))

categories = []
total_expense = 0

for i in range(n):
    print("\nExpense Category", i + 1)

    name = input("Enter category name: ")
    amount = float(input("Enter expense amount in foreign currency: "))
    rate = float(input("Enter exchange rate to INR: "))
    fee_percent = float(input("Enter conversion fee percentage: "))

    # Convert expense into INR
    converted_amount = amount * rate

    # Calculate conversion fee
    conversion_fee = converted_amount * fee_percent / 100

    # Calculate final expense
    final_expense = converted_amount + conversion_fee

    categories.append((name, converted_amount,
                       conversion_fee, final_expense))

    total_expense += final_expense

    print("Converted Amount: Rs.", round(converted_amount, 2))
    print("Conversion Fee: Rs.", round(conversion_fee, 2))
    print("Final Expense: Rs.", round(final_expense, 2))

# Identify largest expense category
largest_category = max(categories, key=lambda x: x[3])

# Compare expenditure with budget
print("\n========== TRAVEL BUDGET SUMMARY ==========")

print("Planned Budget: Rs.", round(budget, 2))

for category in categories:
    print(category[0], ": Rs.", round(category[3], 2))

print("Total Travel Expenditure: Rs.",
      round(total_expense, 2))

print("Largest Expense Category:",
      largest_category[0])

print("Largest Category Expense: Rs.",
      round(largest_category[3], 2))

if total_expense <= budget:
    balance = budget - total_expense
    print("Budget Status: Within Budget")
    print("Remaining Balance: Rs.", round(balance, 2))
else:
    excess = total_expense - budget
    print("Budget Status: Budget Exceeded")
    print("Excess Amount: Rs.", round(excess, 2))

print("\nThank you for using the travel budget analyzer!")
