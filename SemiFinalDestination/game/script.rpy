# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define a = Character('Biff', color="#FF0088")
define n = Character('Billy', color="#0000FF")
define f = Character('Barney', color="#FF00FF")
define v = Character('Betsy', color="#FFFF00")
define w = Character('Belinda', color="#FF0000")
define m = Character('??????', color="000000")
define r = Character('Beep-Boop', color="888888")
define N = Character('Morgan Freeman', color="FFFFFF")

# The game starts here.
label start:
    init python:
        test = False
        pointLimit = 1000
        points = [0,0,0,0,0]
        alive = [True,True,True,True,True]

        def score(a,n,f,v,w):
            points[0] += a
            points[1] += n
            points[2] += f
            points[3] += v
            points[4] += w


    #Scene 1
    N "This is a story."

    N "This is a story about six very typical people."

    N "But this is not a very typical story."

    #Scene 2
    #Show Biff
    N "{color=#FF0088}Biff{/color}. College varsity football quarterback, his ego is bigger than his ____."
    #Hide Biff

    #Show Billy
    N "{color=#0000FF}Billy{/color}. Nerd, 'nuff said."
    #Hide Billy

    #Show Barney
    N "{color=#FF00FF}Barney{/color}. Fool of a Took, I wouldn't trust him with a ."
    #Hide Barney

    #Show Beep-Boop
    N "{color=#888888}Beep-Boop{/color}. Your friendly neighborhood robot. He helps out the elderly with their grocery shopping on the weekends."
    #Hide Beep-Boop

    #Show Betsy
    N "{color=#FFFF00}Betsy{/color}. Cute, innocent, maybe too innocent..."
    #Hide Betsy

    #Show Belinda
    N "{color=#FF0000}Belinda{/color}. Comes with a side of crabs, if you know what I mean."
    #Hide Belinda

    N "How are they related?"

    #Show Murderer
    N "Looks like we're about to find out."
    #Hide Murderer

    #Scene 3
    label intro_1:
    "Our unlikely gang of six have arrived at a cabin in the woods to celebrate the end of a hard school year."

    #Log cabin background
    #Show all 6 characters

    #athlete to front
    a "Brotastic!"

    #fool to front
    f "Let's drink all day and all night and all day again."

    #robot to front
    r "Boop boop beep boop."

    N "What should they do?"
    menu:
        "Party!":
            $ score(0,40,15,30,5)
            #hide all except athlete
            s "Let the brewskies flooowwww!"
            jump intro_2
        "Cook some food on the meager stove.":
            $ score(5,30,0,5,15)
            #hide all except nerd
            n "Damn that was crappy food."
            jump intro_2
        "Explore the woods.":
            $ score(15,0,30,15,40)
            #hide all except fool
            f "I'm gonna go skinny dipping in the lake!"
            jump intro_2
        "Go to sleep.":
            jump scene_1

    label intro_2:
        menu:
            "Go to sleep.":
                jump scene_1

    label scene_1:
        "Test."
        jump panicEvent_1

    label panicEvent_1:
    #Cabin Panic Event
    #show cabin room
    #play music suspenseful
    "The killer is entering the cabin! Hide!"
    menu:
        "Behind Armchair":
            $ score(30, 5, 50, 70, 15)
            jump panicEventResolution_1
        "In Closet":
            $ score(5, 70, 30, 15, 50)
            jump panicEventResolution_1
        "Under Bed":
            $ score(50, 30, 15, 5, 70)
            jump panicEventResolution_1
        "Under Table":
            $ score(70, 15, 5, 50, 30) 
            jump panicEventResolution_1
        "Behind Door":
            $ score(15, 50, 70, 30, 5)
            jump panicEventResolution_1

    label panicEventResolution_1:
        "You are all really stupid and should have ran the fuck away from the house. you are all dead now."
        jump panicEvent_2

    label panicEvent_2:
    #Utility Shed Panic Event
    #show utility shed
    #play music suspenseful

    "The killer is coming into the shed! Pick a defender! Pick a weapon!"
    menu:
        "Saw":
            $ score(15, 70, 30, 50, 0)
            jump panicEventResolution_2    
        "Drill":
            $ score(70, 0, 50, 15, 30)
            jump panicEventResolution_2
        "Hedge Clippers":
            $ score(15, 50, 15, 0, 15)
            jump panicEventResolution_2
        "Machete":
            $ score(30, 70, 0, 50, 15)
            jump panicEventResolution_2
        "Shovel":
            $ score(15, 50, 70, 30, 0)
            jump panicEventResolution_2
        "Rubber Duck":
            $ score(100, 100, 100, 100, 100)
            jump panicEventResolution_2

    label panicEventResolution_2:
        "Why the hell didn't you choose the god damn rubber duck?? Y'all are pretty special. and dead."

    return
