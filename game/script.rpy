# The script of the game goes in this file.

# Define character affection stats
default marlon_friend_score = 0
default spike_friend_score = 10

# define various states the player may trigger
default morning_phone_texts = [0,0]
default unicorn_marlon = False
default spike_visited = False
default marlon_visited = False
default otis_visited = False
default trash_tv_topics = [0,0]
default marlon_maze_topics = [0,0,0,0,0,0,0]

#Define puzzle states
default maze_progress = 0

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character(_("Kai"), color="#aa6f73")
define m = Character(_("Marlon"), color="#7e6a7c")
define s = Character(_("Spike"), color="#ac330f")
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
    show screen phone_pop_but

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
    show screen phone_pop_but
    k "Okay, cool."
    k "I can head to the park now."
    if morning_phone_texts[0] == 0:
        k "Or I can see what's up with Marlon."
    elif morning_phone_texts[1] == 0:
        k "Or I could see what Spike wants."
    k "If I want to go to the park, I should probably look up directions on my phone."
    ""
    jump phone_hold_two


label Marlontextconvo:
    hide screen phone_pop_but
    $ morning_phone_texts[0] = 1
    show bg phone marlon

    m "omg did u watch the new episode of Trashy Cryptids Trash America?"
    m "this new season is lit"
    m "ester is my faveeeee"

    menu:
        m "u up?"
        "{image=emoji/basicsmile_emoji.png} Yes, I'm awake and kicking.":
            jump m_excited_text
        "{image=emoji/basicfrown_emoji.png} No, still sleeping.":
            jump m_sleepy
        "{image=emoji/peach_emoji.png} What's Trashy Cryptids?":
            jump m_question

label m_excited_text:
    k "Yeah, I'm awake and kicking it."
    m "perf, i wanna meet up"
    m "m i gotta catch you up on the new trashy cryptids season {image=emoji/peach_emoji.png}"
    jump m_invite

label m_sleepy:
    k "No, I'm still sleeping"
    m "how u texting if yr asleep?"
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

        "{image=emoji/unicorn_emoji.png} Maybe":
            jump m_unicorn

        "{image=emoji/eggplant_emoji.png} Maybe":
            jump m_eggplant

label m_poop:
    k "{image=emoji/poop_emoji.png} Maybe" #An emoji appears.
    m "lol rude"
    m "meet me by the water fountain if ur there {image=emoji/basicsmile_emoji.png}" #An emoji appears.

    jump phone_hold_two

label m_unicorn:
    $ unicorn_marlon = True
    k "{image=emoji/unicorn_emoji.png} Maybe" #An emoji appears.
    m "ew no u kno i don't like unicorns {image=emoji/basicfrown_emoji.png}" #An emoji appears.
    k "I do?"
    m "ya, they r the woooorst"
    m "meet me by the water fountain if ur there"

    jump phone_hold_two

label m_eggplant:
    k "{image=emoji/eggplant_emoji.png} Maybe"
    m "lollllll girrrrrrrl ur g8"
    m "missed u like a lot a lot"
    m "meet me by the water fountain if ur there"

    jump phone_hold_two

label Spiketextconvo:
    hide screen phone_pop_but
    $ morning_phone_texts[1] = 1
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
            call s_thumbsup_text
        "{image=emoji/mad_emoji.png} If you insist":
            call s_mad_text
        "{image=emoji/opensmile_emoji.png} Wouldn't miss it":
            call s_opensmile_text

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
    k "I thought you said I'd only been done a few days?"
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
    show bg park entrance
    #We see the entrance of the park with its three paths.

    "Well, I made it. It's a beautiful day. The sky is grey, the birds are screaming, and the air smells like fish and chips."
    "Hmm, both Marlon and Spike wanted to meet up. The water fountain is toward the left. That's where Marlon is. I think I see Spike over toward the right, by the bench."
    "I could always just explore on my own for a bit before meeting up with them."

label parkentrancemenu:
#Leaving this here for now until we have the arrows and scene transitions in.
    menu:
        "Left towards Marlon":
            jump Marlonparkconvo

        "Right towards Spike":
            jump Spikeparkconvo

        "Enter park center" if otis_visited == False:
            jump otis_park

