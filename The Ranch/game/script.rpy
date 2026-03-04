# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define player = Character("You")
define meb = Character("Mrs. Meb")
define jelle = Character("Jelle")
define poe = Character("Mr. Poe")
define jert = Character("Jert")
define nessie = Character("Nessie")
# The game starts here.
label start:
    "The sky is a deep shade of Rot because of your cheap sunglasses. You quickly take them off for the bright blue light to caress your little eyes"
    "The car draws close to the ranch, a pristine metal nameplate hangs over the main gate"
    "It reads \"The Silverkine Ranch\". You look at the neatly folded envelope inside your fanny pack and confirm that you are in the right place"
    "You pay the cab and walk into the ranch. There's a plethora of animal noises. You go toward the tiny cottage with smoke bellowing out"
    "You knock the door, noticing the nameplate next to the door jamb"
    meb "Oh Hello! You must be the one Mr Poe sent for, please come in"
    "The smell of tomatoes fill your nostrils as you see Mrs. Meb making her patent pending tomato jam"
    meb "Would you like to try some tomato jam?"
    player "Oh actually..."
    menu:
        "What do you say?"
        "Thank you! But I just ate breakfast at the Moorekeeper's Inn on the way here! Maybe some other time!":
            meb "Oh thats alright. There's always another time"
            jump pond
        "Im really sorry, but I'm allergic to tomatoes":
            jump allergy
        "Tomato jam seems really nice, I'd love to try some!":
            jump tomatojam
    return
label pond:
    meb "Why don't you go meet Jelle! She'll help you with your things"
    player "That's awesome, Thanks for having me!"
    meb "Jut be here by 8pm, I'm hosting a small party of sorts for you!"
    jump firstpondencounter
label firstpondencounter:
    "Along the well trodden path you go carrying your fanny pack and a tiny suitcase of clothes. You think about the peculiar student exchange opportunity that bought you here"
    "....."
    "You are distracted by the distant pond which seems to be glowing in the distance"
    menu:
        "What do you do?"
        "Walk up to the pond and investigate":
            $p=2
            jump jert
        "Continue on to meet Jelle":
            jump jelle
label allergy:
    meb "That's unfortunate. Would you like to try my patented olive bark ice-cream!"
    player "That sounds..."
    menu:
        "How does it sound?"
        "Awesome!!!! I LOVE ICECREAM":
            $i=0
            jump icecream
        "I'm awfully sorry, I have the worst cold in like ever. Maybe after I feel better":
            meb "Oh thats alright. There's always another time"
            $p=0
            jump pond
label tomatojam:
    meb "That's nice to hear! Let me find some nice bread for you to eat it with!"
    "You leave your things in the hallway and follow Mrs. Meb into what seems to be the kitchen"
    "There are lots and LOTS of tomatoes in huge rucksacks all ripe the same colour of Rot. You can faintly catch a glimpse of the vast tomato plantantion through the ajar backdoor"
    meb "Here you go! I just baked this almond sap bread! Hope you like it"
    "The tomato jam and almond sap bread go well together!"
    $p=0
    jump pond
label icecream:
    if i<5:
        if i!=0:
            "Mrs. Meb rushes in"
        meb "That's just perfect! Let me fetch you a bowl!"
        if i==0:
            "You leave your things in the hallway and follow Mrs. Meb into what seems to be the kitchen"
            "There are lots and LOTS of tomatoes in huge rucksacks all ripe the same colour of Rot. You can faintly catch a glimpse of the vast tomato plantantion through the ajar backdoor"
        meb "Here you go!"
        "The olive bark icecream is really refreshing"
        if i==0:
            "Mrs. Meb goes out through the back door"
        else:
            "Mrs. Meb goes out the back door again!"
        menu:
            "What do you do?"
            "Follow Mrs. Meb out the back door":
                jump backdoor
            "Request another bowl of icecream":
                $i+=1
                jump icecream
            "Wait for Mrs. Meb to be back":
                "......."
                "You keep waiting"
                "Mrs. Meb comes back in"
                "Oh, are you done already?"
                $p=1
                jump pond
    else:
        meb "I'm sorry, we're out of icecream"
        jump secretencounter
label backdoor:
    "You finish your icecream and walk toward the door, you slowly push the door forward"
    "It is the most glorious sight of your life! You see rows and rows of tomato plants full of Rot coloured tomatoes"
    meb "This is the result of over 10 years of \"tomato-ing\" Mr Meb loved my tomato jam. This is my way of remembering him"
    "Mrs. Meb wipes a tiny droplet of tear that formed with her Rot coloured handkerchief that appropriately had tomatoes embroidered into"
    meb "Come on, let me accompany you to Jelle's little hut! She's the best help anyone can ask for. Bless her heart"
    "You quickly grab your things and follow Mrs Meb out into the field"
    "RIIIINGGG RIIIIINGG"
    meb "Oh, that's the landline. It has to be Mr Poe calling to ask about you. Why don't you continue along this path. You'll know where to stop when you see it!"
    $p=1
    jump firstpondencounter
label jert:
    "A young man blocks your way"
    jert "You must be the new guy. Mr Poe told me all about you"
    "You don't like the look of him very much"
    jert "I'm Jert the ranch's head engineer"
    jert "... the only engineer"
    "The pond stops glowing. You choose to continue on the path"
    jump jelle
