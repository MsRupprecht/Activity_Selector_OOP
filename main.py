import time
import random
from activities import Activity

## Instantiating each activity and empty lists

full_options = []
available_themes = []

# Reading
read1 = Activity("Read a Rick Riordan book.", "any", "reading", "relaxed")
read2 = Activity("Read a book from Mieke", "any", "reading", "relaxed")
read3 = Activity("Read Saga", "any", "reading", "relaxed")
read1.set_list(full_options)
read2.set_list(full_options)
read3.set_list(full_options)

# Learning
learn1 = Activity("Work through the Computing textbook", "any", "learning", "mentally active")
learn2 = Activity("Spend 30 minutes on Duolingo", "any", "learning", "mentally active")
learn3 = Activity("Work on French study guides", "any", "learning", "mentally active")
learn1.set_list(full_options)
learn2.set_list(full_options)
learn3.set_list(full_options)


# Computing
comp1 = Activity("Further develop your activity selector", "any", "computing", "mentally active")
comp2 = Activity("Start an HTML/CSS course", "inside", "computing", "mentally active")
comp3 = Activity("Investigate Flask/Django for deploying Python to the web", "inside", "computing", "mentally active")
comp4 = Activity("Put together a portfolio to show the development of your activity selector", "inside", "computing", "mentally active")
comp5 = Activity("Further develop your seating plan spreadsheet", "inside", "computing", "mentally active")
comp6 = Activity("Work on your Python Bootcamp Udemy course", "inside", "computing", "mentally active")
comp1.set_list(full_options)
comp2.set_list(full_options)
comp3.set_list(full_options)
comp4.set_list(full_options)
comp5.set_list(full_options)
comp6.set_list(full_options)


# Crafting
craft1 = Activity("Baste and stitch your EPP hexies", "any", "crafting", "relaxed")
craft2 = Activity("Construct your EPP school bag", "inside", "crafting", "relaxed")
craft3 = Activity("Crochet new scrunchies", "any", "crafting", "relaxed")
craft4 = Activity("Work on your Christmas Tree cross-stitch", "inside", "crafting", "relaxed")
craft5 = Activity("Outline next steps for your miniature library", "any", "crafting", "mentally active")
craft1.set_list(full_options)
craft2.set_list(full_options)
craft3.set_list(full_options)
craft4.set_list(full_options)
craft5.set_list(full_options)


# Exercise
exercise1 = Activity("Walk around Tooting Common", "outside", "exercise", "physically active")
exercise2 = Activity("Do a Zumba session", "inside", "exercise", "physically active")
exercise3 = Activity("Do a Nike Training session", "any", "exercise", "physically active")
exercise1.set_list(full_options)
exercise2.set_list(full_options)
exercise3.set_list(full_options)


# London
london1 = Activity("Spend an afternoon at Pinch", "outside", "London", "relaxed")
london2 = Activity("Spend an afternoon at Dee Light", "outside", "London", "relaxed")
london3 = Activity("Pick up new ingredients in China Town", "outside", "London", "physically active")
london4 = Activity("Hop on a bus to somewhere new", "outside", "London", "physically active")
london1.set_list(full_options)
london2.set_list(full_options)
london3.set_list(full_options)
london4.set_list(full_options)


# Media
media1 = Activity("Watch two episodes of Parks and Rec", "inside", "media","passive")
media2 = Activity("Watch two episodes of Ms. Marvel", "inside", "media", "passive")
media3 = Activity("Watch the first Harry Potter that comes up on Netflix", "inside", "media", "passive")
media4 = Activity("Watch two more episodes of the last program I watched", "inside", "media", "passive")
media1.set_list(full_options)
media2.set_list(full_options)
media3.set_list(full_options)
media4.set_list(full_options)

# Instantiating the rescue activities
rescue2 = Activity("Make a worry list, categorise what can be addressed and what needs to be let go, make a plan", "inside", "rescue", "mentally active")
rescue3 = Activity("Look at your autumn/winter Instagram for visualisation.", "any","rescue","passive")
rescue4 = Activity("Listen to some Christmas or lofi music.", "any", "rescue", "passive")
rescue5 = Activity("Organise a corner of the room you are in.", "inside", "rescue", "relaxed")
rescue6 = Activity("Gather blankets and buddies and have a snuggle.", "inside", "rescue", "passive")
rescue3.set_list(full_options)
rescue3.set_list(full_options)
rescue4.set_list(full_options)
rescue5.set_list(full_options)
rescue6.set_list(full_options)
rescue_options = []
rescue3.set_list(rescue_options)
rescue3.set_list(rescue_options)
rescue4.set_list(rescue_options)
rescue5.set_list(rescue_options)
rescue6.set_list(rescue_options)

