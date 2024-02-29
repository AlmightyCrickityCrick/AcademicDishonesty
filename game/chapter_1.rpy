define mc = Character("Me", color="#c8ffc8")
define Viorel = Character("Viorel", color="#674ea7", image="characters/viorel.png")
define surprised_David = Character("David", color="#f1c233", image="characters/David.png")
define sad_David = Character("David", color="#f1c232", image="characters/Sad_David_png.png")
define David = Character("David", color="#f1c232", image="characters/Surprised_David.png")
define serious_David = Character("David", color="#f1c232", image="characters/Serious_David.png")
define Marius = Character("Marius", color="#e97782", image="characters/Marius.png")
define amused_marius = Character("Marius", color="#e97782", image="characters/amused_Marius.png")
define smiling_marius = Character("Marius", color="#e97782", image="characters/smiling_Marius.png")
define Ana = Character("Ana", color="#d5a6bd", image="characters/Ana.png")
define unhappy_Ana = Character("Ana", color="#d5a6bd", image="characters/Unhappy_Ana.png")
define Maria = Character("Maria", color="#b4a7d6", image="characters/Maria.png")
define unhappy_Maria = Character("Maria", color="#b4a7d6", image="characters/Unhappy_Maria.png")
define angry_Maria = Character("Maria", color="#b4a7d6", image="characters/Angry_Maria.png")
define Alex = Character("Alex", color="#38761d", image="characters/Alex.png")
define worried_Alex = Character("Alex", color="#38761d", image="characters/Worried_Alex.png")
define Theodora = Character("Theodora", color="#0b5394", image="characters/Theodora.png")
define Guard = Character("Guard", color="#ae1717", image="characters/Guard.png")
define Unknown = Character("Unknown", color="#5b5b5b")
image dueffel_bag = "chapter_1/Dueffel_Bag.png"
image dueffel_bag_inside = "chapter_1/Dueffel_inside.png"
image flashlight = "chapter_1/Flashlight.png"
image smartphone = "chapter_1/Smartphone.png"
image teacher_id = "chapter_1/Teacher_ID.png"
image keychain = "chapter_1/Keychain.png"
image folded_paper = "chapter_1/Folded_paper.png"
image around_table = "chapter_1/around_table.png"
image cock = "chapter_1/clock.png"
image door = "chapter_1/118_door.png"
image crad_reader = "chapter_1/card_reader.png"

default affection = 0
default consumables = 0
default conflict = 0
default met_david = False
default met_marius = False
default id_found = False
default map_found = False
default left_maria = False

init python:
    def collect_consumables():
        globals()['consumables'] += 1
        renpy.hide_screen("consumables_image")
        return

    def random_chance():
        return random.randint(1, 6)

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
            jump cabinet_exploration
    
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

                            $ phone = True

                            show smartphone at pos with dissolve:
                                zoom 0.55
                            
                            "I gently picked up the phone, turning it around a few times and taking it out of its case to see if I could identify the owner."

                            "No such luck..."

                            "I pressed the power button to reveal a pretty unassuming homescreen."

                            "Huh!? No lock???"

                            "I'll have to call someone from the owner's contact list and inform them about the bag once I'm done with this."

                            hide smartphone with fade

                        "Check the ID":

                            $ id_found = True

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
                "Hide under the desk":

                    jump under_desk

                "Hide in the closet":

                    jump hidden_closet

                "Hide in the adjacent room":

                    jump rommates
            
            "To be added"
            
            scene bg classroom_101_night_panic_darkened


label under_desk:
    scene bg under_desk_view

    $map_found = True

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

    jump regroup


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

    $ met_david = True

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

            hide david
        
    jump regroup


