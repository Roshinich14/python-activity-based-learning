# Problem Statement
The Sports Tournament Ranking System is designed to store match results, calculate team scores, and rank teams according to a specified competition policy. Teams earn points based on match outcomes: 3 points for a win, 1 point for a draw, and 0 points for a loss. The system calculates each team's total points, goal difference, and goals scored. Teams are ranked first by total points, then by goal difference, and finally by goals scored. This system helps determine tournament standings accurately and fairly.
# Objectives
1. To store team names and match results.
2. To calculate points earned by each team.
3. To calculate goals scored, goals conceded, and goal difference.
4. To rank teams according to the competition rules.
5. To display the final tournament standings.
# Assumptions
1. The tournament consists of multiple teams.
2. Each match is played between two different teams.
3. A win awards 3 points, a draw awards 1 point to each team, and a loss awards 0 points.
4. Goal difference is calculated as goals scored minus goals conceded.
5. Teams are ranked using the following order:
   - First: Total points in descending order.
   - Second: Goal difference in descending order.
   - Third: Total goals scored in descending order.
6. If all three values are equal, the teams share the same ranking position.
7. Goals scored must be non-negative integers.
# Algorithm
1. Start the program.
2. Read the number of teams and initialize each team's statistics to zero.
3. Read the number of matches.
4. For every match, input the two team names and their goals.
5. Validate the team names and goal values.
6. Compare the goals scored by both teams.
7. Award 3 points to the winning team, or 1 point to each team if the match is a draw.
8. Update goals scored and goals conceded for both teams.
9. Calculate goal difference for every team.
10. Sort teams by total points, goal difference, and goals scored in descending order.
11. Assign ranking positions, allowing teams with identical statistics to share a rank.
12. Display the final tournament table.
13. Stop the program.
14. ```mermaid flowchart
    flowchart TD
    A([Start]) --> B[Enter team names]
    B --> C[Initialize team statistics]
    C --> D[Enter number of matches]
    D --> E[Enter match results]
    E --> F{Are team names and goals valid?}
    F -- No --> G[Display error and re-enter result]
    G --> E
    F -- Yes --> H{Compare team goals}
    H -- First team wins --> I[Award 3 points to first team]
    H -- Second team wins --> J[Award 3 points to second team]
    H -- Draw --> K[Award 1 point to each team]
    I --> L[Update goals and statistics]
    J --> L
    K --> L
    L --> M{More matches?}
    M -- Yes --> E
    M -- No --> N[Calculate goal differences]
    N --> O[Sort teams by ranking rules]
    O --> P[Display final standings]
    P --> Q([Stop])
    ```
# Sample Input
For testing, enter the following data:
Enter number of teams: 4
Enter team name 1: Tigers
Enter team name 2: Lions
Enter team name 3: Eagles
Enter team name 4: Sharks

Enter number of matches: 4

Match 1
Enter first team name: Tigers
Enter second team name: Lions
Enter goals scored by Tigers: 2
Enter goals scored by Lions: 1

Match 2
Enter first team name: Eagles
Enter second team name: Sharks
Enter goals scored by Eagles: 1
Enter goals scored by Sharks: 1

Match 3
Enter first team name: Tigers
Enter second team name: Eagles
Enter goals scored by Tigers: 0
Enter goals scored by Eagles: 2

Match 4
Enter first team name: Lions
Enter second team name: Sharks
Enter goals scored by Lions: 3
Enter goals scored by Sharks: 0

# Sample Output
FINAL TOURNAMENT STANDINGS
-------------------------------------------------------------------------------------
Rank  Team           P    W    D    L    GF    GA    GD    Points
-------------------------------------------------------------------------------------
1     Eagles         2    1    1    0    3     1     2     4
2     Tigers         2    1    0    1    2     3     -1    3
2     Lions          2    1    0    1    4     2     2     3
4     Sharks         2    0    1    1    1     4     -3    1
-------------------------------------------------------------------------------------
Tournament ranking completed successfully.

