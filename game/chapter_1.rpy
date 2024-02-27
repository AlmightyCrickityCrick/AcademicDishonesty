image dueffel_bag = "chapter_1/Dueffel_Bag.png"
image dueffel_bag_inside = "chapter_1/Dueffel_inside.png"
image flashlight = "chapter_1/Flashlight.png"
image smartphone = "chapter_1/Smartphone.png"
image teacher_id = "chapter_1/Teacher_ID.png"
image keychain = "chapter_1/Keychain.png"

define mc = Character("Me", color="#c8ffc8")
# define Bostan = Character("Professor Bostan", color="#1675c2", image="viorel")

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
    Get into uni. Find professor Bostan’s cabinet. Leave."

    scene bg classroom_101_night_panic_darkened

    "However, as I gazed around the room, I could feel a slight panic rise in me. This was 
    madness. How was I going to even do this? "

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

                    "As I picked it up, carefully, I noticed that it wasn’t a particularly heavy one either, despite its bulging form. But, 
                    after rotating it, I noticed a funny looking charm tied to it."

                    show keychain at pos with dissolve

                    "Still no idea who it belonged to, or why it was there, though."

                    hide keychain at pos with fade
                
                "Check Inside":

                    "“Well, it seems like I'm already on the path to crime, might as well commit another one.”"

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




    
