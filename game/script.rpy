################################################################################
## SCRIPT.RPY - Main Game Script
################################################################################

## The game starts here.
label start:
    $ preferences.text_cps = 40

#################################################################################
## Title Screen
#################################################################################
    $ renpy.music.set_volume(1.0, channel="voice")
    play sound audio.rain loop
    play music audio.credit_theme fadein 1.0 loop
    play movie "video/opening_pan.webm"
    scene forest_night
    centered "{size=180}{color=#FF0000}{font=fonts/bloody.ttf}{b}SCARY HOUSE{/b}\n{size=150}IT'S FRIGHTENING{/size}{/font}{/color}{/size}"

#################################################################################
## Opening Credits Scroll
#################################################################################
    stop movie 
    stop sound fadeout 0.5
    show screen opening_credits
    $ renpy.pause(42.0)
    hide screen opening_credits
    stop music fadeout 0.5

#################################################################################
## Scene 1
################################################################################

    scene forest_night with slow_dissolve 
    play music audio.rain fadein 0.5 loop
    show the_narrator at char_centre
    with dissolve
    the_narrator "Oh hello! I didn't hear you approach. You know why you're here, I am going to tell you a tale of strange consequences."
    the_narrator "It all begins here, on an unrealistically dark and stormy night, when four goons found thier landrover had broken down in the middle of the dark"
    the_narrator "forest where silly people jump out on you and say stupid stuff..."
    hide the_narrator with dissolve

    scene black with slow_dissolve
    show bg forest scroll_stop
    play sound audio.car
    show la_drover at drover_enter_stop
    pause
      

    
    vo "Tom is trying to get the Landrover to go, he is whacking it with a hammer. Jake sits next to him. Jon and Mike are in the back."
    play sound audio.window
    vo "Tom winds down the window"
    
    

    show silly1 at char_left
    with dissolve
    $ camera_shake()
    silly1 "Is your name Terry?"
    

    show tom at char_right
    with dissolve
    tom "???????"
    play sound audio.window
    vo "Tom winds the window back up without saying a word"
    hide tom with dissolve
    hide silly1 with dissolve

    show jon at char_left
    with dissolve
    jon "There really are some strange people around"

    show mike at char_right
    with dissolve
    mike "There's another one by Jake!"
    hide mike with dissolve
    hide jon with dissolve

    show silly2 at char_left
    $ camera_shake()
    show jake at char_right
    play sound audio.window
    with dissolve
    jake "Oh 'eck!"
    silly2 "I AM DRACOREX THE DESTROYER OF WORLDS!"
    hide silly2 with dissolve
    show silly3 at char_left
    with dissolve
    $ camera_shake()
    silly3 "I'm Wayne! His brother!"
    hide jake with dissolve
    hide silly3 with dissolve

    show the_narrator at char_centre
    with dissolve
    the_narrator"It wasn't long before the awesome foursome decided that something needed to be done."
    hide the_narrator with dissolve

    show jake at char_left
    with dissolve
    jake "I've decided, something needs to be done!"
    hide jake with dissolve

    show mike at char_right
    with dissolve
    mike "  Well, now that we've all agree that something needs to be done."
    hide mike with dissolve

    show tom at char_left
    with dissolve
    vo "Tom whacks the steering wheel again, then sits forward with his head in his hands."
    $ wheel_hits = 0
    $ wheel_phrase = ""
    call screen hit_the_wheel
    play sound audio.horn
    $ camera_shake()
    tom "Oh god, why???"

    show jon at char_right
    with dissolve
    jon "Oh leave God alone! He gets blamed for enough as it is! War, famine, religion..."
    hide tom with dissolve

    show jake at char_left
    with dissolve
    jake "Has anyone got a phone? We could call for help!"
    jon "Haven't you got one?"
    jake "I don't carry a phone, this strange woman keeps texting me and saying..."
    hide jake with dissolve
    hide jon with dissolve

    

    vo "Inside, TOM is necking a bottle and JON is rocking backwards and forwards hugging a Bible. JAKE is bewildered at his friends actions and MIKE is leaning forwards."

    show mike at char_right
    with dissolve
    mike "Well tell us more then!"
    hide  mike with dissolve

    show the_narrator at char_centre
    with dissolve
    the_narrator "So, it was eventually realised that nobody in the car had a phone...except for Mike, but he didn't say anything, and I won't explain why until later on in the story."
    the_narrator "Without this knowledge, the group decided that three would go and look for help whilst the fourth remained behind to keep an eye on the car."
    the_narrator "After a few rounds of cards and some golf, it was decided that Jake, Jon and Tom would go. Then Tom revealed that he was pregnant and couldn't possibly leave the car, so Mike had to go."
    the_narrator "And as the three walked through the very dark and horrible forest, they stumbled across a scary house!!!"
    stop music fadeout 0.5

    ######################################################
    ####Scene 2####################
    ######################################################

    scene cinema with slow_dissolve
    play music audio.intermission loop
    show aud at char_left
    aud "Shelly!"
    show shelly at char_right
    shelly "What?!"
    aud "What ya doin' after the film?"
    shelly "Nout with you sunshine!"
    stop music fadeout 0.5

    ######################################################
    ####Scene 3####################
    ######################################################

    scene scary_door with slow_dissolve 
    show jon at char_left 
    with dissolve
    jon "This doornob sure is dusty"
    hide jon with dissolve

    show jake at char_right
    with dissolve
    $ bell_hits = 0
    call screen ring_the_bell()
    $ bell_hits = 0
    hide jake

    vo "They turn to leave. As they do, the door opens and strange man steps out."

    show butler at char_left
    with dissolve

    butler "Good evening."

    show mike at char_right
    with dissolve
    mike "AHH! The ARK PRODUCTIONS guy!"

    butler "Excuse me? You seem to be familiar with my twin brother Tom."
    hide mike with dissolve
    show jake at char_right
    with dissolve

    jake "So who are you then?"

    butler "Tom"

    hide jake with dissolve
    show jon at char_right
    with dissolve

    jon "You're both called Tom?"

    butler "Yes. He is Tom 1 and I am Tom 2. Our parents thought it would save time, because when they wanted us both they only had to yell 'Tom' and we both came."
    
    hide jon with dissolve
    show mike at char_right
    with dissolve

    mike "Makes sense to me"

    hide mike with dissolve
    show jake at char_right
    with dissolve

    jake "Oh by the way, you don't have a phone we can use do you?"
    butler "Oh it's one of those calls is it? Very well, you'd better come in."

    scene lobby with slow_dissolve
    show butler at char_right
    with dissolve
    
    butler "You've arrived on a very special occasion. It's one of the master's affairs."

    show mike at char_left
    with dissolve

    mike "Affairs? You mean, like, with a bird? Does he have an actual bird in here?"
    butler "erm....yes"
    mike "Can I see?"
    butler "Haha! Oh you... teasing me... so you're blue but I can't take a chance on a chick like you... it's something I couldn't do..."

