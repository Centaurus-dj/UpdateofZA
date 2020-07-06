screen Startabout():
    text _("C'est très important !"):
        style "Startabouttext"
    text _(u"[tiptoadvance]"):
        style "tip"


screen Startaboutcont():
    text _("Tu as entre tes mains une version qui n'est disponible que pour mes collaborateurs"):
        style "Startabouttext"
    text _(u"[tiptoadvance]"):
        style "tip"


screen Startaboutcont2():
    text _("""
    La version de ce jeu NE DOIT EN AUCUN CAS être PARTAGÉE ou \nDONNÉE à une
    quelconque personne sans la permission de Unknown Games et du créateur de ce jeu !
    """):
        style "Startabouttext"
        xpos .1
        ypos .1
    text _(u"[tiptoadvance]"):
        style "tip"


screen Startaboutcont3():
    text _("Je vous remercie d'avance de votre compréhension"):
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


screen reshist_fr():
    text _("""

    Nous sommes en 2038, la technologie n'a pas beaucoup évolué contrairement
    à ce que l'on voulait et s'attendait.

    Les entreprises spaciales comme SpaceX ont envoyé des Hommes sur Mars et
    ont construit des colonies et des usines pour extraire les ressources qu'il y a sur Mars...

    Mais un jour, lors d'une livraison banale de fer venant de Mars jusqu'à la Terre,
    un petit invité s'est incrusté dans la cargaison, c'était un virus qui s'était
    retrouvé bloqué dans la glace se situant près du minerai de fer.

    Quand il arriva sur Terre, ce fut une catastrophe !
    Ce virus prenait le contrôle des fonctions nerveuse en s'installant dans le crâne
    de son hôte.


    Nous sommes à peine un mois plus tard et toute la civilisation humaine est en train
    de s'éffondrer.
    """):
        style "reshist_style_size"
    text _(u"[tiptoadvance]"):
        style "tip"


screen reshist2_fr():
    vbox:
        style "reshist_style_place"

        text _("""

        Voilà dans quel monde tu vis maintenant !

        Est-ce que tu dois mourir et tomber comme tous les autres humains sur cette planète ?

                                        Ou

        Est-ce que tu vas survivre pour rebatir la civilisation d'autre fois ?


        Je te laisse décider

        """):
            style "reshist_style_size"

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
        vbox:
            style "langlbl"

            text _("What's your language ?"):
                style "langlbl"
            hbox:
                imagebutton:
                    idle "fr_icon"
                    hover "fr_icon_hov"
                    style "BigNextButton"
                    action [SetLocalVariable("langcheck", "True"), Language(None), ShowMenu("showDevlog")]
                image "devbarmini" xpos 99.0 ypos 1.0
                imagebutton:
                    idle "en_icon"
                    hover "en_icon_hov"
                    style "BigNextButton"
                    action [Language("english"), ShowMenu("showDevlog"), SetLocalVariable("langcheck", "True")]


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


label ShowWhatLang:
    call screen What_lang()

label showDevlog:
    call screen Devlog()
