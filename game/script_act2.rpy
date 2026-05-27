define trousergeist = Achievement(
    name=_("Trousergeist"),
    id="trousergeist",
    description=_("Got startled by a bat. Lost your trousers in the process. Relatable."),
    unlocked_image="images/achievements/trousergeist.png", 
)

define follow_the_red_brick_road = Achievement(
    name=_("Follow the Red Brick Road"),
    id="follow_the_red_brick_road",
    description=_("Followed all five arrows through the lobby. Mike did not enjoy what he found."),
    unlocked_image="images/achievements/follow_the_red_brick_road.png",
)

define i_brought_snacks = Achievement(
    name=_("I Brought Snacks"),
    id="i_brought_snacks",
    description=_("Checked every useless item in the bag before finding the Bible. Thorough, at least."),
    unlocked_image="images/achievements/i_brought_snacks.png",
)

define bible_basher = Achievement(
    name=_("Bible Basher"),
    id="bible_basher",
    description=_("Read the correct holy word on the very first attempt. The Lord provides."),
    unlocked_image="images/achievements/bible_basher.png",
)

define its_a_werewolf = Achievement(
    name=_("It's a Werewolf!"),
    id="its_a_werewolf",
    description=_("Stayed to watch the post-credits sting. You were warned."),
    unlocked_image= "images/achievements/its_a_werewolf.png",
)

define survivors = Achievement(
    name=_("Survivors"),
    id="survivors",
    description=_("Made it all the way through. You've earned a pint."),
    unlocked_image= "images/achievements/survivors.png"
)


################################################################################
## MINI-GAME VARIABLES
##
## `default` is used (not `define`) because these values change during play
## and need to be saved with the game state.
##
## Ren'Py note: `default` must be at the top level — never inside a label.
## `define` is for constants; `default` is for saveable variables.
################################################################################

default arrow_step = 0
default inventory_checked = set()      ## tracks which wrong items the player clicked
default inventory_found_bible = False  ## True once the Bible is selected
default holy_word_first_try = True     ## False if any wrong word was picked first


## arrow_positions: each entry is (x, y, rotation_degrees, tint_colour)
## x/y are pixel offsets from the top-left of the 1920×1080 screen.
## Colours go from white → deep red to hint that something bad is at the end.
## REVIEW: adjust positions once the lobby background is finalised.
define arrow_positions = [
    (180,  460,   0, "#ffffff"),   ## 1 — white (harmless-looking)
    (460,  400, -15, "#ffcccc"),   ## 2 — pale pink (slightly ominous)
    (760,  500,  10, "#ff9999"),   ## 3 — pink (more ominous)
    (1060, 440, -20, "#ff6666"),   ## 4 — light red (quite ominous)
    (1360, 480,   0, "#ff0000"),   ## 5 — red (very ominous)
]


################################################################################
## MINI-GAME SCREENS
##
## These follow the same visual style as hit_the_wheel and ring_the_bell
## in screens/mingames.rpy:
##   - modal True (blocks clicks outside the frame)
##   - frame: with xalign 0.5 yalign 0.5 and Frame("gui/frame.png", ...)
##   - has vbox with descriptive italic text above the interactive element
##
## The arrow_trail screen is the exception: arrows must appear overlaid on
## the scene background, so there is no dialog frame.  Modal True is kept
## so the player can't accidentally advance dialogue while clicking.
################################################################################

## --- Arrow Trail (Scene 6) ---
## Called once per arrow from scene_six_arrows (5 total calls).
## Each call shows the CURRENT arrow (at arrow_positions[arrow_step]).
## Clicking increments arrow_step and returns, letting the script show
## Mike's reaction before calling the screen again for the next arrow.
##
## PLACEHOLDER: currently uses a textbutton "→"; replace the textbutton
## block with an imagebutton using Transform("arrow", ...) once arrow.png
## exists.  The Transform approach is already written below as a comment.
screen arrow_trail():
    modal True

    if arrow_step < len(arrow_positions):
        ## Unpack position/colour for this arrow step.
        ## The $ in a screen runs Python and stores the result in screen scope.
        $ ax, ay, arot, acol = arrow_positions[arrow_step]

        ## Hint text — sits at the top of the screen, out of the way.
        text "Something on the wall catches Mike's eye...":
            xalign 0.5 ypos 20
            italic True
            color "#aaaaaa"
            size 28

        ## PLACEHOLDER arrow button — replace with the imagebutton block below
        ## once images/cg/arrow.png exists.
        ##
        ## PLACEHOLDER textbutton (remove when real art is ready):
        textbutton "{color=[acol]}→{/color}":
            xpos ax ypos ay
            text_size 60
            action [SetVariable("arrow_step", arrow_step + 1), Return()]

        ## REAL imagebutton (uncomment when arrow.png exists):
        ## imagebutton:
        ##     idle  Transform("arrow", rotate=arot, matrixcolor=TintMatrix(acol), zoom=0.45)
        ##     hover Transform("arrow", rotate=arot, matrixcolor=TintMatrix(acol), zoom=0.50)
        ##     xpos ax ypos ay
        ##     action [SetVariable("arrow_step", arrow_step + 1), Return()]


