screen statsbar():
    zorder 200
    window:
        style "statswindow"
        frame:
            style "statsframe"
            hbox:
                if points_faim >= 0 and points_faim <= 25:
                    image "hunger_full"
                elif points_faim > 25 and points_faim <= 50:
                    image "hunger_nearly_full"
                elif points_faim > 50 and points_faim <= 75:
                    image "hunger_middle"
                elif points_faim > 75 and points_faim < 100:
                    image "hunger_nearly_empty"
                elif points_faim == 100:
                    image "hunger_empty"
                default faimpt = 100 - points_faim
                text _("[faimpt]/100")

                if points_soif >= 0 and points_soif <= 25:
                    image "thirst_full"
                elif points_soif > 25 and points_soif <= 50:
                    image "thirst_nearly_full"
                elif points_soif > 50 and points_soif <= 75:
                    image "thirst_middle"
                elif points_soif > 75 and points_soif < 100:
                    image "thirst_nearly_empty"
                elif points_soif == 100:
                    image "thirst_empty"
                default soifpt = 100 - points_soif
                text _("[soifpt]/100")

                if energy >= 0 and energy <= 5:
                    image "energy_empty"
                elif energy > 5 and energy <= 50:
                    image "energy_nearly_empty"
                elif energy > 50 and energy <= 75:
                    image "energy_middle"
                elif energy > 75 and energy < 100:
                    image "energy_nearly_full"
                elif energy == 100:
                    image "energy_full"
                text _("[energy]/100")

                python:
                    day_number = (day%7)
                    day_name_values = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche")
                    dayn = day_name_values[day_number]

                    dtime_number = (dtime%6)
                    dtime_name_values = ("Aube", "Matin", "Midi", "Après midi", "Soir", "Nuit")
                    dtimen = dtime_name_values[dtime_number]
                    hours_number = (hour%24)
                    hour_values = ("1h", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "10h", "11h", "12h", "13h", "14h", "15h", "16h", "17h", "18h", "19h", "20h", "21h", "22h", "23h", "24h")
                    hours_values = hour_values[hours_number]

                text _(" [dayn], [hours_values], Jour [day]"):
                    xpos 1.0
            imagebutton:
                idle "menu_idle"
                hover "menu_hover"
                style "menubutton"
                action ToggleScreen("MenuScreenOptions")

screen MenuScreenOptions():
    zorder 200
    frame:
        style "MenuOptions"
        vbox:
            textbutton _("Paramètres"):
                text_style "MenuOptionsText"
                action ShowMenu('preferences')
            textbutton _("Sauvegarder R."):
                text_style "MenuOptionsText"
                action QuickSave()
            textbutton _("Charger R."):
                text_style "MenuOptionsText"
                action QuickLoad()
            textbutton _("Tricher"):
                text_style "MenuOptionsText"
                action [Hide("MenuScreenOptions"), Jump("firstcheatscreen")]




