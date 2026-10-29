# Campus Event Financial Planning

import math

print("CAMPUS EVENT FINANCIAL PLANNING")

venue_cost = float(input("Enter venue cost: Rs. "))
equipment_cost = float(input("Enter equipment cost: Rs. "))
catering_cost = float(input("Enter catering cost per participant: Rs. "))
transport_cost = float(input("Enter transport cost per participant: Rs. "))
certificate_cost = float(input("Enter certificate cost per participant: Rs. "))

participants = int(input("Enter expected number of participants: "))
sponsorship = float(input("Enter sponsorship amount: Rs. "))
registration_fee = float(input("Enter registration fee per participant: Rs. "))

# Calculate expenses
fixed_cost = venue_cost + equipment_cost

variable_cost = (
    catering_cost + transport_cost + certificate_cost
)

total_variable_cost = variable_cost * participants
total_budget = fixed_cost + total_variable_cost

# Calculate participant contributions and available funds
participant_contribution = registration_fee * participants
total_funds = participant_contribution + sponsorship

# Calculate surplus or sponsorship shortfall
if total_funds >= total_budget:
    surplus = total_funds - total_budget
    shortfall = 0
else:
    surplus = 0
    shortfall = total_budget - total_funds

# Calculate break-even registration count
if registration_fee > variable_cost:
    required_participants = max(
        0,
        math.ceil(
            (fixed_cost - sponsorship) /
            (registration_fee - variable_cost)
        )
    )
    print(
        "\nMinimum registrations required to break even:",
        required_participants
    )
else:
    required_participants = None
    print(
        "\nBreak-even is not possible with the given "
        "registration fee and variable cost per participant."
    )

# Display financial summary
print("\n========== EVENT FINANCIAL SUMMARY ==========")
print("Venue Cost: Rs.", round(venue_cost, 2))
print("Equipment Cost: Rs.", round(equipment_cost, 2))
print("Total Fixed Cost: Rs.", round(fixed_cost, 2))
print("Variable Cost per Participant: Rs.", round(variable_cost, 2))
print("Total Variable Cost: Rs.", round(total_variable_cost, 2))
print("Total Event Budget: Rs.", round(total_budget, 2))
print("Participant Contributions: Rs.", round(participant_contribution, 2))
print("Sponsorship Amount: Rs.", round(sponsorship, 2))
print("Total Available Funds: Rs.", round(total_funds, 2))
print("Sponsorship Shortfall: Rs.", round(shortfall, 2))
print("Budget Surplus: Rs.", round(surplus, 2))

print("\nThank you for using the planner!")
