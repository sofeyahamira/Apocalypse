class Knife():
  name = 'knife'
  attack = 5
  health = 20

class Crowbar():
  name = 'crowbar'
  attack = 3
  health = 22


class Pitchfork():
  name = 'Pitchfork'
  attack = 4
  health = 21


### WEAPON SELECTION ###
weapon = 0
def weaponselect():
  while True:
    print ("There is a\n(1) knife\n(2) crowbar\n(3) pitchfork\n\nWhice will you choose?")
    selection = input("Type 1, 2 or 3: \n> ")
    if selection == "1":
        global weapon
        weapon = Knife
        return weapon

    elif selection == "2":
        weapon = Crowbar
        return weapon

    elif selection == "3":
        weapon = Pitchfork
        return weapon

    else:
        print('Type 1, 2 or 3')
        weaponselect()