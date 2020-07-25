##Default init
init -2:

    $ hide_overlay = False # Mod
    if main_menu_bg_var == "ubi_rewards": #Background of the Game Menu
        image main_menu_bg = "ubi_rewards"
    elif main_menu_bg_var == "test_menu": #Background of the Game Menu
        image main_menu_bg = "test_menu"
    else:
        image main_menu_bg = gui.main_menu_background

    default difficulty = None #Casual | Hard | Mad Max
    default langcheck = False #variable for splashscreen choice of language
    default persistent.fstcheck = False #Variable for the Devlog
    default choice_pos = False #Variable to see if it's a positive choice
    default choice_neg = False #Variable to see if it's a negative choice
    default choice_sex = False #variable to see if it's a sexual choice
init -3:
    define main_menu_bg_var = "" #We define the variable for the Game Menu background
    define startabouttextvar = "" #We define the variable for the startabout screens(no longer used)
    define tiptoadvance = "Cliquer n'importe où pour avancer" #We define the default text for the tip on the screens

##Python Imports
init python:
    #! /usr/bin/env python
    import time #We import time if needed

##DEFAULT VARIABLES
default dtime = 0 #The time variable at start
default day = 1 #The day variable at start
default money = 0 #The money we have at start
default hour = 5 #The hour we begin the game
default pass_intro = None #variable defined to see if we pass intro
default res_icons = False #variable for the Main Menu icons or buttons
default tooltip_var = "activated"
default persistent.user = "user" #variable to know who is entering the game

if hour == 5:
    $ dtime = 0 #We update the time at Early Morning
elif hour == 7:
    $ dtime = 1 #We update the time at Morning
elif hour == 11:
    $ dtime = 2 #We update the time at Noon
elif hour == 12:
    $ dtime = 3 #We update the time at Afternoon
elif hour == 18:
    $ dtime = 4 #We update the time at night
elif hour == 21:
    $ dtime = 5 #We update the time at Late Night
elif hour > 24:
    $ hour = 1 #we reset the hour
    $ day += 1 #We add one day in total

python:
    nexttime = time.time()
    while True:
        HourTime(hour)          # take t sec
        nexttime += 3
        sleeptime = nexttime - time.time()
        if sleeptime > 0:
            time.sleep(sleeptime)


default tt = Tooltip("") # change this default to this exactly (not " ", actually "")
default x = 500 # add three lines to get mouse position
default y = 400
$ x,y = renpy.get_mouse_pos()


##Game Variables
default mainstory = 0
default niveau = 1
#Booleans
default hangarkey = False #The key to enter the hangar
default housekey = False #The key to enter the house
default pongcorrect = False #Have we been able to win the Pong ?
default dieu = False #We've met God HIMSELF
default complo = False #We are sure there's a complo on us
default cuis = False #Have we checked the kitchen ?
default esc = False #Have we checked the first etage ?
default toil = False #have we checked the Toilets ?
default garage = False #Have we checked the garage ?
default boite_lettre = False #Have we checked the Letter Box ?
default inf_dit = False #I don't remember the signification of this ;)

################################################################################
## Social Vars
################################################################################
# Variables for max:
#Numbers
default pnj.max_susp = 0 #The suspicion from max to MC
default pnj.max_love = 0 #The love from max to MC
default pnj.max_angry = 0 #The angry from max to MC
default pnj.max_fear = 0 #The fear from max to MC
default pnj.max_corr = 0 #The corruption from max to MC
default pnj.max_loyalty = 0 #The loyalty from max to MC
default pnj.max_inf = 30 #The influence of Max
default pnj.max_buy = 3000 #The price to buy Max
#Booleans
default pnj.max_enslaved = False #Max haven't been enslaved (yet)
default pnj.max_free = True #Max isn't a slave (yet)
default pnj.max_dead = False #Max isn't dead (yet)
default pnj.max_suicide = False #Max haven't commit suicide (yet)
default pnj.max_killed = False #Max haven't been killed (yet)
default pnj.max_kidnapped = False #Max haven't been kidnapped (yet)
default pnj.max_hadsexwith = False #MC haven't had sex with him (yet)

