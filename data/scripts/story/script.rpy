



################################################################################
####                  SCREENS AND IMAGEBUTTONS                              ####
################################################################################
screen map():
    imagebutton:
        idle "map"
        hover "map_hov"
        xpos 1740
        ypos .5
        action Show("mapview")

################################################################################
####                        START                                           ####
################################################################################
label start:
    call createlog from _call_createlog_1

    python:
        inventory = Inventory()
        spaghetti = Item("Spaghetti", 3)
        olives = Item("Olives", 4)
        chocolate = Item("Chocolate", 11)

    $ inventory.earn(10)
    $ current_money = inventory.money
    $ difficulty = "Casual"

    if _preferences.language == None:
        jump script_fr

    if _preferences.language == "english":
        jump script_eng
    else:
        "The language you've chosen is not supported !!"
        return


label script_fr:
    scene ecran_noir
    show screen Startabout("C'est très important !") with fade
    $ renpy.pause()
    show screen Startabout("Tu as entre tes mains une version qui n'est disponible que pour mes collaborateurs") with fade
    $ renpy.pause()
    show screen Startabout("La version de ce jeu ne doit en aucun cas être PARTAGÉE\n ou DONNÉE à une quelconque personne sans la permission de Unknown Games et du créateur de ce jeu !") with fade
    $renpy.pause()
    show screen Startabout("Je vous remercie d'avance de votre compréhension") with fade
    $ renpy.pause()
    hide screen Startabout with fade
    jump debut_hist_choix


label debut_hist_choix:
    n "test"
    menu:
        note "Que faire...."
        "Commencer par le début\n Recommendé si c'est la première fois que vous jouez":#"Cheat codes":
            $ pass_intro = False
            jump hist_continue_debut#    jump cheat_codes
        "Passer l'intro \n Recommendé si ce n'est pas votre première fois":#"Je commence l'histoire!":
            $ pass_intro = True
            jump hist_continue_debut#    jump hist_continue_debut

label hist_continue_debut:
    scene ecran_noir
    show screen attbugs_fr()
    $ renpy.pause()
    hide screen attbugs_fr
    with fade
    show presplash_fr
    with dissolve
    show screen tip_plus()
    $ renpy.pause()
    hide presplash_fr
    hide screen tip_plus
    with dissolve
    if pass_intro == False:
        jump hist_continue_debut_presplash
    else:
        jump choix_intro


label hist_continue_debut_presplash:
    show screen reshist_fr("Qu'est-ce que la vie ?") with fade
    $ renpy.pause(2, hard=True)
    show screen reshist_fr("Est-ce quelque chose de temporaire comme quand on mange une glace ?\n\nC était bien sur le moment mais maintenant que c'est fini, on aurait aimé avoir un peu plus de temps...") with fade
    $ renpy.pause(2, hard=True)
    show screen reshist_fr("Que vaut notre vie, notre civilization ?") with fade
    $ renpy.pause(2, hard=True)
    show screen reshist_fr("Et puis, Moi, que fais-je ?") with fade
    $ renpy.pause(2, hard=True)
    show screen reshist_fr("A rêver pareils questions ...") with fade
    $ renpy.pause(2, hard=True)
    hide screen reshist_fr with fade
    jump choix_intro

label choix_intro:
    call screen Choix_genre() with fade

label start_story:
    note "Heu..."
    note "Comment est-ce que je m'appelle...."
    $ nomduheros = renpy.input("")
    $ nomduheros = nomduheros.strip()
    if persistent.MC_genre == "girl":
        if not nomduheros:
            $ nomduheros = "Sarah"

        elif nomduheros.strip() in prenoms_insulte:
            prog "TU ES SERIEUX !!"
            prog "On ne donne pas comme nom aux gens des insultes !"
            prog "Même si c'est un jeu vidéo !"
            prog "Recommence !"
            jump Story_part1

        elif nomduheros.strip() in pren_fem:
            prog "Non je n'accepte juste pas !"
            prog "Recommence !"
            jump Story_part1

        elif nomduheros.strip() == "nicky minaj":
            prog "Non je n'accepte juste pas !"
            prog "Recommence !"
            jump Story_part1

        if nomduheros.strip() in cara_non_accept:
            prog "Déso ces caractères ne sont pas acceptés essaye peut-être juste avec des lettres ?"

        elif nomduheros.strip() in cara_non_accept_2:
            prog "Déso ces caractères ne sont pas acceptés essaye peut-être juste avec des lettres ?"

    elif persistent.MC_genre == "guy":
        if not nomduheros:
            $ nomduheros = "Sam"

        elif nomduheros.strip() in prenom_masc:
            a "Tu es sérieux ?!"
            jump start_story

        elif nomduheros.strip() in pren_henri:
            a "Tu sais que t'es le meilleur ?"
            a "Allez je te laisse jouer !"
            jump Story_part1

        elif nomduheros.strip() in prenoms_insulte:
            a "Tu me dégoutes !!"
            a "Recommence !"
            a "Et cette fois mets un meilleur prénom que ça !"
            jump start_story
    else:
        jump Story_part1

