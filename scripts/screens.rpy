################################################################################
## Initialization
################################################################################

init offset = -1




################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    key "h" action ToggleVariable("hide_overlay")

    zorder 6 #Otherwise the character sprite would be obscuring it.



    default two_window = True

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0




## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"
    window:
        ypos .7
        xpos 1.0

        text prompt style "input_prompt"
        input id "input"





## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            $ alignment = ""
            for values in i.args:
                $ alignment = values
            textbutton i.caption :
                if difficulty == "Casual" and alignment is not "":
                    text_style alignment
                action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 1.0
            yalign 1.0

            imagebutton:
                idle "sett_ico"
                hover "sett_ico_hover"
                action ToggleScreen("quick_menu_showed")


screen quick_menu_showed():
    key "s" action ShowMenu("save")
    key "l" action ShowMenu("load")

    frame:
        background "07alpha_black_bg"
        xalign .95
        yalign 1.0
        vbox:
            style_prefix "quick"

            textbutton _("Retour") action Rollback()
            textbutton _("Avance R.") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Sauvegarde R.") action QuickSave()
            textbutton _("Para.") action ShowMenu('preferences')
            textbutton _("Quêtes") action ShowMenu(log.screen())


## Ce code garantit que le menu d’accès rapide sera affiché dans le jeu, tant
## que le joueur n’aura pas explicitement demandé à cacher l’interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True



################################################################################
## Main and Game Menu Screens
################################################################################

## Écran de navigation #########################################################
##
## Cet écran est disponible dans le menu principal et dans le menu de jeu. Il
## fournit l’accès aux autres menus et permet le démarrage du jeu.

screen navigation():
    default is_hovered = False
    if _preferences.language == None:
        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.5

            spacing gui.navigation_spacing

            if main_menu:

                textbutton _("Nouvelle partie"):
                    text_style "raidercrusader"
                    action Start()

            elif not main_menu:

                button:
                    hbox:
                        text _("Menu Principal"):
                            style "raidercrusader"
                        image "main_menu_hover"
                    action MainMenu()

                button:
                    hbox:
                        text _("Sauvegarder"):
                            style "raidercrusader"
                        image "save_hover"
                    action ShowMenu("save")

            else:

                textbutton _("Historique"):
                    text_style "raidercrusader"
                    action ShowMenu("history")

            button:
                hbox:
                    text _("Charger"):
                        style "raidercrusader"
                    image "load_hover"
                action ShowMenu("load")

            #button:
            #    hovered "sett_ico_hover"
            #    hbox:
            #        text _("Paramètres"):
            #            style "raidercrusader"
            #        image "sett_ico"
            #    action ShowMenu("preferences")

            button:
                action ShowMenu("preferences")
                hovered SetScreenVariable("is_hovered", True)
                unhovered SetScreenVariable("is_hovered", False)
                hbox:
                    text "Paramètres":
                        style "raidercrusader"
                    showif is_hovered:
                        add "sett_clicked" at fader
                    else:
                        add "sett_ico" at fader


            button:
                hbox:
                    text _("À propos"):
                        style "raidercrusader"
                    image "about_hover"
                action ShowMenu("about")

            if _in_replay:

                textbutton _("Fin de la rediffusion"):
                    text_style "raidercrusader"
                    action EndReplay(confirm=True)

            if renpy.variant("pc"):

                ## L'aide n’est ni nécessaire ni pertinante sur les appareils
                ## mobiles.
                button:
                    hbox:
                        text _("Aide"):
                            style "raidercrusader"
                        image "help_hover"
                    action ShowMenu("help")

                ## Le bouton pour quitter est banni sur iOs et n'est pas nécessaire
                ## sur Android.
                button:
                    hbox:
                        text _("Quitter"):
                            style "raidercrusader"
                        image "quit_hover"
                    action Quit(confirm=not main_menu)
        #if main_menu == True:
            #hbox:
            #    imagebutton:
                    #idle "test"
                    #hover "test_hover"
                    #action OpenURL("https://aa-studio.itch.io/humanity-games-zombie-apocalypse")

    elif _preferences.language == "english":
        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.5

            spacing gui.navigation_spacing

            if main_menu:

                textbutton _("Start"):
                    text_style "raidercrusader"
                    action Start()
            elif not main_menu:
                textbutton _("Main Menu"):
                    text_style "raidercrusader"
                    action MainMenu()

                textbutton _("Save"):
                    text_style "raidercrusader"
                    action ShowMenu("save")
            else:

                textbutton _("History"):
                    text_style "raidercrusader"
                    action ShowMenu("history")

            textbutton _("Load"):
                text_style "raidercrusader"
                action ShowMenu("load")

            textbutton _("Settings"):
                text_style "raidercrusader"
                action ShowMenu("preferences")

            if _in_replay:

                textbutton _("End of replay"):
                    text_style "raidercrusader"
                    action EndReplay(confirm=True)


            textbutton _("About"):
                text_style "raidercrusader"
                action ShowMenu("about")

            if renpy.variant("pc"):

                ## L'aide n’est ni nécessaire ni pertinante sur les appareils
                ## mobiles.
                textbutton _("Help"):
                    text_style "raidercrusader"
                    action ShowMenu("help")

                ## Le bouton pour quitter est banni sur iOs et n'est pas nécessaire
                ## sur Android.
                textbutton _("Exit"):
                    text_style "raidercrusader"
                    action Quit(confirm=not main_menu)





