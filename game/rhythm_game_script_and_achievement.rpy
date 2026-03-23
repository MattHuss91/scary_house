################################################################################
## ACHIEVEMENT - Add to achievements.rpy
################################################################################
##
## 1. Add an icon image at: images/achievements/disco_fever.png
## 2. Paste the define below into achievements.rpy under the achievements section
##

define disco_fever = Achievement(
    name=_("Disco Fever"),
    id="disco_fever",
    description=_("Hit every single note in the ABBA dance scene. All of them."),
    unlocked_image="images/achievements/disco_fever.png",
)


################################################################################
## SCRIPT BLOCK - Replace your parlour scene in script.rpy
################################################################################
##
## Paste this in place of your existing scene palor block.
##

    scene palor with slow_dissolve
    play music audio.abba fadein 1.0
    show layer master at disco_lights
    show silly1 at char_right
    show silly2 at char_left
    show silly3 at char_centre
    with dissolve
    pause

    ## --- Rhythm minigame ---
    stop music fadeout 0.3
    show layer master at normal

    label rhythm_retry:

    $ rhythm_result = run_rhythm_game()

    ## --- Retry screen if score is very low ---
    if rhythm_result["percent"] < 30:
        menu:
            "You scored [rhythm_result[\"percent\"]]%%. That was... something. Try again?"
            "Try again!":
                jump rhythm_retry
            "Move on...":
                pass

    ## --- Achievement if perfect ---
    if rhythm_result["perfect"]:
        $ disco_fever.grant()

    ## --- Resume scene ---
    play music audio.abba fadein 0.5
    show layer master at disco_lights

    hide silly2 with dissolve
    show jake at char_right
    with dissolve
    jake "I hate ABBA!"

    play sound audio.record_scratch
    stop music fadeout 0.5
    show layer master at normal
    silly1 "Oh fine! We'll go then!"
    hide silly1 with dissolve
    hide silly3 with dissolve