label roommates:

    scene bg classroom_101_night_panic

    $pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

    "I dove into the adjacent room, opening the door widely and remembering only a second later that it bangs loudly when it closes."

    "Oh, no!"

    "I was halfway through the beginning of a heart attack, when the door stopped just a sliver away from the frame."

    mc "Huh?"

    scene bg door_crack

    "I came closer to the opening just as a large, brutish man entered the classroom, followed by a smaller student, but I didn’t pay them any mind, too focused on the door anomaly."

    show folded_paper at pos with dissolve

    "I crouched to look closer at what appeared to be a small paper, folded a few times, propping the heavy wood, when I felt a weird breeze against my ear."

    hide folded_paper

    Unknown "Booo!"

    scene bg adjacent_room

    "I nearly jumped out of the door and right back into the classroom when a hand grabbed my arm and pulled me back and further into the room, accompanied by a barely heard chuckle."

    "I turned my head to look at the unexpected companion and froze like a deer in the headlights. I swore that if it continued like that I'll get gray by twenty five."

    $ met_marius = True
    
    show amused_marius at pos with dissolve

    "The visitor was, fortunately, a student. With black hair and dark clothing he blended pretty well with the shadows of the room, if not for the paleness of his face and white of his smile."

    Marius "Sorry. Didn't think I'd scare you this hard."

    "The ghost guy patted my arm before finally letting go. He didn't look sorry."

    menu:
        "Be rude":

            $ affection -= 1

            mc "What the hell was that? Have you lost your mind? There's a guard on the other side of the door!"

            "The guy continued to smile, but his eyes darkened a bit at my words."

            Marius "Yeah, yeah. Spare me the lecture. Let's consider it a lesson for the both of us, shall we? For me about scaring people. For you about staying vigilant."

            "He proposed courteously, before shuffling closer to the door to peek through the crack."

            "I grumbled but decided to drop it."
        
        "Keep calm":

            $affection += 1

            "Annoyance won't help in this situation."

            mc "No offense, dude, but that could have ended really badly for the both of us"

            "The guy didn't stop smiling, but I did see a shadow of remorse cross his face, before he apologized once more, properly."

            hide amused_marius

            show marius at pos with dissolve

            Marius "“I know. And I really am sorry about that. It was childish and unasked for."

            "He shuffled closer towards the door to peek through the crack."

            "I grumbled but decided to drop it and came closer to him, to look over his head. The student and the guard were speaking 
            about something, but I couldn't hear them properly from here."

            hide marius
    
    jump regroup


label regroup:

    scene bg classroom_101_night

    "I froze as people streamed into the room, some speaking quietly, others on the verge of arguing. Four in total, but judging by their attitude, they were not a single group."

    if met_david:
        jump david_and_friends
    elif met_marius:
        jump marius_and_friends
    else:
        jump single_to_mingle

    "How were we going to break into Professor Bostan's cabinet?"
    # TO DO


label single_to_mingle:

    scene bg classroom_101_night

    $pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $pos_left = Position(xpos=0.25, xanchor=0.25, ypos=0.5, yanchor=0.5)
    $pos_right = Position(xpos=0.65, xanchor=0.65, ypos=0.5, yanchor=0.5)

    "I watched as the four separated as predicted, with two approaching a light haired guy with slippers that exited out of a closet, looking pretty shaken." 
    
    "As the others headed to the back of the classroom, straight to another guy, who came out of the adjacent room."

    "Tall. Dark hair. Dressed in black, inconspicuous attire, more like someone you’d expect to break into the university. No slippers."

    "I stood like a statue while they caught up with whatever they had to, before the guy with the dark hair took notice of me and separated from his group with a light smile."

    Unknown "Oho? We got unexpected company?"

    show amused_marius at pos with dissolve

    Marius "I'm Marius, first year, from biotech. Can I assume that you're here for the Math Analysis exam?"

    "I looked slightly stuppored at his hand, before looking around the room once more and frowning. Did everyone here flunk the exam and decide to commit crimes?"

    mc "... First year, software engineering."

    "I introduced myself and shook his hand, before noticing that I haven't answered his question."

    mc "I assume you also failed?"

    hide amused_marius

    show marius at pos with dissolve:
        zoom 0.85

    Marius "No, just woke up from a nap and chose to take a walk through uni."

    Unknown "You know you don't have to throw a jab at David every five minutes, Marius?"

    hide marius

    "I turned around to find myself face to face with two strikingly similar girls in both clothes, as well as in face. Twins?"

    show ana at pos_left:
        zoom 0.55 

    show maria at pos_right:
        zoom 0.6
    
    Maria "I'm Maria, by the way. Nice to meet you!"

    Maria "This is my sister, Ana, and our friend, David. From IA and biotech."

    "She resumed her hostile stance towards Marius."

    hide ana

    hide maria

    show marius at pos with dissolve:
        zoom 0.85

    Marius "Well, I wouldn't be 'jabbing' anyone if we haven't gotten into this situation because of him in the first place."

    hide marius

    show sad_david at pos with dissolve

    "I watched with a puzzled expression as David tried to make himself look smaller from the scrutiny. Wherever he did or didn't do what 
    they were talking about, he looked guilty."

    hide sad_david

    show maria at pos with dissolve:
        zoom 0.85

    Maria "Well it doesn't matter. What's done is done. At least we got the flashlight back, and no one else was caught beside Viorel"

    hide maria

    "Maria stood her position while the David guy mumbled something about the chosen one never being caught from behind her before stopping dead in his tracks."

    "He frantically patted his jean pockets, before bolting towards where the bag was now gone."


    call light_group_conflicts

    show alex at pos_left:
        zoom 0.65

    show theodora at pos_right:
        zoom 0.6

    Marius "Those are Alex and Theodora. Alex is from AI, like the twins here. Theo from Informational Technology. And you are?"

    "I gave him and his group a once over."

    "The Theodora girl seemed friendly enough, although detached, while the Alex guy seemed quite similar to David, fidgeting with the buttons of his shirt. But instead 
    of nervousness, it was energy that seemed to sip out of his pores."

    menu: 
        "Shake hands":

            "I shook their hand and exchanged pleasantries once again with the other group, before the flashlight incident was forgotten and we moved to the actual topic at hand."

    hide alex

    hide theodora

    return


