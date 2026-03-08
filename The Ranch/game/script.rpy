
define player = Character("You")
define meb = Character("Mrs. Meb")
define jelle = Character("Jelle")
define poe = Character("Mr. Poe")
define jert = Character("Jert")
define nessie = Character("Nessie")
define frog = Character("Froggo the Great")
default b=0
default i=0
default p=0
default a=0
default s=0
init:
    image sky:
        "images/BAKCGROUND MAIN SKY.jpg"
    image nightsky:
        "images/BAKCGROUND MAIN SKY night.jpg"
    image player:
        "images/player.webp"
    image meb:
        "images/mrs meb.webp"
    image jelle:
        "images/jelle.webp"
    image jert:
        "images/jert.webp"
    image frog:
        "images/froggo.webp"
    image fishing:
        "images/skyfishing.png"
    image insidepond:
        "images/froggoinside.png"
    image inside:
        "images/inside.png"
    image secret:
        "images/secretencounter.png"
    image tomatojam:
        "images/tomatojam.webp"
    image icecream:
        "images/icecream.webp"
    image milkshake:
        "images/milkshake.webp"
    image poe:
        "images/poe.webp"
    image end:
        "images/end.png"
    image start:
        "images/map.png"
    image monster:
        "images/monster.webp"
label start:
    show start with Fade(1.0,0.0,3.0)
    scene sky with fade
    show player with dissolve:
        zoom 1.5
        yalign 1.0
    "The sky is a deep shade of Rot because of your cheap sunglasses. You don't take them off for the bright orange light to caress your little eyes."
    "The car draws close to the ranch, a pristine metal nameplate hangs over the main gate."
    "It reads \"The Silverkine Ranch\". You look at the neatly folded envelope inside your fanny pack and confirm that you are in the right place."
    "You pay the cab and walk into the ranch. There's a plethora of animal noises. You go toward the tiny cottage with smoke bellowing out."
    "You knock the door, noticing the nameplate next to the door jamb."
    show meb  at right with dissolve:
        zoom 1.5
    meb "Oh Hello! You must be the one Mr Poe sent for, please come in."
    "The smell of tomatoes fill your nostrils as you see Mrs. Meb making her patent pending tomato jam."
    meb "Would you like to try some tomato jam?"
    player "Oh actually..."
    menu:
        "What do you say?"
        "Thank you! But I just ate breakfast at the Moorekeeper's Inn on the way here! Maybe some other time!":
            meb "Oh thats alright. There's always another time."
            jump pond
        "Im really sorry, but I'm allergic to tomatoes.":
            jump allergy
        "Tomato jam seems really nice, I'd love to try some!":
            jump tomatojam
    return
label pond:
    meb "Why don't you go meet Jelle! She'll help you with your things."
    player "That's awesome, Thanks for having me!"
    meb "Jut be here by 8pm, I'm hosting a small party of sorts for you!"
    hide meb with dissolve
    jump firstpondencounter
label firstpondencounter:
    scene sky with fade
    show player with dissolve:
        zoom 1.5
        yalign 1.0
    "Along the well trodden path you go carrying your fanny pack and a tiny suitcase of clothes. You think about the peculiar student exchange opportunity that bought you here."
    "....."
    "You are distracted by the distant pond which seems to be glowing in the distance."
    menu:
        "What do you do?"
        "Walk up to the pond and investigate.":
            jump jert
        "Continue on to meet Jelle.":
            jump jelle
label allergy:
    meb "That's unfortunate. Would you like to try my patented olive bark ice-cream!"
    player "That sounds..."
    menu:
        "How does it sound?"
        "Awesome!!!! I LOVE ICECREAM":
            $i=0
            jump icecream
        "I'm awfully sorry, I have the worst cold in like ever. Maybe after I feel better.":
            meb "Oh thats alright. There's always another time."
            jump pond
