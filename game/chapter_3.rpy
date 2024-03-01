default visited_320 = False

label counting_loses:
    scene bg classroom_101_night_darkened
    
    "I took deep breaths as I calmed myself down in the darkness of the hallway."

    Unknown "Who's here?"

    "Someone... David, whispered to my left"

    show david with dissolve

    mc "Me"

    hide david with dissolve

    "I answered back with the same tone, throat parched after the sprint."
    "Then, others followed. I counted only three other voices. "
    #TODO: Show Ana, Maria Marius
    "Ana, Maria, and Marius."
    "I felt a node in my throat."
    "Alex and Theo were still down there."

    show david with dissolve

    "David must have also realized the loss"

    David "Should we turn back?"

    hide david with dissolve

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

    show marius with dissolve
    
    Marius "We’ll take the left one, you look it up on the one to the right."

    Marius "David, stand on guard duty."

    hide marius with dissolve

    "The girls and David nodded in understanding."

    "The next couple of minutes were spent perusing the text line by line in silence."

    mc "301, Braga Vasili… 303, Cojuhari Irina… 305…"

    " Finally, under 117 stood the name we were searching for." 

    "I alerted Marius about it, just as a victorious sound came from the side of the girls."

    "We looked at each other in confusion, before Maria voiced out the problem."

    show maria with dissolve
    
    Maria "He's in cabinet 220."

    hide maria with dissolve

    "Marius made his way over to their list and frowned."

    mc "He’s in 217."

    "It was Ana’s turn to move to the left and check out our list."

    show maria with dissolve

    Maria "No, it’s written here that he’s in 220."

    "But the adrenaline was starting to wear off, and I had trouble understanding what she was saying."

    "How could a cabinet be in two places at the same time?"
    show maria with dissolve
    show marius with dissolve

    Marius "It seems like it indeed is."
    hide marius with dissolve

    "Ana went from our list, to theirs a couple of times, as Maria gave Marius a puzzled look."
    show ana with dissolve:
        xpos 300
        ypos 120
        zoom 0.7

    Ana "Mari."

    Ana "There’s two rooms." 

    hide ana with dissolve

    "oh"
    "OH"
    "oh"

    "It finally clicked for me."

    mc "So there’s two cabinets that we have to search now?"

    show marius with dissolve
    Marius "Yes"

    hide marius with dissolve
    
    "It seems like our last lap till victory just turned into two."

    return

label misery_of_a_man:
    "The twins and David followed, swiftly closing the door, just in time for this floor’s guard to cast his shadow under the door."

    "It was just a minute later that the light finally turned and, and with it, ironically, extinguished the hopes of catching up with Marius’ friends."

    menu:
        "Apologize":
            "I opened up my backpack and took out a bottle."
    
    mc "I’m sorry."

    show marius with dissolve

    "I didn’t specify what for, but we both knew what I meant."

    "He just nodded and took a gulp."

    "He must have felt miserable."

    "Losing all three people he came with did that to a man."

    "We waited until no more keys jiggling were heard, before exiting the cabinet and returning to the stairs."

    "This was it. The final act in our drama."

    hide marius with dissolve

    return

label crossroads:
    show ana with dissolve:
        xpos 300
        ypos 120
        zoom 0.7

    Ana "So,"

    "We made our way towards the last two places that we had to search for our answer sheets. Thankfully, they weren’t far apart. "

    Ana "Which cabinet should we look into first? 317 or 320?"
    hide ana with dissolve
    show marius with dissolve

    
    "Marius murmured something I couldn’t understand and looked at me."

    Marius "You’ve been giving pretty good advice till now, you pick."

    "I look at him dumbfounded."

    "That was a lot of responsibility to give to someone he barely knew."

    "But then again, hadn’t he also agreed with most of my other suggestions, till now?"
    hide marius with dissolve

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

    show maria with dissolve

    "Maria looked at the lock, tried the handle a few times, before taking out a bobby pin out of her hair and bending it. With this strange contraption, she proceeded to poke the keyhole."

    Marius "You do know that breaking the lock would raise suspicions, right?"

    "Marius reminded her, but not in a malicious tone. It seemed like it was something they’ve already discussed."

    "This was further demonstrated by the fact that she for once didn’t get mad at him, just shushed the tall guy with a dirty look, before continuing her work."

    hide maria with dissolve
    
    "Less than a minute later, the door was open and we were free to look around."

    #TODO: Reciving Cabinet

    show marius with dissolve

    Marius "Me and David will look out for the guard. You guys hurry up and find what we need."

    hide marius with dissolve

    "I nodded and followed the girls inside."

    "It was a nice room with a nice mahogany table, big wardrobe and a comfortable looking sofa on one of its sides. The wall on the opposite side of the sofa was covered in bookshelves holding documents, within documents, upon documents."

    "Well, this was going to be fun."
    mc "Where do we start?"

    show ana with dissolve:
        xpos 300
        ypos 120
        zoom 0.7

    Ana "Wardrobe, laptop, table… Just check anything that might seem possible."

    "I looked at her deadpan, then motioned towards the cabinet."

    mc "The whole room is possible, considering who it belongs to."

    Maria "Well, then get to it. The more time we spend speaking, the less time we have left for searching."

    "I sighed and looked at my surroundings."

    hide ana with dissolve

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

    show ana with dissolve:
        xpos 300
        ypos 120
        zoom 0.7
    
    Ana "Are you sure? The number of inputs might be limited."

    menu:
        "Say I am sure":
            "I’m pretty sure."
        "Tell the truth":
            "I’m not sure, but having a clue is already better than nothing."
    
    hide ana with dissolve

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

            "I cracked the lid open and was met with the password screen. I tried remembering the digits I saw him introduce in the morning. After a few wrong tries, the screen showed the clue “FCIM anniversary”."

            "I grinned like a madman, because I felt like a hacker from the movies once I was finally in."

            Maria "You do remember that the tests are on paper, right?"

            "I pouted, but closed the laptop."
            if checks_in_317 < 3:
                jump what_are_we_looking_for

    mc "Well, I found nothing."
    "I heard Maria let out a frustrated huff, before flopping dramatically on the couch."
    
    show maria with dissolve

    Maria "It's not here"

    hide maria with dissolve
    
    show ana with dissolve:
        xpos 300
        ypos 120
        zoom 0.7
    
    Ana "Are you sure? We haven’t looked everywhere yet."

    hide ana with dissolve

    show maria with dissolve

    Maria "I’m negatively positive."

    hide maria with dissolve

    "Ana's shoulders dropped."

    mc "Seems like we have no other choice than to look in the other cabinet."

    jump almost_420




