# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Character Definitions
define k = Character("King Theron", color="#c9b037")
define q = Character("Queen Elara", color="#e3a857")
define p = Character("Prince Arion", color="#7fa2c9")
define v = Character("Priest Valerius", color="#b5b5b5")
define n = Character(None) # Narrator

# Image Transforms
transform bg_fullscreen:
    xpos 0
    ypos 0
    xanchor 0
    yanchor 0
    xsize 1920
    ysize 1080

transform portrait_default:
    xpos 0.5
    xanchor 0.5
    ypos 0.75
    yanchor 1.0
    zoom 0.7

# Image Definitions
image king neutral = "game/images/characters/king_neutral.png" at portrait_default
image king angry = "game/images/characters/king_angry.png" at portrait_default
image king sad = "game/images/characters/king_sad.png" at portrait_default
image king ill = "game/images/characters/king_ill.png" at portrait_default
image king content = "game/images/characters/king_content.png" at portrait_default
image king wounded = "game/images/characters/king_wounded.png" at portrait_default

image queen neutral = "game/images/characters/queen_neutral.png" at portrait_default
image queen worried = "game/images/characters/queen_worried.png" at portrait_default
image queen hopeful = "game/images/characters/queen_hopeful.png" at portrait_default
image queen sad = "game/images/characters/queen_sad.png" at portrait_default
image queen happy = "game/images/characters/queen_happy.png" at portrait_default
image queen devastated = "game/images/characters/queen_devastated.png" at portrait_default

image prince determined = "game/images/characters/prince_determined.png" at portrait_default
image prince worried = "game/images/characters/prince_worried.png" at portrait_default
image prince happy = "game/images/characters/prince_happy.png" at portrait_default
image prince sad = "game/images/characters/prince_sad.png" at portrait_default
image prince thoughtful = "game/images/characters/prince_thoughtful.png" at portrait_default
image prince upset = "game/images/characters/prince_upset.png" at portrait_default

image priest neutral = "game/images/characters/priest_neutral.png" at portrait_default
image priest concerned = "game/images/characters/priest_concerned.png" at portrait_default
image priest stern = "game/images/characters/priest_stern.png" at portrait_default
image priest contemplative = "game/images/characters/priest_contemplative.png" at portrait_default
image priest disapproving = "game/images/characters/priest_disapproving.png" at portrait_default
image priest satisfied = "game/images/characters/priest_satisfied.png" at portrait_default

# Background Images
image bg royal_chambers = "game/images/backgrounds/royal_chambers.jpg" at bg_fullscreen
image bg sanctuary = "game/images/backgrounds/sanctuary.jpg" at bg_fullscreen
image bg throne_room = "game/images/backgrounds/throne_room.jpg" at bg_fullscreen
image bg dining_hall = "game/images/backgrounds/dining_hall.jpg" at bg_fullscreen
image bg gatehouse = "game/images/backgrounds/gatehouse.jpg" at bg_fullscreen
image bg gallows = "game/images/backgrounds/gallows.jpg" at bg_fullscreen

# Variables for tracking reputation and health
default rep_queen = 0
default rep_prince = 0
default rep_priest = 0
default king_health = "healthy" # healthy, ill, wounded, dying

label start:
    jump chapter1

# --- Chapter 1: Whispers in the Hall / Child of the Court / The Confession ---
label chapter1:
    scene bg royal_chambers
    show king neutral
    show queen neutral
    n "The sun rises over Folksreach. Within the royal chambers, King Theron sits in contemplation, Queen Elara by his side."
    k "Another restless night, Elara. The air feels heavy with whispers."
    q "You worry too much, my king. But I sense it too. The servants speak of unrest beyond the walls."
    show prince thoughtful
    n "Prince Arion lingers at the doorway, clutching a book, eyes darting between his parents."
    p "Father, may I join you at council today?"
    k "You are young, Arion. The matters discussed are weighty."
    show priest neutral
    n "Priest Valerius enters, bowing respectfully."
    v "Your Majesty, the people seek reassurance. The church stands ready to guide you through these troubled times."
    n "You, the royal advisor, must decide how to address the tension."
    menu:
        "Inform the Queen of rising tension":
            $ rep_queen += 2
            show queen hopeful
            q "Thank you for trusting me. I will speak with the guards and ensure our safety."
            n "Queen Elara's confidence in you grows."
        "Warn the guards directly":
            n "The guards are alerted, but the Queen seems troubled by your secrecy."
            $ rep_queen -= 1
        "Encourage King to spend time with Prince":
            $ rep_prince += 2
            show prince happy
            k "Very well, Arion. Join me. You must learn the burdens of rule."
            n "Prince Arion beams with pride."
        "Encourage King to reflect with Priest Valerius":
            $ rep_priest += 2
            show priest contemplative
            v "Reflection is the path to wisdom, Your Majesty."
            n "Priest Valerius nods approvingly."
    n "The day passes, and the choices you make ripple through the royal household."
    jump chapter2

