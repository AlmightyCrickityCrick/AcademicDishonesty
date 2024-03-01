label patrolling_together:
    # TODO scene
    scene bg second_floor_hall light

    "We went back down the corridor we initially had come from in a light, but tangible silence."
    "Marius kept humming to himself from time to time, but hadn't said a word."

    "At last, we went back far enough to reach a fork. Marius opened the door of one of the classrooms in mock cordiality, and I took him up on the offer, entering the room, and finding myself a seat with enough visibility to notice any passerby."

    "Marius closed the door after himself and sat down next to me, propping his legs on another chair."
    "For someone who was dead by the time we reached our destination, he was acting pretty happy."

    scene bg classroom 315 night

    "I decided to remark after he started humming his tune for the fourth time."
    mc "You're awfully bright"

    show marius
    Marius "Why yes, I quite pride myself on my intelligence" 
    hide marius

    "I thought about dropping the topic if he wanted to play stupid games, but decided to push him more just this once."
    mc "Seriously, did something good happen?"

    "He finally looked at me with the same warm smile he began the evening with."
    show marius
    Marius "It's just life has finally started looking up. Once we get this whole ordeal done and over with, we'll finally be free."
    hide marius

    "I joked"
    mc "From the horror that is the exam?"

    show marius
    Marius "Not only, we'll be finally leaving behind the preparatory year and we'll be working on research and projects that we finally care about, that finally matter."
    hide marius

    "Oh."

    mc "Guess you're really looking forward to work, huh?"

    show marius
    Marius "You could say that."
    hide marius

    "He switched his focus towards the corridor. Right. We were on a job."

    show marius
    Marius "What about you? Do you have any plans, any dreams for the future, or are you here just to pass the time?"
    hide marius

    "I looked at him and wondered wherever I wanted to share this information."
 
    menu: 
        "Share":
            $ m_affection = m_affection + 1
            $ shared_info = True

            "I hesitated. I thought about whether I trusted him enough to speak about this topic, but the puppy eyes he kept throwing at me the longer the silence lasted, made me concede."

            "I sighed loudly and closed my eyes before speaking, so I didn't have to see his expressions."
            mc "It's probably going to sound dumb, but I'm here because I wanted to see how much I could push the line of impossible." 
            mc "A lot of people keep speaking about how we've progressed so much in the past few years, how we've already hit the ceiling when it comes to technology, without even noticing that the time for invention, for innovation is right now."
            mc "The fact that there's so many things appearing on the market both as products and as prototypes means that there's a lot more tools to experiment with, to create on, to build with. And sorry, I'm probably not making much sense right now…"

            show marius
            Marius "No, no. I understand what you're trying to say. And if you are dumb for wanting to make out something bigger of your life, contribute to the evolution of our lives, then so am I."
            


            "I looked at him surprised."
            "He only answered with the same warm smile and looked up, as if he could see something far away."

            Marius "There's room for creation. Room for experimentation."
            Marius "There's no rules about what you can and can't do in tech if you set your mind to it. As long as you work hard and dedicate yourself to your project, anything is possible."

            "I chuckled."

            mc "Well, good to know there's still idealists among us." 
            hide marius
            "The door opened and a panting David entered."
        "Abstain":
            $ m_affection = m_affection - 1
            show marius
            mc "I don't know yet, I haven't given it much thought. Guess I'm just passing the time and seeing what life throws at me."
            "He looked at me with a hurt expression"
            "We both knew that I was lying."
            "But neither I corrected my words, nor he inquired further."

            Marius "Fair enough"

            Marius "You'll find your path some day."

            "And then there was quiet. For a long while. Neither he, nor I spoke."

            "The quiet tethered on the balance between comfortable and uncomfortable, but neither dared disturb it."

            "Only when David opened the door, did we speak once again."

            hide marius

            show david

            David "Are you guys done already?"
            hide david

            show marius
            "Marius rose from his seat and greeted the light haired guy, as if nothing happened."

            Marius "Yeah"
            Marius "We found the file with the tests and changed them."
            Marius "Make sure to put it back onto the upper right shelf."
            Marius "It was between last year's taxes and this year's homework"
            hide marius

            mc "Thanks. Are you leaving already?"

            David "Yeah. The girls went ahead to hunt for the guard. Please hurry. We have to leave pretty soon if we don't want to get stuck."

            "I nodded and followed David and Marius back to the cabinet."

            jump the_culmination

label the_culmination:
    scene bg classroom 315 night

    "The cabinet looked even smaller from the inside, so Marius agreed to courteously wait outside for David to show me the ropes."

    "I watched as the chosen one' sorted through the tests quickly, checking out the names, until he finally pulled my paper."

    show test

    "He was polite enough not to stare into it too much, but I still saw him cringe at my scribbles."
    mc "Don't hold back on me. It's alright to laugh. I haven't prepared at all."

    hide test

    "A shadow of guilt crossed his face before he spoke"

    show david

    David "Then it's good that Father guided you here today. Everything happens for a reason. You might have failed your test, but you helped us change ours."

    menu:
        "Agree with this view":
            $ d_affection = d_affection + 1
            mc "I guess God really does look after you"

            "David positively beamed."
            "He'd have to get rid of his delusion one day, but that day was not today. And I was not the person to do it. He'd have to take that step on his own."

        "Disagree with his view":
            $ d_affection = d_affection - 1

            mc "You know you shouldn't speak like that about God? Or distort the concept of destiny to fit your narrative. What happened, happened."

            "However, I felt like I kicked a puppy when I looked towards him and caught the hurt in his eyes, before he schooled his expression into an easygoing smile."


    hide david

    mc "Alright, back into the stack it went" 
    "I went, as I put the fresh, new and correct sheet back into the pile."

    show marius
    Marius "Are you guys done?"
    mc "Yes, we're done."
    "I confirmed and exited the room with David in tow, speaking about the plans till the next semester."

    scene bg second_floor_hall light

    "We walked a few steps ahead, to give Marius some privacy, when David suddenly stopped and the same unrecognizable look crossed his face again."

    "I also paused, worried that he might have been feeling unwell"

    mc "Is everything alright?"

    if d_affection < 7:
        "David shook his head, smiled, and said “No, I'm fine.”, just as Marius caught up to us."

        show marius
        Marius "Alright guys, the tests are home, we are free and can finally go get some sleep."
        Marius "Hope I'll have the occasion to hang out with you once more, but without committing crimes."
        hide marius

        "We stealthily exited the university, having accomplished our goal. And indeed, everything was fine, we came out of this battle victorious. And yet, I couldn't help but feel as if I've missed something really important tonight."
        jump end_1
    
    if d_affection >= 8:
        jump bad_feelings