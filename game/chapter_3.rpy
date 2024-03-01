label counting_loses:
    scene bg classroom_101_night_darkened
    
    "I took deep breaths as I calmed myself down in the darkness of the hallway."

    Unknown "Who's here?"

    "Someone... David, whispered to my left"

    #TODO: Show David

    mc "Me"

    "I answered back with the same tone, throat parched after the sprint."
    "Then, others followed. I counted only three other voices. "
    #TODO: Show Ana, Maria Marius
    "Ana, Maria, and Marius."
    "I felt a node in my throat."
    "Alex and Theo were still down there."

    #TODO: Show David

    "David must have also realized the loss"

    David "Should we turn back?"

    #TODO: Show Ana, Maria Marius
    
    "However, we all knew that it was not feasible."

    "They were either already caught, or they’ll make their way to us at some point. Going back would only bring trouble."

    "To us and to them."

    "I took a look around at the outlines of the floor plan. It was the same as the last two, but this one was cleaner, neater."

    if map_found:
        jump double_trouble
    else:
        "As I took a first step towards the direction in which the map showed professor Bostan’s cabinet, Marius grabbed me by my arm and dragged me into a nearby cabinet."
        jump misery_of_a_man
    
    jump crossroads
    return

label double_trouble:
    "My eyes widened as I saw what looked like a list of cabinets and their professors from the corner of my eye, but just as I wanted to make it public, Marius dragged me by my arm into a nearby cabinet."

    jump misery_of_a_man

    show ana with dissolve:
        xpos 300
        ypos 120
        zoom 0.7

    Ana "So, what now?"

    Ana "Do we just look from cabinet to cabinet?"

    mc "No need, I saw a list nearby, it’ll show us what we’re looking for."

    "I gestured towards one of the walls."
    
    hide ana with dissolve
