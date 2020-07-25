label fille:

    $ nomduheroes = renpy.input("Comment est-ce que tu t'appelles ?? (écrit ton nom avec le clavier)")
    $ nomduheroes = nomduheroes.strip()
    if not nomduheroes:
        $ nomduheroes = "Sarah"
    elif nomduheroes.strip() in prenoms_insulte:
        prog "TU ES SERIEUX !!"
        prog "On ne donne pas comme nom aux gens des insultes !"
        prog "Même si c'est un jeu vidéo !"
        prog "Recommence !"
        jump fille
    elif nomduheroes.strip() in pren_fem:
        prog "Non je n'accepte juste pas !"
        prog "Recommence !"
        jump fille
    elif nomduheroes.strip() == "nicky minaj":
        prog "Non je n'accepte juste pas !"
        prog "Recommence !"
        jump fille
    if nomduheroes.strip() in cara_non_accept:
        prog "Déso ces caractères ne sont pas acceptés essaye peut-être juste avec des lettres ?"
    if nomduheroes.strip() in cara_non_accept_2:
        prog "Déso ces caractères ne sont pas acceptés essaye peut-être juste avec des lettres ?"

label fille_2:
    $ nom_ami_heroes = renpy.input("Comment s'appelle ta meilleure amie ?")
    $ nom_ami_heroes = nom_ami_heroes.strip()
    if not nom_ami_heroes:
        $ nom_ami_heroes = "Alysson la belle"
    elif nomduheroes.strip() in prenoms_insulte:
        prog "TU ES SERIEUX !!"
        prog "On ne donne pas comme nom aux gens des insultes !"
        prog "Même si c'est un jeu vidéo !"
        prog "Recommence !"
        jump fille_2
    elif nomduheroes.strip() in pren_fem:
        prog "Non je n'accepte juste pas !"
        prog "Recommence !"
        jump fille_2
    elif nomduheroes.strip() == "nicky minaj":
        prog "Non je n'accepte juste pas !"
        prog "Recommence !"
        jump fille_2
label fille_3:
    $ nom_ennemi = renpy.input("Comment s'appelle la personne que t'aimes le moins ?")
    $ nom_ennemi = nom_ennemi.strip()
    if not nom_ennemi:
        $ nom_ennemi = "Alban"
    ass "C'est une femme monsieur et elle s'appelle [nomduheroes]"
    "{color=#F6080C}{b}Alert! Alert! Alert!{/b}{/color}"
    doc "Que se passe t-il ?"
    ass "Je n'en ai aucune idée !!"
    doc "Implantez lui un sédatif et envoyez la dans un endroit sûr !"
    hide doc
    with fade
    ass "Oui monsieur, à vos ordres !!"
    hide ass with fade
    hide lab
    "Deux jours plus tard..."
    "Tu te réveilles au milieu de ton salon..."
    e "Allez, réveille toi allez !!"
    show salon
    with dissolve
    show alex at right
    with fade

#define gui.interface_text_font
#If present, the font used for the text.

#define gui.interface_text_size
#If present, the size of the text.

#define gui.interface_text_color
#If present, the color of the text.


    ue "Heu..."
    e "Ce n'est pas le moment de dormir !!!"
    ue "Qu'est-ce qui s'est passé??"
    e "Eh bien, quand toi tu révassais! Il y a eu une invasion de zombies et presque tout le monde est mort!"
    ue "Pourquoi toi tu ne l'es pas??"
    e "Moi c'est normal, je suis dans ta tête, donc..."
    e "Si t'es pas mort, alors moi aussi!"
    "Heu c'est bizarre..."
    ue "Bon sinon..."
    ue "Quel est ton nom ?"
    "Ah...."
    hide alex
    with fade
    hide salon
    show reasalon
    with dissolve
    "Veux-tu altérer son esprit pour pouvoir choisir son nom ?"
    menu:
        "Oui !":
            python:
                nomdunarrateur = renpy.input("Comment s'appelle t-il ?")
                nomdunarrateur = nomdunarrateur.strip()
                if not nomdunarrateur:
                    nomdunarrateur = "Alexis"
            hide reasalon
            show salon
            with dissolve

        "Non !":
            $ nomdunarrateur = "Alexis"
            $renpy.pause(1.5, hard=True)
            hide reasalon
            show salon
            with dissolve

    show alex at right
    n "Moi c'est [nomdunarrateur]"
    ue "Je suis où ?"
    n "Bah tu vois pas ? Dans ton salon..."
    n "Par contre, il faudrait que tu te couvres car tu es en sous vêtements..."
    ue "Ah!! Merci..."
    ue "Au fait, comment j'ai fini en sous vêtements ?"
    n "Je sais pas, je suis pas Dieu! C'est quoi la dernière chose que t'ais faite ?"
    ue "attends..."
    menu:
        "J'ai bu du whisky !":
          $ drug = True
          jump suitefe
        "Je suis tellement stupide que je m'en souvient pas...":
          jump endgame_1fe
        "J'ai mangé des champignons hallucinogènes avec de la mayonnaise !":
          $ drug = True
          jump champis_debfe
        "J'ai fait un marathon de films sur Netflix":
          n "Ah ouais ?"
          n "Et t'as regardé quoi ?"
          menu:
              "Avengers: The Endgame":
                  n "Mouais..."
                  n "Ce n'est pas mon délire même si la bande son est bien..."
                  jump suitefe
              "Star wars VIII":
                  n "Ce film fait parti de la saga la plus connue au monde !!"
                  n "Même si le VIII est mieux que le VII..."
                  n "Tu es mon nouveau meilleur ami !!!"
                  n "Tu viens de gagner 50 points de sympathie avec [nomdunarrateur] !"
                  $ points_sympathie_narrateur += 50
                  jump suitefe
              "Deadpool":
                  n "Celui-là est tellement bien !!!"
                  n "Tu viens de gagner 100 points de sympathie avec [nomdunarrateur] !"
                  $ points_sympathie_narrateur += 100
                  jump suitefe



label champis_debfe:
 show alex at right
 with fade
 n "Tu es sérieuse ?"
menu:
    ue "Heu..."
    "Oui !":
      n "Mais c'est super ça !"
      n "J'ai toujours rêvé d'avoir une amie qui avait elle aussi mangé des champignons hallucinogènes !"
      n "Du coup ça veut dire..."
      jump suitefe
    "Non !":
      n "Quel dommage !"
      n "J'aurais aimé d'avoir quelqu'un qui savait ce que ça faisait des chamignons hallucinogènes..."
      n "Mais t'inquiètes, c'est pas grave..."
      n "Du coup, ça veut dire ..."
      jump suitefe


label endgame_1fe:
n "T'es sérieuse là???"
ue "heu je crois bien..."
menu:
    "Je suis sûre!":
      jump suppose_endgamefe
    "Non non! Je rigolais! J'ai bu du whisky !":
      jump suitefe


label suitefe:
show screen fullshud
if drug == True :
    n"C'est encore une soirée qui s'est mal finie !"
    n "Bon heureusement, elle ne s'est pas finie avec quelqu'un..."
    n "Qui sait ce que vous auriez pu faire..."
    ue "On aurait pu faire quoi ?"
    n "Je ne sais pas moi..."
    n "..."
    n "......"
    n "Voilà !"
    n "Vous auriez pu ...."
    ue "Faire quoi ?!"
    n "Vous auriez pu faire un jeu de société !!"
    n "Et même pire !"
    n "Vous auriez peut être pu y jouer toute la nuit !"
    ue "Est-ce que tu es sérieux ?"
    n "Bien sûr que oui !"
    n "Attends, un JEU DE SOCIETE !!!"
    ue "Et ?"
    n "UN JEU DE SOCIETE !!!"
    n "C'est pour les grands parents !!"
    n "C'est la pire chose que l'on pourrait rêver jouer avec quelqu'un !"
    ue "T'es quand même bizarre..."
    ue "Mais bon... On ne va pas en faire tout un plat !"
    n "Non t'inquiètes pas!"
    n "Je te laisse voir de toi même comment on est dans cette situation que je qualifierai de..."
    n "Inadéquate !"
    n "Bonne chance !"
else:
    n "T'as du passer du bon temps quand cette planète était encore civilizée..."
    ue "Ouais..."
    "Enfin bon, quel réveil bizarre... Je viens de me réveiller et je suis en sous-vêtements... Il faut que je fasse quelque chose!"
menu:
    "Il faut mieux que je fouille la maison pour voir ce que je trouve...":
      jump suite_correctefe
    "Moi je suis une ninja warrior ! Je préfère aller dehors!":
      jump endgame_2fe

label suppose_endgamefe:
n "Bah vas t-en... Je ne peux pas te laisser jouer !"
hide alex
hide salon
with fade
show game over
with pixellate
return


label endgame_2fe:
n "Tu te prépares à sortir."
hide alex
with fade
hide salon
with dissolve
show zombie
with dissolve
n "Après être sortie, tu croises un zombie et, sans être équipée tu meurs mangée"
n "Au lieu d'avoir survécu, tu t'es donnée à manger à un zombie... On aurait presque pu dire que t'as été altruiste..."
show game over
with dissolve
return


label suite_correctefe:
n "Tu regarde autour de toi et tu vois qu'il y a la porte du garage, la cuisine, des escaliers et des toilettes."
n "Que choisis-tu ?"
jump choix_mais



