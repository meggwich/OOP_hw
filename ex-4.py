# Определение класса Student
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []  # список завершенных курсов
        self.courses_in_progress = []  # список курсов, которые сейчас проходят
        self.grades = {}  # словарь с оценками

    # Переопределение метода __str__ для вывода информации о студенте
    def __str__(self):
        if self.grades:
            average_grade = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        else:
            average_grade = 'Нет оценок'
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    # Переопределение метода __lt__ для сравнения студентов по средней оценке
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return (sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))) < (sum(sum(other.grades.values(), [])) / len(sum(other.grades.values(), [])))

# Определение класса Mentor
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # список курсов, к которым прикреплен наставник

    # Переопределение метода __str__ для вывода информации о наставнике
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

# Определение класса Lecturer, который наследуется от класса Mentor
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures_given = []  # список проведенных лекций
        self.grades = {}  # словарь с оценками

    # Переопределение метода __str__ для вывода информации о лекторе
    def __str__(self):
        if self.grades:
            average_grade = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        else:
            average_grade = 'Нет оценок'
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}'

    # Переопределение метода __lt__ для сравнения лекторов по средней оценке
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return (sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))) < (sum(sum(other.grades.values(), [])) / len(sum(other.grades.values(), [])))

# Определение класса Reviewer, который наследуется от класса Mentor
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Переопределение метода __str__ для вывода информации о проверяющем
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    # Метод для оценки домашних заданий студентов
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Функции для подсчета средних оценок
def avg_grade_students(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return total / count if count else 0

def avg_grade_lecturers(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total / count if count else 0
# Создание двух экземпляров каждого класса
student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('John', 'Doe', 'your_gender')
student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses += ['Введение в программирование']

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']
lecturer1.grades = {'Python': [9.9, 9.8, 10]}

lecturer2 = Lecturer('Jane', 'Doe')
lecturer2.courses_attached += ['Python']
lecturer2.grades = {'Python': [9.7, 9.8, 9.9]}

reviewer1 = Reviewer('First', 'Reviewer')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Second', 'Reviewer')
reviewer2.courses_attached += ['Python']

# Вызов методов
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 10)

reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 9)

# Вывод информации
print(reviewer1)  # Вывод информации о первом проверяющем. Результат: Имя: First\nФамилия: Reviewer
print(reviewer2)  # Вывод информации о втором проверяющем. Результат: Имя: Second\nФамилия: Reviewer

print(lecturer1)  # Вывод информации о первом лекторе. Результат: Имя: Some\nФамилия: Buddy\nСредняя оценка за лекции: 9.9
print(lecturer2)  # Вывод информации о втором лекторе. Результат: Имя: Jane\nФамилия: Doe\nСредняя оценка за лекции: 9.8

print(student1)  # Вывод информации о первом студенте. Результат: Имя: Ruoy\nФамилия: Eman\nСредняя оценка за домашние задания: 9.7\nКурсы в процессе изучения: Python, Git\nЗавершенные курсы: Введение в программирование
print(student2)  # Вывод информации о втором студенте. Результат: Имя: John\nФамилия: Doe\nСредняя оценка за домашние задания: 9.0\nКурсы в процессе изучения: Python, Git\nЗавершенные курсы: Введение в программирование

# Вывод средней оценки за домашние задания по курсу Python для всех студентов
print("Средняя оценка за домашние задания по курсу Python: ", avg_grade_students([student1, student2], 'Python'))  # Результат: Средняя оценка за домашние задания по курсу Python:  9.333333333333334
# Вывод средней оценки за лекции по курсу Python для всех лекторов
print("Средняя оценка за лекции по курсу Python: ", avg_grade_lecturers([lecturer1, lecturer2], 'Python'))  # Результат: Средняя оценка за лекции по курсу Python:  9.85
