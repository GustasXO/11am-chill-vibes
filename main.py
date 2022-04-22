def on_button_pressed_a():
    basic.show_string("Just relax :)")
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.pause(500)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.pause(500)
    basic.show_icon(IconNames.DIAMOND)
    basic.pause(2000)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.pause(500)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("Be Urself :)")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("Ur perfect :)")
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_leds("""
    # . # . #
        # . # . .
        # # # . #
        # . # . #
        # . # . #
""")
basic.pause(2000)
basic.show_icon(IconNames.HEART)
basic.pause(1000)
basic.show_icon(IconNames.HAPPY)