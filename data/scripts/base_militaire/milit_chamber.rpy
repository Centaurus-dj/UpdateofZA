#Dormir toute la journée...
label chamber_sleep:
scene ecran_noir
$ day += 1
$ hour = 5
$ dtime = 0
if day > 6:
    $ day = 0
if day == 0:
    "Nous sommes Lundi..."
elif day == 1:
    "Nous sommes Mardi..."
elif day == 2:
    "Nous sommes Mercredi..."
elif day == 3:
    "Nous sommes Jeudi..."
elif day == 4:
    "Nous sommes Vendredi..."
elif day == 5:
    "Nous sommes Samedi..."
elif day == 6:
    "Nous sommes Dimanche..."

show chambrebas
with fade
jump milit_base_mychamber

#faire une sieste...
label chamber_nap:
scene ecran_noir
$ hour += 1
if hour == 5:
    $ dtime = 0
elif hour == 6:
    $ dtime = 0
elif hour == 7:
    $ dtime = 1
elif hour == 8:
    $ dtime = 1
elif hour == 9:
    $ dtime = 1
elif hour == 10:
    $ dtime = 1
elif hour == 11:
    $ dtime = 2
elif hour == 12:
    $ dtime = 3
elif hour == 13:
    $ dtime = 3
elif hour == 14:
    $ dtime = 3
elif hour == 15:
    $ dtime = 3
elif hour == 16:
    $ dtime = 3
elif hour == 17:
    $ dtime = 3
elif hour == 18:
    $ dtime = 4
elif hour == 19:
    $ dtime = 4
elif hour == 20:
    $ dtime = 4
elif hour == 21:
    $ dtime = 5
elif hour == 22:
    $ dtime = 5
elif hour == 23:
    $ dtime = 5
elif hour == 24:
    $ dtime = 5
elif hour > 24:
    $ hour = 1
    $ day += 1
else:
    pass
"Une heure après..."
show chambrebas
with fade
jump milit_base_mychamber


label chamber_reading:
"Je lis un livre quelque peu intéréssent"
$ u_inteli += 5
"Mon intelligence a été augmentée de 5 points !"
jump milit_base_mychamber


label chamber_train_charisme:
u "Si je veux pouvoir draguer quelqu'un je dois m'entrainer à avoir du charisme..."
n "Tu as réellement besoin de t'entrainer à avoir du charisme ?"
u "Oui et ben quoi ?"
n "Non, c'est juste que c'est drôle !"
n "J'en suis sûr que si tu avais été une fille, tu n'aurais pas eu besoin de t'entrainer à avoir du charisme !"
u "Tais toi un peu !"
jump milit_base_mychamber


label chamber_ordi:
u "Alors, à quoi peut-on accéder avec cette chose ?"
$ cheats = True
menu:
    "Tricher " if cheats == True :
        jump chamber_cheats
    "Regarder mon check-up":
        jump chamber_check_up
    "Éteindre l'ordinateur":
        jump milit_base_mychamber

label chamber_cheats:
menu:
    "De l'argent":
        label cheats_argent:
        menu:
            "Ajouter 50 €":
                $ money += 50
                jump cheats_argent
            "Ajouter 100 €":
                $ money += 100
                jump cheats_argent
            "Ajouter 250 €":
                $ money += 250
                jump cheats_argent
            "Ajouter 500 €":
                $ money += 500
                jump cheats_argent
            "Ajouter 1 000 €":
                $ money += 1000
                jump cheats_argent
            "Retour":
                jump chamber_cheats
    "Mes abilités":
        label cheats_ability:
        menu:
            "Mon charisme":
                menu:
                    "Ajouter 10 points":
                        $ u_charisma += 10
                        jump cheats_ability
                    "Enlever 10 points":
                        $ u_charisma -= 10
                        jump cheats_ability
            "Mon intelligence":
                menu:
                    "Ajouter 10 points":
                        $ u_inteli += 10
                        jump cheats_ability
                    "Enlever 10 points":
                        $ u_inteli -= 10
                        jump cheats_ability
            "Ma force":
                menu:
                    "Ajouter 10 points":
                        $ u_strong += 10
                        jump cheats_ability
                    "Enlever 10 points":
                        $ u_strong -= 10
                        jump cheats_ability
            "Retour":
                jump chamber_cheats
    "Mon État":
        label cheats_etat:
        menu:
            "fatigue":
                menu:
                    "Ajouter 25 points":
                        $ points_fatigue =+25
                        jump cheats_etat
                    "Enlever 25 points":
                        $ points_fatigue -= 25
                        jump cheats_etat
            "faim":
                menu:
                    "Ajouter 25 points":
                        $ points_faim += 25
                        jump cheats_etat
                    "Enlever 25 points":
                        $ points_faim -= 25
                        jump cheats_etat
            "Retour":
                jump chamber_cheats
    "Retour":
        jump chamber_ordi

label chamber_check_up:
menu:
    "Mes abilités":
        label check_up_ability:
        menu:
            "Mon charisme":
                u "Mon charisme est de [u_charisma] points"
                jump check_up_ability
            "Mon intelligence":
                u "Mon intelligence est de [u_inteli] points"
                jump check_up_ability
            "Ma force":
                u "Ma force est de [u_strong] points"
                jump check_up_ability
            "Retour":
                jump chamber_check_up
    "Mon état":
        label check_up_etat:
        menu:
            "Ma fatigue":
                if points_fatigue == 0:
                    u "[string_fatigue]"
                else:
                    u "[string_fatigue]"
                jump check_up_etat
            "Ma faim":
                if points_faim == 0:
                    u "[string_faim]"
                else:
                    u "[string_faim]"
                jump check_up_etat
            "Ma soif":
                if points_soif == 0:
                    u "[string_soif]"
                u ""
                jump check_up_etat
            "Mon énergie":
                u ""
                jump check_up_etat
            "Retour":
                jump chamber_check_up
    "Revenir sur le bureau":
        jump chamber_ordi

label entertain_test:
    menu:
        "Tester le système de quêtes":
            jump startquest
        "Tester notre système de quêtes":
            jump chamber_entertain_quest
        "Tester le système d'heures":
            $ hour += 1
            $ HourTime(hour)
            jump entertain_test
        "Tester une solution":
            call screen tooltip_example
        "test again":
            show chambrebas
            with flashred
            pause.1
            show chambrebas
            with flashred2
            jump entertain_test
        "Retour":
            jump milit_base_mychamber



label chamber_entertain_quest:

    n "Tiens, je te donne une quête"
    $ log.keyon()
    $ log.assign("Une Quete")

    n "Voilà, tu as du normalement recevoir une notif !"
