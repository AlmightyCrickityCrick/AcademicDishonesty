define Marius = Character("Marius", color="#4c4fd4", image="Marius")
define Ana = Character("Ana", color="#75cc69", image="Ana")
define Maria = Character("Maria", color="#979c4c", image="Maria")
define Theodora = Character("Theodora", color="#d4604c", image="Theodora")
define David = Character("David", color="#ac619f", image="David")

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

    $ key = False #TODO should be removed
    menu:
        "Hide in FAFcab":
            jump privileges_used_for_evil
        "Hide in physics lab" if key == True:
            jump a_different_kind_of_lab
    jump scatter

label privileges_used_for_evil:
    "I dove towards the FAFcab, taking out the key out of my pocket, for once grateful not to have it on a ring, and turned the lock open."

    scene bg fafcab room night

    "In less than a moment we were all huddled on the opposite side of the door, breathing heavily, and listening to the guard whistle a tune."

    jump from_bad_to_worse
    jump bad_situations_require_bad_solutions

label a_different_kind_of_lab:
    "asdfsgbg"

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