# --- Chapter 2: The Sanctuary’s Offer / Throne Room Lessons / The Queen’s Plan Unveiled ---
label chapter2:
    scene bg sanctuary
    show king neutral
    show priest neutral
    n "Within the sanctuary, the King kneels in silent prayer. Priest Valerius approaches."
    v "Your Majesty, the burdens you bear are not yours alone. Let faith guide you."
    menu:
        "Encourage King to speak to the Priest":
            $ rep_priest += 2
            show priest satisfied
            k "Your counsel brings me peace, Valerius."
            v "Then let us pray for wisdom."
        "Ignore the Priest":
            $ rep_priest -= 1
            show priest disapproving
            v "Even kings must not turn from the light."
    n "Elsewhere, Queen Elara gathers her advisors."
    scene bg royal_chambers
    show queen hopeful
    q "I have devised a plan—a charity mission to aid the poor. But it will also serve as our escape, should war come."
    menu:
        "Support the Queen’s plan":
            $ rep_queen += 2
            show queen happy
            q "Thank you. With your support, we may yet survive."
        "Challenge the Queen’s plan":
            $ rep_queen -= 1
            show queen worried
            q "You doubt me? I only wish to protect our family."
    n "Meanwhile, Prince Arion attends his first council meeting."
    scene bg throne_room
    show prince determined
    p "I will listen and learn, as you advised."
    n "The seeds of succession are sown."
    jump chapter3

# --- Chapter 3: The Charity Plan / The King’s Trial / The River Rhemes Vision ---
label chapter3:
    scene bg throne_room
    show king neutral
    show queen neutral
    show prince thoughtful
    n "The royal family convenes in the throne room. Tension lingers in the air."
    k "Elara, your charity plan is bold. But will it save us?"
    q "It is our best hope. The people trust me."
    show priest stern
    v "Charity is noble, but deception is a sin."
    menu:
        "Support the Queen’s plan":
            $ rep_queen += 2
            show queen happy
            q "With you beside me, we cannot fail."
        "Doubt the Queen’s plan":
            $ rep_queen -= 1
            show queen sad
            q "I see. I will proceed alone, if I must."
        "Suggest Prince assume partial duties":
            $ rep_prince += 2
            $ king_health = "ill"
            show king ill
            k "Arion, you must shoulder some burdens. My strength wanes."
            show prince determined
            p "I will not fail you, father."
        "Encourage King to reflect on his sins":
            $ rep_priest += 2
            show priest contemplative
            v "Repentance is the first step to redemption."
    n "That night, the King dreams of the River Rhemes."
    scene bg sanctuary
    show king sad
    n "He sees visions—his mother, the city in flames, the priest's stern gaze."
    menu:
        "Interpret as a call to repentance":
            $ rep_priest += 2
            show priest satisfied
            v "God calls you, Your Majesty."
        "Dismiss as madness":
            $ rep_priest -= 1
            show priest disapproving
            v "You turn from the truth at your peril."
    jump chapter4

