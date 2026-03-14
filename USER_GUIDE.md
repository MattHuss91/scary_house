# Ren'Py Project Skeleton - User Guide

This is a reusable skeleton template for Ren'Py visual novel projects. Fork this repo for each new game you make.

## Quick Start

1. **Fork this repo** for your new game project
2. **Open the `game/` folder** in the Ren'Py launcher (point it at the project root)
3. **Edit `game/options.rpy`** - set your game name, build name, and save directory (the three values at the top)
4. **Edit `game/definitions.rpy`** - add your characters
5. **Edit `game/script.rpy`** - write your story
6. **Drop your assets** into the appropriate folders (see below)
7. Launch and test!

---

## Project Structure

```
game/
├── script.rpy              # Your main story script
├── definitions.rpy         # Characters, variables, images, audio defs
├── effects.rpy             # Transitions, transforms, bleeps, effects
├── options.rpy             # Game config (name, version, build settings)
├── styles.rpy              # GUI styles (from EasyRenPyGui)
├── achievements.rpy        # Achievement declarations & screens
├── achievement_backend.rpy # Achievement system backend (don't edit)
│
├── screens/                # All GUI screens (from EasyRenPyGui)
│   ├── main_menu.rpy       # Main menu screen
│   ├── game_menu.rpy       # Pause/game menu
│   ├── dialogue_screens.rpy # Say/NVL screens
│   ├── choice_screen.rpy   # Choice menus
│   ├── preferences.rpy     # Settings screen
│   ├── save_load.rpy       # Save/load screens
│   ├── history_screen.rpy  # Dialogue history
│   ├── input.rpy           # Text input screen
│   ├── popup_screens.rpy   # Confirm dialogs
│   └── other_screens.rpy   # Skip indicator, notify, etc.
│
├── gui/                    # GUI image assets (buttons, bars, frames)
│   ├── bar/
│   ├── button/
│   ├── scrollbar/
│   └── slider/
│
├── images/                 # Game images
│   ├── bg/                 # Backgrounds
│   ├── characters/         # Character sprites
│   ├── cg/                 # CG / event images
│   ├── ui/                 # Custom UI elements
│   └── achievements/       # Achievement icons
│
├── audio/                  # Audio files
│   ├── music/              # Background music (.ogg recommended)
│   ├── sfx/                # Sound effects
│   ├── voice/              # Voice lines
│   └── bleeps/             # Dialogue bleep sounds (30 pre-loaded)
│
├── fonts/                  # Custom font files (.ttf, .otf)
│
└── tl/                     # Translation files
    └── None/
        └── common.rpym
```

---

## File-by-File Guide

### `game/options.rpy` - EDIT THIS FIRST

The three most important values to change for every new game:

```renpy
## The name shown in the window title and error reports
define config.name = _("My Game Name")

## Short name for executables (ASCII only, no spaces)
define build.name = "MyGameName"

## Save directory - use format "GameName-TIMESTAMP"
## Generate a unique one so saves don't conflict between games
define config.save_directory = "MyGameName-1234567890"
```

Other things you may want to change:
- `config.version` - your game's version number
- `config.main_menu_music` - uncomment and set a music file for the main menu
- `config.window` - set to `"show"`, `"hide"`, or `"auto"` for textbox behaviour
- Build section at the bottom - configure what files get included in distributions

---

### `game/definitions.rpy` - Characters & Variables

#### Adding a Character

```renpy
define e = Character(
    _("Eileen"),              # Name shown in textbox
    color="#c8c8ff",          # Name color
    image="eileen",           # Image tag (for side images)
    # callback=bleep_callback, # Enable typing bleeps (see below)
)
```

**Character color tips**: Use hex colors like `"#c8c8ff"`. Pick colors that contrast well with the textbox background.

#### Adding Variables

Use `default` for values that save with the game:
```renpy
default player_name = "Player"
default affection = 0
default route = None
default endings_seen = set()
```

Use `define` for constants:
```renpy
define MAX_AFFECTION = 100
```

#### Image Declarations

Ren'Py auto-detects images in `images/` by filename, so you usually don't need explicit declarations. But for special cases:

```renpy
## Composite image from multiple files
image eileen happy = Composite(
    (300, 600),
    (0, 0), "images/characters/eileen_base.png",
    (0, 0), "images/characters/eileen_happy_face.png",
)

## Layered image for characters with many expressions
layeredimage eileen:
    group outfit:
        attribute casual default "images/characters/eileen_casual.png"
        attribute formal "images/characters/eileen_formal.png"
    group expression:
        attribute happy default "images/characters/eileen_happy.png"
        attribute sad "images/characters/eileen_sad.png"
```

---

### `game/script.rpy` - Your Story

This is where your game's story lives. The `label start:` is the entry point.

#### Basic Scene Structure

```renpy
label chapter1:
    ## Set the scene
    scene bg park
    with fade

    ## Play music
    play music "audio/music/peaceful.ogg" fadein 1.0

    ## Show a character
    show eileen happy at center_stage
    with dissolve

    ## Dialogue
    e "Hello! Welcome to the park."
    narrator "She waves cheerfully."

    ## Choice
    menu:
        e "What would you like to do?"
        "Go for a walk":
            $ affection += 1
            e "Great idea!"
            jump walk_scene
        "Stay here":
            e "That's fine too."

    return
```

#### Splitting Your Script

For larger games, create additional `.rpy` files. Ren'Py merges them all automatically:

```
game/
├── script.rpy          # Main script, label start
├── chapter1.rpy        # label chapter1, etc.
├── chapter2.rpy
├── route_a.rpy
└── endings.rpy
```

---

### `game/effects.rpy` - Transitions, Transforms & Bleeps

#### Using Pre-built Transitions

```renpy
scene bg room
with slow_fade          # Slow cinematic fade
# or: with quick_dissolve, flash, wipe_right, iris_in, pixellate, etc.
```

Available transitions:
| Name | Effect |
|------|--------|
| `slow_fade` | 1s fade with 0.5s black hold |
| `quick_fade` | Fast 0.3s fade |
| `fade_to_black` | Standard fade through black |
| `long_fade` | Dramatic 2s fade |
| `slow_dissolve` | 1.5s dissolve |
| `quick_dissolve` | 0.3s dissolve |
| `flash` | White flash effect |
| `wipe_right/left/up/down` | Directional wipes |
| `iris_in/iris_out` | Circular iris transitions |
| `pixellate` | Pixellation effect |

#### Using Pre-built Transforms

```renpy
show eileen happy at left_side      # Position at left
show eileen happy at enter_right    # Slide in from right
show eileen happy at shake          # Quick shake
show eileen happy at bounce         # Bounce up
show eileen happy at breathing      # Subtle breathing loop
```

Available transforms:
| Name | Effect |
|------|--------|
| `left_side`, `right_side`, `center_stage` | Basic positions |
| `far_left`, `far_right` | Edge positions |
| `enter_left`, `enter_right` | Slide-in entrances |
| `fade_in_center` | Fade in at center |
| `exit_left`, `exit_right` | Slide-out exits |
| `shake` | Quick screen shake |
| `bounce` | Bounce up animation |
| `pulse` | Pulsing alpha (loops) |
| `breathing` | Subtle zoom breathing (loops) |
| `spin` | 360-degree spin (loops) |
| `tint_evening` | Warm orange tint |
| `tint_night` | Cool blue tint |
| `tint_sepia` | Sepia filter |
| `desaturate` | Black and white |

#### Adding Your Own Transitions

```renpy
## In effects.rpy, add:
define my_custom_fade = Fade(0.5, 1.0, 0.5, color="#ff0000")  # Red fade
```

#### Adding Your Own Transforms

```renpy
## In effects.rpy, add:
transform my_position:
    xalign 0.3 yalign 1.0

transform my_animation:
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 2.0
    linear 1.0 alpha 0.0
```

#### Dialogue Bleeps

The skeleton includes 30 bleep sounds from dmochas' dialogue bleeps pack. To give a character typing sounds:

**Option 1: Use the default bleep (bleep001)**
```renpy
## In definitions.rpy:
define e = Character("Eileen", callback=bleep_callback)
```

