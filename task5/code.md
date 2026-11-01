. Problem Statement
Write a Python program to store geographical coordinates of multiple locations as tuples. Calculate the distance between successive locations using the Euclidean distance formula and identify the longest route segment.

The program should:
- Store latitude and longitude coordinates as tuples.
- Calculate distances between consecutive locations.
- Find the longest distance between two successive locations.
- Display all segment distances and the longest route segment.
2. Algorithm
1. Start the program.
2. Define a list of geographical coordinates using tuples.
3. Initialize an empty list to store distances.
4. Read each pair of successive coordinates.
5. Calculate the distance using the Euclidean distance formula:
\[
d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
\]

6. Store each calculated distance.
7. Find the maximum distance using the max() function.
8. Identify the corresponding route segment.
9. Display all distances and the longest route segment.
10. Stop the program.
11. flowchart:(mermaid):
12. 
flowchart TD
    A([Start]) --> B[Define coordinates as tuples]
    B --> C[Initialize distance list]
    C --> D[Select successive coordinate pairs]
    D --> E[Calculate Euclidean distance]
    E --> F[Store calculated distance]
    F --> G{More coordinate pairs?}
    G -- Yes --> D
    G -- No --> H[Find maximum distance]
    H --> I[Identify longest route segment]
    I --> J[Display all distances]
    J --> K[Display longest segment]
    K --> L([Stop])

13. 
5. Sample Input
The geographical coordinates are stored as tuples in the program:
Location 1 = (10, 20)
Location 2 = (15, 25)
Location 3 = (20, 30)
Location 4 = (22, 40)
Location 5 = (30, 45)


6. Sample Output
Route Segment Distances:
Location 1 to Location 2: 7.07
Location 2 to Location 3: 7.07
Location 3 to Location 4: 10.20
Location 4 to Location 5: 9.43

Longest Route Segment:
From: (20, 30)
To: (22, 40)
Distance: 10.20
7. Result
Thus, the Python program successfully stores geographical coordinates as tuples, calculates distances between successive locations using the Euclidean distance formula, and identifies the longest route segment.
Program completed successfully
Note: This example uses the Euclidean distance formula on sample 2D coordinates. For actual latitude and longitude coordinates on Earth, the Haversine formula is more appropriate.
