define Marius = Character("Marius", color="#4c4fd4", image="Marius")
define Ana = Character("Ana", color="#75cc69", image="Ana")
define Maria = Character("Maria", color="#979c4c", image="Maria")
define Theodora = Character("Theodora", color="#d4604c", image="Theodora")
define David = Character("David", color="#ac619f", image="David")
define Alex = Character("Alex", color="#502749", image="Alex")
image window = "chapter_2/window_FAF_cab.png"
image rope = "chapter_2/rope.png"
image smartphone = "chapter_1/Smartphone.png"

label chapter2:
    jump high_way_to_hell

label high_way_to_hell:
    scene bg second_floor_hall

    "The second floor didn't look too different than the first one, except for the fact that it was illuminated."

    "It was still a large hallway with numerous doors on both sides that curved in several places to hide additional sections."

    "However, the space was less empty than I remembered."

    "Between the doors of the physics laboratory and FAF cabinet usually stood two blue sofas, followed by a potted plant, in front of the closet."

    "Further into the hall, the bathroom was framed by two glass cases with trophies, after which there was a sea of tables, and finally, at the end of the corridor, stood the staircase to the third floor."

    "All that separated us from our goal were the objects strewn around."

    "And the guard who came straight from behind the corner."

    "We had a split of a second to make a decision, before our journey and academic carrier were suspended indefinitely."

    $ key = True #TODO should be removed
    menu:
        "Hide in FAFcab":
            jump privileges_used_for_evil
        "Hide in physics lab" if key == True:
            jump a_different_kind_of_lab
    jump scatter

label from_bad_to_worse:
    "We waited for the sound to get quieter, but as it came closer and closer and then stopped, we looked at each other in abject horror."

    "He decided to sit on the sofa."

    show marius with dissolve

    "Marius swore under his breath." 

    Marius "This isn't good. How often does he patrol the corridors?' he turned towards the twins and asked."

    "At this point I came to accept that some things just never made sense in this group, and decided not to bother asking because I probably won't be getting my answer any time soon."
    hide marius with dissolve

    show ana with dissolve:
        xpos 300
        ypos 120
        zoom 0.7

    "Ana thought for a moment, before asking."

    Ana "What shoes?"

    hide ana with dissolve
    show maria with dissolve

    Maria "Martins. Brown. Last year's model."
    "It was Maria who supplied the answer, and her sister frowned."

    hide maria with dissolve
    show ana with dissolve:
        xpos 300
        ypos 120
        zoom 0.7

    Ana "That one is literally a slug. Considering he has a view of the corridor, he'll stay here till his shift is over."

    hide ana with dissolve
    show marius with dissolve

    "Marius cursed again."
    Marius "What can we do? We can't move further if he's sitting right next to us."

    hide marius with dissolve
    show david with dissolve

    David "We'll have to use a distraction again." 

    "The others looked at him like he was stupid."

    hide david with dissolve
    show theodora with dissolve

    "Theodora pinched the bridge of her nose."
    Theodora "David, no offense, but we can't exactly walk from room to room to distract him, and that's kind of needed in this situation."
    hide theodora with dissolve

    return

label privileges_used_for_evil:
    "I dove towards the FAFcab, taking out the key out of my pocket, for once grateful not to have it on a ring, and turned the lock open."

    scene bg fafcab room night

    "In less than a moment we were all huddled on the opposite side of the door, breathing heavily, and listening to the guard whistle a tune."

    jump from_bad_to_worse
    jump bad_situations_require_bad_solutions