label cuisinefe:
show cuis
with fade
$ cuis = True
ue "Je suis allé regarder dans la cuisine voir si, par je ne sais quel miracle, quelqu'un aurait pu laisser quelque chose..."
n "Tu fouilles un peu partout, sous l'évier, dans le frigo, t'es même allé fouiller dans la poubelle..."
hide alex
with fade
ue "Mais tout ça, ça a payé! J'ai trouvé..."
hide cuis
with dissolve
show muesli
with dissolve
ue "une boite de muesli"
hide muesli
with dissolve
show oasis
with dissolve
ue "Et une bouteille d'oasis !"
hide oasis
with dissolve
show cuis
with dissolve
show alex at right
with fade
n "Après avoir fouillé la cuisine tu retournes au salon."
$ dtime += 1
hide cuis
with fade
jump choix_mais


label toilettes_fe:
show toil
with fade
$ toil = True
ue "Je me dis que l'on ne sait jamais! Peut-être qu'il y a quelque-chose de bien..."
n "Et t'avais raison! En ouvrant la porte tu trouves.."
hide alex
with fade
hide toil
with dissolve
show revol at right
n "un revolver chargé"
show munitions magnum at left
n "et une boite de munitions!"
hide revol
hide munitions magnum
with dissolve
show toil
with dissolve
show alex at right
with fade
ue "Il me reste à fouiller..."
$ dtime += 1
hide toil
with fade
jump choix_mais

label garage_fe:
show gara
with fade
$ garage = True
ue "Je décide du coup d'aller fouiller le garage..."
n "Ca ne t'as pas rapporté grand chose à part savoir qu'il y a une voiture dans le garage et que tu ne peux pas la conduire car tu n'as pas la CLÉ!!!"
n "Après ça, tu redescends au salon..."
$ dtime += 1
hide gara
with fade
jump choix_mais

label etage_fe:
$ esc = True
hide salon
with dissolve
show chambre at center
with dissolve
ue "Je monte à l'étage et je trouve deux chambres..."
ue "C'est bizarre..."
n "Quoi ?!"
ue "Les noms écrits sur les portes des chambres ne me disent rien..."
ue "Mais pourtant... J'ai comme une chose à l'intérieur de moi qui me dit que c'est bien là où je dois aller..."
ue "Tu vois... Sur une porte c'est écrit \"Marie\" et l'autre c'est écrit \"[nomduheroes]\"!"
ue "Je ne me souviens même pas que j'ai une soeur..."
n "..."
ue "Bon... Je vais fouiller ma chambre puis celle de ma \"soeur\"."
hide alex
with fade
hide chambre
with dissolve
show arba
with dissolve
ue "Je trouve une arbalète "
hide arba
with dissolve
show casq
with dissolve
ue "et une casquette..."
hide casq
with dissolve
show chambre
with fade
$ dtime += 1
ue "Je redescends après ça, et je reviens au salon..."
hide chambre
with fade
jump choix_mais

label boite_lettre:
$ boite_lettre = True
hide salon
with fade
scene ecran_noir
ue "Alors..."
show boite_let
with fade
n "Regarde dans la boîte aux lettres si il n'y a pas de courier..."
ue "Ah !"
$ money += 150
ue "Ah ! J'ai trouvé [money] €"
$ renpy.save_persistent()
hide boite_let
with fade
jump choix_mais




label choix_mais:
show salon
with fade
menu:
    "Je vais fouiller la cuisine!" if cuis == False:
      hide salon
      with fade
      jump cuisinefe
    "Je vais voir ce qu'il y a au delà des escalier!" if esc == False:
      hide salon
      with fade
      jump etage_fe
    "Je vais voir aux toilettes, on ne sait jamais..." if toil == False:
      hide salon
      with fade
      jump toilettes_fe
    "On sait jamais, je vais voir le garage!" if garage == False:
      hide salon
      with fade
      jump garage_fe
    "Je vais voir la boîte aux lettres qui est juste devant !" if boite_lettre == False:
      hide salon
      with fade
      jump boite_lettre

hide salon
with fade
jump _2fe



















































label _2fe:
queue sound "audio/epic-post_27min.mp3"
"Tu te dis qu'il faudrait tout de même que tu fouilles le salon."
"Après plusieurs heures de recherches..."
hide alex
with fade
hide salon
with fade
scene ecr_sec
show brass
with fade
window hide
$ renpy.pause(2.5, hard=True)
window show
"Tu trouves une brassière"
hide brass
show leg
with fade
window hide
$ renpy.pause(2.5, hard=True)
window show
" un legging sur le canapé"
hide leg
show deba
with fade
window hide
$ renpy.pause(2.5, hard =True)
window show
"Enfin, tu trouves un débardeur sous un coussin..."
hide deba
show salon
with fade
show alex at right
with fade
n "Tu devrais fouiller dans la cheminée, on sait jamais..."
ue "Je pense qu'il n'y aura rien mais on peut toujours regarder..."
hide alex
with fade
hide salon
with fade
show sac_east
with fade
"Tu y trouves un sac à dos!"
hide sac_east
with fade
show salon
with fade
show alex at right
with fade
stop music
stop sound
play sound "night_time_sounds"
n "Je te signale qu'il commence à faire nuit..."
ue "Sans blague! Comme si je ne l'avais pas remarqué!"
n "Hé oh! Calmos, moi je te dis ça comme ça mais bon si ça t'énerves tu peux aller te faire !"
ue "Non c'est bon..."
ue "Je disais ça sur un ton ironique..."
n "Ah !!"
n "Ah !! Mmmmmm...."
n "Ah !! Mmmmmm.... Je m'excuse...."
n "Ah !! Mmmmmm.... Je m'excuse.... Je n'avais pas compris..."
n "Je m'en excuse..."
ue "..."
n "Excuses acceptée ??"
ue "......"
n "Alors ?"
ue "........."
ue "D'accord, excuses acceptées !"
n "Maintenant que ça, c'est derrière nous..."
n "On peut se concentrer sur ce que l'on faisait..."
n "Bon, d'après ce qu'on a vu, il y a deux endroits où l'on pourrait aller dormir..."
ue "Il y a quoi ?"
n "Il y a la possibilité d'aller dormir sur la canapé dans le salon"
ue "C'est peut-être un peu risqué..."
n "Oui, ça peut l'être..."
n "Sinon tu as ta chambre..."
ue "C'est vrai mais comme il y a des barres en fer qui traversent mon lit, je vais être obligée de dormir par terre..."
n "Oui mais au moins tu as moins de risque qu'un rodeur ou un rampant vienne dans ton sommeil te manger..."
ue "Mais j'ai plus de chance d'avoir mal au dos toute la journée de demain..."
n "Alors tu choisis quoi ?"
ue "Je choisis..."
menu:
    "Dormir dans ma chambre!":
      jump chambrefe
    "Dormir au salon!":
      jump salonfe

label salonfe:
hide alex
with fade
hide salon
with dissolve
scene ecran_noir
"Le lendemain matin..."
stop sound
queue sound "audio/epic-post_27min.mp3"
n "Hé oh... Ma jolie réveille toi..."
ue "Mmmm..."
n "Allez, il faut se réveiller..."
ue "Mmm... Tu m'as appelée comment ?..."
n "Ma jolie... Pourquoi ?"
ue "Non... Pour savoir..."
ue "En fait... Personne ne m'a appelée comme ça avant toi..."
n "Si ça te dérange que je t'appelles comme ça, je suis désolé"
ue "Non... C'est pas ça..."
ue "Je trouve ça juste..."
ue "...Mignon..."
show salon
with dissolve
show alex at right
with fade
n "Attends !"
ue "Quoi ?"
ue "Ahh !!"
ue "Qu'est-ce que c'est que cette douleur ?!"
n "Attends..."
n "Hé me*de!! On s'est fait mordre !"
ue "Putain!!"
ue "On fait quoi maintenant??"
n "Hé ben..."
n "On a 23 pourcents de chances de mourir..."
ue "Qu'est-ce que tu veux dire par la ?"
n "Je veux dire par là que l'Etat avait travaillé sur un médicament qui pouvait te sauver mais le fait est que je ne sais pas si ils ont réussi..."
ue "Mais alors qu'est-ce qu'on attend??"
ue "Il faut de toute façon que l'on essaye de trouver ce médicament"
"Tu prends tes affaires puis tu pars..."
"Tu jettes tout de même un dernier regard à ta maison..."
hide alex
with fade
hide salon
with dissolve
show maison depart
with fade
"Tu la regardes longuement..."
"Très longuement..."
"Vraiment longuement..."
"Puis même extrêmement longuement..."
"Puis de nouveau longuement mais attentivement..."
"Puis..."
show alex at right
with fade
n "Hé je te rappelle que ce n'est qu'une maison!!"
ue "Heu, oui!"
ue "Désolée..."
ue "C'est bizarre..."
"Tu regardes ta morsure"
n "Quoi ?"
ue "Bah ma morsure me fait plus mal..."
n "Raison de plus de ne pas trainer !"
hide alex
with fade
hide maison depart
with fade
show autoroute
with fade
"Tu marches pendant des heures..."
"A un moment tu vois une station essence mais tu ne te sents pas apte à te battre..."
show alex at right
with fade
n "Ca va ?"
ue "Pas vraiment..."
ue "Je"
ue "Je ne me sens..."
"{i}Buahhhhhhhhhh{/i}"
"Tu viens de vomir..."
ue "pas bien..."
n "*dégouté* Heu... je comprends mieux maintenant..."
"Après avoir vomi, tu ne te sens plus très bien..."
"Et tu es fatiguée..."
n "Je pense que l'on devrait ne pas risquer d'aller à la station essence"
ue "Ouais... Je pense qu'il ne faut pas prendre ce risque..."
"Tu commences à ressentir des nausées et puis tu as aussi faim..."
"Tu regardes en face de toi et tu vois..."
hide alex
with fade
hide autoroute
with fade
show pharmacie
with fade
"Une pharmacie..."
hide pharmacie
with fade
show camping_car_1
with fade
"Et un camping car."
hide camping_car_1
with fade
show autoroute
with fade
show alex at right
with fade
n "Où est-ce qu'on va ??"
ue "Alors..."
menu:
    "La pharmacie":
      jump salon_fin_1fe
    "Le camping car":
      jump salon_1fe

