label panicEvent_1:
#Cabin Panic Event
#show cabin room
#play music suspenseful
"The killer is entering the cabin! Hide!"

#show biff_scared
a "Where the hell should I go!?"
menu:
    "Behind Armchair":
        "He picks up the chair beforehand and squats it 5 times, giving him just enough time to get out of sight from the murderer"
        $ score(0, 0, 0, 0, 0)
        jump panicChoice_a
    "In Closet":
        "Biff attempts to fit squeeze his broad, muscular body in amongst the clothes, but ultimately does as well at hiding himself as he did in high school algebra."
        $ score(10, 0, 0, 0, 0)
        jump panicChoice_a
    "Under Bed":
        "Biff’s large build can barely squeeze underneath the bed, and the lower half of his legs sticks out conspicuously."
        $ score(20, 0, 0, 0, 0)
        jump panicChoice_a
    "Under Table":
        "Biff tried to fit under the table. However his muscles bulged and applied upwards motion. His instinctual tendency to lift was near threatening his life as the monster drew closer."
        $ score(30, 0, 0, 0, 0) 
        jump panicChoice_a
    "Behind Door":
        "Biff always saw himself as a son towards his ideal father, Superman. He knew that hero would stand up against the monster and physically block the door. However, superman was a Krypton alien and Biff was 20 year old wannabe football player."
        $ score(40, 0, 0, 0, 0)
        jump panicChoice_a

n "Based on my previous calculations, the best spot to hide would be..."
menu:
    "Behind Armchair":
        n "Oh Boy! An armchair! I remember sitting in it pretending to be the King of Gondor"
        $ score(0, 40, 0, 0, 0)
        jump panicChoice_n
    "In Closet":
        "Billy hides where he has been most comfortable during the entirety of his life."
        $ score(0, 0, 0, 0, 0)
        jump panicChoice_n
    "Under Bed":
        "Skinny enough to pretend to be a rug, Billy slides under the bed with ease, but flashbacks of childhood paranoia cause him to weep quietly as he hides."
        $ score(0, 20, 0, 0, 0)
        jump panicChoice_n
    "Under Table":
        "Panicking severely and crying for his mother, Bill scrambles for the kitchen table to hide under. In his haste, he knocks over the glassware, cutting his legs and leaving a bloody trail towards the table."
        $ score(0, 40, 0, 0, 0)
        jump panicChoice_n
    "Behind Door":
        "Bill had noticed that there was a small hole near the front door that he could crawl into and hopefully hide away from the monster."
        $ score(0, 10, 0, 0, 0)
        jump panicChoice_n

f "Sat dere da murderer! Where can I hide?"
menu:
    "Behind Armchair":
        "He sits on the armchair instead, only realizing last minute that sitting on it did not make any sense."
        $ score(0, 0, 20, 0, 0)
        jump panicChoice_f
    "In Closet":
        "Barney enters the closet. He then decides it is a good opportunity to play dress up and starts trying on the clothes inside the closet."
        $ score(0, 0, 0, 0, 0)
        jump panicChoice_f
    "Under Bed":
        "Hiding under beds just happens to be one of Barney’s hobbies. He slips under the bed effortlessly like a graceful swan."
        $ score(0, 0, 10, 0, 0)
        jump panicChoice_f
    "Under Table":
        "Foolishly, Barney dashed for the first thing he could fit himself under, the kitchen table. However instead of keeping the tablecloth on the table inconspicuously, he tore it off and wrapped it around himself."
        $ score(0, 0, 20, 0, 0) 
        jump panicChoice_f
    "Behind Door":
        "Screaming at the top of the lungs, Barney ran around in circles until he finally decided to make a sprint out the door. However, by then the monster was already feet away from him. "
        $ score(0, 0, 30, 0, 0)
        jump panicChoice_f

v "I've never hid from someone before, I hope my inexperience in sex doesn't affect my choice!"
menu:
    "Behind Armchair":
        "Her ability to hide behind the armchair rivals her inexperience in sexual intercourse. It must have been a stroke of luck that she was able correctly determine a position so that she would not be seen."
        $ score(0, 0, 0, 10, 0)
        jump panicChoice_v
    "In Closet":
        "She pretends like she’s playing hide and seek like she had in her childhood and hides in the closet, putting the clothes available between her and the closet door."
        $ score(0, 0, 0, 30, 0)
        jump panicChoice_v
    "Under Bed":
        "Betsy’s best friend is her bed, so putting her life in the trust of a bed is no problem for her. She gladly throws herself beneath the piece of furniture."
        $ score(0, 0, 0, 40, 0)
        jump panicChoice_v
    "Under Table":
        "Betsy ran immediately for the kitchen table and rolling under the furniture piece. She used to hide here when her parents would argue, so she felt safe from the murderer."
        $ score(0, 0, 0, 0, 0)
        jump panicChoice_v
    "Behind Door":
        "Hiding behind the door wasn’t Betsy’s smartest idea, but her other friends were being so loud it might distract the monster away from her horribly bad hiding place."
        $ score(0, 0, 0, 20, 0)
        jump panicChoice_v  

w "Are you calling me a whoer?"
menu:
    "Behind Armchair":
        "Since she does a lot of her hobbies on couches, she knows what position to be in to prevent herself from being seen, and she does so quickly with seemingly practiced motions."
        $ score(0, 0, 0, 0, 30)
        jump panicChoice_w
    "In Closet":
        "Instead of hiding in the closet, Benlinda becomes occupied with insulting the lack of clothes within it. She makes fun of the style of clothing present, and starts loudly complaining how the fashion world is headed for a downward spiral. She then breaks into song about the subject."
        $ score(0, 0, 0, 0, 40)
        jump panicChoice_w
    "Under Bed":
        "Benlinda didn’t know that there was room under beds in the first place, since she’s always on top of them. Hiding beneath the bed should have been a simple task for a monster like her, but she couldn’t understand how to make her limbs work."
        $ score(0, 0, 0, 0, 30)
        jump panicChoice_w
    "Under Table":
        "Still in a drunken hangover, Belinda wasn’t fully aware of the incoming situation. However she did see that there was a half consumed bottle of jack under the table."
        $ score(0, 0, 0, 0, 10) 
        jump panicChoice_w
    "Behind Door":
        "Unaware of the intruder approaching the cabin, Belinda decided to go outside to get some fresh air to cure her "
        $ score(0, 0, 0, 0, 0)
        jump panicChoice_w 

label panicChoice_a:
    #Athlete Resolution
    "He picks up the chair beforehand and squats it 5 times, giving him just enough time to get out of sight from the murderer"
    jump panicEvent_2

label panicChoice_n:
    #stuff
label panicChoice_f:
    #stuff
label panicChoice_v:
    #stuff
label panicChoice_w:
    #stuff