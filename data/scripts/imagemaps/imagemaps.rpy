label lbl_Reception_imagemap:
    call screen Reception_imagemap

screen Reception_imagemap():

    imagemap:
        ground "images/reception.jpg"
        hover "images/reception_hover.jpg"
        hotspot (1048, 174, 146, 545) action Jump("milit_base_mychamber") tooltip "C'est ma chambre"
        hotspot (471, 249, 66, 318) action Jump("milit_base_terrain") tooltip "C'est le 'jardin' de la base"
        hotspot (862, 277, 59, 298) action Jump("milit_base_bur_zya") tooltip "C'est le bureau du commandant"
        hotspot (595, 319, 122, 115) action Jump("milit_base_ordinaire") tooltip "C'est l'ordinaire de la base"
        $ tooltip = GetTooltip()
        $ day_number = (day%7)
        $ day_name_values = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche")
        $ dayn = day_name_values[day_number]

        $ dtime_number = (dtime%6)
        $ dtime_name_values = ("Aube", "Matin", "Midi", "Après midi", "Soir", "Nuit")
        $ dtimen = dtime_name_values[dtime_number]
        $ hours_number = (hour%24)
        $ hour_values = ("1h", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "10h", "11h", "12h", "13h", "14h", "15h", "16h", "17h", "18h", "19h", "20h", "21h", "22h", "23h", "24h")
        $ hours_values = hour_values[hours_number]


        if tooltip:
            text _("[tooltip]"):
                xpos .40
        vbox:
            xalign .01 #change this value between 0 and 1 if you want to move it to a different part of the screen horizontally
            yalign .01 #change this value if you want to move it to a different part of the screen vertically

            text "Argent: [money]€ | Jour [day] | [dayn], [dtimen] | [hours_values]" #this will show your money points variable, you can add extra parameters such as font type, size, alignment etc
            text "| [string_fatigue] | [string_faim]"
            textbutton "Journal de Quêtes" text_color "#ffffff" text_hover_color "#f9300c" action ShowMenu(log.screen()) text_size 19

screen tooltip_example():
    vbox:
        textbutton "North":
            action Return("n")
            tooltip "To meet a polar bear."

        textbutton "South":
            action Return("s")
            tooltip "All the way to the tropics."

        textbutton "East":
            action Return("e")
            tooltip "So we can embrace the dawn."

        textbutton "West":
            action Return("w")
            tooltip "Where to go to see the best sunsets."

        $ tooltip = GetTooltip()

        if tooltip:
            text "[tooltip]"

screen mapview():
    imagemap:
        ground "townmap.png"
        hover "townmap-hover.png"
        hotspot (930, 370, 180, 100) clicked Jump("house")
        hotspot (835, 210, 180, 120) clicked Jump("laboratory")
        hotspot (680, 50, 120, 80) clicked Jump("workshop")
        hotspot (525, 240, 120, 120) clicked Jump("coffeeshop")
        hotspot (125, 280, 180, 100) clicked Jump ("university")
        hotspot (95, 570, 205, 205) clicked Jump ("mall")
        hotspot (300, 500, 300, 205) clicked Jump ("park")
        hotspot (300, 60, 150, 260) clicked Jump("downtown")
        hotspot (660, 120, 120, 180) clicked Jump("PPF")

screen House_imagemap():
    showif tooltip_var == "activated":
        imagemap:
            use money_display
            ground "salon"
            hover "salon_hover.jpg"
            hotspot (564, 235, 46, 225) action [SetVariable("garage", "True"), Jump("garage_1")] tooltip "C'est le garage"
            hotspot (506, 238, 52, 213) action [SetVariable("esc", "True"), Jump("etage_1")] tooltip "C'est pour aller à l'étage"
            hotspot (1180, 83, 97, 612) action [SetVariable("toil", "True"), Jump("toilettes")] tooltip "Ce sont les toilettes"
            hotspot (720, 210, 318, 431) action [SetVariable("cuis", "True"), Jump("cuisine")] tooltip "C'est la cuisine"
            $ tooltip = GetTooltip()
    else:
        imagemap:
            use money_display
            ground "salon"
            hover "salon_hover.jpg"
            hotspot (564, 235, 46, 225) action [SetVariable("garage", "True"), Jump("garage_1")]
            hotspot (506, 238, 52, 213) action [SetVariable("esc", "True"), Jump("etage_1")]
            hotspot (1180, 83, 97, 612) action [SetVariable("toil", "True"), Jump("toilettes")]
            hotspot (720, 210, 318, 431) action [SetVariable("cuis", "True"), Jump("cuisine")]
