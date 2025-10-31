class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly_bonus(self)
        # Syntax Error: Missing colon (:) above
        if self.salary < 50000:
            bonus = self.salary * 0.10
        elif self.salary < 100000:
            bonus = self.salary * 0.07
        else:
            bonus = self.salary * 0.05
        return bonus

def average_salary(employees):
    total = 0
    for e in employees:
        total += e.salary
    # Logical Error: should divide by len(employees), not 100
    return total / 100

def top_performer(employees):
    # Logical Error: wrong comparison (should be > not <)
    top = employees[0]
    for e in employees:
        if e.salary < top.salary:
            top = e
    return top

def main():
    emp1 = Employee("Alice", 60000)
    emp2 = Employee("Bob", 40000)
    emp3 = Employee("Charlie", 120000)

    staff = [emp1, emp2, emp3]
    print("Average Salary:", average_salary(staff))
    print("Top Performer:", top_performer(staff).name)
    print("Bonus for Alice:", emp1.yearly_bonus())

main()
