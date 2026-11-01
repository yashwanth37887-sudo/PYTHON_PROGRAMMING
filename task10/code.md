1. Problem Statement
The Integrated E-Commerce Order Processing and Reconciliation system is designed to manage online product orders efficiently.

The system processes customer orders, applies discounts, manages product dispatches, handles product returns, and updates stock quantities. It calculates the total revenue generated from successful orders and identifies discrepancies between ordered, dispatched, returned, and available stock quantities.

Finally, the system generates a detailed inventory summary containing product names, initial stock, dispatched quantities, returned quantities, remaining stock, total revenue, and any stock discrepancies.

Objectives:
1. Accept product details and customer orders.
2. Calculate order amounts and apply discounts.
3. Process product dispatches.
4. Handle product returns.
5. Update inventory automatically.
6. Calculate total revenue.
7. Identify stock discrepancies.
8. Generate a final inventory report.
2. Algorithm
1. Start the program.
2. Initialize product details with product ID, name, price, and available stock.
3. Display the available products.
4. Accept customer order details.
5. Validate the product ID and requested quantity.
6. Calculate the total order amount.
7. Apply the discount percentage.
8. Calculate the final amount after discount.
9. Update the stock after successful dispatch.
10. Record the dispatched quantity and revenue.
11. Accept product return details.
12. Update inventory by adding returned quantities.
13. Calculate the final stock for each product.
14. Compare expected stock with actual stock.
15. Identify any inventory discrepancies.
16. Calculate total revenue.
17. Display the final inventory summary.
18. Stop the program.
19. flowchart:(mermaid):
20. 
flowchart TD
    A([Start]) --> B[Initialize Product Inventory]
    B --> C[Display Available Products]
    C --> D[Enter Customer Order]
    D --> E{Valid Product and Quantity?}

    E -- No --> F[Display Invalid Order Message]
    F --> D

    E -- Yes --> G[Calculate Order Amount]
    G --> H[Apply Discount]
    H --> I[Calculate Final Amount]
    I --> J[Process Product Dispatch]
    J --> K[Update Available Stock]
    K --> L[Record Revenue and Dispatch]

    L --> M{More Orders?}
    M -- Yes --> D
    M -- No --> N[Enter Product Returns]

    N --> O{Valid Return?}
    O -- Yes --> P[Update Returned Stock]
    O -- No --> Q[Display Invalid Return]

    Q --> N
    P --> R[Calculate Final Inventory]
    R --> S[Identify Stock Discrepancies]
    S --> T[Calculate Total Revenue]
    T --> U[Generate Inventory Summary]
    U --> V([Stop])




5. Sample Input
The following example demonstrates two customer orders and one product return.

Initial inventory:
Product ID	Product	Price	Stock
101	Laptop	₹50,000	20
102	Mobile	₹20,000	30
103	Headphones	₹2,000	50

Customer order 1:
Enter Your Choice: 2
Enter Product ID: 101
Enter Order Quantity: 2
Enter Discount (%): 10


Customer order 2:
Enter Your Choice: 2
Enter Product ID: 102
Enter Order Quantity: 3
Enter Discount (%): 5


Product return:
Enter Your Choice: 3
Enter Product ID for Return: 101
Enter Return Quantity: 1


Generate inventory report:
Enter Your Choice: 4


6. Sample Output
===== E-COMMERCE MANAGEMENT SYSTEM =====

ORDER SUCCESSFUL
Product: Laptop
Total Amount: Rs. 100000
Discount: Rs. 10000
Final Amount: Rs. 90000
Dispatch Quantity: 2

ORDER SUCCESSFUL
Product: Mobile
Total Amount: Rs. 60000
Discount: Rs. 3000
Final Amount: Rs. 57000
Dispatch Quantity: 3

RETURN SUCCESSFUL
Product: Laptop
Returned Quantity: 1
Updated Stock: 19

========== FINAL INVENTORY REPORT ==========

ID      Product        Initial   Sold      Returned  Final
-----------------------------------------------------------------
101     Laptop         20        2         1         19
Stock Status: Matched

102     Mobile         30        3         0         27
Stock Status: Matched

103     Headphones     50        0         0         50
Stock Status: Matched

-----------------------------------------------------------------
Total Orders: 2
Total Revenue: Rs. 147000.0
============================================

Thank you for using the system!


7. Expected Result
The Integrated E-Commerce Order Processing and Reconciliation System successfully:
- Processes customer orders.
- Calculates discounts and final prices.
- Updates stock after dispatch.
- Processes product returns.
- Calculates total revenue.
- Checks inventory discrepancies.
- Generates a final inventory summary.
Final Revenue Calculation:
\[
Revenue = 90000 + 57000
\]

\[
\boxed{Revenue = ₹1,47,000}
\]

Final Inventory:
Product	Initial Stock	Sold	Returned	Final Stock
Laptop	20	2	1	19
Mobile	30	3	0	27
Headphones	50	0	0	50

Expected result: Successful
The program demonstrates an integrated order processing and inventory reconciliation system using basic Python programming concepts such as dictionaries, lists, loops, conditional statements, functions, and arithmetic operations.












Is this conversation helpful so far?
