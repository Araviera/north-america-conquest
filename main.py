import json
import pydata
import flags
import os
import research
import pydata
import time
import art


def main():
    # Load necessary files
    with open('data.json', 'r') as f:
        data = json.load(f)
    with open('save.json', 'r') as f:
        save = json.load(f)
    def load_save():
        with open('save.json', 'r') as f:
            return json.load(f)
        
    # make a turn counter
    def turn_counter():
        save['player_gold'] += save['player_miners'] * data['miner_profit']
        save['cpu1_gold'] += save['cpu1_miners'] * data['miner_profit']
        save['cpu2_gold'] += save['cpu2_miners'] * data['miner_profit']
        save['turn'] += 1
        with open('save.json', 'w') as f:
            json.dump(save, f, indent=4)
        

    pydata.clear_console()
    if save['save'] == "false":
        print(pydata.welcome)

        print("""
              Choose a country to play as:
               USA
                 Canada
                     Mexico
              """)
        player = input()
        while player.lower() not in ["usa", "canada", "mexico"]:
            pydata.clear_console()
            print("Invalid input. Please choose a valid country to play as:")
            player = input()
        save['player'] = player.lower()
        

    ##################  USA  ##################
        if save['player'] == "usa":



            save['player_gold'] = data['usa_gold']
            with open('save.json', 'w') as f:
                json.dump(save, f)

            save['player_miners'] = data['usa_miners']
            with open('save.json', 'w') as f:
                json.dump(save, f)
            
            save['player_firepower'] = data['usa_firepower']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)



            pydata.clear_console()
            save['player_flag'] = flags.usa
            print("And the rocket's red glare,")
            time.sleep(1)
            print("The bombs bursting in air,")
            time.sleep(1)
            print("Gave proof through the night")
            time.sleep(1)
            print("That our flag was still there;")
            time.sleep(1)
            print("O say does that star-spangled banner yet wave")
            time.sleep(1)
            print("O'er the land of the free and the home of the brave!")
            time.sleep(1)
            print("You have chosen to play as the mighty US!")
            print("Prepare to dominate north america!")
            time.sleep(2)

    ##################  Canada  ##################
        elif save['player'] == "canada":


            
            save['player_gold'] = data['canada_gold']
            with open('save.json', 'w') as f:
                json.dump(save, f)

            save['player_miners'] = data['canada_miners']
            with open('save.json', 'w') as f:
                json.dump(save, f)
            
            save['player_firepower'] = data['canada_firepower']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)



            pydata.clear_console()
            save['player_flag'] = flags.canada
            print("O Canada!")
            time.sleep(1)
            print("From far and wide, O Canada,")
            time.sleep(1)
            print("We stand on guard for thee.")
            time.sleep(1)
            print("God keep our land glorious and free!")
            time.sleep(1)
            print("O Canada, we stand on guard for thee.")
            time.sleep(1)
            print("O Canada, we stand on guard for thee.")
            time.sleep(1)



            print("You have chosen to play as Canada!")
            print("Prepare for an epic conquest!")
            print("your objective is clear. take over north america!")
            time.sleep(2)


    ##################  Mexico  ##################
        elif save['player'] == "mexico":


            
            save['player_gold'] = data['mexico_gold']
            with open('save.json', 'w') as f:
                json.dump(save, f)

            save['player_miners'] = data['mexico_miners']
            with open('save.json', 'w') as f:
                json.dump(save, f)
            
            save['player_firepower'] = data['mexico_firepower']
            with open('save.json', 'w') as f:
                json.dump(save, f)


            pydata.clear_console()
            save['player_flag'] = flags.mexico
            print("¡Guerra, guerra sin tregua al que intente")
            time.sleep(1)
            print("de la patria manchar los blasones!")
            time.sleep(1)
            print("¡Guerra, guerra! los patrios pendones")
            time.sleep(1)
            print("en las olas de sangre empapad.")
            time.sleep(1)
            print("¡Guerra, guerra! en el monte, en el valle,")
            time.sleep(1)
            print("los cañones horrísonos truenen")
            time.sleep(1)
            print("y los ecos sonoros resuenen")
            time.sleep(1)
            print("con las voces de ¡Unión! ¡Libertad!")


            pydata.clear_console()
            print("¡Viva México!")
            time.sleep(1)
            print("You have chosen to play as Mexico!")
            print("Prepare for an epic conquest!")
            time.sleep(2)

        save['save'] = "true"
        with open('save.json', 'w') as f:
            json.dump(save, f)

        save['turn'] = 1
        with open('save.json', 'w') as f:
            json.dump(save, f, indent=4)
        pydata.cpu()

    
