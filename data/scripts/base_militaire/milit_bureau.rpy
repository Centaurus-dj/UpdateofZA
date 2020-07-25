label bureau_zya_talk:
"En développement"
jump milit_base_reception

label bureau_zya_commandant:
if sait_commandant == False:
    u "Mr le commandant"
    $ nomdejenn = "Commandante"
    jenn "Oui ? Mon petit ?"
    u "Ah !"
    jenn "Qu'est-ce qu'il y a ?"
    u "Hmm.. Désolé de vous avoir appelé Mr !"
    jenn "Oh ! Mais ça ce n'est rien !"
    jenn "Tous les nouveaux font l'erreur, ne t'inquiètes pas"
    $ sait_commandant = True
    jenn "Alors de quoi voulais-tu me parler ?"
else:
    u "Mme la Commandante"
menu:
    "Altérer son esprit":
        "En développement"
        jump milit_base_reception
        jump jennifer_corruption
    "Parler des politiques de la base":
        "En développement"
        jump milit_base_reception
#        jump milit_bureau_politiques
    "En fait rien du tout":
        "En développement"
        jump milit_base_reception
        jenn "Alors ?"
        u "Hmm... En fait désolé j'ai oublié ce que je voulais vous dire..."
        if jenn_corr < 30:
            jenn "Alors ne venez pas me déranger !"
            jenn "Vous savez il y a bien des personnes qui travaillent dans cette base contrairement à ce que vous pensez !"
            jenn "Donc maintenant si vous m'excusez, je dois faire quelque chose d'important contrairement à vous !"
            jump milit_base_bur_zya
        elif jenn_corr < 60:
            jenn "Oh !"
            jenn "J'espère que tu vas t'en souvenir..."
            jenn "Maintenant si tu m'excuses, je dois aller faire quelque chose d'assez important..."
            jump milit_base_bur_zya
        elif jenn_corr < 90:
            jenn "Ce n'est pas grave mon amour "
            jenn "J'espère que tu vas t'en souvenir assez vite"
            jump milit_base_bur_zya
        elif jenn_corr < 120:
            jenn "Je suis désolé %(jenn_sub)s"
            jenn "Puis-je vous aider d'une quelconque manière le temps que vous vous souveniez de ce que vous vouliez dire ?"
            u "Non !"
            jenn "Alors je vais rester là si vous avez besoin de moi..."
            jump milit_base_bur_zya
        else:
            jenn "Je suis désolé %(jenn_sub)s"
            jenn "Puis-je faire quelque chose pour vous aider %(jenn_sub)s"
            u "Non !"
            jenn "Alors je vais rester là si vous avez besoin de moi..."
            jump milit_base_bur_zya
