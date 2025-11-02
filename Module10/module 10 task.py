import random

# Elevator Class
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print("Elevator is now at floor", self.current_floor)
        else:
            print("Already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print("Elevator is now at floor", self.current_floor)
        else:
            print("Already at the bottom floor.")

    def go_to_floor(self, target_floor):
        print("Moving elevator from floor", self.current_floor, "to floor", target_floor)
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print("Elevator arrived at floor", self.current_floor)
        print()


# Building Class
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, number, destination):
        if number >= 1 and number <= len(self.elevators):
            print("Running elevator", number, "to floor", destination)
            self.elevators[number - 1].go_to_floor(destination)
        else:
            print("Invalid elevator number.")

    def fire_alarm(self):
        print("Fire alarm! All elevators are moving to the bottom floor!")
        number = 1
        for e in self.elevators:
            print("Elevator", number, ":")
            e.go_to_floor(self.bottom)
            number += 1
        print("All elevators are now at the bottom floor.")
        print()


#Car Class
class Car:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def acceleration(self, change):
        self.current_speed += change
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.distance += self.current_speed * hours

    def print_info(self):
        print("Car:", self.reg_num,
              " Max Speed:", self.max_speed,
              " Current Speed:", self.current_speed,
              " Distance:", self.distance)


# Race Class
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.acceleration(change)
            car.drive(1)

    def print_status(self):
        print("Race status:", self.name)
        for car in self.cars:
            car.print_info()
        print()

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False


# Main Program
print("Elevator & Building Test")
building = Building(1, 10, 3)
building.run_elevator(1, 5)
building.run_elevator(2, 8)
building.fire_alarm()

print("Race Simulation")
cars = []
for i in range(1, 11):
    reg = "CAR-" + str(i)
    max_s = random.randint(100, 200)
    cars.append(Car(reg, max_s))

race = Race("Grand Demolition Derby", 8000, cars)
hours = 0

while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        race.print_status()

print("Race finished after", hours, "hours!")
race.print_status()