####scene 4######

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
$ renpy.stop_predict()
$ renpy.block_rollback()
$ renpy.restart_interaction()
stop movie

show layer master at disco_lights

# Show intro screen first
$ renpy.call_screen("rhythm_intro_screen")

# IMPORTANT: reset interaction so countdown can animate
$ renpy.restart_interaction()

# Countdown before the game begins
$ rhythm_countdown()

label rhythm_retry:

    $ rhythm_result = run_rhythm_game()

    ## --- Retry screen if score is very low ---
    if rhythm_result["percent"] < 30:
        menu:
            "You scored [rhythm_result['percent']]%. Try again?"
            "Try again!":
                jump rhythm_retry
            "Move on...":
                pass

## --- Achievement if perfect ---
if rhythm_result["perfect"]:
    $ disco_fever.grant()

## --- Resume scene ---
label after_rhythm:
    play music audio.abba fadein 0.5
    show layer master at disco_lights

    hide silly1 with dissolve
    show jake at char_right
    with dissolve
    play sound audio.record_scratch
    stop music fadeout 0.5
    show layer master
    jake "I hate ABBA!"

    silly1 "Oh fine! We'll go then!"
    hide silly3 with dissolve
    hide silly2 with dissolve

    show count at char_left
    with dissolve
    count "Well, you seem to have chased away all of my guests anyway!"
    hide jake with dissolve
    show butler at char_right
    with dissolve
    butler"Ah! Allow me to introduce the master of the house..."
    count "Count Vincent de Laza de Turcheon de Grumpit de Passamoor de Vile de Smith. I hail from a long and noble family descending from the very early days of Stoke-on-Trent."
    hide butler with dissolve
    show mike at char_right
    with dissolve
    mike "Sorry!?"
    count "Stoke on Trent"
    mike "No I heard you the first time, I was just saying..."
    hide mike with dissolve
    show jake at char_right
    with dissolve
    jake "You'll have to excuse him! He means no harm he's just a complete goon!"
    hide jake with dissolve
    show jon at char_right
    with dissolve
    jon "It always amazes me how people can be complete goons without any formal education!"
    count "Can I ask why you three have just thought to wander into my private residence?"
    hide jon with dissolve
    show jake at char_right
    with dissolve
    jake "Oh yes, sorry. Our car broke down, we were wondering if we could use your phone."
    count "I'm sorry, all our phones are currently out of service."
    play sound audio.phone
    hide jake
    show butler at char_right
    with dissolve
    pause
    butler "Hello Audrey! Yes I'll pick you up later, I thought we'd have chicken sticks."
    hide butler
    show jake at char_right
    with dissolve
    jake "What was that?"
    count "Internal line"
    hide jake with dissolve
    show butler at char_right
    with dissolve
    show pliers at char_centre
    with dissolve
    count "do what needs to be done"
    hide butler with dissolve
    hide pliers with dissolve

    show mike at char_right
    with dissolve
    mike "So when do we meet the missus?"
    hide count 
    show jake at char_left 
    with dissolve
    jake "Never!"
    hide mike with dissolve
    show count at char_right 
    with dissolve
    jake "I'm sorry to have bothered you! We'll be leaving!"
    count "I'm afriad not, you see the door is broken"
    jake "but...we just used it"
    play sound audio.crash
    pause
    count "very recent incident"
    count "Well, it looks like you're here for the night. Why don't you come through to the dining room... for a bite!!!"

    #####scene 4#####
    scene dining_room with slow_dissolve
    show the_narrator at char_right
    with dissolve
    the_narrator "And so our heroes found themselves in a very unexpected situation as they became the dinner guests of their mysterious host. But what would Count Vincent of Stoke-on-Trent be serving?"
    hide the_narrator with dissolve
    show butler at char_left
    with dissolve
    butler "Would you care from some wine?"
    show jake at char_right
    with dissolve
    jake "yes, white please"
    butler "I'm sorry, we only have red"
    hide butler with dissolve
    show mike at char_left
    with dissolve
    mike "So why do you live in this neck of the woods anyway?"
    hide jake with dissolve
    show count at char_right
    with dissolve
    count "Oh, its such a terrible story..."
    count "Oh, its such a terrible story..."
    hide count with dissolve
    hide mike with dissolve
    show butler at char_centre
    with dissolve
    butler "Allow me to pour, sirs."
    show jake at char_left
    with dissolve
    jake "Cheers."
    jake "Right, lets tuck in then!"
    
    # Jake reaches for a napkin
    show count at char_right
    with dissolve
    count "Oh! My dear sir, no! That's not for your hands, its for your neck!"
    
    # Jake panics and drops his napkin
    jake "Why do you want us to clean our necks?"
    count "You see, this is the problem! I have... certain ways of doing things... different ways to that of the civilised world."
    count "As a result I was cast out, banished to this house to live out my numbered days alone."
    hide jake with dissolve
    show mike at char_left
    with dissolve
    mike "That's so cruel!"
    hide mike with dissolve
    show jake at char_left
    with dissolve
    jake "Why do you want us to clean our necks?"
    hide jake with dissolve
    show mike at char_left
    with dissolve
    mike "Leave him alone! Can't you see he's just a lonely soul?"
    hide mike with dissolve
    hide count with dissolve
    show jon at char_centre
    with dissolve
    jon "Did you know that the human neck has the same amount of vertebrae as a giraffe's?"
    hide jon with dissolve
    show jake at char_left
    with dissolve
    jake "Does anyone else think there's something funny going on here?"
    hide jake with dissolve
    show mike at char_left
    with dissolve
    mike "The only thing I think is that you can't accept uniqueness in human beings!"
    mike "I bet there's thousands of innocent people like Count Vincent cast out of society merely for daring to question the way it functions!"
    hide mike with dissolve
    show count at char_right
    with dissolve
    count "Please, sirs, do not fight! I want my one rare moment of human contact to be merry!"
    
    # Jake and Mike calm down. Jake takes a mouthful of wine.
    hide count with dissolve
    show jake at char_left
    with dissolve
    jake "*takes a sip of wine*"
    hide jake with dissolve
    show count at char_right
    with dissolve
    count "Now what blood type are you all?"
    
    # Jake spits his wine out
    hide count with dissolve
    show jake at char_left
    with dissolve
    jake "*spits wine out*"
    hide jake with dissolve
    show mike at char_centre
    with dissolve
    mike "Group A!"
    hide mike with dissolve
    show jake at char_left
    with dissolve
    jake "RIGHT! We're out of here!"
    hide jake with dissolve
    show mike at char_centre
    with dissolve
    mike "Forget it! You just think life should be all big boobs and model dinosaurs!"
    hide mike with dissolve
    show jon at char_right
    with dissolve
    jon "Speaking of blood, has anyone ever wondered how a giraffe drinks without causing horrendous blood pressure to its brain?"
    hide jon with dissolve
    show jake at char_left
    with dissolve
    jake "Well at least I'm not so stupid I think the Liverpool Underground is a genre of music!"
    hide jake with dissolve
    show jon at char_right
    with dissolve
    jon "Yes its funny that, isn't it? About the giraffe I mean! One of those little queries that defies evolution."
    hide jon with dissolve
    show mike at char_centre
    with dissolve
    mike "Let me tell you something Saunders!"
    mike "You may think you're the bee's knees just because half the world wants to sleep with you, but people like myself and Count Vincent think there are things we should value more!"
    hide mike with dissolve
    show jon at char_right
    with dissolve
    jon "Woodpeckers also defy evolution. They have a tongue that goes in their necks and behind their skulls, its weird."
    hide jon with dissolve
    show jake at char_left
    with dissolve
    jake "What? Like your gamer score for Call of Duty?"
    hide jake with dissolve
    show jon at char_right
    with dissolve
    jon "Don't worry Jon, I'm listening."
    hide jon with dissolve
    show mike at char_centre
    with dissolve
    mike "Like companionship! And love for your fellow man!"
    hide mike with dissolve
    show jake at char_left
    with dissolve
    jake "Stand back folks, we got a new Jesus here!"
    hide jake with dissolve
    show count at char_centre
    with dissolve
    count "Will you all stop bickering like children! Both of you, sit down!"
    count "Mike, if you really care for my dilemma, then please let this dinner be a happy one!"
    count "Jake, give me a chance. Perhaps you will find that I am not as distasteful as you seem to believe!"
    
    # Jake and Mike sit down slowly
    hide count with dissolve
    show jake at char_left
    show mike at char_right
    with dissolve
    jake "Maybe..."
    
    # Jake and Jon take a mouthful of wine
    hide jake with dissolve
    hide mike with dissolve
    show mike at char_centre
    with dissolve
    mike "What's for dinner anyway Count?"
    hide mike with dissolve
    show butler at char_left
    with dissolve
    butler "Who's for blood pudding?"
    
    # Jake and Jon spit their wine out
    show jake at char_right
    with dissolve
    jake "*spits wine out*"
    
    scene black with dissolve

    ################################################################################
