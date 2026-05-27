## Wheel ##

screen hit_the_wheel():
    modal True

    frame:
        xalign 0.5 yalign 0.5
        padding (60, 50)
        background Frame("gui/frame.png", 60, 60, 60, 60)

        has vbox
        spacing 24
        xalign 0.5

        text "Tom stares at the steering wheel.":
            xalign 0.5
            italic True
            color "#aaaaaa"
            size 28

        imagebutton:
            xalign 0.5
            idle Transform("images/ui/wheel.png", zoom=0.5)
            hover Transform("images/ui/wheel.png", zoom=0.5)
            action [
                SetVariable("wheel_hits", wheel_hits + 1),
                SetVariable("wheel_phrase",
                    wheel_phrases[(wheel_hits) % len(wheel_phrases)]),
                Play("sound", audio.horn),
        ]

        if wheel_phrase:
            text "[wheel_phrase]":
                xalign 0.5
                color "#ffffff"
                size 32
                italic True

        if wheel_hits > 0:
            textbutton "...I'm done.":
                xalign 0.5
                action Return()
                text_color "#888888"
                text_hover_color "#ffffff"

## bell ###

default bell_hits = 0

screen ring_the_bell():
    modal True

    frame:
        xalign 0.5 yalign 0.5
        padding (60, 50)
        background Frame("gui/frame.png", 60, 60, 60, 60)

        has vbox
        spacing 24
        xalign 0.5

        text "Jake reaches for the doorbell.":
            xalign 0.5
            italic True
            color "#aaaaaa"
            size 28

        imagebutton:
            xalign 0.5
            idle At("images/ui/bell.png", Transform(zoom=0.5))
            hover At("images/ui/bell.png", Transform(zoom=0.5))
            action [
                Play("sound", audio.bell),
                SetVariable("bell_hits", bell_hits + 1),
            ]

        if bell_hits > 0:
            textbutton "...Nobody Home":
                xalign 0.5
                action Return()
                text_color "#888888"
                text_hover_color "#ffffff"

## Chase QTE ###
## Called three times from label chase_minigame with different prompts.
## Returns "a" or "b" via _return.

screen chase_choice(prompt_text, choice_a, choice_b):
    modal True

    ## Red panic tint laid over the lobby background.
    add Solid("#33000099")

    frame:
        xalign 0.5 yalign 0.35
        padding (60, 50)
        background Frame("gui/frame.png", 60, 60, 60, 60)

        has vbox
        spacing 24
        xalign 0.5

        text prompt_text:
            xalign 0.5
            color "#ff4444"
            size 32
            bold True

        null height 10

        hbox:
            spacing 60
            xalign 0.5

            textbutton choice_a:
                action Return("a")
                text_size 24
                text_color "#cccccc"
                text_hover_color "#ffffff"

            textbutton choice_b:
                action Return("b")
                text_size 24
                text_color "#cccccc"
                text_hover_color "#ffffff"