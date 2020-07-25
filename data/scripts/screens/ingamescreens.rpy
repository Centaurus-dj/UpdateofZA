screen Choix_genre():
        text _("Avant tout, qui es-tu ?"):
            yalign .0
            xpos .35
            size 35
        hbox:
            imagebutton:
                xpos 0.0
                xoffset -10
                xanchor -10
                idle "female_icon_idle"
                hover "female_icon_hover"
                action [SetVariable("persistent.MC_genre", "girl"), Jump("start_story")]
            imagebutton:
                xpos 1.3
                idle "male_icon_idle"
                hover "male_icon_hover"
                action [SetVariable("persistent.MC_genre", "guy"), Jump("start_story")]