# --- Chapter 4: The Royal Dinner Debate / The Gallows Verdict / The Sanctuary’s Oath ---
label chapter4:
    scene bg dining_hall
    # Fix conditional king image display
    if king_health == "ill":
        show king ill
    else:
        show king neutral
    show queen neutral
    show prince thoughtful
    show priest neutral
    n "A tense dinner gathers the royal family and their closest advisors."
    q "We must act soon. Goering's armies draw near."
    v "The soul of the kingdom is at stake."
    p "What will become of us?"
    menu:
        "Mediate between Queen, Priest, and Prince":
            $ rep_queen += 1
            $ rep_prince += 1
            $ rep_priest += 1
            show queen hopeful
            show prince happy
            show priest satisfied
            n "Your wisdom brings a fragile peace to the table."
        "Side with the Queen":
            $ rep_queen += 2
            $ rep_priest -= 1
            show queen happy
            show priest disapproving
            n "Elara smiles, but Valerius frowns."
        "Side with the Priest":
            $ rep_priest += 2
            $ rep_queen -= 1
            show priest satisfied
            show queen sad
            n "Valerius nods, but Elara looks away."
        "Side with the Prince":
            $ rep_prince += 2
            show prince happy
            n "Arion beams with pride."
        "Pardon traitors at the gallows":
            $ rep_prince += 2
            show prince happy
            n "The people cheer the Prince's mercy."
        "Execute traitors at the gallows":
            $ rep_prince -= 1
            show prince upset
            n "The Prince looks away, troubled by the bloodshed."
        "Dissolve the royal marriage":
            $ rep_queen -= 2
            $ rep_priest += 2
            show queen devastated
            show priest satisfied
            n "The Queen weeps. The Priest blesses your sacrifice."
    jump chapter5

# --- Chapter 5: Endings ---
label chapter5:
    # Calculate total reputation
    $ total_rep = rep_queen + rep_prince + rep_priest

    # Queen's Escape Plan Ending
    if rep_queen > 0 and rep_prince > 0 and rep_priest > 0 and (king_health == "healthy" or king_health == "ill"):
        jump ending_queen

    # Prince's Ascension Ending
    elif total_rep > 10 and king_health == "healthy":
        jump ending_prince

    # Priest's Devotion Ending
    elif rep_priest > 0 and rep_queen < 0 and (king_health == "wounded" or king_health == "dying"):
        jump ending_priest

    # Fallback: No clear ending
    else:
        jump ending_failure

label ending_queen:
    scene bg gatehouse
    # Conditional king image based on health
    if king_health == "ill":
        show king ill
    else:
        show king neutral
    show queen hopeful
    show prince thoughtful
    n "Under the cover of night, the royal family slips away, the city of Folksreach burning behind them."
    q "We survived, but at what cost?"
    show king sad
    k "Our home is lost, but our bloodline endures."
    show prince sad
    p "Will we ever return?"
    n "The family watches the flames from afar. The world they knew is gone, but hope flickers in the darkness."
    n "{i}Charity Exodus Ending: The Queen's plan succeeds. Folksreach falls, but the royal family survives in exile.{/i}"
    jump credits

label ending_prince:
    scene bg throne_room
    show king content
    show prince happy
    show queen happy
    n "King Theron, restored to health, abdicates the throne. Prince Arion is crowned before a jubilant court."
    k "Rule wisely, my son. The future is yours."
    show prince determined
    p "I will honor our name, and bring peace to Folksreach."
    show queen happy
    q "Our legacy endures."
    n "{i}Golden Age Ending: The Prince ushers in a new era of peace and prosperity.{/i}"
    jump credits

label ending_priest:
    scene bg sanctuary
    # Conditional king image based on health
    if king_health == "wounded":
        show king wounded
    else:
        show king sad
    show priest satisfied
    n "Broken in body and spirit, King Theron renounces his crown and retreats to a monastery."
    show queen devastated
    q "You would leave us? After all we have endured?"
    show priest contemplative
    v "He seeks redemption, Elara. Let him go."
    n "The kingdom fractures. The king vanishes into legend, praying for his people in obscurity."
    n "{i}Holy Redemption Ending: The king surrenders power for spiritual penance. His story becomes a myth.{/i}"
    jump credits

label ending_failure:
    scene bg gallows
    show king sad
    show queen sad
    show prince upset
    show priest disapproving
    n "The kingdom falls into chaos. The royal family is scattered, their fate uncertain."
    n "{i}Failure: No path to salvation was found. Folksreach is lost to history.{/i}"
    jump credits

label credits:
    n "Thank you for playing."
    return
