# The script of the game goes in this file.

# Define character affection stats
default marlon_friend_score = 0
default spike_friend_score = 10
default unicorn_marlon = False

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character(_("Kai"), color="#aa6f73")
define m = Character(_("Marlon"), color="#7e6a7c")
define s = Character(_("Spike"), color="#ac330f")
define o = Character(_("Otis"), color="#f9d62e")

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
    m "m i gotta catch you up on the new trashy cryptids season {image=emoji/peach_emoji.png}"

    jump m_invite

label m_nervous:
    k "No, I'm still sleeping"
    m "how u texting if yr asleep?"
    k "It's one of the world's greatest mysteries I guess"

    m "lol" 

    m "i gotta catch you up on the new trashy cryptids season {image=emoji/peach_emoji.png}" #An emoji appears.

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
        "Maybe {image=emoji/poop_emoji.png}":
            jump m_poop

        "Maybe {image=emoji/unicorn_emoji.png}":
            jump m_unicorn

        "Maybe {image=emoji/eggplant_emoji.png}":
            jump m_eggplant

label m_poop:
    k "Maybe {image=emoji/poop_emoji.png}" #An emoji appears.
    m "lol rude"
    m "meet me by the water fountain if ur there {image=emoji/basicsmile_emoji.png}" #An emoji appears.

    jump parkentrance

label m_unicorn:
    $ unicorn_marlon = True
    k "Maybe {image=emoji/unicorn_emoji.png}" #An emoji appears.
    m "ew no u kno i don't like unicorns {image=emoji/basicfrown_emoji.png}" #An emoji appears.
    k "I do?"
    m "ya, they r the woooorst"
    m "meet me by the water fountain if ur there"

    jump parkentrance

label m_eggplant:
    k "Maybe {image=emoji/eggplant_emoji.png}"
    m "lollllll ur g8"
    m "missed u like a lot a lot"
    m "meet me by the water fountain if ur there"

    jump parkentrance

label Spiketextconvo:

    s "hey kai!! good afternoon sleepyhead"
    k "It's still morning, Spike..."
    s "oh you're right... well it's time to get up and greet the day! what are your plans?"

    menu:
        "{image=emoji/basicsmile_emoji.png}Explore the town":
            call s_smile_text
        "{image=emoji/basicfrown_emoji.png}Probably sulk":
            call s_frown_text
        "{image=emoji/eggplant_emoji.png}Spend time with you":
            call s_eggplant1_text

    s "what do you say to a meet-up? i have some time before bball practice this afternoon"
    k "...what did you have in mind?"
    s "it's a surprise! i promise you won't regret it :) just come to the park in 20"
    s "meet me by the park bench, but don't sit on it because my invisible friend might be there"
    k "Invisible friend? Don't you mean {i}imaginary{/i} friend?"
    s "nope! they're invisible, and they really hate it when people sit on them"
    s "so can i count on you?"

    menu:
        "{image=emoji/thumbsup_emoji.png}See you there!":
            jump s_thumbsup_text
        "{image=emoji/poop_emoji.png}If you insist":
            jump s_poop_text
        "{image=emoji/eggplant_emoji.png}Wouldn't miss it":
            jump s_eggplant2_text

label s_smile_text:
    k "I thought I'd try to explore the town some more and get back into the swing of things"
    k "This is supposed to be my home, but I feel like I know nothing about it"
    s "don't worry! we'll soon have you back to normal in no time!"
    k "I hope you're right"

    return

label s_frown_text:
    k "Oh, I thought I would just sulk in bed for a bit, then wander around in an aimless haze"
    s "we can't have any of that! you've got to keep active, otherwise your muscles will all shrivel up from disuse~"
    k "Thanks, Spike. That's a nice thought."

    return

label s_eggplant1_text:
    k "I was actually hoping you had time to hang out today... interested?"
    s "awoo definitely! it's been so long since we had fun like we used to ;)"
    k "I thought you said I'd only been done a few days?"
    s "like i said. so. long."

    return

label s_thumbsup_text:
    k "{image=emoji/thumbsup_emoji.png}"
    k "See you there!"
    s "can't wait! i'll be the attractive one with the wolf aesthetic."

    jump parkentrance

label s_poop_text:
    k "Fine, but I won't be happy about it"
    s "you're no fun :( don't worry, i can fix that! see you soon!"

    jump parkentrance

label s_eggplant2_text:
    k "I wouldn't miss it! As long as we don't get seriously injured or something"
    s "just you wait... i'll take you to all sorts of places next ;)"

    jump parkentrance

label parkentrance:

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

        "Enter park center":
            jump Otisparkconvo

