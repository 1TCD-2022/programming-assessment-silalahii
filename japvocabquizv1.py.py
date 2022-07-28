"""
Filename: japvocabquiz.py
Author: Isabelle Silalahi
Date: 28.06.2022
Description: This is a program that quizzes the user on their knowledge of
Level 1 Japanese vocabulary.
"""

import random

# generate 2 lists of languages
# 1 list for user to be able to type in Japanese
JAPANESE = ["さんぽ", "しけん", "ぎんこう", "じょうず", "ミルク",
            "いなか", "じんじゃ", "しゃしん", "おみやげ", "うんてん",
            "おはし", "よる", "月", "日", "左", "右"]
ENGLISH = ["stroll", "examination", "bank", "good at", "milk",
           "countryside", "shrine", "photo", "souvenir", "drive",
           "chopsticks", "evening", "month", "day", "left", "right"]
JAPANESE_ROMAJI = ["sanpo", "shiken", "ginkou", "jouzu", "miruku",
            "inaka", "jinjya", "shashin", "omiyage", "unten",
            "ohashi", "yoru", "gatsu", "nichi", "left", "right"]
VALID_MENU_INPUT = ["1", "2", "3"]

# print 3 menu choices
menu_choice = ""
while menu_choice !="3": 
    print("""Welcome to menu!
    This is a program that quizzes you on your
    knowledge of Level 1 Japanese vocabulary.\n
    Please choose from 1, 2, or 3,
    1. I'll give you a word in Japanese, you translate it to English
    2. I'll give you a word in English, you translate it to Japanese (romaji)
    3. Exit quiz\n""")
# validate user input
# strip user input so it is valid
    menu_choice = input("Choose 1, 2, or 3: ").strip()
    while not (menu_choice in (VALID_MENU_INPUT)):
            menu_choice = input("Make sure to enter 1, 2, or 3 (as an integer): ").strip()
                

# randomly generate question for user to answer
# validate input
# japanese to english
    if menu_choice == "1":
        selection = random.choice(JAPANESE)
        print("Please translate '{}' to English: ".format(selection))
        english_input = input().strip()
        
# if user input correct enter correct & vice versa
        if english_input.lower() == ENGLISH[JAPANESE.index(selection)]:
            print("That's correct! Keep it up!\n")
        else:
            print("A little more practice, incorrect.\n")


# menu option 2
# english to japanese romaji
    elif menu_choice == "2":
        selection = random.choice(ENGLISH)
        print("Please translate '{}' to Japanese (write in romaji): ".format(selection))
        japanese_input = input().strip()
        
# if user input correct enter correct & vice versa
        if japanese_input.lower() == JAPANESE_ROMAJI[ENGLISH.index(selection)]:
            print("That's right!\n")
        else:
            print("So close... Not quite right.\n")
        
    else: #menu_choice == "3":
        print("See you next time, keep practicing!!!")

