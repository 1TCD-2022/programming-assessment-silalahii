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
            "ohashi", "yoru", "gatsu", "nichi", "hidari", "migi"]
VALID_MENU_INPUT = ["1", "2", "3"]
start_menu = True
user_score = 0

# print 3 menu choices
menu_choice = ""

while start_menu:
    while menu_choice !="3": 
        print("""\nWelcome to menu!
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
                    


# validate input
# japanese to english
        if menu_choice == "1":
                   
# randomly generate question for user to answer
            for user_questions in range(1,6):
                print("Question {}.".format(user_questions))
                random_question = random.choice(JAPANESE)
                print("Please translate '{}' to English: ".format(random_question))
                english_input = input().strip()
            
# if user input correct enter correct & vice versa
# if user answer incorrect, provide correct answer
                if english_input.lower() == ENGLISH[JAPANESE.index(random_question)]:
                    print("That's correct! Keep it up!\n")
                    user_score += 1
                else:
                    print("Incorrect. The correct translation was '{}'.\n".format(ENGLISH[JAPANESE.index(random_question)]))
# print users current score
            print("Well done, your current score is: {}!".format(user_score))
            
# ask if user wants to return to menu
# exit program if user enters "n"
            return_menu = input("Do you wish to return to menu? (y/n): ").strip()
            while not return_menu.lower() in ["y","n"]:
                return_menu = input("Please enter 'y' or 'n': \n").strip()
            if return_menu.lower() == "y":
                start_menu = True
            else:
                print("Goodbye, さようなら!")
                start_menu = False
                break
                    
        
# menu option 2
# english to japanese romaji
        elif menu_choice == "2":
            for user_questions in range(1,6):
                print("Question {}.".format(user_questions))
                random_question = random.choice(ENGLISH)
                print("Please translate '{}' to Japanese (write in romaji): ".format(random_question))
                japanese_input = input().strip()
            
# if user input correct enter correct & vice versa
# if user answer incorrect, provide correct answer
                if japanese_input.lower() == JAPANESE_ROMAJI[ENGLISH.index(random_question)]:
                    print("That's right!\n")
                    user_score += 1
                else:
                    print("Not quite right, the answer was '{}'.\n".format(JAPANESE_ROMAJI[ENGLISH.index(random_question)]))
# print users current score
            print("Nice, your current score is: {}!".format(user_score))
            
# ask if user wants to return to menu
# exit program if user enters "n"
            return_menu = input("Do you wish to return to menu? (y/n): ").strip()
            while not return_menu.lower() in ["y","n"]:
                return_menu = input("Please enter 'y' or 'n': \n").strip()
            if return_menu.lower() == "y":
                start_menu = True
            else:
                print("Goodbye, さようなら!")
                start_menu = False
                break
            
        else: #menu_choice == "3":
            print("See you next time, じゃあ またね！")
            start_menu = False
