init python hide:

    for file in renpy.list_files():
        if file.startswith('data/images/pc/'):
            if file.endswith('.png'):
                name = file.replace('data/images/pc/','').replace('/', ' ').replace('.png','')
                renpy.image(name, Image(file, yanchor=400))
                continue
            continue



#Images
image newMathneutre = "pose_Math_neutre.png"
image zya = "zya.png"
image side zya_side = "/data/images/pc/SideImages/zya_side"
image ass = "ass.png"
image side ass_side = "/data/images/pc/SideImages/ass_norm_side.png"
image ass_eau = "ass(eau).png"
image side ass_eau_side = "/data/images/pc/SideImages/ass_eau_side.png"
image doc = "doct.png"
image side doc_side = "/data/images/pc/SideImages/scientist_side.png"
image fanatic = "fanatique.png"
image side fanatic_side = "/data/images/pc/SideImages/fanatique_side.png"
image prog = "dev.png"
image side prog_side = "/data/images/pc/SideImages/dev_side.png"
image alex = "/data/images/pc/chars/secondme.png"
image side alex_side = "/data/images/pc/SideImages/secondme_side.png"
image mycha2 = "mycha(2).png"
image mycha3 = "mycha(3).png"
image mycha4 = "mycha(4).png"
image mycha5 = "mycha(5).png"
image mycha6 = "mycha(6).png"
image mycha7 = "mycha(7).png"
image mycha8 = "mycha(8).png"
image Tshirt = "Tshirt.png"
image carterpg = "carte_rpg.png"
image au_revoir = "au_revoir.png"
image apostguy = "postguy.png"
image forest_camp = "forest camp.jpg"
image chambre_nuitc = "chambre_nuit.jpg"
image doli = "doli.png"
image cam = "cam.png"
image boites_de_conserves = "conserve.png"
image extwarehouse = "warehouse(exterior).jpg"
image intwarehouse = "warehouse(interior).jpg"
image sacados = "sacados.png"
image pantalon = "pantalon.png"
image katana = "katana.png"
image chapeau = "chapeau.png"
image magnum = "magnum.png"
image lab = "labo.jpg"
image forest = "foret.jpg"
image salon_nuit = "data/images/pc/locations/start/salon(nuit).jpg"
image patreon = "/res/patreon.png"
image insta = "/res/insta.png"
image twitt = "/res/twitter.png"
image burzya = "bureau_zya.png"
image chambrebas = "chambre_perso.png"
image debase = "dehors_base.png"
image mess = "mess_base.png"
image terr = "terrain.png"
image alttown = "alter_town.png"
image salon = "data/images/pc/locations/start/salon.jpg"
image menu1 = "/data/images/pc/background/menu_1.jpg"
image menu2 = "/data/images/pc/background/menu_2.jpg"
image brass = "/girlie/brass.png"
image casq = "/girlie/casq.png"
image leg = "/girlie/leg.png"
image deba = "/girlie/deba.png"
image sac_east = "/girlie/sac_eastpak.png"
image ecr_sec = "/girlie/ecran_secours.png"
image shop = "/girlie/shop.png"
image lait = "/girlie/lait.png"
image oasis = "/girlie/oasis.png"
image nuro = "/girlie/nurofen.png"
image arba = "/girlie/arbalete.png"
image revol = "/girlie/revol.png"
image flocons = "/girlie/flocon.png"
image muesli = "/girlie/muesli.jpg"
image lyso = "/girlie/lyso.png"
image choco_blnc = "/girlie/choco.png"
image presplash_fr = "/data/images/pc/background/prsplsh_1.png"
image presplash_eng = "/data/images/pc/background/prsplsh_1_eng.png"
image ecran_noir = "/data/images/pc/background/ecran noir.jpg"
image cell = "cell.jpg"
image boite_let = "boite_let.webp"
image toil = "toil.jpg"
image cuis = "cuis.jpg"
image gara = "gara.jpg"
image pls_tard = "/transitions/pls_tard.png"
image infirm = "infirm.jpg"
image oui_but = "/data/images/pc/buttons/oui_but.png"
image oui_but_hover = "/data/images/pc/buttons/oui_but_hover.png"
image non_but = "/data/images/pc/buttons/non_but.png"
image non_but_hover = "/data/images/pc/buttons/non_but_hover.png"
image white_screen = "white.jpg"