## --- Cupboard Inventory (Scene 11) ---
## Uses Return(value) rather than Jump() so the call stack stays clean.
## The script label inv_loop reads _return and jumps to the right punchline.
## Items disappear once clicked (AddToSet marks them as checked).
## The Bible always stays visible — it's the way out.
##
## Ren'Py note: AddToSet(variable_name, value) requires the variable to
## already be a set() object.  We use `default inventory_checked = set()`
## above, and reset it with `$ inventory_checked = set()` at the start of
## the cupboard scene.
screen inventory_check():
    modal True

    frame:
        xalign 0.5 yalign 0.5
        padding (60, 50)
        background Frame("gui/frame.png", 60, 60, 60, 60)

        has vbox
        spacing 24
        xalign 0.5

        text "Jake rummages in Jon's bag...":
            xalign 0.5
            italic True
            color "#aaaaaa"
            size 28

        hbox:
            spacing 40
            xalign 0.5

            ## Wrong items disappear after being clicked once.
            ## Return() value tells inv_loop which punchline to show.
            if "stake" not in inventory_checked:
                vbox:
                    spacing 8
                    xalign 0.5
                    imagebutton:
                        idle  Transform("stake", zoom=0.6)
                        hover Transform("stake", zoom=0.65)
                        xalign 0.5
                        action [AddToSet("inventory_checked", "stake"), Return("stake")]
                    text "Stake":
                        xalign 0.5 color "#cccccc" size 24

            if "garlic" not in inventory_checked:
                vbox:
                    spacing 8
                    xalign 0.5
                    imagebutton:
                        idle  Transform("garlic", zoom=0.6)
                        hover Transform("garlic", zoom=0.65)
                        xalign 0.5
                        action [AddToSet("inventory_checked", "garlic"), Return("garlic")]
                    text "Garlic":
                        xalign 0.5 color "#cccccc" size 24

            if "water" not in inventory_checked:
                vbox:
                    spacing 8
                    xalign 0.5
                    imagebutton:
                        idle  Transform("holy_water", zoom=0.6)
                        hover Transform("holy_water", zoom=0.65)
                        xalign 0.5
                        action [AddToSet("inventory_checked", "water"), Return("water")]
                    text "Holy Water":
                        xalign 0.5 color "#cccccc" size 24

            ## The Bible is always visible — it ends the mini-game.
            vbox:
                spacing 8
                xalign 0.5
                imagebutton:
                    idle  Transform("bible", zoom=0.6)
                    hover Transform("bible", zoom=0.65)
                    xalign 0.5
                    action [SetVariable("inventory_found_bible", True), Return("bible")]
                text "Bible":
                    xalign 0.5 color "#ffffcc" size 24


## --- Holy Word Selection (Scene 12) ---
## Jon picks which passage to read aloud.  Only "righteous" works.
## Called from holy_word_game via `call screen bible_words`.
## Each wrong choice loops back to holy_word_game (see labels below).
screen bible_words():
    modal True

    frame:
        xalign 0.5 yalign 0.5
        padding (60, 50)
        background Frame("gui/frame.png", 60, 60, 60, 60)

        has vbox
        spacing 30
        xalign 0.5

        text "Jon flips to a page at random.  Which word is holiest?":
            xalign 0.5
            italic True
            color "#aaaaaa"
            size 28

        hbox:
            spacing 30
            xalign 0.5

            textbutton "{size=38}{color=#ffdddd}sandwich{/color}{/size}":
                action Return("sandwich")
                text_hover_color "#ffffff"

            textbutton "{size=38}{color=#ffdddd}badger{/color}{/size}":
                action Return("badger")
                text_hover_color "#ffffff"

            textbutton "{size=38}{color=#ffff88}righteous{/color}{/size}":
                action Return("righteous")
                text_hover_color "#ffffff"

            textbutton "{size=38}{color=#ffdddd}biscuit{/color}{/size}":
                action Return("biscuit")
                text_hover_color "#ffffff"


################################################################################
## SCENE 5 — THE BEDROOM
## Mike discovers the bat.  The phone is revealed.  Things get rhymey.
################################################################################

