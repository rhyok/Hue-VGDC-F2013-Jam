#Scene 3
label cabin_ent:
"Our unlikely gang of six have arrived at a cabin in the woods to celebrate the end of a hard school year."

#Log cabin background
#Show all 6 characters

#athlete to front
a "Brotastic!"

#fool to front
f "Let's drink all day and all night and all day again."

#robot to front
r "Boop boop beep boop."

N "Here's where you come in. This motley crew can only have a great time with your help."
N "Make the right decisions for each, and they'll have the time of their lives."

#hide all except athlete
label cabin_ent_a_choice:
a "Like, I wonder what I should do bros?"
menu:
    "Party!":
        $ score(50,0,0,0,0)
        a "Party up in here!"
        N "Biff lunges for the closest Budweiser can. This is just another drunken night for the frat boy, except with a hint of terror to come"
        jump cabin_ent_n_choice
    "Cook some food on the meager stove.":
        $ score(5,0,0,0,0)
        #hide all except nerd
        N "Biff may have been the jock of the group, but he was no stranger to the grill at a fine get-together. Biff roasts up a fine set of burgers and hot dogs for everyone to enjoy."
        jump cabin_ent_n_choice
    "Explore the woods.":
        $ score(30,0,0,0,0)
        #hide all except fool
        N "Biff decides to go find an open patch of field to toss the ball around, when he trips on a object hidden in the grass. A hockey mask?"
        b "Oh sweet, there is an ice rink around here!?"
        jump cabin_ent_n_choice
    "Go to sleep.":
        $ score(10,0,0,0,0)
        N "Biff's gains that he has previously achieved is now being stolen away by petty sleep. The creatine and pronom in his body is now going to waste."
        N "But, the forest has a much quieter night in exchange for Biff's losses."
        jump cabin_ent_n_choice
    "Have sex with Beep Boop":
        $ score(100,0,0,0,0)
        N "Biff finally succumbs to his robo-sexual preferences and romances Beep Boop."
        b "PENIS PENIS PENIS PENIS PENIS PENIS PENIS"
        N "The loud clanking of Biff's athletic body against Beep Boop alerts almost everything in the forest to their presence."

label cabin_ent_n_choice
a " My calculations indicate that the optimal course of action might be amongst these choices..."
menu:
    "Party!":
        $ score(0,0,0,0,0)
        N "With social stigmas pressuring him from all fronts, Bill caves into his newfound \"cool\" friends and requests to party. Not used to the alcohol, Bill passes out within the first hour."
        jump cabin_ent_n_choice
    "Cook some food on the meager stove.":
        $ score(30,0,0,0,0)
        #hide all except nerd
        n "I hope my experiences in the lab have helped me..."
        N "Yeah, you wish Billy. Having only ever made instant noodles and peanut butter and jelly sandwiches, Billy can't cook worth a damn. He produces a blackened mess on the stovetop, which everyone complains about loudly."
        jump cabin_ent_n_choice
    "Explore the woods.":
        $ score(30,0,0,0,0)
        #hide all except fool
        N "Biff decides to go find an open patch of field to toss the ball around, when he trips on a object hidden in the grass. A hockey mask?"
        b "Oh sweet, there is an ice rink around here!?"
        jump cabin_ent_n_choice
    "Go to sleep.":
        $ score(10,0,0,0,0)
        N "Biff's gains that he has previously achieved is now being stolen away by petty sleep. The creatine and pronom in his body is now going to waste."
        N "But, the forest has a much quieter night in exchange for Biff's losses."
        jump cabin_ent_n_choice
    "Have sex with Beep Boop":
        $ score(100,0,0,0,0)
        N "Biff finally succumbs to his robo-sexual preferences and romances Beep Boop."
        b "PENIS PENIS PENIS PENIS PENIS PENIS PENIS"
        N "The loud clanking of Biff's athletic body against Beep Boop alerts almost everything in the forest to their presence."
label intro_2:
menu:
    "Go to sleep.":
        jump scene_1

label scene_1:
    "Test."
    jump panicEvent_1