label Story_part1:
    note "[nomduheros]"
    note "Ouais c'est ça ! Je m'appelle [nomduheros]"
    $ renpy.hide_screen("say")
    show screen transitions_text("Tu te réveilles ...") with fade
    $ renpy.pause(1.2, hard=True)
    hide screen transitions_text with fade
    unknow "Hé oh! tu te réveilles bon sang de bonsoir!"
    show salon
    with dissolve
    show alex at right
    with fade
    u "Heu..."
    unknow "Ce n'est pas mais alors pas du tout le moment de dormir!!!"
    u "Qu'est-ce qui s'est passé??"
    unknow "Eh ben, quand toi tu révassais! Il y a eu une invasion de zombies et presque tout le monde est mort!"
    u "Pourquoi toi tu ne l'es pas??"
    unknow "Moi c'est normal, je suis dans ta tête, donc..."
    unknow "Si t'es pas mort, alors moi aussi!"
    "Heu c'est bizarre..."
    u "Bon sinon..."
    u "Quel est ton nom ?"
    $ nomdunarrateur = "Alexis"
    n "Moi c'est [nomdunarrateur]"
    u "Je suis où ?"
    n "Bah tu vois pas ? Dans ton salon..."
    u "Pourquoi je suis en SOUS VETEMENTS !!"
    n "Je sais pas, je suis pas Dieu! C'est quoi la dernière chose que t'ais faite ?"
    u "attends..."
    menu:
        "J'ai bu de la bonne vodka russe!":
            $ drug = True
            jump suite
        "Je suis tellement bête que je m'en souvient même pas...":
            jump endgame_1
        "J'ai mangé des champignons hallucinogènes !":
            $ drug = True
            jump champis_deb
        "J'ai fait un marathon de films sur Netflix":
          n "Ah ouais ?"
          n "Et t'as regardé quoi ?"
          menu:
              "Les gardiens de la galaxie 2":
                n "Mouais..."
                n "Ce n'est pas mon délire même si la bande son est bien..."
                n "Bon... Et ensuite, tu as regardé quoi ?"
                menu:
                    "Le titanic":
                        n "Mouais.... Tu n'as pas de très bon goûts cinématographiques"
                    "Le dernier chasseur de sorcières":
                        n "Mouais.... Tu n'as pas de très bon goûts cinématographiques"
                jump suite
              "Star wars VIII":
                n "Ce film fait parti de la saga la plus connue au monde !!"
                n "Tu es mon nouveau meilleur ami !!!"
                "Tu viens de gagner 50 points de sympathie avec [nomdunarrateur] !"
                $ points_sympathie_narrateur += 50
                jump suite
              "Le film ÇA":
                n "Tu me déçois très clairement..."
                "Tu viens de perdre 25 points de sympathie avec [nomdunarrateur] !"
                $ points_sympathie_narrateur -= 25
                jump suite
        "J'ai fait un marathon de séries":
          n "Ah ouais ?"
          n "Mais t'as regardé sur quelle plateforme"
          u "Tu veux dire sur PC, Tablette ou tout autre plateforme ?"
          n "Mais non!"
          n "Quand je parle de plateforme, je parle de Netflix, Amazon Prime Vidéo et toutes les autres plateformes qui se sont développées sur le marché du streaming"
          u "Ah... D'accord !"
          menu:
            "J'ai fait le marathon sur Netflix":
                n "Mais du coup t'as regardé quoi ?"
                menu:
                    "Vampire Diaries":
                        n "Si tu veux mon avis, je serai tenté de dire que c'est une bonne série"
                        n "Ses personnages sont attachants et son histoire aussi"
                        n "Et ne parlons même pas de son univers fantastique"
                    "Desperate Housewives":
                        n "Si tu veux mon avis, je serai tenté de dire que je n'aime pas cette série !"
                        menu:
                            "Et pourquoi ça ?":
                                n "Je ne peux pas l'expliquer mais à chaque fois que je commence à regarder un épisode de cette série"
                                n "J'ai tout simplement envie de dégueuler"
                            "Si tu le dis":
                                n "C'est tout ce que tu as à me dire ???"
                                n "Ouah, t'es aussi bavard qu'un poisson rouge"
                    "Demain nous appartient":
                        n "Non mais sérieusement, qui regarde encore cette série ???"
                    "Forever":
                        n "Ça, pour être une série, ça en est une !!!"
                        "."
                        ".."
                        "..."
                        n "C'est bon, on peut continuer, j'ai fini ma charade"
                    "Doctor House":
                        n "Si tu aimes bien les séries hospitalières et les séries où il y a du sang etc..."
                        n "C'est une bonne série, en plus c'est un gars qui trouves toujours des trucs improbables à ses patients"
                    "Good Doctor":
                        n "Je ne suis pas vraiment fan de cette série"
                    "Hawai 5-0":
                        n "Bien mais sans plus à part le fait que le paysage est beau"
                    "NCIS":
                        n "Pas ouf"
                    "NCIS: Los Angeles":
                        n "Cette série est mieux que NCIS mais bon...."
                        n "Ce n'est pas devenu une des meilleures séries que j'ai pu voir"
                    "NCIS: Nouvelle Orléans":
                        n "Franchement, quit à choisir"
                        n "Je préférais me suicider plutôt que de regarder cette série"
            "J'ai fait le marathon sur Amazon Prime Vidéo":
                n "Mais du coup t'as regardé quoi ?"
                menu:
                    "Vampire Diaries":
                        n "Si tu veux mon avis, je serai tenté de dire que c'est une bonne série"
                        n "Ses personnages sont attachants et son histoire aussi"
                        n "Et ne parlons même pas de son univers fantastique"
                    "Desperate Housewives":
                        n "Si tu veux mon avis, je serai tenté de dire que je n'aime pas cette série !"
                        menu:
                            "Et pourquoi ça ?":
                                n "Je ne peux pas l'expliquer mais à chaque fois que je commence à regarder un épisode de cette série"
                                n "J'ai tout simplement envie de dégueuler"
                            "Si tu le dis":
                                n "C'est tout ce que tu as à me dire ???"
                                n "Ouah, t'es aussi bavard qu'un poisson rouge"
                    "Demain nous appartient":
                        n "Non mais sérieusement, qui regarde encore cette série ???"
                    "Forever":
                        n "Ça, pour être une série, ça en est une !!!"
                        "."
                        ".."
                        "..."
                        n "C'est bon, on peut continuer, j'ai fini ma charade"
                    "Doctor House":
                        n "Si tu aimes bien les séries hospitalières et les séries où il y a du sang etc..."
                        n "C'est une bonne série, en plus c'est un gars qui trouves toujours des trucs improbables à ses patients"
                    "Good Doctor":
                        n "Je ne suis pas vraiment fan de cette série"
                    "Hawai 5-0":
                        n "Bien mais sans plus à part le fait que le paysage est beau"
                    "NCIS":
                        n "Pas ouf"
                    "NCIS: Los Angeles":
                        n "Cette série est mieux que NCIS mais bon...."
                        n "Ce n'est pas devenu une des meilleures séries que j'ai pu voir"
                    "NCIS: Nouvelle Orléans":
                        n "Franchement, quit à choisir"
                        n "Je préférais me suicider plutôt que de regarder cette série"
            "J'ai fait le marathon sur un site de streaming quelconque":
                n "Mais du coup t'as regardé quoi ?"
                menu:
                    "Vampire Diaries":
                        n "Si tu veux mon avis, je serai tenté de dire que c'est une bonne série"
                        n "Ses personnages sont attachants et son histoire aussi"
                        n "Et ne parlons même pas de son univers fantastique"
                    "Desperate Housewives":
                        n "Si tu veux mon avis, je serai tenté de dire que je n'aime pas cette série !"
                        menu:
                            "Et pourquoi ça ?":
                                n "Je ne peux pas l'expliquer mais à chaque fois que je commence à regarder un épisode de cette série"
                                n "J'ai tout simplement envie de dégueuler"
                            "Si tu le dis":
                                n "C'est tout ce que tu as à me dire ???"
                                n "Ouah, t'es aussi bavard qu'un poisson rouge"
                    "Demain nous appartient":
                        n "Non mais sérieusement, qui regarde encore cette série ???"
                    "Forever":
                        n "Ça, pour être une série, ça en est une !!!"
                        "."
                        ".."
                        "..."
                        n "C'est bon, on peut continuer, j'ai fini ma charade"
                    "Doctor House":
                        n "Si tu aimes bien les séries hospitalières et les séries où il y a du sang etc..."
                        n "C'est une bonne série, en plus c'est un gars qui trouves toujours des trucs improbables à ses patients"
                    "Good Doctor":
                        n "Je ne suis pas vraiment fan de cette série"
                    "Hawai 5-0":
                        n "Bien mais sans plus à part le fait que le paysage est beau"
                    "NCIS":
                        n "Pas ouf"
                    "NCIS: Los Angeles":
                        n "Cette série est mieux que NCIS mais bon...."
                        n "Ce n'est pas devenu une des meilleures séries que j'ai pu voir"
                    "NCIS: Nouvelle Orléans":
                        n "Franchement, quit à choisir"
                        n "Je préférais me suicider plutôt que de regarder cette série"
        "J'ai été enlevé par des aliens !":
          jump aliens
        "J'ai rendu visite à Dieu...":
          jump Dieu_pre


label Dieu_pre:
    n "Hein ?!"
    n "De quoi ?"
    n "T'as fait quoi ?"
    u "Bah..."
    u "J'ai rencontré Dieu ..."
    n "Mais comment t'as fait ?"
    u "De quoi ?"
    n "Pour le rencontrer"
    u "J'ai fait comme tout le monde..."
    n "Mais t'es bête ou quoi ?"
    u "Mais quoi ??"
    n "Personne peut aller le voir"
    n "Il n'y a que les morts qui peuvent espérer le voir !"
    u "Pourtant moi, je t'assure que je l'ai vu !"
    n "Non mec, c'est impossible !"
    n "T'es juste bizarre"
    $ dieu = True
    jump suite

