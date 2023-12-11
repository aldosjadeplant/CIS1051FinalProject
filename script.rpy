
define a = Character("Aldo")
image aldo = "cat"
image meadow:
    "bg meadow"
    zoom 2
image aldo:
    "cat"
    zoom 2.5
image galaxy:
    "bg galaxy"
    zoom 2
image ice:
    "bg ice"
    zoom 3
image dark:
    "bg dark"
    zoom 2
image forest:
    "bg forest"
    zoom 3.5
image picnic:
    "nic"
    zoom 0.5
image coral:
    "bg coral"
image current:
    "bg current.webp"
    zoom 1.25
image krusty:
    "bg krusty"
    zoom 4.5
image city:
    "bg city"
    zoom 2
image empire:
    "bg empire"
    zoom 4.5

label start:

    scene meadow
    show aldo at truecenter
    a "Howdy! Skies are blue, and the day glows with promise. Let's go on an adventure!"
    a "How're you feeling, spacey or watery?"

    menu:

        "‎‧₊˚✩ Spacey ✩˚₊‧":
            jump space

        "‧̍̊˙· Watery ·˙‧̍̊":
            jump ocean

    label space:

        a "And awaaaayy we go!"
        scene meadow
        show aldo

        scene galaxy
        show aldo
        with fade
        a "Far out! Whaddaya say we hop onto one of these planets for a picnic?"

        scene ice
        show aldo at truecenter
        with fade
        a "Brrr, yeah it's pretty but let's find somewhere cozier."

        scene dark
        show aldo at truecenter
        with fade
        a "Better but a little ominous. Third times the charm?"

        scene forest
        show aldo at truecenter
        with fade
        a "Wow :') very beauty much delight."
        show picnic at truecenter
        show aldo at left:
            xalign 0.0
            yalign 0.5
        a "^_^"
        a "Best day ever."

    return

    label ocean:

        a "Ay ay captain!"
        scene meadow
        show aldo at truecenter

        scene coral
        show aldo at truecenter
        with fade
        a "Wow this isn't my usual kinda environment, but it's a swanky scene!"
        a "Are you hungry for burgers? I know a really good spot."

        menu:

            "Oh yeah, let's grub":
                jump krab

            "Nah let's check out the sights":
                a "x_x I guess we can get something on the way."
                jump atlantis

        label krab:

            a "Righteous, there's the East Australian Current, it'll take us right there!"
            scene coral
            show aldo at truecenter

            scene current
            show aldo at truecenter
            with fade
            a "WooAaAaAhhhh!"

            scene krusty
            show aldo at truecenter
            with fade
            a "*buuuurp*"
            a "Delicious. Let's swim this off somewhere interesting."
            jump atlantis

        label atlantis:

            scene city
            show aldo at truecenter
            with fade
            a "So this is Atlantis! Let's get into some history!"

            scene empire
            show aldo at truecenter
            with fade
            a "Whew, can't believe we toured the whole city in a day."
            a "Thanks for taking this journey with me. Let's explore the Hadalpelagic zone next!"



    return
