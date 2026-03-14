################################################################################
##
## Achievements for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com) v1.5
##
################################################################################
## This file contains code for an achievement system in Ren'Py. It is designed
## as a wrapper to the built-in achievement system, so it hooks into the
## Steam backend as well if you set up your achievement IDs the same as in
## the Steam backend.
##
## Credit: Feniks @ feniksdev.com
################################################################################

################################################################################
## CONFIGURATION
################################################################################
define myconfig.INGAME_POPUP_WITH_STEAM = True
define myconfig.ACHIEVEMENT_HIDE_TIME = 1.0
define myconfig.SHOW_ACHIEVEMENT_POPUPS = True
define myconfig.ACHIEVEMENT_SOUND = None # "audio/sfx/achievement.ogg"
define myconfig.ACHIEVEMENT_CHANNEL = "audio"
define myconfig.HIDDEN_ACHIEVEMENT_NAME = _("???{#hidden_achievement_name}")
define myconfig.HIDDEN_ACHIEVEMENT_DESCRIPTION = _("???{#hidden_achievement_description}")

## Achievement callbacks - add LinkedAchievement entries here if you want
## achievements that auto-unlock when others are earned.
## Example: LinkedAchievement(platinum_id='all') unlocks after ALL achievements.
## Example: LinkedAchievement(combo_id=['ach1', 'ach2']) unlocks after ach1+ach2.
define myconfig.ACHIEVEMENT_CALLBACK = [
    ## LinkedAchievement(platinum_achievement='all'),
]

define achievement.steam_position = None

################################################################################
## DEFINING ACHIEVEMENTS
################################################################################
## The locked_achievement image is defined in definitions.rpy.
## Place your achievement icons in images/achievements/.
##
## HOW TO ADD AN ACHIEVEMENT:
## 1. Add an icon image to images/achievements/
## 2. Define the achievement below using this template:
##
## define my_achievement = Achievement(
##     name=_("Achievement Name"),
##     id="my_achievement",
##     description=_("Description of what the player did."),
##     unlocked_image="images/achievements/my_icon.png",
##     ## Optional parameters:
##     # locked_image="locked_achievement",  ## Custom locked image
##     # hide_name=True,                     ## Hide name until unlocked
##     # hide_description=True,              ## Hide description until unlocked
##     # stat_max=10,                        ## For progress-based achievements
##     # show_progress_bar=True,             ## Show progress bar in gallery
## )
##
## 3. Grant it in script.rpy with: $ my_achievement.grant()
## 4. For progress: $ my_achievement.add_progress(1)
## 5. For set-based progress: $ my_achievement.add_set_progress("unique_value")

## --- YOUR ACHIEVEMENTS GO HERE ---
## Uncomment and modify:
# define first_achievement = Achievement(
#     name=_("Getting Started"),
#     id="first_achievement",
#     description=_("You started the game!"),
#     unlocked_image="images/achievements/started.png",
# )

################################################################################
## SCREENS
################################################################################
## POPUP SCREEN
################################################################################
screen achievement_popup(a, tag, num):

    zorder 190

    default achievement_yoffset = num*170

    frame:
        style_prefix 'achieve_popup'
        at achievement_popout()
        yoffset achievement_yoffset
        has hbox
        add a.unlocked_image:
            fit "contain" ysize 95 align (0.5, 0.5)
        vbox:
            text a.name
            text a.description size 25

    timer 5.0 action [Hide("achievement_popup"),
            Show('finish_animating_achievement', num=num, _tag=tag+"1")]

style achieve_popup_frame:
    is confirm_frame
    align (0.0, 0.0)
style achieve_popup_hbox:
    spacing 10
style achieve_popup_vbox:
    spacing 2
style achieve_popup_text:
    is text


transform achievement_popout():
    on show:
        xpos 0.0 xanchor 1.0
        easein_back 1.0 xpos 0.0 xanchor 0.0
    on hide, replaced:
        easeout_back myconfig.ACHIEVEMENT_HIDE_TIME xpos 0.0 xanchor 1.0

################################################################################
## ACHIEVEMENT GALLERY SCREEN
################################################################################
## Add a button to access this screen from your main menu or pause menu:
##   textbutton _("Achievements") action ShowMenu("achievement_gallery")
screen achievement_gallery():
    tag menu

    add VBox(Transform("#292835", ysize=110), "#21212db2")

    textbutton _("Return") action Return() align (1.0, 1.0)
    viewport:
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"
        xalign 0.5 yalign 0.5
        xsize int(config.screen_width*0.6) ysize int(config.screen_height*0.7)
        xfill False yfill False
        has vbox
        spacing 20

        for a in Achievement.all_achievements:
            button:
                style_prefix 'achievement'
                if config.developer:
                    action a.Toggle()
                else:
                    action NullAction()
                has hbox
                if a.idle_img:
                    fixed:
                        align (0.5, 0.5)
                        xysize (155, 155)
                        add a.idle_img fit "scale-down" ysize 155 align (0.5, 0.5)
                else:
                    null width -10
                vbox:
                    label a.name
                    text a.description
                    if a.has():
                        text a.timestamp size 22
                    elif a.stat_max and a.show_progress_bar:
                        fixed:
                            fit_first True
                            bar value a.stat_progress range a.stat_max:
                                style 'achievement_bar'
                            text "[a.stat_progress]/[a.stat_max]":
                                style_suffix "progress_text"

        null height 100

    label __("Achievements: ") + "{earned}/{total}".format(
            earned=Achievement.num_earned(), total=Achievement.num_total()):
        text_size 52 xalign 0.5 text_color "#f93c3e" top_padding 15

style achievement_button:
    size_group 'achievement'
    xmaximum 750
style achievement_label:
    padding (2, 2)
style achievement_label_text:
    size 40 color "#ff8335"
style achievement_hbox:
    spacing 10
style achievement_vbox:
    spacing 2
style achievement_bar:
    xmaximum 600