# Create master list of available themes
Activity.get_available_themes(full_options,available_themes)

# Subroutines
def breath(repeat):
    for n in range (repeat):
        inhala = "Inhala"
        exhala = "Exhala"
        for n in range(len(inhala)):
            print (inhala[n], end = " ", flush = True)
            time.sleep(0.8)
        print("")
        for n in range(len(exhala)):
            print (exhala[n], end = " ", flush = True)
            time.sleep(1)
        print("\n")


# Starting the program

print("\nInhala, exhala...\n")
breath(2)


print("Hello Sunshine!  I'm proud of you for reaching out for help.")
print("How involved do you want to be in the decision making?")
need = input("1: No more choices, please  \n2: I'll give a bit of guidance \n3: I'll pick the categories if you pick the final activity\n>>")

# Select which mode - Rescue or Planning
typo1 = True
while typo1 == True:
    # Rescue Mode
    if need == "1":
        typo1 = False
        num = random.randint(0,len(rescue_options)-1)
        print("")
        print("First, think about the 4 U's.  Is your concern unimportant, unlikely, uncertain or uncontrollable?")
        print("Remember that worrying will not give you certainty or control.\n")
        print("Then your next step:")
        print("     "+str(rescue_options[num]))
        print("")
    
    # Guidance and Planning Mode
    elif need == "2":
        typo1 = False
        
        # Menu to select location and narrow results
        typo2 = True
        while typo2 == True:
            location_list = []
            location = input("Where do you want to be?\n1: Inside\n2: Outside\n3: Either\n>>")
            if location == "1":
                typo2 = False
                Activity.narrow_by_attribute(full_options, location_list,"location","inside")
                Activity.narrow_by_attribute(full_options, location_list, "location", "any")
            elif location == "2":
                typo2 = False
                Activity.narrow_by_attribute(full_options, location_list, "location", "outside")
                Activity.narrow_by_attribute(full_options, location_list, "location", "any")
            elif location == "3":
                typo2 = False
                Activity.narrow_by_attribute(full_options, location_list, "location", "any")
            else:
                print("Please try again.")
        
        # Menu to select energy and narrow results
        typo3 = True
        while typo3 == True:
            energy_list = []
            energy = input("What is your energy level?\n1: Passive\n2: Relaxed\n3: Mentally Active\n4: Physically Active\n5: Any level\n>>")
            if energy == "1":
                typo3 = False
                Activity.narrow_by_attribute(location_list, energy_list, "energy", "passive")
            elif energy == "2":
                typo3 = False
                Activity.narrow_by_attribute(location_list,energy_list,"energy","relaxed")
            elif energy == "3":
                typo3 = False
                Activity.narrow_by_attribute(location_list, energy_list, "energy", "mentally active")
            elif energy == "4":
                typo3 = False
                Activity.narrow_by_attribute(location_list, energy_list, "energy", "physically active")
            elif energy == "5":
                typo3 = False
                energy_list = location_list
            else:
                print("Please try again.") 
        final_list = energy_list
        num = random.randint(0,len(final_list)-1)
        print(final_list[num])    
        
        # Planning Mode Only
        # Menu to select themes and narrow results
    elif need == "3":
        typo1 = False
        theme_list = []
        themes_to_include = []
        print("Which activity types would you like to consider?\nRespond with Y or N")
        for theme in available_themes:
            typo4 = True
            while typo4 == True:
                include = input(theme.capitalize()+"?")
                if include == "Y" or include == "y":
                    themes_to_include.append(theme)
                    typo4 = False
                elif include == "N" or include == "n":
                    typo4 = False
                else:
                    print("Please try again.")
        
        for i in range(len(themes_to_include)):
            for j in range(len(full_options)):
                if Activity.get_theme(full_options[j]) == themes_to_include[i]:
                    theme_list.append(full_options[j])
        final_list = theme_list

        num = random.randint(0,len(final_list)-1)
        print(final_list[num])
    else:
        need = input("Try again please\n1: No more choices, please  \n2: I'll give a bit of guidance \n3: I'll pick the categories if you pick the final activity\n>>")

print("You've got this!")
