import pandas as pd
import numpy as np

excel_d = pd.read_excel('students and prepods3_without_points.xlsx',
              dtype={'Number': int, 'Group': int, 'StudentName': str, 'StudentSurname': str, 'Subject': str,
                     'LecturerName': str, 'LecturerSurname': str, 'ReviewerName': str, 'ReviewerSurname': str,
                     'LectorGrade': int, 'Grade01': int, 'Grade02': int, 'Grade03': int, 'Grade04': int,
                     'Grade05': int, 'Grade06': int, 'Grade07': int, 'Grade08': int, 'Grade09': int, 'Grade10': int,
                     'Grade11': int, 'Grade12': int})

#excel_d = pd.read_excel("students and prepods3_without_points.xlsx")
data = pd.DataFrame(excel_d, columns=['Number', 'Group', 'StudentName', 'StudentSurname', 'Subject', 'LecturerName',
            'LecturerSurname', 'ReviewerName', 'ReviewerSurname', 'LectorGrade', 'Grade01', 'Grade02', 'Grade03',
            'Grade04', 'Grade05', 'Grade06', 'Grade07', 'Grade08', 'Grade09', 'Grade10', 'Grade11', 'Grade12'])

#print(data['Number'].tolist())

#data.convert_dtypes()

for col_name in ('StudentName', 'StudentSurname'):
    data[col_name] = data[col_name].astype(object)

#for col_name in ('g01', 'g02', 'g03', 'g04', 'g05', 'g06', 'g07', 'g08', 'g09'):
 #   data[col_name] = convert_integer(data[col_name])
#    data[col_name].convert_dtypes(infer_objects=False, convert_string=False, convert_integer=True, convert_boolean=False,
##                            convert_floating=False)
#    pd.to_numeric(data[col_name], downcast='signed')

print(data.dtypes)
print(data['Grade01'])



class Student:

  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}

  def add_finished_courses(self, course_name):
      self.finished_courses.append(course_name)
      self.courses_in_progress = self.courses_in_progress - course_name

  def add_courses_in_progress(self, course_name):
      self.courses_in_progress.append(course_name)

  def rate_lecturer(self, lecturer, course, grade):
    if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and \
            (course in self.courses_in_progress or course in self.finished_courses):
        if course in lecturer.grades:
           lecturer.grades[course] += [grade]
        else:
           lecturer.grades[course] = [grade]
    else:
          return 'Ошибка'

  def __len__(self):
      return len(self.__grades)

  def __average_grade__(self):
    s = 0
    for grade in self.__grades:
        s += grade
    return s/len(grades)
    return self.__grades.mean()

  def __lt__(self, other):
      if not isinstance(other, Student):
          print('Не студент!')
          return
      return self.average_grade < other.average_grade

  def __str__(self):
    return f"Имя: {self.name}"
    return f"Фамилия: {self.surname}"
    return f"Средняя оценка за домашние задания: {self.average_grade}"
    return f"Курсы в процессе изучения: {self.courses_in_progress}"
    return f"Завершенные курсы: {self.finished_courses}"


class Mentor:

  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []

  def add_courses_in_progress(self, course_name):
      self.courses_attached.append(course_name)


class Lecturer(Mentor):

  def __init__(self, name, surname):
    self.grades = {}

  def __len__(self):
      return len(self.__grades)

  def __average_grade__(self):
    s = 0
    for grade in self.__grades:
        s += grade
    return s/len(grades)

  def __str__(self):
    return f"Имя: {self.name}"
    return f"Фамилия: {self.surname}"
    return f"Средняя оценка за лекции: {self.average_grade}"

  def __lt__(self, other):
      if not isinstance(other, Lecturer):
          print('Не лектор!')
          return
      return self.average_grade < other.average_grade


class Reviewer(Mentor):

  def rate_hw(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in student.grades:
        student.grades[course] += [grade]
      else:
        student.grades[course] = [grade]
    else:
        return 'Ошибка'

  def __str__(self):
    return f"Имя: {self.name}"
    return f"Фамилия: {self.surname}"

print(data['LectorGrade'].mean())

#instanceNames = data['StudentName','StudentSurname']
#holder = {name: Student(name=name, surname=surname) for name in instanceNames}



#print(some_reviewer)
#print(some_lecturer)
#print(some_student)