#### Background Menus ####
image bg black:
    "#000000"
image backmen1 = im.Scale("/data/images/pc/background/menu_1.jpg", 1280, 720)
image menu_3_modif = im.Scale("/data/images/pc/background/menu_3_modif.jpg", 1280, 720)
image backmen3 = im.Scale("/data/images/pc/background/menu_3.jpg", 1280, 720)
image backmen4 = im.Scale("/data/images/pc/background/menu_4.jpg", 1280, 720)
image backmen5 = im.Scale("/data/images/pc/background/menu_5.jpg", 1280, 720)
image backmen6 = im.Scale("/data/images/pc/background/menu_6.jpg", 1280, 720)
image backmen7 = im.Scale("/data/images/pc/background/menu_7.png", 1280, 720)
image backmen8 = im.Scale("/data/images/pc/background/menu_8.png", 1280, 720)
image backmen9 = im.Scale("/data/images/pc/background/menu_9.png", 1280, 720)
image backmen10 = im.Scale("/data/images/pc/background/menu_10.png", 1280, 720)
image backmen11 = im.Scale("/data/images/pc/background/menu_11.png", 1280, 720)
image backmen12 = im.Scale("/data/images/pc/background/menu_12.jpg", 1280, 720)
image backmen13 = im.Scale("/data/images/pc/background/menu_13.jpg", 1280, 720)
image backmen14 = im.Scale("/data/images/pc/background/menu_14.jpg", 1280, 720)
image mainmenubg = im.Scale("/data/images/pc/background/main_menu.jpg", 1280, 720)
image backmen16 = im.Scale("/data/images/pc/background/menu_16.jpg", 1280, 720)
image backmen17 = im.Scale("/data/images/pc/background/menu_17.webp", 1280, 720)
image backmen18 = im.Scale("/data/images/pc/background/menu_18.webp", 1280, 720)
image backmen19 = im.Scale("/data/images/pc/background/menu_19.jpg", 1280, 720)
image backmen20 = im.Scale("/data/images/pc/background/menu_20.jpg", 1280, 720)
image backmen21 = im.Scale("/data/images/pc/background/menu_21.jpg", 1280, 720)
image reception = im.Scale("/data/images/pc/locations/military_base/reception.jpg", 1280, 720)
image ubi_rew1 = im.Scale("ubi-rewards/Anno1800_Wallpaper_1920_1080_Polar.png", 1280, 720)
image ubi_rew2 = im.Scale("ubi-rewards/Anno1800_Wallpaper_1920_1080_Forest.jpg", 1280, 720)
image ubi_rew3 = im.Scale("ubi-rewards/Anno1800_Wallpaper_1920_1080_Ships.jpg", 1280, 720)
image ubi_rew4 = im.Scale("ubi-rewards/Anno1800_Wallpaper_1920_1080_Success.jpg", 1280, 720)
image ubi_rew5 = im.Scale("ubi-rewards/FC5_MARYMAY_1920x1080.jpg", 1280, 720)
image ubi_rew6 = im.Scale("ubi-rewards/FC5_NICK_1920x1080.jpg", 1280, 720)
image ubi_rew7 = im.Scale("ubi-rewards/FC5_PASTOR_1920x1080.jpg", 1280, 720)
image ubi_rew8 = im.Scale("ubi-rewards/FCND_BLACK_1920x1080.jpg", 1280, 720)
image ubi_rew9 = im.Scale("ubi-rewards/FCND_WHITE_1920x1080.jpg", 1280, 720)
image ubi_rew10 = im.Scale("ubi-rewards/FCS_1920X1080.jpg", 1280, 720)
image ubi_rew11 = im.Scale("ubi-rewards/FH_MarchingFire_Wide.jpg", 1280, 720)
image ubi_rew12 = im.Scale("ubi-rewards/wallpaper_1.jpg", 1280, 720)
image ubi_rew13 = im.Scale("ubi-rewards/wallpaper_2.jpg", 1280, 720)
image ubi_rew14 = im.Scale("ubi-rewards/wallpaper_4.jpg", 1280, 720)
image ubi_rew15 = im.Scale("ubi-rewards/wallpaper_5.jpg", 1280, 720)
image ubi_rew16 = im.Scale("ubi-rewards/wallpaper_6.jpg", 1280, 720)
image ubi_rew17 = im.Scale("ubi-rewards/wallpaper_7.jpg", 1280, 720)
image ubi_rew18 = im.Scale("ubi-rewards/wallpaper_8.jpg", 1280, 720)
image ubi_rew19 = im.Scale("ubi-rewards/wallpaper_9.jpg", 1280, 720)
image ubi_rew20 = im.Scale("ubi-rewards/ACBF_THEME/ac4_Wallpaper3_1280x720.jpg", 1280, 720)
image ubi_rew21 = im.Scale("ubi-rewards/ACBF_THEME/ac4_Wallpaper2_1280x720.jpg", 1280, 720)
image ubi_rew22 = im.Scale("ubi-rewards/ACBF_THEME/ac4_Wallpaper1_1280x720.jpg", 1280, 720)
image ubi_rew22 = im.Scale("ubi-rewards/ACBF_THEME/ac4_Wallpaper4_1280x720.jpg", 1280, 720)
image ubi_rew23 = im.Scale("ubi-rewards/Desktop/Wallpaper_1920x1080_Boomer.png", 1280, 720)
image ubi_pers1 = im.Scale("ubi-rewards/Fan_Kit/Characters/Kassandra/ACOdyssey_Kassandra_CloseUp_NoHelmet (resized).jpg", 1280, 720)
image gunshop_left = im.Scale("locations_milit_base/gunshop/gunshop_left.jpg", 1280, 720)
image gunshop_left_pers = im.Scale("locations_milit_base/gunshop/gunshop_left_pers.jpg", 1280, 720)
image gunshop_right = im.Scale("locations_milit_base/gunshop/gunshop_right.png", 1280, 720)
image devlog_bg = "/data/images/pc/DevLog.png"
image update_release = "/data/images/pc/update_released_HGZA.png"
image update_release_resized = im.Scale("/data/images/pc/background/update_released_HGZA.png", 640, 360)
image devbar = im.Scale("/data/images/pc/bars/devbar.png", 20, 650)
image devbarmini = im.Scale("/data/images/pc/bars/devbar.png", 10, 50)
image devbarsepar = im.Scale("data/images/pc/bars/devbar_separated.png", 600, 10)

