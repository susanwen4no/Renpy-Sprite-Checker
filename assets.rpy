# Management of character sprites, background images, etc. have been placed
# into this file.

# Define the background images here. (VIVA UNCLE MUGEN)

image bg path = "forest_bg_01.jpg"
image bg forest_outer = "forest_02.jpg"

# Initialize character sprites. Layered images are useful for saving space.

init python:
    # X-Y sizes of sprites
    spriteX = 391 * 1.15
    spriteY = 655 * 1.15

layeredimage chris:

    always:
        im.Scale("images/chris/chris base.png", spriteX, spriteY)

    group eyes:
        attribute open default:
            im.Scale("images/chris/chris default eyes.png", spriteX, spriteY)

    group eyebrows:
        attribute calm default:
            im.Scale("images/chris/chris default eyebrows.png", spriteX, spriteY)
        attribute angry:
            im.Scale("images/chris/chris angry eyebrows.png", spriteX, spriteY)
        attribute furrowed:
            im.Scale("images/chris/chris furrowed eyebrows.png", spriteX, spriteY)
        attribute raised:
            im.Scale("images/chris/chris raised eyebrows.png", spriteX, spriteY)
        attribute worried:
            im.Scale("images/chris/chris worried eyebrows.png", spriteX, spriteY)

    group mouth:
        attribute neutral default:
            im.Scale("images/chris/chris neutral mouth.png", spriteX, spriteY)
        attribute frown:
            im.Scale("images/chris/chris frown mouth.png", spriteX, spriteY)
        attribute smile:
            im.Scale("images/chris/chris smile mouth.png", spriteX, spriteY)
        attribute speechless:
            im.Scale("images/chris/chris speechless mouth.png", spriteX, spriteY)
        attribute grin:
            im.Scale("images/chris/chris grin mouth.png", spriteX, spriteY)

    group extra:
        attribute tears:
            im.Scale("images/chris/chris default tears.png", spriteX, spriteY)
        attribute blush:
            im.Scale("images/chris/chris blush.png", spriteX, spriteY)

layeredimage zelda:

    always:
        im.Scale("images/zelda/zelda base.png", spriteX, spriteY)

    group eyes:
        attribute open default:
            im.Scale("images/zelda/zelda default eyes.png", spriteX, spriteY)
        attribute narrowed:
            im.Scale("images/zelda/zelda narrowed eyes.png", spriteX, spriteY)

    group eyebrows:
        attribute calm default:
            im.Scale("images/zelda/zelda default eyebrows.png", spriteX, spriteY)
        attribute raised:
            im.Scale("images/zelda/zelda raised eyebrows.png", spriteX, spriteY)
        attribute worried:
            im.Scale("images/zelda/zelda worried eyebrows.png", spriteX, spriteY)
        attribute angry:
            im.Scale("images/zelda/zelda angry eyebrows.png", spriteX, spriteY)

    group mouth:
        attribute smile default:
            im.Scale("images/zelda/zelda smile mouth.png", spriteX, spriteY)
        attribute neutral:
            im.Scale("images/zelda/zelda neutral mouth.png", spriteX, spriteY)
        attribute shout:
            im.Scale("images/zelda/zelda shout mouth.png", spriteX, spriteY)
        attribute surprised:
            im.Scale("images/zelda/zelda surprised mouth.png", spriteX, spriteY)
        attribute happy:
            im.Scale("images/zelda/zelda happy mouth.png", spriteX, spriteY)
        attribute grimace:
            im.Scale("images/zelda/zelda grimace mouth.png", spriteX, spriteY)
        attribute frown:
            im.Scale("images/zelda/zelda frown mouth.png", spriteX, spriteY)

    group extra:
        attribute gun default:
            im.Scale("images/zelda/zelda gun.png", spriteX, spriteY)
        attribute backpack default:
            im.Scale("images/zelda/zelda backpack.png", spriteX, spriteY)
    group face_extra:
        attribute blush:
            im.Scale("images/zelda/zelda blush.png", spriteX, spriteY)
        attribute tears:
            im.Scale("images/zelda/zelda narrowed eyes tears.png", spriteX, spriteY)
