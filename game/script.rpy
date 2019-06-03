# The script of the game goes in this file.

# Define character affection stats
default marlon_friend_score = 0
default spike_friend_score = 10

# define various states the player may trigger
default game_state = {
    'morning_phone_texts' : [0,0], #Marlon \ Spike
    'current_location' : 'home',
    'can_map_travel' : False
}

default morning_phone_texts = [0,0]
default unicorn_marlon = False
default spike_visited = False
default marlon_visited = False
default otis_visited = False
default trash_tv_topics = [0,0]
default marlon_maze_topics = [0,0,0,0,0,0,0]
default s_photo_park = False

#Define puzzle states
default maze_progress = 0

# Set up horror flicker
default blink_timer = renpy.random.random()

init python:
    def blink(trans, st, at):
        global blink_timer

        if st >= blink_timer:
            blink_timer = renpy.random.random()
            return None
        else:
            return 0

image no_flicker:
    "madrona_light.png"

image flicker_one:
    "madrona_light.png"
    function blink
    "madrona_dark.png"
    pause 0.02
    "madrona_light.png"
    pause 0.02
    "madrona_dark.png"
    function blink
    repeat

image flicker_two:
    "madrona_light.png"
    pause 0.05
    "madrona_dark.png"
    function blink
    "madrona_gore.png"
    pause 0.02
    "madrona_dark.png"
    pause 0.5
    "madrona_gore.png"
    function blink
    "madrona_light.png"
    pause 0.08
    "madrona_dark.png"
    pause 0.3
    repeat

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character(_("Kai"), color="#aa6f73")
define m = Character(_("Marlon"), color="#7e6a7c")
define s = Character(_("Spike"), color="#ac330f")
define mt = Character(_("[[Marlon]"), color="#7e6a7c")
define st = Character(_("[[Spike]"), color="#ac330f")
define o = Character(_("Otis"), color="#f9d62e")

#define companion
default Companion = "{size=+20}ERROR{/size}"

#define pronouns
default Her = "Her"
default her = "her"
default She = "She"
default she = "she"
default Hers = "Hers"
default hers = "hers"
default Herself = "Herself"
default herself = "herself"

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
            $ herself = "zirself"

    "[She] went to the park. I went with [her]. [She] brought [her] frisbee. At least I think it was [hers]. [She] threw the frisbee to [herself]."

label morning:

    show bg kai bedroom
    #It is morning and we see a still image of Kai's bedroom. They ponder.

    "Feels like home away from home. Well except for the part where I don't remember what or where home is. Good morning, me!"

    # TODO: phone buzz noise?

    k "Text messages already? {i}Guuuuuuh{/i}, it's too early to socialize."
    k "Marlon and Spike? What do they want?"

label open_phone:
    show screen phone_pop_but(game_state)

    k "Guess I need to take a look."
    k "..."
    k "If I reach over to my phone I can look at those juicy, juicy texts."
    k "..."
    k "..."
    k "Just gotta reeeeeaaaaach with my *ahem* {i}hand{/i}, and {i}click{/i} I mean-"
    k "{i}{b}GRAB{/b}{/i}"
    k "my phone."
    k "..."
    k "..."
    k "..."
    jump open_phone

label phone_hold_two:
    $ game_state['can_map_travel'] = True
    hide phone texts
    show screen phone_pop_but(game_state)
    k "Okay, cool."
    k "I can head to the park now."
    if game_state['morning_phone_texts'][0] == 0:
        k "Or I can see what's up with Marlon."
    elif game_state['morning_phone_texts'][1] == 0:
        k "Or I could see what Spike wants."
    k "If I want to go to the park, I should probably look up directions on my phone."
    ""
    jump phone_hold_two

label homefornoreason:
    show bg kai bedroom
    $ game_state['current_location'] = 'home'
    "Why did I come back home?"
    "..."
    "I'm so boooorrrrreeeeed."
    "..."
    "...\n..."
    jump homefornoreason


label Marlontextconvo:
    hide screen phone_pop_but
    $ game_state['morning_phone_texts'][0] = 1
    show phone texts

    m "omg did u watch the new episode of Trashy Cryptids Trash America?"
    m "this new season is lit"
    m "Eileen is my love 5eva"

    menu:
        m "u up?"
        "{image=emoji/basicsmile_emoji.png} Yes, I'm awake":
            jump m_excited_text
        "{image=emoji/basicfrown_emoji.png} No, still sleeping":
            jump m_sleepy
        "{image=emoji/peach_emoji.png} What's Trashy Cryptids?":
            jump m_question

label m_excited_text:
    k "Yeah, I'm alive and kicking it."
    m "perf, let's meet up"
    m "m i gotta catch you up on the new trashy cryptids season {image=emoji/peach_emoji.png}"
    jump m_invite

label m_sleepy:
    k "No, I'm still sleeping"
    m "how u texting if ur asleep?"
    k "It's one of the world's greatest mysteries I guess"
    m "lol"
    m "i gotta catch you up on the new trashy cryptids season {image=emoji/peach_emoji.png}" #An emoji appears.
    jump m_invite

label m_question:
    k "What's Trashy Cryptids?"
    m "UMMMMM"
    m "only the best trashiest reality tv show! {image=emoji/hearteyes_emoji.png}"
    m "don't tell me u forgot"
    m "ima change that"

    jump m_invite

label m_invite:
    m "lets meet up. park?"

    menu:
        "{image=emoji/poop_emoji.png} Maybe":
            jump m_poop

        "{image=emoji/unicorn_emoji.png} If you insist":
            jump m_unicorn

        "{image=emoji/eggplant_emoji.png} Absolutely yes":
            jump m_eggplant

label m_poop:
    k "{image=emoji/poop_emoji.png} Maybe. We'll see how I feel." #An emoji appears.
    m "lol rude"
    m "meet me by the water fountain if ur there {image=emoji/basicsmile_emoji.png}" #An emoji appears.

    jump phone_hold_two

label m_unicorn:
    $ unicorn_marlon = True
    k "{image=emoji/unicorn_emoji.png} Eh, I guess so." #An emoji appears.
    m "ew no u know i don't like unicorns {image=emoji/basicfrown_emoji.png}" #An emoji appears.
    k "You don't?"
    m "they r the woooorst"
    m "anyway meet me by the water fountain if ur there"

    jump phone_hold_two

label m_eggplant:
    k "{image=emoji/eggplant_emoji.png} I'd really like that!"
    m "lollllll buddy ur g8"
    m "missed u like a lot a lot"
    m "meet me by the water fountain if ur there"

    jump phone_hold_two

label Spiketextconvo:
    hide screen phone_pop_but
    show phone texts
    $ game_state['morning_phone_texts'][1] = 1
    s "hey kai!! wake up sleepyhead~*~"
    k "It's still early, Spike..."
    s "time to greet the day ~(^.^~)"
    s "what are your plans?"

    menu:
        "{image=emoji/basicsmile_emoji.png} Explore the town":
            call s_explore_text from _call_s_explore_text
        "{image=emoji/sadfrown_emoji.png} Probably sulk":
            call s_sulk_text from _call_s_sulk_text
        "{image=emoji/wink_emoji.png} Spend time with you":
            call s_wink_text from _call_s_wink_text

    s "wanna meet up? i have time before bball practice this afternoon {image=emoji/sweat_emoji.png}"
    k "...what did you have in mind?"
    s "it's a surprise! you won't regret it :D"
    s "meet me by the park bench in 20"
    s "but don't sit on it :p my invisible friend might be there"
    k "Invisible friend? Don't you mean {i}imaginary{/i} friend?"
    s "nope they're invisible <(^o^)> they hate it when people sit on them"
    s "so can i count on you? {image=emoji/sweat_emoji.png}"

    menu:
        "{image=emoji/thumbsup_emoji.png} See you there!":
            call s_thumbsup_text from _call_s_thumbsup_text
        "{image=emoji/mad_emoji.png} If you insist":
            call s_mad_text from _call_s_mad_text
        "{image=emoji/opensmile_emoji.png} Wouldn't miss it":
            call s_opensmile_text from _call_s_opensmile_text

    jump phone_hold_two

label s_explore_text:
    k "I thought I'd try to explore the town some more and get back into the swing of things"
    k "This is supposed to be my home, but I feel like I know nothing about it"
    s "don't worry! we'll have you right as rain in no time~"
    k "I hope you're right"
    return

label s_sulk_text:
    k "Oh, I thought I would just sulk in bed for a bit, then wander around in an aimless haze"
    s "we can't have any of that! you've got to keep active or your muscles will all shrivel up from disuse (o_O)"
    k "Thanks, Spike. That's a nice thought."
    return

label s_wink_text:
    k "I was actually hoping you had time to hang out today... interested?"
    s "awoo definitely!!"
    s "it's been so long since we had fun like we used to"
    s "~(^o^)~~(^_^)~"
    k "I thought you said I'd only been gone a few days?"
    s "like i said. so. long."
    return

label s_thumbsup_text:
    k "{image=emoji/thumbsup_emoji.png}"
    k "See you there!"
    s "can't wait! i'll be the attractive {image=emoji/wolf_emoji.png} lookin one"
    return

label s_mad_text:
    k "Fine, but I won't be happy about it"
    s "you're no fun :( don't worry, i can fix that!"
    s "see you soon~*~"
    return

label s_opensmile_text:
    k "I wouldn't miss it!"
    k "As long as we don't get seriously injured or something"
    s "just you wait..."
    s "i'll take you to all sorts of places next ;)"
    s "maybe you can help me murder some {image=emoji/tree_emoji.png}{image=emoji/tree_emoji.png}{image=emoji/tree_emoji.png} this weekend :P"
    return

label parkentrance:
    hide screen phone_pop_but
    show bg park main
    #We see the entrance of the park with its three paths.

    "Well, I made it. It's a beautiful day. The sky is grey, the birds are screaming, and the air smells like fish and chips."
    "Hmm, both Marlon and Spike wanted to meet up. The water fountain is toward the left. That's where Marlon is. I think I see Spike over toward the right, by the bench."
    "I could always just explore on my own for a bit before meeting up with them."

label parkentrancemenu:
    $ game_state['can_map_travel'] = True
    $ game_state['current_location'] = 'park'
    show screen phone_pop_but(game_state)
    hide otis neutral
    hide marlon neutral
    hide spike neutral
    show bg park main
    menu:
        "Left towards Marlon":
            hide screen phone_pop_but
            $ game_state['can_map_travel'] = False
            jump Marlonparkconvo

        "Right towards Spike":
            hide screen phone_pop_but
            $ game_state['can_map_travel'] = False
            jump Spikeparkconvo

        "Enter park center" if otis_visited == False:
            hide screen phone_pop_but
            $ game_state['can_map_travel'] = False
            jump otis_park

label otis_park:
    $ otis_visited = True
    show otis neutral
    show bg park fountain_mirror

    o "Hey there, Kai. Kai, the amelioration! How lovely to see you here at the heart of the town. Have you come to admire our famous Port Madrona Tree?"
    k "Uh, right. Hey, to you too... I'm actually here to meet up with one of my friends, but thought I might explore a bit first. What brings you here?"
    show otis explain
    o "Well, as you know, I run the town's grand annual festival to celebrate our beloved Port Madrona tree. I like to check on her often and tend to her. After all, we have a responsibility to protect her, right? We're all connected here."
    hide otis explain
    show otis neutral

    menu:
        "{image=emoji/basicsmile_emoji.png} Absolutely!":
            jump otis_park.k_absolutely
        "{image=emoji/basicfrown_emoji.png} Maybe, but why you?":
            jump otis_park.k_maybe
        "{image=emoji/thumbsup_emoji.png} See you around.":
            jump otis_park.k_seeyou
label .k_absolutely:

    k "Of course! That's really kind of you."
    o "Why, thank you. I just like to do my part. I think I'm just utterly fascinated by our town's history."
    k "It's definitely an interesting place. I take it you must know a lot about it?"
    o "Better than most. However, I won't keep you from your friends. We'll have plenty of time to talk. Come find me in the maze later if you would like to know more."
    k "Okay, but I imagine I'll get there first."
    show otis smirk
    o "We'll see."
    hide otis smirk
    jump parkentrancemenu

label .k_maybe:
    k "I guess, but why you? Are you the chosen one or something?"
    show otis eyebrow raise
    o "Oh Kai, you're full of surprises! You know we choose someone annually to guard the tree year-round, but I have to say, I just don't think anyone could show her the care and attention that I can. Perhaps, it's because I study her needs."
    k "How exactly do you do that?"
    hide otis eyebrow raise
    show otis explain
    o "I make sure her environment is ideal. Make sure she receives water every 10 - 14 days until the soil is moist at a depth of just 6-inches. I prune any dead limbs, trim the outer foliage, and spray in the early spring to kill any insects or larvae that may have nested during the winter months. It's quite simple, really."
    hide otis explain
    show otis neutral
    k "Right.."
    hide otis neutral
    jump parkentrancemenu

label .k_seeyou:

    k "Yeah, sounds good. I'll see you around."
    o "Of course. Come find me in the maze later if you would like to hear more about our enchanting Port Madrona tree."
    hide otis neutral
    jump parkentrancemenu


label Marlonparkconvo:
    show bg park fountain
    if marlon_visited == False:
        $ marlon_visited = True
        show marlon neutral
        m "Oh looky loo. You made it! What took you so long?"
        if spike_visited == True:
            jump m_talked_to_spike
        else:
            jump m_long_morning
    else:
        show marlon neutral
        m "[She]'s back!"
        jump Marlonparkmenu


label m_talked_to_spike:

    k "I met up with Spike real quick before meeting up with you."
    m "Fun! I love Spike. It's all 'awoooos' and sweat with her."

    jump m_kai_weird_greetings

label m_long_morning:

    k "It's been a hectic morning."
    m "Oh no buddy! Why's that?"

    jump m_kai_weird_greetings

label m_kai_weird_greetings:
    k "I felt weird walking over here. Everybody was greeting me."
    k "'Morning, Kai!' and 'Great to see you Kai!'  Everyone was so kind and happy…"
    m "Yep, everyone knows you. And they like you!"
    k "But I don't remember anybody. I remember nothing."
    m "Nothing? Not the time we summoned a banshee in the school cafeteria?"
    k "Nope."
    m "Or the time we covered the statue in front of town hall in glitter?"
    k "Was that one your idea?"
    m "Oh {i}absoluuuuuuutely{/i}."
    k "None of that sounds familiar. Something...{size=-10}someone?{/size}...stuffed my mind into a blender and pressed the smoothie button."
    m "That's disgusting and… a little cool. {p=1.0} You'll remember something! I'm unforgettable after all."
    k "Thanks, Marlon."
    m "I can answer anything for you if you want. I got ALL the dirt."

    jump Marlonparkmenu

label Marlonparkmenu:
    menu:
        "{image=emoji/opensmile_emoji.png} Tell me about you." if trash_tv_topics[0] == 0 | trash_tv_topics[1] == 0:
            jump m_aboutMarlon
        "{image=emoji/basicsmile_emoji.png} Tell me about The Glow.":
            jump m_aboutGlow
        "{image=emoji/eyeroll_emoji.png} Let's talk about something else.":
            jump m_somethingelse

label m_aboutMarlon:
    k "What's your thing? What are you all about?"
    m "Trashy Cryptids Trash America obv."
    k "Did you just use 'obv' in real life conversation?"
    m "Yeah. Obv. Eileen is ALL about that I-R-L slang. She is the QUEEEEEEEN."
    k "So, what's this show about?"
    m "So it's a group of five best friends who road trip around America and change people's lives with their weirdness. It's actually very wholesome and everyone has their shit together."
    m "Except for Tia. Tia is a mess."

label TCTA:
    menu:
        "{image=emoji/sweat_emoji.png} Eileen?" if trash_tv_topics[0] == 0:
            $ trash_tv_topics[0] = 1
            jump m_aboutEileen
        "{image=emoji/eggplant_emoji.png} Tia?" if trash_tv_topics[1] == 0:
            $ trash_tv_topics[1] = 1
            jump m_aboutTia
        "{image=emoji/eyeroll_emoji.png} Let's move on.":
            jump m_moveOn

label m_aboutEileen:
    k "So who is Eileen? Is she your favorite? Wait, let me rephrase. Is she your {i}fave{/i}?"
    m "Ew, no, please don't say 'fave.' That's so two years ago."
    m "Eileen is {size=+10}THE COOLEST{/size}. She is a half-woman, half-shark ghost and gives no fucks about what anyone thinks of her. She is just soooo authentic."
    jump TCTA

label m_aboutTia:
    k "Who is Tia?"
    m "Ugh, don't get me started on Tia. Tia is this basic vampire who does this annoying clicking thing with her teeth when she's excited."
    m "Tia replaced Kimmi last season because there was some drama between Kimmi and Lucretia. They should have worked it out, but instead Kimmi left and we're stuck with Tia."
    k "Fascinating."
    m "{size=+10}I KNOOOOOOOWWWW.{/size}"
    jump TCTA

label m_moveOn:
    k "Let's talk about something else."
    m "Whatever you want!"

    jump Marlonparkmenu

label m_aboutGlow:
    k "How do you like working at the Glow?"
    m "I like the Glow! I actually opened it as my business project."
    k "Really? I didn't take you as the business owner type."
    m "I wanted to open a place that would makes me feel less afraid of the dark."
    k "But, you can see in the dark, right? Why would you be scared of the dark?"
    m "I can see in the dark, but that doesn't make it any less scary. Light means comfort."
    m "Light is infinite, like I'm standing on the edge of forever while the cracks in my life are illuminated with understanding. I remember things I've forgotten."
    m "When I'm in the light, the world just...makes sense."
    m "..."
    m "..."
    k "..."
    k "Buddy.{p=2.0}That was deep."
    m "Was it? Oops."

    jump Marlonparkmenu

label m_somethingelse:
    k "Let's explore or something."
    m "Oh, you probably want to check out that maze, right? Otis made a weird-ass hedge maze this year for the festival. I don't get it."

    menu:
        "{image=emoji/opensmile_emoji.png} Let's go in the maze together!":
            jump m_enterMaze
        "{image=emoji/thumbsup_emoji.png} See you later!":
            jump m_seeYouLater

label m_enterMaze:
    k "I'm intrigued by the maze's weirdness. Maybe he hid something in the middle."
    m "Like treasure? Or gift cards!"
    k "How about we check it out? We can split our findings."
    m "Dibs on the gift cards."

    jump m_maze_withMaron

label m_seeYouLater:
    k "Interesting...well, I'm going to keep looking around this park. See you later!"
    m "See ya, buddy."

    hide marlon neutral
    jump parkentrancemenu

label Spikeparkconvo:
    show bg park bench
    if spike_visited == False:
        $ spike_visited = True
        show spike neutral
        s "There [she] is!"
        if marlon_visited == True:
            jump s_talked_to_marlon
        else:
            jump s_park_intro
    else:
        show spike laugh blush
        s "Awoo! You're back! I missed you so much!"
        hide spike laugh blush
        show spike neutral
        jump Spikeparkmenu

label s_talked_to_marlon:
    s "Awoo! You smell like Marlon! How's my favorite mothman doing?"
    k "Unforgettable. As usual, apparently."
    hide spike neutral
    show spike laugh
    s "Hehe, definitely! I love that dude. He knows everyone's deepest, darkest secrets..."
    hide spike laugh

    jump s_park_intro

label s_park_intro:
    show spike neutral
    s "I'm glad you made it!"
    k "Yeah, I managed to find it by looking at the GPS on my phone."
    s "See? That's why I let my pups use their phones during practice."
    k "Wait, your 'pups'?"
    hide spike neutral
    show spike blush
    s "Oh, sorry! That's what I call my students."
    hide spike blush
    show spike laugh
    s "But it's true! Smartphones help develop hand-eye coordination."
    s "If my pups can dribble down the court with one hand and send a text with the other, they're more skilled than I am! Maybe they should be the pack alpha instead of me!"
    hide spike laugh
    show spike neutral
    k "So you just coach basketball at the high school? Do you teach any other subjects?"
    s "Nope! Just basketball! When I'm not coaching, you can find me in the Weirdwood. I chop down trees and sell quality, non-haunted logs to anyone who needs 'em!"
    s "So... whaddaya think?"

    jump Spikeparkmenu

label Spikeparkmenu:
    menu:
        "{image=emoji/tree_emoji.png} So you're a lumberjack?":
            jump s_lumberjack_park
        "{image=emoji/basicfrown_emoji.png} What's the Weirdwood?":
            jump s_weirdwood_park
        "{image=emoji/sad_emoji.png} Show her the photo of the car crash" if s_photo_park == False:
            jump s_photo_park
        "{image=emoji/thumbsup_emoji.png} Let's move on.":
            jump s_moveon_park

label s_photo_park:
    $ s_photo_park = True
    #This is where code magic goes to show Spike the photo on Kai's phone
    hide spike neutral
    show spike concern
    s "Oh no. Thank the moon you're okay, Kai, that's so scary."
    hide spike concern
    show spike neutral
    k "The thing is, I don't remember any of it. Or anything before it, either."
    k "I was hoping you had some insight for me based on this photo evidence?"
    hide spike neutral
    show spike concern
    s "Sorry, pup, I got nothin'. But I definitely haven't seen that car before."
    hide spike concern
    show spike neutral
    k "That must mean {i}something{/i}..."
    s "Don't worry, Kai. I'll protect you—even if it means that I must attack."

    jump Spikeparkmenu

label s_lumberjack_park:
    k "So, you're basically a lumberjack?"
    hide spike neutral
    show spike laugh
    s "Awoo! You bet! I'm definitely a fan of that job title. Though we don't have anything nearly so sophisticated as a lumber or saw mill here in Port M."
    hide spike laugh
    show spike neutral
    k "Where do you work, then?"
    s "Oh, just a quiet, isolated cabin in the woods with only the wailing tree spirits for company."

    jump s_lumberjack_menu

label s_lumberjack_menu:
    menu:
        "{image=emoji/eyeroll_emoji.png} 'Wailing tree spirits'?":
            jump s_spirits_park
        "{image=emoji/sadfrown_emoji.png} Don't you get lonely?":
            jump s_lonely_park
        "{image=emoji/thumbsup_emoji.png} Let's talk about something else.":
            jump s_somethingelse_park

label s_spirits_park:
    k "Wait... what do you mean {i}tree spirits{/i}?"
    hide spike neutral
    show spike laugh
    s "Don't worry! I'm only kidding... partially. Maybe you'll have to come visit me to find out!"
    hide spike laugh
    show spike neutral

    jump s_lumberjack_menu

label s_lonely_park:
    k "Don't you ever get lonely out there by yourself in the middle of the woods?"
    hide spike neutral
    show spike blush
    s "I haven't really thought about it. No one's ever asked me that, to be honest. I suppose it does get lonely, but my condition kind of necessitates it."
    k "Oh, you mean the whole werewolf... thing?"
    hide spike blush
    show spike laugh
    s "Hahaha. Yeah, that old chestnut. It's not a big deal to me, but having one day out of the month when you can't entertain buds in your folksy cabin in the woods makes it kind of difficult to host extended sleep-overs."
    s "Especially with how much noise the spirits make."
    hide spike laugh
    show spike neutral

    jump s_lumberjack_menu

label s_somethingelse_park:
    k "Let's talk about something else."
    s "Your choice!"

    jump Spikeparkmenu

label s_weirdwood_park:
    k "What's the Weirdwood? I've seen it on my map, but no one's really told me much about it. Honestly, I'm not really enthused by that name."
    s "Oh! It's just our local haunted forest. Nothing to worry about."
    s "I'm sure you saw the outskirts of it on your way back into town. It's full of all sorts of creepies and crawlies, but if you're prepared and well-equipped, I'm sure you could handle it."
    k "Prepared how?"
    hide spike neutral
    show spike laugh
    s "You could always do what I do and pack a loaded crossbow. Gets you by just as well as a firearm does without alerting the real scary forest denizens."
    s "Couple that with some of the Seer's antivenom and/or nightvision goggles, and you're good to go a-huntin' for premium wood."
    hide spike laugh
    show spike neutral

    jump Spikeparkmenu

label s_moveon_park:
    k "Let's move on. Is this what you wanted to show me? It just looks like a regular old park to me."
    s "Maybe from the outside, but Otis just finished putting up the raddest hedge maze. Plus you can do a lot of people watching from the park bench here. I love to drop eaves any time of day."
    k "Tell me more about this hedge maze."
    hide spike neutral
    show spike blush
    s "Oh, I don't know much about it. Otis does something special for the festival every year. I'm sure he could tell you all about his plans, or Mayor Rain could fill you in."
    hide spike blush
    show spike neutral

    menu:

        "{image=emoji/opensmile_emoji.png} Let's go in the maze together!":
            jump s_together_park
        "{image=emoji/thumbsup_emoji.png} See you later!":
            jump s_leave_park

label s_together_park:
    k "I admit that I'm very intrigued. How about we try to navigate the maze together?"
    hide spike neutral
    show spike laugh blush
    s "Awoo! Good idea! Who knows what kinds of goodies we could find inside?"
    hide spike laugh blush
    show spike neutral
    k "Probably whatever's at the center?"
    hide spike laugh blush
    show spike laugh
    s "Hahaha. Wouldn't you love to find out, though? I can just smell the adventure."
    s "Literally. Because of my wolfy nose senses. I can literally smell the adventure."
    hide spike laugh

    jump Spikemazeconvo

label s_leave_park:
    k "Interesting... I'm going to walk around the park some more. See you later!"
    s "Not if I see you first!"

    hide spike neutral
    jump parkentrancemenu

label m_maze_withMaron:

    show bg hedge one
    show marlon neutral

    $ Companion = "Marlon"

    "Turns out, this maze is more than just a family-friendly walk in the park. The imposing hedge walls feel unwelcoming despite the beautiful flora scattered about."
    "Marlon makes himself comfortable on my shoulder and yawns, obviously disinterested in our current predicament. We turn a few corners before I realize I have absolutely no idea where we are."
    "Maybe if I get Marlon to lighten up he'll fly around and figure this maze out faster."

    menu: #1/7

        "I need to say something to get Marlon interested."

        "{image=emoji/unicorn_emoji.png} Ask about unicorns":
            #BAD response
            call m_unicorn_maze from _call_m_unicorn_maze
        "{image=emoji/poop_emoji.png} Find your own way":
            #BAD response
            call m_poop_maze from _call_m_poop_maze
        "{image=emoji/basicsmile_emoji.png} Talk about Eileen":
            #GOOD response
            call m_eileen_maze from _call_m_eileen_maze

    show bg hedge two
    "I peer around intently trying to sense my way to the middle of the maze. I'm laughably bad at it and it shows. Marlon begins to laugh."

    menu: #2/7
        m "Need help?"
        "{image=emoji/sad_emoji.png} Yes I need help":
            #GOOD reponse
            call m_yeshelp_maze from _call_m_yeshelp_maze
        "{image=emoji/eyeroll_emoji.png} No, I can do this myself":
            #BAD response
            call m_nohelp_maze from _call_m_nohelp_maze
        "{image=emoji/heart_emoji.png} I like being stuck here with you":
            #GOOD response
            call m_withyou_maze from _call_m_withyou_maze

    show bg hedge three
    m "Speaking of your navigational skills, remember that one time we went camping with Corliss and Freya? That was amazing. We went into the Weirdwood and you said you knew how to get to a hot spring."
    m "Instead, we walked for {size=+10}HOURS{/size}. The deeper we went into the woods, the louder the spirits howled. They were soooo ANGRY! It was hilarious! We thought we'd never return, but luckily The Seer's Hut was walking around that night."

    menu: #3/7
        "{image=emoji/basicsmile_emoji.png} The Seer's Hut?":
            #GOOD response
            call m_seershut_maze from _call_m_seershut_maze
        "{image=emoji/laugh_emoji.png} What happened next?":
            #GOOD response
            call m_whathappened_maze from _call_m_whathappened_maze
        "{image=emoji/mad_emoji.png} Let's talk about something else":
            #BAD reponse
            call m_somethingelse_maze from _call_m_somethingelse_maze

    show bg hedge two
    m "How would you describe your aesthetic?"

    menu: #4/7
        "{image=emoji/peach_emoji.png} Summoning spirits while dressed in glow-in-the-dark booty shorts":
            #GOOD reponse
            call m_booty_maze from _call_m_booty_maze
        "{image=emoji/wolf_emoji.png} Riding a giant wolf into an apocalyptic sunset":
            #GOOD response
            call m_sunset_maze from _call_m_sunset_maze
        "{image=emoji/tableflip_emoji.png} Confused and barely functioning humanoid":
            #BAD response
            call m_confused_maze from _call_m_confused_maze

    show bg hedge three
    "Marlon starts going on about aesthetics mentions something about being sparkly graveyard chic. Surprisingly, it looks as through we've made progress. The grass beneath us becomes more manicured, which I can take to mean that we're getting closer to the center of the maze."
    "My mind wanders for a moment while I think about what we'll find at the center of the maze. Lots of work obviously went into building this thing, so is it supposed to be keeping us out...or keeping something in?"
    m "Kai, what do you think? Yes or no?"
    "I realize Marlon had been asking me something, but I've obviously missed the entire conversation."

    menu: #5/7
        "{image=emoji/opensmile_emoji.png} Yes":
            #BAD response
            call m_yes_maze from _call_m_yes_maze
        "{image=emoji/eyeroll_emoji.png} No":
            #GOOD response
            call m_no_maze from _call_m_no_maze
        "{image=emoji/basicfrown_emoji.png} I missed everything you said":
            #GOOD response
            call m_missed_maze from _call_m_missed_maze

    show bg hedge one
    m "Do you have your eyes on anyone right now?"

    menu: #6/7
        "{image=emoji/wolf_emoji.png} Spike":
            #GOOD reponse
            call m_spike_maze from _call_m_spike_maze
        "{image=emoji/wink_emoji.png} Still looking":
            #GOOD response
            call m_looking_maze from _call_m_looking_maze
        "{image=emoji/eyeroll_emoji.png} I'm not saying":
            #BAD response
            call m_notsaying_maze from _call_m_notsaying_maze

    show bg hedge three
    "We walk for just a bit longer and the center of the maze seems to be in sight. Marlon and I high-five excitedly, knowing that we've bested the awfully tedious hedge maze."
    k "We did! We actually did it!"
    m "And I thought I was going to have to carry you out of here."
    k "If anything, I would have had to carry {i}you{/i} out."
    m "I don't know about you, but I had a GREAT time."

    menu: #7/7
        "{image=emoji/opensmile_emoji.png} I had a great time with you too":
            #GOOD response
            call m_greattime_maze from _call_m_greattime_maze
        "{image=emoji/eyeroll_emoji.png} Let's just get out of here":
            #BAD response
            call m_leave_maze from _call_m_leave_maze
        "{image=emoji/wink_emoji.png} Let's do the maze again":
            #GOOD response
            call m_again_maze from _call_m_again_maze

    show bg hedge one
    "Marlon friend score: [marlon_friend_score]"
    hide marlon neutral
    show otis neutral
    if otis_visited == True:
        jump m_talked_to_otis
    else:
        jump m_otis_maze

label m_talked_to_otis:
    "Now we're suddenly face-to-face with that bird-man from before, and he's blocking our path."
    hide otis neutral
    show marlon neutral
    m "Ugh, not Otis."
    k "{size=-10}Be cool, be cool.{/size}"
    m "How can I when he has THE worst fashion tastes? Sweater vests? REALLY?"
    k "Calm down, I'll talk to him."
    jump Otis_Maze_Convo

label m_otis_maze:
    "Now we're suddenly face-to-face with a bird-man I don't recognize, and he's blocking our path."
    hide otis neutral
    show marlon neutral
    k "Who is THAT?"
    m "Ugh, that's Otis. He runs the town's grand annual festival celebrating the Madrona Tree."
    m "{size=-10}He also has THE worst fashion tastes.{/size}"
    k "Calm down, I'll talk to him."
    jump Otis_Maze_Convo

label m_unicorn_maze:
    k "So, why DO you hate unicorns?"
    if unicorn_marlon:
        m "Wow, this again?"
        k "I'm curious, that's all."
    m "Did you know that unicorns and mothmen went to war?"
    k "WHAT?!"
    m "That's right. It's called the Grey Rainbow War of 1983."
    k "This actually happened?"
    m "YES!"
    m "..."
    m "Well, okay, it was less of a war and more of a final championship. And less fighting and more roller derby."
    k "So what you're saying is the mothmen lost against unicorns in a roller derby competition?"
    m "YES! IT WAS CARNAGE! Mothmen have never gotten closer to beating unicorns at roller derby than in 1983. {p=2.0} Some say we never will..."
    "Maron stares wistfully into the distance and I can only assume images of roller derby fill his mind's eye. Maybe talking about something else will clear his mind."
    return

label m_poop_maze:
    "I close my eyes and try to focus on the center of the maze. Maybe I'm extra still I can sense the correct path. I open my eyes and point toward one of the paths."
    k "I bet it's a left here."
    "We walk down the path and for a moment I feel confident in my decision. As we turn another corner I hold my breath and it's...a dead end."
    m "Bad move, buddy."
    k "I have a bad sense of direction. I'd be lost without my phone honestly."
    return

label m_eileen_maze:
    k "So, about Eileen from Trashy Cryptids."
    m "OMG EILEEN IS THE QUEEEEEEEEEN!!!"
    m "She is my {size=+10}IDOL{/size}."
    m "This one time I sent her some fan mail and included a piece of my antennae. Don't worry. They grow back."
    m "Anyway, so last Eileen had this really cool—no no, turn right here—she made this really cool..."
    "Oh geez, Marlon can't stop talking about Eileen. At least he knows where to go."
    return

label m_yeshelp_maze:
    k "Yes, please. I am so lost and surprisingly bad at this."
    m "As far as I remember you've always had questionable navigational skills."
    "Marlon flies up causing a dust of dirt and grass to impair my vision for a moment. I crank my head upwards to get a good view of Marlon who is surveying the scene."
    k "See anything?"
    m "We'll need to take a right, another right, and then a left!"
    "Marlon descends and returns to his comfortable perch on my shoulder."
    return

label m_nohelp_maze:
    k "No no no, I got this! I'm going to figure this out for us."
    "Marlon's antenna droop, obviously disappointed at my response."
    k "I got this! I think we make a right here."
    return

label m_withyou_maze:
    k "Hey, it's not so bad if we're stuck here forever right? At least I'm here with you."
    m "Hahaha Kai, there is no one else I'd prefer to be stuck in a dumb maze with."
    m "Except that Trashy Cryptids is on at eight tonight, so I gotta be home for that, so let's get lost together some other time."
    k "Haha, okay. I will use my lackluster navigational skills to get us out."
    return

label m_seershut_maze:
    k "Seer's Hut? Sounds spooky."
    m "It's so cool. The Seer's aesthetic is on point. She lives in a hut with bird legs and wanders the Weirdwood. For those lucky enough to find the Seer, she provides lots of services, but they don't come cheap."
    m "Fortune telling, hexes, potions, forbidden wisdom."
    k "Wow, she sounds incredible."
    m "Oh absolutely. She also makes some killer scones."
    m "Literally. Ask her for a non-fatal scone. Those are delicious."
    return

label m_whathappened_maze:
    k "Seer's Hut? What happened? Was everything okay?"
    m "The Seer came out and chastised us for going into the Weirdwood without any kind of protection or weaponry. But come on, I was too busy packing us floaties to use on the lake."
    m "The Seer gave us a ride back to our campground...at a price."
    k "Oh no! What was the price?"
    m "I think it was about $12.95. We bought two scones and one prophecy from her."
    k "WHAT?! What was it?!"
    m "I think one was blueberry and the other was cranberry-orange."
    k "No! The prophecy!"
    m "Eh, something about the coming storm that would lift the darkness and bring light. I don't really remember."
    m "Mostly I just LOVE the Seer's aesthetic."
    return

label m_somethingelse_maze:
    k "Let's talk about something else. I don't really like hearing about my past screw ups."
    m "Aww! It wasn't that bad. Anyway, we got to visit the Seer's Hut. I just LOVE the Seer's aesthetic."
    return

label m_booty_maze:
    k "Hmm, probably dressing up in my glow-in-the-dark booty shorts and spending my night summoning spirits."
    m "I BOUGHT YOU THOSE BOOTY SHORTS!"
    k "Did you? I found them in my apartment."
    m "Buddy, let's make this happen."
    return

label m_sunset_maze:
    k "Hmm, probably escaping the ruins of the town on top of a giant wolf as the sun sets on an apocalyptic scene."
    k "That feels like me."
    m "Lemme guess, the wolf is Spike."
    k "I..."
    k "No!"
    k "Uh, course not!!!"
    m "Hahaha you're blushing! I knew it."
    k "I never said anything."
    m "Your secret is safe with me."
    return

label m_confused_maze:
    k "Eh, I'm the renmants of a very confused and barely functioning human."
    m "Oh. That's not very fun..."
    k "I'm not exactly the most put-together person. Especially right now."
    return

label m_yes_maze:
    k "Yes! Absolutely."
    m "Um, really?"
    k "Yeah!"
    m "Oh...well that sucks. I hope that doesn't happen."
    k "Wait. I'm so sorry. I wasn't paying attention and I just randomly responsed. What were you asking?"
    m "I asked whether or not you think we'd drift apart if...you started dating someone."
    k "What! No! Of course not!"
    return

label m_no_maze:
    k "No! Absolutely not."
    "Marlon smiles at me and exhales a deep breathe. He looks relieved."
    m "I'm glad."
    k "About?"
    m "About that fact that you won't let our friendship drift away if you end up, you know, dating and spending your time with someone else."
    k "Of course not!"
    return

label m_missed_maze:
    k "Er, sorry. My mind drifted and I missed your question."
    m "I asked if you think that...{p=3.0}we'll drift apart as friends if you start dating and spending time with someone else."
    k "What! No! Of course not!"
    "Marlon smiles at me and exhales a deep breathe. He looks relieved."
    m "I'm glad."
    return

label m_spike_maze:
    k "This is going to sound lame because we've only just started to hang out but...Spike."
    m "I KNEW IT!"
    k "There's no way you could've known."
    m "Nope! I called it. I am soooooo good at this. I knew it I knew I knew."
    k "She's been really nice to me since all this craziness went down. She's been supportive."
    m "You have my complete approval. If you ever need a wingman...{size=-10}because I have wings{/size}...you just let me know."
    k "Thanks, Marlon."
    return

label m_looking_maze:
    k "Honestly, I don't know. I'm still looking."
    m "I get that. You gotta find the right person and that's not something you should rush."
    k "Yeah. Exactly. I'm just getting used to this new reality. Maybe once that happens, I'll start thinking romance."
    m "If you ever need a wingman...{size=-10}because I have wings{/size}...you just let me know."
    k "Thanks, Marlon."
    return

label m_notsaying_maze:
    k "I'd rather not say honestly. I'm worried that bit of info might make it out of the maze."
    m "Whoa whoa whoa, you don't think I can keep a secret."
    k "Weeeeelllllll..."
    m "Fine. I know I'm not the BEST at keeping a secret, but I like to think I can keep a secrets when it counts."
    return

label m_greattime_maze:
    k "This is the best time I have ever spent being lost in a hedge maze."
    "Marlon beams at me. For a second, I think I begin to see him {i}actually{/i} glow. Maybe it was just the sunlight though."
    m "Let's get out of here and never look back!"
    return

label m_leave_maze:
    k "Let's just get out of here. This maze was such a waste of time."
    "Marlon looks hurt, as though I squashed his fun. It hadn't occurred to me that he was having such a good time, especially when he seemed so disinterested at the beginning."
    m "Let's go."
    return

label m_again_maze:
    k "This was SO FUN. We should turn around and do this while thing again."
    m "Hahaha."
    m "No."
    m "Please. Let's not do that."
    k "Okay. Well, I had a great time being lost with you."
    "Marlon beams at me. For a second, I think I begin to see him {i}actually{/i} glow. Maybe it was just the sunlight though."
    m "Let's get out of here and never look back!"
    return

label Spikemazeconvo:
    $ Companion = "Spike"
    show bg hedge one
    show spike neutral

    "Spike and I start to walk side by side through the maze, the seemingly endless labyrinth looming before us as we take each step."
    "Spike sniffs once, twice, deeply inhaling. I try to sniff, as well, only smelling the scents of the park: the freshly upturned dirt below our feet, the almost pungent aromas of the local flora, and the droppings left by various animals."
    "Maybe her wolf senses have picked up something. Should I ask her about it or try another tactic?"

    menu: #1/7
        "{image=emoji/wolf_emoji.png} Ask about wolf senses":
            #GOOD response
            call s_wolf_maze from _call_s_wolf_maze
        "{image=emoji/poop_emoji.png} Find your own way":
            #BAD response
            call s_poop_maze from _call_s_poop_maze
        "{image=emoji/basicsmile_emoji.png} Talk about basketball":
            #GOOD response
            call s_basketball_maze from _call_s_basketball_maze

    show bg hedge two
    show spike laugh
    s "In the pack, I teach my pups to support each other, lift up their teammates, in order to succeed. Maybe we should follow my own advice—literally!"
    hide spike laugh
    show spike neutral
    "She goes on to present an unnecessarily complex idea that pretty much boils down to her lifting me on her shoulders to see over the hedges."
    "I think she's waiting for my response..."

    menu: #2/7
        "{image=emoji/thumbsup_emoji.png} Agree":
            #GOOD response
            call s_agree_maze from _call_s_agree_maze
        "{image=emoji/basicfrown_emoji.png} Disagree":
            #BAD response
            call s_disagree_maze from _call_s_disagree_maze
        "{image=emoji/basicsmile_emoji.png} Talk about teenagers":
            #GOOD response
            call s_teenagers_maze from _call_s_teenagers_maze

    show bg hedge three
    show spike neutral
    "Spike starts talking about the hedges themselves, monologuing about the types of trees and shrubbery typically used in the construction. There's a pause in her speech."

    menu: #3/7
        "{image=emoji/hearteyes_emoji.png} Listen intently":
            #GOOD response
            call s_listen_maze from _call_s_listen_maze
        "{image=emoji/tree_emoji.png} Talk about trees":
            #GOOD response
            call s_tree_maze from _call_s_tree_maze
        "{image=emoji/unicorn_emoji.png} Talk about unicorns":
            #BAD response
            call s_unicorn_maze from _call_s_unicorn_maze

    show bg hedge two
    show spike neutral
    s "Do you have a favorite tree?"

    menu: #4/7
        "{image=emoji/mad_emoji.png} No":
            #BAD response
            call s_no_maze from _call_s_no_maze
        "{image=emoji/wink_emoji.png} Whatever tree you like":
            #GOOD response
            call s_wink_maze from _call_s_wink_maze
        "{image=emoji/tree_emoji.png} Madrona tree":
            #GOOD response
            call s_madrona_maze from _call_s_madrona_maze

    show bg hedge three
    show spike concern
    "She's starting to freak out a little. I should say something."
    hide spike concern
    show spike neutral

    menu: #5/7
        "{image=emoji/heart_emoji.png} Offer support":
            #GOOD response
            call s_support_maze from _call_s_support_maze
        "{image=emoji/tableflip_emoji.png} Demand focus":
            #BAD response
            call s_demand_maze from _call_s_demand_maze
        "{image=emoji/basicfrown_emoji.png} Express concern":
            #GOOD response
            call s_concern_maze from _call_s_concern_maze

    show bg hedge one
    show spike neutral
    s "I think... it's coming from the center of the maze. Let's follow it."

    menu: #6/7
        "{image=emoji/thumbsup_emoji.png} Agree":
            #GOOD response
            call s_agree2_maze from _call_s_agree2_maze
        "{image=emoji/basicfrown_emoji.png} Disagree":
            #BAD response
            call s_disagree2_maze from _call_s_disagree2_maze
        "{image=emoji/poop_emoji.png} Flee":
            #BAD response
            call s_flee_maze from _call_s_flee_maze

    show bg hedge three
    show spike neutral
    "After a while, Spike says that we're getting closer. She explains that whatever we find at the center could be bad, very bad, but she'll protect me."
    s "Do you trust me?"

    menu: #7/7
        "{image=emoji/thumbsup_emoji.png} Yes":
            #GOOD response
            call s_yes_maze from _call_s_yes_maze
        "{image=emoji/basicfrown_emoji.png} No":
            #BAD response
            call s_no2_maze from _call_s_no2_maze
        "{image=emoji/laugh_emoji.png} Laugh it off":
            #GOOD response
            call s_laugh_maze from _call_s_laugh_maze

    show bg hedge one
    "Spike friend score: [spike_friend_score]"
    hide spike neutral
    show otis neutral
    if otis_visited == True:
        jump s_talked_to_otis
    else:
        jump s_otis_maze

label s_talked_to_otis:
    "Now we're suddenly face-to-face with that bird-man from before, and he's blocking our path."
    hide otis neutral
    show spike neutral
    s "It's Otis! Looking snappy as always."
    hide spike neutral
    show spike concern
    s "Something still smells off, though."
    hide spike concern
    show spike neutral
    k "..."
    k "Are you {i}growling{/i}?"
    hide spike neutral
    show spike blush
    s "...{size=-10}no.{/size}"
    k "Let me talk to him."
    hide spike blush
    jump Otis_Maze_Convo

label s_otis_maze:
    "Now we're suddenly face-to-face with a bird-man I don't recognize, and he's blocking our path."
    hide otis neutral
    show spike neutral
    k "Spike, who is this guy?"
    s "Oh, it's just Otis! He's the one I was telling you about, the one who designed this maze for the festival."
    hide spike neutral
    show spike concern
    s "Something still smells off, though."
    hide spike concern
    show spike neutral
    k "..."
    k "Are you {i}growling{/i}?"
    hide spike neutral
    show spike blush
    s "...{size=-10}no.{/size}"
    k "Let me talk to him."
    hide spike blush
    jump Otis_Maze_Convo

label s_wolf_maze:
    k "Smell anything?"
    hide spike neutral
    show spike laugh
    s "Awoo, yes! This way!"
    hide spike laugh
    show spike neutral
    "Spike explains that she can smell something in the center of the maze. She takes my hand and leads me down a series of paths, tugging me along with frenetic certainty."
    "We proceed without trouble, making good progress, until we reach a new crossroads, and Spike stops to sniff again."
    hide spike neutral
    show spike concern
    s "I think someone got lost in here recently. They stopped to eat a snack—a tuna sandwich—but they didn't finish it. They must have discarded the remains somewhere nearby. The rotten fish smell is blocking my nose."
    hide spike concern
    return

label s_poop_maze:
    "I stay silent, trying to work out the branching pathways for myself and analyzing the details before me."
    "The silence drags on for about a minute before I suggest a path. Spike follows happily."
    "We come to a dead end. This was probably the wrong way to go... we backtrack until we reach an entirely new crossroads."
    return

label s_basketball_maze:
    "Perhaps she'd rather chat about basketball than her olfactory system..."
    "I bring up basketball to her, and she instantly perks up, telling me all about the sport and her 'pups.'"
    return

label s_agree_maze:
    "I agree to sit on Spike's shoulders, and she hoists me up to see above the hedges. I get a good enough view of the layout, and we continue on our way—a bit better informed than we were before."
    return

label s_disagree_maze:
    "I tell Spike that I'm not really interested in being boosted up on your shoulders like a child, and she deflates a little. That was probably the wrong thing to say..."
    "As we continue through the maze, she seems a bit downcast. We end up moving a bit slower than we were before, not really making progress."
    return

label s_teenagers_maze:
    "Instead of taking a stand either way, I ask Spike more questions about her 'pack' and she is more than happy to give details. She really seems to love those kids..."
    "But now it seems like she's totally forgotten her plan, and we still have to get through this maze."
    "She's in a good mood, though, and before we know it we appear to have made progress."
    return

label s_listen_maze:
    "Spike goes on to compare the merits of the yew tree versus the boxwood hedge, and I let her ramble uninterrupted."
    "Our course through the maze runs smoothly."
    return

