# Problem Statement
The Food Waste Monitoring System is designed to monitor food preparation, consumption, and leftovers over several days. The system records the number of meals prepared and meals served each day, calculates the number of leftover meals, and determines the food wastage percentage. It compares the wastage percentage against a predefined acceptable limit and identifies days when food waste exceeds that limit. This system helps cafeterias, hostels, restaurants, and canteens reduce food waste and improve meal planning.
# Objectives
1. To record the number of meals prepared and served each day.
2. To calculate the number of leftover meals.
3. To calculate the daily food wastage percentage.
4. To compare wastage percentages against an acceptable limit.
5. To identify days with excessive food waste.
6. To calculate the total wastage percentage over the monitoring period.
# Assumptions
1. The system monitors food waste over multiple days.
2. The number of meals prepared must be a positive integer.
3. The number of meals served must be a non-negative integer.
4. Meals served cannot exceed meals prepared.
5. Leftover meals are calculated as:
   Leftover Meals = Meals Prepared − Meals Served
6. Food wastage percentage is calculated as:
   Wastage Percentage = (Leftover Meals / Meals Prepared) × 100
7. The acceptable wastage limit is entered by the user as a percentage between 0 and 100.
8. A day is flagged when its wastage percentage is greater than the acceptable limit. A percentage equal to the limit is acceptable.
# Algorithm
1. Start the program.
2. Input the number of days to monitor.
3. Input the acceptable food wastage percentage.
4. For each day:
   - Enter the number of meals prepared.
   - Enter the number of meals served.
   - Validate the input values.
   - Calculate leftover meals.
   - Calculate the wastage percentage.
   - Compare the wastage percentage with the acceptable limit.
   - Record whether the day exceeds the limit.
5. Calculate total meals prepared, total meals served, and total leftovers.
6. Calculate the overall wastage percentage.
7. Display daily food waste statistics.
8. ```mermaid flowchart
   flowchart TD
    A([Start]) --> B[Enter number of days]
    B --> C[Enter acceptable wastage limit]
    C --> D[Enter meals prepared and served]
    D --> E{Are inputs valid?}
    E -- No --> F[Display error and re-enter values]
    F --> D
    E -- Yes --> G[Calculate leftover meals]
    G --> H[Calculate wastage percentage]
    H --> I{Wastage exceeds limit?}
    I -- Yes --> J[Mark day as exceeding limit]
    I -- No --> K[Mark day as acceptable]
    J --> L[Store daily statistics]
    K --> L
    L --> M{More days to process?}
    M -- Yes --> D
    M -- No --> N[Calculate overall wastage percentage]
    N --> O[Display daily and overall results]
    O --> P[Identify days exceeding limit]
    P --> Q([Stop])
   ```
# Sample Input
Assume the acceptable food wastage limit is 20% and the system monitors four days.
Enter number of days to monitor: 4
Enter acceptable wastage limit (%): 20

Day 1
Enter meals prepared: 100
Enter meals served: 90

Day 2
Enter meals prepared: 120
Enter meals served: 90

Day 3
Enter meals prepared: 80
Enter meals served: 72

Day 4
Enter meals prepared: 150
Enter meals served: 105

# Sample Output
FOOD WASTE REPORT
------------------------------------------------------------------------------

Day     Prepared    Served      Leftovers   Wastage %    Status
------------------------------------------------------------------------------
1       100         90          10          10.00        ACCEPTABLE
2       120         90          30          25.00        EXCEEDS LIMIT
3       80          72          8           10.00        ACCEPTABLE
4       150         105         45          30.00        EXCEEDS LIMIT
------------------------------------------------------------------------------

OVERALL SUMMARY
Total meals prepared: 450
Total meals served: 357
Total leftover meals: 93
Overall wastage percentage: 20.67 %
Acceptable wastage limit: 20.0 %

Days exceeding the acceptable limit:
Day 2
Day 4

Food waste monitoring completed.
9. Display the days exceeding the acceptable limit.
10. Display the overall wastage percentage.
11. Stop the program.
