import json
import pydata
import flags
import os
import research
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
        
##################  Turns  ##################
    def turn_counter():
        save['player_gold'] += save['player_miners'] * data['miner_profit']
        save['cpu1_gold'] += save['cpu1_miners'] * data['miner_profit']
        save['cpu2_gold'] += save['cpu2_miners'] * data['miner_profit']
        save['turn'] += 1
        with open('save.json', 'w') as f:
            json.dump(save, f, indent=4)
        
##################  Start  ##################
    pydata.clear_console()
    #when there is no save
    if save['save'] == "false":
        #game starts from the beginning
        print(pydata.welcome)
        #player chooses a country to play as
        player = input("""
              Choose a country to play as:
               USA
                 Canada
                     Mexico
                       
              """)
        #while loop to make sure the player chooses a valid country
        while player.lower() not in ["usa", "canada", "mexico"]:
            pydata.clear_console()
            player = input("Invalid input. Please choose a valid country to play as: ")
        
        #save the player's choice into lowercase for convenience
        save['player'] = player.lower()

            
        

    ##############################  USA  ##################
        if save['player'] == "usa":
            #set the player's gold, miners, and firepower to the default values
            save['player_gold'] = data['usa_gold']
            save['player_miners'] = data['usa_miners']
            save['player_firepower'] = data['usa_firepower']
            #save the player's gold, miners, and firepower into the save file
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            pydata.clear_console()


    ###########################  Canada  ##################
        elif save['player'] == "canada":


            #save the player's gold, miners, and firepower into the save file
            save['player_gold'] = data['canada_gold']
            save['player_miners'] = data['canada_miners']
            save['player_firepower'] = data['canada_firepower']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)


            pydata.clear_console()


    ##################  Mexico  ##################
        elif save['player'] == "mexico":


            #save the player's gold, miners, and firepower into the save file
            save['player_gold'] = data['mexico_gold']
            save['player_miners'] = data['mexico_miners']            
            save['player_firepower'] = data['mexico_firepower']
            with open('save.json', 'w') as f:
                json.dump(save, f)

            pydata.clear_console()

        save['save'] = "true"
        with open('save.json', 'w') as f:
            json.dump(save, f)

        save['turn'] = 1
        with open('save.json', 'w') as f:
            json.dump(save, f, indent=4)
        save["nuke"] = "False"
        with open('save.json', 'w') as f:
            json.dump(save, f)
        pydata.cpu()

    
####################################################
    while True:

        print(f"""
                                                **North America Conquest**
              Turn: {save['turn']}   Country: {save['player']}   Gold: {save['player_gold']}   Miners: {save['player_miners']}   Firepower: {save['player_firepower']}
              """)
        
        save = load_save()
        action = input("""what would you like to do?
                       1. buy miners
                       2. research
                       3. attack
                       4. end turn
                       5. send a spy
                       6. exit (progress will be saved)
                       7. reset the game
                       """)
        
#################################  Actions  ################################
##################  Miners  ##################
        if action == "1":
            pydata.clear_console()
            pydata.miners()
            time.sleep(1)
            pydata.clear_console()

##################  Research  ##################
        elif action == "2":
            pydata.clear_console()
            research.researchmenu()
            time.sleep(1)
            pydata.clear_console()

##################  Attack  ##################
        elif action == "3":
            if save['turn'] < 6:
                pydata.clear_console()
                print("You must wait until turn 6 to attack.")
                time.sleep(1)
                pydata.clear_console()
            else:
                pydata.clear_console()
                pydata.attack()
                time.sleep(3)

##################  End Turn  ##################
        elif action == "4":
            turn_counter()
            print("turn ended.")
            pydata.ai(action)
            time.sleep(4)
            pydata.clear_console()

##################  Spy  ##################
        elif action == "5":
            pydata.clear_console()
            pydata.spy()
            time.sleep(3)
            pydata.clear_console()

##################  Exit  ##################
        elif action == "6":
            sure = input("Are you sure you want to exit the game? (yes/no) ")
            if sure == "yes":
                pydata.clear_console()
                break
            else:
                pydata.clear_console()
                continue

##################  Reset  ##################
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

##################  UwU  ##################
        elif action == "uwu":
            pydata.clear_console()
            print(flags.uwu)
            what = input("what is this character's name? ")
            if what.lower() == "astolfo":
                save['player_gold'] += 100000000
                save['player_miners'] += 100
                save['player_firepower'] += 10000000
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                pydata.clear_console()
                print("uwu cheat code activated! you have unlocked the power of Astolfo!")
                time.sleep(3)
            else:
                pydata.clear_console()
                print("you failed! game over! UwU")
                with open('save.json', 'w') as f:
                    f.write('{"save": "false"}')
                print("Save has been reset.")
                time.sleep(3)
                pydata.clear_console()
                break



##################  Invalid Input  ##################
        else:
            pydata.clear_console()
            print("Invalid input. Please choose a valid action")
            continue


if __name__ == '__main__':
    main()