label salon_fin_1fe:
n "Allons-y!"
hide alex
with fade
hide autoroute
with fade
show zombies
with dissolve
ue "AHHHHHHHHH"
show alex at right
with fade
n "AHHHHHHHHHH"
hide alex
with dissolve
"Tu es allée en direction de la pharmacie..."
stop sound
play sound "zombie-sound-effects-free.mp3"
"Mais pas loin, après que tu sois partie tu es tombée sur une horde de zombies"
"Tu es morte déchiquetée..."
hide zombies
with fade
stop sound
show game over
with dissolve
"T'as perdu !!"
return



label salon_1fe:
n "Allons-y !"
hide alex
with fade
hide autoroute
with fade
show camping_car_1
with fade
"Après être montée dans le camping car, tu te dépêches de fermer la porte."
show alex at right
with fade
n "Ouffff...."
n "On a eu chaud !!!"
ue "Ah ça tu peux le dire!"
stop sound
play sound "zombie-sound-effects-free.mp3"
ue "Passer à deux doigts d'une horde de zombies mais chuuuuut!"
"Tu te tais car tu ne veux pas te faire remarquer par les zombies"
stop sound
"Dix minutes plus tard..."
"La horde de zombies venait de passer"
ue "Bon..."
ue "Maintenant que le danger est écarté..."
ue "Je vais me reposer..."
stop sound
play sound "night_time_sounds"
hide alex
with fade
hide camping_car_1
with fade
"Trois heures plus tard..."
ue "Mmmmmm..."
show camping_car_1
with fade
stop sound
play sound "audio/epic-post_27min.mp3"
show alex at right
with fade
n "Rebonjour !"
n "Mon amie, t'es recinquée ?"
ue "Oui..."
n "on devrait aller voir à la pharmacie si on trouve quelque-chose..."
ue "Bonne idée!"
hide alex
with fade
"Tu descends et tu fais bien attention de regarder partout pour ne pas te faire mordre par un zombie solitaire"
hide camping_car_1
with fade
show pharmacie
with dissolve
"Une demi-heure plus tard..."
ue "Ca ne sert à rien!"
ue "Il n'y a pas de médicaments qui pourraient me sauver!"
show alex at right
with fade
n "On est foutus !"
hide alex
with fade
"En repartant tu te regardes dans la glace et tu te rends compte"
"Que tu es en train de perdre tes cheveux!!"
"A ce moment là, tu décides..."
menu:
    "De sortir essayer de quand même trouver un moyen de rester en vie":
      jump salon_fin_2fe
    "De t'enfermer à vie dans la pharmacie":
      jump salon_fin_3fe

label salon_fin_2fe:

"Tu te dépêches de sortir"
"Mais en sortant tu voies..."
hide pharmacie
with fade
show zombies
with fade
stop sound
play sound "zombie-sound-effects-free.mp3"
"Des zombies"
"Tu meurs..."
"Mais pas en zombie"
hide zombies
with fade
stop sound
show game over
with dissolve
return


label salon_fin_3fe:
"Tu meurs..."
"A petit feu..."
"Après quelques jours d'affreuses souffrances..."
"Tu meurs et tu deviens un zombie"
"Ces derniers jours de ta vie ont étés les plus douloureux !!! "
hide pharmacie
with fade
show game over
with fade
return


























label chambrefe:
"Tu décides d'aller dormir sur le sol de ta chambre..."
hide alex
with fade
hide salon
with fade
scene ecran_noir
"Pendant que tu dors..."
unknow "Chéri ?"
unknow "Grand frère ?"
ue "Maman ?"
ue "Jade ?"
ue "Que faites-vous là ?"
mom "Nous resterons toujours avec toi..."
sis "Nous serons dans ton coeur pour l'éternité..."
"Elles commencent à s'éloigner..."
ue "Où allez vous ?"
"Elles s'éloignent de plus en plus..."
ue "Non !"
ue "Revenez !"
"Tu ne les apperçois presque plus..."
show chambre_nuit
with fade
ue "Que s'est-il passé ?"
ue "C'était un rêve ?"
ue "Ca avait pourtant l'air si réel..."
n "Ca tu peux le dire..."
n "Je croyais aussi que c'était réel..."
"Après cette réflexion, tu te rendors..."
hide chambre_nuit
"Quelques-heures plus tard..."
stop sound
ue "Mmmm....."
show chambre
show alex at right
with fade
n "Hé oh... Ma jolie réveille toi..."
ue "Mmmm..."
n "Allez, il faut se réveiller..."
ue "Mmm... Tu m'as appelée comment ?..."
n "Ma jolie... Pourquoi ?"
ue "Non... Pour savoir..."
ue "En fait... Personne ne m'a appelée comme ça avant toi..."
n "Si ça te dérange que je t'appelles comme ça, je suis désolé"
ue "Non... C'est pas ça..."
ue "Je trouve ça juste..."
ue "...Mignon..."
n "Allez, il faut se lever..."
ue "Alors...."
ue "Aïe !"
ue "T'avais raison en disant que j'allais avoir mal au dos si je dormais par terre..."
n "Ah bah ça, on pouvait s'en douter..."
n "Dormir par terre ce n'est pas tout le temps confortable..."
ue "Ah ça, tu peux le dire..."
"En descendant, tu croises un rampant, tu le tues en faisant traverser une flèche dans son crane."
hide alex
with fade
hide chambre
with fade
show salon
with fade
show alex at right
with fade
n "Je me disais que l'on pourrait s'amuser à dézombifier la rue."
ue "Alors que veux dire \"dézombifier\" ?"
n "Ca veut dire: éliminer toute trace de zombies."
ue "heu..."
menu:
    "Je vais aller m'amuser!":
      jump entr_1fe
    "Je préfère aller chercher des survivants":
      jump surv_1fe

label entr_1fe:
hide alex
with fade
hide salon
with fade
show maison depart
with fade
"Tu t'équipes de ton arbalète et tu vas t'amuser à tuer du zombie."
"Quelques heures plus tard, après avoir vidé toute la rue des zombies qu'il pouvait y avoir."
show alex at right
with fade
n "Je pense qu'après ça on est quand même bien entrainés."
ue "Je suis d'accord avec toi !"
jump surv_1fe


label surv_1fe:
hide alex
with fade
hide salon
with fade
"Avant de partir, tu préfères regarder une dernière fois ta maison..."
show maison depart
with dissolve
"Tu la regardes longuement"
"Vraiment longuement"
"Extrêmement longuement..."
show alex at right
with fade
n "Heu..."
n "Je te le dis toute suite"
n "Ce n'est qu'une MAISON !!!"
ue "Euh, c'est vrai... Ce n'est qu'une maison"
ue "Mais ça fait bizarre de quitter cet endroit..."
n "Je sais..."
n "Je te rappelle que je suis dans ta tête..."
ue "Oui enfin bon..."
n "Ouais il faudrait qu'on y aille..."
hide alex
with fade
hide maison depart
with fade
show autoroute
with dissolve
"A un moment tu arrives à un carrefour avec d'un coté"
"un panneau écrit \"ville\"dessus"
"un autre panneau avec écrit \"campagne\""
"Où dois-je aller ?"
menu:
    "A la campagne":
      jump campfe
    "En ville":
      jump villefe


label villefe:

ue "Je décide d'aller en ville..."
show alex at right
with fade
n "C'est un choix risqué..."
n "Mais qui peut rapporter gros !"
"Après plusieurs heures de marche"
hide alex
with fade
hide autoroute
with fade
show villeabb
with dissolve
"tu arrives enfin en ville..."
"Mais malchance du siècle tu tombes sur le début d'une horde de zombies qui fonce droit sur toi..."
ue "Il faut qu'on se cache quelquepart!!"
ue "Mais où??"
show alex at right
with fade
n "J'ai repéré deux cachettes potentielles"
n "l'une est un tank et l'autre est un immeuble mais le fait est que tu seras sûrement fatigué arrivé en haut..."
n "Alors???"
n "Qu'est-ce qu'on fait???"
ue "Hmm..."
hide alex
with fade
menu:
    "Je me cache dans le tank":
      jump town_tankfe
    "Je monte à l'échelle":
      jump town_immfe