label scene_five_bedroom:
    ## LOCATION: a dark, presumably coffin-furnished bedroom somewhere in the house.
    scene bedroom with slow_dissolve

    ## The narrator is mid-sandwich — he's been eating since the interval.
    show the_narrator at char_centre
    with dissolve
    the_narrator "*munching on a sandwich*"
    the_narrator "The dinner engagement was certainly a curiosity, but what happened when the gang were shown to their room was the strangest occurrence yet."
    hide the_narrator with dissolve

    show butler at char_left
    show jake at char_right
    with dissolve
    butler "Here we are, good sirs. You'll be happy to know that this room contains the best beds in the house."
    jake "Where are they?"
    hide jake with dissolve
    show mike at char_right
    with dissolve
    butler "Oh, well, there aren't actually beds of course! The master doesn't use beds!"
    mike "Oh, this is another quirk isn't it! What does he sleep in?"
    butler "Coffin!"
    hide mike with dissolve
    show jake at char_right
    with dissolve
    jake "Excuse me?"
    butler "Coughing!"
    butler "Because I haven't had my pills! Excuse me, I must go."
    hide butler with dissolve

    show mike at char_left
    with dissolve
    mike "Well he certainly is enigmatic, this Vincent! A man after my own heart!"
    jake "Oh please, the only thing enigmatic about you is the smell after a curry!"
    hide jake with dissolve

    mike "Coo! Wonder what's in here?"
    hide mike with dissolve

    ## Mike opens a cupboard and disturbs the bat.

    play sound audio.scream

    show mike_no_trousers at char_right
    with dissolve
    mike "*screams*"

    show jon at char_left
    with dissolve
    jon "Was that the lion or the witch?"
    mike "There's a bat in there!"

    ## Hide Mike before showing the bat — three on screen otherwise.
    hide mike_no_trousers with dissolve
    show bat at char_right
    with dissolve
    bat "Terribly sorry old boy, you rather startled me!"
    jon "What happened to your trousers, Mike?"
    bat "Oh they're here! Sorry, I appear to have made a bit of a hole in them!"
    hide bat with dissolve
    hide jon with dissolve

    ## Achievement: scared by a bat and lost your trousers. Classic.
    $ trousergeist.grant()

    ## Fan/rhyming scene — Jake left, Mike (no trousers) right.
    show jake at char_left
    show mike_no_trousers at char_right
    with dissolve
    jake "Oh for goodness sake can we just GO TO SLEEP?"
    mike "Bit warm isn't it?"
    jake "Go ask the Butler for a fan then!"
    mike "Excuse me Butler... can we have a fan, my good man?"
    jake "Mike, don't rhyme everything!"
    mike "I'm not!"
    mike "It's really hot!"
    jake "MIKE!"
    mike "So if you could bring one in right away, would that be okay?"
    jake "I'm gonna kill you!"

    mike "Great face Jake! Let me take a snap chat!"

    ## The phone reveal — the narrator was right all along.
    jake "What's that?"
    mike "My phone!"
    jake "You said you didn't have a phone!"
    mike "Well, not the sort you make calls on!"

    ## Hide both before narrator — three on screen otherwise.
    hide jake with dissolve
    hide mike_no_trousers with dissolve
    show the_narrator at char_centre
    with dissolve
    the_narrator "I told you he had a phone!"
    the_narrator "And that's why he didn't tell anyone!"
    hide the_narrator with dissolve

    ## Jake chases Mike out — Jake alone, Mike already off screen.

    play sound audio.thwack
    show jake at char_left
    with dissolve
    jake "*grabs a cricket bat that has appeared from nowhere*"
    jake "GET OUT!"
    jake "And stay out!"

    ## The bat has an opinion.  Jake is at left, bat at right.
    show bat at char_right
    with dissolve
    bat "I say, it's rather stuffy in here!"
    hide bat with dissolve
    hide jake with dissolve

    ## Jake and Jon have a vague conversation about something unspecified.
    show jake at char_left
    show jon at char_right
    with dissolve
    jon "Is everything alright, man? You seem a bit on edge today!"
    jake "I'm fine mate, it's just... well... it's been two days since I last... y'know!"
    jon "Y'know?"
    jake "Yeh... y'know!"
    jon "Oh, I know!"

    ## A pause that does a lot of heavy lifting.
    pause 1.5
    jon "..."

    hide jake with dissolve
    hide jon with dissolve

    jump scene_six_arrows