## MINI-GAME VARIABLES
################################################################################

default arrow_step = 0
default inventory_checked = set()
default inventory_found_bible = False

define arrow_positions = [
    (200, 500, 0, "#ffffff"),
    (500, 450, -15, "#ffcccc"),
    (800, 550, 10, "#ff9999"),
    (1100, 480, -20, "#ff6666"),
    (1400, 520, 0, "#ff0000"),
]

################################################################################
## MINI-GAME SCREENS
################################################################################

screen arrow_trail():
    if arrow_step < len(arrow_positions):
        $ x, y, rot, col = arrow_positions[arrow_step]
        imagebutton:
            idle Transform("images/cg/arrow.png", rotate=rot, matrixcolor=TintMatrix(col))
            hover Transform("images/cg/arrow.png", rotate=rot, matrixcolor=TintMatrix(col), zoom=1.1)
            xpos x ypos y
            action [SetVariable("arrow_step", arrow_step + 1), Return()]

screen inventory_check():
    frame:
        xalign 0.5
        yalign 0.5
        background "#000000cc"
        padding (40, 40)
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "{size=40}{color=#ffffff}Check Jon's bag...{/color}{/size}" xalign 0.5
            
            hbox:
                spacing 30
                xalign 0.5
                
                if "stake" not in inventory_checked:
                    imagebutton:
                        idle "images/cg/stake.png"
                        hover Transform("images/cg/stake.png", zoom=1.1)
                        action [AddToSet("inventory_checked", "stake"), Jump("inv_stake")]
                
                if "garlic" not in inventory_checked:
                    imagebutton:
                        idle "images/cg/garlic.png"
                        hover Transform("images/cg/garlic.png", zoom=1.1)
                        action [AddToSet("inventory_checked", "garlic"), Jump("inv_garlic")]
                
                if "water" not in inventory_checked:
                    imagebutton:
                        idle "images/cg/holy_water.png"
                        hover Transform("images/cg/holy_water.png", zoom=1.1)
                        action [AddToSet("inventory_checked", "water"), Jump("inv_water")]
                
                imagebutton:
                    idle "images/cg/bible.png"
                    hover Transform("images/cg/bible.png", zoom=1.1)
                    action [SetVariable("inventory_found_bible", True), Jump("inv_bible")]

