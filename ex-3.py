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

# Функция для сравнения средних оценок двух объектов (студентов или лекторов)
def compare_avg_grades(obj1, obj2):
    if isinstance(obj1, (Lecturer, Student)) and isinstance(obj2, (Lecturer, Student)):
        avg_grade1 = sum(sum(obj1.grades.values(), [])) / len(sum(obj1.grades.values(), []))
        avg_grade2 = sum(sum(obj2.grades.values(), [])) / len(sum(obj2.grades.values(), []))
        if avg_grade1 > avg_grade2:
            return f'{obj1.name} {obj1.surname} имеет более высокую среднюю оценку, чем {obj2.name} {obj2.surname}'
        elif avg_grade1 < avg_grade2:
            return f'{obj2.name} {obj2.surname} имеет более высокую среднюю оценку, чем {obj1.name} {obj1.surname}'
        else:
            return f'{obj1.name} {obj1.surname} и {obj2.name} {obj2.surname} имеют одинаковую среднюю оценку'
    else:
        return 'Ошибка'

# Создание экземпляров классов и выполнение операций...
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.grades = {'Python': [9.9, 9.8, 10]}

print(cool_reviewer)
print(some_lecturer)
print(best_student)
