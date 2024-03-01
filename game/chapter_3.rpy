default visited_320 = False

label counting_loses:
    scene bg classroom_101_night_darkened
    
    "I took deep breaths as I calmed myself down in the darkness of the hallway."

    Unknown "Who's here?"

    "Someone... David, whispered to my left"

    #TODO: Show David

    mc "Me"

    "I answered back with the same tone, throat parched after the sprint."
    "Then, others followed. I counted only three other voices. "
    #TODO: Show Ana, Maria Marius
    "Ana, Maria, and Marius."
    "I felt a node in my throat."
    "Alex and Theo were still down there."

    #TODO: Show David

    "David must have also realized the loss"

    David "Should we turn back?"

    #TODO: Show Ana, Maria Marius
    
    "However, we all knew that it was not feasible."

    "They were either already caught, or they’ll make their way to us at some point. Going back would only bring trouble."

    "To us and to them."

    "I took a look around at the outlines of the floor plan. It was the same as the last two, but this one was cleaner, neater."

    if map_found:
        call double_trouble
    else:
        "As I took a first step towards the direction in which the map showed professor Bostan’s cabinet, Marius grabbed me by my arm and dragged me into a nearby cabinet."
        call misery_of_a_man
    
    jump crossroads
    return

label double_trouble:
    "My eyes widened as I saw what looked like a list of cabinets and their professors from the corner of my eye, but just as I wanted to make it public, Marius dragged me by my arm into a nearby cabinet."

    call misery_of_a_man

    show ana with dissolve:
        xpos 300
        ypos 120
        zoom 0.7

    Ana "So, what now?"

    Ana "Do we just look from cabinet to cabinet?"

    mc "No need, I saw a list nearby, it’ll show us what we’re looking for."

    "I gestured towards one of the walls."
    
    hide ana with dissolve

    "And indeed, on two different papers were noted the cabinets, the professors and the hours within which they could be found there. The only thing left was to search for the right one."

    Marius "We’ll take the left one, you look it up on the one to the right."

    Marius "David, stand on guard duty."

    "The girls and David nodded in understanding."

    "The next couple of minutes were spent perusing the text line by line in silence."

    mc "301, Braga Vasili… 303, Cojuhari Irina… 305…"

    " Finally, under 117 stood the name we were searching for." 

    "I alerted Marius about it, just as a victorious sound came from the side of the girls."
    
    "We looked at each other in confusion, before Maria voiced out the problem."

    Maria "He's in cabinet 220."

    "Marius made his way over to their list and frowned."

    mc "He’s in 217."

    "It was Ana’s turn to move to the left and check out our list."

    Maria "No, it’s written here that he’s in 220."

    "But the adrenaline was starting to wear off, and I had trouble understanding what she was saying."

    "How could a cabinet be in two places at the same time?"

    Marius "It seems like it indeed is."

    "Ana went from our list, to theirs a couple of times, as Maria gave Marius a puzzled look."

    Ana "Mari."

    Ana "There’s two rooms." 

    "oh"
    "OH"
    "oh"

    "It finally clicked for me."

    mc "So there’s two cabinets that we have to search now?"

    Marius "Yes"
    
    "It seems like our last lap till victory just turned into two."

    return

label misery_of_a_man:
    "The twins and David followed, swiftly closing the door, just in time for this floor’s guard to cast his shadow under the door."

    "It was just a minute later that the light finally turned and, and with it, ironically, extinguished the hopes of catching up with Marius’ friends."

    menu:
        "Apologize":
            "I opened up my backpack and took out a bottle."
    
    mc "I’m sorry."

    "I didn’t specify what for, but we both knew what I meant."

    "He just nodded and took a gulp."

    "He must have felt miserable."

    "Losing all three people he came with did that to a man."

    "We waited until no more keys jiggling were heard, before exiting the cabinet and returning to the stairs."

    "This was it. The final act in our drama."

    return

label crossroads:
    Ana "So,"

    "We made our way towards the last two places that we had to search for our answer sheets. Thankfully, they weren’t far apart. "

    Ana "Which cabinet should we look into first? 317 or 320?"

    "Marius murmured something I couldn’t understand and looked at me."

    Marius "You’ve been giving pretty good advice till now, you pick."

    "I look at him dumbfounded."

    "That was a lot of responsibility to give to someone he barely knew."

    "But then again, hadn’t he also agreed with most of my other suggestions, till now?"

    menu:
        "Pick 317":
            mc "How about we look inside 317 first, it’s closer."

            "I wasn’t sure whether that was the right cabinet, but we still had a bit of time, so even if we were wrong, it wouldn’t hurt."
            jump breaking_into_317
        
        "Pick 320":
            mc "I know it’s not exactly logical, but I have a hunch that we should go for 320."

            " I didn’t know why, but I thought that number would make sense to be his cabinet."

            Marius "Well, lead the way."

            jump almost_420

