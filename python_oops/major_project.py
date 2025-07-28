#  Student Management System (OOP-Based)

from datetime import datetime

# ------------------ Base Class ------------------
class Person:
    def __init__(self, name, age):
        self._name = name  # Protected
        self.__age = age   # Private

    # Encapsulation
    def get_name(self):
        return self._name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age

    def info(self):
        return f"Name: {self._name}, Age: {self.__age}"

# ------------------ Student Class ------------------
class Student(Person):
    total_students = 0

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        Student.total_students += 1
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def info(self):
        return f"👨‍🎓 Student: {super().info()}, Grade: {self.grade}, Courses: {self.courses}"

    @classmethod
    def get_total_students(cls):
        return cls.total_students

    @staticmethod
    def is_passed(marks):
        return marks >= 40

# ------------------ Teacher Class ------------------
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def info(self):
        return f"👩‍🏫 Teacher: {super().info()}, Subject: {self.subject}"

# ------------------ Course Class ------------------
class Course:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration  # weeks

    def course_info(self):
        return f"{self.title} ({self.duration} weeks)"

# ------------------ School Class (Composition) ------------------
class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.created_at = datetime.now()

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)

    def add_teacher(self, teacher):
        if isinstance(teacher, Teacher):
            self.teachers.append(teacher)

    def show_students(self):
        print("\n📘 All Students:")
        for s in self.students:
            print(s.info())

    def show_teachers(self):
        print("\n📗 All Teachers:")
        for t in self.teachers:
            print(t.info())

    def summary(self):
        print(f"\n🏫 Welcome to {self.name}!")
        print(f"📅 Started on: {self.created_at.strftime('%Y-%m-%d')}")
        print(f"👨‍🎓 Total Students: {len(self.students)}")
        print(f"👩‍🏫 Total Teachers: {len(self.teachers)}")

# ------------------ MRO Example ------------------
class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    pass

class D(B, C):
    pass

# ------------------ Main Execution ------------------

if __name__ == "__main__":
    # Create Courses
    python_course = Course("Python", 6)
    math_course = Course("Mathematics", 4)

    # Create School
    my_school = School("Coffee Aur Code")

    # Add Teachers
    t1 = Teacher("Mr. Sharma", 35, "Math")
    t2 = Teacher("Ms. Ritu", 29, "Computer Science")
    my_school.add_teacher(t1)
    my_school.add_teacher(t2)

    # Add Students
    s1 = Student("Mann", 21, "12th")
    s1.enroll(python_course.course_info())
    s1.enroll(math_course.course_info())

    s2 = Student("Heli", 22, "12th")
    s2.enroll(python_course.course_info())

    my_school.add_student(s1)
    my_school.add_student(s2)

    # Show Summary
    my_school.summary()
    my_school.show_teachers()
    my_school.show_students()

    # Class method
    print("\n📊 Total students (via class method):", Student.get_total_students())

    # Static method
    print("✅ Heli passed in exam with 45 marks?", Student.is_passed(45))

    # isinstance and issubclass
    print("\n🔍 isinstance(s1, Person)?", isinstance(s1, Person))         # True
    print("🔍 issubclass(Student, Person)?", issubclass(Student, Person))  # True

    # MRO
    print("\n🧬 MRO of class D:", [cls.__name__ for cls in D.mro()])
    d = D()
    print("Greeting from D:", d.greet())
