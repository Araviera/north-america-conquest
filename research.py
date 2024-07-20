import json
def research(data, save, item):
    item_cost_key = item + '_cost'
    if data[item_cost_key] > save['player_gold']:
        print("You do not have enough gold")
    else:
        save['player_gold'] -= data[item_cost_key]
        save['player_firepower'] += data[item]
        with open('save.json', 'w') as f:
            json.dump(save, f, indent=4)
        print(f"You have researched {item}")

def researchmenu():
    with open ('data.json', 'r') as f:
        data = json.load(f)
    with open ('save.json', 'r') as f:
        save = json.load(f)



#####################################################################                       
    research_choice = input("""
    What would you like to research?
    1. Ground Firepower
    2. Air Firepower
    3. Sea Firepower
    4. Nuclear Weapons
    """)
        
#####################################################################                       #1#
    if research_choice == "1":
        groundmenu = input(f"""
        What would you like to research?
        1. Rifles ({data['rifles_cost']}g)
        2. Machine guns ({data['machineguns_cost']}g)
        3. Grenades ({data['grenades_cost']}g)
        4. Rockets ({data['rockets_cost']}g)
        5. Tanks ({data['tanks_cost']}g)
        6. Transport vehicles ({data['transport_vehicles_cost']}g)
        7. Handguns ({data['handguns_cost']}g)
        8. Knives ({data['knives_cost']}g)
        9. Grenade launchers ({data['grenade_launchers_cost']}g)
        10. Mortars ({data['mortars_cost']}g)
        11. Artillery ({data['artillery_cost']}g)
        12. Snipers ({data['snipers_cost']}g)
        13. Basic armor ({data['basic_armor_cost']}g)
        14. Medium armor ({data['med_armor_cost']}g)
        15. Advanced armor ({data['advanced_armor_cost']}g)
        """)

#####################################################################                       1
        if groundmenu == "1":
            research(data, save, 'rifles')


#####################################################################                       2
        elif groundmenu == "2":
            research(data, save, 'machineguns')

#####################################################################                       3
        elif groundmenu == "3":
            research(data, save, 'grenades')


#####################################################################                       4
        elif groundmenu == "4":
            research(data, save, 'rockets')
            

#####################################################################                       5
        elif groundmenu == "5":
            research(data, save, 'tanks')

#####################################################################                       6
        elif groundmenu == "6":
            research(data, save, 'transport_vehicles')


#####################################################################                       7
        elif groundmenu == "7":
            research(data, save, 'handguns')

#####################################################################                       8
        elif groundmenu == "8":
            research(data, save, 'knives')


#####################################################################                       9
        elif groundmenu == "9":
            research(data, save, 'grenade_launchers')


#####################################################################                       10
        elif groundmenu == "10":
            research(data, save, 'mortars')


#####################################################################                       11
        elif groundmenu == "11":
            research(data, save, 'artillery')


#####################################################################                       12
        elif groundmenu == "12":
            research(data, save, 'snipers')


#####################################################################                       13
        elif groundmenu == "13":
            research(data, save, 'basic_armor')


#####################################################################                       14
        elif groundmenu == "14":
            research(data, save, 'med_armor')


#####################################################################                       15
        elif groundmenu == "15":
            research(data, save, 'advanced_armor')


#####################################################################
        else:
            print("Invalid choice")



###############################################################################                       #2#
###############################################################################
###############################################################################
    elif research_choice == "2":
            airmenu = input(f"""
            What would you like to research?
            1. Jets ({data['jets_cost']}g)
            2. Bombers ({data['bombers_cost']}g)
            3. Missiles ({data['missiles_cost']}g)
            4. Helicopters ({data['helicopters_cost']}g)
            5. Drones ({data['drones_cost']}g)
            """)


#################################################################                   1
            if airmenu == "1":
                research(data, save, 'jets')


#################################################################                    2
            elif airmenu == "2":
                research(data, save, 'bombers')


#################################################################                   3

            elif airmenu == "3":
                research(data, save, 'missiles')


#################################################################                   4

            elif airmenu == "4":
                research(data, save, 'helicopters')


#################################################################                   5

            elif airmenu == "5":
                research(data, save, 'drones')

#################################################################                       6

            else:
                print("Invalid choice")
###############################################################################
###############################################################################
###############################################################################                       #3#

    elif research_choice == "3":
        seamenu = input(f"""
        What would you like to research?
        1. Submarines ({data['submarines_cost']}g)
        2. Aircraft Carriers ({data['aircraft_carriers_cost']}g)
        3. Destroyers ({data['destroyers_cost']}g)
        4. Frigates ({data['frigates_cost']}g)
        5. Patrol Boats ({data['patrol_boats_cost']}g)
        """)



#################################################################                           1

        if seamenu == "1":
            research(data, save, 'submarines')



#################################################################                            2
        elif seamenu == "2":
            research(data, save, 'aircraft_carriers')


#################################################################                           3

        elif seamenu == "3":
            research(data, save, 'destroyers')


#################################################################                           4

        elif seamenu == "4":
            research(data, save, 'frigates')


#################################################################                           5

        elif seamenu == "5":
            research(data, save, 'patrol_boats')


#################################################################

        else:
            print("Invalid choice")


###############################################################################
###############################################################################
###############################################################################                       #4#

    elif research_choice == "4":
        nuclearmenu = input(f"""
        What would you like to research?
        1. Nuclear Weapons ({data['nuclear_weapons_cost']}g)
        """)

#################################################################                           1
        if nuclearmenu == "1":
            research(data, save, 'nuclear_weapons')


#################################################################
    else:
        print("Invalid choice")


