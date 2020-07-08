################################################################################
## Jennifer Dialogs and their variations
################################################################################
label jennifer_menu:
    menu:
        "Ouvrir menu Suspicion":
            jump jennifer_suspicion
        "Ouvrir menu Amour":
            jump jennifer_love
        "Ouvrir menu en colère":
            jump jennifer_angry
        "Ouvrir menu appeurée":
            jump jennifer_fear
        "Ouvrir menu corruption":
            jump jennifer_corruption
        "Ouvrir menu loyauté":
            jump jennifer_loyalty
        "Ouvrir menu influence":
            jump jennifer_influence
        "Ouvrir menu Jennifer à acheter":
            jump jennifer_tobuy



label jennifer_suspicion:
    if pnj.jenn_susp == 0:
        jenn "Hey salut [nomduheros]"
    elif pnj.jenn_susp > 1 and pnj.jenn_susp < 20:
        jenn "Salut [nomduheros]"
    elif pnj.jenn_susp > 21 and pnj.jenn_susp < 40:
        jenn "Oh ! Salut [nomduheros]"
    elif pnj.jenn_susp > 41 and pnj.jenn_susp < 60:
        jenn "Hm... salut..."
    elif pnj.jenn_susp > 61 and pnj.jenn_susp < 80:
        jenn "..."
    elif pnj.jenn_susp > 81 and pnj.jenn_susp < 100:
        u "C'est bizarre...."
        u "Cette fois-ci elle ne s'est même pas pris la peine de se retourner..."
        u "Elle doit vraiment se douter de quelque chose..."
        u "Il faut que je fasse attention"
    else:
        jenn "Bonjour [nomduheros], j'espère que tu vas bien parce que moi je vais super bien !"
        u "Heu... Oui je vais bien pourquoi"
        "C'est étrange, elle a tout d'un coup changé de caractère..."
        jenn "Quelle bonne question !"
        jenn "Je vais te dire pourquoi je vais aussi bien"
        jenn "J'ai découvert ce que tu manigançais"
        jenn "Gardes ! Arrêtez ce traître !"
        u "Quoi ! Mais attends [nomdejenn] je t'assure que ce n'est pas ce que tu crois !"
        u "Non ! S'il te plaît, [nomdejenn] laise moi tout t'expliquer !"
        jenn "Tu me dégoutes  [nomduheros] ! Allez faites le disparaitre de ma vue"
    jump jennifer_menu
        #jump gameover_suspicion

label jennifer_love:
    if pnj.jenn_love == 0:
        jenn "salut [nomduheros]"
    elif pnj.jenn_love > 1 & < 20:
        jenn "Salut ça va [nomduheros] ?"
    elif pnj.jenn_love > 21 and pnj.jenn_love < 40:
        jenn "Salut chéri, comment ça va ?"
    elif pnj.jenn_love > 41 and pnj.jenn_love < 60:
        jenn "Salut mon chéri, comment ça va ?"
    elif pnj.jenn_love > 61 and pnj.jenn_love < 80:
        jenn "Hey, mon amour comment tu vas ?"
    elif pnj.jenn_love > 81 and pnj.jenn_love < 100:
        jenn "Hé, mon [heroscutename] ça va ?"
    else:
        jenn "...."