screen bible_words():
    frame:
        xalign 0.5
        yalign 0.5
        background "#000000cc"
        padding (40, 40)
        
        vbox:
            spacing 30
            xalign 0.5
            
            text "{size=35}{color=#ffffff}Pick the holiest word to read aloud...{/color}{/size}" xalign 0.5
            
            hbox:
                spacing 25
                xalign 0.5
                
                textbutton "{size=40}{color=#ffdddd}sandwich{/color}{/size}":
                    action Jump("bible_sandwich")
                textbutton "{size=40}{color=#ffdddd}badger{/color}{/size}":
                    action Jump("bible_badger")
                textbutton "{size=40}{color=#ffff00}righteous{/color}{/size}":
                    action Jump("bible_correct")
                textbutton "{size=40}{color=#ffdddd}biscuit{/color}{/size}":
                    action Jump("bible_biscuit")

################################################################################
## MAIN STORY — picks up after your existing Scene 4 (dining room)
################################################################################

label scene_five_bedroom:
    scene bedroom with slow_dissolve
    show the_narrator at char_centre
    with dissolve
    the_narrator "*munching on a sandwich*"
    
    # Prompt is off-screen — we'll just have a "voice" line
    "{i}(A hissed whisper from off-stage){/i}" "The dinner engagement was certainly a curiosity!"
    
    the_narrator "Oh yes! Thank you!"
    the_narrator "The dinner engagement was certainly a curiosity, but what happened when the gang were shown to their room was the strangest occurrence yet."
    hide the_narrator with dissolve
    
    show butler at char_left
    show jake at char_right
    with dissolve
    butler "Here we are good sirs. You'll be happy to know that this room contains the best beds in the house."
    hide jake with dissolve
    show jon at char_centre
    show mike at char_right
    with dissolve
    jake "Where are they?"
    butler "Oh, well, there aren't actually beds of course! The master doesn't use beds!"
    mike "Oh, this is another quirk isn't it! What does he sleep in?"
    butler "Coffin!"
    show jake at char_right
    with dissolve
    jake "Excuse me?"
    butler "Coughing!"
    butler "Because I haven't had my pills! Excuse me, I must go."
    hide butler with dissolve
    
    mike "Well he certainly is enigmatic this Vincent! A man after my own heart!"
    jake "Oh please, the only thing enigmatic about you is the smell after a curry!"
    
    hide jake
    hide jon
    with dissolve
    mike "Coo! Wonder what's in here?"
    hide mike with dissolve
    
    # Mike enters cupboard — off-screen scream
    play sound "audio/sfx/horn.ogg"  # placeholder scream sound
    
    show mike_no_trousers at char_centre
    with dissolve
    mike "*screams*"
    
    show jon at char_left
    with dissolve
    jon "Was that the lion or the witch?"
    mike "There's a bat in there!"
    
    bat "Terribly sorry old boy, you rather startled me!"
    jon "What happened to your trousers Mike?"
    bat "Oh they're here! Sorry I appear to have made a bit of a hole in them!"
    
    show jake at char_right
    with dissolve
    jake "Oh for goodness sake can we just GO TO SLEEP?"
    mike "Bit warm isn't it?"
    jake "Go ask the Butler for a fan then!"
    mike "Excuse me Butler... can we have a fan my good man?"
    jake "Mike, don't rhyme everything!"
    mike "I'm not!"
    mike "It's really hot!"
    jake "MIKE!"
    mike "So if you could bring one in right away, would that be okay?"
    jake "I'm gonna kill you!"
    
    mike "Great face Jake! Let me take a snap chat!"
    
    # The phone reveal moment
    jake "What's that?"
    mike "My phone!"
    jake "You said you didn't have a phone!"
    mike "Well, not the sort you make calls on!"
    
    show the_narrator at char_centre
    with dissolve
    the_narrator "I told you he had a phone!"
    the_narrator "And that's why he didn't tell anyone!"
    hide the_narrator with dissolve
    
    # Cricket bat mini-beating — just a sound gag for now
    play sound "audio/sfx/horn.ogg"  # placeholder thwack
    jake "*grabs a cricket bat that has appeared from nowhere*"
    jake "GET OUT!"
    hide mike_no_trousers with dissolve
    jake "And stay out!"
    
    bat "I say, it's rather stuffy in here!"
    
    hide jake with dissolve
    show jake at char_left
    show jon at char_right
    with dissolve
    jon "Is everything alright man? You seem a bit on edge today!"
    jake "I'm fine mate, its just... well... its been two days since I last... y'know!"
    jon "Y'know?"
    jake "Yeh... y'know!"
    jon "Oh, I know!"
    
    # Awkward pause
    pause 1.5
    jon "..."
    
    hide jake
    hide jon
    with dissolve
    
    jump scene_six_arrows

