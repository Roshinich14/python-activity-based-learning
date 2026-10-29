# Problem Statement
Develop a Python program for Smart Parking Fee Management to calculate parking charges for vehicles using their entry and exit times. The program should accept the vehicle category, parking entry time, and exit time as inputs. It should calculate the total parking duration, apply the appropriate hourly rates for different vehicle categories, account for overnight parking, enforce daily parking limits, and apply additional penalties when specified conditions are violated. The program must validate time inputs to ensure they follow the correct format and represent valid times. Finally, it should display the vehicle details, parking duration, applicable penalties, and total parking fee.
# Algorithm
1. Start the program.
2. Define the hourly parking rates for different vehicle categories.
3. Define the daily parking limit and penalty charges.
4. Input the vehicle category.
5. Validate the vehicle category.
6. Input the entry time and exit time in 24-hour HH:MM format.
7. Validate both time inputs.
8. Convert the entry and exit times into minutes.
9. If the exit time is earlier than the entry time, consider the exit to be on the following day.
10. Calculate the total parking duration in minutes.
11. Convert the duration into billable hours by rounding up partial hours.
12. Calculate the parking fee using the selected vehicle's hourly rate.
13. Apply the daily parking limit for each 24-hour period.
14. Check whether overnight parking occurred and apply the specified overnight charge.
15. Check whether any penalty conditions apply and add the corresponding penalties.
16. Calculate the final parking fee.
17. Display the vehicle category, entry time, exit time, parking duration, parking charges, penalties, and total fee.
18. Stop the program.
19. ```mermaid flowchart
    flowchart TD
    A([Start]) --> B[Define vehicle rates and daily limits]
    B --> C[/Enter vehicle category/]
    C --> D{Is vehicle category valid?}
    D -- No --> E[Display invalid category]
    E --> Z([Stop])
    D -- Yes --> F[/Enter entry and exit times/]
    F --> G{Are times valid?}
    G -- No --> H[Display time validation error]
    H --> Z
    G -- Yes --> I[Convert times into minutes]
    I --> J{Is exit time earlier than or equal to entry?}
    J -- Yes --> K[Calculate duration across midnight]
    J -- No --> L[Calculate same-day duration]
    K --> M[Calculate billable hours]
    L --> M
    M --> N[Calculate hourly parking charge]
    N --> O[Apply daily parking limit]
    O --> P{Did parking cross midnight?}
    P -- Yes --> Q[Add overnight surcharge]
    P -- No --> R[Check long-stay penalty]
    Q --> R
    R --> S{Did duration exceed 12 hours?}
    S -- Yes --> T[Add long-stay penalty]
    S -- No --> U[Calculate final fee]
    T --> U
    U --> V[Display parking bill]
    V --> Z
    ```
# Sample Input
In this example, a car enters the parking area at 8:30 PM and exits at 10:45 AM the next day.
SMART PARKING FEE MANAGEMENT
Enter vehicle category (Bike/Car/Bus): Car
Enter entry time (HH:MM): 20:30
Enter exit time (HH:MM): 10:45

# Sample Output
========== PARKING BILL ==========
Vehicle Category: Car
Entry Time: 20:30
Exit Time: 10:45
Parking Duration: 14 hours 15 minutes
Billable Hours: 15
Hourly Parking Charge: Rs. 500
Overnight Surcharge: Rs. 50
Long-Stay Penalty: Rs. 100
Total Parking Fee: Rs. 650

Thank you for using Smart Parking!
    
    
