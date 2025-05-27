class Person:
    def __init__(self, name, password):
        self.name = name
        self.password = password

class Staff(Person):
    staffname =input("Enter ur name : ") 
    print(f"The staff monitoring is {staffname}")
    def monitor_lecturer(self, lecturer, courseunit_name):
        print(f"[STAFF:] Monitoring lecturer: {lecturer.name} on course: {courseunit_name}")

class Lecturer(Person):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.results = {}  # Dictionary to store results keyed by student number

    def enter_results(self, student_number, courseunit_name, marks):
        self.results[(student_number, courseunit_name)] = marks
        print(f"[LECTURER] Results entered for {student_number} in {courseunit_name}: {marks}")

class Student(Person):
    tuition_fee = 1000000

    def __init__(self, name, password, student_number):
        super().__init__(name, password)
        self.student_number = student_number
        self.balance = Student.tuition_fee
        self.my_results = {}

    def pay_tuition(self, amount):
        self.balance -= amount
        print(f"[STUDENT] Paid {amount}. Remaining balance: {self.balance}")

    def check_results(self, lecturer, courseunit_name):
        key = (self.student_number, courseunit_name)
        if key in lecturer.results:
            print(f"[STUDENT] Your marks for {courseunit_name}: {lecturer.results[key]}")
        else:
            print("[STUDENT] Results not found for this course unit.")


lecturer = Lecturer("Dr. Smith", "lect123")
student = Student("Alice", "stud123", "S1234")
staff = Staff("Mr. John", "staff123")

lecturer.enter_results("S1234", "CS101", 85)

student.check_results(lecturer, "CS102")#show if results are there by using the course name

student.pay_tuition(300000)

staff.monitor_lecturer(lecturer, "CS101")
