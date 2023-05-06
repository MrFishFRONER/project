# class Human:
#     def __init__(self:
#         print('Hello')
# class Student(Human):
#     def __init__(self):
#         super().__init__()
#         print('World')
#
# a = Student()
# class Class1:
#     var = 20
#     def __init__(self):
#         self.var = 10
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)
# a = Class2()
#

# class Animal:
#     def __init__(self,name,age,species):
#         self.name = name
#         self.age = age
#         self.species = species
#     def make_sound(self):
#         print("The animal makes sound!")
#
# class Dog(Animal):
#     def __init__(self,name,age):
#         super().__init__(name,age,species="Dog")
#     def make_sound(self):
#         print("Woof")
# class Cat(Animal):
#     def __init__(self,name,age):
#         super().__init__(name,age,species="Cat")
#     def make_sound(self):
#         print("Meow")
#
# cat = Cat("Fluffy", 4)
# dog = Dog("Buddy", 6)
#
# print(cat.name)
# print(cat.species)
#
# print(dog.name)
# print(dog.species)
# cat.make_sound()
# dog.make_sound()

# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
# class Student(Person):
#     def __init__(self,name,age,student_id):
#         super().__init__(name, age,gender="male")
#         self.student_id = student_id
#     def say_hello(self):
#         print(f"Hello, my name is {self.name}, I`m {self.gender} and my student ID is {self.student_id}")
# class Teacher(Person):
#     def __init__(self,name,age,subject):
#         super().__init__(name, age, gender="female")
#         self.subject = subject
#     def say_hello(self):
#         print(f"Hello, my name is {self.name}, I`m {self.gender} and my subject is {self.subject}")
#
# class Engineer(Person):
#     def __init__(self, name, age, company):
#         super().__init__(name, age, gender='male')
#         self.company = company
#     def say_hello(self):
#         print(f"Hello, my name is {self.name}, I`m {self.gender} and I work for {self.company}")
#
#
#
# student1 = Student("Max", 23, "7353573")
# student1.say_hello()
# teacher1 = Teacher("Julia", 32, "ICT")
# teacher1.say_hello()
# engineer1 = Engineer("John", 47, "BMW")
# engineer1.say_hello()
# class Shape:
#     def __init__(self,color):
#         self.color = color
#     def get_color(self):
#         self.color
#
# class Circle(Shape):
#     def __init__(self,color,radius):
#         super().__init__(color)
#         self.radius = radius
#
#     def say_form(self, ):
#         print(f'This circle has color {self.color} and radius {self.radius} centimeters')
# class Rectangle(Shape):
#     def __init__(self,color,width,height):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#     def say_form(self,):
#         print(f'This rectangle has color {self.color} , width {self.width} centimeters and height {self.height} centimeters')
# circle1 = Circle('red', 32)
# circle1.say_form()
# rectangle1 = Rectangle('blue', 20,14)
# rectangle1.say_form()

# class Vehicle:
#     def __init__(self,brand, model, speed):
#         self.brand = brand
#         self.model = model
#         self.speed = speed
# class Car(Vehicle):
#     def __init__(self,brand, model, speed,doors,max_speed):
#         super().__init__(brand, model, speed)
#         self.doors = doors
#         self.max_speed = max_speed
#     def say_info(self):
#         print(f'This car from {self.brand} brand, its {self.model} model which has {self.doors} doors, it has avange speed like {self.speed}km/h and max speed is {self.max_speed}km/h')
# car1 = Car('BMW','i5',90,4,230)
# car1.say_info()

# class Car:
#     def __init__(self,brand,year):
#         self.brand = brand
#         self.year = year
# class ElectricCar(Car):
#     def __init__(self,brand,year,acum,lenght):
#         super().__init__(brand,year)
#         self.acum = acum
#         self.lenght = lenght
#     def say_info(self):
#         print(f'brand: {self.brand}, year of release: {self.year},acumulator: {self.acum}, amouth of km by full charge:{self.lenght}')
# class Tesla(ElectricCar):
#     def __init__(self,brand,year,acum,lenght,autopilot,engine):
#         super().__init__(acum,lenght,brand,year,)
#         self.autopilot = autopilot
#         self.engine = engine
#     def say_info(self):
#         print(f'brand: {self.brand}, year of release: {self.year},acumulator: {self.acum},engine: {self.engine}, amouth of km by full charge:{self.lenght}. Do it have autopilot? {self.autopilot}')
#
# car = Tesla('acum321Tesla',1000, 'Tesla',2010,'yes','engine321Tesla' )
# car.say_info()
# elcar = ElectricCar('acum321Tesla',1000, 'Tesla',2010, )
# elcar.say_info()
