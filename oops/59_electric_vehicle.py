import random
import time
class Battery:
    def __init__(self, charge):
        self.charge = charge
        self.current_battery_percent = 100
    def battery_consume(self, amount):
        if self.current_battery_percent - amount >= 0:
            self.current_battery_percent -= amount
        else:
            self.current_battery_percent = 0
            print(f"Battery reduced by {amount}%. Current charge: {self.charge}%")

    def charge_solar(self, amount):
        if self.current_battery_percent + amount <= self.charge:
            self.current_battery_percent = self.current_battery_percent + amount
        else:
            self.current_battery_percent = self.charge
        print(f"Battery charged by {amount}% from solar energy. Current charge: {self.current_battery_percent}%")

    def show_battery(self):
        return self.current_battery_percent
        
class Car:
    def __init__(self, destination):
        self.destination = destination
        self.battery = Battery(charge = 100)
        self.current_location = "Home"

    def set_destination(self, new_destination):
        self.destination = new_destination
        print(f"Destination set to {self.destination}")

    def move(self):
        if self.battery.current_battery_percent > 0:
            print(f"Car is moving from {self.current_location} to {self.destination}...")
            self.battery.battery_consume(random.randint(10, 20)) 
            self.current_location = self.destination
            print(f"Car reached {self.destination}.")
        else:
            print("Battery is empty. Please charge the car.")
    
    def object_detect(self):
        detected = random.random() < 0.3
        if detected:
            print("Object detected! Car is taking necessary action to avoid it.")
        else:
            print("No objects detected. Car is moving safely.")
        return detected
    
    def solar_charge(self):
        if self.battery.show_battery() < 100:
            solar_charge = random.randint(5, 15)
            self.battery.charge_solar(solar_charge)
        else:
            print("Battery is already full.")

    def show_battery_percentage(self):
        print(f"Current battery percentage: {self.battery.show_battery()}%")
        

car = Car(destination="Film Hall")

# Set a new destination
car.set_destination("Office")

# Detect object and move the car
while True:
    time.sleep(2)
    print("***********************************************")
    if not car.object_detect():
        car.move()
    else:
        print("Car stopped due to detected object.")

    car.show_battery_percentage()

    car.solar_charge()

    car.show_battery_percentage()