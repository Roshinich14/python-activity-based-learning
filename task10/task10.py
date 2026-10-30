print("MULTI-CRITERIA LIBRARY RESOURCE DISTRIBUTION")
print("---------------------------------------------")

# Enter the total available copies
while True:
    try:
        available_copies = int(
            input("Enter total available book copies: ")
        )

        if available_copies < 0:
            print("Available copies cannot be negative.")
        else:
            break

    except ValueError:
        print("Please enter a valid whole number.")

# Enter the number of branches
while True:
    try:
        n = int(input("Enter number of library branches: "))

        if n <= 0:
            print("Enter at least one library branch.")
        else:
            break

    except ValueError:
        print("Please enter a valid whole number.")

branches = []
branch_names = set()

# Collect branch details
for i in range(n):
    print("\nBranch", i + 1)

    while True:
        name = input("Enter branch name: ").strip()

        if name == "":
            print("Branch name cannot be empty.")
        elif name in branch_names:
            print("Branch name already exists. Enter a unique name.")
        else:
            branch_names.add(name)
            break

    # Enter borrowing demand
    while True:
        try:
            demand = int(input("Enter number of copies requested: "))

            if demand < 0:
                print("Demand cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid whole number.")

    # Enter priority level
    while True:
        try:
            priority = int(input("Enter priority level (1 = highest): "))

            if priority <= 0:
                print("Priority must be a positive integer.")
            else:
                break

        except ValueError:
            print("Please enter a valid priority number.")

    branches.append({
        "name": name,
        "demand": demand,
        "priority": priority,
        "allocated": 0,
        "unmet": 0
    })

# Sort branches by priority.
# Branches with equal priority retain their entry order.
branches.sort(key=lambda branch: branch["priority"])

remaining_copies = available_copies
total_demand = 0
total_allocated = 0
total_unmet = 0

# Allocate copies according to priority
for branch in branches:
    demand = branch["demand"]

    allocated = min(demand, remaining_copies)
    unmet = demand - allocated

    branch["allocated"] = allocated
    branch["unmet"] = unmet

    remaining_copies -= allocated

    total_demand += demand
    total_allocated += allocated
    total_unmet += unmet

# Display the allocation report
print("\nLIBRARY RESOURCE ALLOCATION REPORT")
print("-" * 78)

print(
    f"{'Branch':<15}{'Priority':<12}{'Demand':<12}"
    f"{'Allocated':<13}{'Unmet Demand':<15}"
)

print("-" * 78)

for branch in branches:
    print(
        f"{branch['name']:<15}"
        f"{branch['priority']:<12}"
        f"{branch['demand']:<12}"
        f"{branch['allocated']:<13}"
        f"{branch['unmet']:<15}"
    )

print("-" * 78)

# Display summary
print("\nOVERALL SUMMARY")
print("Total available copies:", available_copies)
print("Total borrowing demand:", total_demand)
print("Total copies allocated:", total_allocated)
print("Total unmet demand:", total_unmet)
print("Remaining unallocated copies:", remaining_copies)

if total_unmet > 0:
    print("Status: Some branches have unmet demand.")
else:
    print("Status: All branch demands have been satisfied.")

print("\nLibrary resource distribution completed.")
