label AdmintoolSplash:
    menu:
        "Tester Statbar":
            jump _ShowStatBar
        "Tester Menu Principal":
            jump _ShowMainMenu
        "Tester Notifications Screens":
            jump _ShowQuestNotif


################################################################################
##
################################################################################
label _ShowStatBar:
    call screen statsbar() with dissolve

################################################################################
##
################################################################################
label _ShowMainMenu:
    show screen main_menu() with dissolve

################################################################################
##
################################################################################
label _ShowQuestNotif:
    call screen notify_quest("Test Quest") with dissolve
