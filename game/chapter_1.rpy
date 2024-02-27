define mc = Character("Me", color="#c8ffc8")
define Viorel = Character("Viorel", color="#674ea7", image="characters/viorel.png")
define surprised_David = Character("Surprised David", color="#f1c233", image="characters/David.png")
define David = Character("David", color="#f1c232", image="characters/Surprised_David.png")
define Guard = Character("Guard", color="#ae1717", image="characters/Guard.png")
define Unknown = Character("Unknown", color="#5b5b5b")
image dueffel_bag = "chapter_1/Dueffel_Bag.png"
image dueffel_bag_inside = "chapter_1/Dueffel_inside.png"
image flashlight = "chapter_1/Flashlight.png"
image smartphone = "chapter_1/Smartphone.png"
image teacher_id = "chapter_1/Teacher_ID.png"
image keychain = "chapter_1/Keychain.png"

define affection = 0

label breaking_and_entering:

    scene bg classroom_101_night_darkened

    "My heart beat fast as I climbed over the windowsill on the first floor 
    and dropped onto the floor."
    
    "The darkness of the night clouded my movement for now, 
    but the longer this breaking and entering plan took, the more chances were that I 
    would be caught."

    "After the disaster of an exam, I went back to my room and worked on the plan. It 
    seemed easy enough in its concept."

    "Wait for the night. Find that one window on the first floor that no one can close. 
    Get into uni. Find professor Bostan's cabinet. Leave."

    scene bg classroom_101_night_panic_darkened

    "However, as I gazed around the room, I could feel a slight panic rise in me. This was 
    madness. How was I going to even do this?"

    "Here I was standing inside the university, at night, with nothing but my phone, keys, 
    and some flashlight and rope that I picked for God knows why, hoping to break into a cabinet 
    to replace a test sheet."

    "If my family ever learned about this, my mom would have a heart attack and my dad would disown me. 
    Even grandma would be ashamed… Actually, no, grandma would cheer me on, probably. She always did have 
    a bone to pick with authorities."

    scene bg classroom_101_night_darkened

    "So, no more hesitating. If I did end up taken by the police after this, I had to at least make her proud. 
    Or at least proud enough to get invited to family dinner…"

    "I took a deep breath. No more thinking about grandma."

    "First things first, I had to calm down and start looking around the university. I was already past the point of 
    no return. If I wanted to sob my eyes out and play the middle school freshman I could have just stayed home and saved 
    myself the trouble."

    menu:
        # TO DO
        "Leave the Room":
            "Time to put on my big college student pants. If I wanted to find his cabinet, I had to leave this room and actually 
            move through the building to locate it."

            "So, without waiting for another minute, I held my head high, moved my bag to a more comfortable position, and walked 
            straight out of the door."

            "To be added"
        "Look around":
            "To be added"
    
    scene bg classroom_101_night_darkened