label tomatojam:
    meb "That's nice to hear! Let me find some nice bread for you to eat it with!"
    "You leave your things in the hallway and follow Mrs. Meb into what seems to be the kitchen."
    scene inside with fade
    show player with dissolve:
        zoom 1.5
        yalign 1.0
    show meb  at right with dissolve:
        zoom 1.5
    "There are lots and LOTS of tomatoes in huge rucksacks all ripe the same colour of Rot. You can faintly catch a glimpse of the vast tomato plantantion through the ajar backdoor"
    meb "Here you go! I just baked this almond sap bread! Hope you like it."
    show tomatojam at right with dissolve 
    "The tomato jam and almond sap bread go well together!"
    hide tomatojam with dissolve
    jump pond
label icecream:
    if i<5:
        if i!=0:
            "Mrs. Meb rushes in."
        meb "That's just perfect! Let me fetch you a bowl!"
        if i==0:
            "You leave your things in the hallway and follow Mrs. Meb into what seems to be the kitchen."
            scene inside
            show player with dissolve:
                zoom 1.5
                yalign 1.0
            show meb at right with dissolve:
                zoom 1.5
            "There are lots and LOTS of tomatoes in huge rucksacks all ripe the same colour of Rot. You can faintly catch a glimpse of the vast tomato plantantion through the ajar backdoor"
        meb "Here you go!"
        show icecream with dissolve
        "The olive bark icecream is really refreshing."
        hide icecream with dissolve
        if i==0:
            "Mrs. Meb goes out through the back door."
            hide meb with dissolve
        else:
            "Mrs. Meb goes out the back door again!"
            hide meb with dissolve
        menu:
            "What do you do?"
            "Follow Mrs. Meb out the back door.":
                jump backdoor
            "Request another bowl of icecream.":
                show meb at right with dissolve:
                    zoom 1.5
                $i+=1
                jump icecream
            "Wait for Mrs. Meb to be back.":
                "......."
                "You keep waitin."
                "Mrs. Meb comes back in."
                show meb at right with dissolve:
                    zoom 1.5
                "Oh, are you done already?"
                $p=1
                jump pond
    else:
        meb "I'm sorry, we're out of icecream."
        jump secretencounter
label backdoor:
    $b=1
    "You finish your icecream and walk toward the door, you slowly push the door forward."
    scene sky with fade
    "It is the most glorious sight of your life! You see rows and rows of tomato plants full of Rot coloured tomatoes."
    show meb at right with dissolve:
        zoom 1.5
    show player with dissolve:
        zoom 1.5
        yalign 1.0
    meb "This is the result of over 10 years of \"tomato-ing\" Mr Meb loved my tomato jam. This is my way of remembering him."
    "Mrs. Meb wipes a tiny droplet of tear that formed with her Rot coloured handkerchief that appropriately had tomatoes embroidered into."
    meb "Come on, let me accompany you to Jelle's little hut! She's the best help anyone can ask for. Bless her heart."
    "You quickly grab your things and follow Mrs Meb out into the field."
    "RIIIINGGG RIIIIINGG"
    meb "Oh, that's the landline. It has to be Mr Poe calling to ask about you. Why don't you continue along this path. You'll know where to stop when you see it!"
    hide meb with dissolve
    $p=1
    jump firstpondencounter
label jert:
    show jert at right with dissolve:
        zoom 1.5
    "A young man blocks your way."
    jert "You must be the new guy. Mr Poe told me all about you."
    "You don't like the look of him very much."
    jert "I'm Jert the ranch's head engineer"
    jert "... the only engineer."
    "The pond stops glowing. You choose to continue on the path."
    hide jert with dissolve
    jump jelle
label jelle:
    "After a new seconds of walking you feel tired."
    "That's when you notice a tiny hut which looks like a mushroom over by the huge lake."
    show jelle at right with dissolve:
        zoom 1.5
    "A girl comes out holding a rake."
    jelle "Hi! You must be the new exchange student! I'm Jelle, the caretaker of basically everything here!"
    jelle "Follow me, I'll show you your quarters for the duration of the trip!"
    "You follow Jelle down the road and find a smaller mushroom hut near the larger one."
    jelle "You'll stay here! Make yourself comfortable and meet me out by the lake. I'll tell you what you have to do in the ranch."
    "You walk inside and fine a nice cozy bed with a fireplace next to it."
    player "This is so nice!"
    "You quickly get ready for a long day of work at the ranch!"
    jelle "We're opening the ranch to tourists next week so there's a lot to plan!"
    jelle "So what do you want to do for the day?"
    menu:
        "What job do you want?"
        "Work with Jert and help him add the solar panels and nightlights all over the ranch.":
            jump solar
        "Work with Jelle and go fishing in the lake for the rare and elusive silver trout.":
            jump lakefishing
        "Work alone and install fences all along the sides of the well trodden path to Jelle's Hut.":
            jump fence  
