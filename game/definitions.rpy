init python:
    class Guy:
        def __init__(self, name = "Jim", colorHex = "5500FF", kindMode = adv):
            self.chr = Character(name, color = colorHex, kind = kindMode)
            self.hasMet = False

define whitney = Guy(name = "Whitney")
define potato = Guy(name = "Potato", colorHex = "978351")
define badEnding = Guy(name = None, kindMode = nvl)

transform middlish:
    xalign 0.5
    yalign 0.5

transform leftish:
    xalign 0.25
    yalign 0.5

transform rightish:
    xalign 0.75
    yalign 0.5
