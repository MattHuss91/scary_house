################################################################################
## EFFECTS.RPY - Transitions, Transforms, ATL & Special Effects
################################################################################
## This file contains visual effects, transitions, transforms (ATL),
## and special callbacks like dialogue bleeps.
##
## Keep all your custom effects here for easy reference.
################################################################################

################################################################################
## TRANSITIONS
################################################################################
## Custom transitions for scene and sprite changes.
## Use in script like: "with my_transition"

## --- Fades ---
define slow_fade = Fade(1.0, 0.5, 1.0)
define quick_fade = Fade(0.3, 0.0, 0.3)
define fade_to_black = Fade(0.5, 0.5, 0.5)
define long_fade = Fade(2.0, 1.0, 2.0)

## --- Dissolves ---
define slow_dissolve = Dissolve(1.5)
define quick_dissolve = Dissolve(0.3)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

## --- Directional wipes ---
define wipe_right = CropMove(0.5, "wiperight")
define wipe_left = CropMove(0.5, "wipeleft")
define wipe_up = CropMove(0.5, "wipeup")
define wipe_down = CropMove(0.5, "wipedown")

## --- Iris transitions ---
define iris_in = CropMove(0.5, "irisin")
define iris_out = CropMove(0.5, "irisout")

## --- Pixellate ---
define pixellate = Pixellate(0.5, 10)

## --- Blinds ---
define blinds = ImageDissolve("images/ui/blinds.png", 1.0, 8) if renpy.loadable("images/ui/blinds.png") else Dissolve(1.0)


################################################################################
## TRANSFORMS (ATL)
################################################################################
## Position and animate sprites on screen.
## Use in script like: "show eileen happy at left_side"

## --- Basic Positions ---
transform left_side:
    xalign 0.15 yalign 1.0

transform right_side:
    xalign 0.85 yalign 1.0

transform center_stage:
    xalign 0.5 yalign 1.0

transform far_left:
    xalign 0.0 yalign 1.0

transform far_right:
    xalign 1.0 yalign 1.0

## --- Entrance Animations ---
transform enter_left:
    xalign -0.5 yalign 1.0
    easein 0.5 xalign 0.15

transform enter_right:
    xalign 1.5 yalign 1.0
    easein 0.5 xalign 0.85

transform fade_in_center:
    alpha 0.0 xalign 0.5 yalign 1.0
    linear 0.5 alpha 1.0

## --- Exit Animations ---
transform exit_left:
    easeout 0.5 xalign -0.5

transform exit_right:
    easeout 0.5 xalign 1.5

## --- Special Effects ---
transform shake:
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 xoffset 3
    linear 0.05 xoffset -3
    linear 0.05 xoffset 0

transform bounce:
    yoffset 0
    easein 0.15 yoffset -30
    easeout 0.15 yoffset 0

transform pulse:
    alpha 1.0
    linear 0.5 alpha 0.5
    linear 0.5 alpha 1.0
    repeat

transform breathing:
    zoom 1.0
    ease 2.0 zoom 1.02
    ease 2.0 zoom 1.0
    repeat

transform spin:
    rotate 0
    linear 1.0 rotate 360
    repeat

## --- Click-to-Continue Indicator ---
transform ctc:
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.5
    linear 0.5 alpha 1.0
    repeat


################################################################################
## SCREEN SHAKE / CAMERA EFFECTS
################################################################################
## Use with: $ camera_shake()

init python:
    import random

    def camera_shake(duration=0.5, intensity=10):
        """Shake the screen for a given duration and intensity."""
        renpy.with_statement(None)
        start = renpy.time.time()
        while renpy.time.time() - start < duration:
            xoff = random.randint(-intensity, intensity)
            yoff = random.randint(-intensity, intensity)
            renpy.show("_layer master", at_list=[Transform(xoffset=xoff, yoffset=yoff)])
            renpy.pause(0.03, hard=True)
        renpy.show("_layer master", at_list=[Transform(xoffset=0, yoffset=0)])


################################################################################
## DIALOGUE BLEEPS (dmochas dialogue bleeps pack)
################################################################################
## This system plays a bleep sound as text is typed, giving characters
## a distinctive "voice" without full voice acting.
##
## HOW TO USE:
## 1. Pick a bleep sound from audio/bleeps/ (e.g. bleep001.ogg)
## 2. Add a callback to your character in definitions.rpy:
##
##    define e = Character("Eileen", callback=bleep_callback)
##
## 3. Or for a specific bleep per character, make a custom callback:
##
##    init python:
##        def eileen_bleep(event, interact=True, **kwargs):
##            if event == "show":
##                renpy.sound.play("audio/bleeps/bleep005.ogg", channel="blips")
##            elif event == "slow_done" or event == "end":
##                renpy.sound.stop(channel="blips")
##
##    define e = Character("Eileen", callback=eileen_bleep)
##
## The default bleep_callback below uses bleep001. Change the filename
## to pick a different sound.

## Register a dedicated audio channel for bleeps so they don't conflict
## with other sound effects.
init -1 python:
    import random as _random

    _bleep_files = [
        "audio/bleeps/bleep{:03d}.ogg".format(i) for i in range(1, 31)
    ]

    _char_count = [0]

    def bleep_callback(event, interact=True, **kwargs):
        if event == "show":
            _char_count[0] = 0

        elif event == "slow_begin":
            _char_count[0] += 1
            if _char_count[0] % 2 == 0:
                bleep = _random.choice(_bleep_files)
                renpy.sound.play(bleep, channel="blips", loop=False)

        elif event in ("slow_done", "end"):
            renpy.sound.stop(channel="blips")
################################################################################
## IMAGE FILTERS / TINT EFFECTS
################################################################################
## Use these with: show bg room at tint_evening
## Or apply to scenes: scene bg room with dissolve; show layer master at tint_night

transform tint_evening:
    matrixcolor TintMatrix("#ffcc88")

transform tint_night:
    matrixcolor TintMatrix("#6688cc")

transform tint_sepia:
    matrixcolor SepiaMatrix()

transform desaturate:
    matrixcolor SaturationMatrix(0.0)