# Variables for zya:
#Numbers
default pnj.zya_susp = 0 #The Suspicion from zya to MC
default pnj.zya_love = 0 #The love from Zya to MC
default pnj.zya_angry = 0 #The angry from Zya to MC
default pnj.zya_fear = 0 #The fear from zya to MC
default pnj.zya_corr = 0 #the corruption from zya to mc
default pnj.zya_loyalty = 0 #the loyalty from zya to mc
default pnj.zya_inf = 150 #The influence of Zya
default pnj.zya_buy = 12000 #The price to buy Zya
#Booleans
default pnj.zya_enslaved = False #zya haven't been ensalved (yet)
default pnj.zya_free = True #zya isn't a slave (yet)
default pnj.zya_dead = False #zya isn't dead (yet)
default pnj.zya_suicide = False #zya haven't commit suicide (yet)
default pnj.zya_killed = False #zya haven't been killed (yet)
default pnj.zya_kidnapped = False #zya haven't been kidnapped (yet)
default pnj.zya_hadsexwith = False #MC haven't had sex with her (yet)

# Variables for mathilde:
#Numbers
default pnj.mathilde_susp = 0 #The suspicion from mathilde to MC
default pnj.mathilde_love = 0 #The love from Mathilde to MC
default pnj.mathilde_angry = 0 #the angry from Mathilde to mc
default pnj.mathilde_fear = 0 #the fear from Mathilde to mc
default pnj.mathilde_corr = 0 #the corruption from Mathilde to mc
default pnj.mathilde_loyalty = 0 #the loyalty from Mathilde to mc
default pnj.mathilde_inf = 5 #The influence of Mathilde
default pnj.mathilde_buy = 1800 #The price to buy Mathilde
#Booleans
default pnj.mathilde_enslaved = False #Mathilde haven't been enslaved (yet)
default pnj.mathilde_free = True #Mathilde isn't a slave (yet)
default pnj.mathilde_dead = False #Mathilde isn't dead (yet)
default pnj.mathilde_suicide = False #Mathilde haven't commit suicide (yet)
default pnj.mathilde_killed = False #Mathilde haven't been killed (yet)
default pnj.mathilde_kidnapped = False #Mathilde haven't been kidnapped (yet)
default pnj.mathilde_hadsexwith = False #MC haven't had sex with her (yet)

# Variables for Jennifer:
#Numbers
default pnj.jenn_susp = 0 #The suspicion from jennifer to MC
default pnj.jenn_love = 0 #The love from Jennifer to MC
default pnj.jenn_angry = 0 #The angry from Jennifer to MC
default pnj.jenn_fear = 0 #The fear from Jennifer to MC
default pnj.jenn_corr = 0 #The corruption from Jennifer to MC
default pnj.jenn_loyalty = 0 #The loyalty from Jennifer to MC
default pnj.jenn_inf = 0 #The influence of Jennifer
default pnj.jenn_buy = 1200 #The price to buy Jennifer
#Booleans
default pnj.jenn_enslaved = True #Jennifer has been enslaved
default pnj.jenn_free = False #Jennifer is a slave
default pnj.jenn_dead = False #Jennifer isn't dead (yet)
default pnj.jenn_suicide = False #Jennifer haven't commit suicide (yet)
default pnj.jenn_killed = False #Jennifer haven't been killed (yet)
default pnj.jenn_kidnapped = False #Jennifer haven't been kidnapped (yet)
default pnj.jenn_hadsexwith = False #MC haven't had sex with her (yet)

