import random

attempts = 3

while attempts > 0:
    print("Title : Eat, Drink, And Be Sick")
    nouns = []
    for _ in range(4):
        n = input("Enter noun: ")
        nouns.append(n)
    
    plural_nouns = []
    for _ in range(6):
        plural_noun = input("Enter plural noun: ")
        plural_nouns.append(plural_noun)
    
    adjectives = []
    for _ in range(2):
        a = input("Enter adjective: ")
        adjectives.append(a)
    
    adverb = input("Enter adverb: ")
    letter = input("Enter any letter: ")
    body_part = input("Enter any body part: ")

    print("An inspector from the Department of Health and", random.choice(nouns), "Services paid a surprise visit to our", random.choice(adjectives), "school cafeteria.")
    print("The lunch special, prepared by our", random.choice(adjectives), "dietician, was spaghetti and", random.choice(nouns), "balls with a choice of either a", random.choice(nouns), "salad or French", random.choice(plural_nouns), ".")
    print("The inspector found the meat-", random.choice(plural_nouns), "to be overcooked and discovered a live", random.choice(nouns), "in the fries, causing him to have a " + body_part + "ache.")
    print("In response, he threw up all over his", random.choice(plural_nouns), ".")
    print("In his report, the inspector", adverb, "recommended that the school cafeteria serve only nutritious", random.choice(plural_nouns), "as well as low-calorie", random.choice(plural_nouns), "and that all of the saturated", random.choice(plural_nouns), "be eliminated.")
    print("He rated the cafeteria a " + letter + "-minus.")
    
    attempts -= 1
