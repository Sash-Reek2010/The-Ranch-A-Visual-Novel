# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define player = Character("You")
define meb = Character("Mrs. Meb")
define jelle = Character("Jelle")
define poe = Character("Poe")
define jert = Character("Jert")
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
            $c=1
            jump pond
        "Im really sorry, but I'm allergic to tomatoes":
            jump allergy
        "Tomato jam seems really nice, I'd love to try some!":
            jump tomatojam
    return
label pond:
    if c==1:
        meb "Oh thats alright. There's always another time"
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
            $c=1
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
    "You see a tiny hut which looks like a mushroom over by the huge lake"
    "A girl comes out holding a rake"
    
