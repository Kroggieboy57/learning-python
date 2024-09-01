class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Name:", self.name)
        print("Age:", self.age)

myinstance = Person("John Doe", 50)
myinstance.greeting()