label almost_420:
    $ visited_320 = True

    "As we arrived in front of a metal door with a silver plaque with the writing “Rector cabinet” on it, I knew we hit the jackpot."

    "With its lack of doorknob and pincode password pad, it looked more like a safe door, than an entrance to a cabinet. However, if tests and confidential information were kept there, I could understand the need for additional security."

    mc "Does anyone know how we could open this?"

    "Marius looked pointedly at the twins."

    show maria with dissolve
    
    "Maria came closer and looked at the lock for a few moments."

    Maria "All I can tell is that the password is eight characters and that it’ll more than likely alert the entire city, if we try to break it or introduce the incorrect password one too many times."

    hide maria with dissolve
    
    "Well that did not sound optimistic."

    if full_password:
        jump open_sesame
    else:
        jump attempts_were_made

label open_sesame:
    "Wait."

    "The memory of Professor Bostan introducing the password this morning resurfaced in my mind."

    "If that password had 8 characters, and this one also did, what was the probability that he would reuse the same password?"

    "I frowned. Maria did say ‘one too many times’, not ‘one time’, right?"

    "I decided to take the chance."

    menu: 
        "Input Password":
            jump access_granted


label access_granted:
    "I felt my hands shake a little, as I approached the numpad under the stares of my teammates. It was now or never. I introduced, carefully, one by one, the numbers as I remembered."

    "32… 11… 1967."

    "I took a deep breath, as I pressed the OK, expecting the worst, when the door let out a bip and opened itself."

    show marius with dissolve
    
    "Marius grabbed the edge of the door and pulled it towards himself to show an extremely small room behind it."

    "It was barely enough to fit two people inside, three if they manage to cram themselves."

    Marius "Seems like we’ll have to go by groups."

    hide marius with dissolve
    
    show ana with dissolve:
        xpos 300
        ypos 120
        zoom 0.7

    Ana "How about me, Maria and David go together and you go with our little genius."
    
    Ana "We’ll go first and search for the papers, while you stay on the lookout?"

    hide ana with dissolve

    show marius with dissolve
    
    Marius "It’s an idea. We should probably leave separately though."

    Marius "There’s bigger risks of getting caught if we just go out as a team. You think you could distract the guard after you’re done here and leave by yourselves?"

    hide marius with dissolve

    show sad_david with dissolve
    
    "David frowned at his proposal, but Ana quickly agreed."

    hide sad_david with dissolve
    show ana with dissolve:
        xpos 300
        ypos 120
        zoom 0.7
    
    Ana "Sure thing. Just remember not to stay too late. They raise the electric fence at 12."

    hide ana with dissolve
    
    "Marius nodded, mimicking her smile, and motioned for us to leave."

    jump patrolling_together

label attempts_were_made:
    "I looked at the numpad and picked at the bed of my thumb. It was 8 characters long. There were 100 million possible combinations. And just a few possible tries. How should we go about this?"

    menu:
        "Try to find clues in the other cabinet":
            show david with dissolve
            mc "Guys, it’s too risky. We can’t stay and fiddle with the pad until we guess."
            David "He’s right."
            "It was surprisingly David who shared my opinion."
            David "There’s too many combinations and we don’t actually know how the door will react to a wrong one."
            "I nodded."
            mc "We should go back to the other cabinet. See if there’s any clue that could help us at least narrow it down."
            hide david with dissolve
            "The others considered the information, before agreeing to backtrack."
            jump breaking_into_317
        "Try to guess":
            "Eight numbers, eight numbers… What could they be?"
            "It could be the date of someone’s birth. An encoding or encryption of a word. Maybe the date of some event?"
            "As I was thinking about a possible combination, the memory of professor Bostan putting in his laptop password flashed through my mind."
            "I stood up straighter. I haven’t seen it entirely, but I was pretty sure it had eight digits. I wondered wherever professor Bostan would reuse it."
            "It went 32, 11… I stopped my train of thought. What could there be missing? 3211..64. What were the missing digits?"
            python:
                numbers = renpy.input("What could be the number?").strip()
            
            if numbers == "19":
                jump access_granted
            else:
                jump finita_la_comedia

