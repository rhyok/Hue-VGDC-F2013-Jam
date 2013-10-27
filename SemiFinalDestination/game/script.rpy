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
    chars = [a,n,f,v,w,r,m]

    def score(a,n,f,v,w):
        points[0] += a
        points[1] += n
        points[2] += f
        points[3] += v
        points[4] += w

    def score(b, score):
        if b == a:
            a += score
        elif b == n:
            n += score
        elif b == f:
            f += score
        elif b == v:
            v += score
        elif b == w:
            w += score
        else:
            return -1

    def killSomeone():
        max = 0
        kill = -1
        for i in range(0,5):
            if points[i] > max:
                max = points[i]
                kill = i
        alive[i] = False

    def checkStatus(b):
        return {
            a:alive[0],
            n:alive[1],
            f:alive[2],
            v:alive[3],
            w:alive[4]
        }.get(b, -1)

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

jump cabin_ent #cabin.rpy

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
