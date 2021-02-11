# The script of the game goes here

define sprites = []

label dress_up:

    scene bg path

    python:
        if not sprites:          # sprites empty?
            list = renpy.get_available_image_tags()
            for item_tag in list:
                t = type(renpy.get_registered_image(item_tag))

                if t == type(LayeredImage([])):
                    sprites.append((item_tag, item_tag))

        narrator("Who do you choose?", interact=False)
        character = renpy.display_menu(sprites)

    "you chose [character]"
    $ renpy.show(character)
    "there's nothing here :p"
    return

# Input name of sprite to display to display the desired sprite
label text_input:

    scene bg path

    $ display_sprite = renpy.input("what do you want to display? (Type Q to quit): ")

    if display_sprite == "Q":
        "Exiting text input image display"
        return
    elif not (renpy.has_image(display_sprite)):
        "That image does not exist."
        jump text_input

    $ renpy.show(display_sprite)
    "Displaying [display_sprite]"

    $ renpy.hide(display_sprite)
    jump text_input

    return