label david_and_friends:

    $pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $pos_left = Position(xpos=0.25, xanchor=0.25, ypos=0.5, yanchor=0.5)
    $pos_right = Position(xpos=0.65, xanchor=0.65, ypos=0.5, yanchor=0.5)

    scene bg classroom_101_night

    "I watched as the four separated as predicted, with two approaching me and David and the others heading to the back of the classroom, straight to another guy, who came out of the 
    adjacent room."

    "Tall. Dark hair. Dressed in black, inconspicuous attire, more like someone you'd expect to break into the university. No slippers."

    "He exchanged a few words with them, before catching my eyes and throwing a charming smile."

    show david at pos with dissolve

    David "So… those were the friends I was speaking about, Ana and Maria, from Automatics and Informatics."

    hide david

    "I gave a small wave to both of them, as I introduced myself, and looked them over."

    show ana at pos_left:
        zoom 0.55 

    show maria at pos_right:
        zoom 0.6
    
    "Both had really similar faces and the fact that they opted for clothing similar to almost everyone else, didn't help distinguish them. Not only that, but also the frowns they wore 
    were also strikingly similar."

    Ana "Thank God you weren't caught. I almost had a heart attack when I saw Viorel come back with the guard in tow into the classroom."

    "The one with slightly shorter hair said to him, before turning to me."

    Ana "I'm Ana by the way. This here is my sister, Maria."

    "The second girl reached out her hand, and I gently shook it, before giving David a light, but annoyed, slap on the shoulder."

    Maria "We told you to go straight to the bathrooms once you retrieve the flashlight. What if Viorel had been caught a minute earlier?"

    "David mumbled something about the chosen one never being caught before stopping in his tracks."

    "He frantically patted his jean pockets, before frantically running towards where the bag was now gone."

    hide maria

    hide ana

    call light_group_conflicts

    "However, the second he looked into my direction, he sighed and lightened his expression."

    show marius at pos with dissolve

    Marius "I'm Marius, from bioengineering. And those are Alex and Theodora."

    Marius "Alex is from AI, like the twins here. Theo from Informational Technology. And you are?"

    hide marius

    show alex at pos_left:
        zoom 0.65

    show theodora at pos_right:
        zoom 0.6
    
    "I gave him and his group a once over. The Theodora girl seemed friendly enough, although detached, while the Alex guy seemed quite similar to David, 
    fidgeting with the buttons of his shirt."

    "But instead of nervousness, it was energy that seemed to sip out of his pores."

    hide alex

    hide theodora

    menu: 
        "Shake hands":

            show marius at pos with dissolve

            "I shook Marius's hand and exchanged pleasantries once again with the other group, before we moved to the actual topic at hand."

            hide marius
    
    return


label marius_and_friends:

    $pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $pos_left = Position(xpos=0.25, xanchor=0.25, ypos=0.5, yanchor=0.5)
    $pos_right = Position(xpos=0.65, xanchor=0.65, ypos=0.5, yanchor=0.5)

    scene bg classroom_101_night

    "I watched as the four separated as predicted, with two approaching a light haired guy with slippers that exited out of a closet, looking pretty shaken, 
    as the others headed to the back of the classroom, straight to me and Marius."

    "Marius greeted the girl and the guy sunnily before turning to acquaint us."

    show alex at pos_left:
        zoom 0.65

    show theodora at pos_right:
        zoom 0.6

    Marius "Marius greeted the girl and the guy sunnily before turning to acquaint us. “Those are Alex and Theodora. Alex is from AI. Theo from Informational Technology."

    "I gave him and his group a once over. The Theodora girl seemed friendly enough, although detached, while the Alex guy seemed to exude energy, as if he were high on sugar."

    Theodora "Honestly, I'm kind of starting to regret this entire spectacle!"

    Theodora "It was supposed to be just a pop in and pop out operation, and yet here we are, going back and forth."

    hide theodora

    hide alex

    show marius at pos with dissolve

    Marius "Relax~"

    Marius "It's an experience. Plus, we'll work this stuff out soon enough, change the tests, and then all go back home. Just a little bit longer..."

    hide marius
    
    "Ah, so he was capable of  something other than sass. Good to know."

    show alex at pos with dissolve:
        zoom 0.8

    Alex "Well we would have probably been home a while ago, if not for David."

    hide alex

    mc "I suppose you're also here for the exams?"

    show marius at pos with dissolve

    Marius "No, they just woke up from a nap and chose to take a walk through uni."

    Unknown "You know you don't have to throw a jab at David every five minutes, Marius?"

    hide marius

    show ana at pos_left:
        zoom 0.55 

    show maria at pos_right:
        zoom 0.6
    
    Maria "I'm Maria, by the way. Nice to meet you!"

    Maria "This is my sister, Ana, and our friend, David. From IA and biotech."

    "She resumed her hostile stance towards Marius."

    hide ana

    hide maria

    show marius at pos with dissolve:
        zoom 0.85

    Marius "Well, I wouldn't be 'jabbing' anyone if we haven't gotten into this situation because of him in the first place."

    hide marius

    show sad_david at pos with dissolve

    "I watched with a puzzled expression as David tried to make himself look smaller from the scrutiny. Wherever he did or didn't do what 
    they were talking about, he looked guilty."

    hide sad_david

    show maria at pos with dissolve:
        zoom 0.85

    Maria "Well it doesn't matter. What's done is done. At least we got the flashlight back, and no one else was caught beside Viorel"

    hide maria

    "Maria stood her position while the David guy mumbled something about the chosen one never being caught from behind her before stopping dead in his tracks."

    "He frantically patted his jean pockets, before bolting towards where the bag was now gone."

    call light_group_conflicts

    "It was about time we moved to the actual topic of the day at hand."

    return     