################################################################################

label scene_six_arrows:
    scene lobby with slow_dissolve
    show mike_no_trousers at char_centre
    with dissolve
    
    aud "Shelly?"
    shelly "What?"
    aud "Nothing!"
    
    play sound "audio/sfx/horn.ogg"  # placeholder boys laughing
    
    mike "...what was that?"
    mike "Oh! An arrow on the wall. How helpful!"
    hide mike_no_trousers with dissolve
    
    $ arrow_step = 0
    
    scene lobby
    show mike_no_trousers at char_left
    call screen arrow_trail
    
    show mike_no_trousers at char_left
    mike "...okay, another one. Sure, why not."
    hide mike_no_trousers
    scene lobby
    show mike_no_trousers at char_centre
    call screen arrow_trail
    
    show mike_no_trousers at char_centre
    mike "These arrows are getting a bit... red."
    hide mike_no_trousers
    scene lobby
    show mike_no_trousers at char_centre
    call screen arrow_trail
    
    show mike_no_trousers at char_centre
    mike "I'm sure this is fine."
    hide mike_no_trousers
    scene lobby
    show mike_no_trousers at char_right
    call screen arrow_trail
    
    show mike_no_trousers at char_right
    mike "Definitely fine."
    hide mike_no_trousers
    scene lobby
    show mike_no_trousers at char_right
    call screen arrow_trail
    
    # End of trail — Mike meets the Count
    scene lobby with dissolve
    show mike_no_trousers at char_left
    show count at char_right
    with dissolve
    mike "HellO!"
    
    play sound "audio/sfx/horn.ogg"  # placeholder bite sound
    
    hide mike_no_trousers with dissolve
    count "*cackles*"
    hide count with dissolve
    
    jump scene_seven_intermission

