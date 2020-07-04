label milit_base_ordinaire:
scene ecran_noir
show mess_base
with fade
menu:
    "Manger":
        jump mess_manger
    "Faire connaissance":
        jump mess_connaissance
    "Retourner à la réception":
        jump milit_base_reception


label milit_base_bur_zya:
$ nomdejenn = "Commandante"
$ nomdejenns = "la commandante"
scene ecran_noir
show bureau_zya
with fade
menu:
    "Parler à %(nomdezya)s":
        jump bureau_zya_talk
    "Parler au commandant" if sait_commandant == False:
        jump bureau_zya_commandant
    "Parler à la commandante" if sait_commandant == True and jenn_corr < 120:
        jump bureau_zya_commandant
    "Parler à %(nomdejenns)s" if jenn_corr >= 120:
        jump bureau_zya_commandant
    "Sortir du bureau":
        jump milit_base_reception


label milit_base_terrain:
scene ecran_noir
show terrain
with fade
menu:
    "Jouer au foot":
        jump terrain_foot
    "Parler à ceux qui sont assis dans les tribunes":
        jump terrain_speak
    "Retourner à la réception":
        jump milit_base_reception


label milit_base_mychamber:
scene ecran_noir
show chambrebas
with fade
if new_chambre:
    u "Alors voici ma chambre..."
    u "C'est assez spacieux..."
    u "J'ADORE !!!"
    u "C'est cool en fait d'être dans une base militaire !"
    $ new_chambre = False
else:
    u "Je suis dans ma chambre"
menu:
    "dormir toute la journée(Ça fait passer 24h)":
        jump chamber_sleep
    "Se reposer(Ça fait passer 1h)":
        jump chamber_nap
    "Lire":
        jump chamber_reading
    "S'entrainer à avoir du Charisme" if need_charisme == True:
        jump chamber_train_charisme
    "Utiliser l'ordinateur(utiliser postgo)":
        jump chamber_ordi
    "Faire des tests":
        jump entertain_test
    "Sortir de la chambre":
        jump milit_base_reception





label milit_base_reception:
scene ecran_noir
jump lbl_Reception_imagemap
#show reception
#with fade
#menu:
    #"Ordinaire":
    #    jump milit_base_ordinaire
    #"Ma chambre":
    #    jump milit_base_mychamber
    #"Le bureau du commandant(et de %(nomdezya)s)":
    #    jump milit_base_bur_zya
    #"Le terrain de foot":
    #    jump milit_base_terrain
    #"Revenir au menu principal":
        #return
