################################################################################
## CHARACTERS
################################################################################
##
## See effects.rpy for the bleep_callback if you want typing sounds.

## --- Narrator (no name shown) ---
define the_narrator = Character(name="Narrator", what_italic=True, what_color="#c0c0c0", what_outlines=[(2, "#000000")], callback=bleep_callback)
define vo = Character(None, what_italic=True, what_color="#ffeded", what_outlines=[(2, "#000000")], callback=bleep_callback)

## --- characters
define jake = Character(name="Jake", color="#4A6FA5", who_outlines=[(2, "#000000")],callback=bleep_callback)
define jon = Character(name="Jon", color="#3b61fa", who_outlines=[(2, "#000000")], callback=bleep_callback)
define mike = Character(name="Mike", color="#eaff00", who_outlines=[(2, "#000000")], callback=bleep_callback)
define tom = Character(name="Tom", color="#00ff1a", who_outlines=[(2, "#000000")], callback=bleep_callback)
define butler = Character(name="The Butler", color="#0eeedf", who_outlines=[(2, "#000000")], callback=bleep_callback)
define count = Character(name="Count Vincent", color="#ff0000", who_outlines=[(2, "#000000")], callback=bleep_callback)
define silly1 = Character(name="Silly Person 1", color="#ee00ff", who_outlines=[(2, "#000000")], callback=bleep_callback)
define silly2 = Character(name="Silly Person 2", color="#f377fc", who_outlines=[(2, "#000000")], callback=bleep_callback)
define silly3 = Character(name="Silly Person 3", color="#ee00ff", who_outlines=[(2, "#000000")], callback=bleep_callback)
define bat = Character(name="The Bat", color="#080009", who_outlines=[(2, "#000000")], callback=bleep_callback)
define morticus = Character(name="Morticus", color="#8233c7", who_outlines=[(2, "#000000")], callback=bleep_callback)
define prompt = Character(name="Stage Hand", color="#c87076", who_outlines=[(2, "#000000")], callback=bleep_callback)
define aud = Character(name="Audience Member", color="#ee00ff", who_outlines=[(2, "#000000")], callback=bleep_callback)
define shelly = Character(name="Shelly", color="#426f1c", who_outlines=[(2, "#000000")], callback=bleep_callback)
define posh = Character(name="Posh Person", color="#ee00ff", who_outlines=[(2, "#000000")], callback=bleep_callback)
define steward = Character(name="Steward", color="#84c2e6", who_outlines=[(2, "#000000")], callback=bleep_callback)

################################################################################
## Define Audio
################################################################################

define audio.rain = "audio/sfx/rain.ogg"
define audio.credit_theme = "audio/music/credit_theme.mp3"
define audio.horn = "audio/sfx/horn.ogg"
define audio.window ="audio/sfx/window.ogg"
define audio.car = "audio/sfx/break.ogg"

################################################################################
## DEFAULT VARIABLES
################################################################################
## Use `default` for variables that should be saved with the game.
## Use `define` for constants that never change during gameplay.

## --- Player/Story Variables ---
default player_name = "Player"
default affection = 0
default route = None

## --- Flags/Tracking ---
## Track which scenes the player has seen, choices made, etc.
default seen_intro = False

## --- Example: Chapter tracking ---
# default current_chapter = 1
# default endings_seen = set()


################################################################################
## IMAGE DECLARATIONS
################################################################################
## Ren'Py auto-detects images in the images/ folder, but you can also
## declare them explicitly here for transforms, composites, or layered images.
##
## Explicit declarations:
## image bg room = "images/bg/room.png"
## image eileen happy = "images/characters/eileen_happy.png"
##
## Composite/Layered images:
## image eileen = LayeredImage(...)
##
## For most projects, just drop your images in the right folders:
##   images/bg/          - Backgrounds
##   images/characters/  - Character sprites
##   images/cg/          - CG / event images
##   images/ui/          - UI elements
##   images/achievements/ - Achievement icons

## --- Locked Achievement Image (used by achievements plugin) ---
## Replace with your own locked achievement icon
image locked_achievement = Text("?", size=80, color="#888")

####Backgrounds#####

image test = "images/bg/test.jpg"
image forest_night = "images/bg/forest_night.png"
image bg forest scroll_stop:
    "images/bg/forest_night_scroll.png"
    subpixel True
    xanchor 0 xpos 0
    linear 6.0 xanchor 0 xpos -1920
image cinema = "images/bg/cinema.png"
image scary_door = "images/bg/scary_door.png"

#####Characters#####
image the_narrator = im.Scale("images/characters/narrator.png", 1000, 1400)
image silly1 ="images/characters/silly1.png"
image tom = "images/characters/tom.png"
image jon = "images/characters/jon.png"
image jake = "images/characters/jake.png"
image mike = "images/characters/jon.png"
image butler = "images/characters/butler.png"
image count = "images/characters/count.png"
image silly2 = "images/characters/silly2.png"
image silly 3 = "images/characters/silly3.png"
image bat = "images/characters/bat.png"
image morticus = "images/characters/morticus.png"
image prompt = "images/characters/stagehand.png"
image aud = "images/characters/aud.png"
image shelly = "images/characters/shelly.png"
image posh = "images/characters/posh.png"
image steward = "images/characters/steward.png"

######Objects####
image la_drover ="images/cg/la_drover.png"

