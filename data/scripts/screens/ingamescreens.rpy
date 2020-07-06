screen Choix_genre():
    vbox:
        style "centered"

        text _("Avant tout, qui es-tu ?")

        hbox:
            imagebutton:
                idle "female_icon_idle"
                hover "female_icon_hover"
                action SetVariable("persistent.MC_genre", "girl")
            imagebutton:
                idle "male_icon_idle"
                hover "male_icon_hover"
                action SetVariable("persistent.MC_genre", "guy")
