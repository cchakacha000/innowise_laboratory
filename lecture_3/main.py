students = []


def is_name_exist(name):
    for student in students:
        if student["name"] == name:
            return True
    return False


while True:
    print(
        "--- Student Grade Analyzer ---\n 1. Add a new student \n 2. Add grades for a student \n 3. Generate a full report \n 4. Find the top student \n 5. Exit program "
    )

    try:
        choice = int(input("Enter your choice: "))
        if choice not in [1, 2, 3, 4, 5]:
            raise ValueError
    except ValueError:
        print("You can only enter values: 1, 2, 3, 4, 5. Try again.")
        continue

    match choice:
        case 1:
            name = input("Enter student name: ")
            if not is_name_exist(name):
                new_student = {"name": name, "grades": []}
                students.append(new_student)
            else:
                print(
                    f"A student with name {name} alredy exists. Try add student again"
                )

        case 2:
            name = input("Enter student name: ")
            if not is_name_exist(name):
                print(f"A student with name {name} not exists. Try again")
            else:
                for student in students:
                    if student["name"] == name:
                        while True:
                            grade = input("Enter a grade (or 'done' to finish): ")
                            if grade == "done":
                                break
                            try:
                                grade_int = int(grade)
                                if grade_int < 0 or grade_int > 100:
                                    raise ValueError
                                student["grades"].append(int(grade))
                            except:
                                print(
                                    "Value of grade must be integer and between 0 and 100"
                                )
                                continue

                print(students)
        case 3:
            print("---- Students Report ----")
            averages = []
            max_average = 0
            min_average = 101
            if students == []:
                print("List of sudents is empty")
            else:
                for student in students:
                    grades = student["grades"]
                    name = student["name"]
                    average = 0
                    try:
                        average = round(sum(grades) / len(grades), 1)
                    except:
                        print(f"{name}'s average grade is N/A")
                        continue
                    print(f"{name}'s average grade is {average}")
                    if average < min_average:
                        min_average = average
                    elif average > max_average:
                        max_average = average
                    averages.append(average)

                if averages == []:
                    print("Students don't have grades")
                else:
                    overall_average = sum(averages) / len(averages)
                    print("---------------------------------")
                    print(f"Min average: {min_average}")
                    print(f"Max average: {max_average}")
                    print(f"Overall average: {overall_average}")
        case 4:

            if students == []:
                print("List of sudents is empty")
            else:
                students_with_grades = [s for s in students if s["grades"]]

                if students_with_grades:
                    best_student = max(
                        students_with_grades,
                        key=lambda s: sum(s["grades"]) / len(s["grades"]),
                    )
                    average = round(
                        sum(best_student["grades"]) / len(best_student["grades"]), 2
                    )
                    print(
                        f"The student with the higest average is {best_student['name']} with a average grade of {average}"
                    )
                else:
                    print("No students with grades")

        case 5:
            break