label town_tankfe:

"Tu te dépêches de monter dans le tank avant que les zombies te rattrapent..."
"A l'intérieur du tank tu apperçois une jeune femme"
e "Non mais oh, qu'est-ce que tu fais là??"
ue "Ca ne se voit pas?? J'essaye de survivre aux zombies qui sont dehors!!"
"Sans que tu puisses faire un seul mouvement, elle te plaque par terre et t'injectes quelquechose..."
"Après ça, tu ne peux plus bouger..."
"Elle se retourne et appuye sur pleins de bouttons"
show zya
with fade
$ nomdezya = "Zya"
e "Comment t'appelles-tu petite garce ?!"
ue "Moi c'est %(nomduheroes)s"
z "Hé bien, je ne suis pas enchantée de te rencontrer %(nomduheroes)s"
ue "De mêeeeemmee...."
z "C'est ça..."
z "Dors le temps que l'on arrive dans ton nouveau chez toi !"
play sound audio.tank_moving
"Elle roule pendant des kilomètres avec celui-ci"
"laissant derrière elle de la purée de zombie..."
stop sound
hide villeabb
with fade
show entreebase
with fade
"Vous arrivez devant une base militaire en début de soirée..."
"Cet à ce moment là que tu t'endors..."
hide entreebase
with fade
scene ecran_noir
gardem "Ah ! Zoé, t'es enfin revenue !"
z "T'es qui toi ??"
gardem "Heu... Oui, désolé je suis le petit nouveau"
z "C'est..."
$ renpy.pause(5, hard=True)
"Quelques temps plus tard..."

z "Allez, réveille toi !"
ue "Hmmm...."
n "Chut ...."
n "Fais comme si tu dormais toujours..."
n "Comme je suis dans ta tête, on peut se parler sans que les autres nous entendent."
ue "{i}Ma tête, elle me fait super mal...{/i}"
n "Je sais, c'est leffet de l'éphedrine..."
n "A part ça, on a un énorme problème !"
ue "{i}Lequel ?{/i}"
n "Celui que si on ment à cette personne, elle nous garde enfermés jusqu'à ce que l'on meurt !"
ue "{i}Ah... Oui, d'accord...{/i}"
ue "{i}On a pas la possiblité de s'enfuir en courant ?{/i}"
n "Non, on est attachés..."
z "Hé !!"
z "Tu vas te réveiller ou je vais devoir t'obliger ?!"
n "Je pense que tu devrais lui faire croire que tu viens de te réveiler..."
ue "{i}Je pense aussi...{/i}"
show cell
with fade
hide cell
with fade
show cell
with fade
hide cell
with fade
show cell
with fade
ue "Hmmm..."
ue "Où suis-je ?"
show zya at right
with dissolve
z "Ahh !!"
z "Enfin !"
z "Tu es dans une cellule"
ue "Pourquoi ma tête me fait aussi mal ?!"
z "Pour ça, je suis désolée..."
z "J'aurais bien utilisé de la chloroforme..."
z "Mais j'en avais pas..."
z "La seule chose que j'avais..."
z "C'était de l'éphedrine..."
ue "Franchement... Je m'en fous de ce que c'est... J'ai juste un mal de crâne de l'espace !!"
z "Enfin bon, je ne peux pas faire grand chose pour ça..."
z "Maintenant, revenons à nos moutons !"
z "D'où est-ce que tu viens ?!"
ue "Je viens..."
ue "d'Albanie..."
z "Ah! Ah! Ah!"
z "Qu'est-ce que tu peux être drôle !"
ue "Qu'est-ce que j'ai dis ?"
z "L'Albanie a été détruite il y a 20 ans !"
ue "Tu es sûre ?"
ue "Parce que j'ai bien le souvenir que ce pays existe encore..."
z "Mais..."
z "Mais... Tu ne sortirais pas d'une grotte toi ?!"
z "Femme des cavernes ?!"
ue "Non !!"
ue "C'est juste que tout ce bouscule dans ma tête..."
ue "D'aillleurs..."
hide zya
with fade
hide cell
with fade
show cell
with fade
hide cell
with fade
show cell
with fade
hide cell
with fade
z "Hé Hé !"
z "Me clamse pas dans les bras !"
z "Docteur !"
z "Docteur ! Venez !"
z "Docteur ! Venez ! J'ai besoin de vous !"
z "Docteur ! Venez ! J'ai besoin de vous ! IMMEDIATEMENT !"
unknow "C'est bon ! Je suis là..."
unknow "Non mais !"
unknow "Je vous avais interdis de la frapper !"
z "Mais je n'ai pas..."
unknow "Taisez-vous ! Et aidez-moi à l'apporter à l'infirmerie !"
z "Oui madame..."
window hide
show pls_tard
with fade
$ renpy.pause(3, hard=True)
hide pls_tard
with dissolve
unknow "Hé oh ?!"
ue "Mmm..."
unknow "Hé mon amie... Tu te réveilles..."
ue "Hmm..."
show infirm
with dissolve
hide infirm
with dissolve
show infirm
with dissolve
show ass at left
show zya at right
unknow "Hé ? Hé !"
unknow "T'es réveillée !"
ue "Hmm...."
ue "Où suis-je..."
unknow "Tu es à l'imfirmerie..."
unknow "J'ai failli en oublier mes manières !"
unknow "Je m'apelle Anne mais si tu veux tu peux m'appeler l'Infirmère comme tous ceux qui habitent ici..."
ue "{i}Comment est-ce que je vais l'appeler ?{/i}"
menu:
    "Anne":
        $ inf = "Anne"
    "Infirmère":
        $ inf = "Infirmère"
ue "Je pense que je préfère vous appeler [inf]."
inf "Comme tu veux."
inf "Par contre il faut que je te dise..."
inf "Je n'ai jamais vu quelqu'un aussi bizarre que toi..."
ue "Qu'est-ce que vous voulez dire par là ?"
n "Ouais qu'est-ce qu'elle veut dire, je suis bizarre... JE NE SUIS PAS BIZARRE !!!!"
inf "En fait..."
inf "Quand vous êtes tombés dans les pommes, on vous a amené ici et j'en ai profité pour faire une analyse de sang."
inf "Mais je ne m'attendais pas à être autant surprise que ça..."
inf "Au moment des résulstats"
inf "J'ai remarqué que tu avais plusieurs anomalies dans ton sang"
ue "Que voulez-vous dire par \"anomalies\" dans mon sang ?"
inf "Tu as plusieurs enzymes et traces de certaines sources qui, théoriquement auraient du te tuer mais..."
ue "Mais ?!"
inf "Ca fait tout le contraire..."
inf "Ca te soigne plus qu'autre chose..."
inf "Prenons comme exemple..."
inf "...le plutonium 568"
inf "Normalement il devrait ronger petit à petit les cellules de ton cerveau..."
inf "Mais là... Il fait éxactement le contraire... Il crée de plus en plus de connections entre tes neurones."
inf "Par contre ça a affecté ton cerveau car 90 pourcents de ta zone droite est actif tout le temps même quand t'es inconsciente..."
inf "Et..."
inf "Je suis obligée de te le dire..."
inf "Mais..."
inf "N'as-tu pas l'impression que quelques fois quelqu'un te parle dans ta tête ?"
ue "{i}Qu'est-ce que je fais ???{/i}"
n "Tu ne le dis surtout PAS !!"
n "Je la reconnais..."
n "Je l'ai déjà vu quelquepart..."
n "Attends..."
n "Prépare toi au choc !"
ue "{i}De quoi ?!{/i}"
ue "Ahhhhhh !!!!!"
hide ass
hide zya
hide infirm
with fade
show white_screen
with fade
show alex at right
ue "Mais t'es taré ?!"
n "Non..."
ue "Ca fait SUPER mal !"
n "Désolé !"
n "Mais je devais le faire pour qu'on puisse parler tranquillement"
n "Et surtout que je retrouve la mémoire pour savoir pourquoi je connais cette [inf]..."
n "Alors..."
n "Ah !"
n "Trouvé !"
hide white_screen
with fade
show lab
with fade
n "écoute juste et ne parle pas !"
show doc at left
doc "Alors, comment va notre sujet test ??"
show ass at right
ass "Comme d'habitude, je serai tentée de dire..."
doc "Pouvez vous un peu mieux me décrire la situation car c'est mon premier jour avec le sujet test"
ass "Il fait quelques fois des convulsions durant la nuit..."
doc "Et c'est grave ?"
ass "Non, c'est normal avec tout ce qu'on lui a mis dans le crane, c'est normal qu'il y ait des effets secondaires..."
doc "J'aimerais savoir, vous dites \"Le sujet Test\" mais est-ce un homme ou une femme ?"
ass "C'est une femme monsieur et elle s'appelle [nomduheroes]."
hide doc
hide ass
hide lab
with fade
show white_screen
with fade
n "Alors ?"
n "Qu'est-ce que t'en pense ?"
ue "J'en pense que..."
ue "Je suis en fait le sujet d'une expérience..."
ue "C'est un peu bizarre de dire ça..."
n "Voilà..."
n "C'est pourquoi je ne veux pas que l'on dise à [inf] que j'existe et que tu puisses me parler et m'entendre..."
ue "Je comprends mieux maintenant..."
inf "Hé oh !"
inf "Hé ! Réveille toi !"
n "Bon il faut mieux que tu te réveilles..."
hide white_screen
with fade
show infirm
with fade
inf "Ah..."
ue "Hmmm..."
ue "Désolée..."
ue "Que s'est-il passé ?"
inf "Tu t'es de nouveau évanouie..."
inf "Alors ?"
ue "De quoi ?"
inf "Est-ce que tu as déjà entendu quelqu'un te parler dans ta tête ?"
jump inf_1_choix

