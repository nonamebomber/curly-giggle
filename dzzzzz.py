# Дз 1, и у меня почему то не получается вывести всех животных
class zoo:
    group = "animals"

    def __init__(self, name, canfly=False, canswim=False, canwalk=True):
        self.name = name
        self.canfly = canfly
        self.canswim = canswim
        self.canwalk = canwalk

    def print(self):
        if self.canfly:
            print("полетіли")
            if self.canswim:
                print("поплили")
            elif self.canwalk:
                print("пішли")

tiger = zoo("тигр", canwalk=True)
bird = zoo("пташка", canfly=True)
dolphin = zoo("дельфін", canswim=True)
penguin = zoo("пiнгвін", canswim=True, canwalk=True)

tiger.print()
bird.print()
dolphin.print()
penguin.print()


# Дз 2

class Car:
   cars = 0

   def __init__(self, name):
       self.name = name
       self.speed = 0
       Car.cars += 1

   def start(self):
       self.speed +=10
       print ('машина поїхала')

   def stop(self):
       self.speed = 0
       print ('машина зупинилась')

car1 = Car("BMW")
car2 = Car("Mercedes")

car1.start()
car1.stop()

car2.start()
car2.stop()

print('Тест драйв пройшов успiшно')

