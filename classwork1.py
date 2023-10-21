class Student:
    group = "C2016"

    def __init__ (self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Student.counter = +1
        print("Объект был создан")
    def grow(self):
        self.height +=10
    def __str__(self):
        return f"I'm name {self.name}. My age is {self.age}"
    def __del__ (self):
        print("Object is deleted")

nick = Student ("Nick", 20, 180)
print (nick.age)
print (nick.group)

kate = Student ("kate", 20, 165)
print (kate.age)
print (kate.group)
   def to_chill(self):
       print("Rest time")
       self.gladness += 3
       self.p .progress -= 0.1
