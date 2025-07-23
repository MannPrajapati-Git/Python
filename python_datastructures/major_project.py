# Student Report Card System
# This program collects student names and their marks, calculates total, percentage, and assigns grades.

n = int(input("How many students? "))

students = []  # List to store student data
grades_set = set()
top_score = 0
toppers = []

for i in range(n):
    print(f"\n📝 Enter details for Student {i + 1}")
    name = input("Enter student name: ")

    subjects = ["AI", "MERNSTACK", "PYTHON", "WEB DEVELOPMENT", "COMMUNICATION"]
    marks = []

    for sub in subjects:
        score = int(input(f"Marks in {sub}: "))
        marks.append(score)

    total = sum(marks)
    percentage = (total / 500) * 100  # 5 subjects, each out of 100

    # Grade based on percentage
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    grades_set.add(grade)

    if total > top_score:
        top_score = total
        toppers = [name]
    elif total == top_score:
        toppers.append(name)

    students.append((name, marks, total, round(percentage, 2), grade))

# Output Section
print("\n===== 📄 Final Report Card =====\n")

for s in students:
    print("Name:", s[0])
    print("Marks (AI, MERNSTACK, PYTHON, WEB DEV, COMM):", s[1])
    print("Total Marks:", s[2])
    print("Percentage:", s[3], "%")
    print("Grade:", s[4])
    print()

print("----------------------------")
print("🏆 Topper(s):", ', '.join(toppers))
print("🎓 Grades Assigned:", grades_set)
