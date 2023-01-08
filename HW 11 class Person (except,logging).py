
# 1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# 2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
# 3) Створіть клас Група, який містить масив із 10
# об'єктів класу Студент. Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.  ' \
#   'Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.

# 2. Модифікуйте Друге домашнє завдання так, щоб при спробі додавання до групи більше 10-ти студентів,
# # викликалася виняткова ситуація (тип виняткової ситуації треба самостійно реалізувати).

import logging
logging.basicConfig( filename="logs/my_log.log",level=logging.INFO, format='%(asctime)s -%(name)s -%(levelname)s -%(message)s')

# Подію додавання нового студента до групи необхідно фіксувати у лог-файлі.

class Too_many_students (Exception):
    def __init__(self, message):
        self.message=message
    def __str__(self):
        return f"{self.message}"

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    def __str__(self):
        return f'{self.surname} {self.name} '


class Student(Person):

    def __init__(self, name, surname,age,middle_name):
        super().__init__(name, surname)
        self.age = age
        self.middle_name = middle_name

    def __str__(self):
        return f'{super().__str__()} {self.middle_name}, {self.age} years old '


class Group:

    def __init__(self, title, max_students=10):
        self.title = title
        self.__students = []
        self.max_student = max_students
        self.index = 0

    # def __len__(self):
    #     return self.max_student
    #
    # def __getitem__(self, index):
    #     if isinstance(index, slice):
    #         if index.start < 0 or index.stop > self.max_student:
    #             raise IndexError
    #         else:
    #
    #             start = 0 if index.start == None else index.start
    #             stop = self.max_student - 1 if index.stop == None else index.stop
    #             step = 1 if index.step == None else index.step
    #             for i in range(start, stop, step):
    #                 self.__students.append(i)
    #             return self.__students
    #     if isinstance(index, int):
    #         if index < self.max_student:
    #             return index
    #         else:
    #             raise IndexError
    #     raise TypeError()

    def add(self, student):

        if student not in self.__students and len(self.__students) < self.max_student:
            self.__students.append(student)
            logging.info(student)
        else:
            raise Too_many_students("Too_many_students")

    def __iter__(self):
        self.index=0
        return self

    def __next__(self):
        if self.index<len(self.__students):
            self.index+=1
            return self.__students[self.index-1]
        raise  StopIteration





    def remove(self, student):
        if student in self.__students:
            self.__students.remove(student)


    def search(self, age):
        res = []
        for student in self.__students:
            if student.age == age:
                res.append(student)

        return res


    def __str__(self):
        return f'{self.title}\n\n' + '\n'.join(map(str, self.__students))


a = Group('Python', max_students=10)

try:
    a.add(Student('Roman', 'Romanov', 21, "Romanovych"))
    a.add(Student('Oleg', 'Lyah', 21, "Dmytrovych"))
    a.add(Student('Maksym', 'Kovtunov', 30, "Dmytrovych"))
    a.add(Student('Oleksandr', 'Melnuk', 21, "Kostyantunovych"))
    a.add(Student('Taras', 'Topolya', 22, "Petrovych"))
    a.add(Student('Oleg', 'Skrypka', 23, "Anatoliyovych"))
    a.add(Student('Seghiy', 'Gorbatenko', 20, "Romanovych"))
    a.add(Student('Bogdan', 'Byt', 24, "Bogdanovych"))


except Too_many_students:
    print("Too_many_students")

# print()
# print(a)
# res = a.search(21)
# for item in res:
#     print(item.name, item.middle_name,  item.age)

for student in a:
    print(student.name, student.surname)