# Variables for Clara:
#Numbers
default pnj.clara_susp = 0 #The suspicion from Clara to MC
default pnj.clara_love = 0 #The love from Clara to MC
default pnj.clara_angry = 0 #The angry from Clara to MC
default pnj.clara_fear = 0 #The fear from Clara to MC
default pnj.clara_corr = 0 #The corruption from Clara to MC
default pnj.clara_loyalty = 0 #The loyalty from Clara to MC
default pnj.clara_inf = 20 #The influence of Clara
default pnj.clara_buy = 2500 #The price to buy Clara
#Booleans
default pnj.clara_enslaved = False #Clara hasn't been enslaved (yet)
default pnj.clara_free = True #Clara isn't a slave (yet)
default pnj.clara_dead = False #Clara isn't dead (yet)
default pnj.clara_suicide = False #Clara haven't commited suicide (yet)
default pnj.clara_killed = False #Clara haven't been killed (yet)
default pnj.clara_kidnapped = False #Clara haven't been kidnapped (yet)
default pnj.clara_hadsexwith = False #MC haven't had sex with her (yet)
default pnj.unk_clara = True #Is Clara unknown from MC ?

#Mac'n Sell
default pnj.mac_susp = 0 #the suspicion from Mac to MC
default pnj.mac_money = 50000 #The money from Mac
default pnj.mac_inf = 80 #The ifluence of Mac


################################################################################
## Others
################################################################################

# Player Variables:
default need_charisme = False #When MC don't have charism, change True
default u_inteli = 20 #MC's inteligence
default u_strong = 10 #MC's force
default u_charisma = 0 #MC's charism
default u_jspa = 0 #Mc's unknown perk

# Cheats Variables:
default cheats = True #When Cheats codes are available change True, otherwise change False

# Public Variables:
default points_nice = 0 #[Public See] Amount of Good Actions are stored here
default points_bad = 0 #[Public See] Amount of Bad Actions are stored here

# Variables for "narrateur":
default points_nice_narrateur = 0 #No longer used

################################################################################
## Variables for the military base:
################################################################################
default new_chambre = True #Check if it's the first time MC enter his chamber
default sait_commandant = False #Check if it's the first time MC knows about the commander
##Variables for the mess:
default limit_mange = 0 #MC have too eaten
default mange6h = False #Hour when MC eat
default mange7h = False #Hour when MC eat
default mange11h = False #Hour when MC eat
default mange12h = False #Hour when MC eat
default mange18h = False #Hour when MC eat
default mange19h = False #Hour when MC eat

################################################################################
## Persistent Data
################################################################################
$ money = persistent.money

################################################################################
## Minigames Vars
################################################################################
default tst = 0
default puzzle = 0

################################################################################
## Vars about films at the beginning
################################################################################
default gardiensgala = False
default Starwars8 = False
default ca = False
default titanic = False
default lastwitchhunter = False
default letransporteur = False

################################################################################
## Vars about series at the beginning
################################################################################
default vampirediaries = False
default DesperateHousewives = False
default DNA = False
default forever = False
default doctorhouse = False
default gooddoctor = False
default NCIS = False
default NCIS_LA = False
default NCIS_NO = False

################################################################################
## Vars with inventory
################################################################################
#Items (Done and ToDo)
default sacH = False
default sacF = False
default chapH = False
default chapF = False
default armeH = False
default armeF = False
default TshirtH = False
default braF = False
default basH = False
default basF = False
default gillet_parballe_low = False
default gillet_parballe_moy = False
default gillet_parballe_big = False
default balles_pistol = False

################################################################################
## MC Stats
################################################################################
init python:
    food = 0
    water = 0
    energy = 100 #Every action, 10 pts of ennergy are lost !
    player_health = 100 #health is at 100 pts at the beginning, it evolves with clothes, armors, etc... It's not defined
    hungry = 0 #MC is not hungry at start
    thirsty = 0 #MC is not thirsty at start
    sleepy = 0 #MC is not tired at start