label aliens:
    n "Ah ouais..."
    u "Bah, j'étais sur une table en fer et il y avait des machins verts à coté de moi..."
    u "Et en plus ils parlaient une langue super bizarre !"
    n "T'es sûr que ce n'est pas le gouvernement ?"
    u "J'étais ni soul, ni drogué"
    u "Donc je ne pense pas..."
    n "Moi je t'assure que c'est le GOUVERNEMENT !!"
    u "Mais ARRÊTE d'être complotiste à souhait !"
    n "Bon à part que tu as été enlevé par le gouvernement ça veut sûrement dire que..."
    $ complo = True
    jump suite

label champis_deb:
    show alex at right
    with fade
    n "Tu es sérieux ?"
    menu:
        u "Heu..."
        "Oui !":
          n "Mais c'est super ça !"
          n "J'ai toujours rêvé d'avoir un ami qui avait lui aussi mangé des champignons hallucinogènes !"
          n "Du coup ça veut dire..."
          jump suite
        "Non !":
          n "Quel dommage !"
          n "J'aurais aimé avoir quelqu'un qui savait ce que ça faisait des chamignons hallucinogènes..."
          n "Mais t'inquiètes, c'est pas grave..."
          n "Du coup, ça veut dire ..."
          jump suite
label endgame_1:
    n "T'es sérieux là???"
    u "heu je crois bien..."
    menu:
        "Je suis sûr!":
          jump suppose_endgame
        "Non non! Je rigolais! J'ai bu de la vodka!":
          jump suite

################################################################################
##
##
################################################################################
##
##  THIS IS THE NEXT STEP OF THE STORY
##
################################################################################

label suite:
    show screen statsbar()
    if drug == True :
        n"C'est encore une soirée qui s'est mal finie!"
        u "Bon, on ne va pas en faire tout un plat!"
        n "Non t'inquiètes pas!"
        n "Je te laisse voir de toi même comment on est dans la me*de... Bonne chance!"
        "Enfin bon, quel réveil bizarre... Je viens de me réveiller et je suis en sous-vêtements... Il faut que je fasse quelque chose!"
    menu:
        "Il faut mieux que je fouille la maison pour voir ce que je trouve...":
          jump suite_correcte
        "Moi je suis un warrior! Je préfère aller dehors!":
          jump endgame_2
    if dieu == True:
        n "T'as du passer du bon temps sur cette planète..."
        n "Même si t'es bizarre..."
        "Enfin bon, quel réveil bizarre... Je viens de me réveiller et je suis en sous-vêtements... Il faut que je fasse quelque chose!"
    menu:
        "Il faut mieux que je fouille la maison pour voir ce que je trouve...":
          jump suite_correcte
        "Moi je suis un warrior! Je préfère aller dehors!":
          jump endgame_2
    if complo == True:
        n "J'espère que t'as du bon temps sur cette planète..."
        n "Quand elle était encore civilizée et surtout contrôlée par les GOUVERNEMENTS"
        "Enfin bon, quel réveil bizarre... Je viens de me réveiller et je suis en sous-vêtements... Il faut que je fasse quelque chose!"
    menu:
        "Il faut mieux que je fouille la maison pour voir ce que je trouve...":
          jump suite_correcte
        "Moi je suis un warrior! Je préfère aller dehors!":
          jump endgame_2
    if complo == False, dieu == False, drug == False:
        n "T'as du passer du bon temps quand cette planète était encore civilizée..."
        u "Ouais..."
        "Enfin bon, quel réveil bizarre... Je viens de me réveiller et je suis en sous-vêtements... Il faut que je fasse quelque chose!"
    menu:
        "Il faut mieux que je fouille la maison pour voir ce que je trouve...":
          jump suite_correcte
        "Moi je suis un warrior! Je préfère aller dehors!":
          jump endgame_2

label suppose_endgame:
    n "Bah vas t-en... Je ne peux pas te laisser jouer si t'es aussi bête!"
    hide alex
    hide salon
    with fade
    show game over
    with pixellate
    return


label endgame_2:
    n "Tu te prépares à sortir."
    hide alex
    with fade
    hide salon
    with dissolve
    show zombie
    with dissolve
    n "Après être sorti, tu croises un zombie et, sans être équipé tu meurs mangé"
    n "Au lieu d'avoir survécu, tu t'es donné à manger à un zombie... On aurait presque pu dire que t'as été altruiste..."
    show game over
    with dissolve
    return


label suite_correcte:
    n "Tu regarde autour de toi et tu vois qu'il y a la porte du garage, la cuisine, des escaliers et des toilettes."
    n "Que choisis-tu ?"

label choix_maison:
    scene salon
    call screen House_imagemap()


label cuisine:
    u "Je suis allé regarder dans la cuisine voir si, par je ne sais quel miracle, quelqu'un aurait pu laisser quelque chose..."
    n "Tu fouilles un peu partout, sous l'évier, dans le frigo, t'es même allé fouiller dans la poubelle..."
    hide alex
    with fade
    u "Mais tout ça, ça a payé! J'ai trouvé..."
    hide salon
    with dissolve
    show boites_de_conserves
    with dissolve
    u "deux boites de conserves"
    hide boites_de_conserves
    with dissolve
    show coca
    with dissolve
    u "Et un coca!"
    hide coca
    with dissolve
    show salon
    with dissolve
    show alex at right
    with fade
    n "Après avoir fouillé la cuisine tu retournes au salon."
    n "Il te reste..."
    $ dtime += 1
    $ hour += 3
    jump choix_maison


label toilettes:
    u "Je me dis que l'on ne sait jamais! Peut-être qu'il y a quelque-chose de bien..."
    n "Et t'avais raison! En ouvrant la porte tu trouves.."
    hide alex
    with fade
    hide salon
    with dissolve
    show magnum at right
    n "un magnum chargé"
    show munitions magnum at left
    n "et une boite de munitions!"
    hide magnum
    hide munitions magnum
    with dissolve
    show salon
    with dissolve
    show alex at right
    with fade
    u "Je viens de fouiller deux endroits sur quatres et je n'ai toujours pas trouvé d'habits..."
    u "Il me reste à fouiller..."
    $ dtime += 1
    $ hour += 3
    jump choix_maison

label garage_1:
    u "Je décide du coup d'aller fouiller le garage..."
    n "Ca ne t'as pas rapporté grand chose à part savoir qu'il y a une voiture dans le garage et que tu ne peux pas la conduire car tu n'as pas la CLÉ!!!"
    jump choix_maison

label etage_1:
    hide salon
    with dissolve
    show chambre at center
    with dissolve
    u "Je monte à l'étage et je trouve deux chambres..."
    u "Il y a apparemment ma chambre et celle de ma soeur..."
    n "Hop Hop Hop!! Comment tu sais que c'est ta chambre ?"
    u "Bah c'est simple, sur une porte c'est écrit \"ma chambre\" et l'autre c'est écrit \"chambre de ma soeur\", donc ce n'est pas difficile de savoir où se trouve ma chambre!"
    n "Ta logique est imparrable... *en pensées* Mais qu'est-ce qu'il est con..."
    u "Je décide alors d'aller fouiller la mienne puis celle de ma soeur."
    hide alex
    with fade
    hide chambre
    with dissolve
    show katana
    with dissolve
    u "Je trouve un katana"
    hide katana
    with dissolve
    show chapeau
    with dissolve
    u "et un chapeau de shériff..."
    hide chapeau
    with dissolve
    show salon
    with dissolve
    show alex at right
    with fade
    $ dtime += 1
    $ hour += 3
    jump choix_maison





