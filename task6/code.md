
1. Problem Statement
Write a Python program to find the longest route segment between successive coordinate points using the Euclidean distance formula.

The program should:
- Define coordinates as tuples.
- Select successive pairs of coordinates.
- Calculate the Euclidean distance between each pair.
- Store all calculated distances in a list.
- Find the maximum distance.
- Identify the longest route segment.
- Display all distances and the longest route segment.
2. Algorithm
1. Start the program.
2. Define a list of coordinates as tuples.
3. Initialize an empty list to store distances.
4. Select two successive coordinate points.
5. Calculate the Euclidean distance using the formula:
   
   \[
   d = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
   \]
6. Store the calculated distance in the distance list.
7. Repeat steps 4–6 for all successive coordinate pairs.
8. Find the maximum distance from the list.
9. Identify the corresponding longest route segment.
10. Display all calculated distances.
11. Display the longest route segment and its distance.
12. Stop the program.
13. flowchart:(mermaid):
14. flowchart TD
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
 
  
5. Sample Input
Coordinates = [(0, 0), (3, 4), (6, 8), (12, 8), (12, 16)]


6. Sample Output
Distances between successive coordinates:
(0, 0) to (3, 4) = 5.00
(3, 4) to (6, 8) = 5.00
(6, 8) to (12, 8) = 6.00
(12, 8) to (12, 16) = 8.00

Longest Route Segment:
From: (12, 8)
To: (12, 16)
Maximum Distance: 8.0


7. Result
Thus, the Python program successfully calculates the Euclidean distances between successive coordinate points, stores the distances in a list, and identifies the longest route segment.
Program completed successfully
