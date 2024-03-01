
define mc = Character("Me")

init:
    $ d_affection = 0
    $ m_affection = 0
    $ shared_info = False

label start:

    # jump arriving_to_the_exam
    jump dealing_with_a_maniac
    return
