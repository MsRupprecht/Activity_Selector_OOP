import time
from activities import Activity


## Instantiating each activity

# Reading
read1 = Activity("Read a Rick Riordan book.", "any", "reading", "relaxed")
read2 = Activity("Read a book from Mieke", "any", "reading", "relaxed")
read3 = Activity("Read Saga", "any", "reading", "relaxed")

# Learning
learn1 = Activity("Work through the Computing textbook", "any", "learning", "mentally active")
learn2 = Activity("Spend 30 minutes on Duolingo", "any", "learning", "mentally active")
learn3 = Activity("Work on French study guides", "any", "learning", "mentally active")

# Computing
comp1 = Activity("Further develop my activity selector", "any", "computing", "mentally active")
comp2 = Activity("Start an HTML/CSS course", "inside", "computing", "mentally active")
comp3 = Activity("Investigate Flask/Django for deploying Python to the web", "inside", "computing", "mentally active")
comp4 = Activity("Put together a portfolio to show the development of my activity selector", "inside", "computing", "mentally active")
comp5 = Activity("Further develop my seating plan spreadsheet", "any", "computing", "mentally active")

# Crafting
craft1 = Activity("Baste and stitch my EPP hexies", "any", "crafting", "relaxed")
craft2 = Activity("Construct my EPP school bag", "inside", "crafting", "relaxed")
craft3 = Activity("Crochet new scrunchies", "any", "crafting", "relaxed")
craft4 = Activity("Work on my Christmas Tree cross-stitch", "inside", "crafting", "relaxed")
craft5 = Activity("Outline next steps for my miniature library", "any", "crafting", "mentally active")

# Exercise
exercise1 = Activity("Walk around Tooting Common", "outside", "exercise", "physically active")
exercise2 = Activity("Do a Zumba session", "inside", "exercise", "physically active")
exercise3 = Activity("Do a Nike Training session", "any", "exercise", "physically active")

# London
london1 = Activity("Spend an afternoon at Pinch", "outside", "London", "relaxed")
london2 = Activity("Spend an afternoon at Dee Light", "outside", "London", "relaxed")
london3 = Activity("Pick up new ingredients in China Town", "outside", "London", "physically active")
london4 = Activity("Hop on a bus to somewhere new", "outside", "London", "physically active")

# Media
media1 = Activity("Watch two episodes of Parks and Rec", "inside", "media","passive")
media2 = Activity("Watch two episodes of Ms. Marvel", "inside", "media", "passive")
media3 = Activity("Watch the first Harry Potter that comes up on Netflix", "inside", "media", "passive")
media4 = Activity("Watch two more episodes of the last program I watched", "inside", "media", "passive")

# Instantiating the rescue activities
rescue1 = Activity("Remember the 4 Us: unimportant, unlikely, uncertain, uncontrollable.  Worrying will not give me certainty or control.", "inside", "rescue", "mentally active")
rescue2 = Activity("Make a worry list, categorise what can be addressed and what needs to be let go, make a plan", "inside", "rescue", "mentally active")
rescue3 = Activity("Look at my autumn/winter Instagram for visualisation", "any","rescue","passive")
rescue4 = Activity("Listen to some Christmas or lofi music", "any", "rescue", "passive")
rescue5 = Activity("Organise a corner of the room I'm in", "inside", "rescue", "relaxed")
rescue6 = Activity("Gather blankets and buddies and have a snuggle and  rest", "inside", "rescue", "passive")



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
#breath(3)

print("Hello Sunshine!  What are you looking for today?")
need = input("1: Rescue \n2: Plan my day\n>>")
typo = True

while typo == True:
    if need == "1":
        typo = False
        print("Rescue stuff`")
        
    elif need == "2":
        typo = False
        print("Options for activities")

    else:
        need = input("Try again please\n1: Rescue \n2: Plan my day\n>>")
print("out of loop")
