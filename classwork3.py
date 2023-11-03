import random
from data import job_list, brands_of_car
class Human:
    def __init__(self, name="Human",job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.car = car
        self.job = job
        self.home = home

    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food >= 0:
            self.shopping("food")
        if self.satiety > 100:
            self.satiety = 100
            return
        self.satiety += 5
        self.home.food -= 5


    def work (self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
    def shopping(self,manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage =  "fuel"
            else:
              self.to_repair()
              return
        if manage == "fuel":
            print ("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print("I bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print ("Hooray! Delicacies")
            self.money -= 5
            self.gladness += 10
            self.satiety += 2

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
    def to_repair(self):
        self.car.strength = 50
        self.car.fuel = 100

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name} 's life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")
    def is_alive(self):
        if self.gladness < 0:
            print("depression")
            return False
        if self.satiety < 0:
            print("Dead")
            return False
        if self.money < -500:
            print("Bankrupt!!!!")
            return False
    def live(self,day):
        if self.is_alive == False:
            return False
        if self.home is None:
            print("Settled in house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"Let's buy a {self.car.brand} car")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, I'm going to get a job {self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…\nSo I will clean the house ")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")
class House:
    def __init__(self):
        self.mess = 10
        self.food = 0
class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption =  brand_list[self.brand]['consumption']
    def drive (self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.strength -= 1
            self.fuel -= self.consumption
            return True
        else:
            print('the car cannot move')
            return False
class Job:
    def __init__ (self, job_list):
        self.job =  random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']

nick = Human ('Nick')

for day in range (1,365):
    if nick.live(day) ==  False:
        break

# class Auto:
#     def __init__ (self,brand):
#         self.brand =  brand
#         self.passengers = []
#
#     def add_passengers (self, human):
#         self.passengers.append(human)
#
#     def print_name_passengers(self):
#         if self.passengers != []:
#             print(f"Names of {self.brand} passengers")
#             for i in self.passengers:
#                 print(f'{i.name}')
#             else:
#                 print (f"There are no passengers in {self.brand}")
#
# nick =  Human ("Nick")
# kate = Human ("Kate")
# car = Auto ("BMW")
# car.add_passengers(nick)
# car.print_name_passengers()
# car.add_passengers(kate)
# car.print_name_passengers()

# human = Human('Ivan')
# print(human.home)
# human.get_home()
# print(human.home)
# print(human.home.mess)
# print(human.home.food)