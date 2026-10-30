# Problem Statement
The Multi-Criteria Library Resource Distribution system manages the distribution of available book copies among multiple library branches. It analyses book availability, borrowing demand, and the requirements of each branch to allocate resources according to predefined priority rules. The system first considers branches with higher priority and then distributes available copies based on their demand. It calculates the number of copies allocated to each branch, identifies unmet demand, and reports the total shortage of books. This system helps libraries use limited resources efficiently and ensure fair distribution.
# Objectives
1. To record book availability and borrowing demand across library branches.
2. To establish priority levels for different branches.
3. To allocate available book copies according to the specified priority rules.
4. To calculate the number of copies allocated to each branch.
5. To identify unmet demand and book shortages.
6. To generate a branch-wise resource distribution report.
# Assumptions
1. The system distributes copies of one book title among multiple library branches.
2. The total number of available copies is entered by the user.
3. Each branch provides its name, borrowing demand, and priority level.
4. A lower priority number indicates higher priority: priority 1 is served before priority 2.
5. Branches with the same priority are processed in the order in which they are entered.
6. Each branch receives as many copies as possible, up to its demand, before the next branch is considered.
7. Unmet demand is calculated as:
   Unmet Demand = Requested Copies − Allocated Copies
8. The system does not allocate more copies than are available.
# Algorithm
1. Start the program.
2. Input the total number of available book copies.
3. Input the number of library branches.
4. For each branch, enter:
   - Branch name.
   - Number of copies requested.
   - Priority level.
5. Validate all input values.
6. Sort the branches by priority, with higher-priority branches processed first.
7. For each branch:
   - Compare its demand with the remaining available copies.
   - Allocate the smaller of the two values.
   - Calculate unmet demand.
   - Update the remaining available copies.
8. Calculate total demand, total allocated copies, and total unmet demand.
9. Display the branch-wise allocation report.
10. Display the remaining copies, if any.
11. Stop the program.
12. ```mermaid flowchart
    flowchart TD
    A([Start]) --> B[Enter available book copies]
    B --> C[Enter number of library branches]
    C --> D[Enter branch names, demand and priority]
    D --> E{Are inputs valid?}
    E -- No --> F[Display error and re-enter input]
    F --> D
    E -- Yes --> G[Sort branches by priority]
    G --> H[Set remaining copies to available copies]
    H --> I[Select next branch]
    I --> J[Compare branch demand with remaining copies]
    J --> K[Allocate minimum of demand and remaining copies]
    K --> L[Calculate unmet demand]
    L --> M[Update remaining copies]
    M --> N{More branches?}
    N -- Yes --> I
    N -- No --> O[Calculate total demand and unmet demand]
    O --> P[Display allocation report]
    P --> Q([Stop])
    ```
# Sample Input
Suppose a library has 50 copies of a book to distribute among three branches.
Enter total available book copies: 50
Enter number of library branches: 3

Branch 1
Enter branch name: Central
Enter number of copies requested: 25
Enter priority level (1 = highest): 1

Branch 2
Enter branch name: North
Enter number of copies requested: 20
Enter priority level (1 = highest): 2

Branch 3
Enter branch name: South
Enter number of copies requested: 15
Enter priority level (1 = highest): 1

The Central and South branches have priority 1, so they are processed first in their original entry order. The North branch has priority 2 and is processed afterward.
# Sample Output
LIBRARY RESOURCE ALLOCATION REPORT
------------------------------------------------------------------------------

Branch         Priority    Demand      Allocated    Unmet Demand
------------------------------------------------------------------------------
Central        1           25          25           0
South          1           15          15           0
North          2           20          10           10
------------------------------------------------------------------------------

OVERALL SUMMARY
Total available copies: 50
Total borrowing demand: 60
Total copies allocated: 50
Total unmet demand: 10
Remaining unallocated copies: 0
Status: Some branches have unmet demand.

Library resource distribution completed.
    
