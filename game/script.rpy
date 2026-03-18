################################################################################
## SCRIPT.RPY - Main Game Script
################################################################################
## This is the main script file where your story and gameplay logic go.
## For a new game, start writing your story in the "start" label below.
##
## You can split your script across multiple .rpy files if it gets long.
## Ren'Py will automatically combine them. Use labels to organize scenes:
##   label chapter1:
##   label chapter2:
##   etc.
################################################################################

## The game starts here.
label start:
    $ preferences.text_cps = 40

#################################################################################
## Title Screen
#################################################################################
    $ renpy.music.set_volume(1.0, channel="voice")
    play sound audio.rain loop
    play music audio.credit_theme fadein 1.0 loop
    play movie "video/opening_pan.webm"
    scene forest_night
    centered "{size=180}{color=#FF0000}{font=fonts/bloody.ttf}{b}SCARY HOUSE{/b}\n{size=150}IT'S FRIGHTENING{/size}{/font}{/color}{/size}"

#################################################################################
## Opening Credits Scroll
#################################################################################
    stop movie 
    stop sound fadeout 0.5
    show screen opening_credits
    $ renpy.pause(42.0)
    hide screen opening_credits
    stop music fadeout 0.5

#################################################################################
## Scene 1
################################################################################

    scene forest_night with slow_dissolve 
    play audio audio.rain fadein 0.5 loop
    show narrator at char_centre
    with dissolve
    narrator "Oh hello! I didn't hear you approach. You know why you're here, I am going to tell you a tale of strange consequences."
    narrator "It all begins here, on an unrealistically dark and stormy night, when four goons found thier landrover had broken down in the middle of the dark"
    narrator "forest where silly people jump out on you and say stupid stuff..."

    scene black with slow_dissolve
    show bg forest scroll_stop
    show la_drover at drover_enter_stop
    pause

    show silly1 at char_centre
    with dissolve
    silly1 "Is your name Terry?"       