label light_group_conflicts:

    $pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

    scene bg classroom_101_night

    "He returned back, looking almost guilty."

    show sad_david at pos with dissolve

    David "I didn't get to take the flashlight. It's gone now."

    hide sad_david

    show maria at pos with dissolve:
        zoom 0.85

    Maria "What? You had one job, David. That's literally the only reason we came back here."

    hide maria

    show sad_david at pos with dissolve

    David "I know, I know. Sorry!"

    "He started fidgeting again with his bag."

    David "But its fine, we'll manage without it. We'll find something else."

    hide sad_david

    menu:

        "Share flashlight":

            show flashlight at pos with dissolve

            mc "I could lend you mine. I'm fine with sharing, it's not a problem."

            hide flashlight

            show serious_david at pos with dissolve

            David "You would do that?"

            hide serious_david

            "David raised his hand to his chest, just as Ana threw her hands around me."

            show ana at pos with dissolve:
                zoom 0.7
            
            Ana "Thank you so much!"

            Ana "We owe you. David is a bit ditzy, but he's not a bad guy. He'll grow on you once you get past the awkwardness."

            hide ana

            menu:

                "Compliment David":

                    $ affection += 1

                    mc "He does seem pretty nice. And I've seen people a lot more awkward."

                    show david at pos with dissolve

                    "David looked towards the ceiling, embarrassed. Cute~"

                    hide david

                    show unhappy_maria at pos with dissolve

                    "Maria gave me a look that I wasn't sure how to decipher."

                    hide unhappy_maria

                "Act annoyed":

                    $ affection -= 1

                    mc "Yeah, yeah!"

                    show sad_david at pos with dissolve

                    "David looked even more guilty, if possible, but I didn't pay him any mind. We had to move soon enough if we didn't want to get caught."

                    hide sad_david
            
            show marius at pos with dissolve:
                zoom 0.85
            
            if met_david:
                Marius "Ah, so we do have a flashlight, courtesy to a newcomer."
                "The guy from the adjacent room drawled, as he approached David's group, with a light step but a certain judgment in his expression."
            else:
                Marius "Well, would you look at that?"
                
                "Marius seemed to have lightened up a little after the exchange."
                
                Marius "Good to know we can at least count on our new mafia member to be prepared for this escapade."

            "At least it seemed like it, before he threw one last dirty look towards David."

            hide marius

        "Don't share flashlight":

            $ conflict += 1

            show marius at pos with dissolve:
                zoom 0.85

            if met_david:
                
                "Unsurprisingly for David, we not only have no flashlight, but we also lost a team member."

                "The guy from the adjacent room drawled, as he approached David's group, while David tried to make himself smaller under his heavy glare."

            else:

                Marius "So, unsurprisingly for David, we not only have no flashlight, but we also lost a team member"

                Marius "Seems like we'll have to find something else. Hope you're a more reliable partner-in crime."

                "He turned back to me with a smile after throwing a last dirty look into David's direction."
            
            hide marius

    return


