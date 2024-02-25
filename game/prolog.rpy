
define mc = Character("Me", color="#c8ffc8")
image laptop = "prolog/laptop.png"

# The game starts here.

label prolog:

    scene bg mc_room_morning

    # show eileen happy

    $ charcenter = Position(xpos=0.2, xanchor=0.5, ypos=0.7, yanchor=0.5)
    show laptop  at charcenter  with fade :
        zoom 0.8

    "{size=-10}The laptop cast a bluish light around the dark room, highlighting the stack of unopened programming textbooks, 
    mountain of unwashed coffee mugs and the bundle of blankets that separated me from the mental breakdown that I 
    had been teetering on the edge of for the past 15 minutes.{/size}"

    "All because of one unfortunate little email."

    "“Magnetic storm… Faulty electronics… International conference…”"
    "I could feel myself die a little as I tried to make sense of the announcement through a blurry vision."


    # mc "You'."

    # mc R"Once you add a story, pictures!"



    return
