1. Problem Statement
The Smart Parking Fee Management System is a Python-based application designed to calculate parking charges based on vehicle entry time, exit time, and vehicle category.

The system considers the following conditions:
1. Vehicle Categories: Different parking rates for cars, bikes, and trucks.
2. Entry and Exit Time: Calculates the total parking duration.
3. Overnight Parking: Supports parking across multiple days.
4. Daily Parking Limit: Applies a maximum parking fee per day.
5. Penalty Conditions: Adds a penalty if the vehicle exceeds the allowed parking duration.
6. Time Validation: Checks whether the entered date and time are valid and whether exit time is later than entry time.
The system finally displays the total parking duration, parking fee, penalty, and final amount payable.
2. Algorithm
1. Start the program.
2. Define parking rates for different vehicle categories.
3. Define the maximum daily parking limit and penalty amount.
4. Get the vehicle category from the user.
5. Get vehicle entry date and time.
6. Get vehicle exit date and time.
7. Validate the entered date and time.
8. Check whether the exit time is later than the entry time.
9. Calculate the total parking duration in hours.
10. Calculate the parking fee based on the vehicle category.
11. Calculate the number of parking days.
12. Apply the maximum daily parking limit.
13. Check whether the parking duration exceeds the allowed limit.
14. Add the penalty if applicable.
15. Calculate the final parking amount.
16. Display the parking duration, fee, penalty, and total amount.
17. Stop.
18. flowchart:(mermaid):
19. 
flowchart TD
    A([Start]) --> B[Define Vehicle Rates and Daily Limit]
    B --> C[/Enter Vehicle Category/]
    C --> D[/Enter Entry Date and Time/]
    D --> E[/Enter Exit Date and Time/]
    E --> F{Are Date and Time Valid?}
    F -- No --> G[Display Invalid Input]
    G --> D
    F -- Yes --> H{Is Exit After Entry?}
    H -- No --> I[Display Invalid Time Range]
    I --> D
    H -- Yes --> J[Calculate Parking Duration]
    J --> K[Calculate Parking Days]
    K --> L[Calculate Fee Based on Vehicle]
    L --> M[Apply Daily Parking Limit]
    M --> N{Exceeds Allowed Duration?}
    N -- Yes --> O[Add Penalty]
    N -- No --> P[No Penalty]
    O --> Q[Calculate Final Amount]
    P --> Q
    Q --> R[/Display Parking Bill/]
    R --> S([Stop])




5. Sample Input
================================
   SMART PARKING FEE MANAGEMENT
================================

Enter vehicle category (Bike/Car/Truck): car

Enter entry time (YYYY-MM-DD HH:MM):
2026-11-01 08:00

Enter exit time (YYYY-MM-DD HH:MM):
2026-11-02 10:00


6. Sample Output
========== PARKING BILL ==========

Vehicle Category : Car
Entry Time       : 2026-11-01 08:00:00
Exit Time        : 2026-11-02 10:00:00
Parking Duration : 26.0 hours
Parking Days     : 2
Hourly Rate      : Rs. 50
Parking Fee      : Rs. 800
Penalty          : Rs. 200
---------------------------------
Final Amount     : Rs. 1000
=================================
Thank you for parking!


7. Explanation of Output
For the given sample input:
- Vehicle category: Car
- Entry time: 08:00 AM on 1 November 2026.
- Exit time: 10:00 AM on 2 November 2026.
- Total parking duration: 26 hours.
- Car parking rate: ₹50 per hour.
- First day charge: ₹400 (daily maximum).
- Second day charge: ₹400 (daily maximum).
- Parking fee: ₹800.
- Penalty: ₹200 because parking exceeded 24 hours.
Therefore,
\[
\text{Final Amount} = 800 + 200
\]

\[
\boxed{\text{Final Amount} = ₹1000}
\]

8. Conclusion
The Smart Parking Fee Management System successfully calculates parking charges based on vehicle category, entry and exit times, overnight parking, daily maximum limits, and penalty conditions. It also validates user inputs to prevent incorrect time entries.

This Python application helps automate parking fee calculations and reduces manual errors in parking management.

Note: The hourly rates, daily limits, and penalty amounts are example values and can be modified according to parking facility requirements.
