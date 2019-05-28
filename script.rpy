label Otis_Park_Convo_Entrance_Optional

    o "Hey there, Kai. Kai, the amelioration! How lovely to see you here at the heart of the town. Have you come to admire our famous Port Madrona Tree?"

    k "Uh, right. Hey, to you too.. I'm actually here to meet up with one of my friends, but thought I might explore a bit first. What brings you here?"

    o "Well, as you know, I run the town's grand annual festival to celebrate our beloved Port Madrona tree. I like to check on her often and tend to her. After all, we have a responsibility to protect her, right? We're all connected here."

    menu:
        "{image=basicsmile_emoji.png} Absolutely!":
            jump k_absolutely
        "{image=basicfrown_emoji.png} Maybe, but why you?":
            jump k_maybe
        "{image=thumbsup_emoji.png} See you around.":
            jump k_seeyou
label .k_absolutely

    k "Of course! That's really kind of you."

    o "Why, thank you. I just like to do my part. I think I'm just utterly fascinated by our town's history."

    k "It's definitely an interesting place.. I take it you must know a lot about it?"

    o "Better than most. However, I won't keep you from your friends. We'll have plenty of time to talk. Come find me in the maze later if you would like to know more."

    k "Okay, but I imagine I'll get there first."

    o "We'll see."

label .k_maybe

    k "I guess, but why you? Are you the chosen one or something?"

    o "Oh Kai, you're full of surprises! You know we choose someone annually to guard the tree year-round, but I have to say, I just don't think anyone could show her the care and attention that I can. Perhaps, it's because I study her needs."

    k "How exactly do you do that?"

    o "I make sure her environment is ideal. Make sure she receives water every 10 - 14 days until the soil is moist at a depth of just 6-inches. I prune any dead limbs, trim the outer foliage, and spray in the early spring to kill any insects or larvae that may have nested during the winter months. It's quite simple, really."

    k "Right.."

label .k_seeyou

    k "Yeah, sounds good. I'll see you around."

    o "Of course. Come find me in the maze later if you would like to hear more about our enchanting Port Madrona tree."

label Otis_Maze_Convo

    k "How did you get here so fast?! Didn't I see you at the entrance before I came in?"

    o "Oh, I know my way around this place quite well. You see, the maze is the home of my imagination. As a child, I would run through the maze seeing myself in the Great Hall of the People or flying above the Karnak Temple Complex. It was my kingdom. It was anything I needed it to be."

    k "Sounds like a nice place."

    o "Indeed. Would you like to hear about the history of the Madrona tree?"

    menu:
        "{image=basicsmile_emoji.png} Sure!":
            jump k_sure
        "{image=basicfrown_emoji.png}Okay, but the short version.":
            jump k_shortversion
        "{image=thumbsup_emoji.png}No thanks, I'll see you around.":
            jump k_nothanks

label .k_sure

    k "I'd like that."

    o "Well, the Port Madrona, also known as the Arbutus Menziesii species of the order Ericales, is native to the western regions of the North. It is an evergreen that sheds its bark with age and in the autumn produces small red berries known for their healing properties. The tree is said to be over 400 years old with roots so deep that they span the length of the town. And when it rains, the tree appears to come to life taking in water and pumping out a rich red substance like blood stains on its leaves. It's no wonder the tree has come to be revered as the life force of the town. Every year, I host our annual festival so we can celebrate the Port Madrona tree through song, food, sacrifices and prayer. "

    k "Wow. That's pretty amazing. It seems to have thrived here for so long. I wonder, why?"

    o "Some say, it was the Port Madrona tree that gave birth to our entire town, and as long as we honor it, it will continue to protect our home."

    k "What happens if the tree starts to die?"

    o "Don't be silly. That would never happen."

label .k_shortversion

    k "Alright, but keep it short will you?"

    o "Very well. The Port Madrona tree has lived here for over 400 years with roots that are said to span the length of the town. Every year, in order to ensure that the tree continues to thrive and floruish, we honor it. The town gets together and celebrates with a festival. Yusef's Crab House, the Beaver Mill Diner, the Dark Carta all donate food and entertainment to the night's festivities and, of course, we choose the guardian that will tend to the tree year-round."

    k "That sounds pretty great. Guardian, huh?"

    o "Yes, the chosen guardian will have the honor of tending to our beloved tree and ensuring no harm should befall her. "

    k "I wonder who it will be this year… this festival sounds interesting. I can't wait!"

    o "Well, surely, you remember it from last year?"

    k "Oh, right, of course. Um, I should be going now."

    o "I'll be seeing you, Kai."

label .k_nothanks

    k "Maybe later."

    o "No problem. I'll be around if you get curious. I promise it's quite enchanting."

