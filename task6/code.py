import math

# Define coordinates as tuples
coordinates = [(0, 0), (3, 4), (6, 8), (12, 8), (12, 16)]

# Initialize distance list
distances = []

# Calculate distances between successive coordinate pairs
for i in range(len(coordinates) - 1):

    x1, y1 = coordinates[i]
    x2, y2 = coordinates[i + 1]

    # Calculate Euclidean distance
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Store distance
    distances.append(distance)

# Find maximum distance
max_distance = max(distances)

# Identify longest route segment
index = distances.index(max_distance)

# Display all distances
print("Distances between successive coordinates:")

for i in range(len(distances)):
    print(f"{coordinates[i]} to {coordinates[i+1]} = {distances[i]:.2f}")

# Display longest route segment
print("\nLongest Route Segment:")
print("From:", coordinates[index])
print("To:", coordinates[index + 1])
print("Maximum Distance:", round(max_distance, 2))
