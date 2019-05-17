# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kai")
define m = Character("Marlon")
define s = Character("Spike")
default Her = "Her"
default her = "her"
default She = "She"
default she = "she"
default Hers = "Hers"
default hers = "hers"
default Herself = "Herself"
default herself = "herself"


define e = Character("Eileen")

label start:
    menu:
        "Are you a boy or a girl?"
        "I'm a boy. (he/him)":
            $ Her = Hers = "His"
            $ her = hers ="his"
            $ She = "He"
            $ she = "he"
            $ Herself = "Himself"
            $ herself = "herself"
        "I'm a girl. (she/her)":
            pass
        "I'm a detective. (ze/zir)":
            $ Her = "Zir"
            $ her = "zir"
            $ Hers = "Zirs"
            $ hers = "zirs"
            $ She = "Ze"
            $ she = "ze"
            $ Herself = "Zirself"
            $ herself = "Zirself"

    "[She] went to the park. I went with [her]. [She] brought [her] frisbee. At least I think it was [hers]. [She] threw the frisbee to [herself]."
    "I helped darlene with [her] first commit."