label inf_1_choix:
menu:
    "Non":
        inf "D'accord..."
        inf "Tu es sûre que tu me dis la vérité ?"
        ue "Mais si je vous dis que je n'entends personne dans ma tête !"
        inf "C'est bon je te crois..."
        inf "heureusement que tu n'entends personne... Sinon, ça voulait dire que tu allais sûrement perdre contrôle de ton propre esprit dans peu de temps mais bon."
        ue "{i}Attends ! Elle a bien dit perdre le contrôle de mon propre esprit ?!{/i}"
        n "Calmos ! Elle dit ça pour te faire paniquer si tu lui as menti alors calme toi sinon elle va remarquer que tu es en train de stresser..."
        ue "{i}Pfiouuu... Alors faire comme si je ne stressais pas...{/i}"
        inf "Si tu me dis que tu n'entends rien ni personne, je te crois."
        jump inf_suite
    "Oui" if inf_dit == False:
        $ inf_dit = True
        ue "{i}Mais quest-ce que j'allais dire...{/i}"
        ue "{i}J'ai promis de ne pas dire que j'entendais quelqu'un...{/i}"
        jump inf_1_choix

label inf_suite:
inf "Bon !"
inf "Je pense que l'on va pouvoir te lever."
inf "Voilà, une jambe après l'autre..."
ue "Merci"
inf "Tu n'as pas de nausées ?"
ue "Non ..."
z "Alors c'est bon !"
z "D'où est-ce que tu viens ?"
ue "Mais d'Albanie !"
z "Je veux dire réellement !"
ue "Je ne me fous pas de vous !"
ue "Je viens réellement d'Albanie !"
z "Mais arrête de me raconter des conneries !"
inf "Oh ! [nomdezya] calme toi !"
inf "Elle dit la vérité !"
z "Mais madame !"
inf "Il n'y a pas de mais madame !"
inf "Je sais bien que l'Albanie à été détruite il y a 20 ans mais si [nomduheroes] dit qu'elle vient d'Albanie, alors ELLE VIENT D'ALBANIE !!"
inf "Compris !?"
z "Oui madame..."
inf "De quoi ?"
inf "J'ai mal entendu !"
z "OUI MADAME !"
inf "C'est mieux comme ça..."
inf "Ne t'inquiètes pas "
inf "[nomdezya] ne te fera pas mal"
n "Attends !"
ue "{i}Quoi ?{/i}"
n "Elle a dit ton nom..."
menu:
    "{i}Et alors ?{/i}":
        n "Eh bien ! Tu ne lui as pas dit !"
        n "Donc si elle le sait, c'est bizarre !"
        ue "{i}Mmmm.... Je vois....{/i}"

    "{i}Je ne lui ai pas dis mon nom !{/i}":
        ue "{i}Comment elle a pu savoir ?{/i}"
        n "Exactement !"

n "Ca veut dire qu'elle joue mal son jeu !"
n "Comme elle sait que tu t'appelles [nomduheroes] elle l'a dit mais elle n'a pas fait attention à ce qu'elle a dit !"
inf "Hé oh ! Reviens sur Terre..."
ue "Ah euh... Désolée !"
ue "Je me demandais comment vous avez pu dire mon prénom en sachant que je ne vous l'avais pas dit ?"
inf "Désolée pour cette maladresse, en fait tu la dit en dormant"
inf "T as dis exactement ça :"
ue "{b}Lachez moi ! Je m'appelle [nomduheroes] et je suis la présidente des licornes ! Alors je vous ordonne que vous me lachiez !!{/b}"
inf "Et tu répétais sans cesse ces phrases..."
inf "Mais au moins..."
inf "J'ai l'impression que c'était un beau rêve..."
ue "Heuuuuu.... Je ne peux répondre à cette question parce que je ne m'en souviens plus..."
inf "Mais dites-donc, je n'avais pas remarqué mais vous avez un language soutenu à la parole !"
$ nom_ami_heroes = "Alysson la belle"
ue "Oui, je suis en fait la cousine de la princesse [nom_ami_heroes] d'Albanie."
inf "Je vais arrêter de t'embêter avec toutes ces questions"
inf "Je vais plutôt te laisser te balader dans les environs"
inf "pour que tu puisses prendre tes marques parce que tu vas rester longtemps ici..."
ue "Merci"
jump inf_choix

label inf_choix:
menu:
    "Parler à [inf]":
        a "Pas encore fait..."
        jump inf_choix
    "Aller dormir dans le lit":
        a "Pas encore fait..."
        jump inf_choix
    "Aller voir le self":
        a "Pas encore fait..."
        jump inf_choix

a "Déso, c'est la fin de cette version..."
$ renpy.pause(2.5, hard=True)
return





































label town_immfe:

"Tu montes en haut de l'immeuble"
hide villeabb
with dissolve

"Arrivée tout en haut, tu es tellement épuisée que tu tombes dans les pommes..."
unknow "Hé oh tu m'entends ??"
ue "Mmmm..."
show immabb
with fade
unknow "Ah bah t'es enfin réveillée"
ue "Vous êtes qui ?"
ue "Et pourquoi je suis attachée ???"
"Etant suprise, tu essaye de te lever mais tu remarques que tu es attachée"
show alex at right
with fade
n "Ah le salopard!!"
ue "{i}Il a pris mon katana...{/i}"
n "Peut-être mais il n'a pas pris ton revolver qui est dans ta poche droite..."
"Tu le sors et tu tires une balle dans l'épaule de l'étranger"
unknow "AHHH!!!"
"Après lui avoir tiré dessus, tu pries pour pas qu'il tombe en bas"
"Mais malheureusement, il tombe et emporte avec lui, ta seule chance de survie..."
hide alex
with fade
hide immabb
with fade
"Tu meurs deux jours plus tard de soif..."
show game over
with dissolve
return










































label campfe:
hide autoroute
with fade
play sound audio.nature_sounds
show campagne
with fade
show alex at right
with fade
n "Tu as décidé de jouer la carte de la sécurité en allant à la campagne..."
"Après avoir marché quelques heures tu te retrouves devant cinq voitures..."
hide alex
with fade
hide campagne
with fade
show cover voitures
with dissolve
show alex at right
with fade
n "Qu'est-ce qu'on fait ??"
hide alex
with fade
menu:
   "On va les fouiller !!":
     jump camp_voit_1fe
   "Ca ne sert à rien qu'on les fouilles, elle doivent ne rien avoir...":
     jump camp_2fe


label camp_voit_1fe:
show alex at right
with fade
n "D'accord..."
ue "Alors..."
n "Regarde sous la boite à gants, peut-être qu'il y a quelquechose..."
ue "Non il n'y a rien..."
n "Alors sous le fauteuil!!"
ue "Rien non plus..."
n "Dans le coffre alors !!"
n "Il doit bien y avoir quelque-chose!!"
ue "Hmm...."
ue "Nope!"
ue "Il n'y a rien !!!"
n "Alors, qu'est-ce qu'on fait ?"
hide alex
with fade
menu:
    "On continue de fouiller !!!":
      jump camp_voit_2fe
    "Ca ne sert à rien, il faut mieux que l'on parte...":
      jump camp_2fe

label camp_voit_2fe:

ue "Il y aura peut-être quelque-chose dans la deuxième..."
show alex at right
with fade
n "Moi je dis que l'on perd du temps!!"
n "Et c'est un temps qui est extrêmement précieux dans le monde où l'on vit!!!"
ue "Alors qu'est-ce qu'il y a dedans???"
ue "Ah!!"
ue "Voilà!!"
ue "Mais..."
hide alex
with fade
hide cover voitures
with fade
show smecta
with dissolve
ue "C'est quoi du smecta ???"
show alex at right
with fade
n "Attends..."
n "Juste le temps que je prenne mon tel..."
n "Alors postgo(moteur de recherches prévu pour être capable d'être utilisé en cas d'apocalypse...) dit que le smecta est un médicament qui aide digestivement."
ue "Tu peux me traduire ça ?"
n "En gros, si tu manges quelque-chose qui n'est pas frais, tu prends du smecta puis..."
ue "Puis ?"
n "Tu reste un bon moment aux toilettes..."
hide alex
with fade
ue "Bon bah, je vais y marquer sur la boite..."
"T'écris\"à utiliser en cas de danger extrême(nourriture)\" sur la boite..."
ue "Et voilà!"
ue "Je suis sûr de ne pas en prendre sauf si je risque de mourir!!"
hide smecta
with dissolve
show cover voitures
with fade
show alex at right
with fade
n "Et maintenant, on fait quoi ??"
hide alex
with fade
ue "Maintenant..."
menu:
    "On continue de fouiller !!":
      jump camp_voit_3fe
    "On arrête là!!":
      jump camp_2fe

