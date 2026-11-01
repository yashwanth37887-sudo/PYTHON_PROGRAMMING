
# University Admission Decision Engine

# Course eligibility requirements
courses = {
    "Computer Science": {
        "subjects": ["Mathematics", "Physics", "Computer"],
        "cutoff": 75
    },
    "Engineering": {
        "subjects": ["Mathematics", "Physics", "Chemistry"],
        "cutoff": 70
    },
    "Commerce": {
        "subjects": ["Mathematics", "English", "Economics"],
        "cutoff": 65
    }
}

eligible_candidates = []
all_candidates = []

# Get number of candidates
n = int(input("Enter number of candidates: "))

for i in range(n):
    print(f"\nEnter details of Candidate {i+1}")

    name = input("Enter candidate name: ")

    print("\nAvailable Courses:")
    for course in courses:
        print("-", course)

    course = input("Enter selected course: ")

    if course not in courses:
        print("Invalid course!")
        continue

    # Get marks
    subjects = {
        "Mathematics": float(input("Mathematics marks: ")),
        "Physics": float(input("Physics marks: ")),
        "Chemistry": float(input("Chemistry marks: ")),
        "Computer": float(input("Computer marks: ")),
        "English": float(input("English marks: ")),
        "Economics": float(input("Economics marks: "))
    }

    studied = input(
        "Enter studied subjects separated by commas: "
    ).split(",")

    studied = [s.strip() for s in studied]

    aggregate = sum(subjects.values()) / len(subjects)

    required = courses[course]["subjects"]
    cutoff = courses[course]["cutoff"]

    # Check eligibility
    subject_eligible = all(
        subject in studied for subject in required
    )

    marks_eligible = aggregate >= cutoff

    candidate = {
        "name": name,
        "course": course,
        "aggregate": aggregate,
        "maths": subjects["Mathematics"],
        "english": subjects["English"],
        "eligible": subject_eligible and marks_eligible
    }

    all_candidates.append(candidate)

    if candidate["eligible"]:
        eligible_candidates.append(candidate)
        print("Status: Eligible")
    else:
        print("Status: Not Eligible")


# Sort candidates based on tie-breaking criteria
eligible_candidates.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["maths"],
        -x["english"],
        x["name"].lower()
    )
)

# Display ranked admission list
print("\n======================================")
print("       UNIVERSITY ADMISSION LIST")
print("======================================")

if not eligible_candidates:
    print("No eligible candidates found.")

else:
    print("{:<8} {:<15} {:<20} {:<10}".format(
        "Rank", "Name", "Course", "Aggregate"
    ))

    print("-" * 60)

    for rank, candidate in enumerate(
        eligible_candidates, start=1
    ):
        print("{:<8} {:<15} {:<20} {:.2f}%".format(
            rank,
            candidate["name"],
            candidate["course"],
            candidate["aggregate"]
        ))

print("\nAdmission evaluation completed.")