label a_different_kind_of_lab:
    "I dove towards the physics laboratory, taking out the key out of my pocket found in 118, and turned the lock open."
    "In less than a moment we were all huddled on the opposite side of the door, breathing heavily, and listening to the guard whistle a tune."

    scene bg laboratory

    call from_bad_to_worse

    menu:
        "Try a different type of distraction":
            mc "But what if we didn't have to walk around?"
            "Everyone turned in my direction."
            "Some of them wore puzzled faces, while others had an eyebrow raised in curiosity."

            show marius
            "Marius was the one who asked first."
            Marius "Explain"
            hide marius

            mc "We're in the physics lab right now."
            mc "Right next door is the FAFcab."
            mc "It's got really useful stuff in it, like anime posters, a couch, a router, but most important…"
            mc "there's a bluetooth stereo."

            show maria
            "Maria jumped at the possibility."
            Maria "Is it on batteries or…?"
            hide maria

            mc "It's on batteries, but we usually keep it plugged in, so as long as there's power, it should work."

            show ana with dissolve:
                xpos 300
                ypos 120
                zoom 0.7
            Ana "Then we'll have to send someone to turn it on"
            "Ana brightened, before her shoulders dropped."
            Ana "We can't go through the door, though… He's literally next to it."
            hide ana

            "I frowned."
            "We couldn't really be locked though?"
            "There should be other options of movement besides the main hallway?"
            "It's not like we could get locked inside. There had to be some doors, maybe holes in the wall, or some…"

            "It took me a second to remember the time Vasile left his phone in a locked cabinet."

            mc "Guys, we can use another method."
            mc "I once had a colleague who forgot his phone in the nearby cabinet "
            mc "I traversed the room under their questioning gaze and got up on one of the tables" 
            mc "There's a small ledge under the windows, if you're careful enough, you can use it to move from one cabinet to the others."

            show marius
            "Marius came over to confirm my words for himself."
            Marius " Oh. I never noticed."
            "He frowned again."
            Marius "It's extremely narrow, though. There's barely any room for a foot.”"
            hide marius

            show david
            "David came closer, took a look at the ledge, thought for a few seconds, before determination crossed his face."
            David "I can go. I've had to walk in smaller spaces, it won't be a problem."
            "He looked at me."
            David "Do you have any rope or something else I could use?"
            # hide david

            menu:
                "Hand the rope":
                    show rope at center
                    mc "Here"
                    "I put a coil in his hand, and he started wrapping it around the metal bar next to the window"
                    mc "Be careful not to fall there."
                    hide rope

                    David "Thanks, but I'm kinda favored by God, so you shouldn't worry"
                    "He laughed and I started to question the decision of letting him go through this"
                    David "So, how will we do this?” He turned to Marius for indications."
                    hide david

                    "Marius seemed to forget their rivalry for a second and focused on making sure the rope was tied well enough, before he busied himself with opening the window."

                    show marius
                    Marius "You go there, find the stereo, press the button and come back."
                    "He turned to me for a second."
                    Marius "Where's the stereo?"
                    

                    mc "Up on the left wardrobe. It's white, you'll find it."

                    "Marius turned back to David and repeated my words."
                    Marius "Up on the left wardrobe. It's white, you'll find it."
                    hide marius

                    "That was an extremely stupid exchange."

                    show david
                    David "Alright then"
                    David "I'll drop in. Turn it on. Drop out."
                    hide david

                    "“Kinda like my father,” I heard someone whisper in the back."

                    show marius
                    "Marius covered his laughter with a cough."
                    Marius "Well, good luck comrade." 
                    "He gave David a nod, before the slippered man, helped by Maria, got onto the table, out of the window, and out of sight, leaving us waiting for his return."
                    hide marius

                    "Two minutes turned into five, which turned into 10, before a familiar notification appeared on my phone about connecting to a new bluetooth device."

                    "Ten more minutes and our friend was right back where he started, looking prouder of himself than ever."

                    mc "Good job" 
                    "I told him, as he unraveled the rope from around himself and handed it back. I took it from him and joined the others by the exit door."

                    "I quietly counted to three before pressing the button to connect to the stereo. Then, selecting the most annoying song on my playlist I could, I sealed the plan."

                    "We watched as the silhouette of the guard jumped and then promptly moved in the direction of FAFcab. We gaped the door slightly, hoping he would follow through and enter."

                    "Sometimes Murphy's law didn't work, I celebrated, because for once everything was going as it should. This was probably the easiest way we'd gotten out of a hunch."

                    "Or at least it would have been if the lights didn't turn off, just as we stepped foot into the hallway."

                    jump lights_out
        "Find an alternative way to move around":
            jump bad_situations_require_bad_solutions