label otis_park:
    $ otis_visited = True
    show otis neutral

    o "Hey there, Kai. Kai, the amelioration! How lovely to see you here at the heart of the town. Have you come to admire our famous Port Madrona Tree?"

    k "Uh, right. Hey, to you too.. I'm actually here to meet up with one of my friends, but thought I might explore a bit first. What brings you here?"

    o "Well, as you know, I run the town's grand annual festival to celebrate our beloved Port Madrona tree. I like to check on her often and tend to her. After all, we have a responsibility to protect her, right? We're all connected here."

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

    k "It's definitely an interesting place.. I take it you must know a lot about it?"

    o "Better than most. However, I won't keep you from your friends. We'll have plenty of time to talk. Come find me in the maze later if you would like to know more."

    k "Okay, but I imagine I'll get there first."

    o "We'll see."
    hide otis neutral
    jump parkentrancemenu

label .k_maybe:

    k "I guess, but why you? Are you the chosen one or something?"

    o "Oh Kai, you're full of surprises! You know we choose someone annually to guard the tree year-round, but I have to say, I just don't think anyone could show her the care and attention that I can. Perhaps, it's because I study her needs."

    k "How exactly do you do that?"

    o "I make sure her environment is ideal. Make sure she receives water every 10 - 14 days until the soil is moist at a depth of just 6-inches. I prune any dead limbs, trim the outer foliage, and spray in the early spring to kill any insects or larvae that may have nested during the winter months. It's quite simple, really."

    k "Right.."
    hide otis neutral
    jump parkentrancemenu

label .k_seeyou:

    k "Yeah, sounds good. I'll see you around."

    o "Of course. Come find me in the maze later if you would like to hear more about our enchanting Port Madrona tree."
    hide otis neutral
    jump parkentrancemenu


label Marlonparkconvo:
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
    m "I can answer anything up for you if you want. I got ALL the dirt."

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
    m "I like the Glow! I actually opened it as my personal project."
    k "Really? I didn't take you as the business owner type."
    m "I wanted to open a place that would makes me feel less afraid of the dark."
    k "But, you can see in the dark, right? Why would you be scared of the dark?"
    m "I can see in the dark, but that doesn't make it any less scary. Light means comfort. Light is infinite, like I'm standing on the edge of forever while the cracks in my life are illuminated with understanding. I remember things I've forgotten. When I'm in the light, the world just...makes sense."
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
    if spike_visited == False:
        $ spike_visited = True
        show spike neutral
        s "There [she] is!"
        if marlon_visited == True:
            jump s_talked_to_marlon
        else:
            jump s_park_intro
    else:
        show spike neutral
        s "Awoo! You're back! I missed you so much!"
        jump Spikeparkmenu

label s_talked_to_marlon:
    s "Awoo! You smell like Marlon! How's my favorite mothman doing?"
    k "Unforgettable. Like usual, apparently."
    s "Hehe, definitely! I love that dude. He knows everyone's deepest, darkest secrets..."

    jump s_park_intro

label s_park_intro:

    s "I'm glad you made it!"
    k "Yeah, I managed to find it by looking at the GPS on my phone."
    s "See? That's why I let my pups use their phones during practice."
    k "Wait, your 'pups'?"
    s "Oh, sorry! That's what I call my students."
    s "But it's true! Smartphones help develop hand-eye coordination."
    s "If my pups can dribble down the court with one hand and send a text with the other, they're more skilled than I am! Maybe they should be the pack alpha instead of me!"
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
        "{image=emoji/thumbsup_emoji.png} Let's move on.":
            jump s_moveon_park

label s_lumberjack_park:

    k "So, you're basically a lumberjack?"
    s "Awoo! You bet! I'm definitely a fan of that job title. Though we don't have anything nearly so sophisticated as a lumber or saw mill here in Port M."
    k "Where do you work, then?"
    s "Oh, just a quiet, isolated cabin in the woods with only the wailing tree spirits for company."

    menu:

        "{image=emoji/eyeroll_emoji.png} Tree spirits?! Wailing?!":
            jump s_spirits_park
        "{image=emoji/sadfrown_emoji.png} Don't you get lonely?":
            jump s_lonely_park
        "{image=emoji/thumbsup_emoji.png} Let's move on.":
            jump s_moveon_park

label s_spirits_park:

    k "Wait... what do you mean {i}tree spirits{/i}?"
    s "Don't worry! I'm only kidding... partially. Maybe you'll have to come visit me to find out!"

    jump Spikeparkmenu

label s_lonely_park:
    k "An isolated cabin? Don't you ever get lonely out there by yourself in the middle of the woods?"
    s "I haven't really thought about it. No one's ever asked me that, to be honest. I suppose it does get lonely, but my condition kind of necessitates it."
    k "Oh, you mean the whole werewolf... thing?"
    s "Hahaha. Yeah, that old chestnut. It's not a big deal to me, but having one day out of the month when you can't entertain buds in your folksy cabin in the woods makes it kind of difficult to host extended sleep-overs."

    jump Spikeparkmenu

label s_weirdwood_park:
    k "What's the Weirdwood? I've seen it on my map, but no one's really told me much about it. Honestly, I'm not really enthused by that name."
    s "Oh! It's just our local haunted forest. Nothing to worry about."
    s "I'm sure you saw the outskirts of it on your way back into town. It's full of all sorts of creepies and crawlies, but if you're prepared and well-equipped, I'm sure you could handle it."
    k "Prepared how?"
    s "You could always do what I do and pack a loaded crossbow. Gets you by just as well as a firearm does without alerting the real scary forest denizens."
    s "Couple that with some of the Seer's antivenom and/or nightvision goggles, and you're good to go a-huntin' for premium wood."

    jump Spikeparkmenu

label s_moveon_park:
    k "Let's move on. Is this what you wanted to show me? It just looks like a regular old park to me."
    s "Maybe from the outside, but Otis just finished putting up the raddest hedge maze. Plus you can do a lot of people watching from the park bench here. I love to drop eaves any time of day."
    k "Tell me more about this hedge maze."
    s "Oh, I don't know much about it. Otis does something special for the festival every year. I'm sure he could tell you all about his plans, or Mayor Rain could fill you in."

    menu:

        "{image=emoji/opensmile_emoji.png} Let's go in the maze together!":
            jump s_together_park
        "{image=emoji/thumbsup_emoji.png} See you later!":
            jump s_leave_park

label s_together_park:
    k "I admit that I'm very intrigued. How about we try to navigate the maze together?"
    s "Awoo! Good idea! Who knows what kinds of goodies we could find inside?"
    k "Probably whatever's at the center?"
    s "Hahaha. Wouldn't you love to find out, though? I can just smell the adventure."
    s "Literally. Because of my wolfy nose senses. I can literally smell the adventure."

    jump Spikemazeconvo

label s_leave_park:
    k "Interesting... I'm going to walk around the park some more. See you later!"
    s "Not if I see you first!"

    hide spike neutral
    jump parkentrancemenu

label m_maze_withMaron:

    show bg maze one
    show marlon neutral

    "Turns out, this maze is more than just a family-friendly walk in the park. How do I get out of here? Marlon doesn't seem very thrilled to be in this maze. He's made himself comfortable on my shoulder and isn't being his usual self."
    "Maybe if I get him to lighten up he'll help us get through this maze. He's the one with the supernatural powers after all."

    menu:

        "I need to say something to get Marlon interested."

        "{image=emoji/tree_emoji.png} Work?" if marlon_maze_topics[0] == 0:
            $ marlon_maze_topics[0] = 1
            $ marlon_friend_score -= 5
            call m_maze_work from _call_m_maze_work
        "{image=emoji/unicorn_emoji.png} Unicorns?" if marlon_maze_topics[1] == 0:
            $ marlon_friend_score -= 5
            $ marlon_maze_topics[1] = 1
            call m_maze_unicorns from _call_m_maze_unicorns
        "{image=emoji/eggplant_emoji.png} Eileen?" if marlon_maze_topics[2] == 0:
            $ marlon_friend_score += 5
            $ marlon_maze_topics[2] = 1
            call m_maze_Eileen from _call_m_maze_Eileen
        "{image=emoji/tableflip_emoji.png} Tia?" if marlon_maze_topics[3] == 0:
            $ marlon_friend_score -= 5
            $ marlon_maze_topics[3] = 1
            call m_maze_Tia from _call_m_maze_Tia
        "{image=emoji/wink_emoji.png} Gossip?" if marlon_maze_topics[4] == 0:
            $ marlon_friend_score += 5
            $ marlon_maze_topics[4] = 1
            call m_maze_gossip from _call_m_maze_gossip
        "{image=emoji/heart_emoji.png} Dating?" if marlon_maze_topics[5] == 0:
            $ marlon_friend_score += 5
            $ marlon_maze_topics[5] = 1
            call m_maze_dating from _call_m_maze_dating
        "{image=emoji/basicsmile_emoji.png} Aesthetic?" if marlon_maze_topics[6] == 0:
            $ marlon_friend_score += 5
            $ marlon_maze_topics[6] = 1
            call m_maze_aesthetic from _call_m_maze_aesthetic

