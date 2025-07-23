# project gradebook manager

students={
    "Mann":[90,95,100],
    "Heli":[85,90,95],
    "Divyang":[80,85,90],
    "Roshni":[75,80,85]
}

print("Marks of Mann :",students.get("Mann")) 
print("Marks of Heli :",students.get("Heli"))
print("Marks of Divyang :",students.get("Divyang"))
print("Marks of Roshni :",students.get("Roshni"))

# manually calculating average marks
# avg_mann=sum(students.get("Mann"))/len(students.get("Mann"))
# print("Average marks of Mann:", avg_mann)
# avg_heli=sum(students.get("Heli"))/len(students.get("Heli"))
# print("Average marks of Heli:", avg_heli)
# avg_divyang=sum(students.get("Divyang"))/len(students.get("Divyang"))
# print("Average marks of Divyang:", avg_divyang)
# avg_roshni=sum(students.get("Roshni"))/len(students.get("Roshni"))
# print("Average marks of Roshni:", avg_roshni)


# if avg_mann > avg_heli and avg_mann > avg_divyang and avg_mann > avg_roshni:
#     print("Mann has the highest average marks.")
# elif avg_heli > avg_mann and avg_heli > avg_divyang and avg_heli > avg_roshni:
#     print("Heli has the highest average marks.")
# elif avg_divyang > avg_mann and avg_divyang > avg_heli and avg_divyang > avg_roshni:
#     print("Divyang has the highest average marks.")
# elif avg_roshni > avg_mann and avg_roshni > avg_heli and avg_roshni > avg_divyang:
#     print("Roshni has the highest average marks.")
# else:
#     print("There is a tie for the highest average marks.")



# using loop to calculate average marks
for student, marks in students.items():
    avg_marks = sum(marks) / len(marks)
    print(f"Average marks of {student}: {avg_marks}")
# finding the student with highest average marks
highest_avg_student = max(students, key=lambda x: sum(students[x]) / len(students[x]))
print(f"{highest_avg_student} has the highest average marks.")
