import json

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
            if data['rifles_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['rifles_cost']
                save['player_firepower'] += data['rifles']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print("You have researched rifles")


#####################################################################                       2
        elif groundmenu == "2":
            if data['machineguns_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['machineguns_cost']
                save['player_firepower'] += data['machineguns']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print("You have researched machine guns")


#####################################################################                       3
        elif groundmenu == "3":
            if data['grenades_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['grenades_cost']
                save['player_firepower'] += data['grenades']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print("You have researched grenades")


#####################################################################                       4
        elif groundmenu == "4":
            if data['rockets_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['rockets_cost']
                save['player_firepower'] += data['rockets']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print("You have researched rockets")
            

#####################################################################                       5
        elif groundmenu == "5":
            if data['tanks_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['tanks_cost']
                save['player_firepower'] += data['tanks']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print("You have researched tanks")


#####################################################################                       6
        elif groundmenu == "6":
            if data['transport_vehicles_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['transport_vehicles_cost']
                save['player_firepower'] += data['transport_vehicles']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print("You have researched transport vehicles")


#####################################################################                       7
        elif groundmenu == "7":
            if data['handguns_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['handguns_cost']
                save['player_firepower'] += data['handguns']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print("You have researched handguns")


#####################################################################                       8
        elif groundmenu == "8":
            if data['knives_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['knives_cost']
                save['player_firepower'] += data['knives']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print("You have researched knives")


#####################################################################                       9
        elif groundmenu == "9":
            if data['grenade_launchers_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['grenade_launchers_cost']
                save['player_firepower'] += data['grenade_launchers']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print("You have researched grenade launchers")


#####################################################################                       10
        elif groundmenu == "10":
            if data['mortars_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['mortars_cost']
                save['player_firepower'] += data['mortars']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print("You have researched mortars")


#####################################################################                       11
        elif groundmenu == "11":
            if data['artillery_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['artillery_cost']
                save['player_firepower'] += data['artillery']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print("You have researched artillery")


#####################################################################                       12
        elif groundmenu == "12":
            if data['snipers_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['snipers_cost']
                save['player_firepower'] += data['snipers']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print("You have researched snipers")


#####################################################################                       13
        elif groundmenu == "13":
            if data['basic_armor_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['basic_armor_cost']
                save['player_firepower'] += data['basic_armor']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print("You have researched basic armor")


#####################################################################                       14
        elif groundmenu == "14":
            if data['med_armor_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['med_armor_cost']
                save['player_firepower'] += data['med_armor']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print("You have researched medium armor")


#####################################################################                       15
        elif groundmenu == "15":
            if data['advanced_armor_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['advanced_armor_cost']
                save['player_firepower'] += data['advanced_armor']
                with open('save.json', 'w') as f:
                    json.dump(save, f, indent=4)
                print("You have researched advanced armor")


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
                if data['jets_cost'] > save['player_gold']:
                    print("You do not have enough gold")
                else:
                    save['player_gold'] -= data['jets_cost']
                    save['player_firepower'] += data['jets']
                    with open('save.json', 'w') as f:
                        json.dump(save, f, indent=4)
                    print("You have researched jets")


#################################################################                    2
            elif airmenu == "2":
                if data['bombers_cost'] > save['player_gold']:
                    print("You do not have enough gold")
                else:
                    save['player_gold'] -= data['bombers_cost']
                    save['player_firepower'] += data['bombers']
                    with open('save.json', 'w') as f:
                        json.dump(save, f, indent=4)
                    print("You have researched bombers")


#################################################################                   3

            elif airmenu == "3":
                if data['missiles_cost'] > save['player_gold']:
                    print("You do not have enough gold")
                else:
                    save['player_gold'] -= data['missiles_cost']
                    save['player_firepower'] += data['missiles']
                    with open('save.json', 'w') as f:
                        json.dump(save, f, indent=4)
                    print("You have researched missiles")


#################################################################                   4

            elif airmenu == "4":
                if data['helicopters_cost'] > save['player_gold']:
                    print("You do not have enough gold")
                else:
                    save['player_gold'] -= data['helicopters_cost']
                    save['player_firepower'] += data['helicopters']
                    with open('save.json', 'w') as f:
                        json.dump(save, f, indent=4)
                    print("You have researched helicopters")


#################################################################                   5

            elif airmenu == "5":
                if data['drones_cost'] > save['player_gold']:
                    print("You do not have enough gold")
                else:
                    save['player_gold'] -= data['drones_cost']
                    save['player_firepower'] += data['drones']
                    with open('save.json', 'w') as f:
                        json.dump(save, f, indent=4)
                    print("You have researched drones")


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
            if data['submarines_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['submarines_cost']
                save['player_firepower'] += data['submarines']
                with open('save.json', 'w') as f:
                    json.dump(save, f)
                print("You have researched submarines")



#################################################################                            2
        elif seamenu == "2":
            if data['aircraft_carriers_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['aircraft_carriers_cost']
                save['player_firepower'] += data['aircraft_carriers']
                with open('save.json', 'w') as f:
                    json.dump(save, f)
                print("You have researched aircraft carriers")


#################################################################                           3

        elif seamenu == "3":
            if data['destroyers_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['destroyers_cost']
                save['player_firepower'] += data['destroyers']
                with open('save.json', 'w') as f:
                    json.dump(save, f)
                print("You have researched destroyers")


#################################################################                           4

        elif seamenu == "4":
            if data['frigates_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['frigates_cost']
                save['player_firepower'] += data['frigates']
                with open('save.json', 'w') as f:
                    json.dump(save, f)
                print("You have researched frigates")


#################################################################                           5

        elif seamenu == "5":
            if data['patrol_boats_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['patrol_boats_cost']
                save['player_firepower'] += data['patrol_boats']
                with open('save.json', 'w') as f:
                    json.dump(save, f)
                print("You have researched patrol boats")


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
            if data['nuclear_weapons_cost'] > save['player_gold']:
                print("You do not have enough gold")
            else:
                save['player_gold'] -= data['nuclear_weapons_cost']
                save['player_firepower'] += data['nuclear_weapons']
                with open('save.json', 'w') as f:
                    json.dump(save, f)
                print("You have researched nuclear weapons")


#################################################################
    else:
        print("Invalid choice")


