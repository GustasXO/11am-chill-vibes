input.onButtonPressed(Button.AB, function () {
    basic.showString("Be Urself :)")
})
input.onButtonPressed(Button.B, function () {
    basic.showString("Ur perfect :)")
})
basic.showLeds(`
    # . # . #
    # . # . .
    # # # . #
    # . # . #
    # . # . #
    `)
basic.pause(2000)
basic.showIcon(IconNames.Heart)
basic.pause(1000)
basic.showIcon(IconNames.Happy)
loops.everyInterval(500, function () {
    basic.showString("Just relax :)")
    basic.pause(1000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.pause(500)
    basic.showIcon(IconNames.SmallDiamond)
    basic.pause(500)
    basic.showIcon(IconNames.Diamond)
    basic.pause(2000)
    basic.showIcon(IconNames.SmallDiamond)
    basic.pause(500)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
})