label camp_voit_3fe:
show alex at right
with fade
n "C'est risqué de continuer avec tout le vacarne que l'on fait..."
ue "Mais arrête de stresser !!"
ue "T'es vraiment une chochotte !!!"
n "Je n'en SUIS PAS UNE !!!!!!!!"
ue "Te mets pas dans un état pareil ..."
ue "Je disais ça pour rigoler..."
n "Hé ben, moi ça ne me fait pas rire !!!"
ue "Bon, attaquons-nous à cette voiture..."
n "Je suis sûr qu'il y a quelque-chose dans la boîte à gants !!"
n "Regarde !!!"
menu:
    "Je l'écoute":
      jump voit_3fe
    "Ca ne sert à rien de fouiller dans la boite à gants !!!":
      jump voit_3_1fe

label voit_3fe:
ue "Si t'insiste ..."
"Tu ouvres la boite à gants mais tu ne trouves rien..."
n "Bon bah..."
n "Je suis désolé d'avoir eu tort..."
"Tu as gagné 2 points de confiance par rapport à [nomdunarrateur]..."
$ points_sympathie_narrateur += 2
"Même si il a eut tort, il sait que tu l'écoutes et il t'aidera plus souvent"
ue "C'est pas grave, tout le monde peut se tromper."
ue "Oh !!"
ue "Regarde, j'ai trouvé"
hide alex
with fade
hide cover voitures
with fade
show doli
with fade
ue "du doliprane 1000mg"
hide doli
with fade
show cover voitures
with fade
show alex at right
with fade
n "En tout cas, on a fini de fouiller cette voiture..."
ue "Est-ce qu'on continue de les fouiller ??"
menu:
    "Oui !":
      jump camp_voit_4fe
    "Non !":
      jump camp_2fe







label voit_3_1fe:
n "Mais regarde quand même !!!"
ue "Je t'ai dis non!!!"
ue "Je ne fouillerais pas cette boite à gants !!!"
ue "Regarde, j'ai trouvé"
hide alex
with fade
hide cover voitures
with fade
show doli
with fade
ue "du doliprane 1000mg"
hide doli
with fade
show cover voitures
with fade
show alex at right
with fade
n "Moi je pense que l'on aurait pu trouver quelque_chose dans la boite à gants!!!"
"Tu viens de perdre 2 points de confiance de la part du narrateur..."
$ points_nice -= 2
$ points_bad += 2
$ points_sympathie_narrateur -= 2
"Tu as moins de chances qu'il t'aide dans ton aventure..."
ue "Est-ce qu'on continue de les fouiller ??"
hide alex
with fade
menu:
    "Oui !":
      jump camp_voit_4fe
    "Non !":
      jump camp_2fe


label camp_voit_4fe:
ue "Alors..."
ue "Qu'est-ce qu'on peut bien laisser dans une voiture..."
show alex at right
with fade
n "Une arme ?"
ue "Tu le penses vraiment ??"
n "Oui !"
unknow "Un numéro de téléphone ??"
ue "Heu ??"
ue "C'est qui qui vient de parler ??"
n "Je n'en ai aucune idée..."
n "Ce n'est pas toi ??"
ue "Non sinon pourquoi je demanderai qui a parlé si c'était moi ?"
n "Je n'en ai aucune idée..."
ue "Bizarre"
n "Oui très bizarre..."
ue "Enfin bon..."
"Tu continues de fouiller la voiture tout en étant beaucoup plus attentif au moindre bruit suspect que tu puisse entendre..."
ue "C'est quoi ça ???"
n "Attends, laisse moi lire ce qui est écrit..."
n "Album complet de Tal..."
n "Quoi ?!"
n "Lance-le le plus loin possible !!!"
ue "Pourquoi ??"
n "JE T'AI DIS LANCE-LE !!!!"
ue "D'accord..."
"Tu le lance le plus loin possible !!!!"
ue "Pourquoi tu m'as demandé de le jeter ?"
n "Tu connais pas Tal ?"
ue "Non... Pourquoi ? Je devrais ?"
n "Ah non ! Surtout pas !"
ue "Bon bah... D'accord..."
n "Quoi qu'il en soit..."
n "On ne peux pas tout le temps trouver ce que l'on veut..."
ue "On fait quoi ?"
hide alex
with fade
menu:
    "On fouille la dernière voiture !":
      jump camp_voit_5fe
    "On part de là !!!":
      jump camp_2fe

label camp_voit_5fe:

ue "Allez..."
ue "C'est la dernière..."
"Tu te dépêches de fouiller la dernière voiture pour quitter les lieux le plus vite possible..."
ue "Hé regarde ça !"
show alex at right
with fade
n "Mais c'est..."
n "C'est..."
hide alex
with fade
hide cover voitures
with fade
show cam
with fade
ue "Oui c'est une caméra !!!"
"Tu appuyes sur le boutton on/off"
ue "Et en plus elle fonctionne!!"
hide cam
with fade
show cover voitures
with fade
"Tu la mets autour de ton cou car tu n'as plus de place dans ton sac à dos"
$ camera = True
jump camp_2fe


label camp_2fe:
"Après avoir traversé les voitures"
hide cover voitures
with fade
stop sound
play sound audio.forest_sounds
"Tu tombes sur une forêt"
show forest
with fade
show alex at right
with fade
n "Je ne suis pas seraine..."
ue "Moi aussi..."
"30 minutes après, tu entends un bruit"
"Que fais-tu ???"
hide alex
with fade
menu:
    "Je cours voir ce qu'il se passe !!!":
      jump scene_entreefe
    "Je m'en fiche et passe mon chemin...":
      jump mort_foretfe

label mort_foretfe:
"Tu passes ton chemin..."
"Quelques minutes plus tard..."
"Par je ne sais quelle malchance..."
"Tu trébuches sur une racine"
hide forest
with fade
"Et meurs en te cognant contre un cailloux..."
show game over
with fade
"T'es morte comme une me*de !!!"
return

label scene_entreefe:
"Tu cours vers la source du bruit..."
"Et tu trouves un gars qui se bat contre des zombies..."
show alex at right
with fade
n "Il faut que l'on aille l'aider !!!"
hide alex
with fade
"Que fais-tu ???"
menu:
    "On va l'aider!!!":
      jump scene_entreecbtfe
    "On passe notre chemin, c'est trop dangereux...":
      jump mort_foretfe

label scene_entreecbtfe:
ue "Il faut qu'on l'aide !!!"
"Tu cours l'aider"
"20 minutes plus tard, après avoir décapité la plupart des zombies"
e "Je t'en suis infinimment reconnaissant..."
ue "Comment t'appelles-tu ? Mon ami"
show max
$ nomdemaximilian = "Maximilian"
e "Je m'appelle %(nomdemaximilian)s..."
maxi "Et toi alors comment t'appelles-tu ?"
ue "Je m'appelle %(nomduheroes)s"
maxi "Je suis enchanté de te rencontrer %(nomduheroes)s"
ue "Moi aussi!"
maxi "Viens, je vais te montrer l'emplacement d'un camp..."
"Vous marchez pendant une vingtaine de minutes..."
"Puis vous tombez sur..."
hide forest
with fade
show forest camp
with fade
"Sur un camp !!"
show alex at right
with fade
n "Hé oh %(nomduheroes)s, je te rappelle qu'il y a des zombies!!!"
ue "Où ?"
n "Juste devant l'entrée !!!"
hide alex with fade
maxi "Je te jure juste avant que l'on aille se battre que je te dois une fière chandelle et que du coup"
maxi "Je te suivrais jusqu'à la mort !"
"Vous allez vous battre"
"En cinq coups, vous aviez réglé le compte des zombies à l'entrée"
"Vous décidez alors de rentrer et de fermer la porte derrière vous..."
"Quand vous vous retournez"
hide forest camp
with fade
stop sound
play sound "zombie-sound-effects-free.mp3"
show zombies
with dissolve
"Vous remarquez qu'il y a des ZOMBIES!!!!"
"Et ils foncent droit sur vous!!!"
maxi "Viens, il y a la tour de guet"
maxi "Et la cabane à droite"
show alex at right
with fade
n "Qu'est-ce qu'on fait ???"
hide alex
with fade
menu:
    "On va sur la tour de guet !!":
      jump guet_1fe
    "On va dans la cabane !!!":
      jump cabane_1fe