## Écran du menu principal #####################################################
##
## Utilisé pour afficher le menu principal quand Ren'Py démarre.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    ## This empty frame darkens the main menu.
    frame:
        pass



    if _preferences.language == None:
        imagemap:
            #ground "images/background/menu_2.jpg"
            ground "main_menu_bg"
            idle "gui/Game_menu.png"
            hover "gui/Game_menu_hover.png"

            vbox:
                style "main_menu_vbox"

                textbutton("Nouvelle Partie"):
                    text_style "raidercrusader"
                    action Start()
                textbutton("Charger"):
                    text_style "raidercrusader"
                    action ShowMenu("load")
                textbutton("Paramètres"):
                    text_style "raidercrusader"
                    action ShowMenu("preferences")
                textbutton("À propos"):
                    text_style "raidercrusader"
                    action ShowMenu("about")
                textbutton("Aide"):
                    text_style "raidercrusader"
                    action ShowMenu("help")
                textbutton("Quitter"):
                    text_style "raidercrusader"
                    yoffset 70
                    action Quit()

            hotspot(1208, 201, 63, 50) action OpenURL("https://discord.gg/pQg85M")
            hotspot(1214, 263, 60, 58) action OpenURL("https://www.instagram.com/les_studios_aa/")
            hotspot(1213, 324, 66, 77) action OpenURL("https://www.patreon.com/studiosaa")

        vbox:
            text _("Zombie Apocalypse"):
                style "game_title"
    elif _preferences.language == "english":
        imagemap:
            #ground "images/background/menu_2.jpg"
            ground "main_menu_bg"
            idle "gui/Game_menu_eng.png"
            hover "gui/Game_menu_eng_hover.png"

            vbox:
                style "main_menu_vbox"

                textbutton("Start"):
                    text_style "raidercrusader"
                    action Start()
                textbutton("Load"):
                    text_style "raidercrusader"
                    action ShowMenu("load")
                textbutton("Settings"):
                    text_style "raidercrusader"
                    action ShowMenu("preferences")
                textbutton("About"):
                    text_style "raidercrusader"
                    action ShowMenu("about")
                textbutton("Help"):
                    text_style "raidercrusader"
                    action ShowMenu("help")
                textbutton("Quit"):
                    text_style "raidercrusader"
                    yoffset 70
                    action Quit()

            hotspot(1208, 201, 63, 50) action OpenURL("https://discord.gg/pQg85M")
            hotspot(1214, 263, 60, 58) action OpenURL("https://www.instagram.com/les_studios_aa/")
            hotspot(1213, 324, 66, 77) action OpenURL("https://www.patreon.com/studiosaa")

    #style_prefix "main_menu"

    #add gui.main_menu_background


    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    #use navigation

    #if gui.show_name:

    #    vbox:
    #        text "[config.name!t]":
    #            style "main_menu_title"

    style_prefix "my_main_menu"
    vbox:
        text _("[current.version]"):
            style "main_menu_version_txt"



## Écran du menu de jeu ########################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

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
    #if _preferences.language == None:
    #    imagebutton:
    #        idle "ret"
    #        hover "ret_hov"
    #        ypos .9
    #        xpos .048
    #        action Return()
    #elif _preferences.language == "english":
    #    imagebutton:
    #        idle "/translate/buttons/back.png"
    #        hover "/translate/buttons/back_hover.png"
    #        ypos .9
    #        xpos .048
    #        action Return()






    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


## Écran « À propos... » #######################################################
##
## Cet écran présente le générique, les crédits et les informations de copyright
## relatives au jeu et à Ren’Py.
##
## Il n’y a rien de spécial sur cet écran. Par conséquent, il sert aussi
## d’exemple pour créer un écran personnalisé.

