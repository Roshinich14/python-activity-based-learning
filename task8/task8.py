print("FOOD WASTE MONITORING SYSTEM")
print("-----------------------------")

# Get the number of days
while True:
    try:
        days = int(input("Enter number of days to monitor: "))

        if days <= 0:
            print("Number of days must be greater than zero.")
        else:
            break

    except ValueError:
        print("Please enter a valid whole number.")

# Get the acceptable wastage limit
while True:
    try:
        limit = float(input("Enter acceptable wastage limit (%): "))

        if limit < 0 or limit > 100:
            print("Enter a percentage between 0 and 100.")
        else:
            break

    except ValueError:
        print("Please enter a valid percentage.")

records = []

total_prepared = 0
total_served = 0
total_leftovers = 0

# Collect daily data
for day in range(1, days + 1):
    print("\nDay", day)

    while True:
        try:
            prepared = int(input("Enter meals prepared: "))
            served = int(input("Enter meals served: "))

            if prepared <= 0:
                print("Meals prepared must be greater than zero.")
            elif served < 0:
                print("Meals served cannot be negative.")
            elif served > prepared:
                print("Meals served cannot exceed meals prepared.")
            else:
                break

        except ValueError:
            print("Enter meals as whole numbers.")

    # Calculate leftovers and wastage percentage
    leftovers = prepared - served
    wastage = (leftovers / prepared) * 100

    # Check whether wastage exceeds the limit
    if wastage > limit:
        status = "EXCEEDS LIMIT"
    else:
        status = "ACCEPTABLE"

    records.append({
        "day": day,
        "prepared": prepared,
        "served": served,
        "leftovers": leftovers,
        "wastage": wastage,
        "status": status
    })

    total_prepared += prepared
    total_served += served
    total_leftovers += leftovers

# Calculate overall wastage percentage
overall_wastage = (total_leftovers / total_prepared) * 100

# Display daily report
print("\nFOOD WASTE REPORT")
print("-" * 78)

print(
    f"{'Day':<8}{'Prepared':<12}{'Served':<12}"
    f"{'Leftovers':<12}{'Wastage %':<14}{'Status'}"
)

print("-" * 78)

for record in records:
    print(
        f"{record['day']:<8}"
        f"{record['prepared']:<12}"
        f"{record['served']:<12}"
        f"{record['leftovers']:<12}"
        f"{record['wastage']:<14.2f}"
        f"{record['status']}"
    )

print("-" * 78)

# Display overall statistics
print("\nOVERALL SUMMARY")
print("Total meals prepared:", total_prepared)
print("Total meals served:", total_served)
print("Total leftover meals:", total_leftovers)
print("Overall wastage percentage:", round(overall_wastage, 2), "%")
print("Acceptable wastage limit:", limit, "%")

# Identify days exceeding the limit
exceeded_days = [
    record["day"]
    for record in records
    if record["wastage"] > limit
]

if exceeded_days:
    print("\nDays exceeding the acceptable limit:")

    for day in exceeded_days:
        print("Day", day)
else:
    print("\nNo days exceeded the acceptable wastage limit.")

print("\nFood waste monitoring completed.")