################################################################################
## SCENE 6 — THE LOBBY / ARROW TRAIL (Mini-game)
## Mike wanders the lobby following progressively redder arrows, which leads
## him to Count Vincent.  This is the arrow trail mini-game.
##
## MINI-GAME FLOW:
##   scene_six_arrows resets arrow_step to 0, then calls arrow_trail 5 times.
##   Each call to `call screen arrow_trail` shows one arrow.
##   Clicking the arrow increments arrow_step and returns to script.
##   Script shows Mike's reaction, then calls the screen again.
##   After all 5 arrows, Mike meets the Count.  Not well.
################################################################################

label scene_six_arrows:
    ## LOCATION: the lobby — same bg as Scene 3.
    scene lobby with slow_dissolve
    show mike_no_trousers at char_centre
    with dissolve

    ## The cinema audience checks in.
    aud "Shelly?"
    shelly "What?"
    aud "Nothing!"

    ## PLACEHOLDER AUDIO: audio.horn is a stand-in for laughter
    play sound audio.laughing

    mike "...what was that?"
    mike "Oh! An arrow on the wall. How helpful!"

    ## Reset the mini-game counter before we start.
    $ arrow_step = 0

    ## Arrow 1 — white, innocent-looking.
    hide mike_no_trousers
    scene lobby
    show mike_no_trousers at char_left
    with dissolve
    call screen arrow_trail

    mike "...okay, another one. Sure, why not."

    ## Arrow 2 — pale pink, still probably fine.
    hide mike_no_trousers
    scene lobby
    show mike_no_trousers at char_centre
    with dissolve
    call screen arrow_trail

    mike "These arrows are getting a bit... red."

    ## Arrow 3 — pink, not so fine.
    hide mike_no_trousers
    scene lobby
    show mike_no_trousers at char_centre
    with dissolve
    call screen arrow_trail

    mike "I'm sure this is fine."

    ## Arrow 4 — light red, definitely not fine.
    hide mike_no_trousers
    scene lobby
    show mike_no_trousers at char_right
    with dissolve
    call screen arrow_trail

    mike "Definitely fine."

    ## Arrow 5 — red. It is not fine.
    hide mike_no_trousers
    scene lobby
    show mike_no_trousers at char_right
    with dissolve
    call screen arrow_trail

    ## Achievement: completed the full arrow trail.
    $ follow_the_red_brick_road.grant()

    ## End of the trail — Mike finds the Count.
    scene lobby with dissolve
    show mike_no_trousers at char_left
    show count at char_right
    with dissolve
    mike "Hello!"

    ## The Count helps himself.
    ## PLACEHOLDER AUDIO: audio.scream for the bite gag
    play sound audio.scream

    hide mike_no_trousers with dissolve
    count "*cackles*"
    hide count with dissolve

    jump scene_seven_intermission


################################################################################
## SCENE 7 — INTERMISSION
## Shelly is selling ice cream.  Posh Person is unimpressed.
## Mirrors the Scene 2 cinema interlude in structure.
################################################################################

label scene_seven_intermission:
    scene cinema with dissolve
    play music audio.intermission fadein 0.5

    centered "{size=80}{color=#ffffff}INTERMISSION{/color}{/size}"

    show shelly at char_right
    with dissolve
    show aud at char_left
    with dissolve
    shelly "Right. Queue here for ice cream! Tell me what flavour you want and I'll get it for you... so long as you ask for vanilla. If you don't, you can hop it!"
    aud "Shelly?"

    play sound audio.thwack
    hide aud with dissolve
    show posh at char_left
    with dissolve

    posh "Steward? This is worse than their Doctor Who series!"
    steward "Well you keep watching them, ma'am. What right have you to complain?"
    shelly "Alright everyone back to your seats, it's coming on again!"
    posh "That was fast!"

    stop music fadeout 1.0

    jump scene_eight_chase


################################################################################
## CHASE MINI-GAME
## Three QTE panic choices — all paths are silly, all paths escape.
## Called from scene_eight_chase; returns when the chaos subsides.
################################################################################