################################################################################

label scene_seven_intermission:
    scene black with dissolve
    play music "audio/music/intermission.ogg"
    
    centered "{size=80}{color=#ffffff}INTERMISSION{/color}{/size}"
    
    shelly "Right. Queue here for ice cream! Tell me what flavor you want and I'll get it for you... so long as you ask for vanilla. If you don't then you can hop it!"
    aud "Shelly?"
    
    play sound "audio/sfx/horn.ogg"  # placeholder smack
    
    posh "Steward? This is worse than their Doctor Who series!"
    steward "Well you keep watching them ma'am, what right have you to complain?"
    shelly "Alright everyone back to your seats, its coming on again!"
    posh "That was fast!"
    
    stop music fadeout 1.0
    
    jump scene_eight_chase

################################################################################

label scene_eight_chase:
    scene lobby with slow_dissolve
    show jake at char_left
    show jon at char_right
    with dissolve
    jake "Mike?"
    jon "We got your trousers!"
    
    show mike_no_trousers at char_centre
    with dissolve
    jon "What you doing down there lad?"
    jake "Get up you silly twit!"
    
    mike "Hi Dave!"
    jon "No! We're Jon and Jake. Dave died last year remember!"
    mike "Did he?"
    jon "Yeh, you killed him, remember?"
    
    # Count enters with dramatic effect
    play sound "audio/sfx/horn.ogg"  # placeholder thunder/piano sting
    show count_bloody at char_right
    with vpunch
    
    jon "Oh! He's a vampire! I get it now!"
    
    # Quick chase montage — using flashes and shakes
    hide jake
    hide jon
    hide mike_no_trousers
    hide count_bloody
    with dissolve
    
    show the_narrator at char_centre
    with dissolve
    the_narrator "{i}*a chaotic chase sequence ensues*{/i}"
    the_narrator "You know what one of the worst things you can do in film making is? Having a really dramatic scene and then switching it to something completely different!"
    hide the_narrator with dissolve
    
    jump scene_nine_forest