label _2:
    queue sound "audio/epic-post_27min.mp3"
    "Tu te dis qu'il faudrait tout de même que tu fouilles le salon."
    "Après plusieurs heures de recherches..."
    hide alex
    with fade
    hide salon
    with fade
    show Tshirt
    with fade
    "Tu trouves un T-shirt"
    hide Tshirt
    with fade
    show pantalon
    with fade
    "et un pantalon sous le canapé"
    hide pantalon
    with fade
    show salon
    with fade
    show alex at right
    with fade
    n "Tu devrais fouiller dans la cheminée, on sait jamais..."
    u "Je pense qu'il n'y aura rien mais on peut toujours regarder..."
    hide alex
    with fade
    hide salon
    with fade
    show sacados
    with fade
    "Tu y trouves un sac à dos!"
    hide sacados
    with fade
    show salon_nuit
    with fade
    show alex at right
    with fade
    stop music
    stop sound
    play sound audio.night_time_sounds
    $ dtime += 1
    n "Je te signale qu'il commence à faire nuit..."
    u "Sans blague! Comme si je ne l'avais pas remarqué!"
    n "Hé oh! Calmos, moi je te dis ça comme ça mais bon si ça t'énerves, va te faire voir!"
    u "Non c'est bon, arrête!"
    "Dix minutes plus tard..."
    u "C'est bon ? T'as arrêté de faire la tête ?"
    n "Oui mais j'ai arrêté par nécéssité..."
    n "Bon, d'après ce qu'on a vu, il y a deux endroits où l'on pourrait aller dormir..."
    u "Il y a quoi ?"
    n "Il y a la possibilité d'aller dormir sur la canapé dans le salon"
    u "C'est peut-être un peu risqué..."
    n "Oui, ça peut l'être..."
    n "Sinon tu as ta chambre..."
    u "C'est vrai mais comme il y a des barres en fer qui traversent mon lit, je vais être obligé de dormir par terre..."
    n "Oui mais au moins tu as moins de risque qu'un rodeur ou un rampant vienne dans ton sommeil te manger..."
    u "Mais j'ai plus de chance d'avoir mal au dos toute la journée de demain..."
    n "Alors tu choisis quoi ?"
    u "Je choisis..."
    menu:
        "Dormir dans ma chambre!":
          jump chambre
        "Dormir au salon!":
          jump salon

label salon:
    hide alex
    with fade
    hide salon
    with dissolve
    "Le lendemain matin..."
    stop sound
    queue sound "audio/epic-post_27min.mp3"
    n "Réveilles toi !!!"
    u "Mmmm..."
    show salon
    with dissolve
    show alex at right
    with fade
    n "REVEILLE TOI BORDEL !!!!!"
    hide alex
    hide salon
    with dissolve
    show zombie
    with fade
    u "Quoi ? AHHHHHHHHHHHHHHHHHH"
    hide zombie
    with fade
    show salon
    with dissolve
    show alex at right
    with fade
    n "Hé me*de!! Ton katana vite!!"
    u "Putain!! Tiens!"
    "Tu décapites le rampant qui venait juste de te mordre..."
    u "On fait quoi maintenant??"
    n "Hé ben..."
    n "On a 23 pourcents de chances de mourir..."
    u "Qu'est-ce que tu veux dire par la ?"
    n "Je veux dire par là que l'Etat avait travaillé sur un médicament qui pouvait te sauver mais le fait est que je ne sais pas si ils ont réussi..."
    u "Mais alors qu'est-ce qu'on attend??"
    u "Il faut de toute façon que l'on essaye de trouver ce médicament"
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
    u "Heu, oui!"
    u "Désolé..."
    u "C'est bizarre..."
    "Tu regardes ta morsure"
    n "Quoi ?"
    u "Bah ma morsure ne me fait pas mal..."
    n "Raison de plus de ne pas trainer!"
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
    u "Pas vraiment..."
    u "Je"
    u "Je ne me sens..."
    "Buahhhhhhhhhh"
    "Tu viens de vomir..."
    u "pas bien..."
    n "*dégouté* Heu... je comprends mieux maintenant..."
    "Après avoir vomi, tu ne te sens plus très bien..."
    "Et tu es fatigué..."
    n "Je pense que l'on devrait ne pas risquer d'aller à la station essence"
    u "Ouais... Je pense qu'il ne faut pas prendre ce risque..."
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
    u "Alors..."
    menu:
        "La pharmacie":
          jump salon_fin_1
        "Le camping car":
          jump salon_1

label salon_fin_1:
    n "Allons-y!"
    hide alex
    with fade
    hide autoroute
    with fade
    show zombies
    with dissolve
    u "AHHHHHHHHH"
    show alex at right
    with fade
    n "AHHHHHHHHHH"
    hide alex
    with dissolve
    "Tu es allé en direction de la pharmacie..."
    stop sound
    play sound audio.zombie_sound
    "Mais pas loin après que tu sois parti tu es tombé sur une horde de zombies"
    "Tu es mort déchiqueté..."
    hide zombies
    with fade
    stop sound
    show game over
    with dissolve
    "T'as perdu !!"
    return



label salon_1:
    n "Allons-y !"
    hide alex
    with fade
    hide autoroute
    with fade
    show camping_car_1
    with fade
    "Après être monté dans le camping car, tu te dépêches de fermer la porte."
    show alex at right
    with fade
    n "Ouffff...."
    n "On a eu chaud !!!"
    u "Ah ça tu peux le dire!"
    stop sound
    play sound audio.zombie_sound
    u "Passer à deux doigts d'une horde de zombies mais chuuuuut!"
    "Tu te tais car tu ne veux pas te faire remarquer par les zombies"
    stop sound
    "Dix minutes plus tard..."
    "La horde de zombies venait de passer"
    u "Bon..."
    u "Maintenant que le danger est écarté..."
    u "Je vais me reposer..."
    stop sound
    play sound audio.night_time_sounds
    hide alex
    with fade
    hide camping_car_1
    with fade
    "Trois heures plus tard..."
    u "Mmmmmm..."
    show camping_car_1
    with fade
    stop sound
    play sound "audio/epic-post_27min.mp3"
    show alex at right
    with fade
    n "Rebonjour !"
    n "Mon ami, t'es recinqué ?"
    u "Oui..."
    n "on devrait aller voir à la pharmacie si on trouve quelque-chose..."
    u "Bonne idée!"
    hide alex
    with fade
    "Tu descends et tu fais bien attention de regarder partout pour ne pas te faire pas un zombie solitaire"
    hide camping_car_1
    with fade
    show pharmacie
    with dissolve
    "Une demi-heure plus tard..."
    u "Ca ne sert à rien!"
    u "Il n'y a pas de médicaments qui pourraient me sauver!"
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
          jump salon_fin_2
        "De t'enfermer à vie dans la pharmacie":
          jump salon_fin_3

label salon_fin_2:

    "Tu te dépêches de sortir"
    "Mais en sortant tu voies..."
    hide pharmacie
    with fade
    show zombies
    with fade
    stop sound
    play sound audio.zombie_sound
    "Des zombies"
    "Tu meurs..."
    "Mais pas en zombie"
    hide zombies
    with fade
    stop sound
    show game over
    with dissolve
    return


label salon_fin_3:
    "Tu meurs..."
    "A petit feu..."
    "Après quelques jours d'affreuses souffrances..."
    "Tu meurs et tu deviens un zombie"
    "Ces derniers jours de ta vie ont étés les plus douloureux de ta vie!!! "
    hide pharmacie
    with fade
    show game over
    with fade
    return




