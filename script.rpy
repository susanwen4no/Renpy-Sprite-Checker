# The script of the game goes in this file.


# The game starts here.

label start:


    scene bg path

label text_input:

    $ display_sprite = renpy.input("what do you want to display? (Type Q to quit): ")

    if display_sprite == "Q":
        "Exiting text input image display"
        return

    $ renpy.show(display_sprite)
    "displaying [display_sprite]"

    $ renpy.hide(display_sprite)
    jump text_input

    return
