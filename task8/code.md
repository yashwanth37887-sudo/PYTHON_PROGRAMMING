ntegrated Student Record Consistency Checker Using Python
1. Problem Statement
The Integrated Student Record Consistency Checker is a Python-based application used to validate and maintain the accuracy of student academic records.

The system stores student details and course information using lists and tuples. It checks student identifiers, names, marks, attendance percentages, and course records to identify errors and inconsistencies.

The program detects:
1. Duplicate student IDs.
2. Missing student names and identifiers.
3. Missing marks and attendance values.
4. Invalid marks (below 0 or above 100).
5. Invalid attendance percentages.
6. Duplicate course IDs.
7. Invalid or unavailable course IDs.
The main objective is to improve the accuracy, reliability, and consistency of student academic records.
2. Algorithm
Step 1: Start the program.

Step 2: Create a list of student records using tuples containing:
- Student ID
- Student Name
- Marks
- Attendance
- Course ID
Step 3: Create a list of course records using tuples containing course ID and course name.

Step 4: Initialize an empty list to store errors.

Step 5: Read each student record and validate the following:
- Check whether the student ID is missing.
- Check whether the student name is missing.
- Check whether marks are available and within 0–100.
- Check whether attendance is within 0–100.
- Check whether the course ID exists.
Step 6: Check for duplicate student IDs and course IDs.

Step 7: Store all detected errors in the error list.

Step 8: Display valid records and detected inconsistencies.

Step 9: Display the total number of errors.

Step 10: Stop the program.
 flowchart:(mermaid):
 
flowchart TD
    A([START]) --> B[Initialize Student Records]
    B --> C[Initialize Course Records]
    C --> D[Create Empty Error List]
    D --> E[Read Student Record]
    E --> F{More Records?}
    F -->|Yes| G[Check Student ID]
    G --> H{ID Missing or Duplicate?}
    H -->|Yes| I[Add Error]
    H -->|No| J[Check Student Name]
    I --> J
    J --> K{Name Missing?}
    K -->|Yes| L[Add Error]
    K -->|No| M[Validate Marks]
    L --> M
    M --> N{Marks Valid?}
    N -->|No| O[Add Error]
    N -->|Yes| P[Validate Attendance]
    O --> P
    P --> Q{Attendance Valid?}
    Q -->|No| R[Add Error]
    Q -->|Yes| S[Validate Course ID]
    R --> S
    S --> T{Course Exists?}
    T -->|No| U[Add Error]
    T -->|Yes| V[Continue Validation]
    U --> V
    V --> E
    F -->|No| W[Check Course Records]
    W --> X[Display Errors and Valid Records]
    X --> Y[Display Error Count]
    Y --> Z([STOP])

5. Sample Input
The following student and course records are used as input.

Student Records
Student ID	Name	Marks	Attendance	Course ID
S101	Anu	85	92	CSE101
S102	Ravi	None	88	CSE101
S103	Empty	76	80	ECE101
S101	Meera	91	95	CSE101
S104	Kiran	105	101	BIO999
S105	Sara	70	-5	ECE101
S106	Dev	78	85	CSE101

Course Records
courses = [    ("CSE101", "Computer Science"),    ("ECE101", "Electronics")]



6. Sample Output
===== STUDENT RECORD CONSISTENCY REPORT =====

VALID STUDENT RECORDS:
('S101', 'Anu', 85, 92, 'CSE101')
('S106', 'Dev', 78, 85, 'CSE101')

DETECTED INCONSISTENCIES:
- Record 2: Missing Marks
- Record 3: Missing Student Name
- Record 4: Duplicate Student ID: S101
- Record 5: Marks must be between 0 and 100
- Record 5: Attendance must be between 0 and 100
- Record 5: Invalid Course ID: BIO999
- Record 6: Attendance must be between 0 and 100

===== SUMMARY =====
Total Student Records: 7
Valid Student Records: 2
Total Errors Detected: 7

Validation Completed Successfully!


7. Result
Thus, the Integrated Student Record Consistency Checker was successfully implemented using Python.

The program uses lists and tuples to store student and course records. It validates student identifiers, names, marks, attendance, and course information. It also identifies duplicate entries, missing values, and inconsistent academic records.

The system successfully displays valid student records, detected errors, and the total number of inconsistencies.
Program completed
