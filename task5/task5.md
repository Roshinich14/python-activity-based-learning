# Problem Statement
Develop a Python program for Multi-Product Shopping Budget Constraint to help customers manage their shopping expenses within a fixed budget. The program should accept the number of products, product names, unit prices, and quantities. It should calculate the total cost of each product, apply discounts according to predefined conditions, and determine the final shopping cost. The program must compare the final cost with the available budget and identify the products whose quantities can be reduced to bring the total expenditure within the budget. Finally, it should display the product-wise cost, discounts, total expenditure, budget difference, and recommended quantity reductions.
# Algorithm
1. Start the program.
2. Input the customer's shopping budget.
3. Input the number of products to be purchased.
4. For each product:
   - Enter the product name.
   - Enter its unit price.
   - Enter the required quantity.
5. Calculate the original cost of each product by multiplying its unit price by its quantity.
6. Apply the predefined discount conditions.
7. Calculate the total shopping cost after discounts.
8. Compare the total shopping cost with the available budget.
9. If the total cost is within the budget, display the remaining balance.
10. Otherwise, calculate the amount exceeding the budget.
11. Identify products whose quantities can be reduced to decrease the total cost.
12. Recommend quantity reductions until the estimated cost is within the budget.
13. Display the original shopping cost, discounts, final cost, budget difference, and recommended changes.
14. Stop the program.
15. ```mermaid flowchart
    flowchart TD
    A([Start]) --> B[/Enter shopping budget/]
    B --> C[/Enter number of products/]
    C --> D[Input product names, prices and quantities]
    D --> E[Calculate product-wise subtotal]
    E --> F[Apply discount conditions]
    F --> G[Calculate total shopping cost]
    G --> H{Is total cost within budget?}
    H -- Yes --> I[Calculate remaining balance]
    H -- No --> J[Calculate excess amount]
    J --> K[Identify product with highest unit cost]
    K --> L[Reduce its quantity by one]
    L --> M[Recalculate discounts and total cost]
    M --> H
    I --> N[Display final shopping summary]
    N --> O([Stop])
    ```
# Sample Input
Consider a customer with a shopping budget of ₹2,500 who wants to purchase three products.
MULTI-PRODUCT SHOPPING BUDGET CONSTRAINT
Enter your shopping budget: Rs. 2500
Enter the number of products: 3

Product 1
Enter product name: Rice
Enter unit price: Rs. 600
Enter quantity: 2

Product 2
Enter product name: Oil
Enter unit price: Rs. 800
Enter quantity: 2

Product 3
Enter product name: Biscuits
Enter unit price: Rs. 100
Enter quantity: 3

# Sample Output
========== ORIGINAL SHOPPING BILL ==========

Product: Rice
Quantity: 2
Subtotal: Rs. 1200.0
Discount: Rs. 0.0
Final Cost: Rs. 1200.0

Product: Oil
Quantity: 2
Subtotal: Rs. 1600.0
Discount: Rs. 0.0
Final Cost: Rs. 1600.0

Product: Biscuits
Quantity: 3
Subtotal: Rs. 300.0
Discount: Rs. 15.0
Final Cost: Rs. 285.0

Original Total: Rs. 3085.0
Available Budget: Rs. 2500.0

Budget exceeded. Adjusting quantities...

========== RECOMMENDED SHOPPING PLAN ==========

Product: Rice
Original Quantity: 2
Recommended Quantity: 2
Units Reduced: 0

Product: Oil
Original Quantity: 2
Recommended Quantity: 1
Units Reduced: 1

Product: Biscuits
Original Quantity: 3
Recommended Quantity: 3
Units Reduced: 0

Original Total: Rs. 3085.0
Adjusted Total: Rs. 2285.0
Budget: Rs. 2500.0
Savings from Quantity Reductions: Rs. 800.0
Remaining Balance: Rs. 215.0

Thank you for using the shopping budget planner!
