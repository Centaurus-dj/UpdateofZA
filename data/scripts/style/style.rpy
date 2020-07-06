
## Styles ######################################################################
## Here is all the styles defined for and by Ren'py game
## Including the styles I created
################################################################################
init -2:
    style centered:
        xpos .25
        ypos .25

    style unkstyle:
        size 60
        xpos .0
        ypos .1

    style Preststyle:
        size 40
        xpos .7
        ypos .5

    style Gametitle:
        color "#f9300c"
        size 70
        xpos .3
        ypos .3

    style WarnVersText:
        size 50
        xpos .0
        ypos .1
        color "#F6080c"

    style say_named:
        background Image("data/gui/textbox_name.png")

    style say_noname:
        background Image("data/gui/textbox_noname.png")

    style mychoicevbox:
        yalign 0.6
        background "devlog_bg"

    style Res_icons:
        xalign 1.01
        yalign .3
        ymaximum 75
        xmaximum 75

    style Res_buttons:
        xalign 1.0
        yalign .3


    style BigNextButton:
        xpos 3.0
        ypos 1.0
        size 30
        spacing 20

    style langlbl:
        yalign .2
        xalign .5
        color "#ffffff"
        size 50

    style choice_button_text:
        hover_color "#f9300c"

    style pos is choice_button_text:
        color "#ffffff"
        hover_color "#1bef33"
        insensitive_color "#060"
        background "07alpha_black_bg"

    style neg is choice_button_text:
        color "#ffffff"
        hover_color "#ef2d12"

style sexual:
    hover_color "#ed51e2"

style none_borders:
    background None

style Startabouttext:
    size 60
    xpos .1
    ypos .2
    color "#F6080c"
style startaboutstyle:
    color "#ffffff"
    hover_color "#f80e0e"
    size 70

style startaboutvbox:
    xpos .1
    ypos .1


style devhbox:
    xalign .5
    yalign 0.0

style Devlogtitle:
    size 40

style devcls_btn:
    xpos 4.0

style devcls_btntxt:
    hover_color "#f9300c"

style Devlog:
    background "devlog_bg"
    xalign .5
    xmaximum 340
    ymaximum 360

style devleft:
    xalign 0.0
    yalign 0.5
style devright:
    xalign 1.0
    yalign 0.2
    background "07alpha_black_bg"

style Devtext:
    xalign .0
    yalign .0
    size 18

transform fader:
  on show:
    alpha 0.0
    easein 0.15 alpha 1.0

  on hide:
    easeout 0.15 alpha 0.0

style reshist_style_place:
    xpos .1
    ypos .1

style reshist_style_size:
    size 25

style tip:
    xpos .8
    ypos .8
    size 12
style raidercrusader:
    font "data/fonts/raidercrusaderhalf.ttf"
    hover_color "#f80e0e"
    selected_color "#f9300c"
    selected_hover_color "#cc0000"
    size 40

style thunderstrike_lbl:
    font "data/fonts/thunderstrikeitalic.ttf"
    color "#b00101"
    size 20

style thunderstrike:
    font "data/fonts/thunderstrike.ttf"
    hover_color "#f80e0e"
    selected_color "#b00101"
    selected_hover_color "#f80e0e"
    insensitive_color "#260101"
    size 20

style thunderstrike_spebtn:
    font "data/fonts/thunderstrike.ttf"
    hover_color "#f80e0e"
    selected_color "#ffffff"
    selected_hover_color "#f80e0e"
    insensitive_color "#260101"
    size 20

style thunderstrike_txt:
    font "data/fonts/thunderstrike.ttf"
    color "#ffffff"
    size 20

style main_menu_version_txt:
    font "data/fonts/KeeponTruckin.ttf"
    color "#b00101"
    yoffset 22
    xoffset 10
    size 34

style res_btn:
    xalign 1.0
    yalign 1.0
    yoffset 22
    xoffset 10
    size 34

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("data/gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("data/gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("data/gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("data/gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("data/gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("data/gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("data/gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("data/gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("data/gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "data/gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("data/gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "data/gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("data/gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


if inputwindow == True:
    style window:
        xalign 0.5
        xfill True
        yalign gui.textbox_yalign
        ysize gui.textbox_height

        background None

else:
    style window:
        xalign 0.5
        xfill True
        yalign gui.textbox_yalign
        ysize gui.textbox_height

        background Image("data/gui/textbox_noname.png")

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background None
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

style input_prompt is default

style input_prompt:
    xpos .0
    ypos .0
    properties gui.text_properties("input_prompt")

style input:
    yalign .2

style input_hbox:
    xalign .15
    yalign .2

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill False

    background "data/images/pc/background/main_menu.jpg"
        imagebutton:
            idle "data/images/pc/imgbttns/btns.png"
            hover "data/images/pc/imgbttns/btns_hover.png"
            action OpenURL()

style my_main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_vbox:
    xalign .0
    xmaximum 1200
    yalign .8
    yoffset -30
    font "raidercrusader"
    size 30

style game_title:
    xalign 5.0
    xoffset 10
    xmaximum 1200
    yalign 2.0
    yoffset -630
    color "#0ddb1e"
    font "data/fonts/KeeponTruckin.ttf"
    size 60

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar
style game_about_frame is empty
style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background "data/gui/overlay/confirm.png"

style game_menu_outer_frame2:
    bottom_padding 45
    top_padding 180
    background "data/images/pc/background/menu_1.jpg"

style game_menu_outer_frame3:
    bottom_padding 45
    top_padding 180
    background "data/images/pc/background/menu_3.jpg"

style game_about_frame:
    bottom_padding 45
    top_padding 180
    background "data/images/pc/background/menu_5.jpg"

style game_menu_plus_1_frame:
    bottom_padding 45
    top_padding 180
    background "data/images/pc/background/menu_3_modif.jpg"

style game_menu_plus_2_frame:
    bottom_padding 45
    top_padding 180
    background "data/images/pc/background/menu_3_modif_about.jpg"

style game_menu_plus_3_frame:
    bottom_padding 45
    top_padding 180
    background "data/images/pc/background/menu_5_modif.jpg"

style game_menu_plus_4_frame:
    bottom_padding 45
    top_padding 180
    background "data/images/pc/background/menu_6_modif.jpg"

style game_menu_outer_frame5:
    bottom_padding 45
    top_padding 180
    background "data/images/pc/background/menu_6.jpg"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "data/gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "data/gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "data/gui/confirm_frame.png", "data/gui/frame_cust.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("data/gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("data/gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

style pref_vbox:
    variant "medium"
    xsize 675

style window:
    variant "small"
    background "data/gui/phone/textbox_modif.png"

style radio_button:
    variant "small"
    foreground "data/gui/phone/button/check_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "data/gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "data/gui/phone/nvl.png"

style about_frame:
    variant "small"
    background "data/images/pc/background/menu_6.jpg"

style game_menu_about_frame:
    variant "small"
    background "data/images/pc/background/menu_3_modif.jpg"
style game_menu_navigation_about_frame:
    variant "small"
    xsize 510

style game_menu_content_about_frame:
    variant "small"
    top_margin 0

style main_menu_frame:
    variant "small"
    background "data/images/pc/background/main_menu.jpg"

style game_menu_outer_frame:
    variant "small"
    background "data/images/pc/background/menu_4_modif.jpg"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("data/gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("data/gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("data/gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("data/gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("data/gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("data/gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("data/gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("data/gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("data/gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "data/gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("data/gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "data/gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900