label Marlonparkconvo:

    m "Oh looky loo. You made it! What took you so long?"
        if spike_visited == True:
	        m_talked_to_spike
        else:
            m_long_morning

label m_talked_to_spike:

    k "I met up with Spike real quick before meeting up with you."
    m "Fun! I love Spike. It's all 'awoooos' and sweat with her."

    jump m_kai_weird_greetings

label m_long_morning:

    k "It's been a hectic morning."
    m "Oh no buddy! Why's that?"

    jump m_kai_weird_greetings

m_kai_weird_greetings:
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
    m "That's disgusting and…a little cool. {p=1.0} You'll remember something! I'm unforgettable after all."
    k "Thanks, Marlon."
    m "I can answer anything up for you if you want. I got ALL the dirt."

    jump Marlonparkmenu

label Marlonparkmenu:
    menu:
        "Tell me about you.":
            jump m_aboutMarlon
        "Tell me about The Glow.":
            jump m_aboutGlow
        "Let's talk about something else."
            jump m_somethingelse

label m_aboutMarlon:
    k "What's your thing? What are you all about?"
    m "Trashy Cryptids Trash America obv."
    k "Did you just use 'obv' in real life conversation?"
    m "Yeah. Obv. Eileen is ALL about that I-R-L slang. She is the QUEEEEEEEN."
    k "So, what's this show about?"
    m "So it's a group of five best friends who road trip around America and change people's lives with their weirdness. It's actually very wholesome and everyone has their shit together."
    m "Except for Tia. Tia is a mess."

        menu:
            "Eileen?":
                jump m_aboutEileen
            "Tia?":
                jump m_aboutTia
            "Let's move on.":
                jump m_moveOn

label m_aboutEileen:
    k "So who is Eileen? Is she your favorite? Wait, let me rephrase. Is she your {i}fave{/i}?"
    m "Ew, no, please don't say 'fave.' That's so two years ago."
    m "Eileen is {size=+10}THE COOLEST{/size}. She is a half-woman, half-shark ghost and gives no fucks about what anyone thinks of her. She is just soooo authentic."
    return

label m_aboutTia:
    k "Who is Tia?"
    m "Ugh, don't get me started on Tia. Tia is this basic vampire who does this annoying clicking thing with her teeth when she's excited."
    m "Tia replaced Kimmi last season because there was some drama between Kimmi and Lucretia. They should have worked it out, but instead Kimmi left and we're stuck with Tia."
    k Fascinating.
    m "{size=+10}I KNOOOOOOOWWWW.{/size}"
    return
    
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
    m ...
    m ...
    k ...
    k "Buddy.{p=2.0}That was deep."
    m "Was it? Oops."

    jump Marlonparkmenu

label m_somethingelse:
    k "Let's explore or something."
    m "Oh, you probably want to check out that maze, right? Otis made a weird-ass hedge maze this year for the festival. I don't get it."

    menu:
        "Let's go in the maze together!":
            jump m_enterMaze
        "See you later!":
            jump m_seeYouLater

label m_enterMaze:
    k "I'm intrigued by the maze's weirdness. Maybe he hid something in the middle."
    m "Like treasure? Or gift cards!"
    k "How about we check it out? We can split our findings."
    m "Dibs on the gift cards."

    jump m_maze_withMaron

label: m_seeYouLater:
    k "Interesting...well, I'm going to keep looking around this park. See you later!"
    m "See ya, buddy."

    jump parkentrancemenu

label Spikeparkconvo:

    $ spike_visited = True
    s "There [she] is! Hey, Kai, you made it!"
    k "Hey, Spike. Yeah I managed to find it by looking at the GPS on my phone."
    s "See? That's why I let my students use their phones during practice. Smartphones help develop hand-eye coordination."
    s "If kids can dribble down the court with one hand and send a text with the other, they're more skilled than I am!"
    k "So you just coach basketball at the high school? Do you teach any other subjects?"
    s "Nope! Just basketball! When I'm not coaching, you can find me in the Weirdwood. I chop down trees and sell quality, non-haunted logs to anyone who needs 'em!"

    jump Spikeparkmenu

label Spikeparkmenu:
    s "So... whaddaya think?"

    menu:
        "{image=basicsmile_emoji.png}You're a lumberjack?":
            jump s_lumberjack
        "{image=basicfrown_emoji.png}Um, the Weirdwood?":
            jump s_wood
        "{image=thumbsup_emoji.png}Let's move on.":
            jump s_moveon

