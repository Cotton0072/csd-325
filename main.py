[
    {
        "F_Name": "Ellen",
        "L_Name": "Ripley",
        "Student_ID": 45604,
        "Email": "eripley@gmail.com"
    },
    {
        "F_Name": "Arthur",
        "L_Name": "Dallas",
        "Student_ID": 45605,
        "Email": "adallas@gmail.com"
    },
    {
        "F_Name": "Joan",
        "L_Name": "Lambert",
        "Student_ID": 45714,
        "Email": "jlambert@gmail.com"
    },
    {
        "F_Name": "Thomas",
        "L_Name": "Kane",
        "Student_ID": 68554,
        "Email": "tkane@gmail.com"
    }
]

import json

def print_students(students, message):
    print(message)
    for s in students:
        print(f"{s['L_Name']}, {s['F_Name']} : ID = {s['Student_ID']} , Email = {s['Email']}")
    print("-" * 50)

# Step 1: Load JSON file
with open("student.json", "r", encoding="utf-8") as file:
    students = json.load(file)

# Step 2: Print original list
print_students(students, "Original Student List:")

# Step 3: Append your info
new_student = {
    "F_Name": "Will",
    "L_Name": "Cotton",
    "Student_ID": 99999,
    "Email": "wcotton@example.com"
}
students.append(new_student)

# Step 4: Print updated list
print_students(students, "Updated Student List:")

# Step 5: Save back to JSON
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

print("Notification: student.json file has been updated.")



