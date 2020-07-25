screen Startabout(txt):
    text _(txt):
        style "Startabouttext"
    text _(u"[tiptoadvance]"):
        style "tip"

screen attbugs_fr():
    text _("ATTENTION, le jeu est encore en développement alors\n soyez compréhensif"):
        style "Startabouttext"
        xpos .1
        ypos .1
    text _("Merci d'avance"):
        style "Startabouttext"
        xpos .1
        ypos .4
    text _("Suivant >>>"):
        style "startaboutstyle"
        xpos .6
        ypos .5
    text _("Cordialement,"):
        style "Startabouttext"
        xpos .1
        ypos .7
    text _("Unknown Games"):
        style "Startabouttext"
        xpos .1
        ypos .8
    text _(u"[tiptoadvance]"):
        style "tip"

screen Warn_Vers():
    vbox:
        text _("""By having downloaded the game you accepted the contract !! \n
    The version you have is still in development and is strictly managed by Unknown Games
    You are only allowed to test the new features and the UI, for any modifications of this contract contact {a=mailto:unknowngamesoff@gmail.com}Unknown Games{/a}
        """):
            style "WarnVersText"
        textbutton _("Continue"):
            xpos .5
            action Jump("ShowWhatLang")

screen What_lang():
        imagemap:
            idle "gui/lang_test2.png"
            hover "gui/lang_test2_hover.png"

            hotspot(752, 0, 525, 719) action [SetLocalVariable("langcheck", "True"), Language("english"), ShowMenu("showDevlog")]
            hotspot(0, 0, 446, 719) action [SetLocalVariable("langcheck", "True"), Language(None), ShowMenu("showDevlog")]


        text _("What's your language ?"):
            style "langlbl"


screen Devlog(scroll="auto", yinitial=0.0):
    modal True
    zorder 200
    add "main_menu_bg"
    vbox:
        spacing 45
        hbox:
            style "devhbox"
            if _preferences.language == None:
                text _("Devlog de {color=#f9300c}Zombie Apocalypse{/color}"):
                    style "Devlogtitle"
            else:
                text _("Devlog of {color=#f9300c}Zombie Apocalypse{/color}"):
                    style "Devlogtitle"
            button:
                action [SetLocalVariable("persistent.fstcheck", "True"),MainMenu(confirm=main_menu)]
                style "devcls_btn"
                if _preferences.language == None:
                    text _("Fermer"):
                        style "devcls_btntxt"
                elif _preferences.language == "english":
                    text _("Close"):
                        style "devcls_btntxt"
        hbox:
            vbox:
                style "devleft"

                image "update_release_resized"
            image "devbar"
            vbox:
                style "devright"

                if _preferences.language == None:
                    text _("""
La nouveauté dans la 2.1:

    - L'interface graphique a été revue et refaite
    - Les dialogues sont plus fluides et sont plus cohérents !
    - Les PNJ sont plus intelligents et leur dialogues ont étés retravaillés !
    - Intégration totale de l'Anglais
    - De nouvelles fonctionnalités ont étés établies, allez donc faire un tour dans les paramètres pour voir.
    - Vous pouvez maintenant choisir entre trois difficultés qui auront chacunes des impacts dans le gameplay

    Il y a encore d'autres ajouts mais je vous laisse les découvrir par vous même

Ce devlog a été écrit par Centaurus
                        """):
                        style "Devtext"
                else:
                    text _("""
What's new in the 2.1:

    - The entire GUI has been re made
    - Dialogs are more fluids and coherents !
    - PNJs are more clever and their dialogs were remade !
    - English is now totally integrated !!
    - New features added, go check the settings tab to see by yourself
    - You can now choose between thre difficulties wich are impacting the gameplay

    And there's more adding but I'll let you see it by yourself

This devlog is written by Centaurus

                        """):
                        style "Devtext"

screen Unktxt():
    text _("Unknown Games"):
        style "unkstyle"


screen Prestxt():
    text _("Presents"):
        style "Preststyle"

screen hgzatitle():
    text _("Zombie Apocalypse"):
        style "Gametitle"

screen mdewthrnpy():
    vbox:
        style "centered"

        text _("A game made with Ren'py")

        image "Renpy logo"



label ShowWhatLang:
    call screen What_lang()

label showDevlog:
    call screen Devlog()
