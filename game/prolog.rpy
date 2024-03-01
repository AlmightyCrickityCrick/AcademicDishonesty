
define mc = Character("Me", color="#c8ffc8")
define Bostan = Character("Professor Bostan", color="#1675c2", image="characters/viorel")
image laptop = "prolog/laptop.png"
image openBinder = "prolog/binder.png"
image test = "prolog/test.png"
image whiteboard = "prolog/whiteboard with lock_screen.png"
image inky = "prolog/inky_screen.png"
image cameraOff = "prolog/camera_off.png"

# The game starts here.

default full_password = False

label prolog:

    scene bg mc_room_morning

    $ charcenter = Position(xpos=0.2, xanchor=0.5, ypos=0.7, yanchor=0.5)
    show laptop  at charcenter  with fade :
        zoom 0.8

    "{size=-10}The laptop cast a bluish light around the dark room, highlighting the stack of unopened programming textbooks, 
    mountain of unwashed coffee mugs and the bundle of blankets that separated me from the mental breakdown that I 
    had been teetering on the edge of for the past 15 minutes.{/size}"

    "All because of one unfortunate little email."

    "“Magnetic storm… Faulty electronics… International conference…”"
    "I could feel myself die a little as I tried to make sense of the announcement through a blurry vision."

    "“...Professor Bostan invited. Schedules for next week shifted. Laboratories awaiting further grading.”"

    "I reread it again."

    "And again."

    "And yet no mention about the upcoming Mathematical Analysis exam, except for one cursed line."

    "“The test will be 80\% of the final grade. Reexamination in august. Rescheduled for tomorrow.”"

    hide laptop with fade

    "I was screwed. Royally. Wholly. Contract-switchingly, wallet-bankruptingly screwed."

    "I closed my eyes and let out a heavy breath."

    "Ten hours till doom."

    "How could I spend them?"



    menu:
        "Go to sleep and test my luck":
            jump feeling_lucky

        "Try cramming a last night of study":
            jump futile_preparations
        
        "Come up with a plan":
            jump middle_of_night_scheming

    scene bg mc_room_morning

label feeling_lucky:

    "{size=-10}Professor Bostan always said that there's no point in preparing for an exam twelve hours before it. 
    Moreover, most of his exams have always consisted of both essay questions and multiple choice ones.{/size}"

    "{size=-10}So, with a bit of luck, I'd be able to score just enough to pass and then correct my grade next semester.{/size}"

    "But is it really a good idea to push my luck today?"

    menu:
        "I only live once. Might as well wing it today.":

            "{size=-10}If the probability of having multiple choice questions is above 50%, 
            the quiz itself amounts to about 30% of the grade for the test, each question has 3 wrong answers, 
            with one of them being super wrong and obvious, and the grading usually follows normal distribution…{/size}"

            "That leaves me with a 25% probability of receiving a passing grade"

            "Which was higher than the chance of Hitler invading Czechoslovakia."

            "So while not ideal, it was still a pretty good chance in my book."

            jump prolog_bad_end

        "Better not risk it.":
            "Let's be honest here."
            "I know myself." 
            "I know my luck."
            "And I know that my luck is on par with the luck of Archduke Franz Ferdinand on the day of his assassination."
            "Which meant that winging it was not an appropriate solution and I had to figure out something else."

            menu:
                "Come up with a plan":
                    jump middle_of_night_scheming

label futile_preparations:
    "This is okay."

    "It isn't the first time I've had to study what we'd been learning for 3 months in one night."

    "I have managed to do it before, I would manage to do it today."
    "Will this be hard? Yes."
    "Will I barely scrape the surface of the material? Yes."
    "But it should be enough to get me by with a passing grade, if I start within the next 10 minutes…"
    "…"
    "Except when I turned to open the textbook, I knocked over one of the study guides and my stomach sank."

    $ pos = Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    show openBinder at pos with dissolve
   
    "The deadline for the last laboratory work for the database course was also tomorrow."
    "And the grades were to be based solely on this laboratory."
    "Worse, it was an implementation and design laboratory."

    hide openBinder with dissolve

    "There was no way I'd be able to both prepare for the exam, and do the lab tonight."

    menu:
        "Come up with a plan": 
            jump middle_of_night_scheming

