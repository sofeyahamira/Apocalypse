from colorama import Fore
import sys, time
import weapon
import dice

### TYPE WRITER FUNCTION ###
def typewriter(message):
  for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
     
    if char != '\n':
      time.sleep(0.05)
    else:
      time.sleep(0.5)
  return ''
      
### STORY ###
while True:
  print("\033c")
  print(f"{Fore.BLUE}A stormy night, rain beating down like an angry zombie...")
  time.sleep(2)
  print(f"{Fore.GREEN}Jake, I think that IS a zombie")
  time.sleep(2)
  print(f"{Fore.BLUE}Huh- ")
  time.sleep(2)
  print(f"{Fore.WHITE}The door gets knock down")
  time.sleep(2)
  print(typewriter('''\n
  ▄▀█ █▀█ █▀█ █▀▀ ▄▀█ █░░ █▄█ █▀█ █▀ █▀▀
  █▀█ █▀▀ █▄█ █▄▄ █▀█ █▄▄ ░█░ █▀▀ ▄█ ██▄\n'''))
  enter = input(f'{Fore.RED}Press ENTER to continue... \n')
  if enter == '':
    print("\033c")
    print(f'{Fore.GREEN}Jake, go to the basement')
    time.sleep(2)
    print(f'{Fore.BLUE}But.. what about you?')
    time.sleep(2)
    print(f"{Fore.GREEN}I'll join you in a bit, promise.")
    time.sleep(3)
    print(f'{Fore.WHITE}')
    while True:
      print('''
    █░░ █▀█ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█ ▀   █▄▄ ▄▀█ █▀ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀
    █▄▄ █▄█ █▄▄ █▀█ ░█░ █ █▄█ █░▀█ ▄   █▄█ █▀█ ▄█ ██▄ █░▀░█ ██▄ █░▀█ ░█░\n''')
      enter = input(f"{Fore.RED}Press enter to continue... \n")
      if enter == '':
        print("\033c")
        print(typewriter(f"{Fore.BLUE}I should go help. But first, let's grab a weapon. \n"))
        time.sleep(2)
        print(f'{Fore.WHITE}')
        weapon.weaponselect()
        print(f'{Fore.BLUE}This weapon is quite sick! My sister is going to be so impress when she sees me fight!')
        time.sleep(3)
        print(f'''{Fore.WHITE}
    █░░ █▀█ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█ ▀   █▀█ █░█ ▀█▀ █▀ █ █▀▄ █▀▀
    █▄▄ █▄█ █▄▄ █▀█ ░█░ █ █▄█ █░▀█ ▄   █▄█ █▄█ ░█░ ▄█ █ █▄▀ ██▄''')
        enter = input(f"{Fore.RED}Press enter to continue... \n")
        if enter == '':
          print("\033c")
          print(f'{Fore.BLUE}Where is she?')
          time.sleep(2)
          print(f'{Fore.WHITE}Someone taps your shoulder and pulls you into a bush.')
          time.sleep(1)
          print('You swing your weapon')
          time.sleep(2)
          print(f'{Fore.BLUE}AHHHH TAKE THAT YOU ZOMBIE')
          time.sleep(2)
          print(f'{Fore.MAGENTA}Woah, chill kid. I aint no zombie')
          time.sleep(2)
          print(f'{Fore.BLUE}OH, Im sorry.. Uh... Sir?')
          time.sleep(2)
          print(f"{Fore.MAGENTA}No sweat bro, call me Chad! Since were both still human, How about we chill at my place? Me and my bro are working on a cure for this Apocalypse")
          time.sleep(3)
          print(f'{Fore.BLUE}Thanks for the offer Chad but im looking for my sister,\nher name is Jade.\nA bunch of zombies broke into our place and she stayed to fight them.')
          time.sleep(3)
          print(f"{Fore.MAGENTA}I'm sorry to say bro, but, I think they got her.")
          time.sleep(2)
          print(f"{Fore.BLUE}Nah, she's really tough.")
          time.sleep(2)
          print(f"{Fore.MAGENTA}I'll help you out kid.")
          time.sleep(2)
          print(f"{Fore.BLUE}Than-")
          time.sleep(2)
          print(f"{Fore.WHITE}You feel a touch on you shoulder and hesitantly turn behind...")
          time.sleep(2)
          print(f"{Fore.BLUE}J... Jade?")
          time.sleep(2)
          print(f"{Fore.WHITE}Your sister attacks")
          time.sleep(2)
          print('Chad pulls you aside and gets his weapon ready for attack')
          time.sleep(2)
          print(f"{Fore.BLUE}NO THATS MY SISTER! DON'T-  ")
          time.sleep(2)
          print(f"{Fore.MAGENTA}But kid, she's- ")
          time.sleep(2)
          print(f"{Fore.WHITE}A white van pulls over")
          time.sleep(2)
          print(f"{Fore.CYAN}CHAD GET IN!")
          time.sleep(2)
          print(f"{Fore.BLUE}But my-")
          time.sleep(2)
          print(f"{Fore.WHITE}Chad pulls you in the van...")
          time.sleep(2)
          while True:
            print("""
      █░░ █▀█ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█ ▀   █░█ ▄▀█ █▄░█
      █▄▄ █▄█ █▄▄ █▀█ ░█░ █ █▄█ █░▀█ ▄   ▀▄▀ █▀█ █░▀█""")
            enter = input(f"{Fore.RED}Press enter to continue... \n")
            if enter == '':
              print("\033c")
              print(f"{Fore.BLUE}Let me go back! I want to see my sister")
              time.sleep(2)
              print(f"{Fore.CYAN}When we make this cure, you can go back to your sister without her turning you brain-less...")
              time.sleep(2)
              while True:
                print(f"""{Fore.WHITE} 
        █░░ █▀█ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█ ▀   █▀▀ █░█ ▄▀█ █▀▄ ▀ █▀   █▄▄ ▄▀█ █▀ █▀▀
        █▄▄ █▄█ █▄▄ █▀█ ░█░ █ █▄█ █░▀█ ▄   █▄▄ █▀█ █▀█ █▄▀ ░ ▄█   █▄█ █▀█ ▄█ ██▄""")
                enter = input(f"{Fore.RED}Press enter to continue... \n")
                if enter == '':
                  print("\033c")
                  print(f"{Fore.BLUE}I have to help my sister..")
                  time.sleep(2)
                  print(f"{Fore.MAGENTA}You'll help her a lot by staying safe and helping us make the zombie cure")
                  time.sleep(2)
                  print(f"{Fore.BLUE}What's in the cure anyway")
                  time.sleep(2)
                  print(f"{Fore.CYAN}A ton of chemicals")
                  time.sleep(2)
                  print(f"{Fore.BLUE}Do they have to drink it?")
                  time.sleep(2)
                  print(f"{Fore.CYAN}No Way! That's gross, we'll just spray the cure and whoever touches it will be cured!")
                  time.sleep(2)
                  print("Hey Chad we're missing an ingredient.")
                  time.sleep(2)
                  print(f"{Fore.MAGENTA}What ingredient?")
                  time.sleep(2)
                  print(f"{Fore.CYAN}The one I told you to bring but instead you found a kid, no offence.")
                  time.sleep(2)
                  print(f"{Fore.BLUE}None taken!")
                  time.sleep(2)
                  print(f"{Fore.MAGENTA}Hey kid wanna fight zombies?")
                  time.sleep(2)
                  print(f"{Fore.BLUE}I thought I should stay safe?")
                  time.sleep(2)
                  print(f"{Fore.MAGENTA}You will be! As long as you follow my instructions ;)")
                  time.sleep(2)
                  print(f"{Fore.BLUE}YEAH LET'S GO!")
                  time.sleep(2)
                  while True:
                    print(f'''{Fore.WHITE}
            █░░ █▀█ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█ ▀   █▀█ █░█ ▀█▀ █▀ █ █▀▄ █▀▀
            █▄▄ █▄█ █▄▄ █▀█ ░█░ █ █▄█ █░▀█ ▄   █▄█ █▄█ ░█░ ▄█ █ █▄▀ ██▄''')
                    enter = input(f"{Fore.RED}Press enter to continue... \n")
                    if enter == '':
                      print("\033c")
                      print(f"{Fore.MAGENTA}Alright kid, which path should we take on first?")
                      choice = input('(1) Left\n(2) Right?\n> ')
                      if choice == '1':
                        print(f"{Fore.WHITE}You walk along the path before being greated by a zombie")
                        dice.rolldice()
                        print(f'{Fore.MAGENTA}Wow kid, your quite tough!')
                      elif choice == '2':
                        print('Zombie avoided')
                      time.sleep(2)  
                      while True:
                        print(f'''{Fore.WHITE}
                      █░░ █▀█ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█ ▀   █▀ █▀▀ █ █▀▀ █▄░█ █▀▀ █▀▀   █░░ ▄▀█ █▄▄
                      █▄▄ █▄█ █▄▄ █▀█ ░█░ █ █▄█ █░▀█ ▄   ▄█ █▄▄ █ ██▄ █░▀█ █▄▄ ██▄   █▄▄ █▀█ █▄█''')
                        enter = input(f"{Fore.RED}Press enter to continue... \n")
                        if enter == '':
                          print("\033c")
                          print(f"{Fore.MAGENTA}Alright kid, we're in the state scince lab")
                          time.sleep(2)
                          print("All we need to do now if get to the top floor")
                          time.sleep(2)
                          print("There are 2 elevators, which should we go in?")
                          choice = input("1. The right one\n2. The left one\n>  ")
                          print(f'{Fore.WHITE}')
                          if choice == '1':
                            print('You have entered the right elevator')
                          elif choice == '2':
                            print('You have entered the left elevator')
                            time.sleep(2)
                            print('3 zombies appeared!')
                            dice.rolldice()
                            dice.rolldice()
                            dice.rolldice()
                            print(f"{Fore.MAGENTA}WOW that was hard")
                            time.sleep(2)
                          print(f'{Fore.WHITE}Arrived at floor 3')
                          time.sleep(2)
                          print(f'{Fore.MAGENTA}Alright, now we have to sneak into that room, hopefully not running into more zombies!')
                          time.sleep(2)
                          print(f"Make sure to stay quite...")
                          time.sleep(2)
                          print(f'{Fore.WHITE}Pick your move:\n(1) Crawl under the table\n(2) Hide behind the curtains')
                          choice = input('> ')
                          if choice == '1':
                            print('Uh oh, you meet some zombies under the table')
                            dice.rolldice()
                            dice.rolldice()
                          elif choice == '2':
                            print('The brainless dont spot you!')
                          time.sleep(2)
                          print(f"{Fore.BLUE}The last ingredient!")
                          time.sleep(2)
                          print(f"{Fore.WHITE}You grab the ingredient!")
                          time.sleep(2)
                          print("You run out of the room and bump into another zombie...")
                          time.sleep(2)
                          print(f"{Fore.BLUE}J.. Jade...")
                          time.sleep(2)
                          print("Move Jade! I don't want to hurt you...")
                          time.sleep(2)
                          choice = input(f"{Fore.WHITE}Choose your next move...\n1. Attack Jade\n2. Get turned into a zombie\n> ")
                          if choice == '1':
                            dice.rolldice()
                            print(f'{Fore.BLUE}...')
                            time.sleep(2)
                            print("Let's go make that cure...")
                            time.sleep(2)
                            print(f"{Fore.WHITE}You head back to Chad's base and help make the cure.")
                            time.sleep(2)
                            print(f"{Fore.MAGENTA}Alright, we need to get to the highest point of this city and use the giant spray we built to spray the cure.")
                            time.sleep(2)
                            print(f"{Fore.WHITE}You head to the light house")
                            time.sleep(2)
                            print(f"{Fore.CYAN}3... 2.. 1. SPRAY")
                            time.sleep(2)
                            print(f"{Fore.WHITE}With great force, the 3 of you spray the cure, curing the entire city..")
                            time.sleep(2)
                            print(f"{Fore.BLUE}We.. WE DID IT")
                            time.sleep(2)
                            print(f"{Fore.MAGENTA}Nice work team.")
                            time.sleep(2)
                            print(f"{Fore.WHITE}You spot your sister from the top of the lighthouse.")
                            time.sleep(2)
                            print(f"{Fore.BLUE}JADE!")
                            time.sleep(2)
                            print(f"{Fore.WHITE}You rush down the lighthouse and hug your sister.")
                            time.sleep(2)
                            print(f"{Fore.GREEN}Jake... wake up...")
                            time.sleep(2)
                            print(f"{Fore.WHITE}You get up from bed to see your sister standing beside you...")
                            time.sleep(2)
                            time.sleep(1)
                            print("""
  ████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗░██████╗  ███████╗░█████╗░██████╗░
  ╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝██╔════╝  ██╔════╝██╔══██╗██╔══██╗
  ░░░██║░░░███████║███████║██╔██╗██║█████═╝░╚█████╗░  █████╗░░██║░░██║██████╔╝
  ░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░░╚═══██╗  ██╔══╝░░██║░░██║██╔══██╗
  ░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗██████╔╝  ██║░░░░░╚█████╔╝██║░░██║
  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝
  
  ██████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗███╗░░██╗░██████╗░
  ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██║████╗░██║██╔════╝░
  ██████╔╝██║░░░░░███████║░╚████╔╝░██║██╔██╗██║██║░░██╗░
  ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██║██║╚████║██║░░╚██╗
  ██║░░░░░███████╗██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝
  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░
  
  ░█████╗░██████╗░░█████╗░░█████╗░░█████╗░██╗░░░░░██╗░░░██╗██████╗░░██████╗███████╗
  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░░░╚██╗░██╔╝██╔══██╗██╔════╝██╔════╝
  ███████║██████╔╝██║░░██║██║░░╚═╝███████║██║░░░░░░╚████╔╝░██████╔╝╚█████╗░█████╗░░
  ██╔══██║██╔═══╝░██║░░██║██║░░██╗██╔══██║██║░░░░░░░╚██╔╝░░██╔═══╝░░╚═══██╗██╔══╝░░
  ██║░░██║██║░░░░░╚█████╔╝╚█████╔╝██║░░██║███████╗░░░██║░░░██║░░░░░██████╔╝███████╗
  ╚═╝░░╚═╝╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░░░░╚═════╝░╚══════╝""")
                            quit()
                              
                          elif choice == '2':
                            print(f'{Fore.BLUE}CHAD!')
                            time.sleep(2)
                            print(f"{Fore.WHITE}You pass the last ingredient to Chad")
                            time.sleep(2)
                            print(f"{Fore.BLUE}Go make that cure...")
                            time.sleep(2)
                            print(f"{Fore.WHITE}Chad nodes as your sister attacks...")
                            time.sleep(2)
                            print("You've been turned into a zombie...")
                            time.sleep(2)
                            print(f"{Fore.GREEN}Jake...")
                            time.sleep(2)
                            print(f"{Fore.BLUE}JADE")
                            time.sleep(2)
                            print(f"{Fore.WHITE}You run towards your sister in the white room...")
                            time.sleep(2)
                            print(f"{Fore.BLUE}Is... is this real?")
                            time.sleep(2)
                            print(f"{Fore.GREEN}Nope, you're just dreaming")
                            time.sleep(2)
                            print(f"{Fore.WHITE}You're alarm clock rings...")
                            time.sleep(3)
                            print("""
  ████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗░██████╗  ███████╗░█████╗░██████╗░
  ╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝██╔════╝  ██╔════╝██╔══██╗██╔══██╗
  ░░░██║░░░███████║███████║██╔██╗██║█████═╝░╚█████╗░  █████╗░░██║░░██║██████╔╝
  ░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░░╚═══██╗  ██╔══╝░░██║░░██║██╔══██╗
  ░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗██████╔╝  ██║░░░░░╚█████╔╝██║░░██║
  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝
  
  ██████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗███╗░░██╗░██████╗░
  ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██║████╗░██║██╔════╝░
  ██████╔╝██║░░░░░███████║░╚████╔╝░██║██╔██╗██║██║░░██╗░
  ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██║██║╚████║██║░░╚██╗
  ██║░░░░░███████╗██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝
  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░
  
  ░█████╗░██████╗░░█████╗░░█████╗░░█████╗░██╗░░░░░██╗░░░██╗██████╗░░██████╗███████╗
  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░░░╚██╗░██╔╝██╔══██╗██╔════╝██╔════╝
  ███████║██████╔╝██║░░██║██║░░╚═╝███████║██║░░░░░░╚████╔╝░██████╔╝╚█████╗░█████╗░░
  ██╔══██║██╔═══╝░██║░░██║██║░░██╗██╔══██║██║░░░░░░░╚██╔╝░░██╔═══╝░░╚═══██╗██╔══╝░░
  ██║░░██║██║░░░░░╚█████╔╝╚█████╔╝██║░░██║███████╗░░░██║░░░██║░░░░░██████╔╝███████╗
  ╚═╝░░╚═╝╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░░░░╚═════╝░╚══════╝""")
                            quit()
                              