label splashscreen:
    scene bg black
    show text "Unknown Games":
        size 40
    $ pause.renpy(.5)
    show text _("Presents"):
        size 50
    show Renpy logo at center with dissolve:
        xalign 1.0
        linear 2.0 xalign 0.5
    centered "A game made with Ren'py"
    $ renpy.pause(1)
    if persistent.user == "tester":
        call screen Warn_Vers() with fade
    elif persistent.user == "player":
        if langcheck == False:
            call screen What_lang() with fade
        else:
            jump showDevlog
    elif persistent.user == "developer":
        return
    return
