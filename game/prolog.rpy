
define mc = Character("Me", color="#c8ffc8")
image laptop = "prolog/laptop.png"

# The game starts here.

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

    "{size=-10}Professor Bostan always said that there’s no point in preparing for an exam twelve hours before it. 
    Moreover, most of his exams have always consisted of both essay questions and multiple choice ones.{/size}"

    "{size=-10}So, with a bit of luck, I’d be able to score just enough to pass and then correct my grade next semester.{/size}"

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

    return