################################################################################

label scene_nine_forest:
    scene forest_night with slow_dissolve
    show tom at char_centre
    with dissolve
    tom "*reading a Beano, sipping a drink*"
    tom "Wonder where the others got to..."
    hide tom with dissolve
    
    jump scene_ten_butler

################################################################################

label scene_ten_butler:
    scene lobby with slow_dissolve
    show tom at char_centre
    with dissolve
    tom "Hello?"
    tom "Ooh, a bottle of whiskey on a giant red X. That's not suspicious at all."
    
    show butler at char_left
    with dissolve
    play sound "audio/sfx/horn.ogg"  # placeholder thwack
    
    tom "What was that for?"
    hide tom with dissolve
    hide butler with dissolve
    
    jump scene_eleven_cupboard

################################################################################

label scene_eleven_cupboard:
    scene bedroom with slow_dissolve
    show jake at char_left
    show jon at char_right
    with dissolve
    jake "*panting*"
    jon "*also panting*"
    
    jake "In here!"
    jon "Won't open!"
    jake "Fiddle with the nob."
    jon "I don't like fiddling with the nob!"
    jake "Let me do it then!"
    
    hide jake with dissolve
    jon "*to camera*"
    jon "Going in the closet!"
    hide jon with dissolve
    
    bat "Oh hello!"
    
    # Plastic bat gets thrown out
    show plastic_bat_toy at char_centre
    with vpunch
    pause 0.5
    hide plastic_bat_toy with dissolve
    
    # Inside the cupboard
    scene black with dissolve
    show jake at char_left
    show jon at char_right
    with dissolve
    jake "Well this is a bit camp!"
    jon "Woah! Don't press down on my stomach!"
    jake "Why not?"
    
    play sound "audio/sfx/horn.ogg"  # placeholder fart
    pause 1.0
    
    # Inventory mini-game
    call cupboard_inventory
    
    jump scene_twelve_bible

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
    
    $ inventory_checked = set()
    $ inventory_found_bible = False

label inv_loop:
    call screen inventory_check
    return

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
    hide jake
    hide jon
    with dissolve
    return

################################################################################

label scene_twelve_bible:
    scene bedroom with slow_dissolve
    show count_bloody at char_centre
    with dissolve
    count "*looking around fruitlessly*"
    hide count_bloody with dissolve
    
    # Jon pops out
    show jon at char_left
    show count_bloody at char_right
    with dissolve
    jon "Oh hello! Was wondering if you'd like to hear this."
    
    hide jon
    hide count_bloody
    with dissolve
    
    # Bible mini-game
    call holy_word_game
    
    # After the mini-game ends, Count is collapsed (just hidden)
    show jake at char_left
    show jon at char_centre
    with dissolve
    jake "He gone then?"
    
    show count_happy at char_right
    with dissolve
    count "Hallelujah! Its a miracle! The evil within me has been purged."
    count "I'm free! I feel so alive! I just want to sing!"
    jake "Please don't!"
    count "Oh what a beautiful morning! Oh what a beautiful day!"
    count "I've got a wonderful feeling, everything's going my..."
    
    show butler at char_left
    with dissolve
    play sound "audio/sfx/horn.ogg"  # placeholder thwack
    
    hide count_happy with dissolve
    hide butler with dissolve
    
    jon "Well, I think everything turned out alright!"
    jon "I suppose you'll be off to... y'know... then... with that girl you mentioned earlier?"
    jake "Urr.. I don't think she plays Pokemon!"
    
    # Bomb ticking starts
    play sound "audio/sfx/horn.ogg" loop  # placeholder tick
    
    jon "Pokemon? Oh! It's that sort of... y'know..."
    jake "What sort of... y'know... did you think I meant!"
    jon "Oh... never mind!"
    jake "JON! You really have a filthy mind! And another thing, what's that ticking noise?"
    jon "Oh that'll be the bomb I mentioned!"
    jake "Oh right!"
    
    show bomb at char_centre
    with dissolve
    jake "Flip!"
    
    stop sound
    play sound "audio/sfx/carsh.mp3"  # using your existing crash sound for explosion
    
    scene black with flash
    pause 1.0
    
    jump scene_thirteen_wreckage