label lakefishing:
    jelle "That's awesome! Let me go bring the bait and the equipment. Set up the kayaks for me please."
    "You finish setting up the kayaks and row toward the middle of the lake."
    scene skyfishing with fade
    show player with dissolve:
        zoom 1.5
        yalign 1.0
    show jelle at right with dissolve:
        zoom 1.5
    jelle "Remember, when you catch the silver trout...."
    nessie "GRBRNRRRRRRRNNNNRNNNNNN"
    "Nessie's scream has hindered your ability to hear."
    menu:
        "What do you do?"
        "Follow the scream":
            jump nessieencounter
        "Ask Jelle about the silver trout.":
            jump jellecatch
        "Ignore it and keep fishing.":
            jump youcatch
label jellecatch:
    "You see Jelle struggling to reel her line in."
    jelle "Nevermind that, I have one on my line now."
    "After a few seconds of struggling, she successfully has a silvertrout in her hands."
    jelle "That's all we need for dinner tonight! We're having a party afterall!"
    jelle "After we get back to the huts, why don't you go get ready for the party. It's getting dark soon."
    jump secondpondencounter
label youcatch:
    "You continue waiting for your fish."
    jelle "So how's the ranch life treating you?"
    "The string suddenly goes taut. You have your very own silver trout!"
    jelle "Thats it! PULL!"
    "You successfully catch the silver trout!"
    jelle "That's all we need for dinner tonight! We're having a party afterall!"
    jelle "After we get back to the huts, why don't you go get ready for the party. It's getting dark soon."
    jump secondpondencounter
label nessieencounter:
    "You ignore the fishing duties and follow the scream."
    jelle "It's alright! I can fish for the silver trout myself. Maybe tomorro......"
    "Jelle's voice fades as you move farther and farther."
    hide jelle with dissolve
    "The light dims as dusk begins."
    nessie "GNRNSSNSSSSNSNNSNSS"
    "You hear Nessie again"
    player "This is really boring, I should get back to the Party."
    "Something rams past your kayak and you lose balance."
    player "Okay this is really creepy now."
    "You try turning back but something has you anchored in."
    show jert at right with dissolve:
        zoom 1.5
    jert "HEY! WHAT ARE YOU DOING HERE?"
    jert "You're not supposed to be here in this part of the lake."
    "Jert is up on top of a night lamp plugging in a comically large light bulb."
    menu:
        "What do you do?"
        "Ignore Jert":
            jump nessiehelp
        "Ask for help":
            jump jerthelp
label jerthelp:
    jert "Alright, this is Nessie's territory. We choose to let her be."
    "Jert comes over to the lake and swims toward the kayak and pulls it on to the shore."
    "You are very surprised by the strength Jert has"
    nessie "MERMRMNSMAN (it sounds sadder)"
    jert "I will be taking this up with Mrs. Meb. This is what happens when we let random kids into the ranch."
    "You quickly run away from Jert"
    "It starts getting dark around you"
    jump secondpondencounter
label nessiehelp:
    hide jert with dissolve
    "You row as fast as you can and go further into the depths of the lake."
    "It gets darker and darker as you go in."
    nessie "HEASDHASJJAHSDIISJK"
    "Suddenly your kayak starts moving very fast. Something is pushing you from the back."
    scene nightsky with fade
    "You somehow end up at the side of the well trodden path! There is a lot of light here thanks to Jert."
    "You get off and start walking towards your hut to get a new pair of clothes."
    jump secondpondencounter