###############################################################################
## Define Opening Credits
###############################################################################

transform scroll_credits:
    ypos 1080
    linear 40.0 ypos -6000

screen opening_credits():
    frame:
        xfill True
        yfill True
        background "#000000"

        vbox:
            xalign 0.5
            spacing 60
            at scroll_credits

            ## --- Jake ---
            vbox:
                xalign 0.5
                spacing 20
                text "{size=40}{color=#8B0000}{font=fonts/bloody.ttf}The Rather Terrifying{/font}{/color}{/size}":
                    xalign 0.5
                add Solid("#8B0000") size (200, 300)
                text "{size=50}{color=#FF0000}{font=fonts/bloody.ttf}Jake Saunders{/font}{/color}{/size}":
                    xalign 0.5

            null height 80

            ## --- Jon ---
            vbox:
                xalign 0.5
                spacing 20
                text "{size=40}{color=#8B0000}{font=fonts/bloody.ttf}They say the bogeyman looks under his bed for{/font}{/color}{/size}":
                    xalign 0.5
                add Solid("#8B0000") size (200, 300)
                text "{size=50}{color=#FF0000}{font=fonts/bloody.ttf}Jon Bowen{/font}{/color}{/size}":
                    xalign 0.5

            null height 80

            ## --- Mike ---
            vbox:
                xalign 0.5
                spacing 20
                text "{size=40}{color=#8B0000}{font=fonts/bloody.ttf}He'll kill you before you know he's there{/font}{/color}{/size}":
                    xalign 0.5
                add Solid("#8B0000") size (200, 300)
                text "{size=50}{color=#FF0000}{font=fonts/bloody.ttf}Mike Rhodes{/font}{/color}{/size}":
                    xalign 0.5

            null height 80

            ## --- Tom Broughton ---
            vbox:
                xalign 0.5
                spacing 20
                text "{size=40}{color=#8B0000}{font=fonts/bloody.ttf}He's really rather mortifying{/font}{/color}{/size}":
                    xalign 0.5
                add Solid("#8B0000") size (200, 300)
                text "{size=50}{color=#FF0000}{font=fonts/bloody.ttf}Tom Broughton{/font}{/color}{/size}":
                    xalign 0.5

            null height 80

            ## --- Tom Rich ---
            vbox:
                xalign 0.5
                spacing 20
                text "{size=40}{color=#8B0000}{font=fonts/bloody.ttf}You'll personally wet yourself{/font}{/color}{/size}":
                    xalign 0.5
                add Solid("#8B0000") size (200, 300)
                text "{size=50}{color=#FF0000}{font=fonts/bloody.ttf}Tom Rich as The Butler{/font}{/color}{/size}":
                    xalign 0.5

            null height 80

            ## --- Matt Husselbury ---
            vbox:
                xalign 0.5
                spacing 20
                text "{size=40}{color=#8B0000}{font=fonts/bloody.ttf}He frightens little boys{/font}{/color}{/size}":
                    xalign 0.5
                add Solid("#8B0000") size (200, 300)
                text "{size=50}{color=#FF0000}{font=fonts/bloody.ttf}Matt Husselbury as Count Vincent of Stoke-on-Trent{/font}{/color}{/size}":
                    xalign 0.5

            null height 80

            ## --- Matt Schofield ---
            vbox:
                xalign 0.5
                spacing 20
                text "{size=40}{color=#8B0000}{font=fonts/bloody.ttf}He doesn't always wipe his feet{/font}{/color}{/size}":
                    xalign 0.5
                add Solid("#8B0000") size (200, 300)
                text "{size=50}{color=#FF0000}{font=fonts/bloody.ttf}Matt Schofield as The Narrator{/font}{/color}{/size}":
                    xalign 0.5

            null height 80

            ## --- Chris Stevens ---
            vbox:
                xalign 0.5
                spacing 20
                text "{size=40}{color=#8B0000}{font=fonts/bloody.ttf}He isn't in this film{/font}{/color}{/size}":
                    xalign 0.5
                add Solid("#8B0000") size (200, 300)
                text "{size=50}{color=#FF0000}{font=fonts/bloody.ttf}Chris Stevens{/font}{/color}{/size}":
                    xalign 0.5

            null height 120

            ## --- Technicolor gag ---
            vbox:
                xalign 0.5
                spacing 20
                text "{size=60}{color=#FF0000}{font=fonts/bloody.ttf}Filmed in glorious Technicolor*{/font}{/color}{/size}":
                    xalign 0.5
                text "{size=25}{color=#FF0000}*Combination of the word \"Techni\" and the American variant on \"colour\"{/color}{/size}":
                    xalign 0.5
                text "{size=18}{color=#FF0000}Ice cream will be available at the interval - today your stewardess is Shelly{/color}{/size}":
                    xalign 0.5

            null height 1080

###############################################################################
## Transforms - Character positions
###############################################################################

transform char_left:
    xalign 0.15
    yalign 1.0
    zoom 0.8

transform char_centre:
    xalign 0.5
    yalign 1.0
    zoom 0.8

transform char_right:
    xalign 0.85
    yalign 1.0
    zoom 0.8

transform char_fade_in:
    alpha 0.0
    linear 0.3 alpha 1.0

transform char_fade_out:
    alpha 1.0
    linear 0.3 alpha 0.0
