screen qkey():
    if log.screen():
        key "Q" action ShowMenu(log.screen())

screen qlog():
    use quick_menu
    if log.key():
        key "Q" action [ Hide(log.screen()), Return() ]
    zorder 100
    window:
        background None

    frame:
        align (0.5, 0.5)
        background "quest_bg"

        frame:
            align (0.5, 0.5)
            maximum (650, 500)
            yminimum 500
            background None

            vbox:
                xfill True
                hbox:
                    xalign 0.5
                    yalign 0.5
                    text "Quêtes" color "#ffffff" size 30
                    textbutton "X" background None xpos 9.0 text_hover_color "#f10303" text_size 25 action [ Hide(log.screen()), Return() ]
                hbox:
                    for i in log.displayedtabs():
                        textbutton i action [ SetField(log, "tvar", i), log.newtab ]
                hbox:
                    vbox:
                        xmaximum 200
                        xfill True
                        text "Nom:" color "#ffffff"
                        for i in log.activetab():
                            textbutton i.title() text_hover_color "#CCCCCC" action SetField(log, "qvar", i) background None xpadding 0.0 text_size 18
                    vbox:
                        xmaximum 450
                        if log.activeimage():
                            add log.activeimage()
                        text "Description:" color "#ffffff"
                        fixed:
                            ymaximum 100
                            text log.activedescription() size 18
                        text "Progression:" color "#ffffff"
                        for i in log.activeprogress():
                            text formatgoal(i) size 18
                        null height 10
                        if log.trackable():
                            textbutton "Suivre cette quête" text_color "#ffffff" text_hover_color "#f10303" text_size 17 action [ log.track, Return() ]

screen tracker():
    fixed:
        align (1.0, 0.0)
        maximum (200,150)
        if log.tracked():
            textbutton "X" background None text_color "#ffffff" text_hover_color "#f10303" text_size 12 align (1.0, 0.0) action [ log.stoptracking, Hide(log.tracker()), Show(log.tracker()) ]
        vbox:
            xfill True
            spacing 3
            if log.tracked():
                text log.trackedtitle() color "#ffffff" size 18
                for i in log.trackerprogress():
                    text formatgoal(i) color "#ffffff" size 12

image notification:
    align (0.5, 0.25)

    alpha 0.0
    Text(log.message(), color="#ffffff")
    linear 0.5 alpha 1.0
    pause 2.0
    linear 0.5 alpha 0.0

init python:

    def formatgoal(goal):
        str = ''

        if not goal.hidden():
            if goal.completed():
                str = "X {0}".format(goal.description())
            else:
                if goal.fetch():
                    str = "-{0}  {1}/{2}".format(goal.description(), goal.have(), goal.need())
                else:
                    str = "-{0}".format(goal.description())
        else:
            if goal.required():
                str = "- ?????"

        return str
