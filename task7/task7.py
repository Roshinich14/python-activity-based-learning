print("SPORTS TOURNAMENT RANKING SYSTEM")
print("---------------------------------")

# Enter the team names
n = int(input("Enter number of teams: "))

teams = {}

for i in range(n):
    name = input("Enter team name " + str(i + 1) + ": ")

    while name in teams or name.strip() == "":
        print("Invalid or duplicate team name. Enter a different name.")
        name = input("Enter team name " + str(i + 1) + ": ")

    teams[name] = {
        "points": 0,
        "goals_scored": 0,
        "goals_conceded": 0,
        "goal_difference": 0,
        "played": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0
    }

# Enter the match details
matches = int(input("Enter number of matches: "))

for i in range(matches):
    print("\nMatch", i + 1)

    while True:
        team1 = input("Enter first team name: ")
        team2 = input("Enter second team name: ")

        if team1 not in teams or team2 not in teams:
            print("Error: Enter team names from the registered teams.")
        elif team1 == team2:
            print("Error: A team cannot play against itself.")
        else:
            break

    while True:
        try:
            goals1 = int(input("Enter goals scored by " + team1 + ": "))
            goals2 = int(input("Enter goals scored by " + team2 + ": "))

            if goals1 < 0 or goals2 < 0:
                print("Goals cannot be negative. Try again.")
            else:
                break

        except ValueError:
            print("Please enter goals as whole numbers.")

    # Update match statistics
    teams[team1]["played"] += 1
    teams[team2]["played"] += 1

    teams[team1]["goals_scored"] += goals1
    teams[team1]["goals_conceded"] += goals2

    teams[team2]["goals_scored"] += goals2
    teams[team2]["goals_conceded"] += goals1

    # Award points based on the match result
    if goals1 > goals2:
        teams[team1]["points"] += 3
        teams[team1]["wins"] += 1
        teams[team2]["losses"] += 1

    elif goals2 > goals1:
        teams[team2]["points"] += 3
        teams[team2]["wins"] += 1
        teams[team1]["losses"] += 1

    else:
        teams[team1]["points"] += 1
        teams[team2]["points"] += 1
        teams[team1]["draws"] += 1
        teams[team2]["draws"] += 1

# Calculate goal difference
for name in teams:
    teams[name]["goal_difference"] = (
        teams[name]["goals_scored"]
        - teams[name]["goals_conceded"]
    )

# Sort by points, goal difference, and goals scored
ranking = sorted(
    teams.items(),
    key=lambda item: (
        item[1]["points"],
        item[1]["goal_difference"],
        item[1]["goals_scored"]
    ),
    reverse=True
)

# Display the final standings
print("\nFINAL TOURNAMENT STANDINGS")
print("-" * 85)

print(
    f"{'Rank':<6}{'Team':<15}{'P':<5}{'W':<5}"
    f"{'D':<5}{'L':<5}{'GF':<6}{'GA':<6}"
    f"{'GD':<6}{'Points':<8}"
)

print("-" * 85)

previous_stats = None
rank = 0

for position, (name, stats) in enumerate(ranking, start=1):
    current_stats = (
        stats["points"],
        stats["goal_difference"],
        stats["goals_scored"]
    )

    if current_stats != previous_stats:
        rank = position

    print(
        f"{rank:<6}{name:<15}{stats['played']:<5}"
        f"{stats['wins']:<5}{stats['draws']:<5}"
        f"{stats['losses']:<5}{stats['goals_scored']:<6}"
        f"{stats['goals_conceded']:<6}"
        f"{stats['goal_difference']:<6}"
        f"{stats['points']:<8}"
    )

    previous_stats = current_stats

print("-" * 85)
print("Tournament ranking completed successfully.")