label m_maze_work:
    k "How's work been?"
    m "Lame. I really don't like talking about work. Can we not?"
    k "Oh, of course."
    "Okay, bad choice."
    return

label m_maze_unicorns:
    k "So, why DO you hate unicorns?"
    m "Wow, this again?"
    k "I'm curious, that's all."
    m "Did you know that unicorns and mothmen went to war? Yeah, that's right. It's called the Grey Rainbow War of 1983."
    k "This actually happened?"
    m "YES! Well, okay, it was less of a war and more of a final championship. And less fighting and more roller skating."
    k "So what you're saying is the mothmen lost against unicorns in a roller skating competition?"
    m "YES! IT WAS CARNAGE! Mothmen have never gotten closer to beating unicorns at roller skating than in 1983. {p=2.0} Some say we never will..."
    "Marlon doesn't seem very happy about that topic. Maybe I should let it rest."
    return

label m_maze_Eileen:
    k "So, about Eileen from Trashy Cryptids."
    m "OMG EILEEN IS THE QUEEEEEEEEEN!!!"
    m "She is my {size=+10}IDOL{/size}."
    m "This one time I sent her some fan mail and included a piece of my antennae. Don't worry. They grow back."
    "Oh geez, Marlon can't stop talking about Eileen."
    return

label m_maze_Tia:
    k "Tell me about Tia from Trashy Crypids."
    m "Wow, no thanks. Tia is honestly the worst and a waste. She ruined the last season."
    "Oh no, Marlon didn't like that at all."
    return

label m_maze_gossip:
    k "Any interesting stuff happening around town?"
    m "OH YES. So you know Ferris Castro? He's the barista at the bookstore where you work. So I was walking by one night while he was closing by himself. I don't think he noticed me looking through the window. You know how he has those antlers that grow out of his head?"
    m "Well I absolutely SWEAR I saw him TAKE OFF his antlers."
    m "Want to know what I think? I think he's hiding that fact that he's a normal human. CRAZY, RIGHT?"
    "Wow, Marlon really does have dirt on everybody in the town."
    return

label m_maze_dating:
    k "So um, what's the dating scene look like in Port Madrona?"
    m "OH. {p=1.0} Ohhhhhh, you're into somebody, aren't you?"
    k "No! I was just making conversation!"
    m "Oh yeah, I'm sure that's all it was. Don't you worry. I'm your go-to wingman any time you need it."
    "Glad to see Marlon is really loyal when it comes to dating."
    return

label m_maze_aesthetic:
    k "How would you describe your aesthetic?"
    m "Sparkly graveyard chic is what the poets call it. I call it 'being ready to cut anybody if they cross my sweet, raged-filled self.'"
    k "You really have yourself figured out."
    m "I am the change I want to see in the world."
    "Who knew mothmen were so...cut-throaty."
    return

    "Marlon friend score: [marlon_friend_score]"
    hide marlon neutral
    jump Otis_Maze_Convo

label Spikemazeconvo:

    show bg maze one
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

    s "In the pack, I teach my pups to support each other, lift up their teammates, in order to succeed. Maybe we should follow my own advice—literally!"
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

    "She's starting to freak out a little. I should say something."

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

    "Spike friend score: [spike_friend_score]"
    hide spike neutral
    show otis neutral
    if otis_visited == True:
        jump s_talked_to_otis
    else:
        jump s_otis_maze

label s_talked_to_otis:
    "Now we're suddenly face-to-face with that bird-man from before, and he's blocking our path."
    jump Otis_Maze_Convo