label guet_1fe:
stop sound
hide zombies
with fade
show tour de guet
with fade
"Vous montez tous les deux par l'échelle sur la tour de guet"
"Après être montés, les zombies se sont acharnés sur la structure de la tour"
"Mais la tour a tenu bon !!"
"Vous commencez à tirer sur les zombies"
maxi "Hé ben dites-donc..."
ue "Qu'est-ce qu'il y a ??"
maxi "C'est comment tu tires ..."
ue "Hé bien quoi ??"
maxi "Je n'ai jamais vu quelqu'un tirer aussi bien"
ue "Je n'ai pas l'impression que je tire aussi bien..."
"Pas vraiment..."
"En fait sur un chargeur"
"Tu as réussi à toucher tous les zombies à proximité..."
"Tu tires tellement bien que tes balles font \"un tir, un mort\""
hide tour de guet
with fade
"Dix minutes plus tard..."
show tour de guet
with fade
ue "Je ne me sens pas très bien..."
show alex at right
with fade
n "C'est normal avec ce qu'on a mangé depuis deux jours..."
n "C'est à dire RIEN"
n "NOTHING"
n "NADA"
n "nichts"
n "Donc c'est normal, moi j'ai la dalle!!!"
hide alex
with fade
maxi "Je vois ça..."
maxi "Tiens prend ce médoc"
maxi "Dans dix minutes à peine, tu seras en pleine forme"
"Au début tout allait bien..."
"Ce n'est que deux minutes après"
"Que tu commences à voir des choses étranges..."
"Tu vois des gars super musclés..."
ue "Ohhhhh.... Des bodybuildeurs..."
"Tu vois même passer des éléphants roses avec des AK-47..."
ue "Ohhhh.... Des éléphants roses armés...."
"A un moment tu entends même Indila chanter correctement..."
"Et sans autothune !!!"
ue "Ohhhhh.... Indila est en train de chanter sans autothune..."
ue "Et c'est plutôt agréable..."
maxi "Euhhhhh...."
maxi "Ca va ?"
ue "Ohhhhhh.... Oui, nickellll chrooooooooome...."
"%(nomdemaximilian)s, voyant que tu titubais..."
"Décida de te donner le bon médicament cette fois-ci..."
"Et il jura sur sa tête de ne jamais remettre du crack dans sa poche arrière gauche..."
hide tour de guet
with fade
"Après cet évènement, tu dors étonnamment bien jusqu'au lendemain..."
"Le lendemain matin..."
show tour de guet
with fade
show alex at right
with fade
n "Je vois que quelqu'un a bien dormi..."
ue "Ne rigoles pas!"
n "Je ne rigoles pas."

if camera == True:
    ue "Je me disais que l'on pourrait peut-être faire un live..."
    n "Tu penses vraiment que ça va nous aider ?"
    ue "Bah on sait jamais..."
    n "Vas-y..."
    n "Qui ne tente rien à rien..."
    hide alex
    with fade
    "Tu allumes la caméra"
    ue "Hm Hm!"
    ue "Bonjour à tous"
    ue "Je me présente, je m'appelle %(nomduheroes)s"
    ue "Et je me disais que peut-être"
    ue "Il pourrait y avoir un sponsor qui soit sympa"
    ue "Et nous envoyer un petit cadeau"
    ue "Voili voilou"
    ue "C'est tout ce que j'avais à vous dire..."
    ue "Alors si un sponsor pouvait être sympa, ce serait cool..."
    "Tu éteins la caméra"
    ue "Alors?"
    show alex at right
    with fade
    n "Eh ben, on attend et puis on voit ce qui se passe..."
    hide alex
    with fade
    "Deux heures plus tard"
    hide tour de guet
    with fade
    show redbull_helip
    with fade
    "Un hélicoptère, avec écrit redbull dessus arriva au dessus du camp et largua un paquet de fer"
    "Assez de fer pour renforcer un batiment du camp"
    show alex at right
    with fade
    n "Que fait-t'on ?"
    hide alex
    with fade
    hide redbull_helip
    with fade
    menu:
        "On fortifie la porte d'entrée":
          jump fort_camp
        "On fortifie la cabane":
          jump fort_cab

else:
    n "Hier, quand on courait, j'ai vu qu'il y avait un tas de fer près de la porte..."
    ue "Et ?"
    n "On pourrait fortifier le camp avec..."
    ue "On pourrait..."
    ue "Mais, je n'ai vraiment aucune idée de ce que l'on pourrait fortifier avec..."
    menu:
        n "Bah il y a :"
        "La port d'entrée à fortifier !":
          jump fort_campfe
        "La cabane":
          jump fort_cabfe


label cabane_1fe:
stop sound
hide zombies
with fade
show cabane_1
with fade
"Vous rentrez dans la cabane et tuez au passage, quelques zombies sur votre chemin."
"Dès que vous êtes rentrés, les zombies se sont acharnés sur la porte d'entrée..."
maxi "Dès que j'ouvre, tu tires"
maxi "OK ?"
ue "Oui, j'ai compris!"
"Il ouvre la porte, et vous ouvrez le feu"
"Vous recommencez cette manoeuvre plusieurs fois jusqu'à arriver à bout de ces maudits zombies !!!"
ue "He ben dis-donc, on les a eu ces satanées créatures !!!"
maxi "Ah ça tu peux le dire !!"
hide cabane_1
with fade
"Dix minutes plus tard..."
show cabane_1
with fade
ue "Je ne me sens pas très bien..."
show alex at right
with fade
n "C'est normal avec ce qu'on a mangé depuis deux jours..."
n "C'est à dire RIEN"
n "NOTHING"
n "NADA"
n "nichts"
n "Donc c'est normal, moi j'ai la dalle!!!"
hide alex
with fade
maxi "Je vois ça..."
maxi "Tiens prend ce médoc"
maxi "Dans dix minutes à peine, tu seras en pleine forme"
"Au début tout allait bien..."
"Ce n'est que deux minutes après"
"Que tu commences à voir des choses étranges..."
"Tu vois des bodybuildeurs..."
ue "Ohhhhh.... Des bodybuildeurs..."
"Le problème... C'est qu'ils ont tous la tête de [nom_ennemi]..."
"Tu vois même passer des éléphants roses avec des AK-47..."
ue "Ohhhh.... Des éléphants roses armés...."
"A un moment tu entends même Tal chanter correctement..."
"Et sans autothune !!!"
ue "Ohhhhh.... Tal est en train de chanter sans autothune..."
ue "Et c'est plutôt agréable..."
maxi "Euhhhhh...."
maxi "Ca va ?"
ue "Ohhhhhh.... Oui, nickellll chrooooooooome...."
"%(nomdemaximilian)s, voyant que tu titubais..."
"Décida de te donner le bon médicament cette fois-ci..."
"Et il jura sur sa tête de ne jamais remettre du crack dans sa poche arrière droite..."
hide cabane_1
with fade
"Après cet évènement, tu dors étonnamment bien jusqu'au lendemain..."
"Le lendemain matin..."
show cabane_1
with fade
show alex at right
with fade
n "Je vois que quelqu'un a bien dormi..."
ue "Ne rigoles pas!"
n "Je ne rigoles pas."
ue "Je me disais que l'on pourrait peut-être faire un live..."
n "Tu penses vraiment que ça va nous aider ?"
ue "Bah on sait jamais..."
n "Vas-y..."
n "Qui ne tente rien à rien..."
hide alex
with fade
"Tu allumes la caméra"
ue "Hm Hm!"
ue "Bonjour à tous"
ue "Je me présente, je m'appelle %(nomduheroes)s"
ue "Et je me disais que peut-être"
ue "Il pourrait y avoir un sponsor qui soit sympa"
ue "Et nous envoyer un petit cadeau"
ue "Voili voilou"
ue "C'est tout ce que j'avais à vous dire..."
ue "Alors si un sponsor pouvait être sympa, ce serait cool..."
"Tu éteins la caméra"
ue "Alors?"
show alex at right
with fade
n "Eh ben, on attend et puis on voit ce qui se passe..."
hide alex
with fade
"Deux heures plus tard"
hide cabane_1
with fade
show redbull_helip
with fade
"Un hélicoptère, avec écrit redbull dessus arriva au dessus du camp et largua un paquet de fer"
"Assez de fer pour renforcer un batiment du camp"
show alex at right
with fade
n "Que fait-t'on ?"
hide alex
with fade
hide cabane_1
with fade
menu:
    "On fortifie la porte d'entrée":
      jump fort_campfe
    "On fortifie la cabane":
      jump fort_cabfe

label fort_campfe:
hide redbull_helip
with dissolve
show forest camp
with fade
"Tu fortifies la porte d'entrée..."
"Deux heures plus tard"
"Tu as fini de renforcer la porte"
"Et il te reste du métal"
ue "qu'est-ce qu'on pourrait en faire ???"
show alex at right
with fade
n "On pourrait faire notre logo sur la porte ?"
ue "C'est vrai, on pourrait faire un logo..."
ue "On va faire une fleur !"
n "Pourquoi ?"
ue "Si on a l'air sympa"
ue "On va pouvoir attirer plus de personnes !!"
"Tu es bizarre..."
hide alex
with fade
jump suite_histfe






label fort_cabfe:
hide redbull_helip
with dissolve
show cabane_1
with fade
"Tu fortifies la cabane"
"Il te reste un peu de fer"
"Tu pourrais faire un lit"

menu:
    " Mais pour qui ??"
    "Je vais en faire un pour moi !":
      jump lit_moife
    "Je vais faire un lit pour %(nomdemaximilian)s":
      jump lit_maxfe

label lit_moife:
"Tu décides de faire un lit pour toi"
"%(nomdemaximilian)s t'en tiens compte..."
"Tu perds deux point de sympathie avec %(nomdemaximilian)s"
$ points_sympathie_max -= 2
$ points_bad += 2
jump cab_2_cabfe


label lit_maxfe:
"Tu décides de faire un lit pour %(nomdemaximilian)s"
"%(nomdemaximilian)s t'en remercie et décide de te promettre de vraiment t'aider si tu en as besoin"
"Tu viens de gagner deux points de sympathie avec %(nomdemaximilian)s"
$ points_sympathie_max += 2
$ points_bad -= 2
$ points_nice += 2
jump cab_2_cabfe



