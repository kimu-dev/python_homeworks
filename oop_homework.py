import numpy as np

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def put_a_rating(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade <= 10:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        for values in self.grades.values():
            values += values
        return np.mean(values)

    def __str__(self):
        res = f'Имя: {self.name}\nФамиля: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res

    # def compare_scores(self, other_student):
    #     if not isinstance(self, Student):
    #         return
    #     if other_student.avg_grade() < self.avg_grade():
    #         print(f'Успеваемость {self.name} выше чем у {other_student.name}')
    #     else:
    #         print(f'Успеваемость {self.name} ниже чем у {other_student.name}')

    def __lt__(self, other_student):
        if not isinstance(self, Student):
            return
        if self.avg_grade() < other_student.avg_grade():
            print(f'Успеваемость {self.name} выше чем у {other_student.name}')
        else:
            print(f'Успеваемость {self.name} ниже чем у {other_student.name}')        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    lecturer_grades = {}

    def avg_grade(self):
        for values in self.lecturer_grades.values():
            values += values
        return np.mean(values)

    # def compare_scores(self, other_lecturer):
    #     if not isinstance(self, Lecturer):
    #         return
    #     if other_lecturer.avg_grade() < self.avg_grade():
    #         print(f'Профессионализм {self.name} выше чем у {other_lecturer.name}')
    #     else:
    #         print(f'Профессионализм {self.name} ниже чем у {other_lecturer.name}')

    def __lt__(self, other_lecturer):
        if not isinstance(self, Lecturer):
            return
        if other_lecturer.avg_grade() < self.avg_grade():
            print(f'Профессионализм {self.name} выше чем у {other_lecturer.name}')
        else:
            print(f'Профессионализм {self.name} ниже чем у {other_lecturer.name}')           

    def __str__(self):
        for values in self.lecturer_grades.values():
            values += values
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}'
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__ (self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

mentor_1 = Mentor('Max', 'Fadeev')
mentor_2 = Mentor('Tony', 'Stark')

lecturer_1 = Lecturer('Lydia', 'Mukhina')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Andrey', 'Gorin')
lecturer_2.courses_attached += ['Python']

student_1 = Student('Kirill', 'Mukhin', 'male')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']

student_2 = Student('Joe', 'Biden', 'male')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['SQL']

reviewer_1 = Reviewer('Yri', 'Buzaev')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Artem', 'Chernov')
reviewer_2.courses_attached += ['Python']

student_1.put_a_rating(lecturer_1, 'Python', 7)
student_1.put_a_rating(lecturer_2, 'Python', 3)
student_2.put_a_rating(lecturer_1, 'Python', 3)
student_2.put_a_rating(lecturer_2, 'Python', 9)

reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 3)
reviewer_2.rate_hw(student_2, 'Python', 5)

# student_1.compare_scores(student_2)
# lecturer_2.compare_scores(lecturer_1)

print(student_1 < student_2)
print(lecturer_2 > lecturer_1)

print(reviewer_1)
print(reviewer_2)
print(lecturer_1)
print(lecturer_2)
print(student_1)
print(student_2)

def avg_grade_stud(list_students, course_name):
    list_values = []
    for stud in list_students:
        for avg_values in stud.grades.get(course_name):
            list_values.append(avg_values)
    return np.mean(list_values)

students = [student_1, student_2]
avg_grade_stud(students, 'Python')

def avg_grade_lect(list_lecturers, course_name):
    list_values = []
    for lect in list_lecturers:
        for avg_values in lect.lecturer_grades.get(course_name):
            list_values.append(avg_values)
    return np.mean(list_values)

lecturers = [lecturer_1, lecturer_2]
avg_grade_lect(lecturers, 'Python')

