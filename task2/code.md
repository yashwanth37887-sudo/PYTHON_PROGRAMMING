1. Problem Statement
The University Admission Decision Engine is a Python-based application designed to evaluate student applications and generate a ranked list of eligible candidates for university admission.

The system evaluates candidates based on the following criteria:
1. Subject Eligibility: Checks whether the candidate has studied the required subjects for the selected course.
2. Aggregate Marks: Calculates the average marks obtained by the candidate.
3. Course-Specific Threshold: Checks whether the candidate meets the minimum aggregate percentage required for the course.
4. Tie-Breaking Criteria: If two or more candidates have the same aggregate marks, Mathematics marks are considered. If still tied, English marks are considered.
5. Ranking: Eligible candidates are ranked in descending order based on their marks.
The system displays the final admission list with candidate names, aggregate marks, eligibility status, and rank.
2. Algorithm
   
Step 1: Start the program.
Step 2: Define the courses and their eligibility requirements.
Step 3: Define the minimum aggregate marks required for each course.
Step 4: Get the number of candidates.
Step 5: Enter each candidate's name, selected course, subject marks, and studied subjects.
Step 6: Calculate the aggregate percentage.
Step 7: Check whether the candidate satisfies the required subject eligibility.
Step 8: Check whether the candidate meets the course-specific minimum aggregate percentage.
Step 9: If both conditions are satisfied, add the candidate to the eligible list.
Step 10: Sort eligible candidates using:
- Highest aggregate marks.
- Highest Mathematics marks.
- Highest English marks.
- Candidate name in alphabetical order.
Step 11: Assign ranks to eligible candidates.
Step 12: Display the ranked admission list.
Step 13: Stop the program.
flowchart:(mermaid):

flowchart TD
    A([Start]) --> B[Define Courses and Eligibility Criteria]
    B --> C[Enter Number of Candidates]
    C --> D[Enter Candidate Details]
    D --> E[Calculate Aggregate Percentage]
    E --> F{Required Subjects Studied?}
    F -->|No| G[Mark as Not Eligible]
    F -->|Yes| H{Meets Course Threshold?}
    H -->|No| G
    H -->|Yes| I[Add Candidate to Eligible List]
    G --> J{More Candidates?}
    I --> J
    J -->|Yes| D
    J -->|No| K[Sort Eligible Candidates]
    K --> L[Apply Tie-Breaking Criteria]
    L --> M[Assign Ranks]
    M --> N[Display Ranked Admission List]
    N --> O([Stop])

5. Sample Input
For the above program, consider the following three candidates.

EXAMPLE CANDIDATE DATA
Candidate	Course	Aggregate	Maths	English
Arun	Computer Science	85.00	90	80
Banu	Engineering	80.00	85	75
Charan	Commerce	70.00	70	80

All three candidates have studied the required subjects for their selected courses.
6. Sample Output
Enter number of candidates: 3

Enter details of Candidate 1
Enter candidate name: Arun
Enter selected course: Computer Science
Mathematics marks: 90
Physics marks: 85
Chemistry marks: 80
Computer marks: 90
English marks: 80
Economics marks: 85
Enter studied subjects separated by commas:
Mathematics,Physics,Computer,English,Economics
Status: Eligible

Enter details of Candidate 2
Enter candidate name: Banu
Enter selected course: Engineering
Mathematics marks: 85
Physics marks: 80
Chemistry marks: 85
Computer marks: 75
English marks: 75
Economics marks: 80
Enter studied subjects separated by commas:
Mathematics,Physics,Chemistry,English,Economics
Status: Eligible

Enter details of Candidate 3
Enter candidate name: Charan
Enter selected course: Commerce
Mathematics marks: 70
Physics marks: 65
Chemistry marks: 60
Computer marks: 65
English marks: 80
Economics marks: 80
Enter studied subjects separated by commas:
Mathematics,English,Economics
Status: Eligible

======================================
       UNIVERSITY ADMISSION LIST
======================================

Rank    Name            Course              Aggregate
------------------------------------------------------------
1       Arun            Computer Science    85.00%
2       Banu            Engineering         80.00%
3       Charan          Commerce            68.33%

Admission evaluation completed.


7. Expected Result
The University Admission Decision Engine successfully:
- Accepts multiple student applications.
- Checks subject eligibility.
- Calculates aggregate marks.
- Applies course-specific cutoffs.
- Resolves ties using predefined criteria.
- Generates a ranked list of eligible candidates.
- Displays the final admission results.
8. Conclusion
The University Admission Decision Engine automates the university admission process using Python. It reduces manual effort, improves consistency, and provides a systematic method for evaluating and ranking applicants based on academic performance and course eligibility requirements.