label chambre:
    "Tu décides d'aller dormir sur le sol de ta chambre..."
    hide alex
    with fade
    hide salon
    with fade
    "Pendant que tu dors..."
    e "Chéri ?"
    e "Grand frère ?"
    u "Maman ?"
    u "Jade ?"
    u "Que faites-vous là ?"
    mom "Nous resterons toujours avec toi..."
    sis "Nous serons dans ton coeur pour l'éternité..."
    "Elles commencent à s'éloigner..."
    u "Où allez vous ?"
    "Elles s'éloignent de plus en plus..."
    u "Non !"
    u "Revenez !"
    "Tu ne les apperçois presque plus..."
    show chambre_nuit
    with fade
    u "Que s'est-il passé ?"
    u "C'était un rêve ?"
    u "Ca avait pourtant l'air si réel..."
    n "Ca tu peux le dire..."
    n "Je croyais aussi que c'était réel..."
    "Après cette réflexion, tu te rendors..."
    hide chambre_nuit
    "Quelques-heures plus tard..."
    stop sound
    u "Ahhhhhh...."
    show chambre
    with fade
    u "Qu'est-ce que j'ai mal au dos!!"
    show alex at right
    with fade
    n "Ah bah ça, on pouvait s'en douter..."
    n "Dormir par terre ce n'est pas tout le temps confortable..."
    u "Ah ça, tu peux le dire..."
    "En descendant, tu croises un rampant, tu le tues en faisant traverser ton katana dans son crane."
    hide alex
    with fade
    hide chambre
    with fade
    show salon
    with fade
    show alex at right
    with fade
    n "Je me disais que l'on pourrait s'amuser à dézombifier la rue."
    u "Alors que veux dire \"dézombifier\""
    n "Ca veut dire: éliminer toute trace de zombies."
    u "heu..."
    menu:
        "Je vais aller m'amuser!":
          jump entr_1
        "Je préfère aller chercher des survivants":
          jump surv_1

label entr_1:
    hide alex
    with fade
    hide salon
    with fade
    show maison depart
    with fade
    "Tu t'équipes de ton katana et tu vas t'amuser à tuer du zombie."
    "Quelques heures plus tard, après avoir vidé toute la rue des zombies qu'il pouvait y avoir."
    show alex at right
    with fade
    n "Je pense qu'après ça on est comme même bien entrainés."
    u "Je suis d'accord avec toi !"
    jump surv_1


label surv_1:
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
    u "Euh, c'est vrai... Ce n'est qu'une maison"
    u "Mais ça fait bizarre de quitter cet endroit..."
    n "Je sais..."
    n "Je te rappelle que je suis dans ta tête..."
    u "Oui enfin bon..."
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
          jump camp
        "En ville":
          jump ville


label ville:
    u "Je décide d'aller en ville..."
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
    u "Il faut qu'on se cache quelquepart!!"
    u "Mais où??"
    show alex at right
    with fade
    n "J'ai repéré deux cachettes potentielles"
    n "l'une est un tank et l'autre est un immeuble mais le fait est que tu seras sûrement fatigué arrivé en haut..."
    n "Alors???"
    n "Qu'est-ce qu'on fait???"
    u "Hmm..."
    hide alex
    with fade
    menu:
        "Je me cache dans le tank":
          jump town_tank
        "Je monte à l'échelle":
          jump town_imm

label town_tank:
    "Tu te dépêches de monter dans le tank avant que les zombies te rattrapent..."
    "A l'intérieur du tank tu apperçois une jeune femme"
    e "Non mais oh, qu'est-ce que tu fais là??"
    u "Ca ne se voit pas?? J'essaye de survivre aux zombies qui sont dehors!!"
    "Elle se retourne et appuye sur pleins de bouttons"
    show zya
    with fade
    "ahhh"
    hide zya
    show alttown
    with fade
    menu:
        "Veux-tu altérer son esprit ?"
        "Oui":
          jump nomzya
        "Non":
          $ nomdezya = "Zya"
          jump nomdezya_suite

label nomzya:
    n "Je suis désolé mais cette fonction n'est plus disponible...."
    $ nomdezya = "Zya"
    jump nomdezya_suite
    #$ nomdezya = renpy.input("Comment est-ce qu'elle s'appelle ?(Si tu ne sais pas comment l'appeler, appuyes juste sur entrée et son nom sera celui de défaut.)")
    #$ nomdezya = nomdezya.strip()
    #if not nomdezya:
    #    $ nomdezya = "Zya"
    #if nomdezya.strip() in pren_fem:
    #    a "recommence !"
    #    jump nomzya
    #if nomdezya.strip() in prenoms_insulte:
    #    a "arrête de mettre des insultes !!"
    #    jump nomzya

label nomdezya_suite:
    hide salon_nuit
    hide salon
    hide alttown
    with fade
    e "Au fait je m'appelle %(nomdezya)s et toi c'est comment?"
    u "Moi c'est %(nomduheros)s"
    z "Hé bien, je suis enchantée de te rencontrer %(nomduheros)s"
    u "De même"
    "Elle réussit à démarrer le tank"
    play sound audio.tank_moving
    "Vous roulez pendant des kilomètres avec celui-ci"
    "laissant derrière vous de la purée de zombie..."
    stop sound
    hide villeabb
    with fade
    show entreebase
    with fade
    "Vous arrivez devant une base militaire en début de soirée..."
    "Tu es accueilli par quatres HK416"
    u "Bon, bonjour?"
    gardem "T'es qui toi ??"
    u "Heu je suis..."
    z "C'est..."
    "Tu vois que Zya essaye de parler, est-ce que tu la laisse ou pas ?"
    menu:
        "Oui":
          jump miliba_entry_1
        "Non":
          jump miliba_entry_2


label miliba_entry_1:
    z "Il est avec moi et il m'a sauvé en tuant un zombie qui était derrière moi..."
    gardem "Mais il fallait le dire plus tôt!!!!"
    "Ils t'accueillent à bras ouverts et t'offrent même une chambre!"
    jump suite_hist_town

label miliba_entry_2:
    u "Je suis un vagabond qui vient de se réveiller"
    z "%(u)s attends!!"
    u "Non c'est bon %(nomdezya)s."
    "Tu expliques ton voyage"
    "A un moment tu essayes de détendre l'athmosphère en faisant une blague sur les zombies..."
    "Ils t'en sont reconnaissant et décident de te passer une chambre qu'à toi mais surtout une HK416!!"
    "(Les armes sont la chose la plus importante)"
    hide entreebase
    with fade
    show au_revoir
    with fade
    jump suite_hist_town


label suite_hist_town:
    scene ecran_noir
    z "Le lendemain matin..."
    show entreebase
    with fade
    z "Hé ça va ?"
    u "Je vais bien et toi ?"
    z "Mouais..."
    u "Qu'est-ce qu'il y a ?"
    z "何も"
    u "De quoi ?"
    z "Ca veut dire \"rien\"..."
    u "De quoi ?! Ca veut rien dire ?"
    u "Mais alors pourquoi tu le dis ?"
    z "Mais non !"
    z "Le mot \"何も\" veut dire rien en Français !"
    u "Hein ??"
    z "Bon laisse tomber..."
    u "Ok..."
    z "Bon je te fais visiter ?"
    u "Je veux bien"
    z "Alors à droite tu as le réfectoire, on appelle ça l'ordinaire ici."
    show mess
    with fade
    $ renpy.pause(3.0, hard=True)
    z "Si tu prends ce couloir, tu tombes sur le bureau du Colonel et le mien."
    hide mess
    show burzya
    with fade
    $ renpy.pause(3.0, hard=True)
    z "Voilà c'est ici que je travaille donc c'est aussi ici que tu pourras me trouver si tu veux parler..."
    hide burzya
    show terr
    with fade
    $ renpy.pause(3.0, hard=True)
    z "Si tu sors, tu peux aller au camp d'entrainement"
    z "C'est là ou il y a la plupart des militaires en permission..."
    hide terr
    with fade
    z "Voilà les endroits auquels tu peux accéder pour l'instant..."
    u "Pour l'instant ??"
    z "Oui je te signale que c'est une base militaire !"
    z "mais ..."
    u "?"
    z "Mais si tu participes à la vie de la base et que tu fais de bonnes actions tu auras le droit d'avoir accès à d'autres zones"
    u "C'est bon à savoir tout ça !"
    z "Ne t'emballes pas trop parce que si, au contraire tu ne nous aides pas où que tu fais de mauvaises actions volontairement on te resteindra l'accès à certaines zones"
    z "Peut-être même que tu passeras quelques temps en cellule pour te remettre les idées en tête !"
    u "D'accord..."
    u "Ça aussi c'est bon à savoir..."
    u "Maintenant que je suis libre de faire ce que je veux, où est-ce que je devrais aller ?"
    $ new_chambre = True
    show reception
    with fade
    menu:
        "L'ordinaire ":
            jump milit_base_ordinaire
        "Le bureau du commandant et de zya ":
            jump milit_base_bur_zya
        "Le terrain de foot ":
            jump milit_base_terrain
        "Ma chambre ":
            jump milit_base_mychamber