label cab_2_cabfe:
"Il comence à faire nuit..."
n "Je pense que l'on devrait aller se coucher ..."
ue "Tu as raison..."
hide cabane_1
with fade
"Le lendemain matin"
show cabane_1
with fade
ue "Salut %(nomdemaximilian)s !"
ue "Ca va ?"
if points_sympathie_max >= 2:
    maxi "Super!"
    maxi "Et toi ?"
    maxi"Avant que tu répondes, tiens."
    hide cabane_1
    with dissolve
    show choco_blnc
    with dissolve
    maxi "J'ai trouvé ça ce matin, je te l'offre."
    hide choco_blnc
    with fade
    show cabane_1
    with dissolve

else:
    maxi "Salut ..."
    "Je trouve que %(nomdemaximilian)s est distant ces temps-ci..."
jump suite_histfe














label suite_histfe:
menu:
    "Veux-tu voir les personnages faits ?"
    "Oui!":
      jump suite_hist_2fe
    "Non !":
      jump choix_finfe


label suite_hist_2fe:

hide prog with fade
"hé"
show ass_eau with fade
"hé"
hide ass_eau with fade
"hé"
show alex with fade
"hé"
hide alex with fade
"hé"
show zya with fade
"hé"
hide zya with fade
"hé"
show doc with fade
"hé"
hide doc with fade
"hé"
show mycha2 with fade
"hé"
hide mycha2 with fade
"hé"
show mycha3 with fade
"hé"
hide mycha3 with fade
"hé"
show mycha4 with fade
"hé"
hide mycha4 with fade
"hé"
show mycha5 with fade
"hé"
hide mycha5 with fade
"hé"
show mycha6 with fade
"hé"
hide mycha6 with fade
"hé"
show mycha7 with fade
"hé"
hide mycha7 with fade
"hé"
show mycha8 with fade
jump choix_finfe

label choix_finfe:
menu:
    "Que veux-tu faire ?"
    "Je quitte le jeu !":
      jump fin_choisiefe
    "Je veux voir l'espace test !(si tu ne quittes pas, tu va tomber dans l'espace test qui est encore en développement... Ce qui inclut la possiblité que tu ais du mal à quitter après...)":
      jump testfe
    "Je regarde, avec les choix que j'ai fait, les possibilités de dialogue avec les personnages...":
      jump diadiafe

label fin_choisiefe:
a "Fin de cette version !"
hide cabane_1
with dissolve
show au_revoir
with fade
a "Merci d'avoir testé le jeu, svp dites moi comment vous l'avez trouvé..."
a "Je vous en remercierai d'avance."
return






label testfe:
"In developpement"
return

label diadia2fe:
hide mycha8
with fade
hide cabane_1
with fade
show carterpg
with fade
"hé"
"ça va ??"

#label timeforwardfe:
#    if dtime == 5:
#        jump userroomfe
#    else:
#        $dtime += 1

#label userroomfe:
#prog "En développement"

#screen money_display():
"Et la?"
show apostguy at center
with fade
"Non ?"
show apostguy at left
with move
show alex at center
with dissolve
show alex at right
with move

"BAH DOMMAGE..."


label diadiafe:


#$ maxsus = 0
#if maxsus >= 10:
#    maxi "Je ne te fais pas confiance..."
#else:
#    maxi "Je n'ai pas grand chose à te dire..."
#if maxsus >= 20:
#    maxi "Je ne te fais toujours pas confiance..."
#else:
#    maxi "Je n'ai pas grand chose à te dire..."
#if maxsus >= 30:
#    maxi "Désolé mais je ne préfère pas te parler..."
#else:
#    maxi "Je n'ai pas grand chose à te dire..."
#if maxsus >= 40:
#    maxi "Lalalala"
#else:
#    maxi "Lalalala"
#if maxsus >= 50:
#    maxi "Lalalala"
#else:
#    maxi "Lalalala"
#if maxsus >= 60:
#    maxi "Lalalala"
#else:
#    maxi "Lalalala"
#if maxsus >= 70:
#    maxi "Lalalala"
#else:
#    maxi "Lalalala"
#if maxsus >= 80:
#    maxi "Lalalala"
#else:
#    maxi "Lalalala"
#if maxsus >= 90:
#    maxi "Lalalala"
#else:
#    maxi "Lalalala"
#if maxsus >= 100:
#    maxi "Je ne reste plus avec toi, t'es louche !!"
#else:
#    maxi "Je n'ai pas grand chose à te dire..."
#$ mainstory = 0
#$ zyalove = 0
#show zya
#$ nomdezya = renpy.input("Comment est-ce qu'elle s'appelle ?(Si tu ne sais pas comment l'appeler, appuyes juste sur entrée et son nom sera celui de défaut.)")
#$ nomdezya = nomdezya.strip()
#if not nomdezya:
#    $ nomdezya = "Zya"
#if zyalove >= 10:
#    z "Lalalala"
#else:
#    z "Lalalala"

#if zyalove >= 20:
#    z "Lalalala"
#else:
#    z "Lalalala"

#if zyalove >= 30:
#    z "Lalalala"
#else:
#    z "Lalalala"

#if zyalove >= 40:
#    z "Lalalala"
#else:
#    z "Lalalala"

#if zyalove >= 50:
#    z "Lalalala"
#else:
#    z "Lalalala"

#if zyalove >= 60:
#    z "Lalalala"
#else:
#    z "Lalalala"

#if zyalove >= 70:
#    z "Lalalala"
#else:
#    z "Lalalala"

#if zyalove >= 80:
#    z "Lalalala"
#else:
#    z "Lalalala"

#if zyalove >= 90:
#    z "Lalalala"
#else:
#    z "Lalalala"

#if zyalove >= 100:
#    z "Lalalala"
#else:
#    z "Lalalala"

#$ zyasus = 0
#$ mathildelove = 0
#$ mathildesus = 0
#jump camphangarpreentryfe

label camphangarpreentryfe:
show forest_camp
$ hangarkey = False
show alex at right
with move
n "Regarde !"
hide forest_camp
show extwarehouse
with fade
n "Il y a un hangar"
"Tu vas voir si tu trouves quelque-chose à l'intérieur de ce hangar."
ue "On ne peut pas entrer car on n'a pas la clé !"
jump camphangarentryfe

label camphangarentryfe:
menu:
    n "Que fait-on ?"
    "On cherche aux alentours":
      jump camphangaralentoursfe
    "On essaie d'entrer":
      jump camphangarfe

label camphangaralentoursfe:
define voithang = False
define hangarcart = False
define hangarfrig = False
define hangarsac = False
n "D'accord, allons chercher aux alentours"
ue "Oui, il faut mieux que l'on fouille pour voir ce que l'on peut trouver."
jump camphangarchoicesfe

label camphangarchoicesfe:
menu:
    "Il y a une voiture adandonnée" if voithang == False:
      jump hangarvoitfe
    "Il y a un tas de cartons" if hangarcart == False:
      jump hangarcartfe
    "Il y a un frigo" if hangarfrig == False:
      jump hangarfrigfe
    "Il y a un sac à dos" if hangarsac == False:
      jump hangarsacfe


label hangarvoitfe:
"Tu fouilles un peu partout dans la voiture mais tu ne trouves rien..."
$ voithang = True
jump camphangarchoicesfe

label hangarcartfe:
"Tu fouilles un peu mais tu ne penses pas vraiment qu'il y a quelque chose dans ce tas de cartons..."
"Alors tu abandonnes..."
$ hangarcart = True
jump camphangarchoicesfe

label hangarfrigfe:
"Tu fouilles un peu et tu trouve la clé !"
ue "Mais qui peut bien ranger une clé dans un frigo ??"
n "Je n'en ai vraiment aucune idée..."
e "Une personne vraiment bizarre !!"
e "Peut-être ..."
ue "Mais bordel c'est qui qui nous parle !!"
n "Je n'en ai acune idée..."
$ hangarfrig = True
"Tu repars vers la porte et tu l'ouvres..."
hide extwarehouse
show intwarehouse
"Tu ne trouves rien..."
ue "Cet endroit pourrait devenir une partie de notre base..."
ue "Un entrepot ou bien une maison ..."
n "Je n'en ai aucune idée..."
hide intwarehouse
show au_revoir

label hangarsacfe:
$ hangarsac = True
"lalala"
jump camphangarfe

label camphangarfe:
hide extwarehouse
show intwarehouse
with fade
$ money = 325
#renpy.variant(money)
#ui.text("Hello, World", size=40, xalign=0.5)

n "Alors allons fouiller !!"
"Tu fouilles tous les endroits inimaginables qui sont autour du hangar..."
$ hangarkey = True
$ housekey = False

$ points_sympathie_max = 0
$ points_sympathie_pat = 0
$ points_fatigue = 0
$ points_nice = 0
$ points_bad = 0

#label puzzle:
#def __init__self:

    # Constants that let us easily change where the game is
    # located.
    #LEFT=100 #half of the size of the piece
    #TOP=100
    #COL_SPACING = 200 #the size of the piece
    #ROW_SPACING = 200
    #self.COL_NUM = 4
    #self.ROW_NUM = 3














return
