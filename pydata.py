import json
import random
import os
import time
import art

av_countries = ["usa", "canada", "mexico"]

with open('save.json', 'r') as f:
    save = json.load(f)
with open('data.json', 'r') as f:
    data = json.load(f)

############# Welcome Message ################
welcome = """
******************************************************
Welcome to North America Conquest!
******************************************************

In this game, you have the power to conquer North America.
Choose your country wisely and embark on an epic journey of conquest and domination.

You can play as one of the mighty nations of North America:
- USA: The land of opportunity and freedom!. (Easy mode)
- Canada: The great northern wilderness!. (Medium mode)
- Mexico: The land of ancient ruins!. (Hard mode)

Research and acquire powerful weapons to strengthen your forces and crush your enemies.


Let the conquest begin!
******************************************************
"""

############################################################################################################
###################### Clear Console Function ############################################################
def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

############################################################################################################
###################### Spy Function ######################################################################
def spy():
    with open('save.json', 'r') as f:
        save = json.load(f)
    with open('data.json', 'r') as f:
        data = json.load(f)

    choice = input(f"""
                    Who do you want to spy on?
                    1. {save['cpu1']} (will cost {data['spy_cost']} gold)
                    2. {save['cpu2']} (will cost {data['spy_cost']} gold)
                    3. Exit
                    """)

    if choice == "1":
        if save['player_gold'] < data['spy_cost']:
            print("You don't have enough gold to spy on", save['cpu1'])
        else:
            save['player_gold'] -= data['spy_cost']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            print(f"""
                You have spied on {save['cpu1']}!
                {save['cpu1']} has {save['cpu1_gold']} gold, {save['cpu1_miners']} miners, and {save['cpu1_firepower']} firepower.
                """)
            
    elif choice == "2":
        if save['player_gold'] < data['spy_cost']:
            print("You don't have enough gold to spy on", save['cpu2'])
        else:
            save['player_gold'] -= data['spy_cost']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            print(f"""
                You have spied on {save['cpu2']}!
                {save['cpu2']} has {save['cpu2_gold']} gold, {save['cpu2_miners']} miners, and {save['cpu2_firepower']} firepower.
                """)
############################################################################################################
###################### Miners Function ###################################################################
def miners():
    with open('save.json', 'r') as f:
        save = json.load(f)
    with open('data.json', 'r') as f:
        data = json.load(f)

    print("you have", save['player_miners'], "miners")
    buyminers = input("""
                  Do you want to buy a miner?
                  1. Yes
                  2. No
                  """)
    
    if buyminers == "1":
    
        if save['player_gold'] < data['miner_cost']:
            print("You don't have enough gold to buy a miner.")
        else:
            save['player_gold'] -= data['miner_cost']
            save['player_miners'] += 1
            print("You have bought a miner.")
            print("You now have", save['player_miners'], "miners.")

        with open('save.json', 'w') as f:
            json.dump(save, f, indent=4)
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

############################################################################################################
###################### CPU Function #####################################################################
def cpu():
    with open('save.json', 'r') as f:
        save = json.load(f)
    with open('data.json', 'r') as f:
        data = json.load(f)
    

    if save['player'] == "usa":

        save['cpu1'] = "mexico"
        save['cpu1_gold'] = data['mexico_gold']
        save['cpu1_miners'] = data['mexico_miners']
        save['cpu1_firepower'] = data['mexico_firepower']
        
        save['cpu2'] = "canada"
        save['cpu2_gold'] = data['canada_gold']
        save['cpu2_miners'] = data['canada_miners']
        save['cpu2_firepower'] = data['canada_firepower']

##############################################################
    elif save['player'] == "canada":

        save['cpu1'] = "mexico"
        save['cpu1_gold'] = data['mexico_gold']
        save['cpu1_miners'] = data['mexico_miners']
        save['cpu1_firepower'] = data['mexico_firepower']

        save['cpu2'] = "usa"
        save['cpu2_gold'] = data['usa_gold']
        save['cpu2_miners'] = data['usa_miners']
        save['cpu2_firepower'] = data['usa_firepower']