label town_imm:
    "Tu montes en haut de l'immeuble"
    hide villeabb
    with dissolve
    "Arrivé tout en haut, tu es tellement épuisé que tu tombes dans les pommes..."
    e "Hé oh tu m'entends ??"
    u "Mmmm..."
    show immabb
    with fade
    e "Ah bah t'es enfin réveillé"
    u "Vous êtes qui ?"
    u "Et pourquoi je suis attaché ???"
    "Etant supris, tu essaye de te lever mais tu remarques que tu es attaché"
    show alex at right
    with fade
    n "Ah le salopard!!"
    u "*en pensées* Il a pris mon katana..."
    n "Peut-être mais il n'a pas pris ton magnum qui est dans ta poche droite..."
    "Tu le sors et tu tires une balle dans l'épaule de l'étranger"
    e "AHHH!!!"
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


label camp:
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
         jump camp_voit_1
       "Ca ne sert à rien qu'on les fouilles, elle doievent ne rien avoir...":
         jump camp_2


label camp_voit_1:
    show alex at right
    with fade
    n "D'accord..."
    u "Alors..."
    n "Regarde sous la boite à gants, peut-être qu'il y a quelquechose..."
    u "Non il n'y a rien..."
    n "Alors sous le fauteuil!!"
    u "Rien non plus..."
    n "Dans le coffre alors !!"
    n "Il doit bien y avoir quelque-chose!!"
    u "Hmm...."
    u "Nope!"
    u "Il n'y a rien !!!"
    n "Alors, qu'est-ce qu'on fait ?"
    hide alex
    with fade
    menu:
        "On continue de fouiller !!!":
          jump camp_voit_2
        "Ca ne sert à rien, il faut mieux que l'on parte...":
          jump camp_2

label camp_voit_2:
    u "Il y aura peut-être quelque-chose dans la deuxième..."
    show alex at right
    with fade
    n "Moi je dis que l'on perd du temps!!"
    n "Et c'est un temps qui est extrêmement précieux dans le monde où l'on vit!!!"
    u "Alors qu'est-ce qu'il y a dedans???"
    u "Ah!!"
    u "Voilà!!"
    u "Mais..."
    hide alex
    with fade
    hide cover voitures
    with fade
    show smecta
    with dissolve
    u "C'est quoi du smecta ???"
    show alex at right
    with fade
    n "Attends..."
    n "Juste le temps que je prenne mon tel..."
    n "Alors postgo(moteur de recherches prévu pour être capable d'être utilisé en cas d'apocalypse...) dit que le smecta est un médicament qui aide digestivement."
    u "Tu peux me traduire ça ?"
    n "En gros, si tu manges quelque-chose qui n'est pas frais, tu prends du smecta puis..."
    u "Puis ?"
    n "Tu reste un bon moment aux toilettes..."
    hide alex
    with fade
    u "Bon bah, je vais marquer sur la boite..."
    "T'écris\"à utiliser en cas de danger extrême\" sur la boite..."
    u "Et voilà!"
    u "Je suis sûr de ne pas en prendre sauf si je risque de mourir!!"
    hide smecta
    with dissolve
    show cover voitures
    with fade
    show alex at right
    with fade
    n "Et maintenant, on fait quoi ??"
    hide alex
    with fade
    u "Maintenant..."
    menu:
        "On continue de fouiller !!":
          jump camp_voit_3
        "On arrête là!!":
          jump camp_2

label camp_voit_3:
    show alex at right
    with fade
    n "C'est risqué de continuer avec tout le vacarne que l'on fait..."
    u "Mais arrête de stresser !!"
    u "T'es vraiment une chochotte !!!"
    n "Je n'en SUIS PAS UNE !!!!!!!!"
    u "Te mets pas dans un état pareil ..."
    u "Je disais ça pour rigoler..."
    n "Hé ben, moi ça ne me fait pas rire !!!"
    u "Bon, attaquons-nous à cette voiture..."
    n "Je suis sûr qu'il y a quelque-chose dans la boîte à gants !!"
    n "Regarde !!!"
    menu:
        "Je l'écoute":
          jump voit_3
        "Ca ne sert à rien de fouiller dans la boite à gants !!!":
          jump voit_3_1

label voit_3:
    u "Si t'insiste ..."
    "Tu ouvres la boite à gants mais tu ne trouves rien..."
    n "Bon bah..."
    n "Je suis désolé d'avoir eu tort..."
    "Tu as gagné 2 points de confiance de la part du narrateur..."
    "Même si il a eut tort, il sait que tu l'écoutes et il t'aidera plus souvent"
    u "C'est pas grave, tout le monde peut se tromper."
    u "Oh !!"
    u "Regarde, j'ai trouvé"
    hide alex
    with fade
    hide cover voitures
    with fade
    show doli
    with fade
    u "du doliprane 1000mg"
    hide doli
    with fade
    show cover voitures
    with fade
    show alex at right
    with fade
    n "En tout cas, on a fini de fouiller cette voiture..."
    u "Est-ce qu'on continue de les fouiller ??"
    menu:
        "Oui !":
          jump camp_voit_4
        "Non !":
          jump camp_2




label voit_3_1:
    n "Mais regarde quand même !!!"
    u "Je t'ai dis non!!!"
    u "Je ne fouillerais pas cette boite à gants !!!"
    u "Regarde, j'ai trouvé"
    hide alex
    with fade
    hide cover voitures
    with fade
    show doli
    with fade
    u "du doliprane 1000mg"
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
    "Tu as moins de chances qu'il t'aide dans ton aventure..."
    u "Est-ce qu'on continue de les fouiller ??"
    hide alex
    with fade
    menu:
        "Oui !":
          jump camp_voit_4
        "Non !":
          jump camp_2


