# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
class definition:
    def __init__(self, first_name, second_name, surname):
        self.first_name = first_name
        self.second_name = second_name
        self.surname = surname

class schoolboy(definition):
    def __init__(self, first_name, second_name, surname, father_name, mother_name, class_name):
        definition.__init__(self, first_name, second_name, surname)
        self.father_name = father_name
        self.mother_name = mother_name
        self.class_name = class_name
        self.lessons = set()

    def participate(self, lesson_name):
        self.lessons.add(lesson_name)

    def display_information(self):
        print(self.surname, self.first_name[0] + '.', self.second_name[0] + '.', self.class_name, self.lessons)

    def number_classes(self):  #--------
        list_classes = []
        list_classes.append(self.class_name)
        return list_classes


    def name_by_class(self, class_name):
        if class_name == self.class_name:
            print(self.surname, self.first_name[0] + '.', self.second_name[0] + '.')

    def parent_name(self, surname_schoolboy, first_name, second_name):
        if surname_schoolboy == self.surname and first_name == self.first_name[0] and second_name == self.second_name[0]:
            print('Father name: ', self.father_name)
            print('Mother name: ', self.mother_name)

class teacher(definition):
    def __init__(self, first_name, second_name, surname, lesson_name):
        definition.__init__(self, first_name, second_name, surname)
        self.lesson_name = lesson_name
        self.take_class = set()

    def taking(self, class_name):
        self.take_class.add(class_name)

    def display_information(self):
        print(self.surname, self.first_name[0] + '.', self.second_name[0] + '.', self.take_class, self.lesson_name)



class Lesson:
    def __init__(self, lesson_name):
        self.lesson_name = lesson_name
        self.hours = 2




lessons = [Lesson('Math'), Lesson('Bilogie')]
teachers = [teacher('Alexandr', 'Ivanovich', 'Petrov', 'Math'), teacher('Vladmir', 'Ivanovich', 'Sidorov', 'Math')]

for teacher in teachers:
    teacher.taking('5A')
    #teacher.display_information()




persons = [schoolboy('Dmitriy', 'Alexandrovich', 'Ivanov', 'Alexandr Ivanov', 'Elena Ivanova', '5A'),
           schoolboy('Ivan', 'Alexandrovich', 'Ivanov', 'Alexandr Ivanov', 'Elena Ivanova', '6A'),
           schoolboy('Vasiliy', 'Alexandrovich', 'Sidorov', 'Alexandr Sidorov', 'Elena Sidorova', '7B'),
           schoolboy('Constantin', 'Alexandrovich', 'Ivanov', 'Alexandr Ivanov', 'Elena Ivanova', '8C'),
           schoolboy('Mariya', 'Alexandrovna', 'Ivanova', 'Alexandr Ivanov', 'Elena Ivanova', '5B'),
           schoolboy('Mariya', 'Alexandrovna', 'Petrova', 'Alexandr Petrov', 'Elena Petrova', '5B'),
           schoolboy('Olga', 'Alexandrovna', 'Petrova', 'Ivan Petrov', 'Svetlana Petrova', '6C')]

a = '5B'
b, d, e = 'Petrova', 'O', 'A'

for person in persons:
    #person.number_classes()
    #print(person.number_classes())
    #person.name_by_class(a)
    #person.parent_name(b, d, e)
    person.participate('Biologie')
    person.display_information()