label cabinet_exploration:

    scene bg classroom_101_night_darkened

    $pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

    "It was time to put on my big college student pants. If I wanted to find his cabinet, I had to start by actually observing my 
    surroundings and making a route as stealthy as possible around the building."

    "So I shook off the last of my nerves and took a good look around the classroom I've landed in."

    scene bg classroom_101_night

    "The room appeared the same as during the day, although with less students, making it seem kinda eerie in the way it appeared 
    almost abandoned under the current lighting. The whiteboard still had the same writings on it."

    "The projector turned off, with the cap missing as always. The desks still slightly scribbled, as if someone gave up halfway through 
    erasing the doodles, with the chairs all in the risen positions."

    "No, not all chairs. There, closer to the middle, one seemed to have had something keeping it down."

    menu:
        "Check":
            "I slowly and carefully made my way over to the chair, with each step bringing the object more and more into the view, 
            until I was face to face, well, knee to face, with my findings."

            "It was a… bag? "

            show dueffel_bag at pos with dissolve:
                zoom 0.7
            
            "Indeed, on closer inspection, there, on the seat, unperturbed, sat a brown duffel bag."

            "I might not have been a bag connoisseur, but I did know a thing or two about them. And this did not seem to be a cheap one."

            "But who would have left it here? And why?"

            menu:
                "Check Outside":

                    "As already a symbolic member of the breaking-and-entering community, I decided I was too chicken to commit two crimes in 
                    the same night, so I just studied the outside of the bag."

                    "It wasn’t leather, or any particularly known brand of expensive bags, but it still seemed to have a pretty solid build."

                    hide dueffel_bag

                    "As I picked it up, carefully, I noticed that it wasn't a particularly heavy one either, despite its bulging form. But, 
                    after rotating it, I noticed a funny looking charm tied to it."

                    show keychain at pos with dissolve

                    "Still no idea who it belonged to, or why it was there, though."

                    hide keychain at pos with fade
                
                "Check Inside":

                    me "Well, it seems like I'm already on the path to crime, might as well commit another one."

                    "I gathered some courage, looked around to make sure no one could see me, before slowly unzipping the biggest compartment"

                    "Huh..!?"

                    hide dueffel_bag

                    show dueffel_bag_inside at pos with dissolve:
                        zoom 0.6
                    
                    "Within it was a light colored gym uniform, a bottle of water and some personal stuff, like a phone, an ID, and, interestingly enough, a flashlight."

                    hide dueffel_bag_inside

                    menu:
                        "Check the flaslight":

                            show flashlight at pos with dissolve:
                                zoom 0.7
                            
                            "I took a closer look at the flashlight, taking it into my hands and rotating it around."

                            "It was a nice one that showed the charge of the batteries on one side. Didn’t tell me anything about the owner though."

                            hide flashlight with fade


                        "Check the phone":

                            show smartphone at pos with dissolve:
                                zoom 0.55
                            
                            "I gently picked up the phone, turning it around a few times and taking it out of its case to see if I could identify the owner."

                            "No such luck..."

                            "I pressed the power button to reveal a pretty unassuming homescreen."

                            "Huh!? No lock???"

                            "I'll have to call someone from the owner's contact list and inform them about the bag once I'm done with this."

                            hide smartphone with fade

                        "Check the ID":

                            show teacher_id at pos with dissolve:
                                zoom 0.55

                            "I took the ID out of the bag and turned it over to see who the mysterious student was."

                            "However, upon inspection, the ID didn’t seem to belong to a student, but to the nice professor from 118."

                            "Just how in the seven hills of Chisinau did that end up in the hands of a student?"

                            menu:
                                "Take ID":

                                    "Would stealing something already stolen make someone more of a criminal? I decided that I’m already racking up charges, might as well add one more."

                                "Leave ID":     
                                    "I put the ID back where I found it. Better not get caught with stolen school property."       

                            hide teacher_id with fade
            
            "Now, we might not have had the past semesters on site, but I was pretty sure full bags must not have been a common object to forget after hours."

            "Or even if forgotten, the cleaning lady either would have brought it to 'lost and found', or its owner would have shown up at some point in time, 
            before the university gates' closing, to grab it."

            "Which meant that the bag had been brought here recently. And that I wasn’t the only person breaking and entering tonight."

            scene bg classroom_101_night_panic_darkened

            "Just as I scrambled to put everything the way it was, I heard voices from the corridor. One of them for sure not belonging to a student, but to someone older, 
            bigger."

            "A security guard."

            "And they were getting closer by the second. I had to make a quick decision."

            menu:
                # TO DO
                "Hide under the desk":

                    "To be added"

                "Hide in the closet":

                    "To be added"

                "Hide in the adjacent room":

                    "To be added"
            
            "To be added"
            
            scene bg classroom_101_night_panic_darkened

