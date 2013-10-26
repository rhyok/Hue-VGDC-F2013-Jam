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

    #init python:
    #    def scenes(sceneName):


    $ test = False
    $ pointLimit = 1000
    $ points = [0,0,0,0,0]
    $ alive = [True,True,True,True,True]

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
    label intro:



    return