label camp_voit_4:
    u "Alors..."
    u "Qu'est-ce qu'on peut bien laisser dans une voiture..."
    show alex at right
    with fade
    n "Une arme ?"
    u "Tu le penses vraiment ??"
    n "Oui !"
    e "Un numéro de téléphone ??"
    u "Heu ??"
    u "C'est qui qui vient de parler ??"
    n "Je n'en ai aucune idée..."
    n "Ce n'est pas toi ??"
    u "Non sinon pourquoi je demanderai qui a parlé si c'était moi ?"
    n "Je n'en ai aucune idée..."
    u "Bizarre"
    n "Oui très bizarre..."
    u "Enfin bon..."
    "Tu continues de fouiller la voiture tout en étant beaucoup plus attentif au moindre bruit suspect que tu puisse entendre..."
    u "C'est quoi ça ???"
    n "Attends, laisse moi lire ce qui est écrit..."
    n "Album complet de Jul..."
    n "Quoi ?!"
    n "Lance-le le plus loin possible !!!"
    u "Pourquoi ??"
    n "JE T'AI DIS LANCE-LE !!!!"
    u "D'accord..."
    "Tu le lance le plus loin possible !!!!"
    u "Pourquoi tu m'as demandé de le jeter ?"
    n "Tu connais pas Jul ?"
    u "C'est pas le gars qui chante avec de la quoi, déjà ?"
    n "De l'autothune..."
    u "Oui c'est-ça, de l'autothune..."
    n "Si c'est lui !!!"
    u "Je comprends mieux alors..."
    n "Quoi qu'il en soit..."
    n "On ne peux pas tout le temps trouver ce que l'on veut..."
    u "On fait quoi ?"
    hide alex
    with fade
    menu:
        "On fouille la dernière voiture !":
          jump camp_voit_5
        "On part de là !!!":
          jump camp_2

label camp_voit_5:
    u "Allez..."
    u "C'est la dernière..."
    "Tu te dépêches de fouiller la dernière voiture pour quitter les lieux le plus vite possible..."
    u "Hé regarde ça !"
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
    u "Oui c'est une caméra !!!"
    "Tu appuyes sur le boutton on/off"
    u "Et en plus elle fonctionne!!"
    hide cam
    with fade
    show cover voitures
    with fade
    "Tu la mets autour de ton cou car tu n'as plus de place dans ton sac à dos"
    $ camera = True
    jump camp_2


label camp_2:
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
    n "Je ne suis pas serain..."
    u "Moi aussi..."
    "30 minutes après, tu entends un bruit"
    "Que fais-tu ???"
    hide alex
    with fade
    menu:
        "Je cours voir ce qu'il se passe !!!":
          jump scene_entree
        "Je m'en fiche et passe mon chemin...":
          jump mort_foret

label mort_foret:
    "Tu passes ton chemin..."
    "Quelques minutes plus tard..."
    "Par je ne sais quelle malchance..."
    "Tu trébuches sur une racine"
    hide forest
    with fade
    "Et meurs en te cognant contre un cailloux..."
    show game over
    with fade
    "T'es mort comme une me*de !!!"
    return

label scene_entree:
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
          jump scene_entreecbt
        "On passe notre chemin, c'est trop dangereux...":
          jump mort_foret

label scene_entreecbt:
    u "Il faut qu'on l'aide !!!"
    "Tu cours l'aider"
    "20 minutes plus tard, après avoir décapité la plupart des zombies"
    e "Je t'en suis infinimment reconnaissant..."
    u "Comment t'appelles-tu ? Mon ami"
    show max
    $ nomdemaximilian = "Maximilian"
    e "Je m'appelle %(nomdemaximilian)s..."
    maxi "Et toi alors comment t'appelles-tu ?"
    u "Je m'appelle %(nomduheros)s"
    maxi "Je suis enchanté de te rencontrer %(nomduheros)s"
    u "Moi aussi!"
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
    n "Hé oh %(u)s, je te rappelle qu'il y a des zombies!!!"
    u "Où ?"
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
    play sound audio.zombie_sound
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
          jump guet_1
        "On va dans la cabane !!!":
          jump cabane_1

label guet_1:
    stop sound
    hide zombies
    with fade
    show tour de guet
    with fade
    "Vous montez tous les deux par l'échelle sur la tour de guet"
    "Après être montés, les zombies se sont acharnés sur la structure de la tour"
    "Mais la tour a tenu bon !!"
    "Vous commencez à tirer sur les zombies"
    maxi "Ha! Ha! Ha!"
    u "Qu'est-ce qui te fait rire ??"
    maxi "C'est comment tu tires ..."
    u "Hé bien quoi ??"
    maxi "Je n'ai jamais vu quelqu'un tirer aussi mal"
    u "Je tire très bien !!!"
    "Pas vraiment..."
    "En fait sur un chargeur"
    "Tu as réussi à toucher que quelques zombies..."
    hide tour de guet
    with fade
    "Dix minutes plus tard..."
    show tour de guet
    with fade
    u "Je ne me sens pas très bien..."
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
    "Tu vois des licornes..."
    u "Ohhhhh.... Des licornes..."
    "Tu vois même passer des éléphants roses avec des AK-47..."
    u "Ohhhh.... Des éléphants roses armés...."
    "A un moment tu entends même Jul chanter correctement..."
    "Et sans autothune!!!"
    u "Ohhhhh.... Jul il est en train de chanter sans autothune..."
    u "Et c'est plutôt agréable..."
    maxi "Euhhhhh...."
    maxi "Ca va ?"
    u "Ohhhhhh.... Oui, nickellll chrooooooooome...."
    "%(nomdemaximilian)s, voyant que tu titubais..."
    "Décida de te donner le bon médicament cette fois-ci..."
    "Et il jura sur sa tête de ne jamais remettre du crack dans sa poche droite..."
    hide tour de guet
    with fade
    "Après cet évènement, tu dors étonnamment bien jusqu'au lendemain..."
    "Le lendemain matin..."
    show tour de guet
    with fade
    show alex at right
    with fade
    n "Je vois que quelqu'un a bien dormi..."
    u "Ne rigoles pas!"
    n "Je ne rigoles pas."
    if camera == True:
        u "Je me disais que l'on pourrait peut-être faire un live..."
        n "Tu penses vraiment que ça va nous aider ?"
        u "Bah on sait jamais..."
        n "Vas-y..."
        n "Qui ne tente rien à rien..."
        hide alex
        with fade
        "Tu allumes la caméra"
        u "Hm Hm!"
        u "Bonjour à tous"
        u "Je me présente, je m'appelle %(nomduheros)s"
        u "Et je me disais que peut-être"
        u "Il pourrait y avoir un sponsor qui soit sympa"
        u "Et nous envoyer un petit cadeau"
        u "Voili voilou"
        u "C'est tout ce que j'avais à vous dire..."
        u "Alors si un sponsor pouvait être sympa, ce serait cool..."
        "Tu éteins la caméra"
        u "Alors?"
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
        u "Et ?"
        n "On pourrait fortifier le camp avec..."
        u "On pourrait..."
        u "Mais, je n'ai vraiment aucune idée de ce que l'on pourrait fortifier avec..."
        menu:
            n "Bah il y a :"
            "La port d'entrée à fortifier !":
              jump fort_camp
            "La cabane":
              jump fort_cab