label secondpondencounter:
    scene nightsky
    show player with dissolve:
        zoom 1.5
        yalign 1.0
    "You see the pond again. It is glowing brighter than ever before."
    menu:
        "What do you do?"
        "Ignore the pond and get ready for the party.":
            jump party
        "Ignore the party and start exploring the pond.":
            jump finalpondencounter

label solar:
    jelle "Alright! Just walk along the well trodden path until you meet Jert along the way!"
    "You start walking back."
    hide jelle with dissolve
    "After a while you finally meet Jert."
    show jert at right with dissolve:
        zoom 1.5
    jert "So, you wanna work with me?"
    jert "The first thing you'll do is to make me a milkshake. Use Mrs. Meb's olive bark icecream and tomato jam."
    jump tomilkshakeornottomilkshake
label tomilkshakeornottomilkshake:
    menu:
        "What do you do?"
        "Make Jert his milkshake." if a!=1:
            jump milkshake
        "Run away from Jert and go fishing with Jelle.":
            "You run away from Jert and go back to the mushroom huts."
            hide jert with dissolve
            show jelle at right with dissolve:
                zoom 1.5
            "You see Jelle."
            player "I changed my mind, can I go fishing with you?"
            jump lakefishing
        "Run away to work on the fence":
            "You walk back to Jelle's hut."
            hide jert with dissolve
            show jelle at right with dissolve:
                zoom 1.5
            player "I changed my mind. Can I work on the fence instead?"
            jump fence
label fence:
    jelle "Alright!! You can go up to Jert's workspace and get some of the fenceposts and a mallet. Start from here and move toward the stables then to Mrs. Meb's cottage!"
    hide jelle with dissolve
    "You walk over to Jert's workspace hoping to not run into him."
    "You bring a wagon full of supplies with you and start pushing down the fenceposts."
    "It is mundane work but you like being in the silence."
    if b==1:
        show meb at right with dissolve:
            zoom 1.5
        meb "Oh look at you working hard on your first day! Here! I bought your favourite olive bark icecream.. but in the form of a refreshing milkshake!"
        show milkshake at right with dissolve
        "You thank Mrs. Meb and take a sip of the milkshake!"
        "It fills you up with determination and you finish the fence job a few hours earlier than you expected!"
        menu:
            "What do you want to do?"
            "Add a line of fence to the stables.":
                "You go back to Jert's workspace and get more supplies and start fencing the path to the stables."
            "Go find Jelle and try lake fishing!":
                jump lakefishing
    scene nightsky
    show player with dissolve:
        zoom 1.5
        yalign 1.0
    "The sun slowly fades down the horizon and Jert's nightlights pump into action."
    "You finally finish the fence and you look around for your wagon."
    "You do not find your wagon.."
    "Instead a glowing pond catches your eye from the distance. Its the same pond!"
    menu:
        "What do you do?"
        "Explore the pond.":
            jump finalpondencounter
        "Ignore the pond and get back to the huts.":
            "You walk back to Jert's workspce and leave the wagon and supplies."
            jump party   
label milkshake:
    if i>=5:
        player "I ate all the icecream."
        jump tomilkshakeornottomilkshake
        $a=1
    else:
        hide jert with dissolve
        "You go to Mrs. Meb's cottage to see if she has more icecream."
        scene inside with fade
        if b==1:
            show meb at right with dissolve:
                zoom 1.5
            meb "I was just about to bring you olive bark milkshake! This is a happy coincidence."
            show milkshake at right with dissolve
            "You ignore Jert's request and drink the milkshake yourself"
            menu:
                "What do you do now?"
                "Work with Jelle and try lakefishing.":
                    hide jert with dissolve
                    "You walk back to Jelle's hut."
                    show jelle at right with dissolve:
                        zoom 1.5
                    player "I changed my mind, can I fish with you instead?"
                    jump lakefishing
                "Work on the fence.":
                    hide jert with dissolve
                    "You walk back to Jelle's hut."
                    show jelle at right with dissolve:
                        zoom 1.5
                    player "I changed my mind, can I work on the fence?"
                    jump fence
        else:
            "You make Jert his milkshake and bring it to him."
            scene sky with fade
            show player with dissolve:
                zoom 1.5
                yalign 1.0
            show jert at right with dissolve:
                zoom 1.5
            jert "Now go away. Let me work in peace."
            menu:
                "What do you do?"
                "What do you do now?"
                "Work with Jelle and try lakefishing.":
                    hide jert with dissolve
                    "You walk back to Jelle's hut."
                    show jelle at right with dissolve:
                        zoom 1.5
                    player "Jert sent me off, can I fish with you instead?"
                    jump lakefishing
                "Work on the fence.":
                    hide jert with dissolve
                    "You walk back to Jelle's hut."
                    show jelle at right with dissolve:
                        zoom 1.5
                    player "Jert sent me off, can I work on the fence?"
                    jump fence