screen about():
    tag menu
    if _preferences.language == None:
        use game_menu_test(_("À propos"), scroll="viewport"):
                    style_prefix "about"

                    vbox:
                #    image "menu_2"
                        label _("[config.name!t]"):
                            text_style "thunderstrike_lbl"
                        text _("Version {color=#f9300c}[current.version!t]\n{/color}"):
                            style "thunderstrike_txt"

                        ## gui.about est généralement initialisé dans le fichier
                        ## options.rpy.
                        if gui.aboutfr:
                            text "[gui.aboutfr!t]\n"

                        text _("")

                        vbox:
                            text _("""

Ce programme contient un logiciel gratuit sous un certain nombre de  licences, incluant la MIT Licence et la GNU Lesser General Public Licence.
La liste complète du Logiciel, incluant des liens pour le code source sont accessibles {a=https://www.renpy.org/doc/html/license.html}{font=fonts/thunderstrike.ttf}ici{/font}{/a}
Fait avec {a=https://www.renpy.org/}{font=fonts/thunderstrike.ttf}Ren'py{/font}{/a} 7.3.5.606

                            """):
                                style "thunderstrike_txt"
                        textbutton _("Plus..."):
                            text_style "thunderstrike"
                            action ShowMenu("test")



    elif _preferences.language == "english":
        use game_menu_test(_("À propos"), scroll="viewport"):
            style_prefix "about"

            vbox:
                #    image "menu_2"
                label _("[config.name!t]"):
                    text_style "thunderstrike_lbl"
                text _("Version {color=#f9300c}[current.version!t]\n{/color}"):
                    style "thunderstrike_txt"

                ## gui.about est généralement initialisé dans le fichier
                ## options.rpy.
                if gui.abouteng:
                    text "[gui.abouteng!t]\n"

                    vbox:
                        text _("""

This program contains free software under a number of licenses, including the MIT License and GNU Lesser General Public License.
A complete list of Software, including links to full source code, can be found {a=https://www.renpy.org/doc/html/license.html}{font=fonts/thunderstrike.ttf}here{/font}{/a}
Made with {a=https://www.renpy.org/}{font=fonts/thunderstrike.ttf}Ren'py{/font}{/a} 7.3.5.606

                        """):
                            style "thunderstrike_txt"


## Ceci est généralement redéfini dans le fichier options.rpy  pour ajouter le
## texte dans l’écran « À propos ».
define gui.about = ""



## Écran de chargement et de sauvegarde ########################################
##
## Ces écrans permettent au joueur d’enregistrer le jeu et de le charger
## à nouveau. Comme ils partagent beaucoup d’éléments communs, ils sont
## tous les deux implémentés dans un troisième écran, appelé fichiers_slots
## (emplacement_de_fichier).
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu
    if _preferences.language == None:
        use file_slots(_("Sauvegarde"))
    elif _preferences.language == "english":
        use file_slots(_("Saves"))

screen load():

    tag menu
    if _preferences.language == None:
        use file_slots(_("Charger"))
    elif _preferences.language == "english":
        use file_slots(_("Load"))



screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Sauvegardes automatiques"), quick=_("Sauvegardes rapides"))

    use game_menu_test(title):

        fixed:

            ## Cette instruction s’assure que l’évenement enter aura lieu avant
            ## que l’un des boutons ne fonctionne.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## La grille des emplacements de fichiers.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A %d %B %Y, %H:%M"), empty=_("emplacement vide")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Boutons pour accéder aux autres pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


## Écran des mini-jeux #######################################################
##
## L’écran des mini-jeux permet au joueur de choisir un mini-jeux à choisir pour jouer.
##
##
## Il n’y a rien de spécial sur cet écran. Par conséquent, il sert aussi
## d’exemple pour créer un écran personnalisé.


screen minijeux():
#image logo solidexample = Solid("#0000cc", xysize=(200, 200))
    tag menu
    if _preferences.language == None:
            use game_menu_test("mini-jeux"):
                frame:

                    xalign 1.0
                    yalign 0.5
                    background None
                    #background "gui/game_menu.png"
                    #add SideImage("images/minigame_hover.png")
                    #add Image("images/minigame_hover.png", size=(400,300), xpos=0.5, ypos=0.5, xanchor=0, yanchor=0)
                    #add Image("gui/game_menu.png",size=(1280,720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                    #add Movie(play="images/video/mm2_video.avi", size=(1280,720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                    #image ("minigame.png")
                    imagebutton:
                        idle "minigame.png"
                        hover "minigame_hover.png"
                        action Start("mini_jeux1")


                    hbox:
                        style_prefix "page"

                        xalign 0.5
                        yalign 1.0

                        spacing gui.page_spacing

                        textbutton _("<") action FilePagePrevious()

                        ## range(1, 10) gives the numbers from 1 to 9.
                        for page in range(1, 5):
                            textbutton "[page]" action FilePage(page)

                            textbutton _(">") action FilePageNext()
                    imagebutton:
                        xalign .56
                        yalign .05
                        idle "puzzle1.png"
                        hover "puzzle1_hover.png"
                        action Start("start_puzzle")
                    imagebutton:
                        xalign 1.0
                        yalign .05
                        idle "intit.jpg"
                        hover "intit_hover.jpg"
                        action Start("clicker")
    elif _preferences.language == "english":
            use game_menu_plus_4("mini-games"):
                frame:

                    xalign 1.0
                    yalign 0.5
                    background None
                    #background "gui/game_menu.png"
                    #add SideImage("images/minigame_hover.png")
                    #add Image("images/minigame_hover.png", size=(400,300), xpos=0.5, ypos=0.5, xanchor=0, yanchor=0)
                    #add Image("gui/game_menu.png",size=(1280,720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                    #add Movie(play="images/video/mm2_video.avi", size=(1280,720), xpos=0, ypos=0, xanchor=0, yanchor=0)
                    #image ("minigame.png")
                    imagebutton:
                        idle "minigame.png"
                        hover "minigame_hover.png"
                        action Start("mini_jeuxeng")


                    hbox:
                        style_prefix "page"

                        xalign 0.5
                        yalign 1.0

                        spacing gui.page_spacing

                        textbutton _("<") action FilePagePrevious()

                        ## range(1, 10) gives the numbers from 1 to 9.
                        for page in range(1, 5):
                            textbutton "[page]" action FilePage(page)

                            textbutton _(">") action FilePageNext()
                    imagebutton:
                        xalign .56
                        yalign .05
                        idle "puzzle1.png"
                        hover "puzzle1_hover.png"
                        action Start("start_puzzleng")
                    imagebutton:
                        xalign 1.0
                        yalign .05
                        idle "intit.jpg"
                        hover "intit_hover.jpg"
                        action Start("clickereng")