#Logo imgs
image test = "logo_main_menu.png"
image test_hover = "logo_main_menu_hover.png"
image fr_icon = im.Scale("/data/images/pc/icons/lang/french/fr.png", 60, 40)
image fr_icon_hov = im.Scale("/data/images/pc/icons/lang/french/fr_hover.png", 60, 40)
image en_icon = im.Scale("/data/images/pc/icons/lang/english/en.png", 60, 40)
image en_icon_hov = im.Scale("/data/images/pc/icons/lang/english/en_hover.png", 60, 40)
image de_icon = "/data/images/pc/icons/lang/deutsch/de.png"
image de_icon_hov = "/data/images/pc/icons/lang/deutsch/de_hover.png"
image logo_new = "gui/studio_icon.png"
image sett_ico = im.Scale("/data/images/pc/buttons/settings_icon.png", 50, 50)
image sett_hov1 = im.Scale("/data/images/pc/buttons/settings_icon_hover2.png", 50, 50)
image sett_hov2 = im.Scale("/data/images/pc/buttons/settings_icon_hover3.png", 50, 50)
image sett_hov3 = im.Scale("/data/images/pc/buttons/settings_icon_hover4.png", 50, 50)
image sett_hov4 = im.Scale("/data/images/pc/buttons/settings_icon_hover5.png", 50, 50)
image sett_hov5 = im.Scale("/data/images/pc/buttons/settings_icon_hover6.png", 50, 50)
image sett_hov6 = im.Scale("/data/images/pc/buttons/settings_icon_hover7.png", 50, 50)
image sett_hov7 = im.Scale("/data/images/pc/buttons/settings_icon_hover8.png", 50, 50)
image sett_hov8 = im.Scale("/data/images/pc/buttons/settings_icon_hover9.png", 50, 50)
image sett_hov9 = im.Scale("/data/images/pc/buttons/settings_icon_hover10.png", 50, 50)
image sett_hov10 = im.Scale("/data/images/pc/buttons/settings_icon_hover11.png", 50, 50)
image sett_hov11 = im.Scale("/data/images/pc/buttons/settings_icon_hover12.png", 50, 50)
image sett_hov12 = im.Scale("/data/images/pc/buttons/settings_icon_hover13.png", 50, 50)
image sett_hov13 = im.Scale("/data/images/pc/buttons/settings_icon_hover14.png", 50, 50)
image sett_hov14 = im.Scale("/data/images/pc/buttons/settings_icon_hover15.png", 50, 50)
image sett_clicked = im.Scale("/data/images/pc/buttons/settings_icon_clicked.png", 50, 50)
image load_ico = "/data/images/pc/buttons/load.png"
image load_hov1 = "/data/images/pc/buttons/load_hover.png"
image save_ico = "/data/images/pc/buttons/save.png"
image save_hov1 = "/data/images/pc/buttons/save_hover.png"
image about_ico = "/data/images/pc/buttons/about.png"
image about_hov1 = "/data/images/pc/buttons/about_hover.png"
image help_ico = "/data/images/pc/buttons/help.png"
image help_hov1 = "/data/images/pc/buttons/help_hover.png"
image quit_ico = im.Scale("/data/images/pc/buttons/quit.png", 50, 50)
image quit_hov1 = im.Scale("/data/images/pc/buttons/quit_hover.png", 50, 50)
image main_menu_ico = "/data/images/pc/buttons/main_menu_ico.png"
image main_menu_ico_hov1 = "/data/images/pc/buttons/main_menu_ico_hover.png"
image insta_icon idle = im.Scale("/data/images/pc/buttons/insta_icon.png", 60, 60)
image twitter_icon idle = im.Scale("data/images/pc/buttons/twitter_icon.png", 75, 75)
image discord_icon idle = im.Scale("data/images/pc/buttons/discord_icon.png", 75, 75)
image patreon_icon idle = im.Scale("data/images/pc/buttons/patreon_icon_idle.png", 50, 50)
image insta_icon hover = im.Scale("data/images/pc/buttons/insta_icon_hover.png", 60, 60)
image twitter_icon hover = im.Scale("data/images/pc/buttons/twitter_icon_hover.png", 75, 75)
image discord_icon hover = im.Scale("data/images/pc/buttons/discord_icon_hover.png", 75, 75)
image patreon_icon hover = im.Scale("data/images/pc/buttons/patreon_icon_hover.png", 50, 50)
image female_icon_idle = im.Scale("data/images/pc/icons/female/female_icon.png", 400, 720)
image female_icon_hover = im.Scale("data/images/pc/icons/female/female_icon_hover.png", 400, 720)
image male_icon_idle = im.Scale("data/images/pc/icons/male/male_icon.png", 400, 720)
image male_icon_hover = im.Scale("data/images/pc/icons/male/male_icon_hover.png", 400, 720)

