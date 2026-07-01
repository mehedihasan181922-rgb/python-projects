import csv

students = []

while True:
    name = input("Enter Student Name: ")

    math = int(input("Enter Math Marks: "))
    physics = int(input("Enter Physics Marks: "))
    chemistry = int(input("Enter Chemistry Marks: "))
    english = int(input("Enter English Marks: "))

    totalmarks = math + physics + chemistry + english
    average = totalmarks / 4

    if average >= 80:
        grade = "A+"
    elif average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "A-"
    elif average >= 50:
        grade = "B"
    elif average >= 40:
        grade = "C"
    elif average >= 33:
        grade = "D"
    else:
        grade = "F"

    if (
        average >= 33
        and math >= 33
        and physics >= 33
        and chemistry >= 33
        and english >= 33
    ):
        result = "Pass"
    else:
        result = "Fail"

    print("\n-------- Student Result --------")
    print("Name:", name)
    print("Total Marks:", totalmarks)
    print("Average:", average)
    print("Grade:", grade)
    print("Result:", result)

    student = {
        "Name": name,
        "Math": math,
        "Physics": physics,
        "Chemistry": chemistry,
        "English": english,
        "Total marks": totalmarks,
        "Average": average,
        "Grade": grade,
        "Result": result,
    }

    students.append(student)

    choice = input("\nAdd another student? (yes/no): ")

    if choice.lower() != "yes":
        break

print("\nThank You!")

print("\n----- All Students -----")

for student in students:
    print("------------------------")
    print("Name:", student["Name"])
    print("Total Marks:", student["Total marks"])
    print("Average:", student["Average"])
    print("Grade:", student["Grade"])
    print("Result:", student["Result"])

top_student = students[0]

for student in students:
    if student["Average"] > top_student["Average"]:
        top_student = student

print("\n----- Top Student -----")
print("Name:", top_student["Name"])
print("Average:", top_student["Average"])
print("Grade:", top_student["Grade"])
print("Result:", top_student["Result"])
students.sort(key=lambda student: student["Average"], reverse=True)

print("\n----- Student Ranking -----")
rank = 1
for student in students:
    print(rank, "=", student["Name"], "=", student["Average"])
    rank += 1
search_name = input("\nEnter student name to search: ")
found = False
for student in students:
    if student["Name"].lower() == search_name.lower():
        print("\n----- Student Found -----")
        print("Name:", student["Name"])
        print("Math:", student["Math"])
        print("Physics:", student["Physics"])
        print("Chemistry:", student["Chemistry"])
        print("English:", student["English"])
        print("Total Marks:", student["Total marks"])
        print("Average:", student["Average"])
        print("Grade:", student["Grade"])
        print("Result:", student["Result"])


        found = True
        break

if not found:
    print("Student not found.")

pass_count = 0
fail_count = 0

for student in students:
    if student["Result"] == "Pass":
        pass_count += 1
    else:
        fail_count += 1

print("\n----- Summary -----")
print("Total Students:", len(students))
print("Pass Students:", pass_count)
print("Fail Students:", fail_count)
choice = input("\nDo you want to update a student? (yes/no): ")

if choice.lower() == "yes":
   update_name = input("Enter student name to update: ")
   found = False
   for student in students:
       if student["Name"].lower() == update_name.lower():
        print("\n----- Enter New Marks -----")

        student["Math"] = int(input("Enter Math: "))
        student["Physics"] = int(input("Enter Physics: "))
        student["Chemistry"] = int(input("Enter Chemistry: "))
        student["English"] = int(input("Enter English: "))

        student["Total marks"] = (
                student["Math"] +
                student["Physics"] +
                student["Chemistry"] +
                student["English"]
        )

        student["Average"] = student["Total marks"] / 4

        if student["Average"] >= 80:
            student["Grade"] = "A+"
        elif student["Average"] >= 70:
            student["Grade"] = "A"
        elif student["Average"] >= 60:
            student["Grade"] = "A-"
        elif student["Average"] >= 50:
            student["Grade"] = "B"
        elif student["Average"] >= 40:
            student["Grade"] = "C"
        elif student["Average"] >= 33:
            student["Grade"] = "D"
        else:
            student["Grade"] = "F"

        if (
                student["Average"] >= 33
                and student["Math"] >= 33
                and student["Physics"] >= 33
                and student["Chemistry"] >= 33
                and student["English"] >= 33
        ):
            student["Result"] = "Pass"
        else:
            student["Result"] = "Fail"

        found = True

        print("\nStudent Updated Successfully!")
        break
   if not found:
       print("Student not found.")
   else:
        print("\n----- Updated Student -----")
        print("Name:", student["Name"])
        print("Math:", student["Math"])
        print("Physics:", student["Physics"])
        print("Chemistry:", student["Chemistry"])
        print("English:", student["English"])
        print("Total Marks:", student["Total marks"])
        print("Average:", student["Average"])
        print("Grade:", student["Grade"])
        print("Result:", student["Result"])

choice = input("\nDo you want to delete a student? (yes/no): ")

if choice.lower() == "yes":

    delete_name = input("Enter student name to delete: ")

    found = False

    for student in students:
        if student["Name"].lower() == delete_name.lower():
            students.remove(student)
            found = True
            print("Student Deleted Successfully!")
            break

    if not found:
        print("Student not found!")

else:
    print("No student deleted.")
with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Name",
        "Math",
        "Physics",
        "Chemistry",
        "English",
        "Total Marks",
        "Average",
        "Grade",
        "Result"
    ])

    for student in students:
        writer.writerow([
            student["Name"],
            student["Math"],
            student["Physics"],
            student["Chemistry"],
            student["English"],
            student["Total marks"],
            student["Average"],
            student["Grade"],
            student["Result"]
        ])

print("\nStudent data saved successfully in students.csv")
print("\n========== FINAL STUDENT LIST ==========")

for student in students:
    print("--------------------------------")
    print("Name:", student["Name"])
    print("Math:", student["Math"])
    print("Physics:", student["Physics"])
    print("Chemistry:", student["Chemistry"])
    print("English:", student["English"])
    print("Total Marks:", student["Total marks"])
    print("Average:", student["Average"])
    print("Grade:", student["Grade"])
    print("Result:", student["Result"])
pass_count = 0
fail_count = 0

for student in students:
    if student["Result"] == "Pass":
        pass_count += 1
    else:
        fail_count += 1

print("\n========== FINAL SUMMARY ==========")
print("Total Students:", len(students))
print("Pass Students:", pass_count)
print("Fail Students:", fail_count)

print("\n🎉 Student Management System Finished Successfully!")