label middle_of_night_scheming:    
    scene bg mc_room_morning

    "My entire major could have been summed up in two sets of skills: problem solving and stuff building."
    "And while I was not particularly proficient in either, I could still muster up enough brain cells to build a plan to figure my way out of this one."

    "At least I hoped I could."

    jump morning_before_exam

label prologue_bad_end:
    scene bg exam_auditorium

    "I felt my face get clammy and my palms get cold the more I waited for the introduction before the exam to end."

    scene bg mc_room_morning faded

    "{size=-10}When I woke up this morning, feeling nothing but exhaustion and anxiety for the test to come,
    I could neither cram a last perusal of lecture notes, nor eat anything.{/size}" 

    "I'd decided to put all my bets on luck and had hoped that fortune smiled at me at least today."

    scene bg exam_auditorium

    "However, as the clock on the wall continued its quiet tick tock, I felt myself slipping deeper and deeper into the waters of despair."
    "Why didn't I study?"
    "How was I going to wing this?"
    "I had no plan."
    "I had no powers to concentrate enough to think of one."

    "I watched as professor Bostan finished up his discourse and took out the papers from his briefcase."
    "As he went through the rows and distributed the sheets, I prayed to any Gods I knew that it was multiple choice or at least contained a 
    multiple choice section."

    "Once he reached my seat and handed me my test, I took it with a trembling hand."
    "I closed my eyes before turning it, praying for that section."

    show test at center with dissolve:
        # # xpos 700 
        ypos 1050
        zoom 0.7

    "Only to lose all hope."
    "It was not multiple choice."
    "It didn't even have a small section of answers to select from."
    "All items were essay types."
    "I felt my eyes well up and defeat settle deep in my bones."
    "This was the end of a TUM student."

    hide test with dissolve

    show bg bad ending with fade

label morning_before_exam:
    scene bg mc_room_morning

    "I barely managed to open my eyes when the alarm sounded, exhausted both physically and morally."
    "{size=-10}The night passed in a blur leaving me feeling as if someone had swapped my brain with a slushie and not even a breakfast or
    the panic in the group chat of those who just woke up to the email could fix it.{/size}"
    "I had been dedicated to come up with a plan before I went to bed, I told myself while opening the door to the main hall of the university."
    "I was a master problem solver."
    "A rockstar coder."
    "One of the brightest minds of our generation."
    
    jump arriving_to_the_exam