## Écran des préférences #######################################################
##
## L’écran de préférence permet au joueur de configurer le jeu pour mieux
## correspondre à ses attentes.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences
#def Test(False)

#def lang(arg):
#    if lang == "fr":
#        Jump("about_fr")


screen preferences():

    tag menu
    if _preferences.language == None:
            use game_menu_test(_("Paramètres"), scroll="viewport"):

                vbox:

                    hbox:
                        box_wrap True

                        if renpy.variant("pc"):

                            vbox:

                                #add Image("/background/menu_2.jpg", xpos = 0, ypos = 0)
                                style_prefix "radio"
                                label _("Affichage"):
                                    text_style "thunderstrike_lbl"
                                textbutton _("Fenêtre"):
                                    text_style "thunderstrike"
                                    action Preference("display", "window")
                                textbutton _("Plein écran"):
                                    text_style "thunderstrike"
                                    action Preference("display", "fullscreen")

                        vbox:
                            style_prefix "radio"
                            label _("Sens d’annulation"):
                                text_style "thunderstrike_lbl"
                            textbutton _("Désactivé"):
                                text_style "thunderstrike"
                                action Preference("rollback side", "disable")
                            textbutton _("Gauche"):
                                text_style "thunderstrike"
                                action Preference("rollback side", "left")
                            textbutton _("Droite"):
                                text_style "thunderstrike"
                                action Preference("rollback side", "right")

                        vbox:
                            style_prefix "check"
                            label _("Avance rapide"):
                                text_style "thunderstrike_lbl"
                            textbutton _("Texte non lu"):
                                text_style "thunderstrike"
                                action Preference("skip", "toggle")
                            textbutton _("Après les choix"):
                                text_style "thunderstrike"
                                action Preference("after choices", "toggle")
                            textbutton _("Transitions"):
                                text_style "thunderstrike"
                                action InvertSelected(Preference("transitions", "toggle"))

                        ## Des boites vbox additionnelles de type "radio_pref" ou
                        ## "check_pref" peuvent être ajoutées ici pour ajouter des
                        ## préférences définies par le créateur du jeuself.
                        vbox:
                            style_prefix "radio"
                            xalign 0.5
                            label _("Langues"):
                                text_style "thunderstrike_lbl"
                            imagebutton:
                                idle "fr_icon"
                                hover "fr_icon_hov"
                                action Language(None)
                            imagebutton:
                                idle "en_icon"
                                hover "en_icon_hov"
                                action Language("english")
                            #textbutton _("Espagnol"):
                                #text_style "thunderstrike
                                #action Language("spanish()")
                            imagebutton:
                                idle "de_icon"
                                hover "de_icon_hov"
                                action Language("Deutsch()")
                            #textbutton _("Russe"):
                                #text_style "thunderstrike"
                                #action Language("rus()")

                    null height (4 * gui.pref_spacing)

                    hbox:
                        style_prefix "slider"
                        box_wrap True

                        vbox:

                            label _("Vitesse du texte"):
                                text_style "thunderstrike_lbl"

                            bar value Preference("text speed")

                            label _("Avance automatique"):
                                text_style "thunderstrike_lbl"

                            bar value Preference("auto-forward time")

                        vbox:

                            if config.has_music:
                                label _("Volume de la musique"):
                                    text_style "thunderstrike_lbl"

                                hbox:
                                    bar value Preference("music volume")

                            if config.has_sound:

                                label _("Volume du son"):
                                    text_style "thunderstrike_lbl"

                                hbox:
                                    bar value Preference("sound volume")

                                    if config.sample_sound:
                                        textbutton _("Test") action Play("sound", config.sample_sound)


        #                    if config.has_voice:
        #                        label _("Volume des voix")
        #
        #                        hbox:
        #                            bar value Preference("voice volume")
        #
        #                            if config.sample_voice:
        #                                textbutton _("Test") action Play("voice", config.sample_voice)

                            if config.has_music or config.has_sound or config.has_voice:
                                null height gui.pref_spacing

                                textbutton _("Couper tous les sons"):
                                    text_style "thunderstrike"
                                    action Preference("all mute", "toggle")
                                    style "mute_all_button"
    elif _preferences.language == "english":
                use game_menu_test(_("Settings"), scroll="viewport"):

                    vbox:

                        hbox:
                            box_wrap True

                            if renpy.variant("pc"):

                                vbox:

                                    #add Image("/background/menu_2.jpg", xpos = 0, ypos = 0)
                                    style_prefix "radio"
                                    label _("Display"):
                                        text_style "thunderstrike_lbl"
                                    textbutton _("Window"):
                                        text_style "thunderstrike"
                                        action Preference("display", "window")
                                    textbutton _("Full screen"):
                                        text_style "thunderstrike"
                                        action Preference("display", "fullscreen")

                            vbox:
                                style_prefix "radio"
                                label _("Rollback Side"):
                                    text_style "thunderstrike_lbl"
                                textbutton _("Deactivated"):
                                    text_style "thunderstrike"
                                    action Preference("rollback side", "disable")
                                textbutton _("Left"):
                                    text_style "thunderstrike"
                                    action Preference("rollback side", "left")
                                textbutton _("Right"):
                                    text_style "thunderstrike"
                                    action Preference("rollback side", "right")

                            vbox:
                                style_prefix "check"
                                label _("Skip"):
                                    text_style "thunderstrike_lbl"
                                textbutton _("unseen Text"):
                                    text_style "thunderstrike"
                                    action Preference("skip", "toggle")
                                textbutton _("After choices"):
                                    text_style "thunderstrike"
                                    action Preference("after choices", "toggle")
                                textbutton _("Transitions"):
                                    text_style "thunderstrike"
                                    action InvertSelected(Preference("transitions", "toggle"))

                            ## Des boites vbox additionnelles de type "radio_pref" ou
                            ## "check_pref" peuvent être ajoutées ici pour ajouter des
                            ## préférences définies par le créateur du jeuself.
                            vbox:
                                style_prefix "radio"
                                xalign 0.5
                                label _("Language"):
                                    text_style "thunderstrike_lbl"
                                imagebutton:
                                    idle "fr_icon"
                                    hover "fr_icon_hov"
                                    action Language(None)
                                imagebutton:
                                    idle "en_icon"
                                    hover "en_icon_hov"
                                    action Language("english")
                                #textbutton _("Spanish"):
                                    #text_style "thunderstrike
                                    #action Language("spanish()")
                                imagebutton:
                                    idle "de_icon"
                                    hover "de_icon_hov"
                                    action Language("Deutsch()")
                                #textbutton _("Russian"):
                                    #text_style "thunderstrike"
                                    #action Language("rus()")
                        null height (4 * gui.pref_spacing)

                        hbox:
                            style_prefix "slider"
                            box_wrap True

                            vbox:

                                label _("Text speed"):
                                    text_style "thunderstrike_lbl"

                                bar value Preference("text speed")

                                label _("Auto-forward time"):
                                    text_style "thunderstrike_lbl"

                                bar value Preference("auto-forward time")

                            vbox:

                                if config.has_music:
                                    label _("Music volume"):
                                        text_style "thunderstrike_lbl"

                                    hbox:
                                        bar value Preference("music volume")

                                if config.has_sound:

                                    label _("sound volume"):
                                        text_style "thunderstrike_lbl"

                                    hbox:
                                        bar value Preference("sound volume")

                                        if config.sample_sound:
                                            textbutton _("Test"):
                                                text_style "thunderstrike"
                                                action Play("sound", config.sample_sound)


            #                    if config.has_voice:
            #                        label _("Volume des voix")
            #
            #                        hbox:
            #                            bar value Preference("voice volume")
            #
            #                            if config.sample_voice:
            #                                textbutton _("Test") action Play("voice", config.sample_voice)

                                if config.has_music or config.has_sound or config.has_voice:
                                    null height gui.pref_spacing

                                    textbutton _("Mute all sounds"):
                                        text_style "thunderstrike"
                                        action Preference("all mute", "toggle")
                                        style "mute_all_button"