label s_lumberjack:
    k "So, you're basically a lumberjack?"
    s "Awoo! You bet! I'm definitely a fan of that job title. Though we don't have anything nearly so sophisticated as a lumber or saw mill here in Port M."
    k "Where do you work, then?"
    s "Oh, just a quiet, isolated cabin in the woods with only the wailing tree spirits for company."

    menu:
        "{image=basicfrown_emoji.png}Tree spirits?! Wailing?!":
            jump s_spirits
        "{image=eggplant_emoji.png}Don't you get lonely?":
            jump s_lonely
        "{image=thumbsup_emoji.png}Let's move on.":
            jump s_moveon

label s_spirits:
    k "Wait... what do you mean {i}tree spirits{/i}?"
    s "Don't worry! I'm only kidding... partially. Maybe you'll have to come visit me to find out!"

    jump Spikeparkmenu

label s_lonely:
    k "An isolated cabin? Don't you ever get lonely out there by yourself in the middle of the woods?"
    s "I haven't really thought about it. No one's ever asked me that, to be honest. I suppose it does get lonely, but my condition kind of necessitates it."
    k "Oh, you mean the whole werewolf... thing?"
    s "Hahaha. Yeah, that old chestnut. It's not a big deal to me, but having one day out of the month when you can't entertain buds in your folksy cabin in the woods makes it kind of difficult to host extended sleep-overs."

    jump Spikeparkmenu

label s_wood:
    k "What's the Weirdwood? I've seen it on my map, but no one's really told me much about it. Honestly, I'm not really enthused by that name."
    s "Oh! It's just our local haunted forest. Nothing to worry about."
    s "I'm sure you saw the outskirts of it on your way back into town. It's full of all sorts of creepies and crawlies, but if you're prepared and well-equipped, I'm sure you could handle it."
    k "Prepared how?"
    s "You could always do what I do and pack a loaded crossbow. Gets you by just as well as a firearm without alerting the real scary forest denizens."
    s "Couple that with some of the Seer's antivenom and/or nightvision goggles, and you're good to go a-huntin' for those premium logs."

    jump Spikeparkmenu

label s_moveon:
    k "Let's move on. Is this what you wanted to show me? It just looks like a regular old park to me."
    s "Maybe from the outside, but Otis just finished putting up the raddest hedge maze. Plus you can do a lot of people watching from the park bench here. I love to drop eaves any time of day."
    k "Tell me more about this hedge maze."
    s "Oh, I don't know much about it. Otis does something special for the festival every year. I'm sure he could tell you all about his plans, or Mayor Rain could fill you in."

    menu:
        "{image=basicsmile_emoji.png}Let's go in the maze together!":
            jump s_together
        "{image=thumbsup_emoji.png}See you later!":
            jump s_leave

label s_together:
    k "I admit that I'm very intrigued. How about we try to navigate the maze together?"
    s "Awoo! Good idea! Who knows what kinds of goodies we could find inside?"
    k "Probably whatever's at the center?"
    s "Hahaha. Wouldn't you love to find out, though? I can just smell the adventure."
    s "Literally. Because of my wolfy nose senses. I can literally smell the adventure."

    jump maze

label s_leave:
    k "Interesting... I'm going to walk around the park some more. See you later!"
    s "Not if I see you first!"

    jump parkentrancemenu

label s_maze_withSpike:
#Placeholder for maze stuff

label m_maze_withMaron:

    show bg maze one

    "Turns out, this maze is more than just a family-friendly walk in the park. How do I get out of here? Marlon doesn't seem very thrilled to be in this maze. He's made himself comfortable on my shoulder and isn't being his usual self."
    "Maybe if I get him to lighten up he'll help us get through this maze. He's the one with the supernatural powers after all."

    menu:

        "I need to say something to get Marlon interested."

        "Work?":
            $ marlon_friend_score -= 5
            call m_maze_work
        "Unicorns?":
            $ marlon_friend_score -= 5
            call m_maze_unicorns
        "Eileen?":
            $ marlon_friend_score += 5
            call m_maze_Eileen
        "Tia?":
            $ marlon_friend_score -= 5
            call m_maze_Tia
        "Gossip?":
            $ marlon_friend_score += 5
            call m_maze_gossip
        "Dating?":
            $ marlon_friend_score += 5
            call m_maze_dating
        "Aesthetic?":
            $ marlon_friend_score += 5
            call m_maze_aesthetic

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
    m "OH YES. So you know Ferris Castro? He's the barista at the bookstore you work. So I was walking by one night while he was closing by himself. I don't think he noticed me looking through the window. You know how he has those antlers that grow out of his head?" 
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
    "Who knew mothmen were so…cut-throaty."
    return
    
    "Marlon friend score: [marlon_friend_score]" 
    jump end_of_maze



label end_of_maze:
    "SPOOKY SHIT"