#Player's health Strings:
python early:
    points_fatigue = 0 #Variable for MC when he's tired or not
    fatigue = False #When he's tired, change True
    string_fatigue = "je ne suis pas fatigué" #String for being not tired
    if points_fatigue == 25:
        string_fatigue = "je suis un peu fatigué" #String for being a little tired
    elif points_fatigue == 50:
        string_fatigue = "je suis fatigué" #String for being tired
        fatigue = True
    elif points_fatigue == 75:
        string_fatigue = "je suis très fatigué" #String for being very tired
        fatigue = True
    elif points_fatigue == 100:
        string_fatigue = "je suis VRAIMENT TRÈS FATIGUÉ !!" #String for being VERY VERY TIRED
        fatigue = True
    else:
        string_fatigue = "je ne suis pas fatigué" #String if MC not tired

init python:
    points_faim = 0 #Variable for MC when he's hungry
    faim = False #When he's hungry, change True
    string_faim = "je n'ai pas faim" #String for not being hungry
    if points_faim <= 25:
        string_faim = "j'ai un peu faim" #string for being a little hungry
    elif points_faim == 50:
        string_faim = "j'ai faim" #string for being hungry
        faim = True
    elif points_faim == 75:
        string_faim = "j'ai très faim" #string for being very hungry
        faim = True
    elif points_faim == 100:
        string_faim = "j'ai VRAIMENT TRÈS FAIM !!" #string for being Deadly hungry
        faim = True
    else:
        string_faim = "je n'ai pas faim" #String if MC is not hungry

python:
    if points_faim < 0:
        points_faim = 0
python early:
    points_soif = 0 #variable for MC when he's thirsty
    soif = False #When he's thirsty, change True
    string_soif = "je n'ai pas soif" #string for not being thirsty
    if points_soif == 25:
        string_soif = "jai un peu soif" #string for being a little thirsty

################################################################################
## Monsters Stats
################################################################################
#Zombie rank 1
$ zlife = 100 #Zombie's life
$ zatck = 25 #Damages when hit Player
$ zzone_dmg = 0 #Zone of Damages
#loots available
$ zchaire_contammined = True #we can loot contamined skin
$ zapple = True #We can loot apple(s)
$ zWood = False #We can't loot Wood
$ zIron = False #We can't loot Iron

#zombie rank 2(Jump to hit):
$ z2life = 125 #Zombie's life
$ z2atck = 10 #Damages when hit Player
$ z2zone_dmg = 15 #Zone of Damages
#loots available
$ z2chaire_contammined = True #We can loot contamined skin
$ apple = True #We can loot apple(s)
$ Wood = True #We can loot Wood
$ Iron = False #we can't loot Iron

#zombie rank 3(attack of corpse to corpse(is like orc, with damages)):
$ z3life = 175 #Zombie's life
$ z3atck = 25 #Damages when hit Player
$ z3zone_dmg = 35 #Zone of Damages
#loots available
$ z3chaire_contammined = True #We can loot contamined skin
$ z3apple = True #We can loot apple(s)
$ z3Wood = True #We can loot Wood
$ z3Iron = True #We can loot Iron

#scorpio:
$ scolife = 75 #Scorpio's life
$ corps_atck = 0 #Damages when hit Player
$ dist_atck = 12 #Damages when throw something
$ zone_dmg = 0 #Zone of Damages
#loots available
$ coquille = False #we can't loot "coquille"
$ carapace = True #We can loot "carapace"

################################################################################
###########                   DEFINED FUNCTIONS                      ###########
################################################################################
python early:

    def vers_test(True):
        if tst == True:
            Jump("story_exp")
        else:
            Jump("story_norm")

    def vers_test2(old, new, current):
        curent.update(old)
        curent.update(new)
        return current

    def HourTime(hour):
        if hour == 5:
            dtime = 0
        elif hour == 7:
            dtime = 1
        elif hour == 11:
            dtime = 2
        elif hour == 12:
            dtime = 3
        elif hour == 18:
            dtime = 4
        elif hour == 21:
            dtime = 5
        elif hour > 24:
            hour = 1
