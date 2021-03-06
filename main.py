import random

basic_roll_stats = None

#
#
#   FUNCTIONS
#
#
#Rolls four D6, removes the lowest and then
#adds numbers and returns total
def dice_roll():
    die_one = random.randint(1,6)
    die_two = random.randint(1,6) 
    die_three = random.randint(1,6)
    die_four =  random.randint(1,6)
   
    die_list = [die_one, die_two, die_three, die_four]
    sort = sorted(die_list, reverse = True)
    sorted_die_roll = sort
    sorted_die_roll.pop()
    total = sorted_die_roll[0] + sorted_die_roll[1] + sorted_die_roll[2]
    return total

#Takes five values from dice_roll and places them in a list
#Step 2
def points_roll():
    points = []
    for i in range(6):
        x = dice_roll()
        points.append(x)
    return points

#Adds modifers to ability scores
def roll_stats_modifiers(roll):
    roll_stats = roll

    for i in range(6):
        x = roll_stats[i]
        if x == 1:  
            mod_list = [x,-5] 
            roll_stats.pop(i)
            roll_stats.insert(i, mod_list)
        elif x == 2 or x == 3:
            mod_list = [x,-4] 
            roll_stats.pop(i)
            roll_stats.insert(i, mod_list)
        elif x == 4 or x == 5:
            mod_list = [x,-3]
            roll_stats.pop(i)
            roll_stats.insert(i, mod_list)
        elif x == 6 or x == 7:
            mod_list = [x,-2]
            roll_stats.pop(i)
            roll_stats.insert(i, mod_list)
        elif x == 8 or x == 9:
            mod_list = [x,-1]
            roll_stats.pop(i)
            roll_stats.insert(i, mod_list)
        elif x == 10 or x == 11:
            mod_list = [x,0]
            roll_stats.pop(i)
            roll_stats.insert(i, mod_list)
        elif x == 12 or x == 13:
            mod_list = [x,1]
            roll_stats.pop(i)
            roll_stats.insert(i, mod_list)
        elif x == 14 or x == 15:
            mod_list = [x,2]
            roll_stats.pop(i)
            roll_stats.insert(i, mod_list)
        elif x == 16 or x == 17:
            mod_list = [x,3]
            roll_stats.pop(i)
            roll_stats.insert(i, mod_list)
        elif x == 18 or x == 19:
            mod_list = [x,4]
            roll_stats.pop(i)
            roll_stats.insert(i, mod_list)
        elif x == 20:
            mod_list = [x,5]
            roll_stats.pop(i)
            roll_stats.insert(i, mod_list)
        else:
          print("Oops")
        
    return roll_stats

#Uses a while loop to ask user to asign abilities to the roll
#Controls for mispelling and trying to assign more than one number to an ability
def check_stats(roll, i, y, character_stats, abilities):
    

    while True:
        x = input(str(abilities) + " >>>")
        
        if x.lower() == "charisma" or x.lower() == "ch":
            if "Charisma" in abilities:
                character_stats["Charisma"]= roll[i]
                print("Charisma = "+ str(y))
                abilities.remove("Charisma")
                print(abilities)
                break
            else:
                print("You already assigned a value to Charisma")
        elif x.lower() == "constitution" or x.lower() == "co":
            if "Constitution" in abilities:
                character_stats["Constitution"]= roll[i]
                print("Constitution = "+ str(y))
                abilities.remove("Constitution")
                print(abilities)
                break
            else:
                print("You already assigned a value to Constitution.")
        elif x.lower() == "wisdom" or x.lower() == "w":
            if "Wisdom" in abilities:
                character_stats["Wisdom"]= roll[i]
                print("Wisdom = "+ str(y))
                abilities.remove("Wisdom")
                print(abilities)
                break
            else:
                print("You already assigned a value to Wisdom")

        elif x.lower() == "strength" or x.lower() == "s":
            if "Strength" in abilities:
                character_stats["Strength"]= roll[i]
                print("Strength = "+ str(y))
                abilities.remove("Strength")
                print(abilities)
                break
            else:
                print("You already assigned a value to Strength")
        elif x.lower() == "intelligence" or x.lower() == "i":
            if "Intelligence" in abilities:
                character_stats["Intelligence"]= roll[i]
                print("Intelligence = "+ str(y))
                abilities.remove("Intelligence")
                print(abilities)
                break
            else:
                print("You already assigned a value to Intelligence")
        elif x.lower() == "dexterity" or x.lower() == "d":
            if "Dexterity" in abilities:
                character_stats["Dexterity"]= roll[i]
                print("Dexterity = "+ str(y))
                abilities.remove("Dexterity")
                print(abilities)
                break
            else:
                print("You already assigned a value to Dexterity")
            
        else:
            #i -= 1
            print("Try again. Please check spelling.")
        
        print(character_stats)

#This builds the character stats. User chooses order of abilities based 
#on scores from highest to lowest. A dictionary is built that has
#the ability (such as Charisma) as the key and the stats as the value.
#The stats/value is [ability score, modifier]
#Step 3
def build_stats(x):
    roll = roll_stats_modifiers(x)  
    character_stats = {}
    abilities_list = ["Charisma", "Constitution", "Wisdom", "Strength", "Dexterity", "Intelligence"]
    print (roll)
    print("Enter stats in order.")
    
    #Need to solve this. How to determine the roll number
    #while being able to correct the user if they mistype
    #or try to reasign a value

    for i in range(len(roll)):
        y = roll[i][0]
        print("For the ability score of: " + str(y))

        check_stats(roll, i, y, character_stats, abilities_list)

    return character_stats

#Executes points_roll two times for a set of 5 abilities
#User will choose which set to use
#Step 1
def create_character_sheet():
    roll_one = points_roll()
    roll_two = points_roll()
    
    print("Now you will choose your character's traits.")
    print("You rolled two sets: ")
    print("Set 1: " + str(roll_one))
    print("Set 2: " + str(roll_two))
    print("")
    
    choice_roll = input("Choose a roll [1|2] >>> ")
    
    #This let's the user choose which set to use
    while True:
        if choice_roll == "1":
            basic_roll_stats = roll_one
            print("You chose: " + str(roll_one))
            break
        elif choice_roll == "2":
            basic_roll_stats = roll_two
            print("You chose: " + str(roll_two))
            break
        else:
            print("Please choose between 1 or 2.")
    
    # Takes the chosen roll and sorts them from highest to lowest
    sort = sorted(basic_roll_stats, reverse = True)
    sorted_roll_stats = sort
    
    #This call builds the character ability stats.
    character_ability = build_stats(sorted_roll_stats)
    
    #This will print out the character sheet
    #Ability:[score, modifier]
    return character_ability

#
#
#   GAME PLAY
#
#
char_one_ability_sheet = create_character_sheet()

print(char_one_ability_sheet)
