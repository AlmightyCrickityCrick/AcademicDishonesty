
define mc = Character("Me", color="#c8ffc8")

label caught_ending:

    scene bg hall_first_floor

    "And directly into another kid (Viorel) lectured by a security guard..."

    "Seems like my reverse-burglar life was over..."

    "In a fraction of a second, the guard looked into my direction, made eye contact and schooled his expression into an ever deeper frown."

    "Dishonor to the family it was!"

    "Dishonor with a flavor of with a brand new and laminated suspension notice, with no scholarship and no placinte from granny to at least alleviate the pain of failure, but..."

    scene bg bad_ending

    "Here, my game is over..."
    $ MainMenu(confirm=False)()


label finita_la_comedia:
    "Just as I introduced the password, the room filled with a deafening sound. I felt myself panic, but I couldn’t move."

    "What have I done?"

    "We were so close, just a little further. I turned towards my partners in crime to apologize, but instead of looking at me they were looking backwards."

    "There stood the security guard, looking angrier than the waters of the Pacific in spring."

    scene bg bad_ending

    "And I knew that I was past the point of suspension."
    $ MainMenu(confirm=False)()


label end_1:

    scene bg exam_auditorium

    "I watched as the class filled with students. Some faces were new, some faces were known."

    "I still remembered the friendships I made during the one time I snuck into the university late at night to change my answers for the university exam."

    scene bg good_ending

    "However, for the rest of the world, and even some of my partners in crime..."

    "...that day never existed, leaving both the characters that played pivotal roles in this drama, as well as their lives and secrets, shrouded in shadow."
    $ MainMenu(confirm=False)()


label end_2:

    scene bg exam_auditorium

    $pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

    "I watched in bitterness as my colleagues answered questions at a lecture I didn't care enough to listen to."

    "I tried to concentrate on it, I really did, but Marius' face in the first row kept reminding me of that night. Of what I should have done but couldn't."

    "It had been a week already, the anniversary of FCIM just a day away, and while I hadn't kept tabs on Marius and his friends, I still spoke freely with Maria, 
    Ana and David."

    "Both about the future and about that day."

    "And yet no matter how much I talked, no matter how much I theorized, the baggage of the knowledge that I let someone like Marius roam innocently..."

    "...with no penalty, with no consequences for his past, present and future actions, it weighed me down, it drowned me in guilt."

    show serious_david at pos with dissolve

    David "If you feel like choosing justice over friendship, do it. It's not worth it to shield friends, if it kills you."

    hide serious_david

    menu:

        "Make things right in detriment to all":

            scene bg bad_ending

            "And so today, I'd finally decided to execute my last plan, to burn all bridges and let light shine on the truth."

            mc "I was going to make things right one last time!"

            "I thought as I clutched  to my chest the laptop with the videogame that I was going to submit for the faculty anniversary, 
            even if the fire of justice burned everyone, including myself."

            "At least it would end with a bang that would make grandma proud."
        
        "Leave it fester":

            "But I am nothing but a coward." 
            "And even as it burns me from the inside out, I'm still too scared to ever tell another soul about my sins."
    $ MainMenu(confirm=False)()


label end_3:

    scene bg exam_auditorium

    "I watched my friends, both old and new, gather around the room as a new semester approached and new subjects were introduced."

    "With a lack of mathematics came a lack of university style reverse-burglaring. And although I sometimes missed that night, 
    I was happy to have gotten scot free from the burning disaster that it was."

    scene bg bad_ending

    "Since that day, lots of things have changed, some friends having remained as a shadow in my memory, while others continued to thrive like succulents in the desert."

    "Would I have changed something, if I knew how’d it turn out? Probably. But what I would never give up, would be the deserved justice."
    $ MainMenu(confirm=False)()


label reprimand_ending:

    scene bg exam_auditorium

    "The morning of the day after the event was a surprisingly quiet one. The lectures continued as usual, professor Bostan returned and began preparing for the FCIM anniversary."

    "Nothing was amiss, nothing appeared to show that someone, anyone knew what happened the night before."

    "And me and my new friends enjoyed the quietness while it lasted. Because as quiet as the morning was, the afternoon turned out to be the beginning of a tragedy."

    "Because just as we were preparing to leave the university, someone entered the lecture hall and asked us to follow them."

    "As we went higher and higher up the stairs and then down the familiar corridor, a feeling of unease settled in the pit of my stomach."

    scene bg receiving_cabinet

    "When we finally arrived at the wooden door of cabinet 317 and knocked, we were asked to enter."

    "There, on the sofa, next to professor Bostan stood no one other than Marius. As our eyes met and his lips spread into a mocking grin, I finally realized what happened."

    scene bg bad_ending

    "He had snitched on all of us."
    $ MainMenu(confirm=False)()


