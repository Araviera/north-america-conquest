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
def atk(cpu, save):
            attack_power = random.randint(save['player_firepower']// 4, save['player_firepower']// 2)
            cpuf = cpu + '_firepower'
            save['player_firepower'] -= attack_power
            save[cpuf] -= attack_power
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            if save['nuke'] == "True":
                art.rising()
                art.falling()
            print("You attacked", save[cpu], "with", attack_power, "firepower!")

            if save[cpuf] < 0:
                print(save[cpu], "has been defeated!")


            if save['player_firepower'] == 0:
                print(f"You don't have enough firepower to attack", {cpu})

def cpu_assign(cpu, name, save, data):
    save[cpu] = name
    save[cpu + '_gold'] = data[name + '_gold']
    save[cpu + '_miners'] = data[name + '_miners']
    save[cpu + '_firepower'] = data[name + '_firepower']
############################################################################################################
def cpu():
    with open('save.json', 'r') as f:
        save = json.load(f)
    with open('data.json', 'r') as f:
        data = json.load(f)
    

    if save['player'] == "usa":

        cpu_assign('cpu1', 'canada', save, data)
        cpu_assign('cpu2', 'mexico', save, data)
        cpu_assign('cpu3', 'uk', save, data)
        cpu_assign('cpu4', 'france', save, data)
        cpu_assign('cpu5', 'russia', save, data)
        cpu_assign('cpu6', 'china', save, data)
        cpu_assign('cpu7', 'germany', save, data)

    if save['player'] == "canada":
            
        cpu_assign('cpu1', 'usa', save, data)
        cpu_assign('cpu2', 'mexico', save, data)
        cpu_assign('cpu3', 'uk', save, data)
        cpu_assign('cpu4', 'france', save, data)
        cpu_assign('cpu5', 'russia', save, data)
        cpu_assign('cpu6', 'china', save, data)
        cpu_assign('cpu7', 'germany', save, data)



##############################################################
    elif save['player'] == "mexico":
                
            cpu_assign('cpu1', 'usa', save, data)
            cpu_assign('cpu2', 'canada', save, data)
            cpu_assign('cpu3', 'uk', save, data)
            cpu_assign('cpu4', 'france', save, data)
            cpu_assign('cpu5', 'russia', save, data)
            cpu_assign('cpu6', 'china', save, data)
            cpu_assign('cpu7', 'germany', save, data)
            


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
                    3. {save['cpu3']}
                    4. {save['cpu4']}
                    5. {save['cpu5']}
                    6. {save['cpu6']}
                    7. {save['cpu7']}
                    8. Exit
                    """)
    

    if choice == "1":
            atk("cpu1", save)

    elif choice == "2":
            atk("cpu2", save)
    
    elif choice == "3":
            atk("cpu3", save)

    elif choice == "4":
            atk("cpu4", save)

    elif choice == "5":
            atk("cpu5", save)

    elif choice == "6":
            atk("cpu6", save)

    elif choice == "7":
            atk("cpu7", save)

    elif choice == "8":
        pass

    else:
        print("Invalid choice.")
        attack()

############################################################################################################

def ai_research_logic(cpu, action, save, data):
    if save[cpu + '_gold'] < 5000:
        c = 0.1
        if random.random() < c:
            if save[cpu +'_gold'] < data['rifles_cost']:
                if action == "debug":
                    print(cpu, " doesn't have enough gold to buy a miner.")
                    pass
            else:
                save[cpu + '_gold'] -= data['rifles_cost']
                save[cpu + '_firepower'] += data['rifles']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print(cpu, "has bought rifles.")

##############################################################
##############################################################

    if save[cpu + '_gold'] > 4000 and save[cpu + '_gold'] < 8000:
        c = random.uniform(0.2, 0.3)
        if random.random() < c:
            if save[cpu + '_gold'] < data['miner_cost']:
                if action == "debug":
                    print(cpu, " doesn't have enough gold to buy a miner.")
                pass
            else:
                save[cpu + '_gold'] -= data['miner_cost']
                save[cpu + '_miners'] += 1
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print(cpu, "has bought a miner.")

        if save[cpu + '_firepower'] < 1000:
            c = 1
        elif save[cpu + '_firepower'] < 3000:
            c = 0.9
        else:
            c = random.uniform(0.2, 0.3)

        if random.random() < c:
            if save[cpu + '_gold'] < data['tanks_cost']:
                if action == "debug":
                    print(cpu + " doesn't have enough gold to research tanks.")
                pass
            else:
                save[cpu + '_gold'] -= data['tanks_cost']
                save[cpu + '_firepower'] += data['tanks']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print(cpu, "has researched tanks.")
        
        if save[cpu + '_firepower'] < 1000:
            c = 1
        elif save[cpu + '_firepower'] < 3000:
            c = 0.9
        else:
            c = random.uniform(0.2, 0.3)

        if random.random() < c:
            research_options = ['rifles', 'machineguns', 'grenades', 'rockets', 'transport_vehicles', 'handguns', 'snipers', 'basic_armor']
            research_choice = random.choice(research_options)

            if save[cpu + '_gold'] < data[f'{research_choice}_cost']:
                if action == "debug":
                    print(f"{cpu} doesn't have enough gold to research {research_choice}.")
            else:
                save[cpu + '_gold'] -= data[f'{research_choice}_cost']
                save[cpu + '_firepower'] += data[f'{research_choice}']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print(f"{cpu} has researched {research_choice}.")
##############################################################
##############################################################
    if save[cpu + '_gold'] > 10000 and save[cpu + '_miners'] < 10:
        c = random.uniform(0.4, 0.8)
        if random.random() < c:
            if save[cpu + '_gold'] < data['miner_cost']:
                if action == "debug":
                    print(cpu, "doesn't have enough gold to buy a miner.")
                pass
            else:
                save[cpu + '_gold'] -= data['miner_cost']
                save[cpu + '_miners'] += 1
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print(cpu, "has bought a miner2222.")
 ###############################################################
 ###############################################################

    if save[cpu + '_gold'] > 10000 and save[cpu + '_gold'] < 15000:
        if save[cpu + '_firepower'] < 1000:
            c = 1
        elif save[cpu + '_firepower'] < 3000:
            c = 0.9
        else:
            c = random.uniform(0.4, 0.8)
        if random.random() < c:
            research_options = ['rifles', 'machineguns', 'grenades', 'rockets', 'knives', 'grenade_launchers', 'snipers', 'med_armor', 'advanced_armor', 'helicopters', 'drones', 'submarines', 'frigates', 'patrol_boats']
            research_choice = random.choice(research_options)

            if save[cpu + '_gold'] < data[f'{research_choice}_cost']:
                if action == "debug":
                    print(f"{cpu} doesn't have enough gold to research {research_choice}.")
            else:
                save[cpu + '_gold'] -= data[f'{research_choice}_cost']
                save[cpu + '_firepower'] += data[f'{research_choice}']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print(f"{cpu} has researched {research_choice}.")

##############################################################
##############################################################

    if save[cpu + '_gold'] > 12000 and save[cpu + '_gold'] < 20000:
        research_options = ['tanks', 'mortars', 'basic_armor']
        research_choice = random.choice(research_options)

        if save[cpu + '_gold'] < data[f'{research_choice}_cost']:
            if action == "debug":
                print(f"{cpu} doesn't have enough gold to research {research_choice}.")
        else:
            save[cpu + '_gold'] -= data[f'{research_choice}_cost']
            save[cpu + '_firepower'] += data[f'{research_choice}']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            if action == "debug":
                print(f"{cpu} has researched {research_choice}.")

##############################################################
##############################################################
    if save[cpu + '_gold'] > 20000 and save[cpu + '_gold'] < 80000:

        if save[cpu + '_firepower'] < 1000:
            c = 1
        elif save[cpu + '_firepower'] < 3000:
            c = 0.9
        else:
            c = random.uniform(0.2, 0.8)
        if random.random() < c:
            research_options = ['artillery', 'snipers', 'med_armor', 'advanced_armor', 'helicopters', 'drones', 'submarines', 'frigates', 'patrol_boats']
            research_choice = random.choice(research_options)

            if save[cpu + '_gold'] < data[f'{research_choice}_cost']:
                if action == "debug":
                    print(f"{cpu} doesn't have enough gold to research {research_choice}.")
            else:
                save[cpu + '_gold'] -= data[f'{research_choice}_cost']
                save[cpu + '_firepower'] += data[f'{research_choice}']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                if action == "debug":
                    print(f"{cpu} has researched {research_choice}.")
##############################################################
##############################################################
    if save[cpu + '_gold'] > 80000 and save[cpu + '_gold'] < 250000:
        research_options = ['jets', 'bombers', 'missiles', 'aircraft_carriers', 'destroyers']
        research_choice = random.choice(research_options)

        if save[cpu + '_gold'] < data[f'{research_choice}_cost']:
            if action == "debug":
                print(f"{cpu} doesn't have enough gold to research {research_choice}.")
        else:
            save[cpu + '_gold'] -= data[f'{research_choice}_cost']
            save[cpu + '_firepower'] += data[f'{research_choice}']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            if action == "debug":
                print(f"{cpu} has researched {research_choice}.")

##############################################################
##############################################################

    if save[cpu + '_gold'] > 250000 and save[cpu + '_gold'] < 1000000:
        research_options = ['aircraft_carriers', 'destroyers']
        research_choice = random.choice(research_options)

        if save[cpu + '_gold'] < data[f'{research_choice}_cost']:
            if action == "debug":
                print(f"{cpu} doesn't have enough gold to research {research_choice}.")
        else:
            save[cpu + '_gold'] -= data[f'{research_choice}_cost']
            save[cpu + '_firepower'] += data[f'{research_choice}']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            if action == "debug":
                print(f"{cpu} has researched {research_choice}.")

##############################################################
##############################################################
    if save[cpu + '_gold'] > 1000000:
        if save[cpu + '_gold'] < data['nuclear_weapons_cost']:
            if action == "debug":
                print(cpu, "doesn't have enough gold to research tanks.")
            pass
        else:
            save[cpu + '_gold'] -= data['nuclear_weapons_cost']
            save[cpu + '_firepower'] += data['nuclear_weapons']
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            if action == "debug":
                print(cpu, "has researched nuclear weapons.")

##############################################################
def ai_attack_logic(cpu, cpu2, save):
    c = random.uniform(0.1, 0.3)
    if random.random() < c:
        if save[cpu + '_firepower'] >= save['player_firepower']:
            attack_power = random.randint(save[cpu + '_firepower']// 4, save[cpu + '_firepower']// 2)
            save[cpu + '_firepower'] -= attack_power
            save['player_firepower'] -= attack_power
            with open('save.json', 'w') as f:
                json.dump(save, f, indent=4)
            print(save[cpu], f"attacked you with {attack_power} firepower!")

    ##############################################################

    if save[cpu + '_firepower'] >= save[cpu2 + '_firepower']:
        if save[cpu2 + '_firepower'] > 0:
            c = random.uniform(0.1, 0.3)
            if random.random() < c:
                if save[cpu2 + '_firepower'] > 0:
                    attack_power = random.randint(save[cpu + '_firepower']// 4, save[cpu + '_firepower']// 2)
                    save[cpu + '_firepower'] -= attack_power
                    save[cpu2 + '_firepower'] -= attack_power
                    with open('save.json', 'w') as f:
                        json.dump(save, f, indent=4)
                    print(save[cpu], "attacked", save[cpu2], "with", attack_power, "firepower!")

                    if save[cpu2 + '_firepower'] < 0:
                        print(save[cpu2], "has been defeated!")
        
############################################################################################################
###################### AI Function #######################################################################
def ai(action):
    with open('save.json', 'r') as f:
        save = json.load(f)
    with open('data.json', 'r') as f:
        data = json.load(f)
###############

    ai_research_logic('cpu1', action, save, data)
    ai_research_logic('cpu2', action, save, data)
    ai_research_logic('cpu3', action, save, data)
    ai_research_logic('cpu4', action, save, data)
    ai_research_logic('cpu5', action, save, data)
    ai_research_logic('cpu6', action, save, data)
    ai_research_logic('cpu7', action, save, data)

    ##############################################################
    ##############################################################

    if save['turn'] > 6:
        for cpu1 in range(1, 8):
            for cpu2 in range(1, 8):
                if cpu1 != cpu2:
                    ai_attack_logic(f'cpu{cpu1}', f'cpu{cpu2}', save)


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
    if save['cpu1_firepower'] < 0 and save['cpu2_firepower'] < 0 and save['cpu3_firepower'] < 0 and save['cpu4_firepower'] < 0 and save['cpu5_firepower'] < 0 and save['cpu6_firepower'] < 0 and save['cpu7_firepower'] < 0:
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
        
