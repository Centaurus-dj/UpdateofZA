label girl_chosed:
    default girl = True
    "Je suis une femme"
    jump start_story


label guy_chosed:
    default guy = True
    "Je suis un homme"
    jump start_story

label casual_chosed:
    "Je préfère jouer avec une difficulté normale"
    jump after_diff

label hard_chosed:
    "Je préfère jouer avec une difficulté difficile"
    jump after_diff

label madmax_chosed:
    "Je préfère jouer avec la plus haute difficulté possible"
    jump after_diff
