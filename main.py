# class Student:
#     def __init__(self,name,surname,age,grades):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.grades = grades
#     def info(self):
#         self.grades = sum(self.grades) / len(self.grades)
#         print(f"Student: {self.name} {self.surname}, {self.age} років.Його оцінки: {self.grades}")
#
# s1 = Student("Oleg","Havron", 28,[12,9,10,3,7])
# # print(s1.name,s1.surname, s1.age)
# s2 = Student("Oleksandr","Chernysh",90,[10,3,1,8,12])
# s1.info()
# s2.info()

class Human:
    def __init__(self,name):
        self.name = name
class Free_Space:
    def __init__(self,number):
        self.number = number
class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passengers = []
    def add_passenger(self,human):
        self.passengers.append(human)
    def print_passengers(self):
        if self.passengers != []:
            print(f"В машині {self.brand} є пасажири: ")
            for passengers in self.passengers:
                print(passengers.name)
        else:
            print(f"В машині {self.brand} немає пасажирів!")

car = Auto("Volkswagen polo")
car.add_passenger(Human("Oleg"))
car.add_passenger(Human("Vlad"))
car.add_passenger(Human("Andrii"))
car.add_passenger(Human("Igor"))
car.print_passengers()