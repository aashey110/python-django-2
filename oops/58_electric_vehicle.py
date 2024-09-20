import random
import time

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity  # Max battery capacity in percentage
        self.current_battery_percent = 100         # Start with full battery (100%)
    
    def discharge(self, amount):
        if self.current_battery_percent - amount >= 0:
            self.current_battery_percent -= amount
        else:
            self.current_battery_percent = 0
        print(f"Battery discharged by {amount}%. Current charge: {self.current_battery_percent}%")

    def charge_solar(self, amount):
        if self.current_battery_percent + amount <= self.capacity:
            self.current_battery_percent += amount
        else:
            self.current_battery_percent = self.capacity
        print(f"Battery charged by {amount}% from solar energy. Current charge: {self.current_battery_percent}%")
    
    def get_percentage(self):
        return self.current_battery_percent

class Car:
    def __init__(self, destination):
        self.destination = destination
        self.battery = Battery(capacity=100)  # Initialize car with a battery
        self.current_location = "Home"
    
    def set_destination(self, new_destination):
        self.destination = new_destination
        print(f"Destination set to: {self.destination}")

    def move(self):
        if self.battery.get_percentage() > 0:
            print(f"Car is moving from {self.current_location} to {self.destination}...")
            self.battery.discharge(random.randint(10, 20))  # Randomly discharge battery
            self.current_location = self.destination
            print(f"Car reached {self.destination}.")
        else:
            print("Battery is empty. Please charge the car.")

    def detect_object(self):
        # Simulate object detection, randomly decides if an object is detected
        detected = random.random() < 0.3
        if detected:
            print("Object detected! Car is taking necessary action to avoid it.")
        else:
            print("No objects detected. Car is moving safely.")
        return detected

    def charge_battery_solar(self):
        if self.battery.get_percentage() < 100:
            solar_charge = random.randint(5, 15)
            self.battery.charge_solar(solar_charge)
        else:
            print("Battery is already full.")

    def show_battery_percentage(self):
        print(f"Current battery percentage: {self.battery.get_percentage()}%")

# Example usage
car = Car(destination="City Center")

# Set a new destination
car.set_destination("Park")

# Detect object and move the car
while True:
    time.sleep(2)
    print("***********************************************")
    if not car.detect_object():
        car.move()
    else:
        print("Car stopped due to detected object.")

    # Show battery percentage
    car.show_battery_percentage()

    # Charge battery using solar energy
    car.charge_battery_solar()

    # Show battery percentage after charging
    car.show_battery_percentage()
