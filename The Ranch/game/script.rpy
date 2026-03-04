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
    "Along the well trodden path you go carrying your fanny pack and a tiny suitcase of clothes. You think about the peculiar student exchange opportunity that bought you here"
    "....."
    "You are distracted by the distant pond which seems to be glowing in the distance"
    menu:
        "What do you do?"
        "Walk up to the pond and investigate":
            jump Jert
        "Continue on to meet Jelle":
            jump Jelle
label allergy:
    meb "That's unfortunate. Would you like to try my patented olive bark ice-cream!"
    player "That sounds..."
    menu:
        "How does it sound?"
        "Awesome!!!! I LOVE ICECREAM":
            jump icecream
        "I'm awfully sorry, I have the worst cold in like ever. Maybe after I feel better":
            $c=1
            jump pond
label tomatojam:
    meb "That's nice to hear! Let me find some nice bread for you to eat it with!"
    "You leave your things in the hallway and follow Mrs. Meb into what seems to be the kitchen"
    "There are lots and LOTS of tomatoes in huge rucksacks all ripe the same colour of Rot. You can faintly catch a glimpse of the vast tomato plantantion through the ajar backdoor"
    meb "Here you go! I just baked this almond sap bread! Hope you like it"
    "The tomato jam and almond sap bread go well together!"