**Option 2: Give each character a unique bleep**
```renpy
## In effects.rpy, add a custom callback:
init python:
    def eileen_bleep(event, interact=True, **kwargs):
        if event == "show":
            renpy.sound.play("audio/bleeps/bleep005.ogg", channel="blips", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="blips")

## In definitions.rpy:
define e = Character("Eileen", callback=eileen_bleep)
```

**Available bleeps**: `bleep001.ogg` through `bleep030.ogg` in `audio/bleeps/`. Test them to find the right "voice" for each character.

---

### `game/achievements.rpy` - Achievements System

Credit: Feniks @ feniksdev.com

#### Adding an Achievement

```renpy
## In achievements.rpy, add:
define my_achievement = Achievement(
    name=_("First Steps"),
    id="first_steps",
    description=_("Complete the tutorial."),
    unlocked_image="images/achievements/first_steps.png",
)
```

#### Granting an Achievement

```renpy
## In your script:
$ my_achievement.grant()
```

#### Progress-Based Achievements

```renpy
define chapter_progress = Achievement(
    name=_("Bookworm"),
    id="bookworm",
    description=_("Read all 10 chapters."),
    unlocked_image="images/achievements/bookworm.png",
    stat_max=10,
    show_progress_bar=True,
)

## In your script, at the end of each chapter:
$ chapter_progress.add_progress(1)
```

#### Set-Based Progress (Rollback-Safe)

```renpy
define all_endings = Achievement(
    name=_("Completionist"),
    id="all_endings",
    description=_("See all endings."),
    unlocked_image="images/achievements/completionist.png",
    stat_max=3,
)

## At each ending:
$ all_endings.add_set_progress("good_end")   # Only counts once
$ all_endings.add_set_progress("bad_end")
$ all_endings.add_set_progress("neutral_end")
```

#### Hidden Achievements

```renpy
define secret = Achievement(
    name=_("Secret Found"),
    id="secret",
    description=_("You found the hidden room!"),
    unlocked_image="images/achievements/secret.png",
    hide_name=True,           # Shows "???" until unlocked
    hide_description=True,    # Shows "???" until unlocked
)

## Or with custom hidden text:
define secret2 = Achievement(
    name=_("The Truth"),
    id="secret2",
    description=_("You discovered the truth."),
    unlocked_image="images/achievements/truth.png",
    hide_name=_("???"),
    hide_description=_("Something lurks beneath the surface..."),
)
```

#### Adding Achievement Gallery to Menus

Add this button to your main menu or pause menu screen:
```renpy
textbutton _("Achievements") action ShowMenu("achievement_gallery")
```

#### Platinum / Linked Achievements

To auto-unlock an achievement when all others are earned:
```renpy
## In achievements.rpy, in the ACHIEVEMENT_CALLBACK list:
define myconfig.ACHIEVEMENT_CALLBACK = [
    LinkedAchievement(platinum_id='all'),
]
```

---

### `game/styles.rpy` - GUI Styling

This file (from EasyRenPyGui by Feniks) controls all visual styling. Key things you'll want to customize:

#### Resolution
```renpy
## Change 1920, 1080 to your target resolution:
init python:
    gui.init(1920, 1080)
```

#### Fonts
1. Drop your `.ttf` or `.otf` files into `game/fonts/`
2. Update in `styles.rpy`:
```renpy
define gui.text_font = gui.preference("font", "fonts/MyFont.ttf")
define gui.interface_text_font = gui.preference("interface_font", "fonts/MyFont.ttf")
define gui.name_text_font = gui.preference("name_font", "fonts/MyFont.ttf")
```

#### Text Size
```renpy
define gui.text_size = gui.preference("size", 33)       # Dialogue text
define gui.name_text_size = gui.preference("name_size", 45)  # Name text
```

#### Colors
Key colors to change in `styles.rpy`:
```renpy
## In the button_text style:
idle_color '#888888'       # Default button text
hover_color '#ff8335'      # Hovered button text
selected_color '#ffffff'   # Selected/active button text

## In label_text style:
color '#f93c3e'            # Menu headers, labels
```