label schemes_crimes:

    scene bg classroom_101_night

    $pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $clock_pos = Position(xpos=0.37, xanchor=0.37, ypos=0.3, yanchor=0.3)

    show around_table at pos with dissolve:
        zoom 0.8

    "Apparently I didn't get the memo about the heist being more of a military operation, because after the moment with the lantern had passed, everyone had taken a chair around a table, 
    as if practiced, with Marius at one head and Ana at the other."

    "Theo quickly found her way to one side, with Alex in tow, just as Maria sat down between Marius and David. Ana motioned slightly with her head for me to take David's 
    other side, and I found myself settling in, just as someone cleared his throat."

    hide around_table

    show marius at pos with dissolve

    Marius "So, we've lost Viorel and his bag of supplies already, and we haven't even moved to the upper floors. What do we do?"

    hide marius

    show theodora at pos with dissolve:
        zoom 0.8

    Theodora "We could just go up already and look at the cabinets ourselves."

    Theodora "It's not like he stays in the basement or something. And the first floor is a dead end at this point."

    Theodora "The guard pretty much knows that there's people breaking in left and right. No point in stalling."

    hide theodora

    show maria at pos with dissolve:
        zoom 0.8

    Maria "There could also be guards upstairs."

    hide maria

    show alex at pos with dissolve:
        zoom 0.8

    Alex "Not could. There are. I hid under the table in the PBL zone and saw one come down and go back up."

    hide alex

    show theodora at pos with dissolve:
        zoom 0.8

    Theodora "Don't forget we should also be mindful of the time we spent searching."

    "She seems to noticing my puzzled expression."

    Theodora "It's currently around 22.10. The gates to the university that you probably jumped to get here close every night at 21.50."

    Theodora "However, what they usually don't tell is that they reinforce them at around 23.30. So we should be gone by then, unless we plan to sleep with the guards."

    hide theodora

    show clock at clock_pos with dissolve:
        zoom 0.8
    
    mc "What do you mean?"

    show serious_david at pos with dissolve

    David "The fence is electric. They power it on after midnight."

    hide serious_david

    "Oh! Oh! OH! oh!?"

    mc "Oh!"

    "It was at this moment that I was glad that I wasn't alone here tonight, because I would have not know about that little detail."

    "Maria took a gulp of her water and nodded to Alex and Theo."

    show maria at pos with dissolve:
        zoom 0.8

    Maria "Then we should be careful on our way up and hurry there already, unless we want however many people are out there to be on the lookout for intruders."

    hide maria

    hide clock

    if met_david or met_marius or id_found:
        jump following_dead
    else:
        jump up_we_go


label up_we_go:

    scene bg classroom_101_night

    $pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

    show smiling_marius at pos with dissolve

    Marius "Then, if everyone agrees, we should pick a stairwell and just go for it."

    hide smiling_marius

    "Ana drummed her fingers on the table and hummed."

    show ana at pos with dissolve:
        zoom 0.8
    
    Ana "We could go by the PBL stairwell, but if Alex saw a guard using it…"

    hide ana

    mc "The lobby stairwell isn't any better..."

    mc "It's probably even riskier, because there's always someone sitting at the entrance, looking at the cameras."

    show serious_david at pos with dissolve

    David "The cameras are shut off though..."

    hide serious_david

    "David is right about that, however…"

    mc "Even if they're shut off, there's most likely someone looking after the front door."

    show ana at pos with dissolve:
        zoom 0.8

    Ana "But if it's the brute who caught Viorel, then he's most likely walking around right now."

    mc "But if there's someone else besides him, we'll have to watch not only our front but also our back."

    "I don't know what else I could say to show how much of a bad idea it was."

    Ana "How much do you think is their budget to hire so many guards? What is this, the president's residency?"

    hide ana

    show marius at pos with dissolve

    Marius "I say we vote."

    Marius "It'll be only fair and we won't lose this much time on arguments. We can't know for sure who's right until we check anyway."

    hide marius

    mc "Alright!"

    menu:

        "But I'm voting for the PBL staircase.":

            $ PBL = True
            $ Lobby = False

        "But I'm voting for the Lobby staircase":

            $ Lobby = True
            $ PBL = False
        
    show ana at pos with dissolve:
        zoom 0.8

    Ana "I'm voting for the lobby one!"

    hide ana

    show maria at pos with dissolve:
        zoom 0.8

    Maria "Lobby!"

    hide maria

    show david at pos with dissolve

    David "Lobby!"

    hide david

    show throdora at pos with dissolve:
        zoom 0.8

    Theodora "PBL!"

    hide theodora

    show alex at pos with dissolve:
        zoom 0.8

    Theodora "PBL!"

    hide alex

    "With only Marius remaining, he sat up and grinned before announcing..."

    if Lobby:
        "Do something"
    elif PBL:
        "Do something"
    # TO DO


# TO DO: Change
screen consumables_image:
    imagebutton:
            idle "chapter_1/clock.png"  
            hover "chapter_1/clock.png"
            action Function(collect_consumables)


