import random


class Entity:
    def __init__(self, location):
        self.location = location

class Missile(Entity):
    def __init__(self, target_location):
        Entity.__init__(self,target_location)
        self.destroyed = False
   
    def move(self):
        print(f"Missile moving towards {self.location}.")

class IronDome(Entity):
    def __init__(self, location):
        Entity.__init__(self,location)

    def intercept(self, missile):
        interception_success = random.random() > 0.2
        if interception_success:
            missile.destroyed = True
            print(f"Missile intercepted at {missile.location}.")
        else:
            print(f"Missile missed by Iron Dome at {self.location}.")

class Radar:
    def __init__(self, range):
        self.range = range
   
    def detect(self, missile):
        detected = random.random() > 0.1
        if detected:
            print(f"Missile detected at {missile.location}.")
            return True
        else:
            print("Missile not detected.")
            return False

target_location = "City A"
missile = Missile(target_location)

radar = Radar(range=100)
iron_dome = IronDome(location="City A")

if radar.detect(missile):
    iron_dome.intercept(missile)
else:
    print("Missile not intercepted.")

if missile.destroyed:
    print("The city is safe.")
else:
    print(f"Missile hit {target_location}!")