image Renpy logo = "data/images/pc/icons/logo renpy.png"
##Stats Bar Icons
image hunger_full = im.Scale("data/images/pc/icons/statbar/hungry_icon.png", 60, 60)
image hunger_nearly_full = im.Scale("data/images/pc/icons/statbar/hungry_icon_nearly_full.png", 60 , 60)
image hunger_middle = im.Scale("data/images/pc/icons/statbar/hungry_icon_middle_full.png", 60 , 60)
image hunger_nearly_empty = im.Scale("data/images/pc/icons/statbar/hungry_icon_nearly_empty.png", 60, 60)
image hunger_empty = im.Scale("data/images/pc/icons/statbar/hungry_icon_empty.png", 60, 60)
image thirst_full = im.Scale("data/images/pc/icons/statbar/thirst_icon.png", 50, 50)
image thirst_nearly_full = im.Scale("data/images/pc/icons/statbar/thirst_icon_nearly_full.png", 50, 50)
image thirst_middle = im.Scale("data/images/pc/icons/statbar/thirst_icon_middle.png", 50, 50)
image thirst_nearly_empty = im.Scale("data/images/pc/icons/statbar/thirst_icon_nearly_empty.png", 50, 50)
image thirst_empty = im.Scale("data/images/pc/icons/statbar/thirst_icon_empty.png", 50, 50)
image energy_full = im.Scale("data/images/pc/icons/statbar/energy_icon.png", 40, 40)
image energy_nearly_full = im.Scale("data/images/pc/icons/statbar/energy_icon_nearly_full.png", 40, 40)
image energy_middle = im.Scale("data/images/pc/icons/statbar/energy_icon_middle.png", 40, 40)
image energy_nearly_empty = im.Scale("data/images/pc/icons/statbar/energy_icon_nearly_empty.png", 40, 40)
image energy_empty = im.Scale("data/images/pc/icons/statbar/energy_icon_empty.png", 40, 40)
image menu_idle = im.Scale("data/images/pc/icons/statbar/menu_icon.png", 70, 70)
image menu_hover = im.Scale("data/images/pc/icons/statbar/menu_icon_hover.png", 70, 70)



