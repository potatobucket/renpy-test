# The script of the game goes in this file.

# The game starts here.

define hasMetWhitney = False

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    show whitney smile at middlish with dissolve

    # These display lines of dialogue.

    whitney.chr "I'm so glad you could make it!"

    show whitney neutral at middlish

    whitney.chr "Oh, it's you." with hpunch

    jump branching_path

    return

label branching_path:
    if hasMetWhitney == False:
        whitney.chr "Would you at least like to go outside?"

        menu:
            "Sure!":
                $ hasMetWhitney = True
                jump go_outside

            "Nah.":
                $ hasMetWhitney = True
                jump no_go_outside

    else:
        show whitney neutral at middlish with move
        whitney.chr "Have you changed your mind about going outside?"

        menu:
            "I guess.":
                jump go_outside

            "Still no.":
                whitney.chr "Well, I guess there's no helping you, then."
                jump bad_ending

    # This ends the game.

    return

label go_outside:
    
    scene bg outside
    show whitney smile at middlish with dissolve

    whitney.chr "Well, at least we got to go outside."

    show potato_bucket at middlish with dissolve

    potato.chr "Congratulations on achieving the golden ending!"

    show whitney neutral at rightish with move

    whitney.chr "Hey!"

    potato.chr "We hope you've enjoyed out little pageant!"

    show whitney neutral at leftish with move

    whitney.chr "That was very rude!"

    return

label no_go_outside:

    show whitney neutral at leftish with move
    whitney.chr "Boo! Boo this man!"

    show whitney neutral at rightish with move
    whitney.chr "Boooooo!"

    menu:
        "Give in to peer pressure":
            jump branching_path

        "Continue to show reticence at experiencing Mother Nature":
            jump bad_ending

    return

label bad_ending:

    scene bg black

    whitney.chr """
    I'm sorry it had to come to this.

    I really wanted to go outside.

    But you leave me no choice.
    """

    show whitney kill at middlish with dissolve
    play sound "trumpet sting.wav"

    "BZZZZZ-OIP!"

    show whitney smile at middlish

    "That'll learn ya!"

    badEnding.chr """
    And so you died the way you lived: being lasered down by the eyes of Whitney.

    At least you can take the smallest bit of comfort in knowing that it was always going to end this way.

    Ashes to ashes; dust to dust.
    """

    return
