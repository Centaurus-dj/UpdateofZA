label test_statbar:
    scene salon
    call screen statsbar() with fade

label firstcheatscreen:
    show screen statsbar()
    show screen cheatscreen("mc")

label add_hunger10:
    python:
        if points_faim >= 100:
            points_faim = 100
            renpy.notify("Points are at their maximum")
        else:
            points_faim += 10
            renpy.notify("Points well added !")
    show screen statsbar()
    show screen cheatscreen("mc")

label sust_hunger10:
    python:
        if points_faim <= 0:
            points_faim = 0
            renpy.notify("Points are at their minimum")
        else:
            points_faim -= 10
            renpy.notify("Points well sustracted !")
    show screen statsbar()
    call screen cheatscreen("mc")




label add_thirst10:
    python:
        if points_soif >= 100:
            points_soif = 100
            renpy.notify("Points are at their maximum")
        else:
            points_soif += 10
            renpy.notify("Points well added !")
    show screen statsbar()
    call screen cheatscreen("mc")

label sust_thirst10:
    python:
        if points_soif <= 0:
            points_soif = 0
            renpy.notify("Points are at their minimum")
        else:
            points_soif -= 10
            renpy.notify("Points well sustracted !")
    show screen statsbar()
    call screen cheatscreen("mc")




label add_energy10:
    python:
        if energy >= 100:
            energy = 100
            renpy.notify("Points are at their maximum")
        else:
            energy += 10
            renpy.notify("Points well added !")
    show screen statsbar()
    call screen cheatscreen("mc")

label sust_energy10:
    python:
        if energy <= 0:
            energy = 0
            renpy.notify("Points are at their minimum")
        else:
            energy -= 10
            renpy.notify("Points well sustracted !")
    show screen statsbar()
    call screen cheatscreen("mc")


label add_hour1:
    python:
        hour += 1
        if hour == 5:
            dtime = 0
        elif hour == 6:
            dtime = 0
        elif hour == 7:
            dtime = 1
        elif hour == 8:
            dtime = 1
        elif hour == 9:
            dtime = 1
        elif hour == 10:
            dtime = 1
        elif hour == 11:
            dtime = 2
        elif hour == 12:
            dtime = 3
        elif hour == 13:
            dtime = 3
        elif hour == 14:
            dtime = 3
        elif hour == 15:
            dtime = 3
        elif hour == 16:
            dtime = 3
        elif hour == 17:
            dtime = 3
        elif hour == 18:
            dtime = 4
        elif hour == 19:
            dtime = 4
        elif hour == 20:
            dtime = 4
        elif hour == 21:
            dtime = 5
        elif hour == 22:
            dtime = 5
        elif hour == 23:
            dtime = 5
        elif hour == 24:
            dtime = 5
        elif hour > 24:
            hour = 1
            day += 1
        renpy.notify("1 Hour added")
    show screen statsbar()
    call screen cheatscreen("mc")