label jelle:
    "After a new seconds of walking you feel tired"
    "That's when you notice a tiny hut which looks like a mushroom over by the huge lake"
    "A girl comes out holding a rake"
    jelle "Hi! You must be the new exchange student! I'm Jelle, the caretaker of basically everything here!"
    jelle "Follow me, I'll show you your quarters for the duration of the trip!"
    "You follow Jelle down the road and find a smaller mushroom hut near the larger one"
    jelle "You'll stay here! Make yourself comfortable and meet me out by the lake. I'll tell you what you have to do in the ranch"
    "You walk inside and fine a nice cozy bed with a fireplace next to it"
    player "This is so nice!"
    "You quickly get ready for a long day of work at the ranch!"
    jelle "We're opening the ranch to tourists next week so there's a lot to plan!"
    jelle "So what do you want to do for the day?"
    menu:
        "What job do you want?"
        "Work with Jert and help him add the solar panels and nightlights all over the ranch":
            jump solar
        "Work with Jelle and go fishing in the lake for the rare and elusive silver trout":
            jump lakefishing
        "Work alone and install fences all along the sides of the well trodden path to Jelle's Hut":
            jump fence  
label lakefishing:
    jelle "That's awesome! Let me go bring the bait and the equipment. Set up the kayaks for me please."
    "You finish setting up the kayaks and row toward the middle of the lake."
    jelle "Remember, when you catch the silver trout...."
    nessie "GRBRNRRRRRRRNNNNRNNNNNN"
    "Nessie's scream has hindered your ability to hear"
    menu:
        "What do you do?"
        "Follow the scream":
            jump nessieencounter
        "Ask Jelle about the silver trout":
            jump jellecatch
        "Ignore it and keep fishing":
            jump youcatch
label jellecatch:
    "You see Jelle struggling to reel her line in"
    jelle "Nevermind that, I have one on my line now"
    "After a few seconds of struggling, she successfully has a silvertrout in her hands"
    jelle "That's all we need for dinner tonight! We're having a party afterall!"
    jelle "After we get back to the huts, why don't you go get ready for the party. It's getting dark soon"
    jump secondpondencounter
label youcatch:
    "You continue waiting for your fish"
    jelle "So how's the ranch life treating you?"
    "The string suddenly goes taut. You have your very own silver trout!"
    jelle "Thats it! PULL!"
    "You successfully catch the silver trout!"
    jelle "That's all we need for dinner tonight! We're having a party afterall!"
    jelle "After we get back to the huts, why don't you go get ready for the party. It's getting dark soon"
    jump secondpondencounter
label nessieencounter:
    "You ignore the fishing duties and follow the scream"
    jelle "It's alright! I can fish for the silver trout myself. Maybe tomorro......"
    "Jelle's voice fades as you move farther and farther"
    "The light dims as dusk begins"
    nessie "GNRNSSNSSSSNSNNSNSS"
    "You hear Nessie again"
    player "This is really boring, I should get back to the Party"
    "Something rams past your kayak and you lose balance."
    player "Okay this is really creepy now"
    "You try turning back but something has you anchored in"
    jert "HEY! WHAT ARE YOU DOING HERE?"
    jert "You're not supposed to be here in this part of the lake"
    "Jert is up on top of a night lamp plugging in a comically large light bulb"
    menu:
        "What do you do?"
        "Ignore Jert":
            jump nessiehelp
        "Ask for help":
            jump jerthelp
label jerthelp:
    jert "Alright, this is Nessie's territory. We choose to let her be"
    "Jert comes over to the lake and swims toward the kayak and pulls it on to the shore"
    "You are very surprised by the strength Jert has"
    nessie "MERMRMNSMAN (it sounds sadder)"
    jert "I will be taking this up with Mrs. Meb. This is what happens when we let random kids into the ranch"
    "You quickly run away from Jert"
    jump secondpondencounter
label nessiehelp:
    "You row as fast as you can and go further into the depths of the lake."
    "It gets darker and darker as you go in."
    nessie "HEASDHASJJAHSDIISJK"
    "Suddenly your kayak starts moving very fast. Something is pushing you from the back"
    "You somehow end up at the side of the well trodden path! There is a lot of light here thanks to Jert."
    "You get off and start walking towards your hut to get a new pair of clothes"
    jump secondpondencounter
label secondpondencounter:
    "You see the pond again. It is glowing brighter than ever before"
    menu:
        "What do you do?"
        "Ignore the pond and get ready for the party":
            jump party
        "Ignore the party and start exploring the pond":
            jump finalpondencounter
label party:
    "You have your priorities set!"
    "You reach your hut and realise that Jelle has already left for Mrs. Meb's cottage. You quickly get dressed and leave as fast as you can"
    "You finally reach Mrs. Meb's cottage! You knock on the door"
    jert "Oh its you. You seem late for your own party"
    meb "Its fine Jert! You aren't late at all dear. We're waiting for Mr. Poe to arrive so we can all celebrate!"
    "After a while of waiting and having fun talking to Jelle and Mrs. Meb someone knocks the door"
    poe "Hello! You must be the exchange student! How are you?"
    poe "I'm Mr. Poe! The local bank manager. I take care of most of the things happening around the ranch. I remember my own days of working here."
    meb "Oh yes, you would try stealing all the tomatoes to feed the silverkine. But I always caught you"
    poe "I would always be caught red handed. Literally"
    "Everyone laughs, even Jert."
    jelle "Okay, I think its time we bring out the cake!"
    player "A cake!! For me? You didn't have to"
    meb "Nonsense! Its your first day here!"
    "They bring out the cake and your face lights up with joy!"
    "It reads \"For the best rancher anyone could ask for\""
    "Everyone eats the cake and they all gather round the TV next to the fireplace for a surprise movie night"
    "You look around and then as the movie starts to play, you feel a peculiar sense of calm"
    "You..."
    "Are..."
    "Home!..."
