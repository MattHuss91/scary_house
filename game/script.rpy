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

    ## -------------------------------------------------------------------------
    ## GAME SETUP - runs once at game start
    ## -------------------------------------------------------------------------
    ## Set the default window mode to auto (hides textbox during transitions)
    window auto

    ## -------------------------------------------------------------------------
    ## CHAPTER 1 - Replace this with your story
    ## -------------------------------------------------------------------------

    ## Show a background
    # scene bg room
    ## with a transition
    # with fade

    ## Show a character sprite
    # show eileen happy at center
    # with dissolve

    ## Dialogue - use character variables defined in definitions.rpy
    # narrator "This is narration text with no character name."
    # protagonist "This is dialogue from the protagonist."
    # e "This is dialogue from a character named Eileen."

    ## --- Example: Choices ---
    # menu:
    #     "What do you want to do?"
    #     "Choice A":
    #         $ choice_made = "a"
    #         e "You picked choice A!"
    #     "Choice B":
    #         $ choice_made = "b"
    #         e "You picked choice B!"

    ## --- Example: Jumping to other labels ---
    # jump chapter2

    ## --- Example: Playing music/sound ---
    # play music "audio/music/main_theme.ogg" fadein 1.0
    # play sound "audio/sfx/door_open.ogg"

    ## --- Example: Granting an achievement ---
    # $ my_achievement.grant()

    ## Placeholder - remove this when you add your story
    "Welcome to your new Ren'Py project!"
    "Edit script.rpy to start writing your story."
    "Check definitions.rpy for characters, effects.rpy for transitions."

    return

## -------------------------------------------------------------------------
## ADDITIONAL LABELS - Add your story scenes below
## -------------------------------------------------------------------------
## Organize your game into labels for each chapter, scene, or route.
## Example:
##
## label chapter2:
##     scene bg park
##     with fade
##     e "Welcome to chapter 2!"
##     return
