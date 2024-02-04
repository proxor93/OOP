class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade] 
        else:
            return 'Ошибка'
    
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_rating() < other.average_rating()
        
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_rating() == other.average_rating()
    
    def average_rating(self):
        for course, grades in self.grades.items():
            result = sum(grades) / len(grades)
        return result

    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rating():.1f}\n"\
               f"Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        for course, grades in self.grades.items():
            res = sum(grades) / len(grades)
        return res
    
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_rating() < other.average_rating()
        
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_rating() == other.average_rating()
    
    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оченка за лекции: {self.average_rating():.1f}"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

      
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}"



def average_students(list_students, course):
    everyone = 0 # общая оценка студентов
    general = 0 # общее кол-во студентов
    for student in list_students:
        if course in student.courses_in_progress:
            everyone += student.average_rating()
            general += 1
        else:
            return 
    average_for_all = everyone / general
    return f"Средняя оценка студентов на курсе {course}: {average_for_all:.1f}"


def average_lecturer(list_lecturer, course):
    everyone = 0 # общая оценка лекторов
    general = 0 # общее кол-во лекторов
    for lecturer in list_lecturer:
        if course in lecturer.courses_attached:
            everyone += lecturer.average_rating()
            general += 1
        else:
            return 
    average_for_all = everyone / general
    return f"Средняя оценка лекторов на курсе {course}: {average_for_all:.1f}"



group_students_1 = Student("Aleks", "Popov", "man")
group_students_1.finished_courses += ["Git"]
group_students_1.courses_in_progress += ["Python"]
group_students_1.courses_in_progress += ["JS"]

group_students_2 = Student("Olga", "Popova", "woman")
group_students_2.finished_courses += ["Git", "PHP"]
group_students_2.courses_in_progress += ["Python"]

teacher_1 = Lecturer("Stepan", "Ivanov")
teacher_1.courses_attached += ["Python"]

teacher_2 = Lecturer("Petr", "Markov")
teacher_2.courses_attached += ["Python"]

inspector_1 = Reviewer("Anna", "Kartehsova")
inspector_1.courses_attached += ["Python"]

inspector_2 = Reviewer("Kate", "Putina")
inspector_2.courses_attached += ["Python"]

study_list = [group_students_1, group_students_2]
lectur_list = [teacher_1, teacher_2]

inspector_1.rate_hw(group_students_1, "Python", 7)
inspector_1.rate_hw(group_students_1, "Python", 6)
inspector_1.rate_hw(group_students_1, "Python", 10)

inspector_2.rate_hw(group_students_2, "Python", 5)
inspector_2.rate_hw(group_students_2, "Python", 7)
inspector_2.rate_hw(group_students_2, "Python", 10)

group_students_1.rate_hw(teacher_1, "Python", 9)
group_students_1.rate_hw(teacher_1, "Python", 5)
group_students_1.rate_hw(teacher_1, "Python", 6)

group_students_2.rate_hw(teacher_2, "Python", 7)
group_students_2.rate_hw(teacher_2, "Python", 9)
group_students_2.rate_hw(teacher_2, "Python", 8)

print(group_students_1, "\n")
print(group_students_2, "\n")
print(teacher_1, "\n")
print(teacher_2, "\n")
print(inspector_1, "\n")
print(inspector_2, "\n")
print(group_students_1 < group_students_2, "\n")
print(group_students_1 == group_students_2, "\n")
print(teacher_1 < teacher_2, "\n")
print(teacher_1 == teacher_2, "\n")
print(average_lecturer(lectur_list, "Python"))
print(average_students(study_list, "Python"))







