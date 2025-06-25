import random
from colorama import Fore
import weapon
### ENEMY ###
class Zombie:
  health = random.randint(5,10)
  attack = random.randint(1,5)

def rolldice():
  dice = input('Press ENTER to role the dice\n')
  if dice == '':
    dice_roll = random.randint(1,6)
    if dice_roll > 3:
      print('You attack')
      Zombie.health = Zombie.health - weapon.weapon.attack
      print('Zombies Health is now', Zombie.health)

      if Zombie.health < 1:
        print('Zombie has been defeated')
        weapon.weapon.health = 30
        Zombie.health = random.randint(2,5)
        
      if weapon.weapon.health < 1:
        print('Oh no! You have been defeated :o')
        quit()
        
      if Zombie.health > 0:
        zomattack()

      if weapon.weapon.health > 0:
        attack()
        
    else:
      print('You attack and miss')
      zomattack()
      
      if Zombie.health < 1:
        print('Zombie has been defeated')
        weapon.weapon.health = 30
        Zombie.health = random.randint(2,5)

      if weapon.weapon.health < 1:
        print('Oh no! You have been defeated :o')
        quit()

      if weapon.weapon.health > 0:
        attack()

      if Zombie.health > 0:
        zomattack()


### ATTACKS ###
def attack():
  print(f'{Fore.WHITE}You attack')
  Zombie.health = Zombie.health - weapon.weapon.attack
  print('Zombies Health is now', Zombie.health)

def zomattack():
  print('Zombie is attacking')
  weapon.weapon.health = weapon.weapon.health - Zombie.attack
  print('Your health is now', weapon.weapon.health)

def spawnd():
  roll = random.randint(1,6)
  if roll > 3:
    rolldice()
  else:
    print('No zombie encountered')