label secretencounter:
    meb "Wait, on second thought. I'll go look if we have more icecream in the basement frezer"
    "RIIING RIIIING"
    meb "Wait a while dear. Don't go down without me."
    hide meb with dissolve
    "Mrs. Meb runs away to pick the call."
    "You start losing your patience."
    "You decide to go down to the basement freezer yourself."
    scene secretencounter with fade
    show player with dissolve:
        zoom 1.5
        yalign 1.0
    "You open the latch next to the backdoor and decend."
    "The walk in freezer is at the end of the stairs. You open it"
    "It is very cold...."
    "You finally find the icecream section and rummage through the piles of boxes to find the one you need. The olive bark icecream."
    "You instead fine a tomato jam box labelled \"Memories\""
    "You open it"
    "There's a bunch of postcards of people and lots of random trinkets and bracelets and other junk of sorts"
    "You also find a lot of folded notes. You take it out of the shelf and decide to read them."
    "\"Day 1 at the ranch!\" \n \"Mrs. Meb is a really nice woman! I love her olive bark icecream!\" \n \"Day 18 at the ranch\" \"I cannot seem to stop eating the icecream and something about the eerie pond in this ranch irks me out\" It seems to be logs of a previous rancher here."
    "You look at the photographs and realise that there is a boy in all of it. He is about your age too."
    "Things get silent and you feel this eerie sensation in your spine."
    show meb at right with dissolve:
        zoom 1.5
    meb "I told you not to wander into the freezer dear."
    meb "It was for your own good."
    "Mrs Meb smiles in a soft way........almost selling the act."
    meb "This is exactly what happened to the other exchange student."
    "Mrs. Meb grabs a pint of icecream and starts eating it. She slowly turns blue and starts sorta melting."
    hide meb with dissolve
    show monster at right with dissolve:
        zoom 1.5
    "She becomes THE ICECREAM GOBLIN."
    "You try to bolt past her."
    meb "YOU SHALL NOT PASS"
    "She reaches out and grabs you against the wall."
    "She grabs a ball of icecream and flings it at your face."
    "Everything goes black."
    "......................."
    scene inside with fade
    show meb at right with dissolve:
        zoom 1.5
    meb "Oh dear, are you alright?"
    "You open your eyes."
    show player with dissolve:
        zoom 1.5
        yalign 1.0
    player "Where am I?"
    "You look around and realise that you are in the living room."
    meb "I'm extremely sorry my dear, I might have accidentally topped the icecream with my tomato jam."
    meb "The doctors here tell me that you hallucinated your way through the day. They treated you but I will understand if you want to go back home"
    "Your parents are here"
    player "I guess my student exchange is a fail"
    window hide
    show end with Fade(1.0,0.0,3.0)
    return