################################################################################

label holy_word_game:
    scene bedroom with dissolve
    show jon at char_left
    show count_bloody at char_right
    with dissolve
    jon "*flips through the bible*"
    jon "Hmm... which bit is holiest..."
    hide jon
    hide count_bloody
    with dissolve
    
    call screen bible_words

label bible_sandwich:
    show jon at char_left
    show count_bloody at char_right
    with dissolve
    jon "\"...and Jesus did eat of the sandwich...\""
    count "...I'm sorry, is this going somewhere?"
    hide jon
    hide count_bloody
    with dissolve
    jump holy_word_retry

label bible_badger:
    show jon at char_left
    show count_bloody at char_right
    with dissolve
    jon "\"...and lo, the badger was upon him...\""
    count "That's not in the Bible."
    jon "It might be in the apocrypha!"
    count "It really isn't."
    hide jon
    hide count_bloody
    with dissolve
    jump holy_word_retry

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
    jump holy_word_retry

label holy_word_retry:
    show jon at char_left
    with dissolve
    jon "Let me try a different bit..."
    hide jon with dissolve
    call screen bible_words

label bible_correct:
    show jon at char_left
    show count_bloody at char_right
    with dissolve
    jon "\"...the Lord watches over the way of the righteous...\""
    
    play sound "audio/sfx/horn.ogg"  # placeholder fire whoosh
    hide count_bloody
    show count_on_fire at char_right
    with dissolve
    
    jon "Oh gosh! Sorry!"
    count "What was that for???"
    jon "Well... y'know... you where trying to suck our blood!"
    count "Look! I'm a vampire! I have to! There was no need for that!"
    
    hide count_on_fire with dissolve
    jon "I'm really sorry, I didn't mean to..."
    hide jon with dissolve
    return

################################################################################

label scene_thirteen_wreckage:
    scene bedroom_wreckage with slow_dissolve
    show jake at char_left
    show jon at char_centre
    show mike_no_trousers at char_right
    with dissolve
    
    jake "Gosh! That was lucky!"
    
    show the_narrator at char_centre
    with dissolve
    the_narrator "And so, our friends survived a night in the scary house."
    the_narrator "And now, with a new mindset and a renewed appreciation for life and all they have been given in it, they looked at the rising sun and spoke the first words of this new dawn..."
    hide the_narrator with dissolve
    
    jake "Let's go the pub!"
    
    scene black with dissolve
    centered "{size=80}{color=#ff0000}{font=fonts/bloody.ttf}END CREDITS{/font}{/color}{/size}"
    pause 3.0
    
    jump scene_fourteen_stinger

################################################################################

label scene_fourteen_stinger:
    scene forest_bright with slow_dissolve
    show count_happy at char_centre
    with dissolve
    count "*skipping happily through the forest*"
    
    show werewolf at char_right
    with vpunch
    play sound "audio/sfx/horn.ogg"  # placeholder werewolf growl
    
    count "Oh! Not again!"
    
    hide count_happy
    hide werewolf
    with dissolve
    
    play sound "audio/sfx/horn.ogg"  # placeholder biting sounds
    pause 2.0
    
    scene black with dissolve
    centered "{size=60}{color=#ff0000}{font=fonts/bloody.ttf}FIN{/font}{/color}{/size}"
    pause 3.0
    
    return