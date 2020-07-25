label mess_manger:
if day == 0:
    if hour == 7:
        u "Au menu pour ce matin, il y avait du jus d'orange"
        u "Avec des croissants, de la brioche et un un petit café"
        u "J'en ai profité pour prendre un yaourt..."
        u "Mais chuut !!!! Il ne faut pas le dire !"
        $ limit_mange = 1
        $ mange7h = True
        $ hour += 1
    elif hour == 8:
        u "J'ai raté le service..."
        $ limit_mange = 0
    elif hour == 9:
        u "J'ai raté le service..."
        $ limit_mange = 0
    elif hour == 10:
        u "J'ai raté le service..."
        $ limit_mange = 0
    elif hour == 11:
        u "Ce midi au menu il y a"
        u "qqlch"
        u "qqlch"
        u "qqlch"
        $ limit_mange = 1
        $ hour += 1
        $ mange11h == True
    elif hour == 12:
        if mange11h == True:
            "J'ai déjà mangé ce midi"
        else:
            u "Ce midi au menu il y a"
            u "qqlch"
            u "qqlch"
            u "qqlch"
            $ limit_mange = 1
            $ hour += 1
            $ mange12h == True
    elif hour == 13:
            if mange11h == True or mange12h == True or limit_mange == 1:
                u "J'ai déjà mangé ce midi"
                u "Je n'ai plus faim"
            else:
                u "J'ai raté le service"
    elif hour == 14:
        if mange11h == True or mange12h == True or limit_mange == 1:
            u "J'ai déjà mangé ce midi"
            u "Je n'ai plus faim"
        else:
            u "J'ai raté le service"
    elif hour == 15:
        if mange11h == True or mange12h == True or limit_mange == 1:
            u "J'ai déjà mangé ce midi"
            u "Je n'ai plus faim"
        else:
            u "J'ai raté le service"
    elif hour == 16:
        if mange11h == True or mange12h == True or limit_mange == 1:
            u "J'ai déjà mangé ce midi"
            u "Je n'ai plus faim"
        else:
            u "J'ai raté le service"
    elif hour == 17:
        if mange11h == True or mange12h == True or limit_mange == 1:
            u "J'ai déjà mangé ce midi"
            u "Je n'ai plus faim"
        else:
            u "J'ai raté le service"
    elif hour == 18:
            u "Ce soir il y a au menu"
            u "qqlch"
            u "qqlch"
            u "qqlch"
            $ limit_mange = 1
            $ hour += 1
            $ mange18h = True
    elif hour == 19:
        if mange18h == True:
            "J'ai déjà mangé ce soir"
        else:
            u "Ce soir il y a au menu"
            u "qqlch"
            u "qqlch"
            u "qqlch"
            $ limit_mange = 1
            $ hour += 1
            $ mange19h = True
    elif hour == 20:
        "L'ordinaire est fermé à partir de 20h, je n'ai rien à faire ici..."
    elif hour == 21:
        "L'ordinaire est fermé à partir de 20h, je n'ai rien à faire ici..."
    elif hour == 22:
        "L'ordinaire est fermé à partir de 20h, je n'ai rien à faire ici..."
    elif hour == 23:
        "L'ordinaire est fermé à partir de 20h, je n'ai rien à faire ici..."
    elif hour == 24:
        "L'ordinaire est fermé à partir de 20h, je n'ai rien à faire ici..."
else:
    if hour == 1:
        "L'ordinaire est fermé à partir de 20h, je n'ai rien à faire ici..."
    elif hour == 2:
        "L'ordinaire ouvre à 6h du matin donc je n'ai rien à faire ici..."
    elif hour == 3:
        "L'ordinaire ouvre à 6h du matin donc je n'ai rien à faire ici..."
    elif hour == 4:
        "L'ordinaire ouvre à 6h du matin donc je n'ai rien à faire ici..."
    elif hour == 5:
        "L'ordinaire ouvre à 6h du matin donc je n'ai rien à faire ici..."
    elif hour == 6:
        "J'ai mangé, c'était assez bon..."
        $ hour += 1
    elif hour == 7:
        "J'ai mangé, c'était assez bon..."
        $ hour += 1
    elif hour == 8:
        "J'ai mangé, c'était assez bon..."
        $ hour += 1
    elif hour == 9:
        "J'ai mangé, c'était assez bon..."
        $ hour += 1
    elif hour == 10:
        "J'ai mangé, c'était assez bon..."
        $ hour += 1
    elif hour == 11:
        "J'ai mangé, c'était assez bon..."
        $ hour += 1
    elif hour == 12:
        "J'ai mangé, c'était assez bon..."
        $ hour += 1
    elif hour == 13:
        "J'ai mangé, c'était assez bon..."
        $ hour += 1
    elif hour == 14:
        "J'ai mangé, c'était assez bon..."
        $ hour += 1
    elif hour == 15:
        "J'ai mangé, c'était assez bon..."
        $ hour += 1
    elif hour == 16:
        "J'ai mangé, c'était assez bon..."
        $ hour += 1
    elif hour == 17:
        "J'ai mangé, c'était assez bon..."
        $ hour += 1
    elif hour == 18:
        "J'ai mangé, c'était assez bon..."
        $ hour += 1
    elif hour == 19:
        "J'ai mangé, c'était assez bon..."
        $ hour += 1
    elif hour == 20:
        "L'ordinaire est fermé à partir de 20h, je n'ai rien à faire ici..."
    elif hour == 21:
        "L'ordinaire est fermé à partir de 20h, je n'ai rien à faire ici..."
    elif hour == 22:
        "L'ordinaire est fermé à partir de 20h, je n'ai rien à faire ici..."
    elif hour == 23:
        "L'ordinaire est fermé à partir de 20h, je n'ai rien à faire ici..."
    elif hour == 24:
        "L'ordinaire est fermé à partir de 20h, je n'ai rien à faire ici..."
jump milit_base_ordinaire

label mess_connaissance:
u "Je vois plusieurs personnes assises à l'ordinaire à qui je pourrais parler"
menu:
    "Un couple à table":
        jump mess_connaissance_couple
    "Une femme dans une robe rouge" if unk_clara == True:
        jump mess_connaissance_clara
    "Clara" if unk_clara == False:
        jump mess_connaissance_clara
    "Un homme avec beaucoup de médailles sur sa veste":
        jump mess_connaissance_marine
    "Retour":
        jump milit_base_ordinaire
jump milit_base_ordinaire

label mess_connaissance_couple:


label mess_connaissance_clara:
$ unk_clara = False

label mess_connaissance_marine:

