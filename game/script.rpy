# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character(_("Kai"), color="#aa6f73")
define m = Character(_("Marlon"), color="#7e6a7c")
define s = Character(_("Spike"), color="#ac330f")
define o = Character(_("Otis"), color="#f9d62e")
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
            $ herself = "himself"
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

label morning:

    show bg kai bedroom
    #It is morning and we see a still image of Kai's bedroom. They ponder.

    "Feels like home away from home. Well except for the part where I don't remember what or where home is. Good morning, me!"
    
    show bg phone
    #The phone is rendered over the image of Kai's bedroom. Navigate to two text messages.
    
    k "Text messages already? {i}Guuuuuuh{/i}, it's too early to socialize."
    k "Marlon and Spike? What do they want?"

    menu:
        "Read Marlon's text":
            jump Marlontextconvo
        "Read Spike's text":
            jump Spiketextconvo

label Marlontextconvo:
    show bg phone marlon text

    m "omg did u watch the new episode of Trashy Cryptids Trash America?"
    m "this new season is lit"
    m "ester is my faveeeee" 
   
    menu:
        m "u up?"

        "Yes, I'm awake and kicking.":
            jump m_excited_text
        "No, still sleeping.":
            jump m_nervous

        "What's Trashy Cryptids?":
            jump m_question

label m_excited_text:
    k "Yeah, I'm awake and kicking it."
    m "perf, i wanna meet up"
    m "m i gotta catch you up on the new trashy cryptids season {image=peach_emoji.png}"

    jump m_invite

label m_nervous:
    k "No, I'm still sleeping"
    m "how u texting if you're asleep?"
    k "It's one of the world's greatest mysteries I guess"
    m "lol" 
    m "i gotta catch you up on the new trashy cryptids season {image=peach_emoji.png}" #An emoji appears.

    jump m_invite

label m_question:
    k "What's Trashy Cryptids?"
    m "UMMMMM"
    m "only the best trashiest reality tv show! don't tell me u forgot"
    m "ima change that"

    jump m_invite

label m_invite:
    m "lets meet up. park?"

    menu:
        "Maybe {image=poop_emoji.png}":
            jump m_poop

        "Maybe {image=unicorn_emoji.png}":
            jump m_unicorn
        
        "Maybe {image=eggplant_emoji.png}":
            jump m_eggplant

label m_poop:
    k "Maybe {image=poop_emoji.png}" #An emoji appears.
    m "lol rude"
    m "meet me by the water fountain if ur there {image=basicsmile_emoji.png}" #An emoji appears.

    jump parkentrance

label m_unicorn:
    k "Maybe {image=unicorn_emoji.png}" #An emoji appears.
    m "you know i have a fear of unicorns {image=basicfrown_emoji.png}" #An emoji appears.
    m "meet me by the water fountain if ur there"

    jump parkentrance

label m_eggplant:
    k "Maybe {image=eggplant_emoji.png}"
    m "lollllll ur g8"
    m "missed u like a lot a lot"
    m "meet me by the water fountain if ur there"

    jump parkentrance

label Spiketextconvo:
#Emily, you can continue here.

label parkentrance:

    show bg park entrance
    #We see the entrance of the park with its three paths.

    "Well, I made it. It's a beautiful day. The sky is grey, the bird are screaming, and the air smells like fish and chips."
    "Hmm, both Marlon and Spike wanted to meet up. The water fountain is toward the left. That's where Marlon is. I think I see Spike over toward the right."
    "I could always just explore on my own for a bit before meeting up with them."

    menu:
        "Left towards Marlon":
            jump Marlonparkconvo

        "Right towards Spike":
            jump Spikeparkconvo
        
        "Enter park center":
            jump Otisparkconvo

label Marlonparkconvo:

label Spikeparkconvo:
#Emily, this is for you!
