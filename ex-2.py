# Определение класса Mentor
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Определение класса Student
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

# Определение класса Lecturer, который наследуется от класса Mentor
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures_given = []
        self.grades = {}  # словарь с оценками

# Определение класса Reviewer, который наследуется от класса Mentor
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def review_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Создание экземпляров классов
student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']

student2 = Student('John', 'Doe', 'your_gender')
student2.courses_in_progress += ['Python']

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Jane', 'Doe')
lecturer2.courses_attached += ['Python']

reviewer1 = Reviewer('First', 'Reviewer')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Second', 'Reviewer')
reviewer2.courses_attached += ['Python']

# Вызов методов
reviewer1.review_hw(student1, 'Python', 10)
reviewer1.review_hw(student1, 'Python', 9)
reviewer1.review_hw(student1, 'Python', 10)

reviewer2.review_hw(student2, 'Python', 9)
reviewer2.review_hw(student2, 'Python', 9)
reviewer2.review_hw(student2, 'Python', 9)

student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Python', 10)

student2.rate_lecture(lecturer2, 'Python', 9)
student2.rate_lecture(lecturer2, 'Python', 9)
student2.rate_lecture(lecturer2, 'Python', 9)


# Вывод информации
print("Оценки студента 1:", student1.grades)  # Выводит оценки студента 1
print("Оценки студента 2:", student2.grades)  # Выводит оценки студента 2
print("Оценки лектора 1:", lecturer1.grades)  # Выводит оценки лектора 1
print("Оценки лектора 2:", lecturer2.grades)  # Выводит оценки лектора 2