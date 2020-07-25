## Écran des préférences #######################################################
##
## L’écran de préférence permet au joueur de configurer le jeu pour mieux
## correspondre à ses attentes.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    default affichage_screen = False
    default text_screen = False
    default narr_screen = False
    tag menu
    if _preferences.language == None:
            use game_menu_test(_("Paramètres"), scroll="viewport"):

                vbox:

                    vbox:
                        box_wrap True
                        frame:
                            style "prefs_widget"
                            vbox:
                                if renpy.variant("pc"):
                                    if not affichage_screen:
                                        textbutton _("Paramètres d'Affichage +"):
                                            style "widget_button"
                                            action ToggleLocalVariable("affichage_screen")
                                    else:
                                        textbutton _("Paramètres d'Affichage -"):

                                            action ToggleLocalVariable("affichage_screen")

                                if affichage_screen:
                                    vbox:
                                        hbox:
                                            vbox:

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
                                                label _("Tooltip"):
                                                    text_style "thunderstrike_lbl"
                                                hbox:
                                                    textbutton _("Activé"):
                                                        text_style "thunderstrike"
                                                        action SetVariable("tooltip_var", "activated")
                                                    textbutton _("Désactivé"):
                                                        text_style "thunderstrike"
                                                        action SetVariable("tooltip_var", "deactivated")
                                            vbox:
                                                style_prefix "radio"
                                                label _("Reseaux Sociaux\n Boutons / Icônes"):
                                                    text_style "thunderstrike_lbl"
                                                if res_icons:
                                                    textbutton _("Boutons"):
                                                        text_style "thunderstrike_spebtn"
                                                        action ToggleVariable("res_icons")
                                                else:
                                                    textbutton _("Icônes"):
                                                        text_style "thunderstrike_spebtn"
                                                        action ToggleVariable("res_icons")

                        frame:
                            style "prefs_widget"
                            vbox:
                                if not text_screen:
                                    textbutton _("Paramètres du texte +"):

                                        action ToggleLocalVariable("text_screen")
                                else:
                                    textbutton _("Paramètres du texte -"):

                                        action ToggleLocalVariable("text_screen")


                                if text_screen:
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

                        frame:
                            style "prefs_widget"

                            vbox:

                                if not narr_screen:
                                    textbutton _("Paramètres de Narration +"):
                                        action ToggleLocalVariable("narr_screen")
                                else:
                                    textbutton _("Paramètres de Narration -"):
                                        action ToggleLocalVariable("narr_screen")

                                if narr_screen:
                                    vbox:
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
                                imagebutton:
                                    idle "de_icon"
                                    hover "de_icon_hov"

                            vbox:
                                style_prefix "radio"
                                label _("Social Networks\n Buttons / Icons"):
                                    text_style "thunderstrike_lbl"
                                if res_icons:
                                    textbutton _("Buttons"):
                                        text_style "thunderstrike_spebtn"
                                        action ToggleVariable("res_icons")
                                else:
                                    textbutton _("Icons"):
                                        text_style "thunderstrike_spebtn"
                                        action ToggleVariable("res_icons")

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


                                if config.has_music or config.has_sound or config.has_voice:
                                    null height gui.pref_spacing

                                    textbutton _("Mute all sounds"):
                                        text_style "thunderstrike"
                                        action Preference("all mute", "toggle")
                                        style "mute_all_button"

style prefs_widget:
    background "08alpha_black_bg"
    size 60
style widget_button:
    size 80