####################################################
    while True:
        print("                                **North   America   Conquest**")
        print(f"""
              Turn: {save['turn']}   Country: {save['player']}   Gold: {save['player_gold']}   Miners: {save['player_miners']}   Firepower: {save['player_firepower']}
              """)
        save = load_save()
        print(save['player_flag'])
        action = input("""what would you like to do?
                       1. buy miners
                       2. research
                       3. attack
                       4. end turn
                       5. send a spy
                       6. exit (progress will be saved)
                       7. reset the game
                       """)

        if action == "gold":
            pydata.clear_console()
            print('you have:', save['player_gold'], 'amount of gold.')
            time.sleep(1)


        elif action == "turn":
            pydata.clear_console()
            print('you are on turn:', save['turn'])
            time.sleep(1)
        
        elif action == "5":
            pydata.clear_console()
            pydata.spy()
            time.sleep(3)
            pydata.clear_console()


        elif action == "1":
            pydata.clear_console()
            pydata.miners()
            time.sleep(1)
            pydata.clear_console()

        elif action == "firepower":
            pydata.clear_console()
            print('you have:', save['player_firepower'], 'amount of firepower.')
            time.sleep(1)


        elif action == "2":
            pydata.clear_console()
            research.researchmenu()
            time.sleep(1)
            pydata.clear_console()

############################################
############### DO NOT USE #################
############## SUPER BUGGY #################
############################################
        elif action == "debug":
            while True:
                time.sleep(1)
                turn_counter()
############################################
############################################
############################################

                

        elif action == "4":
            turn_counter()
            print("turn ended.")
            pydata.ai(action)
            time.sleep(2)
            pydata.clear_console()
                
        elif action == "3":
            if save['turn'] < 3:
                pydata.clear_console()
                print("You must wait until turn 3 to attack.")
                time.sleep(1)
                pydata.clear_console()
                
            else:
                pydata.clear_console()
                pydata.attack()
                time.sleep(3)


        elif action == "7":
            sure = input("Are you sure you want to reset the game? (yes/no) ")
            if sure == "yes":
                pydata.clear_console()
                with open('save.json', 'w') as f:
                    f.write('{"save": "false"}')
                print("Save has been reset.")
                time.sleep(1)
                pydata.clear_console()
                break
            else:
                pydata.clear_console()
                continue

        elif action == "6":
            sure = input("Are you sure you want to exit the game? (yes/no) ")
            if sure == "yes":
                pydata.clear_console()
                break
            else:
                pydata.clear_console()
                continue

        elif action == "test":
            pydata.clear_console()
            turn_counter()
            pydata.ai(action)
            action = "debug"
            time.sleep(1)


#super secret uwu cheat code
        elif action == "uwu":
            pydata.clear_console()
            print(flags.uwu)
            what = input("what is this character's name? ")
            if what.lower() == "astolfo":
                save['player_flag'] = flags.uwu
                save['player_gold'] += 100000000
                save['player_miners'] += 100
                save['player_firepower'] += 10000000
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print("uwu cheat code activated! you have unlocked the power of Astolfo!")
            else:
                print("you failed! game over! UwU")
                with open('save.json', 'w') as f:
                    f.write('{"save": "false"}')
                print("Save has been reset.")
                time.sleep(3)
                pydata.clear_console()
                break




        else:
            pydata.clear_console()
            print("Invalid input. Please choose a valid action")
            continue


if __name__ == '__main__':
    main()