label chase_minigame:

    ## — Step 1 ----------------------------------------------------------------
    call screen chase_choice("THE COUNT IS RIGHT BEHIND YOU!", "DUCK!", "JUMP!")
    if _return == "a":
        the_narrator "Jon ducks into a pile of coats."
        the_narrator "The Count trips over Jon's legs. It is fortunate. It is also entirely accidental."
    else:
        the_narrator "Jake leaps over a small occasional table."
        the_narrator "So does the Count."
        the_narrator "They are now both jumping over the same table, which achieves very little."

    ## — Step 2 ----------------------------------------------------------------
    call screen chase_choice("HE'S STILL COMING!", "HIDE IN THE VASE!", "THROW SOMETHING!")
    if _return == "a":
        the_narrator "Mike is already in the vase."
        the_narrator "There is a brief, tetchy argument about whose turn it is to be in the vase."
        the_narrator "Nobody wins."
    else:
        the_narrator "Jake reaches into his coat and produces a kipper."
        the_narrator "Nobody asks where it came from."
        the_narrator "He throws it. The Count slips on it. This is, apparently, how Van Helsing also died."

    ## — Step 3 ----------------------------------------------------------------
    call screen chase_choice("HE'S RIGHT THERE!", "SCREAM!", "SLAM THE DOOR!")
    if _return == "a":
        the_narrator "Jake screams."
        the_narrator "It achieves absolutely nothing, but everyone agrees it was very committed."
    else:
        the_narrator "Jake slams a large oak door directly into the Count's face."
        the_narrator "The Count says something in Romanian."
        the_narrator "Jake has no idea what it means but suspects it isn't a compliment."

    return


################################################################################
## SCENE 8 — THE CHASE
## Jake and Jon find Mike on the floor.  Dave gets mentioned.
## The Count reveals himself.  Jon remains calm about it.
################################################################################

label scene_eight_chase:
    ## LOCATION: lobby — the lads regroup.
    scene lobby with slow_dissolve
    show jake at char_left
    with dissolve
    jake "Mike?"

    hide jake with dissolve
    show jon at char_left
    show mike_no_trousers at char_right
    with dissolve
    jon "We got your trousers!"
    jon "What you doing down there, lad?"
    jake "Get up, you silly twit!"

    mike "Hi Dave!"
    jon "No! We're Jon and Jake. Dave died last year, remember?"
    mike "Did he?"
    jon "Yeh, you killed him, remember?"

    ## The Count makes a dramatic entrance.
    ## PLACEHOLDER AUDIO: audio.thunder and audio.piano_sting for the reveal
    play sound audio.thunder
    hide jon
    hide mike_no_trousers
    with dissolve
    show count_bloody at char_centre
    with vpunch

    ## Hide Count before showing Jake and Jon — three on screen otherwise.
    hide count_bloody with dissolve
    show jake at char_left
    show jon at char_right
    with dissolve
    jon "Oh! He's a vampire! I get it now!"

    ## Chase sequence — QTE mini-game with three panic choices.
    hide jake
    hide jon
    hide count_bloody
    with dissolve

    show the_narrator at char_centre
    with dissolve
    the_narrator "{i}*a chaotic chase sequence ensues*{/i}"
    hide the_narrator with dissolve

    ## Player makes three frantic decisions — lobby background stays visible
    ## behind the red-tinted chase_choice overlay.
    call chase_minigame

    show the_narrator at char_centre
    with dissolve
    the_narrator "You know what one of the worst things you can do in film making is? Having a really dramatic scene and then switching it to something completely different!"
    hide the_narrator with dissolve

    jump scene_nine_forest


################################################################################
## SCENE 9 — THE FOREST (TOM)
## Tom has been in the car this whole time.  He is unbothered.
################################################################################

label scene_nine_forest:
    ## LOCATION: dark forest — Tom at the car, minding his own business.
    scene forest_night with slow_dissolve
    show tom at char_centre
    with dissolve
    tom "*reading a Beano, sipping a drink*"
    tom "Wonder where the others got to..."
    hide tom with dissolve

    jump scene_ten_butler


################################################################################
## SCENE 10 — BUTLER AMBUSH
## Tom wanders into the house.  The Butler has a surprise for him.
################################################################################

label scene_ten_butler:
    ## LOCATION: lobby — Tom wanders in and spots the trap.
    scene lobby with slow_dissolve
    show tom at char_centre
    with dissolve
    tom "Hello?"
    tom "Ooh, a bottle of whiskey on a giant red X. That's not suspicious at all."

    ## The Butler appears from nowhere, as butlers do.
    show butler at char_left
    with dissolve

    ## PLACEHOLDER AUDIO: audio.thwack — Tom takes a bop
    play sound audio.thwack

    tom "What was that for?"
    hide tom with dissolve
    hide butler with dissolve

    jump scene_eleven_cupboard


################################################################################
## SCENE 11 — THE CUPBOARD (Inventory Mini-game)
## Jake and Jon hide in a cupboard and go through Jon's bag.
## The bat is in there already.  So is Jon's trumpet, apparently.
##
## MINI-GAME FLOW:
##   call cupboard_inventory  →  shows inventory screen repeatedly
##   Each wrong item (stake, garlic, holy water) triggers a short punchline
##   and then loops back to the inventory screen.
##   Clicking the Bible ends the game and continues the story.
##
##   Call stack: scene_eleven_cupboard calls cupboard_inventory,
##   which falls through to inv_loop.  inv_loop calls screen inventory_check.
##   Wrong item → Return("item") → jump to punchline → jump inv_loop (loops).
##   Bible → Return("bible") → jump inv_bible → return (to cupboard_inventory
##   call frame, which unwinds back to scene_eleven_cupboard).
################################################################################

