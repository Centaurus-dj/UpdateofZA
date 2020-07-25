screen test():
 tag menu
 add Image("/images/background/menu_1.jpg")
 textbutton _("Retour") ypos .954 action ShowMenu("about")
 vbox:
    text _("{b}{color=#f9300c}L'écran des curieux...{/color}{/b}") xpos 1.9

 textbutton _("Infos") ypos 0.2 xpos .35 action ShowMenu("infos")







screen infos():
  tag menu
  add Image("/images/background/menu_3_modif.jpg")
  textbutton _("Retour") ypos .954 action ShowMenu("test")
  vbox:
    text _("""{b}{color=#f9300c} Sur qui ou quoi veux tu en savoir un peu plus ?? {/color}{/b}""") xpos .7
  textbutton _("Unknown Games") ypos 0.2 xpos .29 action ShowMenu("Unknown_Games")
  textbutton _("Le créateur de ce jeu") ypos 0.2 xpos .55 action ShowMenu("alexis")


screen alexis():
    tag menu
    use game_menu_plus_5(_("Alexis"), scroll="viewport"):
        style_prefix "about"
        vbox:
            text _("""Je suis un gars lambda qui aime bien programmer(je peux passer 15h à programmer par jour juste par pure plaisir...)
            J'ai 15 ans. J'ai toujours été intéréssé par les jeux vidéos jusqu'à que j'ai la possiblité de faire mes jeux !
            Ca fait presque 1 an que je travaille à créer ce jeux...
            Sachez que je suis très sérieux mais au fond de moi... Il y a comme un brin de folie qui se réveille de temps en temps...


            """)
    text _("{color=#f9300c}{b}Alexis{/b}{/color}") style_prefix "about" ypos .2 xpos 0.2
screen Unknown_Games():
    tag menu
    use game_menu_plus_5(_("Unknown Games"), scroll="viewport"):
        style_prefix "about"
        vbox:
            text _(""" Le PDG est {color=#f9300c}{b}Alexis O.{/b}{/color}
            \n Le PDG adjoint est {color=#004cff}{b}Alban B.{/b}{/color}
            \n Le DRH est {color=#09c636}{b}Henri C.{/b}{/color}
            \n Il y a {color=#6f16db}{b}Léo M.{/b}{/color} qui est un de nos codeurs

            \n Unknown Games est une "pseudo" entreprise fictive, c'est à dire qu'il n'existe que sur internet...
            \n Elle a été fondée sur une règle fondamentale qui est : "Tous nos jeux sont et seront gratuits à leur sortie officielles"
            Nous sommes à votre écoute et nous serons enclins à répondre à vos questions à {a=send_email}aetagamestudio@gmail.com{/a}
             """)

python:
    def staboutfunc():
        pass



################################################################################
#################              Changed                              ############
################################################################################

screen game_menu_plus_1(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu_plus_1"


    frame:
        style "game_menu_plus_1_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

        textbutton _("Retour") ypos .9 xpos .048 action ShowMenu("infos")


################################################################################

screen game_menu_plus_2(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu_plus_2"


    frame:
        style "game_menu_plus_2_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude
    use navigation

    #textbutton _("Retour"):
    #    style "return_button"
    if _preferences.language == None:
        imagebutton:
            idle "ret"
            hover "ret_hov"
            ypos .9
            xpos .048
            action Return()
    elif _preferences.language == "english":
        imagebutton:
            idle "/translate/buttons/back.png"
            hover "/translate/buttons/back_hover.png"
            ypos .9
            xpos .048
            action Return()
        #textbutton _("Retour") ypos .9 xpos .048 action ShowMenu("main_menu")


screen Test():
    tag menu
    use game_menu_plus_2(_("Test"), scroll="viewport"):
        vbox:
            text _("Ce n'est qu'un test...")




################################################################################


screen game_menu_plus_3(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu_plus_3"



    frame:
        style "game_menu_plus_3_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    #textbutton _("Retour"):
    #    style "return_button"
    if _preferences.language == None:
        imagebutton:
            idle "ret"
            hover "ret_hov"
            ypos .9
            xpos .048
            action Return()
    elif _preferences.language == "english":
        imagebutton:
            idle "/translate/buttons/back.png"
            hover "/translate/buttons/back_hover.png"
            ypos .9
            xpos .048
            action Return()

################################################################################
screen game_menu_plus_4(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu_plus_4"



    frame:
        style "game_menu_plus_4_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    #textbutton _("Retour"):
    #    style "return_button"
    if _preferences.language == None:
        imagebutton:
            idle "ret"
            hover "ret_hov"
            ypos .9
            xpos .048
            action Return()
    elif _preferences.language == "english":
        imagebutton:
            idle "/translate/buttons/back.png"
            hover "/translate/buttons/back_hover.png"
            ypos .9
            xpos .048
            action Return()

################################################################################
screen game_menu_plus_5(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu_plus_5"


    frame:
        style "game_menu_plus_5_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

        imagebutton:
            idle "ret"
            hover "ret_hov"
            ypos .9
            xpos .048
            action ShowMenu("infos")


style game_menu_plus_5_frame:
    bottom_padding 45
    top_padding 180
    background "images/background/menu_3_modif_about.jpg"

################################################################################
screen game_menu_test(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu_test"

    if main_menu:
        add "test_menu"
    else:
        add "test_menu"
    text _("[current.statement!q]"):
        style "game_menu_statement"
    frame:
        style "game_menu_test_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude
    use navigation

    textbutton _("Retour"):
        ypos .9
        xpos .048
        text_style "raidercrusader"
        action Return()

style game_menu_test_frame is empty

style game_menu_test_frame:
    bottom_padding 45
    top_padding 180
    background "gui/overlay/confirm.png"


################################################################################
################################################################################
################################################################################

screen tip_plus():
    text _(u"[tiptoadvance]"):
        style "tip"