## Écran de l'historique #######################################################
##
## Il s’agit d’un écran qui affiche l’historique des dialogues au joueur. Bien
## qu’il n'y ait rien de spécial sur cet écran, il doit accéder à l’historique
## de dialogue stocké dans _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Cette instruction permet d’éviter de prédire cet écran, car il peut être
    ## très large
    predict False

    use game_menu_test(_("Historique"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Cela positionne correctement l'écran si history_height est
                ## initialisé à None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Utilise pour la couleur du texte, la couleur par
                        ## défaut des dialogues du personnage si elle a été
                        ## initialisée.
                        if "color" in h.who_args:
                            text_color h.who_args["black"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("L'historique des dialogues est vide."):
                text_style "thunderstrike_lbl"


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


## Écran d'aide ################################################################
##
## Cet écran fournit des informations sur les touches et les boutons de souris.
## En interne, il utilise d’autres écrans (keyboard_help, mouse_help et
## gamepad_help) pour afficher une aide dédiée.

screen help():

    tag menu

    default device = "keyboard"
    if _preferences.language == None:
        use game_menu_test(_("Aide"), scroll="viewport"):

            style_prefix "help"

            vbox:
                spacing 23

                hbox:

                    textbutton _("Clavier"):
                        text_style "thunderstrike"
                        action SetScreenVariable("device", "keyboard")
                    textbutton _("Souris"):
                        text_style "thunderstrike"
                        action SetScreenVariable("device", "mouse")

                    if GamepadExists():
                        textbutton _("Manette"):
                            text_style "thunderstrike"
                            action SetScreenVariable("device", "gamepad")

                if device == "keyboard":
                    use keyboard_help
                elif device == "mouse":
                    use mouse_help
                elif device == "gamepad":
                    use gamepad_help

    if _preferences.language == "english":
        use game_menu_test(_("Help"), scroll="viewport"):

            style_prefix "help"

            vbox:
                spacing 15

                hbox:

                    textbutton _("Keyboard"):
                        text_style "thunderstrike"
                        action SetScreenVariable("device", "keyboard")
                    textbutton _("Mouse"):
                        text_style "thunderstrike"
                        action SetScreenVariable("device", "mouse")

                    if GamepadExists():
                        textbutton _("Gamepad"):
                            text_style "thunderstrike"
                            action SetScreenVariable("device", "gamepad")

                if device == "keyboard":
                    use keyboard_help_eng
                elif device == "mouse":
                    use mouse_help_eng
                elif device == "gamepad":
                    use gamepad_help_eng


screen keyboard_help_eng():

    hbox:
        label _("Enter"):
            text_style "thunderstrike_lbl"
        text _("Advances dialogue and activates the interface."):
            style "thunderstrike_txt"

    hbox:
        label _("Space"):
            text_style "thunderstrike_lbl"
        text _("Advances dialogue without selecting choices."):
            style "thunderstrike_txt"

    hbox:
        label _("Arrow Keys"):
            text_style "thunderstrike_lbl"
        text _("Navigate the interface."):
            style "thunderstrike_txt"

    hbox:
        label _("Escape"):
            text_style "thunderstrike_lbl"
        text _("Accesses the game menu."):
            style "thunderstrike_txt"

    hbox:
        label _("Ctrl"):
            text_style "thunderstrike_lbl"
        text _("Skips dialogue while held down."):
            style "thunderstrike_txt"

    hbox:
        label _("Tab"):
            text_style "thunderstrike_lbl"
        text _("Toggles dialogue skipping."):
            style "thunderstrike_txt"

    hbox:
        label _("Page Up"):
            text_style "thunderstrike_lbl"
        text _("Rolls back to earlier dialogue."):
            style "thunderstrike_txt"

    hbox:
        label _("Page Down"):
            text_style "thunderstrike_lbl"
        text _("Rolls forward to later dialogue."):
            style "thunderstrike_txt"

    hbox:
        label _("H"):
            text_style "thunderstrike_lbl"
        text _("Hides the user interface."):
            style "thunderstrike_txt"

    hbox:
        label _("S"):
            text_style "thunderstrike_lbl"
        text _("Takes a screenshot."):
            style "thunderstrike_txt"

    hbox:
        label _("V"):
            text_style "thunderstrike_lbl"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}{font=fonts/thunderstrikeitalic.ttf}self-voicing{/font}{/a}."):
            style "thunderstrike_txt"


screen mouse_help_eng():

    hbox:
        label _("Left Click"):
            text_style "thunderstrike_lbl"
        text _("Advances dialogue and activates the interface."):
            style "thunderstrike_txt"

    hbox:
        label _("Middle Click"):
            text_style "thunderstrike_lbl"
        text _("Hides the user interface."):
            style "thunderstrike_txt"

    hbox:
        label _("Right Click"):
            text_style "thunderstrike_lbl"
        text _("Accesses the game menu."):
            style "thunderstrike_txt"

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side"):
            text_style "thunderstrike_lbl"
        text _("Rolls back to earlier dialogue."):
            style "thunderstrike_txt"

    hbox:
        label _("Mouse Wheel Down"):
            text_style "thunderstrike_lbl"
        text _("Rolls forward to later dialogue."):
            style "thunderstrike_txt"


screen gamepad_help_eng():

    hbox:
        label _("Right Trigger\nA/Bottom Button"):
            text_style "thunderstrike_lbl"
        text _("Advances dialogue and activates the interface."):
            style "thunderstrike_txt"

    hbox:
        label _("Left Trigger\nLeft Shoulder"):
            text_style "thunderstrike_lbl"
        text _("Rolls back to earlier dialogue."):
            style "thunderstrike_txt"

    hbox:
        label _("Right Shoulder"):
            text_style "thunderstrike_lbl"
        text _("Rolls forward to later dialogue."):
            style "thunderstrike_txt"


    hbox:
        label _("D-Pad, Sticks"):
            text_style "thunderstrike_lbl"
        text _("Navigate the interface."):
            style "thunderstrike_txt"

    hbox:
        label _("Start, Guide"):
            text_style "thunderstrike_lbl"
        text _("Accesses the game menu."):
            style "thunderstrike_txt"

    hbox:
        label _("Y/Top Button"):
            text_style "thunderstrike_lbl"
        text _("Hides the user interface."):
            style "thunderstrike_txt"

    textbutton _("Calibrate"):
        text_style "thunderstrike"
        action GamepadCalibrate()



screen keyboard_help():

    hbox:
        label _("Entrée"):
            text_style "thunderstrike_lbl"
        text _("Avance dans les dialogues et active l’interface (effectue un choix)."):
            style "thunderstrike_txt"

    hbox:
        label _("Espace"):
            text_style "thunderstrike_lbl"
        text _("Avance dans les dialogues sans effectuer de choix."):
            style "thunderstrike_txt"

    hbox:
        label _("Flèches directionnelles"):
            text_style "thunderstrike_lbl"
        text _("Permet de se déplacer dans l’interface."):
            style "thunderstrike_txt"

    hbox:
        label _("Echap."):
            text_style "thunderstrike_lbl"
        text _("Ouvre le menu du jeu."):
            style "thunderstrike_txt"

    hbox:
        label _("Ctrl"):
            text_style "thunderstrike_lbl"
        text _("Fait défiler les dialogues tant que la touche est pressée."):
            style "thunderstrike_txt"

    hbox:
        label _("Tab"):
            text_style "thunderstrike_lbl"
        text _("Active ou désactives les «sauts des dialogues»."):
            style "thunderstrike_txt"

    hbox:
        label _("Page Haut"):
            text_style "thunderstrike_lbl"
        text _("Retourne au précédent dialogue."):
            style "thunderstrike_txt"

    hbox:
        label _("Page Bas"):
            text_style "thunderstrike_lbl"
        text _("Avance jusqu'au prochain dialogue."):
            style "thunderstrike_txt"

    hbox:
        label _("H"):
            text_style "thunderstrike_lbl"
        text _("Cache l’interface utilisateur."):
            style "thunderstrike_txt"

    hbox:
        label _("S"):
            text_style "thunderstrike_lbl"
        text _("Prend une capture d’écran."):
            style "thunderstrike_txt"

    hbox:
        label _("V"):
            text_style "thunderstrike_lbl"
        text _("Active la {a=https://www.renpy.org/l/voicing}{size=24}{font=fonts/thunderstrikeitalic.ttf}vocalisation automatique{/font}{/size}{/a}."):
            style "thunderstrike_txt"


screen mouse_help():

    hbox:
        label _("Bouton gauche"):
            text_style "thunderstrike_lbl"
        text _("Avance dans les dialogues et active l’interface (effectue un choix)."):
            style "thunderstrike_txt"

    hbox:
        label _("Bouton central"):
            text_style "thunderstrike_lbl"
        text _("Cache l’interface utilisateur."):
            style "thunderstrike_txt"

    hbox:
        label _("Bouton droit"):
            text_style "thunderstrike_lbl"
        text _("Ouvre le menu du jeu."):
            style "thunderstrike_txt"

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side"):
            text_style "thunderstrike_lbl"
        text _("Retourne au précédent dialogue."):
            style "thunderstrike_txt"

    hbox:
        label _("Molette vers le bas"):
            text_style "thunderstrike_lbl"
        text _("Avance jusqu'au prochain dialogue."):
            style "thunderstrike_txt"


screen gamepad_help():

    hbox:
        label _("Bouton R1\nA/Bouton du bas"):
            text_style "thunderstrike_lbl"
        text _("Avance dans les dialogues et active l’interface (effectue un choix)."):
            style "thunderstrike_txt"

    hbox:
        label _("Left Trigger\nLeft Shoulder"):
            text_style "thunderstrike_lbl"
        text _("Retourne au précédent dialogue."):
            style "thunderstrike_txt"

    hbox:
        label _("Bouton R1"):
            text_style "thunderstrike_lbl"
        text _("Avance jusqu'au prochain dialogue."):
            style "thunderstrike_txt"


    hbox:
        label _("Boutons directionnels, stick gauche"):
            text_style "thunderstrike_lbl"
        text _("Permet de se déplacer dans l’interface."):
            style "thunderstrike_txt"

    hbox:
        label _("Start, Guide"):
            text_style "thunderstrike_lbl"
        text _("Ouvre le menu du jeu."):
            style "thunderstrike_txt"

    hbox:
        label _("Y/Bouton du haut"):
            text_style "thunderstrike_lbl"
        text _("Cache l’interface utilisateur."):
            style "thunderstrike_txt"

    textbutton _("Calibrage"):
        text_style "thunderstrike"
        action GamepadCalibrate()




################################################################################
## Écrans additionnels
################################################################################


## Écran de confirmation #######################################################
##
## Cet écran est appelé quand Ren'Py souhaite poser une question au joueur dont
## la réponse est oui ou non.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Cette instruction s’assure que les autres écrans resteront en arrière
    ## plan tant que cet écran sera affiché.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                vbox:
                    textbutton _("Oui"):
                        text_style "yes_button_confirm"
                        action yes_action
                vbox:
                    textbutton _("Non"):
                        text_style "no_button_confirm"
                        action no_action


    ## Le clic bouton droit et la touche Echap. correspondent à la réponse
    ## "non".
    key "game_menu" action no_action

style yes_button_confirm:
    idle_color "#0ddb1e"
    hover_color "#e34b00"
    size 30

style no_button_confirm:
    idle_color "#e34b00"
    hover_color "#0ddb1e"
    size 30





## Écran de l’indicateur d'avance rapide #######################################
##
## L’écran skip_indicator est affiché pour indiquer qu’une avance rapide est en
## cours.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Je rate Quelque chose")

            text "." at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "." at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "." at delayed_blink(0.4, 1.0) style "skip_triangle"


## Cette transformation est utilisé pour faire clignoter les flèches l’une après
## l’autre.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat



## Écran de notification #######################################################
##
## Cet écran est utilisé pour affiché un message au joueur. (Par exemple, quand
## une sauvegarde rapide a eu lieu ou quand une capture d’écran vient d’être
## réalisée.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0



## Écran NVL ###################################################################
##
## Cet écran est utilisé pour les dialogues et les menus en mode NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Les dialogues sont affichés soit dans une vpgrid soit dans une vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Si fourni, affiche le menu. Le menu peut s’afficher de manière
        ## incorrecte si config.narrator_menu est initialisé à True, comme c’est
        ## le cas au-dessus.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Ce paramètre controle le maximum d’entrée dans le mode NVL qui peuvent être
## affichée simultanément.
define config.nvl_list_length = gui.nvl_list_length



################################################################################
## Variantes pour les mobiles
################################################################################

## Comme la souris peut ne pas être présente, nous remplaçons le menu rapide
## avec une version qui utilise des boutons plus gros et qui sont plus faciles à
## toucher du doigt.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 1.0
            yalign 1.0

            imagebutton:
                idle "sett_ico"
                hover "sett_ico_hover"
                selected_idle "sett_clicked"
                selected_hover "sett_clicked"
                action ToggleScreen("quick_menu_showed")
screen quick_menu_showed():
    variant "touch"

    frame:
        background "07alpha_black_bg"
        xalign .95
        yalign 1.0
        vbox:
            style_prefix "quick"

            textbutton _("Retour") action Rollback()
            textbutton _("Avance R.") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Sauvegarde R.") action QuickSave()
            textbutton _("Para.") action ShowMenu('preferences')
            textbutton _("Quêtes") action ShowMenu(log.screen())



if _preferences.language == "english":

    screen money_displayeng():

        $ day_number = (day%7)
        $ day_name_values = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
        $ dayn = day_name_values[day_number]

        $ dtime_number = (dtime%6)
        $ dtime_name_values = ("Early mor.", "Morning", "Noon", "Afternoon", "Night", "Late night")
        $ dtimen = dtime_name_values[dtime_number]

        vbox:
            xalign .01 #change this value between 0 and 1 if you want to move it to a different part of the screen horizontally
            yalign .01 #change this value if you want to move it to a different part of the screen vertically

            text "Money: $[money] Day N°:[day] - [dayn] - [dtimen]" #this will show your money points variable, you can add extra parameters such as font type, size, alignment etc

if _preferences.language == None:


    screen money_display():
        $ day_number = (day%7)
        $ day_name_values = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche")
        $ dayn = day_name_values[day_number]

        $ dtime_number = (dtime%6)
        $ dtime_name_values = ("Aube", "Matin", "Midi", "Après midi", "Soir", "Nuit")
        $ dtimen = dtime_name_values[dtime_number]
        $ hours_number = (hour%24)
        $ hour_values = ("1h", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "10h", "11h", "12h", "13h", "14h", "15h", "16h", "17h", "18h", "19h", "20h", "21h", "22h", "23h", "24h")
        $ hours_values = hour_values[hours_number]
        vbox:
            xalign .01 #change this value between 0 and 1 if you want to move it to a different part of the screen horizontally
            yalign .01 #change this value if you want to move it to a different part of the screen vertically

            text "Argent: [money]€ | Jour [day] | [dayn], [dtimen] | [hours_values]" #this will show your money points variable, you can add extra parameters such as font type, size, alignment etc
            text "| [string_fatigue] | [string_faim]"
            textbutton "Journal de Quêtes" text_color "#ffffff" text_hover_color "#f9300c" action ShowMenu(log.screen()) text_size 19
else:
    screen money_displayinc():
        image "moneyhud"
        $ day_number = (day%7)
        $ day_name_values = ("?????", "?????", "?????", "?????", "??????", "???????", "???????")
        $ dayn = day_name_values[day_number]

        $ dtime_number = (dtime%6)
        $ dtime_name_values = ("???????", "????????", "???????", "???????", "??????", "?????")
        $ dtimen = dtime_name_values[dtime_number]

        vbox:
            xalign .01 #change this value between 0 and 1 if you want to move it to a different part of the screen horizontally
            yalign .01 #change this value if you want to move it to a different part of the screen vertically

            text "???????: [money]?   ?????? N°:[day] - [dayn] - [dtimen] " #this will show your money points variable, you can add extra parameters such as font type, size, alignment etc

if hour_values > 23:
    $ day += 1
