
import math

# Store geographical coordinates as tuples
locations = [
    (10, 20),
    (15, 25),
    (20, 30),
    (22, 40),
    (30, 45)
]

# List to store distances
distances = []

# Calculate distance between successive locations
for i in range(len(locations) - 1):
    x1, y1 = locations[i]
    x2, y2 = locations[i + 1]

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    distances.append(distance)

# Display distances
print("Route Segment Distances:")

for i in range(len(distances)):
    print(
        f"Location {i+1} to Location {i+2}: "
        f"{distances[i]:.2f}"
    )

# Find the longest route segment
max_distance = max(distances)
max_index = distances.index(max_distance)

print("\nLongest Route Segment:")
print(f"From: {locations[max_index]}")
print(f"To: {locations[max_index + 1]}")
print(f"Distance: {max_distance:.2f}")

