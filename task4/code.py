
# Traffic Flow and Congestion Analysis

def classify_congestion(percentage):

    if percentage < 40:
        return "Low"

    elif percentage < 70:
        return "Moderate"

    elif percentage < 100:
        return "High"

    else:
        return "Severe"


def traffic_analysis():

    roads = []

    num_roads = int(input("Enter number of roads: "))
    intervals = int(input("Enter number of time intervals: "))

    # Collect traffic data
    for i in range(num_roads):

        print("\nEnter details for Road", i + 1)

        road_name = input("Enter road name: ")
        capacity = int(input("Enter road capacity: "))

        vehicle_counts = []

        for j in range(intervals):

            count = int(input(
                f"Enter vehicle count for interval {j + 1}: "
            ))

            vehicle_counts.append(count)

        total = sum(vehicle_counts)

        peak_count = max(vehicle_counts)
        peak_interval = vehicle_counts.index(peak_count) + 1

        # Calculate congestion percentage
        percentage = (peak_count / capacity) * 100

        congestion = classify_congestion(percentage)

        # Check capacity
        if peak_count > capacity:
            status = "Over Capacity"
        else:
            status = "Within Capacity"

        roads.append({
            "name": road_name,
            "counts": vehicle_counts,
            "total": total,
            "peak": peak_count,
            "peak_interval": peak_interval,
            "percentage": percentage,
            "congestion": congestion,
            "status": status
        })

    # Display report
    print("\n========== TRAFFIC ANALYSIS REPORT ==========")

    for road in roads:

        print("\nRoad Name:", road["name"])
        print("Total Vehicles:", road["total"])
        print("Peak Vehicles:", road["peak"])
        print("Peak Time Interval:", road["peak_interval"])
        print("Congestion Percentage:",
              round(road["percentage"], 2), "%")
        print("Congestion Level:", road["congestion"])
        print("Capacity Status:", road["status"])

    # Find overall peak traffic period
    interval_totals = []

    for j in range(intervals):

        total = sum(road["counts"][j] for road in roads)
        interval_totals.append(total)

    overall_peak = max(interval_totals)
    peak_time = interval_totals.index(overall_peak) + 1

    print("\n========== OVERALL TRAFFIC ==========")
    print("Peak Traffic Interval:", peak_time)
    print("Maximum Vehicles:", overall_peak)

    print("\nRoads Exceeding Capacity:")

    found = False

    for road in roads:

        if road["status"] == "Over Capacity":
            print(road["name"])
            found = True

    if not found:
        print("No roads exceeded capacity.")

    print("\n========== END OF REPORT ==========")


# Main program
traffic_analysis()