label s_tree_maze:
    "I ask for more detail about the hedges, and her face brightens. She goes on to compare the merits of the yew tree versus the boxwood hedge, and I jump in with more questions at appropriate times."
    "Our course through the maze runs smoothly."
    return

label s_unicorn_maze:
    "I take control of the conversation completely and start talking about unicorns."
    hide spike neutral
    show spike concern
    s "Oh, uh, yeah. I like unicorns, too, I guess..."
    hide spike concern
    show spike neutral
    "Spike's enthusiasm dies out, and it distracts her from our course in the maze. She isn't entirely done with the subject of trees, though."
    return

label s_no_maze:
    "I grumpily state that I don't have a favorite tree, which seems to put an end to the conversation at last."
    "But then Spike starts, her nostrils widening. She says she's picked up a scent: the scent of blood."
    return

label s_wink_maze:
    hide spike neutral
    show spike blush
    "Spike blushes but quickly recovers and wiggles her eyebrows at me."
    hide spike blush
    show spike laugh blush
    s "Well, then, that would be the {i}you{/i} tree. Awoo!"
    hide spike laugh blush
    show spike neutral
    "We laugh together, but then Spike stops, her nostrils widening. She says she's picked up a scent: the scent of blood."
    return

label s_madrona_maze:
    "I instinctively mention the Madrona tree, and Spike smiles."
    "She talks a little bit about the town's namesake before she stops, her nostrils widening. She says she's picked up a scent: the scent of blood."
    return

label s_support_maze:
    "Spike's breathing slows down as I speak soothingly to her."
    "She quickly recovers as I pat her back, and a determined look settles on her face."
    return

label s_demand_maze:
    "Spike doesn't respond to me as I try to verbally slap sense into her."
    "We end up wasting a fair amount of time waiting for Spike's sense of smell to adjust itself."
    "Eventually, she manages to recover enough, and a determined look settles on her face."
    return

label s_concern_maze:
    "I fixate on the blood, and Spike manages to calm down as she tells me the details, a determined look settling on her face."
    return

label s_agree2_maze:
    "I let Spike take the lead, and she walks on, presumably in the direction of this blood."
    hide spike neutral
    show spike laugh blush
    s "Thank you for trusting my nose."
    hide spike laugh blush
    return

label s_disagree2_maze:
    k "How do you know it's in the center? Let's just continue as we were."
    "Spike seems put out by my not trusting her nose, but we continue as we were, all sense of urgency gone."
    return

label s_flee_maze:
    "I try to take off running, back to the entrance of the maze, but Spike catches my arm."
    s "We're not giving up."
    "I feel like one of her disobedient pups, but she looks more determined than ever as she pulls me along, our pace slowed somewhat due to my resistance."
    return

label s_yes_maze:
    "Spike beams back at me, and we turn the corner together."
    return

label s_no2_maze:
    "Spike looks crestfallen, but I had to be honest. She turns the corner, and I follow."
    return

label s_laugh_maze:
    "I start laughing, trying to force the tension from my system."
    k "It can't be as bad as all that, right?"
    "Spike just looks fondly at me and shakes her head. She takes my hand in hers, and we turn the corner together."
    return

label Otis_Maze_Convo:
    hide spike neutral
    hide marlon neutral
    show otis neutral

    k "How did you get here so fast?! Didn't I see you at the entrance before I came in?"
    show otis explain
    o "Oh, I know my way around this place quite well. You see, the maze is the home of my imagination."
    o "As a child, I would run through the maze seeing myself in the Great Hall of the People or flying above the Karnak Temple Complex. It was my kingdom. It was anything I needed it to be."
    hide otis explain
    show otis neutral
    k "Sounds like a nice place."
    o "Indeed. Would you like to hear about the history of the Madrona tree?"

    menu:
        "{image=emoji/basicsmile_emoji.png} Sure!":
            jump Otis_Maze_Convo.k_sure
        "{image=emoji/basicfrown_emoji.png} Okay, but the short version.":
            jump Otis_Maze_Convo.k_shortversion
        "{image=emoji/thumbsup_emoji.png} No thanks, I'll see you around.":
            jump Otis_Maze_Convo.k_nothanks

label .k_sure:

    k "I'd like that."
    show otis explain
    o "Well, the Port Madrona, also known as the Arbutus Menziesii species of the order Ericales, is native to the western regions of the North."
    o "It is an evergreen that sheds its bark with age and in the autumn produces small red berries known for their healing properties. "
    o "The tree is said to be over 400 years old with roots so deep that they span the length of the town. And when it rains, the tree appears to come to life taking in water and pumping out a rich red substance like blood stains on its leaves. "
    o "It's no wonder the tree has come to be revered as the life force of the town. Every year, I host our annual festival so we can celebrate the Port Madrona tree through song, food, sacrifices and prayer. "
    hide otis explain
    show otis neutral
    k "Wow. That's pretty amazing. It seems to have thrived here for so long. I wonder, why?"
    hide otis neutral
    show otis explain
    o "Some say, it was the Port Madrona tree that gave birth to our entire town, and as long as we honor it, it will continue to protect our home."
    hide otis explain
    show otis neutral
    k "What happens if the tree starts to die?"
    show otis eyeroll
    o "Don't be silly. That would never happen."
    hide otis eyeroll
    hide otis neutral
    jump maze_center

label .k_shortversion:

    k "Alright, but keep it short will you?"
    show otis explain
    o "Very well. The Port Madrona tree has lived here for over 400 years with roots that are said to span the length of the town."
    o "Every year, in order to ensure that the tree continues to thrive and floruish, we honor it."
    o "The town gets together and celebrates with a festival. Yusef's Crab House, the Beaver Mill Diner, the Dark Carta all donate food and entertainment to the night's festivities and, of course, we choose the guardian that will tend to the tree year-round."
    hide otis explain
    show otis neutral
    k "That sounds pretty great. Guardian, huh?"
    o "Yes, the chosen guardian will have the honor of tending to our beloved tree and ensuring no harm should befall her. "
    k "I wonder who it will be this year... this festival sounds interesting. I can't wait!"
    hide otis neutral
    show otis eyebrow raise
    o "Well, surely, you remember it from last year?"
    k "Oh, right, of course. Um, I should be going now."
    hide otis eyebrow raise
    show otis smirk
    o "I'll be seeing you, Kai."
    hide otis smirk
    hide otis neutral
    jump maze_center

label .k_nothanks:

    k "Maybe later."
    o "No problem. I'll be around if you get curious. I promise it's quite enchanting."
    hide otis neutral
    jump maze_center

label maze_center:
    show no_flicker
    "[Companion] and I finally reach the center of the hedge maze."
    show flicker_one
    "What the hell? Is that.. No."
    show flicker_two
    "This isn't real… is that me?! Holy shit. What the hell is going on here? I don't understand. Am I dead? How can I be dead? I thought I just lost my memories, but is this all some type of pseudo world I'm living out in my head?! Oh god, I need to figure this out."
    "I can't lose it now. If I can't trust my memories, I'll need to find the answers from the people of this town. I need to remember who I am and why I came here. I can't explain it, but I know it's the only way to prevent this."
    show madrona_light