label following_dead:

    scene bg classroom_101_night

    # show screen consumables_image

    $pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

    menu:

        "But what about 118?":

            "Everyone turned in my direction."

            show surprised_david at pos with dissolve

            David "What about 118?"

            hide surprised_david
        
    menu:

        "Stay silent":

            mc "Sorry, nevermind!"

            "I dismissed the idea. I had half a mind to explore the PBL zone to look for the map their friend mentioned, but decided against it. Time was of essence here."

            show amused_marius at pos with dissolve

            "If you feel like there's something that's better…"

            mc "No, it's fine, there's not enough time for that."

            mc "We should just go up already."

            "Marius shrugged, but let it go."

            hide amused_marius

            jump up_we_go

        "Tell them about 118":

            if map_found:

                "I took a deep breath and told them about what happened just before the meeting."

                mc "After the guard and Viorel came by, they spoke about a map in 118. If we want to find professor Bostan's cabinet, 
                the map would be our best try."
            
            elif id_found:

                "I took a deep breath and told them about what happened just before the meeting."

                mc "When I climbed into this classroom, just before the guard appeared, I noticed there was a bag on one of the chairs. 
                I wanted to check it out closer, and found the ID of the professor from 118 lying around."

                "I didn't specify where, because that would not have made a good first impression. "

                mc "I think your friend might have gotten it before he was caught. If he did, which is highly probable, there might be something important inside."
            
            "Ana started drumming her fingers on the table."

            show ana at pos with dissolve:
                zoom 0.6

            Ana "I do remember Viorel mentioning finding it once, but if Alex saw a guard in the PBL zone recently, going there would be kind of risky."    

            mc "Not riskier than having to go floor to floor, cabinet to cabinet for God knows how much time, though. Any clue is a good clue if it saves time."

            hide ana

            show unhappy_ana at pos with dissolve:
                zoom 0.8
            
            "She pursed her lips, but didn't say anything."

            hide unhappy_ana

            show marius at pos with dissolve

            Marius "It's worth a try! We don't know how many guards are walking around the building right now."

            Marius "The faster we leave, the better. If his cabinet actually is somewhere on the sixth floor, we won't have enough time to search for it with no additional help."

            hide marius

            show unhappy_maria at pos with dissolve:
                zoom 0.8

            Maria "But it'll still require us to spend more time here, where the guard is already, well, guarded, and we may find nothing after all."

            hide unhappy_maria

            show marius at pos with dissolve

            Marius "But if we don't do this now, we'll be spending more time overall, and we'll risk the guy from the first floor alerting the guards from the upper floor."

            hide marius

            show unhappy_maria at pos with dissolve:
                zoom 0.8

            Maria "Well moving forward is better than moving nowhere at all."

            "A bit too loud for my comfort."

            hide unhappy_maria

            show marius at pos with dissolve

            Marius "Don't forget that we lost Viorel because of your stupid idea to go back for the flashlight."

            "And he should match the tone... The constructive criticism was starting to get out of hand."

            hide marius

            show unhappy_maria at pos with dissolve:
                zoom 0.8

            Maria "So you think that it's my fault?"

            hide unhappy_maria

            show marius at pos with dissolve

            Marius "Yes, if you stuck to the plan and didn't bring your Jesus wannabe boyfriend, we most likely would have been home by now."

            hide marius

            show serious_david at pos with dissolve

            "Even David, who was mostly spacing out till now, winced at that one."

            "Someone had to stop them. I looked around the table, everyone kept their head low and didn't seem to want to interrupt them."

            hide serious_David

            jump peace_duties


