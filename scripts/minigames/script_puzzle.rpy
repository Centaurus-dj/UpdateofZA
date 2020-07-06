# You can place the script of your game in this file.
label retour:
return


init:
    $ eil = Character('Eileen', color="#c8ffc8")

    image eileen happy = "eileen_happy.png"
    image bg table = "table.jpg"
    image dim = "#0008"

    # Some styles for show text.
#    $ style.centered_text.drop_shadow = (2, 2)
#    $ style.centered_text.drop_shadow_color = "#000b"

if _preferences.language == None:
    label start_puzzle:

    menu:
        "Quel puzzle veux tu faire ?"
        "Le 1er ":
            $ puzzle = 1
            jump start_puzzle_2
        "le 2ème ":
            $ puzzle = 2
            jump start_puzzle_2
        "Aucun ":
            jump retour


    label start_puzzle_2:
        init -1 python hide:

            ## Should we enable the use of developer tools? This should be
            ## set to False before the game is released, so the user can't
            ## cheat using developer tools.

            config.developer = True

            ## These control the width and height of the screen.

            config.screen_width = 1280
            config.screen_height = 720

        scene ecran_noir

        python:
            k = Puzzle()
            k.set_sensitive(False)
            k.show()

        show dim at center
        show prog at center
        with dissolve

        a "Bienvenue dans la démo du puzzle."
        a "Clique sur les pièces pour les faire tourner."
        a "Attrappe une pièce et met là où tu veux avec ta souris."
        a "Bonne chance !"

    label continue:

        hide dim
        hide prog
        with dissolve
        window hide
    label quick_continue:

        while True:

            python:

                ui.textbutton("Abandonner", ui.jumps("giveup"), xalign=.02, yalign=.98)
                k.set_sensitive(True)
                event = k.interact()

                if event:
                    renpy.checkpoint()

                k.set_sensitive(False)
            # a "[event]"
            if event == "win":
                jump win


    label win:

        "Tu as fini !"
        show dim
        show prog
        with dissolve

        "Bravo !"

        jump newgame

    label giveup:

        $ k.set_sensitive(False)

        show dim
        show prog
        with dissolve

        menu:
            a "Es-tu sûr(e) de vouloir abandonner ?"

            "Oui":

                "Bon, bah... T'auras peut-être plus de chance la prochaine fois..."

                jump newgame

            "Non":

                jump continue

    label newgame:

        menu:
            a "Veux-tu essayer de nouveau ?"

            "Oui":
                pass

            "Non":
                a "Bon, j'espère te revoir bientôt..."
                return

        a "Okay, voilà !"

        scene ecran_noir

        python:
            k = Puzzle()
            k.sensitive = False
            k.show()

        jump continue



elif _preferences.language == "english":
    label start_puzzleeng:
        init -1 python hide:

            ## Should we enable the use of developer tools? This should be
            ## set to False before the game is released, so the user can't
            ## cheat using developer tools.

            config.developer = True

            ## These control the width and height of the screen.

            config.screen_width = 1280
            config.screen_height = 720

        scene ecran_noir

        python:
            k = Puzzle()
            k.set_sensitive(False)
            k.show()

        show dim at center
        show prog at center
        with dissolve

        a "Welcome to the puzzle demo."
        a "Click on pieces to rotate them."
        a "Drag pieces onto each other to switch."
        a "Good luck!"

    label continueeng:

        hide dim
        hide prog
        with dissolve
        window hide
    label quick_continueeng:

        while True:

            python:

                ui.textbutton("Give Up", ui.jumps("giveup"), xalign=.02, yalign=.98)
                k.set_sensitive(True)
                event = k.interact()

                if event:
                    renpy.checkpoint()

                k.set_sensitive(False)
            # a "[event]"
            if event == "win":
                jump wineng


    label wineng:

        "Finished!"
        show dim
        show prog
        with dissolve

        "Congratulations!"

        jump newgameeng

    label giveupeng:

        $ k.set_sensitive(False)

        show dim
        show prog
        with dissolve

        menu:
            a "Are you sure you want to give up?"

            "Yes":

                "Oh well, better luck next time."

                jump newgameeng

            "No":

                jump continueeng

    label newgameeng:

        menu:
            a "Would you like to try again?"

            "Yes":
                pass

            "No":
                a "Well, I hope to see you again soon."
                return

        a "Okay, here we go!"

        scene bg table

        python:
            k = Puzzle()
            k.sensitive = False
            k.show()

        jump continueeng
