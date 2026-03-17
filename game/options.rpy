define config.name = _("Scary House")
define build.name = "Scary.House.v1"

## Save directory ##############################################################
define config.has_autosave = True
define config.autosave_slots = 1

define config.save_directory = "scary_house-1690000000"

define config.window_icon = None


## The version of the game.

define config.version = "0.0.1"


## Sounds and music ############################################################

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"
# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################

## Entering or exiting the game menu.
define config.enter_transition = dissolve
define config.exit_transition = dissolve

## Between screens of the game menu.
define config.intra_transition = dissolve

## A transition that is used after a game has been loaded.
define config.after_load_transition = None

## Used when entering the main menu after the game has ended.
define config.end_game_transition = None

## Window management ###########################################################

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################
default preferences.text_cps = 0
default preferences.afm_time = 15

## Icon ########################################################################
define config.window_icon = "gui/window_icon.png"

## Custom Options ##############################################################
##
define config.allow_underfull_grids = True

## Default volume % for the various volume sliders

define config.default_music_volume = 0.5
define config.default_sfx_volume = 0.5
define config.default_voice_volume = 0.5
define config.preserve_volume_when_muted = False

## The number of auto save slots Ren'Py will save to before it
## starts overwriting the first one
define config.autosave_slots = 6
## Same thing, but for quick save
define config.quicksave_slots = 6

## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.psd', None)
    build.classify('game/cache/**', None)
    ## NOTE: This excludes markdown and txt files. If you use these formats
    ## for README or instructions, you may want to remove these lines.
    build.classify('**.txt', None)
    build.classify('**.md', None)

    ## To archive files, classify them as 'archive'.

    build.classify("game/**.rpy", "archive")
    build.classify("game/**.rpym", "archive")

    build.classify("game/**.webp", "archive")
    build.classify("game/**.webm", "archive")
    build.classify("game/**.mp4", "archive")
    build.classify("game/**.png", "archive")
    build.classify("game/**.jpg", "archive")
    build.classify("game/**.ttf", "archive")
    build.classify("game/**.otf", "archive")
    build.classify("game/**.mp3", "archive")
    build.classify("game/**.wav", "archive")
    build.classify("game/**.ogg", "archive")
    build.classify("game/**.opus", "archive")
    build.classify("game/**.rpyc", "archive")
    build.classify("game/**.rpymc", "archive")

## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
