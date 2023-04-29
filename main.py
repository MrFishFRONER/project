class Student:
    def __init__(self,name,surname,age,grades):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = grades
    def info(self):
        self.grades = sum(self.grades) / len(self.grades)
        print(f"Student: {self.name} {self.surname}, {self.age} років.Його оцінки: {self.grades}")

s1 = Student("Oleg","Havron", 28,[12,9,10,3,7])
# print(s1.name,s1.surname, s1.age)
s2 = Student("Oleksandr","Chernysh",90,[10,3,1,8,12])
s1.info()
s2.info()
