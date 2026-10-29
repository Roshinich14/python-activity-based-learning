# Railway Fare and Reservation Calculator

def calculate_basic_fare(distance):
    if distance <= 100:
        fare = distance * 2
    elif distance <= 300:
        fare = (100 * 2) + ((distance - 100) * 1.5)
    else:
        fare = (100 * 2) + (200 * 1.5) + ((distance - 300) * 1)

    return fare


print("RAILWAY FARE AND RESERVATION CALCULATOR")

distance = int(input("Enter travel distance in km: "))
passengers = int(input("Enter number of passengers: "))

print("\nSelect Travel Class:")
print("1. Sleeper")
print("2. AC 3-Tier")
print("3. AC 2-Tier")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    class_name = "Sleeper"
    multiplier = 1
elif choice == 2:
    class_name = "AC 3-Tier"
    multiplier = 2
elif choice == 3:
    class_name = "AC 2-Tier"
    multiplier = 3
else:
    print("Invalid travel class.")
    raise SystemExit

reservation_fee = 40
total_fare = 0

for i in range(1, passengers + 1):
    print("\nPassenger", i)
    age = int(input("Enter passenger age: "))

    basic_fare = calculate_basic_fare(distance) * multiplier

    if age < 5:
        basic_fare = 0
    elif age < 12:
        basic_fare = basic_fare * 0.50
    elif age >= 60:
        basic_fare = basic_fare * 0.80

    passenger_fare = basic_fare + reservation_fee
    total_fare += passenger_fare

    print("Passenger fare: Rs.", round(passenger_fare, 2))

print("\n========== FARE SUMMARY ==========")
print("Travel Distance:", distance, "km")
print("Travel Class:", class_name)
print("Number of Passengers:", passengers)
print("Total Ticket Fare: Rs.", round(total_fare, 2))

cancel = input("\nDo you want to cancel the reservation? (yes/no): ")

if cancel.lower() == "yes":
    penalty = total_fare * 0.25
    refund = total_fare - penalty

    print("\nCancellation Penalty: Rs.", round(penalty, 2))
    print("Refundable Amount: Rs.", round(refund, 2))
else:
    print("Cancellation not requested.")
    print("Final Amount Payable: Rs.", round(total_fare, 2))

print("\nThank you for using the calculator!")
