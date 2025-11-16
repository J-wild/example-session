#inherited class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    print(f"name: {self.name}, age: {self.age}")

#main class
class Student(Person):
  def __init__(self, name, age, id ):
    super().__init__(name, age)
    self.id = id
    

  def get_Student_info(self):
    print(f"name: {self.name}, age: {self.age}, id: {self.id}")



p1 = Student("Josh", 20, 11223344)

p1.get_Student_info()