label scene_eleven_cupboard:
    ## Fleeing the Count, Jake and Jon hide in the bedroom cupboard.
    scene bedroom with slow_dissolve
    show jake at char_left
    show jon at char_right
    with dissolve
    jake "*panting*"
    jon "*also panting*"

    jake "In here!"
    jon "Won't open!"
    jake "Fiddle with the knob."
    jon "I don't like fiddling with the knob!"
    jake "Let me do it then!"

    ## Jon acknowledges the audience.
    hide jake with dissolve
    jon "{i}*to camera*{/i}"
    jon "Going in the closet!"
    hide jon with dissolve

    ## The bat is already in there.
    show bat at char_centre
    with dissolve
    bat "Oh hello!"
    hide bat with dissolve

    ## The plastic bat toy gets ejected.
    show plastic_bat_toy at char_centre
    with vpunch
    pause 0.5
    hide plastic_bat_toy with dissolve

    ## Inside the cupboard — pitch black.
    scene black with dissolve
    show jake at char_left
    show jon at char_right
    with dissolve
    jake "Well this is a bit camp!"
    jon "Woah! Don't press down on my stomach!"
    jake "Why not?"

    ## PLACEHOLDER AUDIO: audio.fart — the answer to "why not"
    play sound audio.fart
    pause 1.0

    ## Now we check the bag.  call jumps into cupboard_inventory.
    ## When inv_bible: return fires, we land back here on the next line.
    call cupboard_inventory

    jump scene_twelve_bible


################################################################################
## SCENE 12 — THE BIBLE SCENE (Holy Word Mini-game)
## Jon confronts the Count with the Bible.
## The player picks which word to read aloud.  Only "righteous" works.
##
## MINI-GAME FLOW:
##   call holy_word_game  →  call screen bible_words
##   Wrong word → short dialogue → jump back to holy_word_game (loops).
##   "righteous" → jump bible_correct → return (to holy_word_game call frame
##   in scene_twelve_bible).  Story continues from there.
################################################################################

label scene_twelve_bible:
    scene bedroom with slow_dissolve
    show count_bloody at char_centre
    with dissolve
    count "{i}*looking around fruitlessly*{/i}"
    hide count_bloody with dissolve

    ## Jon pops out of the cupboard with the Bible.
    show jon at char_left
    show count_bloody at char_right
    with dissolve
    jon "Oh hello! Was wondering if you'd like to hear this."

    hide jon
    hide count_bloody
    with dissolve

    ## Reset "first try" tracker before the mini-game.
    ## We do this here (not in the label) so it resets on reload from save.
    $ holy_word_first_try = True

    ## The holy word mini-game.  Returns here when bible_correct: return fires.
    call holy_word_game

    ## The Count is now cured (count_on_fire → count_happy handled in bible_correct).
    ## Jake alone first — count_happy comes in right; three on screen otherwise.
    show jake at char_left
    with dissolve
    jake "He gone then?"

    show count_happy at char_right
    with dissolve
    count "Hallelujah! It's a miracle! The evil within me has been purged."
    count "I'm free! I feel so alive! I just want to sing!"
    jake "Please don't!"
    count "Oh what a beautiful morning! Oh what a beautiful day!"
    count "I've got a wonderful feeling, everything's going my..."

    ## The Butler puts a stop to it.
    ## Hide Jake first — butler would be at char_left on top of jake otherwise.
    hide jake with dissolve
    show butler at char_left
    with dissolve
    ## PLACEHOLDER AUDIO: audio.thwack
    play sound audio.thwack

    hide count_happy with dissolve
    hide butler with dissolve

    show jon at char_left
    with dissolve
    jon "Well, I think everything turned out alright!"
    jon "I suppose you'll be off to... y'know... then... with that girl you mentioned earlier?"
    show jake at char_right
    with dissolve
    jake "Urr... I don't think she plays Pokemon!"

    ## The bomb subplot pays off.  Jon foreshadowed this in the cupboard.
    ## PLACEHOLDER AUDIO: audio.bomb_tick — looping tick until explosion
    play sound audio.bomb_tick loop

    jon "Pokemon? Oh! It's that sort of... y'know..."
    jake "What sort of... y'know... did you think I meant?!"
    jon "Oh... never mind!"
    jake "JON! You really have a filthy mind! And another thing, what's that ticking noise?"
    jon "Oh that'll be the bomb I mentioned!"
    jake "Oh right!"

    ## Clear both so the bomb can be shown alone — jake speaks off-screen.
    hide jake with dissolve
    hide jon with dissolve
    show bomb at char_centre
    with dissolve
    jake "Flip!"

    stop sound
    ## Using the existing crash sound — close enough for a bomb.
    ## PLACEHOLDER: swap for a proper explosion sfx if you have one.
    play sound audio.explode

    scene black with flash
    pause 1.0

    jump scene_thirteen_wreckage


