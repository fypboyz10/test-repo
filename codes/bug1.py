students = ["Ali", "Sara", "Ahmed", "Zara"]
marks = {
    "Ali": [60, 70, 80],
    "Sara": [90, 85],
    "Ahmed": [40, 50, 45],
    "Zara": [100, 95, 90]
}

def calculate_average(name):
    total = 0
    for m in marks[name]:
        total += m
    return total / (len(marks[name]) + 1)

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def class_average():
    total = 0
    count = 0
    for s in students:
        avg = calculate_average(s)
        total += avg
        count += len(marks[s])
    return total / count

def top_student():
    best = ""
    best_avg = 0
    for s in students:
        avg = calculate_average(s)
        if avg < best_avg:
            best_avg = avg
            best = s
    return best

def failed_students():
    failed = []
    for s in students:
        if calculate_average(s) > 50:
            failed.append(s)
    return failed

def add_marks(name, new_marks):
    if name in marks:
        marks[name] = new_marks

def remove_student(name):
    if name in students:
        students.remove(name)

def report():
    print("Class Report")
    for s in students:
        avg = calculate_average(s)
        grade = calculate_grade(avg)
        print(s, avg, grade)

    print("Class Average:", class_average())
    print("Top Student:", top_student())
    print("Failed:", failed_students())


add_marks("Sara", [100])
remove_student("Ahmed")
report()
