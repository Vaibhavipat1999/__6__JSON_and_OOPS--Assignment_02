# 👉 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. 
# You must perform the following operations:

# 🔴 a. It should have a function ‘description()’ which prints the name and age of the dog.
# 🔴 b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# 🔴 c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# 🔴 d. Create objects and implement the above functionalities.

class Dog:
  def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

  def description(self):
        return f"{self.name} is {self.age} years old"

  def get_info(self):
        return f"{self.name} is {self.coat_color} in color"

class JackRussellTerrier(Dog):
  def __init__(self, name="Mickey", age='7', coat_color="grey"):
        super().__init__(name,age,coat_color)

class Bulldog(Dog):
  def __init__(self, name="Lucky", age='4', coat_color="Brown"):
        super().__init__(name,age,coat_color)

a = JackRussellTerrier()
b = Bulldog()
print(a.description())
print(a.get_info())
print(b.description())
print(b.get_info())