#Res Buttons:
image butt_discorden_idle = im.Scale("data/images/pc/buttons/discord_buttonen_idle.png", 156, 66)
image butt_discordfr_idle = im.Scale("data/images/pc/buttons/discord_buttonfr_idle.png", 156, 66)
image butt_discord_hover = im.Scale("data/images/pc/buttons/discord_button_hover.png", 156, 66)
image butt_twitteren_idle = im.Scale("data/images/pc/buttons/twitter_button_idle.png", 156, 66)
image butt_twitterfr_idle = im.Scale("data/images/pc/buttons/twitter_buttonfr_idle.png", 156, 66)
image butt_twitter_hover = im.Scale("data/images/pc/buttons/twitter_button_hover.png", 156, 66)
image butt_instaen_idle = im.Scale("data/images/pc/buttons/insta_buttonen_idle.png", 156, 66)
image butt_instafr_idle = im.Scale("data/images/pc/buttons/insta_buttonfr_idle.png", 156, 66)
image butt_insta_hover = im.Scale("data/images/pc/buttons/insta_button_hover.png", 156, 66)
image butt_patreonen_idle = im.Scale("data/images/pc/buttons/patreon_buttonen_idle.png", 156, 66)
image butt_patreonfr_idle = im.Scale("data/images/pc/buttons/patreon_buttonfr_idle.png", 156, 66)
image butt_patreon_hover = im.Scale("data/images/pc/buttons/patreon_button_hover.png", 156, 66)

#Settings Icons/Buttons
image icon_exemple_idle = im.Scale("/data/images/pc/buttons/icon_exemple_idle.png", 26, 46)
image icon_exemple_hover = im.Scale("/data/images/pc/buttons/icon_exemple_hover.png", 26, 46)
image butt_exemple_min_idle = im.Scale("/data/images/pc/buttons/patreon_button_idle.png", 86, 46)
image butt_exemple_min_hover = im.Scale("/data/images/pc/buttons/patreon_button_hover.png", 86, 46)

#Email Button
image email_idle = "/data/images/pc/buttons/email_idle.png"
image emailen_hover = "/data/images/pc/buttons/emailen_hover.png"
image emailfr_hover = "/data/images/pc/buttons/emailfr_hover.png"










###SCREENS EFFECT###############################################################
################################################################################
################################################################################

init -2:
    $ flashred = Fade(0.2, 0.0, 0.8, color='#bb2211')
    $ flashred2 = Fade(0.3, 0.2, 0.8, color='#bb2211') # RED
    $ alertred = Fade(0.3, 0.2, 0.3, color='#bb2211')

###IMAGES MOVIES################################################################
################################################################################
################################################################################

