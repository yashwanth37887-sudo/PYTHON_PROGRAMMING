
from datetime import datetime
import math

# Parking rates per hour
vehicle_rates = {
    "bike": 20,
    "car": 50,
    "truck": 80
}

# Maximum daily parking charges
daily_limit = {
    "bike": 150,
    "car": 400,
    "truck": 600
}

# Penalty for exceeding 24 hours
penalty = 200

# Maximum allowed parking duration in hours
allowed_hours = 24

print("================================")
print("   SMART PARKING FEE MANAGEMENT")
print("================================")

# Get vehicle category
while True:
    vehicle = input(
        "Enter vehicle category (Bike/Car/Truck): "
    ).lower()

    if vehicle in vehicle_rates:
        break
    else:
        print("Invalid vehicle category. Try again.")

# Get and validate entry and exit times
date_format = "%Y-%m-%d %H:%M"

while True:
    try:
        entry = datetime.strptime(
            input("Enter entry time (YYYY-MM-DD HH:MM): "),
            date_format
        )

        exit_time = datetime.strptime(
            input("Enter exit time (YYYY-MM-DD HH:MM): "),
            date_format
        )

        if exit_time <= entry:
            print("Error: Exit time must be after entry time.")
            continue

        break

    except ValueError:
        print("Invalid date or time format. Try again.")

# Calculate parking duration
duration = (exit_time - entry).total_seconds() / 3600

# Calculate parking days
days = math.ceil(duration / 24)

# Calculate total parking fee
rate = vehicle_rates[vehicle]

total_fee = 0
remaining_hours = duration

# Apply daily maximum limit
for day in range(days):
    hours = min(remaining_hours, 24)

    daily_fee = hours * rate

    daily_fee = min(
        daily_fee,
        daily_limit[vehicle]
    )

    total_fee += daily_fee
    remaining_hours -= hours

# Calculate penalty
if duration > allowed_hours:
    total_penalty = penalty
else:
    total_penalty = 0

# Final amount
final_amount = total_fee + total_penalty

# Display parking bill
print("\n========== PARKING BILL ==========")
print("Vehicle Category :", vehicle.capitalize())
print("Entry Time       :", entry)
print("Exit Time        :", exit_time)
print("Parking Duration :", round(duration, 2), "hours")
print("Parking Days     :", days)
print("Hourly Rate      : Rs.", rate)
print("Parking Fee      : Rs.", total_fee)
print("Penalty          : Rs.", total_penalty)
print("---------------------------------")
print("Final Amount     : Rs.", final_amount)
print("=================================")
print("Thank you for parking!")

