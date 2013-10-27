#Scene 3
label cabin_ent:
scene bg cabin interior

"Our unlikely gang of six have arrived at a cabin in the woods to celebrate the end of a hard school year."

#Log cabin background
#Show all 6 characters

show athlete:
    yalign_aboveText
    slide_in_from_left_to(0.4)
a "Brotastic!"

show fool:
    yalign_aboveText
    slide_in_from_left_to(0.2)
f "Let's drink all day and all night and all day again!"

show beepboop2 behind athlete
show beepboop2:
    yalign_aboveText
    slide_in_from_left_to(-.2)
r "Boop boop beep boop."
show athlete:
    slide_out_right
show beepboop2:
    slide_out_right
show fool:
    slide_out_right
pause 0.5
hide athlete
hide beepboop2
hide fool

N "Here's where you come in. This motley crew can only have a great time with your help."
N "Make the right decisions for each, and they'll have the time of their lives."
N "Make the wrong decisions and well... you'll find out soon enough."
N "What should the group do?"

#hide all except athlete
label cabin_ent_choice:
$ charSelected = renpy.random.randint(0,4) # Select a random character for the quote to be said
menu:
    "Party!":
        $ score(40,0,20,10,30)
        if charSelected == 0:
            show athlete:
                xalign 0.0
                yalign_aboveText
            a "Party up in here!"
            show athlete:
                slide_out_right
            N "Biff lunges for the closest Budweiser can. This is just another drunken night for the frat boy, except with a hint of terror to come"
            hide athlete with fade
        elif charSelected == 1:
            show nerd:
                xalign 0.0
                yalign_aboveText        
            N "With social stigmas pressuring him from all fronts, Billy caves into his newfound \"cool\" friends and requests to party. Not used to the alcohol, Billy passes out within the first hour, making a quieter night for the group of friends."
            n "W-well... my shirt has this anime chick on it because she's my waifu..."
            hide nerd with fade
        elif charSelected == 2:
            show fool:
                center
                yalign_aboveText
            N "Barney was always known to drink a little too much during the parties. Tonight was no difference as he lines up 4 straight shots of vodka"
            f "Hell yeah! Let's get smashed!"
            hide fool with fade
        elif charSelected == 3:
            show virgin:
                center
                yalign_aboveText
            N "Betsy was still new to the whole college party scene, being a bit uncomfortable around people. But somehow she felt like she could open up here, as if for some unforeseen reason she was safe"
            v "Thanks for having me out here, guys!"
            hide virgin with fade
        elif charSelected == 4:
            show whore:
                center
                yalign_aboveText
            N "Bass pumps from the speakers. The rest of the night for Belinda was a blur of sweaty bodies, booze, and slightest hint of illicit substances."
            w "This is my jam!"
            show whore:
                dance
            w "*shakes what her momma gave to her*"
            hide whore with fade
        jump cabin_ent_choice
    "Cook some food on the meager stove.":
        $ score(30,50,10,40,0)
        if charSelected == 0:
            show athlete:
                xalign 0.0
                yalign_aboveText
            N "Biff may have been the jock of the group, but he was no stranger to the grill at a fine get-together. He roasts up a fine set of burgers and hot dogs for everyone to enjoy."
            a "Like, order up dudes!"
            hide athlete with fade
        elif charSelected == 1:
            show nerd:
                xalign 0.0
                yalign_aboveText
            n "I hope my experiences in the lab have helped me..."
            N "Yeah, you wish Billy. Having only ever made instant noodles and peanut butter and jelly sandwiches, Billy can't cook worth a damn. He produces a blackened mess on the stovetop, which everyone complains about loudly."
            hide nerd with fade
        elif charSelected == 2:
            show fool:
                xalign 0.0
                yalign_aboveText
            N "Barney took it upon as his personal quest to make a sandwich for he and and his friends. However, this combination of alcohol, drugs and hot flames is never a good thing."
            f "Hey guys... what's this bright, dancing light on my sleeve?"
            hide fool with fade
        elif charSelected == 3:
            show virgin:
                xalign 0.0
                yalign_aboveText
            N "As her friends went off to slack off and enjoy their vacation, Betsy decided to prepare for the morning after with some food. However as she scoured the cabin kitchen, there were no knifes in the knife drawer."
            v "No knives? Oh dear..."
            hide virgin with fade
        elif charSelected == 4:
            show athlete:
                xalign 0.5
                yalign_aboveText
            a "I need some grub in here!"
            N "Biff boasted loudly throughout the cabin. To his surprise, Belinda, who didn’t look like she knew any useful skills, pulled out a frying pan and started to make a meal."
            show whore:
                yalign_aboveText
                slide_in_from_left_to(0.3)
            w "Anything for you Biffikins~! *glomp*"
            hide whore with fade
            hide athlete
        jump cabin_ent_choice
    "Explore the woods.":
        $ score(10,0,20,30,40)
        scene bg forest with fade
        if charSelected == 0:
            show athlete:
                xalign 0.0
                yalign_aboveText
            N "Biff decides to go find an open patch of field to toss the ball around, when he trips on a object hidden in the grass. A hockey mask?"
            a "Oh sweet, there is an ice rink around here!?"
            hide athlete with fade
        elif charSelected == 1:
            show nerd:
                xalign 0.0
                yalign_aboveText
            n "A new location needs to be fully explored!"
            show nerd:
                slide_out_right
            N "As Billy fulfills his curiosity, he notices strange footprints and markings around the cabin."
            hide nerd with fade
        elif charSelected == 2:
            show fool:
                yalign_aboveText
            f "I’m going to find the lake and go skinny dipping!"
            show fool:
                slide_out_right
            N "Barney ran off into the woods, with no direction in mind. Hopefully, he’ll return before the sun sets."
            hide fool with fade
        elif charSelected == 3:
            show virgin:
                yalign_aboveText
                slide_in_from_left_to(0.3)
                pause 0.5
                slide_out_right
                repeat
            N "Betsy explored the surroundings of the cabin like she explored her sexuality. Very badly."
            v "Wasn't I here a minute ago...?"
            hide virgin with fade
        elif charSelected == 4:
            N "Drunk, in a stupor, and desperately needing fresh air, Belinda walks outside into the dark woods. While everything that happened there was a blur, Belinda eventually returned though she had strange cuts on her right leg."
            show whore:
                yalign_aboveText
                slide_in_from_left_to(0.3)
            w "Alright... which one of you was it?"
            hide whore with fade
        jump cabin_ent_choice
    "Go to sleep.":    
        $ score(10,0,0,0,0)   
        if charSelected == 0:
            N "Biff may have been the jock of the group, but he was no stranger to the grill at a fine get-together. He roasts up a fine set of burgers and hot dogs for everyone to enjoy."
            a "Like, order up dudes!"
        elif charSelected == 1:
            n "I hope my experiences in the lab have helped me..."
            N "Yeah, you wish Billy. Having only ever made instant noodles and peanut butter and jelly sandwiches, Billy can't cook worth a damn. He produces a blackened mess on the stovetop, which everyone complains about loudly."
        elif charSelected == 2:
            N "Barney took it upon as his personal quest to make a sandwich for he and and his friends. However, this combination of alcohol, drugs and hot flames is never a good thing."
            f "Hey guys... what's this bright, dancing light on my sleeve?"
        elif charSelected == 3:
            N "As her friends went off to slack off and enjoy their vacation, Betsy decided to prepare for the morning after with some food. However as she scoured the cabin kitchen, there were no knifes in the knife drawer."
            v "No knives? Oh dear..."
        elif charSelected == 4:
            a "I need some grub in here!"
            N "Biff boasted loudly throughout the cabin. To his surprise, Belinda, who didn’t look like she knew any useful skills, pulled out a frying pan and started to make a meal."
            w "Anything for you Biffikins~!"
        jump cabin_ent_choice
    "Have sex with Beep Boop":
        $ score(100,0,0,0,0)
        if charSelected == 0:
            N "Biff may have been the jock of the group, but he was no stranger to the grill at a fine get-together. He roasts up a fine set of burgers and hot dogs for everyone to enjoy."
            a "Like, order up dudes!"
        elif charSelected == 1:
            n "I hope my experiences in the lab have helped me..."
            N "Yeah, you wish Billy. Having only ever made instant noodles and peanut butter and jelly sandwiches, Billy can't cook worth a damn. He produces a blackened mess on the stovetop, which everyone complains about loudly."
        elif charSelected == 2:
            N "Barney took it upon as his personal quest to make a sandwich for he and and his friends. However, this combination of alcohol, drugs and hot flames is never a good thing."
            f "Hey guys... what's this bright, dancing light on my sleeve?"
        elif charSelected == 3:
            N "As her friends went off to slack off and enjoy their vacation, Betsy decided to prepare for the morning after with some food. However as she scoured the cabin kitchen, there were no knifes in the knife drawer."
            v "No knives? Oh dear..."
        elif charSelected == 4:
            a "I need some grub in here!"
            N "Biff boasted loudly throughout the cabin. To his surprise, Belinda, who didn’t look like she knew any useful skills, pulled out a frying pan and started to make a meal."
            w "Anything for you Biffikins~!"
        jump cabin_ent_choice