#### GUI Images
Replace the PNG files in `game/gui/` to change:
- `textbox.png` - The dialogue textbox
- `namebox.png` - The character name box
- `frame.png` - General frame/panel background
- `notify.png` - Notification background
- `window_icon.png` - Window/taskbar icon
- `button/choice_*.png` - Choice menu buttons
- `button/slot_*.png` - Save/load slot backgrounds
- `bar/`, `slider/`, `scrollbar/` - UI element graphics

---

### `game/screens/` - Screen Files

These screens (from EasyRenPyGui) handle all the UI. Most common edits:

- **`main_menu.rpy`** - Add/remove main menu buttons, change layout
- **`game_menu.rpy`** - Modify the pause menu
- **`preferences.rpy`** - Add/remove settings options
- **`dialogue_screens.rpy`** - Modify the textbox/say screen

---

## Common Workflows

### Starting a New Game from This Template

1. Fork/clone this repository
2. Open `game/options.rpy` and set:
   - `config.name` - Your game's display name
   - `build.name` - Short name for builds (no spaces)
   - `config.save_directory` - Unique save folder name
3. Add your characters in `definitions.rpy`
4. Drop images into `images/bg/`, `images/characters/`, etc.
5. Drop music into `audio/music/`
6. Write your story in `script.rpy`
7. Test with Ren'Py launcher

### Adding a New Character

1. **Create sprites**: Place in `images/characters/` named like `charactername expression.png`
   - Example: `eileen happy.png`, `eileen sad.png`
2. **Define character** in `definitions.rpy`:
   ```renpy
   define e = Character(_("Eileen"), color="#c8c8ff", image="eileen")
   ```
3. **Use in script**:
   ```renpy
   show eileen happy
   e "Hello!"
   ```

### Adding Music

1. Place `.ogg` files in `audio/music/` (Ren'Py prefers Ogg Vorbis)
2. Optionally define them in `definitions.rpy`:
   ```renpy
   define audio.main_theme = "audio/music/main_theme.ogg"
   ```
3. Use in script:
   ```renpy
   play music "audio/music/main_theme.ogg" fadein 1.0
   ## or if you defined it:
   play music main_theme fadein 1.0
   ```

### Adding Sound Effects

1. Place `.ogg` files in `audio/sfx/`
2. Use in script:
   ```renpy
   play sound "audio/sfx/door_open.ogg"
   ```

### Changing the GUI Theme

1. Replace images in `game/gui/` (keep the same filenames and sizes)
2. Edit colors in `game/styles.rpy`
3. Edit fonts in `game/styles.rpy`
4. For the resolution, change `gui.init(1920, 1080)` in `styles.rpy`

---

## Included Plugins

### 1. EasyRenPyGui (by Feniks)
Pre-integrated into `game/screens/`, `game/styles.rpy`, `game/options.rpy`, and `game/gui/`. Provides clean, separated screen files instead of one massive `screens.rpy`. No setup needed - it's ready to use.

### 2. Achievements System (by Feniks)
Files: `game/achievements.rpy` and `game/achievement_backend.rpy`. Provides popup notifications, a gallery screen, progress tracking, hidden achievements, and Steam integration support.

### 3. dmochas Dialogue Bleeps Pack
30 bleep sound effects in `game/audio/bleeps/`. Pre-wired with a `bleep_callback` function in `effects.rpy`. Just add `callback=bleep_callback` to any character definition to enable typing bleeps.

---

## Tips

- **File naming**: Ren'Py is case-sensitive on Linux. Use lowercase filenames.
- **Image formats**: Use `.png` for sprites (transparency), `.jpg` for backgrounds, `.webp` for both (smaller files).
- **Audio formats**: `.ogg` (Vorbis) is preferred. `.mp3` and `.wav` also work.
- **Testing**: Press `Shift+D` in-game to open the developer menu. Press `Shift+R` to reload scripts.
- **Console**: Press `Shift+O` in-game to open the console for testing commands.
- **Rollback**: Players can scroll up to undo. Use `$ renpy.block_rollback()` to prevent it at key moments.
- **The `_()` function**: Wrap text strings in `_()` to mark them for translation.
- **Don't edit** `achievement_backend.rpy` - it's the engine that powers the achievement system.
