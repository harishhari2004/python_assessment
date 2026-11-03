n = int(input("Enter number of students: "))

students = {}

passed = 0
failed = 0
highest_avg = -1
top_performer = ""

for i in range(n):

    name = input("Enter student name: ")

    p = int(input("Enter Python mark: "))
    d = int(input("Enter Database mark: "))
    a = int(input("Enter Aptitude mark: "))

    avg = (p + d + a) / 3

    if p >= 40 and d >= 40 and a >= 40 and avg >= 50:

        result = "Passed"
        passed += 1

        if avg >= 80:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "D"

        students[name] = [avg, result, grade]

    else:
        result = "Failed"
        failed += 1

        students[name] = [avg, result]

    if avg > highest_avg:
        highest_avg = avg
        top_performer = name

for name, details in students.items():

    if details[1] == "Passed":
        print(f"{name} - Average: {details[0]:.2f} - Passed - Grade: {details[2]}")
    else:
        print(f"{name} - Average: {details[0]:.2f} - Failed")

print("Passed:", passed)
print("Failed:", failed)
print("Top Performer:", top_performer)
