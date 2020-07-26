## Écran du menu principal #####################################################
##
## Utilisé pour afficher le menu principal quand Ren'Py démarre.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu
screen main_menu():
    default hoverof = None
    ## This ensures that any other menu screen is replaced.
    tag menu
    imagemap:
        ground "mainmenubg"
        if renpy.variant("pc"):
            if _preferences.language == None:
                idle "gui/main_menu.png"
                hover "gui/main_menu.png"
            elif _preferences.language == "english":
                idle "gui/main_menuen.png"
                hover "gui/main_menuen.png"

        if _preferences.language == None:
            text _("Zombie Apocalypse"):
                style "game_title"
        elif _preferences.language == "english":
            text _("Zombie Apocalypse"):
                style "game_title"

        vbox:
            style "my_main_menu_vbox"
            #imagebutton:
                #idle "gui/button/mainmenu_bg.png"
                #hover "gui/button/mainmenu_bg_hover.png"
            button:
                hovered SetLocalVariable("hoverof", "start")
                unhovered SetLocalVariable("hoverof", None)
                action Start()
                hbox:
                    showif hoverof == "start":
                        add "mainmenu_anim_hover_start"
                    else:
                        image "gui/button/mainmenu_bg.png"

            button:
                yoffset -8
                hovered SetLocalVariable("hoverof", "load")
                unhovered SetLocalVariable("hoverof", None)
                action ShowMenu("load")
                hbox:
                    showif hoverof == "load":
                        add "mainmenu_anim_hover_load"
                    else:
                        image "gui/button/mainmenu_bg.png"
            button:
                yoffset -16
                hovered SetLocalVariable("hoverof", "prefs")
                unhovered SetLocalVariable("hoverof", None)
                action ShowMenu("preferences")
                hbox:
                    showif hoverof == "prefs":
                        add "mainmenu_anim_hover_prefs"
                    else:
                        image "gui/button/mainmenu_bg.png"
            if renpy.variant("pc"):

                button:
                    yoffset -24
                    hovered SetLocalVariable("hoverof", "help")
                    unhovered SetLocalVariable("hoverof", None)
                    action ShowMenu("help")
                    hbox:
                        showif hoverof == "help":
                            add "mainmenu_anim_hover_help"
                        else:
                            image "gui/button/mainmenu_bg.png"

            button:
                yoffset -32
                hovered SetLocalVariable("hoverof", "about")
                unhovered SetLocalVariable("hoverof", None)
                action ShowMenu("about")
                hbox:
                    showif hoverof == "about":
                        add "mainmenu_anim_hover_about"
                    else:
                        image "gui/button/mainmenu_bg.png"

            button:
                yoffset 20
                hovered SetLocalVariable("hoverof", "quit")
                unhovered SetLocalVariable("hoverof", None)
                action Quit(confirm=not main_menu)
                hbox:
                    showif hoverof == "quit":
                        add "mainmenu_anim_hover_quit"
                    else:
                        image "gui/button/mainmenu_bg.png"

        hotspot(513, 151, 275, 63) hovered SetLocalVariable("hoverof", "start") unhovered SetLocalVariable("hoverof", None) action Start()
        hotspot(568, 210, 182, 50) hovered SetLocalVariable("hoverof", "load") unhovered SetLocalVariable("hoverof", None) action ShowMenu("load")
        hotspot(527, 265, 251, 45) hovered SetLocalVariable("hoverof", "prefs") unhovered SetLocalVariable("hoverof", None) action ShowMenu("preferences")
        hotspot(591, 314, 138, 44) hovered SetLocalVariable("hoverof", "help") unhovered SetLocalVariable("hoverof", None) action ShowMenu("help")
        hotspot(549, 360, 205, 47) hovered SetLocalVariable("hoverof", "about") unhovered SetLocalVariable("hoverof", None) action ShowMenu("about")
        hotspot(568, 466, 170, 46) hovered SetLocalVariable("hoverof", "quit") unhovered SetLocalVariable("hoverof", None) action Quit(confirm=not main_menu)
        vbox:
            style "main_menu_version_txt"
            if _preferences.language == None or _preferences.language == "english":
                text _("[current.version!q]"):
                    style "main_menu_version_txt"
            frame:
                style "lang_choice"

                hbox:
                    imagebutton:
                        idle "fr_icon"
                        hover "fr_icon_hov"
                        selected_idle "fr_icon_hov"
                        action Language(None)
                    imagebutton:
                        idle "en_icon"
                        hover "en_icon_hov"
                        selected_idle "en_icon_hov"
                        action Language("english")
                    #imagebutton:
                        #idle "de_icon"
                        #hover "de_icon_hov"
        text _("[current.statement!q]"):
            style "main_menu_statement"
    if _preferences.language == None:
        if res_icons:
            vbox:
                style "Res_icons"
                imagebutton:
                    idle "discord_icon idle"
                    hover "discord_icon hover"
                    action OpenURL("https://discord.gg/pQg85M")
                imagebutton:
                    idle "twitter_icon idle"
                    hover "twitter_icon hover"
                    action OpenURL("https://twitter.com/UnknownGames12")
                imagebutton:
                    idle "insta_icon idle"
                    hover "insta_icon hover"
                    action OpenURL("https://www.instagram.com/unknowngames_off/")
                imagebutton:
                    idle "patreon_icon idle"
                    hover "patreon_icon hover"
                    action OpenURL("https://www.patreon.com/unknowngames_off")
        else:
            vbox:
                style "Res_buttons"
                imagebutton:
                    idle "butt_discordfr_idle"
                    hover "butt_discord_hover"
                    action OpenURL("https://discord.gg/pQg85M")
                imagebutton:
                    idle "butt_twitterfr_idle"
                    hover "butt_twitter_hover"
                    action OpenURL("https://twitter.com/UnknownGames12")
                imagebutton:
                    idle "butt_instafr_idle"
                    hover "butt_insta_hover"
                    action OpenURL("https://www.instagram.com/unknowngames_off/")
                imagebutton:
                    idle "butt_patreonfr_idle"
                    hover "butt_patreon_hover"
                    action OpenURL("https://www.patreon.com/unknowngames_off")
    elif _preferences.language == "english":
        if res_icons:
            vbox:
                style "Res_icons"
                imagebutton:
                    idle "discord_icon idle"
                    hover "discord_icon hover"
                    action OpenURL("https://discord.gg/pQg85M")
                imagebutton:
                    idle "twitter_icon idle"
                    hover "twitter_icon hover"
                    action OpenURL("https://twitter.com/UnknownGames12")
                imagebutton:
                    idle "insta_icon idle"
                    hover "insta_icon hover"
                    action OpenURL("https://www.instagram.com/unknowngames_off/")
                imagebutton:
                    idle "patreon_icon idle"
                    hover "patreon_icon hover"
                    action OpenURL("https://www.patreon.com/unknowngames_off")
        else:
            vbox:
                style "Res_buttons"
                imagebutton:
                    idle "butt_discorden_idle"
                    hover "butt_discord_hover"
                    action OpenURL("https://discord.gg/pQg85M")
                imagebutton:
                    idle "butt_twitteren_idle"
                    hover "butt_twitter_hover"
                    action OpenURL("https://twitter.com/UnknownGames12")
                imagebutton:
                    idle "butt_instaen_idle"
                    hover "butt_insta_hover"
                    action OpenURL("https://www.instagram.com/unknowngames_off/")
                imagebutton:
                    idle "butt_patreonen_idle"
                    hover "butt_patreon_hover"
                    action OpenURL("https://www.patreon.com/unknowngames_off")