################################################################################
## SCENE 13 — THE WRECKAGE
## Everyone survived, somehow.  It's time for the pub.
################################################################################

label scene_thirteen_wreckage:
    ## LOCATION: the bedroom, now comprehensively wrecked.
    scene bedroom_wreckage with slow_dissolve

    ## Show survivors in pairs — three at once would break the two-char rule.
    show jake at char_left
    show mike_no_trousers at char_right
    with dissolve
    jake "Gosh! That was lucky!"

    hide mike_no_trousers with dissolve
    show jon at char_right
    with dissolve
    jon "Rather!"
    hide jake with dissolve
    hide jon with dissolve

    show the_narrator at char_centre
    with dissolve
    the_narrator "And so, our friends survived a night in the scary house."
    the_narrator "And now, with a new mindset and a renewed appreciation for life and all they have been given in it, they looked at the rising sun and spoke the first words of this new dawn..."
    hide the_narrator with dissolve

    show jake at char_left
    with dissolve
    jake "Let's go the pub!"
    hide jake with dissolve

    ## Achievement: you made it to the end.
    $ survivors.grant()

    scene black with dissolve
    centered "{size=80}{color=#ff0000}{font=fonts/bloody.ttf}END CREDITS{/font}{/color}{/size}"
    pause 3.0

    jump scene_fourteen_stinger


################################################################################
## SCENE 14 — POST-CREDITS STINGER
## Count Vincent is skipping happily through the forest.
## He will not be doing so for long.
################################################################################

label scene_fourteen_stinger:
    ## LOCATION: the daylight forest — the Count's fresh start.
    ## PLACEHOLDER: forest_bright is Solid("#2d4a1e") until real art exists.
    scene forest_bright with slow_dissolve
    show count_happy at char_centre
    with dissolve
    count "{i}*skipping happily through the forest*{/i}"

    ## Achievement: stayed for the stinger.
    $ its_a_werewolf.grant()

    ## The werewolf arrives.
    show werewolf at char_right
    with vpunch
    ## PLACEHOLDER AUDIO: audio.werewolf_growl
    play sound audio.werewolf_growl

    count "Oh! Not again!"

    hide count_happy
    hide werewolf
    with dissolve

    ## PLACEHOLDER AUDIO: audio.scream
    play sound audio.scream
    pause 2.0

    scene black with dissolve
    centered "{size=60}{color=#ff0000}{font=fonts/bloody.ttf}FIN{/font}{/color}{/size}"
    pause 3.0

    ## `return` here ends the game and returns to the main menu.
    return


################################################################################
## MINI-GAME LABELS — CUPBOARD INVENTORY
##
## cupboard_inventory: resets state and falls through to inv_loop.
## inv_loop: calls the inventory screen in a loop until the Bible is found.
## inv_stake / inv_garlic / inv_water: wrong-item punchlines, loop back.
## inv_bible: success — grants achievement if all wrong items were tried first.
##
## Why `fall-through` from cupboard_inventory to inv_loop?
## In Ren'Py, labels are just markers.  Execution continues past a label
## marker if nothing redirects it (return/jump/call).  cupboard_inventory's
## code ends without a jump, so it naturally reaches inv_loop next.
################################################################################

label cupboard_inventory:
    show jake at char_left
    show jon at char_right
    with dissolve
    jake "Right! We need to figure out what we've got. Have a rummage in the bag."
    jon "Righto!"
    hide jake
    hide jon
    with dissolve

    ## Reset the mini-game state each time the cupboard is entered.
    $ inventory_checked = set()
    $ inventory_found_bible = False
    ## Falls through to inv_loop below.

label inv_loop:
    ## Call the inventory screen.  It returns a string: "stake", "garlic",
    ## "water", or "bible".  We use _return to decide what to do.
    call screen inventory_check
    if _return == "stake":
        jump inv_stake
    elif _return == "garlic":
        jump inv_garlic
    elif _return == "water":
        jump inv_water
    elif _return == "bible":
        jump inv_bible
    else:
        jump inv_loop  ## safety net — should never fire