screen cheatscreen(*val):
    if not val:
        default cheatfor = None
    else:
        default cheatfor = val
    zorder 200
    window:
        background "07alpha_black_bg"
        style "cheatwindow"
        frame:
            style "cheatframe"

            hbox:
                vbox:
                    hbox:
                        viewport:
                            scrollbars "horizontal"
                            mousewheel True
                            draggable True

                            side_xfill True
                            hbox:
                                textbutton _("Admin"):
                                    action SetLocalVariable("cheatfor", "admin")
                                textbutton _("Moi"):
                                    action SetLocalVariable("cheatfor", "mc")
                                textbutton _("Alexis"):
                                    action SetLocalVariable("cheatfor", "alex")
                                textbutton _("Clara"):
                                    action SetLocalVariable("cheatfor", "clara")
                                textbutton _("Jennifer"):
                                    action SetLocalVariable("cheatfor", "jenn")
                                textbutton _("Mathilde"):
                                    action SetLocalVariable("cheatfor", "mathilde")
                                textbutton _("Maximilian"):
                                    action SetLocalVariable("cheatfor", "max")
                                textbutton _("Zya"):
                                    action SetLocalVariable("cheatfor", "zya")
                                textbutton _("Mac'n Sell"):
                                    action SetLocalVariable("cheatfor", "macnsell")
                                textbutton _("Unknown Character"):
                                    action NullAction()
                                textbutton _("Unknown Character"):
                                    action NullAction()
                        textbutton _("X"):
                            style "CheatClsBtn"
                            text_style "CheatClsBtnText"
                            action [Hide("cheatscreen"), Return()]
                    hbox:
                        if cheatfor == "admin":
                            vbox:
                                label _("Admin Tools"):
                                    style "cheatlabel"
                                hbox:
                                    textbutton _("Console"):
                                        clicked _console.enter
                        elif cheatfor == "mc":
                            hbox:
                                vbox:
                                    label _("Hunger"):
                                        style "cheatlabel"
                                    hbox:
                                        ##Test in Python
                                        #python:
                                        #    ui.textbutton("- 10", clicked=change_stat(hungry, 10))
                                        textbutton _("- 10"):
                                            clicked Function(change_stat, hungry, 10)
                                            #clicked Call("add_hunger10")
                                        textbutton _("+ 10"):
                                            #clicked Function(change_stat, hungry, -10)
                                            clicked Call("sust_hunger10")
                                    label _("Thirst"):
                                        style "cheatlabel"
                                    hbox:
                                        textbutton _("- 10"):
                                            clicked Call("add_thirst10")
                                        textbutton _("+ 10"):
                                            clicked Call("sust_thirst10")
                                    label _("Energy"):
                                        style "cheatlabel"
                                    hbox:
                                        textbutton _("- 10"):
                                            clicked Call("sust_energy10")
                                        textbutton _("+ 10"):
                                            clicked Call("add_energy10")
                                vbox:
                                    label _("Hours"):
                                        style "cheatlabel"
                                    hbox:
                                        textbutton _("+ 1"):
                                            action Call("add_hour1")


                        elif cheatfor == "alex":
                            vbox:
                                label _("Love"):
                                    style "cheatlabel"
                                hbox:
                                    textbutton _("+")#:
                                        #action Function(LovePlus)
                                    textbutton _("-")#:
                                        #action Function(LoveMinus)
                            image "devbarmini"
                            vbox:
                                label _("Suspicion"):
                                    style "cheatlabel"
                                hbox:
                                    textbutton _("+")#:
                                        #action Function(SuspPlus)
                                    textbutton _("-")#:
                                        #action Function(SuspMinus)


                        elif cheatfor == "clara":
                            text _("Cheats for Clara are enabled")
                        elif cheatfor == "jenn":
                            text _("Cheats for Jennfier are enabled")
                        elif cheatfor == "mathilde":
                            text _("Cheats for Mathilde are enabled")
                        elif cheatfor == "max":
                            text _("Cheats for Maximilian are enabled")
                        elif cheatfor == "zya":
                            text _("Cheats for Zya are enabled")
                        elif cheatfor == "macnsell":
                            text _("Cheats for Mac'n Sell are enabled")
                        else:
                            text _("Cheats aren't enabled.... You need to chose one of the characters available")

screen clock6():
    image "clock6"

style cheatlabel:
    color "#ffffff"

style CheatClsBtn:
    xalign .5

style CheatClsBtnText:
    size 20
    idle_color "#ffffff"
    hover_color "#f9300c"

style MenuOptionsText:
    size 15
    idle_color "#ffffff"
    hover_color "#f9300c"

style cheatframe:
    background None
    xsize 580
    ysize 50

style cheatwindow:
    background "07alpha_black_bg"
    xalign .5
    yalign .3
    xsize 600
    ysize 300

style statswindow:
    background "data/images/pc/ui/statsbar_vers3.png"

style statsframe:
    background None
    xsize 1110
    ysize 40
    xpos .08
style menubutton:
    yoffset -20
    xalign 1.0

style MenuOptions:
    background "07alpha_black_bg"
    xalign .96
    yalign .065
