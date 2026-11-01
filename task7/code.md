1. Problem Statement
The Smart Campus Management Simulation is a menu-driven Python application designed to manage various academic and administrative activities within a college campus.

The system integrates the following modules:
1. Student Records Management: Add and display student details such as student ID and name.
2. Attendance Management: Record and maintain student attendance.
3. Marks Management: Enter subject-wise marks and calculate average marks.
4. Event Registration: Register students for campus events while checking registration capacity.
5. Resource Allocation: Allocate campus resources such as projectors, computers, and laboratory equipment.
6. Summary Reporting: Generate reports containing student details, attendance percentage, average marks, event registrations, and resource allocation details.
The program uses Python concepts such as:
- Conditional statements (if, elif, else)
- Loops (for, while)
- Strings
- Lists and nested lists
- Tuples and tuple unpacking
- Functions
- Dictionaries
The main objective is to simplify campus administration through a single interactive Python program.

2. Algorithm
Step 1: Start the program.

Step 2: Initialize the required data structures:
- Student records
- Attendance records
- Marks records
- Event details
- Resource details
Step 3: Display the main menu with the following options:
1. Add Student
2. View Students
3. Mark Attendance
4. Enter Marks
5. Event Registration
6. Resource Allocation
7. Generate Summary Report
8. Exit
Step 4: Accept the user's menu choice.

Step 5: Perform the selected operation:
- If the choice is 1, accept student ID and name and store the details.
- If the choice is 2, display all student records.
- If the choice is 3, accept student ID, date, and attendance status.
- If the choice is 4, accept student ID, subject, and marks.
- If the choice is 5, display available events and register students.
- If the choice is 6, allocate available campus resources.
- If the choice is 7, calculate and display the summary report.
- If the choice is 8, terminate the program.
Step 6: If an invalid choice is entered, display an error message.

Step 7: Repeat the menu until the user selects Exit.

Step 8: Stop the program.
flowchart:(mermaid):

flowchart TD
    A([START]) --> B[Initialize Student Records]
    B --> C[Initialize Attendance, Marks, Events and Resources]
    C --> D[Display Main Menu]
    D --> E[/Enter Menu Choice/]

    E --> F{Check Choice}

    F -->|1| G[Add Student Details]
    F -->|2| H[Display Student Records]
    F -->|3| I[Mark Student Attendance]
    F -->|4| J[Enter Student Marks]
    F -->|5| K[Register for Campus Events]
    F -->|6| L[Allocate Campus Resources]
    F -->|7| M[Generate Summary Report]
    F -->|8| N([END])
    F -->|Invalid| O[Display Invalid Choice]

    G --> P[Store Updated Records]
    H --> D
    I --> P
    J --> P
    K --> P
    L --> P
    M --> D
    O --> D
    P --> D


 
5. Sample Input
The following inputs demonstrate a sample execution of the program.
Operation	Sample input
Add Student	ID: S101, Name: Rahul
Mark Attendance	S101, 01-11-2026, P
Mark Attendance	S101, 02-11-2026, P
Mark Attendance	S101, 03-11-2026, A
Enter Marks	S101, Python, 90
Enter Marks	S101, Mathematics, 85
Event Registration	S101, E101
Resource Allocation	Projector, 2, Seminar


6. Sample Output
The following is an illustrative output for the sample inputs above.
Python console
Sample execution

SMART CAMPUS MANAGEMENT SYSTEM
================================
 SMART CAMPUS MANAGEMENT SYSTEM
================================

1. Add Student
2. View Students
3. Mark Attendance
4. Enter Marks
5. Event Registration
6. Resource Allocation
7. Student Summary Report
8. Overall Campus Report
9. Exit

Enter Your Choice: 1

Enter Student ID: S101
Enter Student Name: Rahul

Student added successfully!

Enter Your Choice: 3
Enter Student ID: S101
Enter Date: 01-11-2026
Enter Attendance (P/A): P

Attendance recorded successfully!

Enter Your Choice: 3
Enter Student ID: S101
Enter Date: 02-11-2026
Enter Attendance (P/A): P

Attendance recorded successfully!

Enter Your Choice: 3
Enter Student ID: S101
Enter Date: 03-11-2026
Enter Attendance (P/A): A

Attendance recorded successfully!

Enter Your Choice: 4
Enter Student ID: S101
Enter Subject Name: Python
Enter Marks (0-100): 90

Marks entered successfully!

Enter Your Choice: 4
Enter Student ID: S101
Enter Subject Name: Mathematics
Enter Marks (0-100): 85

Marks entered successfully!

Enter Your Choice: 5
Enter Student ID: S101
Enter Event ID: E101

Successfully registered for Tech Fest

Enter Your Choice: 6
Enter Resource Name: Projector
Enter Quantity: 2
Enter Purpose: Seminar

Resource allocated successfully!

Enter Your Choice: 7
Enter Student ID: S101

========== STUDENT REPORT ==========

Student ID: S101
Student Name: Rahul

Total Attendance: 3
Present Days: 2
Attendance Percentage: 66.67 %

--- MARKS DETAILS ---
Python : 90.0
Mathematics : 85.0

Average Marks: 87.5

--- REGISTERED EVENTS ---
Tech Fest

====================================

Enter Your Choice: 8

======= CAMPUS SUMMARY REPORT =======

Total Students: 1
Overall Attendance: 66.67 %
Overall Average Marks: 87.5

--- EVENT REGISTRATION SUMMARY ---
Tech Fest : 1 / 3 registered
Sports Day : 0 / 5 registered
Cultural Fest : 0 / 4 registered

--- RESOURCE ALLOCATION SUMMARY ---
Projector : Allocated = 2 , Available = 3
Computer : Allocated = 0 , Available = 10
Microphone : Allocated = 0 , Available = 8
Lab Equipment : Allocated = 0 , Available = 6

====================================

Enter Your Choice: 9

Thank you for using Smart Campus Management System!




7. Python Concepts Used
This table explains how the required Python concepts are implemented in the project.
Python concept	Application in the project
Conditional statements	Menu selection and validation
while loop	Repeatedly displays the main menu
for loop	Iterates through students, events, and resources
Strings	Student names, subjects, and event names
Lists	Stores students' attendance and marks
Nested lists	Stores attendance as [date, status] and marks as [subject, marks]
Tuples	Stores event and resource information
Tuple unpacking	for sid, details in students.items() and for eid, event_name, capacity in events
Dictionaries	Stores student records and event registrations
Functions	Separates each campus management operation

8. Expected Result
The Smart Campus Management Simulation was successfully developed using Python programming concepts.

The program allows users to manage student records, attendance, marks, event registrations, and campus resources through a menu-driven interface. It also calculates attendance percentages, average marks, and generates individual and overall campus summary reports.

Thus, the project demonstrates the practical application of Python conditional statements, loops, strings, lists, nested lists, tuples, and tuple unpacking in a Smart Campus Management System.