label bad_situations_require_bad_solutions:
    "I frowned."
    "We couldn't really be locked though?"
    "There should be other options of movement besides the main hallway?"
    "It's not like we could get locked inside. There had to be some doors, maybe holes in the wall, or some…"
    "It took me a second to remember the time Vasile left his phone in a locked cabinet."

    "I jumped at the possibility immediately."
    mc "Guys, we can use another method. I once had a colleague who forgot his phone in the nearby cabinet"
    "I traversed the room under their questioning gaze and got up on the sofa,"
    mc "There's a small ledge under the windows, if you're careful enough, you can use it to move from one cabinet to the others."

    show window at center with dissolve:
        xpos 950 
        ypos 700

    "Marius brightened and came over to confirm my words for himself."

    show marius at left with dissolve
    Marius "Oh. I never noticed."
    Marius "It's extremely narrow, though. There's barely any room for a foot."
    hide marius with dissolve

    show david at right with dissolve
    "David came closer and took a look at the ledge before determination crossed his face."
    David "I can distract him. I've had to walk in smaller spaces, it won't be a problem."
    "He looked at me."
    David "Do you have any rope or something else I could use?"
    hide david with dissolve

    hide window with dissolve

    $ phone = True # remove later when combine with chap 1
    menu: 
        "Hand the rope":
            jump dangerous_maneuvre
        "Hide in physics lab" if phone == True:
            jump stealing_or_saving
        
label dangerous_maneuvre:
    show rope at center with dissolve
    mc "Here, I said as I put a coil in his hand, and he started wrapping it around the metal bar next to the window,  Be careful not to fall there."
    hide rope

    show david at right with dissolve
    David "Thanks, but I'm kinda favored by God, so you shouldn't worry,” the guy laughed and I started to question the decision of letting him go through this."
    David "So, how will we do this? He turned to Marius for indications."
    hide david with dissolve

    "Marius seemed to forget their rivalry for a second and focused on making sure the rope was tied well enough, before he busied himself with opening the window."
    
    show marius at right with dissolve
    Marius "It'll go as usual. Same flash for distraction, two for help, then move, and if you're close to being spotted, crouch."
    hide marius with dissolve

    "David furrowed his brow."
    show david at right with dissolve
    David "Is someone else going to be walking the ledge on the other side of the hall?"
    hide david with dissolve

    show marius at right with dissolve
    Marius "It's not necessary, neither for you, nor for the partner."
    Marius "The gig will work as usual, it's only distracting the guard for the first time and getting the partner to the first position that is going to be troublesome." 
    Marius "You climb to another cabinet, distract the guard, then you'll be walking the hallways as before."
    

    "He turned towards me and the others."
    Marius "Does anyone want to volunteer to be the second distraction?"
    hide marius with dissolve

    menu:
        "Volunteer":
            $ d_affection = d_affection + 1
            mc "I'll do it,"
            "I looked through the window, calculating the height if David did decide to take the plunge."

            show ana with dissolve:
                xpos 300
                ypos 120
                zoom 0.7
            "Ana looked at me with a raised eyebrow." 
            Ana "Are you sure? Do you know what you're supposed to do?"
            hide ana

            menu:
                "No (see tutorial)":
                    jump tutorial_screen
                "Yes (skip tutorial)":
                    mc "Yes, it's fine. We'll be back before you say Chebyshev,"

                    show theodora at right with dissolve
                    "Alright, then suit yourself,  Theodora shrugged." 
                    Theodora "Just be careful not to be caught and not to get your partner caught."
                    hide theodora

            "I nodded my thanks and prepared myself morally for the mission."

            "David climbed onto the windowsill, eyeing me gratefully and told me to wait for the signal."
            "I saluted him and moved closer to the door, just as the guy disappeared from the view of the group in his whole slippery glory."

            "I listened to the guard's whistle, until it got quiet and his keys started giggling."
            "After his steps were gone, I immediately set out for my position."

            jump minigame

            if _return:
                "Feeling victorious, we rushed out of the cabinet, towards the stairs, when the unexpected happened. The lights turned off."

                jump lights_out

        "Abstain":   
            $ d_affection = d_affection - 1

            "I watched in silence as people considered whether to volunteer. While Marius made it sound easy, the truth was, on unknown territory, with lots of obstacles, the mission increased its difficulty at least twofold."

            "After a few minutes of silent debating and anxious waiting on David's part, Ana stepped forth and agreed to be his partner."

            "Maria once again checked the rope, before helping David onto the ledge and out of the window. We all huddled around the entrance to the room, keeping our eyes on the outline of the guard and waiting for the signal."

            "Two minutes turned into five minutes, turned into twelve, and there was still nothing from the guy."

            show ana with dissolve:
                xpos 300
                ypos 120
                zoom 0.7
            "Ana started chewing on her lip in worry." 
            Ana "Do you think he fell?”"
            hide ana

            show maria with dissolve
            "Maria didn't say anything, just left the side of the door and went to check the window. She moved this way and that before letting out a frustrated sigh."
            Maria "I can't see him from here. So he's probably not dead, just picked a cabinet farther away."
            hide maria

            show alex with dissolve
            "Just as Ana nodded her understanding, Alex jumped."
            Alex "It's the signal. He started. Get ready"

            "The minute the guard turned his back towards the door, Ana dashed to the other side of the corridor, inside a cabinet."
            "It didn't take long for the guard to reach David, that his light went dead and Ana started clicking her flashlight, pointing at the guard. He changed direction, but David didn't come out of his cabinet."

            "However, when the guard started approaching Ana, his light came from another room. He probably decided to use the windows, instead of the corridor."

            "The dance continued, leading the guard further and further away, until he couldn't be seen anymore."

            "We were almost celebrating our victory when the lights went out."

            jump lights_out