label cabin_ent_f_choice:
n "Duuuuuuude... this cabin is tiiiiight!"
menu:
    "Party!":
        $ score(20,0,0,0,0)
        N "Barney was always known to drink a little too much during the parties. Tonight was no difference as he lines up 4 straight shots of vodka"
        f "Shoooooots!"
        jump cabin_ent_n_choice
    "Cook some food on the meager stove.":
        $ score(50,0,0,0,0)
        #hide all except nerd
        n "I hope my experiences in the lab have helped me..."
        N "Yeah, you wish Billy. Having only ever made instant noodles and peanut butter and jelly sandwiches, Billy can't cook worth a damn. He produces a blackened mess on the stovetop, which everyone complains about loudly."
        jump cabin_ent_n_choice
    "Explore the woods.":
        $ score(0,0,0,0,0)
        n "A new location needs to be fully explored! That's what I've always said!"
        N "As Billy fulfills his curiosity, he notices strange footprints and markings around the cabin."
        jump cabin_ent_n_choice
    "Go to sleep.":
        $ score(30,0,0,0,0)
        N "Not the partying type, Billy decides to turn in early. Unfortunately, the raucous noise his friends make celebrating leaves him rather sleepless."
        jump cabin_ent_n_choice
    "Have sex with Beep Boop":
        $ score(10,0,0,0,0)
        N "Thanks to experiences with his Yui body pillow, Billy was no stranger to intimate relations with inanimate objects. However, having spent the entirety of his college experience in the lab, he IS a stranger to sex."
        N "Billy treats Beep Boop right, and cuddles with him into the night."
        jump cabin_ent_n_choice
label intro_2:
menu:
    "Go to sleep.":
        jump scene_1

label scene_1:
    "Test."
    jump panicEvent_1
