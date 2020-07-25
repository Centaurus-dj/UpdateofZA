init python:
    def LovePlus():
        renpy.notify("One Love Point added !")
        return None

    def LoveMinus():
        renpy.notify("One Love Point Sustracted !")
        return None

    def SuspPlus():
        renpy.notify("One Suspicion Point added !")
        return None

    def SuspMinus():
        renpy.notify("One Suspicion Point Sustracted !")
        return None

    def change_stat(stat, amount):
        stat += amount
        if stat > 100:
            stat = 100
        elif stat < 0:
            stat = 0