label cabane_1:
    stop sound
    hide zombies
    with fade
    show cabane_1
    with fade
    "Vous rentrez dans la cabane et tuez au passage, quelques zombies sur votre chemin."
    "Dès que vous êtes rentrés, les zombies se sont acharnés sur la porte d'entrée..."
    maxi "Dès que j'ouvre, tu tires"
    maxi "OK ?"
    u "Oui, j'ai compris!"
    "Il ouvre la porte, et vous ouvrez le feu"
    "Vous recommencez cette manoeuvre plusieurs fois jusqu'à arriver à bout de ces maudits zombies !!!"
    u "He ben dis-donc, on les a eu ces satanées créatures !!!"
    maxi "Ah ça tu peux le dire !!"
    hide cabane_1
    with fade
    "Dix minutes plus tard..."
    show cabane_1
    with fade
    u "Je ne me sens pas très bien..."
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
    "Tu vois des licornes..."
    u "Ohhhhh.... Des licornes..."
    "Tu vois même passer des éléphants roses avec des AK-47..."
    u "Ohhhh.... Des éléphants roses armés...."
    "A un moment tu entends même Jul chanter correctement..."
    "Et sans autothune!!!"
    u "Ohhhhh.... Jul il est en train de chanter sans autothune..."
    u "Et c'est plutôt agréable..."
    maxi "Euhhhhh...."
    maxi "Ca va ?"
    u "Ohhhhhh.... Oui, nickellll chrooooooooome...."
    "%(nomdemaximilian)s, voyant que tu titubais..."
    "Décida de te donner le bon médicament cette fois-ci..."
    "Et il jura sur sa tête de ne jamais remettre du crack dans sa poche droite..."
    hide cabane_1
    with fade
    "Après cet évènement, tu dors étonnamment bien jusqu'au lendemain..."
    "Le lendemain matin..."
    show cabane_1
    with fade
    show alex at right
    with fade
    n "Je vois que quelqu'un a bien dormi..."
    u "Ne rigoles pas!"
    n "Je ne rigoles pas."
    u "Je me disais que l'on pourrait peut-être faire un live..."
    n "Tu penses vraiment que ça va nous aider ?"
    u "Bah on sait jamais..."
    n "Vas-y..."
    n "Qui ne tente rien à rien..."
    hide alex
    with fade
    "Tu allumes la caméra"
    u "Hm Hm!"
    u "Bonjour à tous"
    u "Je me présente, je m'appelle %(nomduheros)s"
    u "Et je me disais que peut-être"
    u "Il pourrait y avoir un sponsor qui soit sympa"
    u "Et nous envoyer un petit cadeau"
    u "Voili voilou"
    u "C'est tout ce que j'avais à vous dire..."
    u "Alors si un sponsor pouvait être sympa, ce serait cool..."
    "Tu éteins la caméra"
    u "Alors?"
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
          jump fort_camp
        "On fortifie la cabane":
          jump fort_cab

label fort_camp:
    hide redbull_helip
    with dissolve
    show forest camp
    with fade
    "Tu fortifies la porte d'entrée..."
    "Deux heures plus tard"
    "Tu as fini de renforcer la porte"
    "Et il te reste du métal"
    u "qu'est-ce qu'on pourrait en faire ???"
    show alex at right
    with fade
    n "On pourrait faire notre logo sur la porte ?"
    u "C'est vrai, on pourrait faire un logo..."
    u "On va faire une fleur !"
    n "Pourquoi ?"
    u "Si on a l'air sympa"
    u "On va pouvoir attirer plus de personnes !!"
    "Tu es bizarre..."
    hide alex
    with fade
    jump suite_hist



label fort_cab:
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
          jump lit_moi
        "Je vais faire un lit pour %(nomdemaximilian)s":
          jump lit_max

label lit_moi:
    "Tu décides de faire un lit pour toi"
    "%(nomdemaximilian)s t'en tiens compte..."
    "Tu perds deux point de sympathie avec %(nomdemaximilian)s"
    $ points_sympathie_max -= 2
    jump cab_2_cab


label lit_max:
    "Tu décides de faire un lit pour %(nomdemaximilian)s"
    "%(nomdemaximilian)s t'en remercie et décide de te promettre de vraiment t'aider si tu en as besoin"
    "Tu viens de gagner deux points de sympathie avec %(nomdemaximilian)s"
    $ points_sympathie_max += 2
    jump cab_2_cab



label cab_2_cab:
    "Il comence à faire nuit..."
    n "Je pense que l'on devrait aller se coucher ..."
    u "Tu as raison..."
    hide cabane_1
    with fade
    "Le lendemain matin"
    show cabane_1
    with fade
    u "Salut %(nomdemaximilian)s !"
    u "Ca va ?"
    if points_sympathie_max >= 2:
        maxi "Super!"
        maxi "Et toi ?"
        maxi"Avant que tu répondes, tiens."
        hide cabane_1
        with dissolve
        show chocolat
        with dissolve
        maxi "J'ai trouvé ça ce matin, je te l'offre."
        hide chocolat
        with fade
        show cabane_1
        with dissolve
    else:
        maxi "Salut ..."
        "Je trouve que %(nomdemaximilian)s est distant ces temps-ci..."
    jump suite_hist



label suite_hist:
    menu:
        "Veux-tu voir les personnages faits ?"
        "Oui!":
          jump suite_hist_2
        "Non !":
          jump choix_fin


label suite_hist_2:
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
    jump choix_fin

label choix_fin:
    menu:
        "Que veux-tu faire ?"
        "Je quitte le jeu !":
          jump fin_choisie
        "Je veux voir l'espace test !(si tu ne quittes pas, tu va tomber dans l'espace test qui est encore en développement... Ce qui inclut la possiblité que tu ais du mal à quitter après...)":
          jump test
        "Je regarde, avec les choix que j'ai fait, les possibilités de dialogue avec les personnages...":
          jump diadia

label fin_choisie:
    a "Fin de cette version !"
    hide cabane_1
    with dissolve
    show au_revoir
    with fade
    a "Merci d'avoir testé le jeu, svp dites moi comment vous l'avez trouvé..."
    a "Je vous en remercierai d'avance."
    return




label test:
    "In developpement"
    return

label diadia2:
    hide mycha8
    with fade
    hide cabane_1
    with fade
    show carterpg
    with fade
    "hé"
    "ça va ??"
    #label timeforward:
    #    if dtime == 5:
    #        jump userroom
    #    else:
    #        $dtime += 1
    #label userroom:
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


label diadia:
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
    #jump camphangarpreentry

label camphangarpreentry:
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
    u "On ne peut pas entrer car on n'a pas la clé !"
    jump camphangarentry

label camphangarentry:
    menu:
        n "Que fait-on ?"
        "On cherche aux alentours":
          jump camphangaralentours
        "On essaie d'entrer":
          jump camphangar

label camphangaralentours:
    define voithang = False
    define hangarcart = False
    define hangarfrig = False
    define hangarsac = False
    n "D'accord, allons chercher aux alentours"
    u "Oui, il faut mieux que l'on fouille pour voir ce que l'on peut trouver."
    jump camphangarchoices

label camphangarchoices:
    menu:
        "Il y a une voiture adandonnée" if voithang == False:
          jump hangarvoit
        "Il y a un tas de cartons" if hangarcart == False:
          jump hangarcart
        "Il y a un frigo" if hangarfrig == False:
          jump hangarfrig
        "Il y a un sac à dos" if hangarsac == False:
          jump hangarsac


label hangarvoit:
    "Tu fouilles un peu partout dans la voiture mais tu ne trouves rien..."
    $ voithang = True
    jump camphangarchoices

label hangarcart:
    "Tu fouilles un peu mais tu ne penses pas vraiment qu'il y a quelque chose dans ce tas de cartons..."
    "Alors tu abandonnes..."
    $ hangarcart = True
    jump camphangarchoices

label hangarfrig:
    "Tu fouilles un peu et tu trouve la clé !"
    u "Mais qui peut bien ranger une clé dans un frigo ??"
    n "Je n'en ai vraiment aucune idée..."
    e "Une personne vraiment bizarre !!"
    e "Peut-être ..."
    u "Mais bordel c'est qui qui nous parle !!"
    n "Je n'en ai acune idée..."
    $ hangarfrig = True
    "Tu repars vers la porte et tu l'ouvres..."
    hide extwarehouse
    show intwarehouse
    "Tu ne trouves rien..."
    u "Cet endroit pourrait devenir une partie de notre base..."
    u "Un entrepot ou bien une maison ..."
    n "Je n'en ai aucune idée..."
    hide intwarehouse
    show au_revoir

label hangarsac:
    $ hangarsac = True
    "lalala"
    jump camphangar

label camphangar:
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

return