label stealing_or_saving:
    "I rummaged through my bag to find the rope that I brought from home, when my hand stumbled upon a slick brick of unfamiliar shape."
    "I stopped for a second, before remembering that I've picked up Viorel's phone when I still had no idea about the existence of the group."

    "I thought whether it would be questionable or not that I had possession of their friend's property, before I decided to roll with the ball."
    show smartphone with dissolve

    mc "I actually have a different idea"  
    "I take out the spoil of war and showthe big smartphone to the others."
    "Immediately recognition passed through their gazes, before settling on warriness."

    "Yeah, about what I was expecting."
    mc "I picked this up back in the classroom when I was trying to identify who forgot their stuff..."
    mc "Didn't manage to put it back before the guard showed up, and kind of forgot about it after meeting you guys."

    "The reasoning was dumb, but somehow, either due to actually showing the phone or due to exhaustion, it did the job because they dropped the hostile attitude immediately."

    hide smartphone with dissolve

    show marius at center with dissolve
    "Marius inquired as he eyed the device."
    Marius "What are you proposing?" 
    hide marius

    mc "You guys know his phone number, right?" 
    mc "I was thinking that instead of playing hide and seek we could plant the phone on the other side of the corridor and call it."
    mc "This way we won't have to risk running back and forth in plain light."

    "The others considered the plan carefully before Theo tugged Marius by his sleeve."
    show theodora
    Theodora "It's a good idea. They've already caught Viorel."
    Theodora "If we leave his phone to be found by the guards, he'll have a good motive for entering the university at night."
    hide theodora

    show david
    "David's eyes widened at her words."
    David "Then I'm all for this plan."
    "He must have still felt guilty about setting the poor fellow to be caught."
    hide david

    "One by one the others weighed the pros and cons and also decided in favor." 
    "All that was left was the unofficial leader of the group."

    show marius
    "Marius hummed, and we could all see on his face the moment he made the decision." 
    Marius "Alright. Then that's what we'll do."
    hide marius

    "Alex gave out an appreciative “yes”, waited for me to take out the rope and hurried to help David tie it around himself and to the pole near the window."
    "After the knots were all tied, he took the device in his hand and, with the help of Maria, went through and out of the window."

    "Everybody huddled in the dimly lit cabinet around the sofa, awaiting David's return."

    "Two minutes turned into five minutes, turned into twelve, and there was still nothing from the guy."

    show ana with dissolve:
        xpos 300
        ypos 120
        zoom 0.7
    "Ana started chewing on her lip in worry."
    Ana "Do you think he fell?"
    hide ana

    show maria
    "Maria didn't say anything, just checked the window again." 
    "She moved this way and that, before letting out a frustrated sigh."
    Maria "I can't see him from here."
    Maria "So he's probably not dead, just picked a cabinet farther away."
    hide maria

    "Just as Ana nodded her understanding, a figure came through the window and arms wound themselves around Maria's shoulders, startling her."

    show david
    David "Did you miss your lord and savior?"
    "David joked, poorly imitating Marius's cockiness."
    hide david

    "Maria jumped and then playfully slapped him for scaring her."

    show marius
    "Marius rolled his eyes and asked the slipper knight" 
    Marius "Did you place it?"
    hide marius

    show david
    David "Yep"
    "David moved towards the door. Everyone else followed, settling their gaze on the still silhouette of the guard."
    hide david
    "Marius took out his phone." 
    "The call went through and we heard a tiny beep once, twice, and then finally the ringtone started blasting through the hall, startling the guard and forcing him to check the cabinet."

    "Feeling victorious, we rushed out of the cabinet, towards the stairs, when the unexpected happened. The lights turned off."
    jump lights_out
    
