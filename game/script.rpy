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
    play sound audio.rain fadein 0.5 loop
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
    vo "Tom winds the window back up without saying a word"
    play sound audio.window
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

    show mike at char_right
    with dissolve
    mike "  Well, now that we've all agree that something needs to be done."
    hide mike with dissolve

    show tom at char_left
    with dissolve
    vo "Tom whacks the steering wheel again, then sits forward with his head in his hands."
    play sound audio.horn
    $ camera_shake

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
    stop sound fadeout 0.5

    ######################################################
    ####Scene 2####################
    ######################################################

    scene cinema with slow_dissolve
    show aud at char_left
    aud "Shelly!"
    show shelly at char_right
    shelly "What?!"
    aud "What ya doin' after the film?"
    shelly "Nout with you sunshine!"

    ######################################################
    ####Scene 3####################
    ######################################################

    scene scary_door with slow_dissolve  

    


