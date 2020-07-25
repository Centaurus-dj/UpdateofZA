screen notify_quest(title):
    frame:
        style "QuestNotifFrame"
        vbox:
            style "QuestNotifVbox"
            text _(title)

            text _("Test")

style QuestNotifFrame:
    background "#ffffff"
    xsize 500
    ysize 300
    xalign .9
    yalign 0.3

style QuestNotifVbox:
    background "#000000"
    color "#ffffff"
    xsize 298
    ysize 248
