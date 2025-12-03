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

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed,battery_capacity):
        super().__init__(registration_number , maximum_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed,tank_volume):
        super().__init__(registration_number , maximum_speed)
        self.tank_volume = tank_volume


#main program
car1 = ElectricCar("ABC-15",180,52.5)
car2 = GasolineCar("ACD-123",165,32.3)
car1.acceleration(100)
car2.acceleration(120)
car1.drive(3)
car2.drive(3)
print(f"Traveled distance for car1 is {car1.travelled_distance}")
print(f"Traveled distance for car2 is {car2.travelled_distance}")