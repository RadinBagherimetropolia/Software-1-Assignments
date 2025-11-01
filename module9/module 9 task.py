import random
#car class
class Car:
    def __init__(self ,registration_number , maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def print_info(self):
        print(f" registration number: {self.registration_number} \n"
              f" maximum speed: {self.maximum_speed} \n"
              f" current speed: {self.current_speed} \n"
              f" travelled distance: {self.travelled_distance}")

    def acceleration(self , speed_change):
        if speed_change < 0 :
            if self.current_speed == 0 or  self.current_speed < 0:
               print(f"the current speed is {self.current_speed} you can not change it")
            else:
                self.current_speed = self.current_speed + speed_change
        else:
            if self.current_speed + speed_change > self.maximum_speed:
                print(f"the maximum speed is {self.maximum_speed} "
                      f"but the change is higher than maximum")
            else:
               self.current_speed += speed_change

    def drive(self , hours):
        self.travelled_distance += self.current_speed * hours


#main program
cars = []
for i in range(1 , 11):
    ident = f"ABC-{i}"
    high_speed = random.randint(100 , 200)
    new_car = Car(ident , high_speed)
    cars.append(new_car)

hours = 0
race_over = False
while not race_over:
    hours += 1
    for car in cars:
        speed_change = random.randint(-10 , 15)
        car.acceleration(speed_change)
        car.drive(1)
    for car in cars:
        if car.travelled_distance >= 10000:
            race_over = True

for car in cars:
    car.print_info()