label lights_out:
    scene bg second_floor_hall

    "No, No, No."

    "I panicked as the lamps above us went off, leaving us in shrouded darkness, among a sea of obstacles scattered between us and our path to freedom, with its guardian right behind us, just waiting for us to stall."

    "I didn't think twice before grabbing the hand that was closest to me and dragging whoever I got right behind me."
    "I prayed that I still remembered the layout because this was either the place where we would succeed and get closer to our goal or the place where we would get utterly hurt and humiliated."

    $ correct_order = ['sofa', 'sofa', 'plant', 'trophy', 'trophy', 'table', 'table', 'table']
    $ correct_num = 0
    $ current_index = 0


    while current_index < 8:        
        menu:
            "sofa":
                if correct_order[current_index] == 'sofa':
                    $ correct_num = correct_num +1
                    "I jumped over something, prepared for it to be a sofa and felt my heart stop, before it beat faster, because I made it."
                else: 
                    "I jumped over something, prepared for it to be a sofa and felt my heart stop, before regretting, because what should have been a clean jump, ended in a painful stumble."
                $ current_index = current_index + 1
            "plant":
                if correct_order[current_index] == 'plant':
                    $ correct_num = correct_num +1
                    "I squeezed my way besides something leafy, narrowly missing the base of the vase."
                else: 
                    "I squeezed my way while passing by, but instead of feeling foliage, my elbow collided with something hard, leaving my arm throbbing."
                $ current_index = current_index + 1
            "trophy":
                if correct_order[current_index] == 'trophy':
                    $ correct_num = correct_num +1
                    "I dodged and hoped not to hear the sound of glass shattering, and when all I left behind was dust, I sighed relieved, but didn't stop running."
                else: 
                    "I dodged at just the wrong time, colliding with a heavy object, and heard the sound of something breaking."
                $ current_index = current_index + 1
            "table":
                if correct_order[current_index] == 'table':
                    $ correct_num = correct_num +1
                    "I crawled beneath what I believed was a table, barely tall enough to fit me and my partner."
                else: 
                    "I started to crawl beneath what I believed was a table, only to bump my head and lose a few precious seconds."
                $ current_index = current_index + 1
    
    if correct_num>4:
        "We sped through the chaos of the hallway, praying to make it out of there in one piece, listening to the steps of both my friends and enemy behind me."

        "Just as I was starting to feel like we took a wrong turn somehow, my foot hit a stair and I fell forward."
        "It was probably the first time I was happy to have stabbed a toe."

        "Not stopping for the pain, I continued dragging my companion forward, up the stairs, until we finally reached the first flight."
        "I let go of their hand, but didn't stop running."
        "I kept going up and up and up, until finally the stairs gave way to flat ground and I heard no more steps behind me, only panting."

           
        jump counting_losses
    else:
        "{size=-10}I tried to keep up with the rest of the footsteps ahead of me, as I poorly maneuvered within the labyrinth, but as time went by, and as more and more objects kept being thrown at me by whichever deity I managed to anger this evening, I lost track of both my friends, as well as the direction.{/size}"

        "I prayed that I would be given a sight. A way to at least guess what stood ahead of me when the universe decided to grant me my wish."

        scene bg second_floor_hall light

        "The light turned on."

        "And as my eyes got used to the brightness once more, all I could see in front of me was the angry guard, and my doom."

        scene bg bad ending with fade