label breaking_into_317:
    "When we finally arrived, we were presented with a simple wooden door on which hung a silver plaque with the writing “Receiving cabinet” written on it."

    "I tried the handle, but it didn’t work."

    mc "Can anyone pick a lock?"

    "This wasn’t a James Bond movie, but I did feel kind of like him, considering all the action of today."

    "As usual, one of the twins stepped up to put their questionable knowledge to good use."

    "Maria looked at the lock, tried the handle a few times, before taking out a bobby pin out of her hair and bending it. With this strange contraption, she proceeded to poke the keyhole."

    Marius "You do know that breaking the lock would raise suspicions, right?"

    "Marius reminded her, but not in a malicious tone. It seemed like it was something they’ve already discussed."

    "This was further demonstrated by the fact that she for once didn’t get mad at him, just shushed the tall guy with a dirty look, before continuing her work."

    "Less than a minute later, the door was open and we were free to look around."

    #TODO: Reciving Cabinet

    Marius "Me and David will look out for the guard. You guys hurry up and find what we need."

    "I nodded and followed the girls inside."

    "It was a nice room with a nice mahogany table, big wardrobe and a comfortable looking sofa on one of its sides. The wall on the opposite side of the sofa was covered in bookshelves holding documents, within documents, upon documents."

    "Well, this was going to be fun."
    mc "Where do we start?"

    Ana "Wardrobe, laptop, table… Just check anything that might seem possible."

    "I looked at her deadpan, then motioned towards the cabinet."

    mc "The whole room is possible, considering who it belongs to."

    Maria "Well, then get to it. The more time we spend speaking, the less time we have left for searching."

    "I sighed and looked at my surroundings."

    if visited_320:
        jump desperation_second_name
    else:
        jump what_are_we_looking_for

default checks_in_317 = 0

label desperation_second_name:
    menu:
        "Check the Wardrobe":
            $ time += 10
            $ checks_in_317 +=1

            "I looked inside the wardrobe hoping to find… something? Anything? Whatever I was searching for it wasn’t a pack of japanese cat food."

            if checks_in_317 < 3:
                jump desperation_second_name

        "Check the Table":
            $ time += 10
            $ checks_in_317 +=1

            "I frantically searched around the stacks of documents on professor Bostan’s table."

            "Legal papers, some documents of unknown origin, a few partnership agreements, culminated with the approval requests for the upcoming anniversary."

            "Finally, a slip of paper with the numbers 32111967 on it found its way into my hands."

            "I stopped the search, feeling victorious, until a sliver of doubt slid inside my head. Was it this easy? Was this really the password?"

            menu:
                "Continue Searching":
                    jump desperation_second_name
                "Stop Searching":
                    "We didn't have enough time. This will have to do."

        "Check the Laptop":
            $ time += 10
            $ checks_in_317 +=1

            "Surprisingly enough, there was a laptop kept in this cabinet. Either professor Bostan was extremely trusting in the university’s security, or he was trusting that no student would dare do something stupid if they ever found it."

            "Unfortunately for him, I was stupid enough to break into the university, so I was also stupid enough to look into other people’s computers."

            "I cracked the lid open and was met with the password screen. I tried remembering the digits I saw him introduce in the morning. After a few wrong tries, the screen showed the clue “FCIM anniversary”."

            "I looked for the password through most of the text files that even hinted at keeping any passcode in them, until I remembered."

            "The password for the computer was eight digits. So was the password for the cabinet."

            "I jumped at the possibility, but doubt still clouded my mind. Would he actually use the same password?"
            menu:
                "Continue Searching":
                    jump desperation_second_name
                "Stop Searching":
                    "We didn't have enough time. This will have to do."


    mc "Guys, I might have found what we needed."

    Ana "Are you sure? The number of inputs might be limited."

    menu:
        "Say I am sure":
            "I’m pretty sure."
        "Tell the truth":
            "I’m not sure, but having a clue is already better than nothing."
    
    "Let’s go back."

    jump access_granted


label what_are_we_looking_for:
    menu:
        "Check the Wardrobe":
            $ time += 10
            $ checks_in_317 +=1

            "Because the least obvious place is, apparently, the best place to start, I took a look into the wardrobe."
            "I had hoped for nothing, and yet I was still disappointed in my findings."
            "Ten minutes lost in vain."

            if checks_in_317 < 3:
                jump what_are_we_looking_for

        "Check the Table":
            $ time += 10
            $ checks_in_317 +=1

            "I looked at the table and felt myself die a little when I saw the amount of paperwork professor Bostan had to deal with."

            "Legal papers, some documents of unknown origin, a few partnership agreements, culminated with the approval requests for the upcoming anniversary."

            "A slip of paper with the numbers 32111964 on it."

            "However, there was no stack of exams."

            if checks_in_317 < 3:
                jump what_are_we_looking_for

        "Check the Laptop":
            $ time += 10
            $ checks_in_317 +=1

            "Surprisingly enough, there was a laptop kept in this cabinet. Either professor Bostan was extremely trusting in the university’s security, or he was trusting that no student would dare do something stupid if they ever found it."

            "Unfortunately for him, I was stupid enough to break into the university, so I was also stupid enough to look into other people’s computers."

            "I cracked the lid open and was met with the password screen. I tried remembering the digits I saw him introduce in the morning. After a few wrong tries, the screen showed the clue “FCIM anniversary”."\

            " I grinned like a madman, because I felt like a hacker from the movies once I was finally in."

            Maria "You do remember that the tests are on paper, right?"

            "I pouted, but closed the laptop."
            if checks_in_317 < 3:
                jump what_are_we_looking_for

    mc "Well, I found nothing."
    "I heard Maria let out a frustrated huff, before flopping dramatically on the couch."
    Maria "It's not here"

    Ana "Are you sure? We haven’t looked everywhere yet."

    Maria "I’m negatively positive."

    "Ana's shoulders dropped."

    mc "Seems like we have no other choice than to look in the other cabinet."

    jump almost_420




label almost_420:
    $ visited_320 = True


    
