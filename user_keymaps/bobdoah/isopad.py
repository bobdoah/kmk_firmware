from kb import KMKKeyboard

from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.tapdance import TapDance

Isopad = KMKKeyboard()

tapdance = TapDance()
tapdance.tap_time = 750
Isopad.modules.append(tapdance)

SHIP_IT = simple_key_sequence(
    (
        KC.COLON,
        KC.S,
        KC.H,
        KC.I,
        KC.P,
        KC.I,
        KC.T,
        KC.COLON,
        KC.MACRO_SLEEP_MS(500),
        KC.ENTER,
    )
)

THIS_IS_FINE = simple_key_sequence(
    (
        KC.COLON,
        KC.T,
        KC.H,
        KC.I,
        KC.S,
        KC.MINUS,
        KC.I,
        KC.S,
        KC.MINUS,
        KC.F,
        KC.I,
        KC.N,
        KC.E,
        KC.MINUS,
        KC.F,
        KC.I,
        KC.R,
        KC.E,
        KC.COLON,
        KC.MACRO_SLEEP_MS(500),
        KC.ENTER,
    )
)


Isopad.keymap = [[KC.TD(
    KC.ENTER,
    SHIP_IT,
    THIS_IS_FINE,
)]]

if __name__ == '__main__':
    Isopad.go()