label s_otis_maze:
    "Now we're suddenly face-to-face with a bird-man I don't recognize, and he's blocking our path."
    jump Otis_Maze_Convo

label s_wolf_maze:
    k "Smell anything?"
    s "Awoo, yes! This way!"
    "Spike explains that she can smell something in the center of the maze. She takes my hand and leads me down a series of paths, tugging me along with frenetic certainty."
    "We proceed without trouble, making good progress, until we reach a new crossroads, and Spike stops to sniff again."
    s "I think someone got lost in here recently. They stopped to eat a snack—a tuna sandwich—but they didn't finish it. They must have discarded the remains somewhere nearby. The rotten fish smell is blocking my nose."
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
    s "Oh, uh, yeah. I like unicorns, too, I guess..."
    "Spike's enthusiasm dies out, and it distracts her from our course in the maze. She isn't entirely done with the subject of trees, though."
    return

label s_no_maze:
    "I grumpily state that I don't have a favorite tree, which seems to put an end to the conversation at last."
    "But then Spike starts, her nostrils widening. She says she's picked up a scent: the scent of blood."
    return

label s_wink_maze:
    "Spike blushes but quickly recovers and wiggles her eyebrows at me."
    s "Well, then, that would be the {i}you{/i} tree. Awoo!"
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
    s "Thank you for trusting my nose."
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
    show otis neutral

    k "How did you get here so fast?! Didn't I see you at the entrance before I came in?"

    o "Oh, I know my way around this place quite well. You see, the maze is the home of my imagination."

    o "As a child, I would run through the maze seeing myself in the Great Hall of the People or flying above the Karnak Temple Complex. It was my kingdom. It was anything I needed it to be."

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

    o "Well, the Port Madrona, also known as the Arbutus Menziesii species of the order Ericales, is native to the western regions of the North."
    o "It is an evergreen that sheds its bark with age and in the autumn produces small red berries known for their healing properties. "
    o "The tree is said to be over 400 years old with roots so deep that they span the length of the town. And when it rains, the tree appears to come to life taking in water and pumping out a rich red substance like blood stains on its leaves. "
    o "It's no wonder the tree has come to be revered as the life force of the town. Every year, I host our annual festival so we can celebrate the Port Madrona tree through song, food, sacrifices and prayer. "

    k "Wow. That's pretty amazing. It seems to have thrived here for so long. I wonder, why?"

    o "Some say, it was the Port Madrona tree that gave birth to our entire town, and as long as we honor it, it will continue to protect our home."

    k "What happens if the tree starts to die?"

    o "Don't be silly. That would never happen."
    hide otis neutral
    jump maze_center

label .k_shortversion:

    k "Alright, but keep it short will you?"

    o "Very well. The Port Madrona tree has lived here for over 400 years with roots that are said to span the length of the town."
    o "Every year, in order to ensure that the tree continues to thrive and floruish, we honor it."
    o "The town gets together and celebrates with a festival. Yusef's Crab House, the Beaver Mill Diner, the Dark Carta all donate food and entertainment to the night's festivities and, of course, we choose the guardian that will tend to the tree year-round."

    k "That sounds pretty great. Guardian, huh?"

    o "Yes, the chosen guardian will have the honor of tending to our beloved tree and ensuring no harm should befall her. "

    k "I wonder who it will be this year… this festival sounds interesting. I can't wait!"

    o "Well, surely, you remember it from last year?"

    k "Oh, right, of course. Um, I should be going now."

    o "I'll be seeing you, Kai."
    hide otis neutral
    jump maze_center

label .k_nothanks:

    k "Maybe later."

    o "No problem. I'll be around if you get curious. I promise it's quite enchanting."
    hide otis neutral
    jump maze_center

label maze_center:
    "[Companion] and I finally reach the center of the hedge maze."

    show bg maze center

    "What the hell? Is that.. No. This isn't real… is that me?! Holy shit."
    "What the hell is going on here? I don't understand. Am I dead? How can I be dead? I thought I just lost my memories, but is this all some type of pseudo world I'm living out in my head?! Oh god, I need to figure this out."
    "I can't lose it now. If I can't trust my memories, I'll need to find the answers from the people of this town. I need to remember who I am and why I came here. I can't explain it, but I know it's the only way to prevent this."