label inv_stake:
    show jake at char_left
    show jon at char_right
    with dissolve
    jake "Do we have a stake?"
    jon "No, I had it for lunch!"
    hide jake
    hide jon
    with dissolve
    jump inv_loop

label inv_garlic:
    show jake at char_left
    show jon at char_right
    with dissolve
    jake "Garlic?"
    jon "Had that with the stake."
    hide jake
    hide jon
    with dissolve
    jump inv_loop

label inv_water:
    show jake at char_left
    show jon at char_right
    with dissolve
    jake "Holy water?"
    jon "Errr... no!"
    jake "Anything holy?"
    hide jake
    hide jon
    with dissolve
    jump inv_loop

label inv_bible:
    show jake at char_left
    show jon at char_right
    with dissolve
    jon "What about this?"
    jake "Brilliant! I didn't know you had a Bible!"
    jon "You should have done, I was hugging it in a scene earlier, remember?"
    jake "Oh yeh! Good foreshadowing!"
    jon "Thanks! Incidentally I think a bomb might go off later!"
    jake "Well, we'll cross that bridge when we come to it!"

    ## Achievement: clicked all three useless items before finding the Bible.
    ## inventory_checked contains everything that was clicked (except the Bible).
    ## len() >= 3 means all three wrong items were tried.
    if len(inventory_checked) >= 3:
        $ i_brought_snacks.grant()

    hide jake
    hide jon
    with dissolve
    ## `return` unwinds to scene_eleven_cupboard (where `call cupboard_inventory` was).
    return


################################################################################
## MINI-GAME LABELS — HOLY WORD GAME
##
## holy_word_game: shows the bible_words screen and dispatches on _return.
## bible_sandwich / bible_badger / bible_biscuit: wrong word punchlines.
## bible_correct: the right word — sets the Count on fire.
##
## On wrong answers, holy_word_first_try is set to False.
## If bible_correct is reached with holy_word_first_try still True,
## the "Bible Basher" achievement is granted.
##
## `return` in bible_correct unwinds to scene_twelve_bible
## (where `call holy_word_game` was).
################################################################################

label holy_word_game:
    ## Show the word selection.  Loop back here after each wrong answer.
    call screen bible_words

    if _return == "righteous":
        jump bible_correct
    elif _return == "sandwich":
        $ holy_word_first_try = False
        jump bible_sandwich
    elif _return == "badger":
        $ holy_word_first_try = False
        jump bible_badger
    elif _return == "biscuit":
        $ holy_word_first_try = False
        jump bible_biscuit
    else:
        jump holy_word_game  ## safety net

label bible_sandwich:
    show jon at char_left
    show count_bloody at char_right
    with dissolve
    jon "\"...and Jesus did eat of the sandwich...\""
    count "...I'm sorry, is this going somewhere?"
    hide jon
    hide count_bloody
    with dissolve

    show jon at char_left
    with dissolve
    jon "Let me try a different bit..."
    hide jon with dissolve
    jump holy_word_game

label bible_badger:
    show jon at char_left
    show count_bloody at char_right
    with dissolve
    jon "\"...and lo, the badger was upon him...\""
    count "That's not in the Bible."
    jon "It might be in the Apocrypha!"
    count "It really isn't."
    hide jon
    hide count_bloody
    with dissolve

    show jon at char_left
    with dissolve
    jon "Let me try a different bit..."
    hide jon with dissolve
    jump holy_word_game

label bible_biscuit:
    show jon at char_left
    show count_bloody at char_right
    with dissolve
    jon "\"...blessed are the biscuit-makers...\""
    count "Are you just making these up?"
    jon "...maybe!"
    hide jon
    hide count_bloody
    with dissolve

    show jon at char_left
    with dissolve
    jon "Let me try a different bit..."
    hide jon with dissolve
    jump holy_word_game

label bible_correct:
    ## The right word.  The Count combusts.
    show jon at char_left
    show count_bloody at char_right
    with dissolve
    jon "\"...the Lord watches over the way of the righteous...\""

    ## PLACEHOLDER AUDIO: audio.fire_whoosh
    play sound audio.fire_whoosh
    hide count_bloody
    show count_on_fire at char_right
    with dissolve

    jon "Oh gosh! Sorry!"
    count "What was that FOR???"
    jon "Well... y'know... you were trying to suck our blood!"
    count "Look! I'm a vampire! I {i}have{/i} to! There was no need for that!"

    ## Achievement: got the right word on the first attempt.
    if holy_word_first_try:
        $ bible_basher.grant()

    hide count_on_fire with dissolve
    jon "I'm really sorry, I didn't mean to..."
    hide jon with dissolve

    ## `return` sends execution back to scene_twelve_bible, after `call holy_word_game`.
    return