label peace_duties:

    scene bg classroom_101_night

    $pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

    menu:
        "Intervene":
            $ affection += 1

            mc "Guys, that's enough"

            "I sat up from my place beside David and settled between the two quarreling students, so they couldn't see each other." 
            
            "Was it a technique for rowdy dogs? Yes. But I was hoping it'll work."

            "I turned to Maria and caught from the corner of my eye a laughing David. Ah, so someone caught onto my maneuver."

            show unhappy_maria at pos with dissolve
            
            Maria "It's not the time or the place to argue about stuff that already happened and can't be changed."

            hide unhappy_maria

            "Seems like luck was at least somewhat on my side today, because they both grumbled, but settled on stopping."

            David "Let's give the cabinet plan a shot. Worst case scenario, we find nothing and we'll just go up through the PBL stairway."

            "I heard David's voice from behind me and thanked him in my mind. If there was someone who could convince Maria, it was him."

            "When I was sure that no one would attack each other again, I took my place back between Ana and David. The same person as in the 
            beginning of the meeting cleared his throat."

            show marius at pos with dissolve
            
            Marius "So, are we all okay with checking out 118 first?"

            hide marius

            menu:

                "Raise Hand":

                    "As six hands rose into the air, I thought to myself that this group might just be more trouble than what I bargained for."

                    jump problem_based_learning
                
        "Don't Intervene":

            $ conflict += 1

            "I could have stopped them. I know I could, but I didn't feel like it was my place to do it, because, at the end of the day, 
            I didn't know those people and what brought on this conflict."

            show angry_maria at pos with dissolve
                    
            Maria "If I didn't bring who? You should be thankful we even considered your little plan."

            Maria "Do you understand how high the stakes are for us? I'm happy with a five on this cursed exam."

            Maria "Ana probably won't get less than an eight. And here we are, risking expulsion, because you 
            needed our help 'in case the cameras were on' and you yourself agreed to let us bring David."

            hide angry_maria

            show marius at pos with dissolve

            Marius "I agreed because I didn't think your little burnout buddy would put my friends at risk, and yet here we are"

            "Marius propped his hands on the table. He was basically half a tone away from shouting at this point, and his friends were starting to look nervous."
                    
            hide marius

            show unhappy_ana at pos with dissolve:
                zoom 0.8
                    
            Ana "Guys, maybe we should all just calm down!"

            Ana "If we continue arguing we won't move anywhere."

            hide unhappy_ana

            if conflict >= 2:

                show angry_maria at pos with dissolve

                Maria "No. I'm not calming down."

                "Maria gave her sister an ugly look and turned towards Marius once more."

                Maria "I'm sick of you always playing the leader when you can't manage to plan your personal life."

                Maria "You know what? You go and have fun in your little cabinet. We're going up and home."

                "She grabbed David's hand and storming towards the door. Then, paused before opening, checked if the coast was clear and then caught my eye."

                Maria "Feel free to join us if you get sick of being bossed around by a loser."

                hide angry_maria

                $ left_maria = True

                menu:
                    "Stay":

                        "And just like that, the two left."

                        "Ana and Marius let out a shaky exhale, with Marius looking positively exhausted from the fight. He turned his head towards the remaining twin and asked:"

                        show marius at pos with dissolve
                                
                        Marius "You're not going with them?"

                        hide marius

                        show unhappy_ana at pos with dissolve:
                            zoom 0.8

                        Ana "Don't worry. You know her. She'll calm down and come back soon enough."

                        hide unhappy_ana

                        show marius at pos with dissolve

                        Marius "Then I assume all who are present are willing to try the plan?"

                        hide marius

                        menu:

                            "Raise Hand":

                                "Four hands were raised into the air, but the absence of the remaining two was stifling."

                                jump problem_based_learning

                    "Leave":

                        "Something"

                        # TO DO: Placating Spirits

            else:

                "There was a stifling second of silence in the room that somewhat reminded me of the stand off during the Cuban crisis. Not a sound was heard. 
                Not a paper was moved."

                "And then with an exhale from both guilty parties, the conflict ended in the same way as the cold war, with a shaky truce."

                show unhappy_maria at pos with dissolve
                        
                Maria "You're right..."

                Maria "We can't afford to lose more time on this."

                "She looked towards an exhausted Marius"

                Maria "We'll speak about this later"

                hide unhappy_maria

                "The guy only nodded his head once and left it down, so his hair covered his eyes. He stayed like that for a moment, gathering his wits, 
                before finally looking at the rest of the table to confirm the plan."

                mc "I assume that all people here agree to go to 118?"

                "Six hands rose into the air, although one of them reluctantly."

                jump problem_based_learning


label problem_based_learning:

    scene bg classroom_101_night

    $pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

    "Now, with the plan decided, it was time to put it in motion. We slowly got up from the desk and put the chairs into place, 
    while Alex ran ahead towards the door to check wherever the path was clear."

    if random_chance() == 1:
        call smooth_sailing
    else:
        call complications

    jump between_door_place

label smooth_sailing:

    scene bg classroom_101_night

    "Fortuna might not have been on our side today, or yesterday, or the other day… But at least the universe decided to show us some mercy."

    show alex at pos with dissolve:
        zoom 0.8
    
    Alex "Coast is clearer than my memory after exams."

    hide alex

    "And although I wasn't sure his memory wasn't clear all the time, considering where he was and why, 
    I decided not prod the fragile group any further."

    scene bg hall_first_floor

    "We walked leisurely, but quietly through the hallway and into the PBL section, stopping right in front of the door."

    "Ana and Marius stood a way back to make sure the guard wouldn't show up and catch us unguarded."

    menu: 

        "Check the door":
            
            "So, here we go!"
    
    return


label complications:

    scene bg classroom_101_night

    $pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

    show alex at pos with dissolve:
        zoom 0.8

    Alex "Guys, it's all fun and games!"

    "...whispered as he frantically looked through the keyhole and back towards us."

    Alex "But the guard is still there and he's moving towards the direction we need."

    hide alex

    "Marius furrowed his brow in concentration, before his face solidified into determination."

    show marius at pos with dissolve

    Marius "We have to use a distraction again."

    hide marius

    "The mood of the people around us soured. It finally clicked in my head."
    
    mc "Wait, so that's how you ended here? David forgot his flashlight and Viorel provided a distraction, but got caught?"

    "When the atmosphere grew even darker, I got my answer."

    menu:

        "Volunteer to provide distraction":

            $ affection += 1

            call playing_heroics
        
        "Abstain":

            call thinkers_live_longer

    return


