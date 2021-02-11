# The script of the game goes here

label start:

    scene bg path
    "there's nothing here :p"
    return

# Input name of sprite to display to display the desired sprite
label text_input:

    scene bg path

    $ display_sprite = renpy.input("what do you want to display? (Type Q to quit): ")

    if display_sprite == "Q":
        "Exiting text input image display"
        return

    $ renpy.show(display_sprite)
    "Dsplaying [display_sprite]"

    $ renpy.hide(display_sprite)
    jump text_input

    return
