################################################################################
## SCRIPT.RPY - Main Game Script
## Scenes 1-4 only. Act 2 (Scenes 5-14) lives in script_act2.rpy.
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

    ## --- Rhythm minigame setup (runs once before the retry loop) ---
    ## FIX: these lines must be indented inside label start, not at column 1.
    stop music fadeout 0.3
    $ renpy.stop_predict()
    $ renpy.block_rollback()
    $ renpy.restart_interaction()
    stop movie

    show layer master at disco_lights

    ## Show intro screen first
    $ renpy.call_screen("rhythm_intro_screen")

    ## IMPORTANT: reset interaction so countdown can animate
    $ renpy.restart_interaction()

    ## Countdown before the game begins
    $ rhythm_countdown()
    jump rhythm_retry

## rhythm_retry is a top-level label so the player can reload a save here.
## The rhythm setup above (inside label start) only runs once.
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

    ## --- Achievement if perfect score ---
    ## FIX: this block must be indented inside label rhythm_retry, not at column 1.
    if rhythm_result["perfect"]:
        $ disco_fever.grant()
    jump after_rhythm

## after_rhythm continues the story once the disco sequence is done.
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

    ## Jake reaches for a napkin
    show count at char_right
    with dissolve
    count "Oh! My dear sir, no! That's not for your hands, its for your neck!"

    ## Jake panics and drops his napkin
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

    ## Jake and Mike sit down slowly
    hide count with dissolve
    show jake at char_left
    show mike at char_right
    with dissolve
    jake "Maybe..."

    ## Jake and Jon take a mouthful of wine
    hide jake with dissolve
    hide mike with dissolve
    show mike at char_centre
    with dissolve
    mike "What's for dinner anyway Count?"
    hide mike with dissolve
    show butler at char_left
    with dissolve
    butler "Who's for blood pudding?"

    ## Jake and Jon spit their wine out
    show jake at char_right
    with dissolve
    jake "*spits wine out*"

    scene black with dissolve
    ## FIX: jump added here — scene 4 was previously a dead end.
    jump scene_five_bedroom
