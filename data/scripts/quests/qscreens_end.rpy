screen notify_quest(title):
    frame:
        style "QuestNotifFrame"
        vbox:
            style "QuestNotifVbox"
            text _(title):
                style "QuestTitle"

            text _("Test"):
                style "NotifyText"

    timer 3.0 action Hide("notify_quest", transition=fade)

style QuestNotifFrame:
    background "gui/questend.png"
    xsize 500
    ysize 300
    xalign .9
    yalign 0.3

style QuestNotifVbox:
    background "#000000"
    color "#ffffff"
    xsize 298
    ysize 248

style QuestTitle:
    size 40
    xalign .5
    yalign .4

style NotifyText:
    size 30
    xalign .15
    yalign .2

style lang_choice:
    background "gui/langchoice.png"
    xsize 200
    ysize 50
    xoffset -10
