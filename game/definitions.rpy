################################################################################
## CHARACTERS
################################################################################
##
## See effects.rpy for the bleep_callback if you want typing sounds.

## --- Narrator (no name shown) ---
define narrator = Character(None, what_italic=True, what_color="#c0c0c0", what_outlines=[(2, "#000000")], callback=bleep_callback)

## --- characters
define jake = Character(name="Jake", color="#4A6FA5", who_outlines=[(2, "#000000")],callback=bleep_callback)
define jon = Character(name="Jon", color= "#3b61fa", who_outlines=(2,"#000000"), callback=bleep_callback)
define mike = Character(name="Mike", color="#eaff00", who_outlines=(2,"#000000"), callback=bleep_callback)
define tom = Character(name="Tom", color="#00ff1a", who_outlines=(2,"#000000"), callback=bleep_callback)
define butler = Character(name="The Butler", color="#0eeedf", who_outlines=(2,"#000000"), callback=bleep_callback)
define count = Character(name="Count Vincent", color="#ff0000", who_outlines=(2,"#000000"), callback=bleep_callback)
define silly1 = Character(name="Silly Person 1", color="#ee00ff", who_outlines=(2,"#000000"), callback=bleep_callback)
define silly2 = Character(name="Silly Person 2", color="#f377fc", who_outlines=(2,"#000000"), callback=bleep_callback)
define silly3 = Character(name="Silly Person 3", color="#ee00ff", who_outlines=(2,"#000000"), callback=bleep_callback)
define bat = Character(name="The Bat", color="#080009", who_outlines=(2,"#000000"), callback=bleep_callback)
define morticus = Character(name="Morticus", color="#8233c7", who_outlines=(2,"#000000"), callback=bleep_callback)
define prompt = Character(name="Stage Hand", color="#c87076", who_outlines=(2,"#000000"), callback=bleep_callback)
define aud = Character(name="Audience Member", color="#ee00ff", who_outlines=(2,"#000000"), callback=bleep_callback)
define shelly = Character(name="Shelly", color="#426f1c", who_outlines=(2,"#000000"), callback=bleep_callback)
define posh = Character(name="Posh Person", color="#ee00ff", who_outlines=(2,"#000000"), callback=bleep_callback)
define steward = Character(name="Steward", color="#84c2e6", who_outlines=(2,"#000000"), callback=bleep_callback)

################################################################################
## Define Audio
################################################################################

define audio.rain = "audio/sfx/rain.wav"

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

image test = "images/bg/test.jpg"


################################################################################
## AUDIO DEFINITIONS
################################################################################
## Define audio files for easy reference in your script.
## You can then use: play music main_theme
##
## Folder structure:
##   audio/music/   - Background music
##   audio/sfx/     - Sound effects
##   audio/voice/   - Voice lines
##   audio/bleeps/  - Dialogue bleep sounds

## --- Music ---
# define audio.main_theme = "audio/music/main_theme.ogg"
# define audio.battle_theme = "audio/music/battle.ogg"

## --- Sound Effects ---
# define audio.click = "audio/sfx/click.ogg"
# define audio.door = "audio/sfx/door_open.ogg"

## --- Bleep Sounds (from dmochas dialogue bleeps pack) ---
## These are pre-loaded from audio/bleeps/. See effects.rpy for usage.
