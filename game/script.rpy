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
################################################################################
## Scene 1
################################################################################

    scene test with slow_dissolve 
    play audio audio.rain fadein 2.0
    narrator "The Scary House"
    narrator "It's Frightening"