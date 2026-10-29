# Smart Parking Fee Management

from datetime import datetime
import math

print("SMART PARKING FEE MANAGEMENT")

# Vehicle rates and daily limits
rates = {
    "bike": 20,
    "car": 50,
    "bus": 80
}

daily_limits = {
    "bike": 200,
    "car": 500,
    "bus": 800
}

# Input vehicle category
vehicle = input(
    "Enter vehicle category (Bike/Car/Bus): "
).strip().lower()

if vehicle not in rates:
    print("Invalid vehicle category!")
    raise SystemExit

# Function to validate time
def get_valid_time(message):
    while True:
        time_text = input(message)

        try:
            return datetime.strptime(
                time_text, "%H:%M"
            )
        except ValueError:
            print("Invalid time! Enter time in HH:MM format.")

# Input and validate times
entry_time = get_valid_time("Enter entry time (HH:MM): ")
exit_time = get_valid_time("Enter exit time (HH:MM): ")

# Convert times into minutes
entry_minutes = entry_time.hour * 60 + entry_time.minute
exit_minutes = exit_time.hour * 60 + exit_time.minute

# Calculate parking duration
overnight = exit_minutes <= entry_minutes

if overnight:
    duration = (1440 - entry_minutes) + exit_minutes
else:
    duration = exit_minutes - entry_minutes

# Calculate billable hours
hours = math.ceil(duration / 60)

# Calculate hourly parking charge
parking_charge = hours * rates[vehicle]

# Apply daily parking limit
parking_charge = min(
    parking_charge, daily_limits[vehicle]
)

# Calculate overnight surcharge
overnight_fee = 50 if overnight else 0

# Apply long-stay penalty
penalty = 100 if duration > 12 * 60 else 0

# Calculate final fee
total_fee = parking_charge + overnight_fee + penalty

# Display parking bill
print("\n========== PARKING BILL ==========")
print("Vehicle Category:", vehicle.capitalize())
print("Entry Time:", entry_time.strftime("%H:%M"))
print("Exit Time:", exit_time.strftime("%H:%M"))
print("Parking Duration:", duration // 60, "hours",
      duration % 60, "minutes")
print("Billable Hours:", hours)
print("Hourly Parking Charge: Rs.", parking_charge)
print("Overnight Surcharge: Rs.", overnight_fee)
print("Long-Stay Penalty: Rs.", penalty)
print("Total Parking Fee: Rs.", total_fee)

print("\nThank you for using Smart Parking!")
