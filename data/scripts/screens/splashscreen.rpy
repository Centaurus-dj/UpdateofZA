label splashscreen:
    return
    default persistent.user = "player"
    scene bg black
    show screen Unktxt() with fade
    $ renpy.pause(1, hard=True)
    hide screen Unktxt
    show screen Prestxt()
    with fade
    $ renpy.pause(1, hard=True)
    hide screen Prestxt
    show screen hgzatitle()
    with fade
    $ renpy.pause(1, hard=True)
    hide screen hgzatitle
    show screen mdewthrnpy
    with fade
    $ renpy.pause(1, hard=True)
    hide screen mdewthrnpy with fade
    menu:
        "Developer Mode !":
            jump AdmintoolSplash
        "Player Mode !":
            call screen What_lang() with fade
        "Tester Mode !":
            jump TestChoice
        "UI See Mode !":
            jump UIlabel
    #if persistent.user == "tester":
    #    call screen Warn_Vers() with fade
    #elif persistent.user == "player":
    #    if langcheck == False:
    #        call screen What_lang() with fade
    #    else:
    #        jump showDevlog
    #elif persistent.user == "developer":
    #    return
    return
