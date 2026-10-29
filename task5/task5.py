# Multi-Product Shopping Budget Constraint

print("MULTI-PRODUCT SHOPPING BUDGET CONSTRAINT")

budget = float(input("Enter your shopping budget: Rs. "))
n = int(input("Enter the number of products: "))

products = []

# Input product details
for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter unit price: Rs. "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity < 0:
        print("Price and quantity cannot be negative.")
        raise SystemExit

    products.append({
        "name": name,
        "price": price,
        "original_quantity": quantity,
        "quantity": quantity
    })


# Function to calculate cost and discount
def calculate_total(items):
    total = 0
    details = []

    for item in items:
        subtotal = item["price"] * item["quantity"]

        if subtotal >= 2000:
            discount_rate = 0.10
        elif item["quantity"] >= 3:
            discount_rate = 0.05
        else:
            discount_rate = 0

        discount = subtotal * discount_rate
        final_cost = subtotal - discount

        total += final_cost

        details.append({
            "name": item["name"],
            "quantity": item["quantity"],
            "subtotal": subtotal,
            "discount": discount,
            "final_cost": final_cost
        })

    return total, details


# Calculate original shopping cost
original_total, original_details = calculate_total(products)

print("\n========== ORIGINAL SHOPPING BILL ==========")

for item in original_details:
    print("\nProduct:", item["name"])
    print("Quantity:", item["quantity"])
    print("Subtotal: Rs.", round(item["subtotal"], 2))
    print("Discount: Rs.", round(item["discount"], 2))
    print("Final Cost: Rs.", round(item["final_cost"], 2))

print("\nOriginal Total: Rs.", round(original_total, 2))
print("Available Budget: Rs.", round(budget, 2))

# Reduce quantities if budget is exceeded
if original_total > budget:
    print("\nBudget exceeded. Adjusting quantities...")

    while True:
        current_total, details = calculate_total(products)

        if current_total <= budget:
            break

        # Find the most expensive product that has quantity remaining
        candidates = [
            item for item in products
            if item["quantity"] > 0
        ]

        if not candidates:
            break

        selected = max(candidates, key=lambda x: x["price"])

        selected["quantity"] -= 1

    print("\n========== RECOMMENDED SHOPPING PLAN ==========")

    for item in products:
        reduced = (
            item["original_quantity"] - item["quantity"]
        )

        print("\nProduct:", item["name"])
        print("Original Quantity:", item["original_quantity"])
        print("Recommended Quantity:", item["quantity"])
        print("Units Reduced:", reduced)

    final_total, final_details = calculate_total(products)

    print("\nOriginal Total: Rs.", round(original_total, 2))
    print("Adjusted Total: Rs.", round(final_total, 2))
    print("Budget: Rs.", round(budget, 2))
    print("Savings from Quantity Reductions: Rs.",
          round(original_total - final_total, 2))
    print("Remaining Balance: Rs.", round(budget - final_total, 2))

else:
    print("\nYour shopping is within budget.")
    print("Remaining Balance: Rs.",
          round(budget - original_total, 2))

print("\nThank you for using the shopping budget planner!")