label playing_heroics:

    scene bg classroom_101_night

    $pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

    "Well, nothing quite like exercising a bit in the evening, I thought to myself."

    "Though, if I were frank, I was just hoping the remains of the conflict would be gone by the time I was back."

    "Not my circus. Not my monkeys. And yet, here we were…"

    mc "I'll do it!"

    "Let's stretching my arms over my head in an attempt to loosen up the muscles in case I had to make a run for it."
    
    "Ana looked at me with a raised eyebrow."

    show unhappy_ana at pos with dissolve
    
    Ana "Are you sure? Do you know what you're supposed to do?"

    hide unhappy_ana

    menu:

        "No":

            "Tutorial time"

            # TO DO: Tutorial

        "Yes":

            "No tutorial"

            # TO DO: Skip Tutorial

    "I nodded and looked as she and Ana moved towards Alex, while Marius came closer to me."

    show amused_marius at pos with dissolve
    
    Marius "So, ready for some adventure, partner in crime?"

    "That cheshire smile that spelled nothing but trouble..."

    "I could only nod, worried about what I’ve just gotten myself into."

    hide amused_marius

    # TO DO: Flashlight Minigame

    scene bg hall_first_floor

    "After getting rid of the guard and finishing the circle around the floor, we finally reached our final destination, panting."

    "At first the space appeared empty and I thought that the others had already gotten into the cabinet, when the surroundings 
    started to move and I started to make out the shapes of my accomplices."

    "I exhaled relieved that we made it, and took a minute to calm my breath."

    menu:
        "Check door":

            "Here we go..."
    
    return


label thinkers_live_longer:

    scene bg classroom_101_night

    $pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

    "I was a thinker, not a fighter, and I had no reason to start a military carrier at this point in time."

    "So I watched as people considered the pros and cons of leaving for the covert operation, before finally 
    Ana and Marius decided to sacrifice themselves for the sake of the others."

    scene bg door_crack_hall_first_floor

    "We watched in silence as the guard drew near the door behind which we were hiding, only to be distracted by a flashing light further down the corridor."

    "It took only a few seconds for him to come close enough to one of the volunteers, before the light blinked twice and disappeared, only to reappear a few 
    cabinets further down the corridor."

    "This dance continued for a while, until we could see neither the guard, nor the lights."

    show worried_alex at pos with dissolve:
        zoom 0.8
    
    Alex "Time to go"

    hide worried_alex
    
    "We quickly opened the door and started to move towards the PBL section."

    scene bg hall_first_floor

    "Running on pure adrenaline, even with no guard in sight, we only stopped when we finally reached the door for cabinet 118."

    "The others took cover under the tables in the hall, while I caught my breath right in front of the glass."

    menu:

        "Check Door":

            "Here we go..."
    return


label between_door_place:

    scene bg pbl_hall

    $ pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.43)
    $ door_pos = Position(xpos=0.48, xanchor=0.48, ypos=0.43, yanchor=0.43)

    show door at door_pos with dissolve:
        zoom 0.3
    
    "The door was made fully out of glass with only the handles and the frame showing a metallic shine."

    "And while the view shouldn't be this familiar because we haven't exactly spent much time at university this year, it still brought a bit of nostalgia."

    "I hoped that at least after the anniversary we'd get to switch again to full on-site education."


    show theodora at pos with dissolve:
        zoom 0.8
    
    Theodora "Did you fall asleep out there, or?"

    "Theodora's voice broke my trance and I remembered where I was."

    hide theodora

    "Right, we were here to commit crimes, not to cry over ruined university experiences."

    "I took a second look, this one less sentimental, and tried to understand how it's locked."

    menu:

        "Check for keyhole":

            hide door

            show door at pos with dissolve

            "Alright, if the previous cabinets had keyholes, this probably meant that this one should too, right?"

            "Wrong."

            "I checked all sides, and yet there was no sign of one ever existing here."

            hide door
        
        "Check for card lock":

            hide door

            show card_reader at pos with dissolve

            "I searched for a cardlock, and sure enough, just behind the handle was a small crack, just enough to slip in a card… or something of similar shape."

            hide card_reader
        
        "Check for fingerprint scanner":

            "I had half a mind to check for a fingerprint scanner but caught myself halfway through."

            "We may be roleplaying Hitman, but this was not a game."
        
    hide door

    "I stopped the investigation and told the others of my findings."

    mc "Yep, it's using a card lock."

    if id_found:

        "Easy way"

        # TO DO: The Easy Way In
    
    elif left_maria:

        "Friends?"

        # To DO: Friends With Benefits?
    
    else:

        "Impossible"

        # TO DO: Mission Impossible
    
    return

        

# show at pos with dissolve



        










    