##############################################################
    elif save['player'] == "mexico":
        save['cpu1'] = "canada"
        save['cpu1_gold'] = data['canada_gold']
        save['cpu1_miners'] = data['canada_miners']
        save['cpu1_firepower'] = data['canada_firepower']

        save['cpu2'] = "usa"
        save['cpu2_gold'] = data['usa_gold']
        save['cpu2_miners'] = data['usa_miners']
        save['cpu2_firepower'] = data['usa_firepower']

##############################################################
    with open('save.json', 'w') as f:
        json.dump(save, f, indent=4)
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
                  
############################################################################################################
###################### Attack Function ###################################################################
def attack():
    with open('save.json', 'r') as f:
        save = json.load(f)
    with open('data.json', 'r') as f:
        data = json.load(f)

    choice = input(f"""
                    Who do you want to attack?
                    1. {save['cpu1']}
                    2. {save['cpu2']}
                    3. Exit
                    """)
    

    if choice == "1":
            attack_power = random.randint(save['player_firepower']// 4, save['player_firepower']// 2)
            save['player_firepower'] -= attack_power
            save['cpu1_firepower'] -= attack_power
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            art.rising()
            art.falling()
            print("You attacked", save['cpu1'], "with", attack_power, "firepower!")

            if save['cpu1_firepower'] < 0:
                print(save['cpu1'], "has been defeated!")


            if save['player_firepower'] == 0:
                print("You don't have enough firepower to attack", save['cpu1'])

    elif choice == "2":
            attack_power = random.randint(save['player_firepower']// 4, save['player_firepower']// 2)
            save['player_firepower'] -= attack_power
            save['cpu2_firepower'] -= attack_power
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            art.rising()
            art.falling()
            print("You attacked", save['cpu2'], "with", attack_power, "firepower!")

            if save['cpu2_firepower'] < 0:
                print(save['cpu2'], "has been defeated!")

            if save['player_firepower'] == 0:
                print("You don't have enough firepower to attack", save['cpu2'])

    elif choice == "3":
        pass

    else:
        print("Invalid choice.")
        attack()

############################################################################################################
###################### AI Function #######################################################################
def ai(action):
    with open('save.json', 'r') as f:
        save = json.load(f)
    with open('data.json', 'r') as f:
        data = json.load(f)

    if save['cpu1_gold'] < 5000:
        c = 0.1
        if random.random() < c:
            if save['cpu1_gold'] < data['rifles_cost']:
                if action == "debug":
                    print("cpu1 doesn't have enough gold to buy a miner.")
                    pass
            else:
                save['cpu1_gold'] -= data['rifles_cost']
                save['cpu1_firepower'] += data['rifles']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print("cpu1 has bought rifles.")

##############################################################
##############################################################

    if save['cpu1_gold'] > 4000 and save['cpu1_gold'] < 8000:
        c = random.uniform(0.2, 0.3)
        if random.random() < c:
            if save['cpu1_gold'] < data['miner_cost']:
                if action == "debug":
                    print("cpu1 doesn't have enough gold to buy a miner.")
                pass
            else:
                save['cpu1_gold'] -= data['miner_cost']
                save['cpu1_miners'] += 1
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print("cpu1 has bought a miner.")

        if save['cpu1_firepower'] < 1000:
            c = 1
        elif save['cpu1_firepower'] < 3000:
            c = 0.9
        else:
            c = random.uniform(0.2, 0.3)

        if random.random() < c:
            if save['cpu1_gold'] < data['tanks_cost']:
                if action == "debug":
                    print("cpu1 doesn't have enough gold to research tanks.")
                pass
            else:
                save['cpu1_gold'] -= data['tanks_cost']
                save['cpu1_firepower'] += data['tanks']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print("cpu1 has researched tanks.")
        
        if save['cpu1_firepower'] < 1000:
            c = 1
        elif save['cpu1_firepower'] < 3000:
            c = 0.9
        else:
            c = random.uniform(0.2, 0.3)

        if random.random() < c:
            research_options = ['rifles', 'machineguns', 'grenades', 'rockets', 'transport_vehicles', 'handguns', 'snipers', 'basic_armor']
            research_choice = random.choice(research_options)

            if save['cpu1_gold'] < data[f'{research_choice}_cost']:
                if action == "debug":
                    print(f"cpu1 doesn't have enough gold to research {research_choice}.")
            else:
                save['cpu1_gold'] -= data[f'{research_choice}_cost']
                save['cpu1_firepower'] += data[f'{research_choice}']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print(f"cpu1 has researched {research_choice}.")
        
##############################################################
##############################################################

    if save['cpu1_gold'] > 10000 and save['cpu1_miners'] < 10:
        c = random.uniform(0.4, 0.8)
        if random.random() < c:
            if save['cpu1_gold'] < data['miner_cost']:
                if action == "debug":
                    print("cpu1 doesn't have enough gold to buy a miner.")
                pass
            else:
                save['cpu1_gold'] -= data['miner_cost']
                save['cpu1_miners'] += 1
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print("cpu1 has bought a miner2222.")
    
 ###############################################################
 ###############################################################

    if save['cpu1_gold'] > 10000 and save['cpu1_gold'] < 15000:
        if save['cpu1_firepower'] < 1000:
            c = 1
        elif save['cpu1_firepower'] < 3000:
            c = 0.9
        else:
            c = random.uniform(0.4, 0.8)
        if random.random() < c:
            research_options = ['rifles', 'machineguns', 'grenades', 'rockets', 'knives', 'grenade_launchers', 'snipers', 'med_armor', 'advanced_armor', 'helicopters', 'drones', 'submarines', 'frigates', 'patrol_boats']
            research_choice = random.choice(research_options)

            if save['cpu1_gold'] < data[f'{research_choice}_cost']:
                if action == "debug":
                    print(f"cpu1 doesn't have enough gold to research {research_choice}.")
            else:
                save['cpu1_gold'] -= data[f'{research_choice}_cost']
                save['cpu1_firepower'] += data[f'{research_choice}']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print(f"cpu1 has researched {research_choice}.")

##############################################################
##############################################################

    if save['cpu1_gold'] > 12000 and save['cpu1_gold'] < 20000:
        research_options = ['tanks', 'mortars', 'basic_armor']
        research_choice = random.choice(research_options)

        if save['cpu1_gold'] < data[f'{research_choice}_cost']:
            if action == "debug":
                print(f"cpu1 doesn't have enough gold to research {research_choice}.")
        else:
            save['cpu1_gold'] -= data[f'{research_choice}_cost']
            save['cpu1_firepower'] += data[f'{research_choice}']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            if action == "debug":
                print(f"cpu1 has researched {research_choice}.")

##############################################################
##############################################################

    if save['cpu1_gold'] > 20000 and save['cpu1_gold'] < 80000:

        if save['cpu1_firepower'] < 1000:
            c = 1
        elif save['cpu1_firepower'] < 3000:
            c = 0.9
        else:
            c = random.uniform(0.2, 0.8)
        if random.random() < c:
            research_options = ['artillery', 'snipers', 'med_armor', 'advanced_armor', 'helicopters', 'drones', 'submarines', 'frigates', 'patrol_boats']
            research_choice = random.choice(research_options)

            if save['cpu1_gold'] < data[f'{research_choice}_cost']:
                if action == "debug":
                    print(f"cpu1 doesn't have enough gold to research {research_choice}.")
            else:
                save['cpu1_gold'] -= data[f'{research_choice}_cost']
                save['cpu1_firepower'] += data[f'{research_choice}']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print(f"cpu1 has researched {research_choice}.")
    
##############################################################
##############################################################

    if save['cpu1_gold'] > 80000 and save['cpu1_gold'] < 250000:
        research_options = ['jets', 'bombers', 'missiles', 'aircraft_carriers', 'destroyers']
        research_choice = random.choice(research_options)

        if save['cpu1_gold'] < data[f'{research_choice}_cost']:
            if action == "debug":
                print(f"cpu1 doesn't have enough gold to research {research_choice}.")
        else:
            save['cpu1_gold'] -= data[f'{research_choice}_cost']
            save['cpu1_firepower'] += data[f'{research_choice}']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            if action == "debug":
                print(f"cpu1 has researched {research_choice}.")

##############################################################
##############################################################

    if save['cpu1_gold'] > 250000 and save['cpu1_gold'] < 1000000:
        research_options = ['aircraft_carriers', 'destroyers']
        research_choice = random.choice(research_options)

        if save['cpu1_gold'] < data[f'{research_choice}_cost']:
            if action == "debug":
                print(f"cpu1 doesn't have enough gold to research {research_choice}.")
        else:
            save['cpu1_gold'] -= data[f'{research_choice}_cost']
            save['cpu1_firepower'] += data[f'{research_choice}']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            if action == "debug":
                print(f"cpu1 has researched {research_choice}.")

##############################################################
##############################################################

    if save['cpu1_gold'] > 1000000:
        if save['cpu1_gold'] < data['nuclear_weapons_cost']:
            if action == "debug":
                print("cpu1 doesn't have enough gold to research tanks.")
            pass
        else:
            save['cpu1_gold'] -= data['nuclear_weapons_cost']
            save['cpu1_firepower'] += data['nuclear_weapons']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            if action == "debug":
                print("cpu1 has researched nuclear weapons.")

##############################################################
##############################################################
##############################################################
##############################################################

    if save['cpu2_gold'] < 5000:
        if save['cpu2_firepower'] < 3000:
            c = 1
        elif save['cpu2_firepower'] < 5000:
            c = 0.9
        else:
            c = random.uniform(0.2, 0.3)
        if random.random() < c:
            if save['cpu2_gold'] < data['rifles_cost']:
                if action == "debug":
                    print("cpu2 doesn't have enough gold to buy a miner.")
                    pass
            else:
                save['cpu2_gold'] -= data['rifles_cost']
                save['cpu2_firepower'] += data['rifles']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print("cpu2 has bought rifles.")

    ##############################################################
    ##############################################################

    if save['cpu2_gold'] > 4000 and save['cpu2_gold'] < 8000:
        if save['cpu2_firepower'] < 3000:
            c = 1
        elif save['cpu2_firepower'] < 5000:
            c = 0.9
        else:
            c = random.uniform(0.2, 0.3)
        if random.random() < c:
            if save['cpu2_gold'] < data['miner_cost']:
                if action == "debug":
                    print("cpu2 doesn't have enough gold to buy a miner.")
                pass
            else:
                save['cpu2_gold'] -= data['miner_cost']
                save['cpu2_miners'] += 1
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print("cpu2 has bought a miner.")

        if save['cpu2_firepower'] < 3000:
            c = 1
        elif save['cpu2_firepower'] < 5000:
            c = 0.9
        else:
            c = random.uniform(0.2, 0.3)

        if random.random() < c:
            if save['cpu2_gold'] < data['tanks_cost']:
                if action == "debug":
                    print("cpu2 doesn't have enough gold to research tanks.")
                pass
            else:
                save['cpu2_gold'] -= data['tanks_cost']
                save['cpu2_firepower'] += data['tanks']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print("cpu2 has researched tanks.")
        
        if save['cpu2_firepower'] < 3000:
            c = 1
        elif save['cpu2_firepower'] < 5000:
            c = 0.9
        else:
            c = random.uniform(0.2, 0.3)

        if random.random() < c:
            research_options = ['rifles', 'machineguns', 'grenades', 'rockets', 'transport_vehicles', 'handguns', 'snipers', 'basic_armor']
            research_choice = random.choice(research_options)

            if save['cpu2_gold'] < data[f'{research_choice}_cost']:
                if action == "debug":
                    print(f"cpu2 doesn't have enough gold to research {research_choice}.")
            else:
                save['cpu2_gold'] -= data[f'{research_choice}_cost']
                save['cpu2_firepower'] += data[f'{research_choice}']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print(f"cpu2 has researched {research_choice}.")
        
    ##############################################################
    ##############################################################

    if save['cpu2_gold'] > 10000 and save['cpu2_miners'] < 10:
        c = random.uniform(0.4, 0.8)
        if random.random() < c:
            if save['cpu2_gold'] < data['miner_cost']:
                if action == "debug":
                    print("cpu2 doesn't have enough gold to buy a miner.")
                pass
            else:
                save['cpu2_gold'] -= data['miner_cost']
                save['cpu2_miners'] += 1
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print("cpu2 has bought a miner.")

    ###############################################################
    ###############################################################

    if save['cpu2_gold'] > 10000 and save['cpu2_gold'] < 15000:
        if save['cpu2_firepower'] < 3000:
            c = 1
        elif save['cpu2_firepower'] < 5000:
            c = 0.9
        else:
            c = random.uniform(0.4, 0.8)
        if random.random() < c:
            research_options = ['rifles', 'machineguns', 'grenades', 'rockets', 'knives', 'grenade_launchers', 'snipers', 'med_armor', 'advanced_armor', 'helicopters', 'drones', 'submarines', 'frigates', 'patrol_boats']
            research_choice = random.choice(research_options)

            if save['cpu2_gold'] < data[f'{research_choice}_cost']:
                if action == "debug":
                    print(f"cpu2 doesn't have enough gold to research {research_choice}.")
            else:
                save['cpu2_gold'] -= data[f'{research_choice}_cost']
                save['cpu2_firepower'] += data[f'{research_choice}']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print(f"cpu2 has researched {research_choice}.")

    ##############################################################
    ##############################################################

    if save['cpu2_gold'] > 12000 and save['cpu2_gold'] < 20000:
        research_options = ['tanks', 'mortars', 'basic_armor']
        research_choice = random.choice(research_options)

        if save['cpu2_gold'] < data[f'{research_choice}_cost']:
            if action == "debug":
                print(f"cpu2 doesn't have enough gold to research {research_choice}.")
        else:
            save['cpu2_gold'] -= data[f'{research_choice}_cost']
            save['cpu2_firepower'] += data[f'{research_choice}']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            if action == "debug":
                print(f"cpu2 has researched {research_choice}.")

    ##############################################################
    ##############################################################

    if save['cpu2_gold'] > 20000 and save['cpu2_gold'] < 80000:
        if save['cpu2_firepower'] < 3000:
            c = 1
        elif save['cpu2_firepower'] < 5000:
            c = 0.9
        else:
            c = random.uniform(0.5, 0.9)
        if random.random() < c:
            research_options = ['artillery', 'snipers', 'med_armor', 'advanced_armor', 'helicopters', 'drones', 'submarines', 'frigates', 'patrol_boats']
            research_choice = random.choice(research_options)

            if save['cpu2_gold'] < data[f'{research_choice}_cost']:
                if action == "debug":
                    print(f"cpu2 doesn't have enough gold to research {research_choice}.")
            else:
                save['cpu2_gold'] -= data[f'{research_choice}_cost']
                save['cpu2_firepower'] += data[f'{research_choice}']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print(f"cpu2 has researched {research_choice}.")

    ##############################################################
    ##############################################################

    if save['cpu2_gold'] > 80000 and save['cpu2_gold'] < 250000:
        research_options = ['jets', 'bombers', 'missiles', 'aircraft_carriers', 'destroyers']
        research_choice = random.choice(research_options)

        if save['cpu2_gold'] < data[f'{research_choice}_cost']:
            if action == "debug":
                print(f"cpu2 doesn't have enough gold to research {research_choice}.")
        else:
            save['cpu2_gold'] -= data[f'{research_choice}_cost']
            save['cpu2_firepower'] += data[f'{research_choice}']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            if action == "debug":
                print(f"cpu2 has researched {research_choice}.")

    ##############################################################
    ##############################################################

    if save['cpu2_gold'] > 250000 and save['cpu2_gold'] < 1000000:
        research_options = ['aircraft_carriers', 'destroyers']
        research_choice = random.choice(research_options)

        if save['cpu2_gold'] < data[f'{research_choice}_cost']:
            if action == "debug":
                print(f"cpu2 doesn't have enough gold to research {research_choice}.")
        else:
            save['cpu2_gold'] -= data[f'{research_choice}_cost']
            save['cpu2_firepower'] += data[f'{research_choice}']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            if action == "debug":
                print(f"cpu2 has researched {research_choice}.")

    ##############################################################
    ##############################################################

    if save['cpu2_gold'] > 1000000:
        if save['cpu2_gold'] < data['nuclear_weapons_cost']:
            if action == "debug":
                print("cpu2 doesn't have enough gold to research tanks.")
            pass
        else:
            save['cpu2_gold'] -= data['nuclear_weapons_cost']
            save['cpu2_firepower'] += data['nuclear_weapons']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            if action == "debug":
                print("cpu2 has researched nuclear weapons.")
    

    ##############################################################
    ##############################################################

    if save['turn'] > 3:
        c = random.uniform(0.1, 0.3)
        if random.random() < c:
            if save['cpu1_firepower'] >= save['player_firepower']:
                attack_power = random.randint(save['cpu1_firepower']// 4, save['cpu1_firepower']// 2)
                save['cpu1_firepower'] -= attack_power
                save['player_firepower'] -= attack_power
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print(save['cpu1'], f"attacked you with {attack_power} firepower!")

        ##############################################################

        if save['cpu1_firepower'] >= save['cpu2_firepower']:
            if save['cpu2_firepower'] > 0:
                c = random.uniform(0.1, 0.3)
                if random.random() < c:
                    if save['cpu2_firepower'] > 0:
                        attack_power = random.randint(save['cpu1_firepower']// 4, save['cpu1_firepower']// 2)
                        save['cpu1_firepower'] -= attack_power
                        save['cpu2_firepower'] -= attack_power
                        with open('save.json', 'w') as f:
                            json.dump(save, f, indent=4)
                        print(save['cpu1'], "attacked", save['cpu2'], "with", attack_power, "firepower!")

                        if save['cpu2_firepower'] < 0:
                            print(save['cpu2'], "has been defeated!")
            
        ##############################################################
        if save['cpu2_firepower'] >= save['player_firepower']:
            c = random.uniform(0.1, 0.3)
            if random.random() < c:
                attack_power = random.randint(save['cpu2_firepower']// 5, save['cpu2_firepower']// 2)
                save['cpu2_firepower'] -= attack_power
                save['player_firepower'] -= attack_power
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print(save['cpu2'], f"attacked you with {attack_power} firepower!")

        ##############################################################
        if save['cpu2_firepower'] >= save['cpu1_firepower']:
            if save['cpu1_firepower'] > 0:
                c = random.uniform(0.1, 0.3)
                if random.random() < c:
                    if save['cpu1_firepower'] > 0:
                        attack_power = random.randint(save['cpu2_firepower']// 5, save['cpu2_firepower']// 2)
                        save['cpu2_firepower'] -= attack_power
                        save['cpu1_firepower'] -= attack_power
                        with open('save.json', 'w') as f:
                            json.dump(save, f, indent=4)
                        print(save['cpu2'], "attacked", save['cpu1'], "with", attack_power, "firepower!")

                        if save['cpu1_firepower'] < 0:
                            print(save['cpu1'], "has been defeated!")


        ##############################################################
    if save['player_firepower'] < 0:
        print("You have been defeated!")
        with open('save.json', 'w') as f:
            f.write('{"save": "false"}')
        print("press enter to exit")
        input()
        clear_console()
        exit()

    if save['cpu1_firepower'] < 0:
        save['cpu1_gold'] = -1
        save['cpu1_miners'] = -1
        save['cpu1_firepower'] = -1
        with open('save.json', 'w') as f:
            json.dump(save, f, indent=4)
    
    if save['cpu2_firepower'] < 0:
        save['cpu2_gold'] = -1
        save['cpu2_miners'] = -1
        save['cpu2_firepower'] = -1
        with open('save.json', 'w') as f:
            json.dump(save, f, indent=4)

        ##############################################################
    if save['cpu1_firepower'] < 0 and save['cpu2_firepower'] < 0:
        print("Congratulations! You have defeated all countries!")
        print("You are the ultimate conqueror!")
        print("You are the champion of north america!")
        print("You win!")
        print("Press enter to exit and celebrate your victory!")
        print("(cheat code: uwu)")
        input()
        with open('save.json', 'w') as f:
            f.write('{"save": "false"}')
        clear_console()
        exit()
        
############# US Anthem ################
def us_anthem():
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

############# Canada Anthem ################
def can_anthem():
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

############# Mexico Anthem ################
def mx_anthem():
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
    clear_console()
    print("¡Viva México!")
    time.sleep(1)
    print("You have chosen to play as Mexico!")
    print("Prepare for an epic conquest!")
    time.sleep(2)
