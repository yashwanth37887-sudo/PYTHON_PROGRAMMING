
# Integrated Student Record Consistency Checker

# Student records stored as tuples inside a list
# Format: (Student ID, Name, Marks, Attendance, Course ID)

students = [
    ("S101", "Anu", 85, 92, "CSE101"),
    ("S102", "Ravi", None, 88, "CSE101"),
    ("S103", "", 76, 80, "ECE101"),
    ("S101", "Meera", 91, 95, "CSE101"),
    ("S104", "Kiran", 105, 101, "BIO999"),
    ("S105", "Sara", 70, -5, "ECE101"),
    ("S106", "Dev", 78, 85, "CSE101")
]

# Course records stored as tuples inside a list
# Format: (Course ID, Course Name)

courses = [
    ("CSE101", "Computer Science"),
    ("ECE101", "Electronics")
]

# Lists for storing errors and valid records
errors = []
valid_records = []

# Store existing student IDs
student_ids = []

# Store course IDs
course_ids = []

# Step 1: Validate course records
for course in courses:
    if len(course) != 2:
        errors.append(f"Invalid course record: {course}")
        continue

    cid, cname = course

    if not cid or not str(cid).strip():
        errors.append("Missing Course ID")
    elif str(cid).strip().upper() in course_ids:
        errors.append(f"Duplicate Course ID: {cid}")
    else:
        course_ids.append(str(cid).strip().upper())

    if not cname or not str(cname).strip():
        errors.append(f"Missing Course Name for {cid}")

# Step 2: Validate student records
for index, student in enumerate(students, start=1):

    if len(student) != 5:
        errors.append(
            f"Record {index}: Invalid student record format"
        )
        continue

    sid, name, marks, attendance, course_id = student

    record_errors = []

    # Check Student ID
    if not sid or not str(sid).strip():
        record_errors.append("Missing Student ID")
    else:
        sid = str(sid).strip().upper()

        if sid in student_ids:
            record_errors.append(
                f"Duplicate Student ID: {sid}"
            )
        else:
            student_ids.append(sid)

    # Check Student Name
    if not isinstance(name, str) or not name.strip():
        record_errors.append("Missing Student Name")

    # Check Marks
    if marks is None:
        record_errors.append("Missing Marks")
    elif (isinstance(marks, bool)
          or not isinstance(marks, (int, float))):
        record_errors.append("Invalid Marks Format")
    elif marks < 0 or marks > 100:
        record_errors.append("Marks must be between 0 and 100")

    # Check Attendance
    if attendance is None:
        record_errors.append("Missing Attendance")
    elif (isinstance(attendance, bool)
          or not isinstance(attendance, (int, float))):
        record_errors.append("Invalid Attendance Format")
    elif attendance < 0 or attendance > 100:
        record_errors.append(
            "Attendance must be between 0 and 100"
        )

    # Check Course ID
    if not course_id or not str(course_id).strip():
        record_errors.append("Missing Course ID")
    elif str(course_id).strip().upper() not in course_ids:
        record_errors.append(
            f"Invalid Course ID: {course_id}"
        )

    # Store errors or valid records
    if record_errors:
        for error in record_errors:
            errors.append(f"Record {index}: {error}")
    else:
        valid_records.append(student)

# Step 3: Display valid records
print("\n===== STUDENT RECORD CONSISTENCY REPORT =====")

print("\nVALID STUDENT RECORDS:")

for record in valid_records:
    print(record)

# Step 4: Display detected errors
print("\nDETECTED INCONSISTENCIES:")

if errors:
    for error in errors:
        print("-", error)
else:
    print("No errors found.")

# Step 5: Display summary
print("\n===== SUMMARY =====")
print("Total Student Records:", len(students))
print("Valid Student Records:", len(valid_records))
print("Total Errors Detected:", len(errors))

print("\nValidation Completed Successfully!")