label under_desk:
    scene bg under_desk_view

    $pos_left = Position(xpos=0.1, xanchor=0.1, ypos=0.5, yanchor=0.5)
    $pos_right = Position(xpos=0.9, xanchor=0.9, ypos=0.5, yanchor=0.5)

    "I immediately dove under the closest desk, just as the door opened and two people walked in."

    Unknown "The sheer audacity of breaking into a public academic building… If I were the one deciding your fate, you would have been expelled immediately."

    "A large, brutish man chastised a much smaller student, as they both stopped just in front of the door."

    show viorel at pos_left:
        zoom 0.8 

    show guard at pos_right:
        zoom 0.8
    
    with dissolve

    "I vaguely remembered seeing their faces before, but couldn't be sure when or where."

    "The student hung his head low, looking as shaken as one could be after being caught committing a crime."

    "The brutish man didn't look pleased by the current situation either. He motioned to the student to continue further into the room, 
    as he made himself more comfortable by the door."

    Guard "Grab your stuff. You'll be hearing from the dean. You better pray he'll be merciful with your punishment."

    "It took me a second to process that he was referring to the bag. That was literally right next to me."

    "Oh! Oh no!"

    "I slowly crawled my way further up, away from the desk with the bag, as the student neared it. I held my breath and tucked my legs closer 
    to myself once he reached it, feeling big despite how cramped my position was."

    "The student took a look at it, fumbled a bit and then mumbled under his breath. Did he notice I went through it?"

    Guard "WHAT? SPEAK LOUDER!"

    Viorel "I said I'm sorry. I just forgot my project in 118."

    Guard "Should have gotten it tomorrow, instead of trespassing."

    "The student nervously picked at the straps of the bag as he continued."

    Viorel "It's a map of the building. For the anniversary. I haven't finished it yet and it's due tomorrow."

    Guard "Kid, tomorrow you'll have more to worry about than the anniversary."

    Guard "Now stop standing there and get over here. Can't wait to get this day over with. It's all those cursed cameras."

    "The student stopped muddling around and walked his way back towards the door, before leaving the room with the guard behind him, 
    escorting him like a prisoner of war."

    hide viorel

    hide guard

    with fade

    "I waited a few seconds before getting out of my hiding spot, and walked back towards the center of the class."

    "Well this was unfortunate. A close call. Most likely the first of many tonight."

    "I'd have to be more careful, more stealthy, if I wanted to make it into professor Bostan's cabinet and back home 
    without getting caught. No reckless decisions, no playing hero."

    "Just a simple in and out. Like a ninja. Like a shadow. No one shall see, and no one will know that I've been here tonight."

    "And just like that, ironically, the moment I finished that thought was also the moment several other doors, including the door 
    the guard just left through, opened simultaneously."

    scene bg under_desk_view

    #TO DO

