## Main Menu screen ############################################################

## Button style — bloody font, bare text (no box), red hover glow.
style main_menu_button:
    background None
    hover_background None
    ypadding 6

style main_menu_button_text:
    font "fonts/bloody.TTF"
    size 54
    color "#cc1a00"
    outlines [(2, "#000000", 0, 0)]

style main_menu_button_text_hover:
    color "#ff4400"
    outlines [(2, "#330000", 0, 0)]


screen main_menu():
    tag menu

    ## Full-screen background
    add "images/ui/menu.png"
   

    ## Dark overlay — keeps text legible over any image
    add Solid("#00000077")


    ## Navigation — left side, below the title
    vbox:
        xpos 80
        yalign 0.65
        spacing 4

        textbutton _("Start") action Start() style "main_menu_button"

        textbutton _("Load") action ShowMenu("load") style "main_menu_button"

        textbutton _("Achievements") action ShowMenu("achievement_gallery") style "main_menu_button"

        textbutton _("Preferences") action ShowMenu("preferences") style "main_menu_button"

        textbutton _("About") action ShowMenu("about") style "main_menu_button"

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("Help") action ShowMenu("help") style "main_menu_button"

        if renpy.variant("pc"):
            textbutton _("Quit") action Quit(confirm=not main_menu) style "main_menu_button"