label arriving_to_the_exam:
    scene bg exam_auditorium

    "Or at least that's what professor Bostan said while I made my way along the back of the auditorium, because I felt like neither of those things."

    "Because I had no plan on how to get through this."

    "I felt my palms sweat and chest burn as he repeated once more the content of yesterday's email, trying to figure out something…"
    "anything…"
    "that I could do to pass."

    show bostan at center with dissolve:
        ypos 900
    Bostan "Thank you for coming today."
    Bostan "As you've all probably noticed from your tech acting up, 
    we've been dealing with anomalous magnetic storms worldwide this week, Republic of Moldova included"
    Bostan  "With this occasion, I've been cordially invited to attend an international summit…"
    hide bostan with dissolve

    "I could try and copy the answers from one of my colleagues"
    "Stefan would usually sit in front of me and he seemed to be pretty good at this class."

    show bostan at center with dissolve:
        ypos 900
    Bostan "... I apologize for changing the exam dates…"
    Bostan "But I believe you've had all semester to learn, so a few days wouldn't change the results too much..."
    hide bostan with dissolve

    "But as I took a close look at my colleagues to find him, I realized that there were more of us than usual."
    "A lot more."
    "Had all majors had their Math Analysis exams moved to today?"
    "Not only that, but all spaces around Stefan were occupied already."
    "My hands started to tremble as more people filtered in and took their seats." 
    "This wasn't looking good."

    show bostan at center with dissolve:
        ypos 900
    Bostan "... However, considering that the 65th anniversary of FCIM is approaching"
    Bostan "I would be willing to give additional points to those of you who would be able to prepare a game about our university."
    Bostan "Let me show you an example."
    hide bostan with dissolve

    "I raised my head towards the whiteboard like a deer caught in the highlights just as professor Bostan started approaching his laptop."
    "A distant memory of him spoiling the answers to a quiz while showing his screen last month flashed before my eyes."
    "This was it."
    "This was my chance."
    "I made an immediate decision."

    menu:
        "Sit in the front row":
            "I bolted towards the first row under the questioning gazes of my peers, but I didn't pay them any heed, 
            taking the last available seat just as he reached it."
            $ row = 1
            $ chance_of_password = 0.83

            call awaiting_fortuna_gift
        "Sit in the second row":
            "I bolted towards the second row under the questioning gazes of my peers, but I didn't pay them any heed,
            taking the last available seat just as he reached it."
            $ row = 2
            $ chance_of_password = 0.33

            call awaiting_fortuna_gift

    jump no_more_dream

label awaiting_fortuna_gift:
    "Just a glance. Just a second."
    "I saw him sit down…"
    "Move the mouse to turn off the screen saver…"

    show whiteboard at center with dissolve:
        xpos 1500
        ypos 490
        zoom 0.7
    "Start typing in his password."
    "… 32…11…"

    $ random_integer = renpy.random.randint(0, 1)

    if random_integer < chance_of_password:
        "Something flew before my eyes, distracting me for barely a second."
    else:
        $ full_password = True
        "19…"
        "…72."

    "I felt my stomach clench as all my being focused on the rotating icon of loading icon…"
    "Please, God."
    "Just one glance. One second. One look at the answers…"
    hide whiteboard with dissolve

    show inky at center with dissolve:
        xpos 1450
        ypos 430
        zoom 0.9

    "Only to feel the last of my hope die down as I was greeted with the sight of a clear 
    home screen with only a text game tab open."

    "I blinked several times in quick succession to stop my eyes from watering and exhaled shaky breath."

    "This was it."

    "Game over."

    hide inky with dissolve

    return

label no_more_dream:
    "I didn't listen to anything around me, my sight focused on the spot that could have been my last saving grace,
    even as the whiteboard was turned off, even as the professor gave out the tests."

    show test at center with dissolve:
        # # xpos 700 
        ypos 1050
        zoom 0.7
    
    "I spent my whole time begging the clock to move faster as I read and reread the questions until the professor 
    told us to put our pencils down…"

    "I gave my paper filled with unintelligible scribbles and walked out the class with my head raised towards the ceiling, 
    trying to contain the tears of despair."

    hide test

    scene bg hall_first_floor with fade

    "If only I had studied properly before this."
    "If only I hadn't left the revisions for the last week."
    "If only they hadn’t changed the dates."
    "If only God hadn’t been so merciless and had answered my question…"

    "I stopped as I felt the emotions finally catch up to me, and tried to rub my eyes to stop the tears from spilling, 
    but stopped just as something caught my attention."

    show cameraOff at center with dissolve:
        xpos 200 
        ypos 310
        zoom 0.4

    "A camera, in the corner of the hall, with its usually blinking led nowhere to be seen."
    "Suddenly, all of today’s and yesterday’s information flooded my brain."
    "Magnetic storms."
    "Technology acting up."
    "The international summit."
    "Profesor Bostan leaving."

    hide cameraOff with dissolve

    "I was going to submit a different answer sheet to professor Bostan."
    "Even if I had to break into his cabinet in the middle of the night to do it."
    
    hide bg hall_first_floor with fade

    jump breaking_and_entering

    return