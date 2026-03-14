################################################################################
## DEFINITIONS.RPY - Characters, Images, Variables & Configuration
################################################################################
## This file is for defining all your game's characters, default variables,
## image declarations, and audio channels.
##
## Keep all your definitions here so they're easy to find and update.
################################################################################

################################################################################
## CHARACTERS
################################################################################
## Define your characters here. The color argument sets the name color.
## You can also set voice/text properties per character.
##
## Character properties you can use:
##   color          - Name color (hex like "#c8ffc8" or color name)
##   who_color      - Same as color
##   what_color     - Dialogue text color
##   image          - Side image tag for this character
##   voice_tag      - Tag for voice auto-play (used with auto voice)
##   callback       - Called when dialogue is shown (used for bleeps)
##   kind           - Base character to inherit from (e.g. nvl_narrator)
##
## See effects.rpy for the bleep_callback if you want typing sounds.

## --- Narrator (no name shown) ---
define narrator = Character(ctc="ctc", ctc_position="fixed")

## --- Protagonist (the player character) ---
define protagonist = Character(
    _("Me"),
    color="#c8ffc8",
)

## --- Example Character ---
## Uncomment and modify to create your characters:
# define e = Character(
#     _("Eileen"),
#     color="#c8c8ff",
#     image="eileen",             ## For side images: "eileen" tag
#     ## callback=bleep_callback, ## Uncomment for typing bleeps
# )

## --- NVL Mode Narrator (for novel-style text) ---
## Uncomment if you want NVL mode support:
# define nvl_narrator = Character(None, kind=nvl)


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
