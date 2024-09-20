#radar sense the enemy rocket and send to control system
#if enemy is detected then control system processes and send signal to missile system
#missile system launch rocket to destory the enemy's rocket
#write its program
import random
from colorama import Fore, Style
import time

class Airdefence:
    def __init__(self, enemy_rocket):
        self.enemy_rocket = enemy_rocket



    def radar(self):
            print(Fore.RED + "\nWarning!!!!!!! Enemy detected, Sending the signal to our control system!!!!!!!!!!!" + Style.RESET_ALL)
            



    def control_system(self):
        angle = random.randint(1,361)
        speed = random.randint(1,1000)
        print(f"\nEnemy's rocket is coming at {angle} degree")
        print(f"\nEnemy's rocket is coming at {speed} km/h")
        
    def missile_system(self):
        print(Fore.GREEN+"\nOur missile system is activated to hit enemy's rocket\n"+ Style.RESET_ALL)
        print("________________________________________________________________________________________________")



while  True:zz
    time.sleep(2)
    enemy_rocket = random.choice([True, False])



    air_defence_obj = Airdefence(enemy_rocket)


    if enemy_rocket == True:
        air_defence_obj.radar()
        random.randint(1,361)
        random.randint(1,361)
        air_defence_obj.control_system()
        air_defence_obj.missile_system()
    else:
        print("\nNo enemy detected\n")
        print("________________________________________________________________________________________________")