init -3:
    image test_menu:
        "backmen1" with dissolve
        3.0
        "backmen3" with dissolve
        3.0
        "backmen4" with dissolve
        3.0
        "backmen5" with dissolve
        3.0
        "backmen6" with dissolve
        3.0
        "backmen7" with dissolve
        3.0
        "backmen8" with dissolve
        3.0
        "backmen9" with dissolve
        3.0
        "backmen10" with dissolve
        3.0
        "backmen11" with dissolve
        3.0
        "backmen12" with dissolve
        3.0
        "backmen13" with dissolve
        3.0
        "backmen14" with dissolve
        3.0
        "backmen16" with dissolve
        3.0
        "backmen17" with dissolve
        3.0
        "backmen18" with dissolve
        3.0
        "backmen19" with dissolve
        3.0
        "backmen20" with dissolve
        3.0
        "backmen21" with dissolve
        3.0
        repeat

    image ubi_rewards:
        "ubi_rew1" with dissolve
        2.5
        "ubi_rew2" with dissolve
        2.5
        "ubi_rew3" with dissolve
        2.5
        "ubi_rew4" with dissolve
        2.5
        "ubi_rew5" with dissolve
        2.5
        "ubi_rew6" with dissolve
        2.5
        "ubi_rew7" with dissolve
        2.5
        "ubi_rew8" with dissolve
        2.5
        "ubi_rew9" with dissolve
        2.5
        "ubi_rew10" with dissolve
        2.5
        "ubi_rew11" with dissolve
        2.5
        "ubi_rew12" with dissolve
        2.5
        "ubi_rew13" with dissolve
        2.5
        "ubi_rew14" with dissolve
        2.5
        "ubi_rew15" with dissolve
        2.5
        "ubi_rew16" with dissolve
        2.5
        "ubi_rew17" with dissolve
        2.5
        "ubi_rew18" with dissolve
        2.5
        "ubi_rew19" with dissolve
        2.5
        "ubi_rew20" with dissolve
        2.5
        "ubi_rew21" with dissolve
        2.5
        "ubi_rew22" with dissolve
        2.5
        "ubi_rew23" with dissolve
        2.5
        repeat

    image sett_ico_hover:
        "sett_hov1"
        1.0
        "sett_hov2"
        1.0
        "sett_hov3"
        1.0
        "sett_hov4"
        1.0
        "sett_hov5"
        1.0
        "sett_hov6"
        1.0
        "sett_hov7"
        1.0
        "sett_hov8"
        1.0
        "sett_hov9"
        1.0
        "sett_hov10"
        1.0
        "sett_hov11"
        1.0
        "sett_hov12"
        1.0
        "sett_hov13"
        1.0
        "sett_hov14"
        1.0
        repeat

    image sett_ico_unhover:
        "sett_hov14"
        1.0
        "sett_hov13"
        1.0
        "sett_hov12"
        1.0
        "sett_hov11"
        1.0
        "sett_hov10"
        1.0
        "sett_hov9"
        1.0
        "sett_hov8"
        1.0
        "sett_hov7"
        1.0
        "sett_hov6"
        1.0
        "sett_hov5"
        1.0
        "sett_hov4"
        1.0
        "sett_hov3"
        1.0
        "sett_hov2"
        1.0
        "sett_hov1"
        1.0

    image load_hover:
        "load_ico"
        1.0
        "load_hov1"
        1.0
        repeat
    image save_hover:
        "save_ico"
        1.0
        "save_hov1"
        1.0
        repeat

    image about_hover:
        "about_ico"
        1.0
        "about_hov1"
        1.0
        repeat
    image help_hover:
        "help_ico"
        1.0
        "help_hov1"
        1.0
        repeat
    image quit_hover:
        "quit_ico"
        1.0
        "quit_hov1"
        1.0
        repeat

    image main_menu_hover:
        "main_menu_ico"
        1.0
        "main_menu_ico_hov1"
        1.0
        repeat

    image quest_bg:
        "#000000"
        alpha 0.7

    image 07alpha_black_bg:
        "#000000"
        alpha 0.7
    image 08alpha_black_bg:
        "#000000"
        alpha 0.8
