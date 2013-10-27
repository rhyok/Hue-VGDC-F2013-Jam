label forest_intro:
    N "Murder is nigh!"

    N "Flee! Flee for your lives!"

    "The dark and gloomy forest looms ahead. There appears to be a small beaten path to the side."

    $ murderDistance = 25
    $ lastDir = ''

    #Athlete:   OK
    #Nerd:      Bad
    #Fool:      Good
    #Virgin:    Bad
    #Whore:     Good

    init python:
        caughtUp = False
        def distanceCheck():
            caughtUp = False
            if murderDistance <= 0:
                caughtUp = True
            return

    label maze:
        menu:
            "Run down the path.":
                $ lastDir = 'p'
                $ murderDistance += 15
                jump path
            "Run left.":
                $ murderDistance += 5
                $ lastDir = 'l'
                jump maze_2
            "Run right.":
                $ murderDistance += 5
                $ lastDir = 'r'
                jump maze_2
            "Run straight ahead.":
                $ murderDistance += 10
                $ lastDir = 's'
                jump maze_2

    label path:
        $ distanceCheck()
        if caughtUp: 
            jump caught

    label maze_2:
        $ distanceCheck()
        if caughtUp: 
            jump caught
    
    label caught:
        $ killSomeone()