label party:
    "You reach your hut and realise that Jelle has already left for Mrs. Meb's cottage. You quickly get dressed and leave as fast as you can."
    "You finally reach Mrs. Meb's cottage! You knock on the door."
    scene inside with fade
    show player with dissolve:
        zoom 1.5
        yalign 1.0
    show jert at right with dissolve:
        zoom 1.5
    jert "Oh its you. You seem late for your own party"
    hide jert with dissolve
    show meb at right with dissolve:
        zoom 1.5
    meb "Its fine Jert! You aren't late at all dear. We're waiting for Mr. Poe to arrive so we can all celebrate!"
    "After a while of waiting and having fun talking to Jelle and Mrs. Meb someone knocks the door."
    poe "Hello! You must be the exchange student! How are you?"
    poe "I'm Mr. Poe! The local bank manager. I take care of most of the things happening around the ranch. I remember my own days of working here."
    meb "Oh yes, you would try stealing all the tomatoes to feed the silverkine. But I always caught you."
    poe "I would always be caught red handed. Literally"
    "Everyone laughs, even Jert."
    jelle "Okay, I think its time we bring out the cake!"
    player "A cake!! For me? You didn't have to."
    meb "Nonsense! Its your first day here!"
    "They bring out the cake and your face lights up with joy!"
    "It reads \"For the best rancher anyone could ask for\""
    "Everyone eats the cake and they all gather round the TV next to the fireplace for a surprise movie night."
    "You look around and then as the movie starts to play, you feel a peculiar sense of calm."
    "The ranch finally feels like home..."
    window hide
    show end with Fade(1.0,0.0,5.0)
    return
label finalpondencounter:
    "You walk toward the pond. Looking around for any signs of danger. Jert's night lights do not reach this far, so the only source of light is the glowof the pond."
    "You get down and inspect the pond."
    "SPLASH!"
    show frog at right with dissolve
    "A tiny frog jumps out. It is wearing a tophat and a monocle!"
    frog "Welcome! I am Froggo the Great!"
    if p!=0:
        frog "URGH!! You stink of olive bark icecream. Begone mortal! At once!!"
        hide frog with dissolve
        "You decide to leave. You feel dissapointed."
        jump party
    else:
        frog "Follow me into the pond and I shall show you the meaning of a Rancher!"
        "You jump inside the pond."
        scene insidepond with fade
        show player with dissolve:
            zoom 1.5
            yalign 1.0
        show frog at right with dissolve
        "You emerge out into a tiny \'hobbit hole\'-esque area and see what you might expect in a teenager's bedroom."
        "The really tiny game console is on and the tv is running a crude version of Forza"
        frog "This is my home! But besides that. Care to join me for a match? I will reveal the truth once you beat me ingame."
        menu:
            "What do you do?"
            "You accept the offer and play!":
                jump frogplay
            "You decline the offer and get back to the party":
                jump aftermath
label aftermath:
    scene nightsky with fade
    show player with dissolve:
        zoom 1.5
        yalign 1.0
    "You emerge out of the pond fully dry. The owls are hooting in the distance and the moon is directly over you."
    "You are extremely late for the party. You run down to Mrs. Meb's cottage."
    "You knock on the door."
    show poe at right with dissolve:
        zoom 1.5
    poe "Now you show up!"
    poe "I'm Mr. Poe the local banker. Mrs. Meb was very dissapointed you didn't show up."
    poe "She has sold the ranch off to the Ketchup buiness in the next town and decided to move to The Bahamas and enjoy her retirement."
    hide poe with dissolve
    show jert at right with dissolve:
        zoom 1.5
    jert "I hope youre happy now!"
    hide jert with dissolve
    show jelle at right with dissolve:
        zoom 1.5
    jelle ".............."
    "You feel a sense of dread creeping up"
    poe "Your parents are inside. They're taking you back home."
    scene inside with fade
    if s==1:
        show player with dissolve:
            zoom 1.5
            yalign 1.0
        show icecream with dissolve
        "You find a cup of olive bark ice cream. Although it is completely a liquid now."
        "You take a sip of it, ignoring the spoon."
        player "URGH, who likes olive bark?"
        hide icecream
        "You leave it there."
    player "I guess my summer exchange is a fail."
    window hide
    show end with Fade(1.0,0.0,3.0)
    return
label frogplay:
    "You play the knockoff version of Forza with the frog. You actually have human sized controllers."
    frog "You're going down human!"
    "After a very long gaming session. The frog wins."
    "Obviously. It's a frog which plays video games."
    frog "Fret not, for I have something to give you."
    "He reaches out into his \"pockets\" and takes an intricately carved spoon out."
    frog "Go on, go eat the olive bark icecream Mrs. Meb makes"
    $s=1
    jump aftermath