label hidden_closet:

    $pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

    scene bg keyhole_peer

    "I dove into the nearest closet and glued my eye to its keyhole, just as the door to the classroom opened and a large, brutish man entered, 
    followed by a smaller student."

    "Both of them looked miserable, though for different reasons. While the student looked as if he was caught with a hand in the cookie jar, 
    the guard gave off the vibe that he was not paid enough to handle whatever happened."

    "I focused on the movement of the two, with the student going towards his bag, as the guard settled more comfortably by the door. 
    But just as the man opened his mouth to speak, I heard a muttered from my right."

    Unknown "What the?"

    "Too close for comfort."

    "I whipped my head to the side."

    scene bg closet

    show surprised_david at pos with dissolve

    "it seemed he was ready to scream bloody murder!"

    mc "Please don't shout"

    "The student froze, I could physically see him processing my request and the situation we were in, before his shoulders relaxed and he took 
    a deep breath."

    "Once settled, he whispered back, in a more laid back manner than his initial reaction suggested he was capable of."

    hide surprised_david

    show david at pos with dissolve:
        zoom 0.8

    David "Sorry… Panicked there for a second."

    "The mystery student gave me a sheepish smile and offered his hand."

    David "David, from bioengineering, first year. Nice to meet you."

    "I took a look at him. Light hair. Average stature. Cross on his neck. Nothing unusual, except he was wearing the university's shirt with puffy 
    slippers, as if he just ran out of the dorms and randomly decided to commit crime on his way to grab dinner."

    "Yep, this one spelled trouble for me. Lots of it. And not the founding a criminal syndicate kind. More like the sticking a fork into an outlet one."

    "If this wasn't just my luck."

    menu:
        "Shake hands":
            
            "I sighed, shook his hand."

            mc "..., software engineering. First year as well."

            "Ok, turning back towards the keyhole and the caught student."

            hide david

            scene bg keyhole_peer

            "Thankfully, both were still speaking about something, with the student rummaging through his stuff, unaware of the exchange from the closet."

            scene bg closet

            show david

            "The slipper guy distracted me from my espionage mission once more, as he took me by my shoulders, turned me around, stuck his face far too close 
            for my comfort in a pandemic, and narrowed his eyes in thought, before pointing with both hands at me."

            David "You're the bolt."

            "He seemed a little too satisfied with his discovery, while I furrowed my brows. The what?"

            "David saw that I understood nothing from the exchange after I failed to give whatever answer he was waiting for and supplied another clue."

            David "From the Numerical Analysis exam?"

            "Nope, still nothing."

            David "I was sitting behind you? You sprinted to your place like a madman?"

            "Ah, this finally rang a bell and this time it was my turn to look embarrassed. I didn't consider that people would take notice or remember what 
            I did in my desperation."

            "Anxiety was one hell of a distraction. Speaking about distractions…"

            menu:

                "Hostile":
                    $ affection -= 1
                    
                    mc "What the hell are you doing here, in a closet, at this hour?"
                    
                    "We were alone, in a dark closet room, hiding from the security, because we were committing something extremely illegal. And yet here the 
                    guy went, speaking in vain and risking attracting attention."

                    David "Oh! Sorry. I didn't want to upset you."

                    "He fumbled for a bit with the zipper of a bag that I haven't seen until now, before actually answering"

                    David "Sneaking into the university?"

                    "Ah yes, and I was here selling pies and meeting Queen Elisabeth."

                    "The guy must have caught on to my annoyance because he quickly backtracked."

                    David "Sorry. I'm trying to sneak into Professor Bostan's cabinet. I kinda didn't prepare for the exam, because ours was tomorrow, so I'm trying to change my answers…"

                    "Well, I'll be damned. Like they say, geniuses (or idiots) think alike."

                    mc "Yeah... Ok! I'm here for the same reasons. Seems like it was just one of those bad luck days for quite a few people, huh?"

                    "I tried to lighten my voice at the end, and he must have understood."

                    David "Seems like it..."
                
                "Friendly":
                    $ affection += 1

                    mc "Yeah, I might have embarrassed myself a little today."

                    David "No, no, it's fine. I don't think anyone else noticed. I was just fidgety, so that's why. Don't worry."

                    "He seemed like a pretty nice guy, although a bit awkward."

                    mc "...But what are you doing here at this hour?"

                    David "Oh!"

                    "He seemed to have finally realized properly where we were and what we were doing."

                    David "Uhm, I've actually flunked Mr. Bostan's exam today and thought, if he was leaving for a few days, I could have the chance to change my answer sheet?"

                    "His explanation somehow turned into a question at the end, but I caught the meaning. Seems like I wasn't the only person whose second resort to failing 
                    a test was burglary."

                    mc "Same actually. Seems like we'll be partners in crime tonight?"

                    "He laughed quietly, and gave a sound of accord, before fiddling with a bag I haven't noticed on him before."
            

            scene bg keyhole_peer

            "Considering this conversation kinda finished, I turned towards the door to check the keylock once more, only to confirm that the student and the guard were long gone now. 
            Finally, freedom."

            scene bg classroom_101_night

            mc "So, are you here alone, or..?"

            "I opened the door of the closet and stepped out and into the classroom once more, closely followed by David."

            David "Not really. “I've actually been roped into this by a few friends."

            "A few other doors opened."













    
