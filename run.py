import gspread
from google.oauth2.service_account import Credentials
import random
import sys
import emoji
from time import sleep
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('world_capital_cities')

def game_intro():
    user_name = input("\nHi there! What's your name? \n")
    while user_name == '':
        print("\nOops! That's an empty input \n")
        user_name = input("Try again! Type your name here: \n")
    print("\nNice meeting you, " + user_name.capitalize() + emoji.emojize(":grinning_face_with_smiling_eyes:"), "\n")
    print("My name is Anna, but you can call me Ann" + emoji.emojize(":handshake:") + "\n")

    instructions = ["Let's play the game that checks how well you know the world's capital cities" + emoji.emojize(":nerd_face:") + '\n', 
            "You will have to type in the capital city for the country I randomly choose.\n", 
            "To make it easier there will be a hint with the first and last letter of the capital.\n",
            emoji.emojize(":index_pointing_up: ") + "If capital name consists of two or more words, you have to type it as one word.\n"
            ]

    for i in instructions:
        print(i) ; sleep(1)

def ask_user():
    try:
        ready = input("Are you ready to play? (yes/no)  \n")
        if ready == 'yes':
            return True
        elif ready == 'no':
            print("That's a shame! Come back next time", emoji.emojize(":grinning_face_with_big_eyes:"), "\n")
            sys.exit()
        elif ready != 'yes' & ready != 'no':
            raise Exception
        
    except Exception as error:
        print("Hmmm... Check if you typed 'yes' to play or 'no' to exit the game. Please try again.\n")
        return ask_user()


def continent_choice():
    global google_list
    positive = 'yes'
    negative = 'no'
    continents = ['asia','africa','europe','north south americas','australia oceania']
    play = True
    print("\nGo ahead and pick a continent:\n\n")
    print("\n".join(str(x) for x in continents))
    chosen_continent = input('\n'"").lower()
    
    try:

        if chosen_continent == continents[0]:
            google_sheet_data = SHEET.worksheet('asian_countries').get_all_values()
            google_list = google_sheet_data
            print("\n\n"f"{chosen_continent} is a great choice!\n")
        
        
        elif chosen_continent == continents[1]:
            google_sheet_data = SHEET.worksheet('african_countries').get_all_values()
            google_list = google_sheet_data
            print("\n\n"f"{chosen_continent} is a great choice!\n")
            
        elif chosen_continent == continents[2]:
            google_sheet_data = SHEET.worksheet('european_countries').get_all_values()
            google_list = google_sheet_data
            print("\n\n"f"{chosen_continent} is a great choice!\n")

        elif chosen_continent == continents[3]:
            google_sheet_data = SHEET.worksheet('north_south_america_countries').get_all_values()
            google_list = google_sheet_data
            print("\n\n"f"{chosen_continent} is a great choice!\n")

        elif chosen_continent == continents[4]:
            google_sheet_data = SHEET.worksheet('australia_oceania_countries').get_all_values()
            google_list = google_sheet_data
            print("\n\n"f"{chosen_continent} is a great choice!\n")
        
        else:
            raise Exception (f"only the continents from the list provided are considered")
    
    except Exception as error:
        print(f"\nThis is invalid input as {error}, please try again.\n")
        return continent_choice()


def get_random_pair():
    global country, capital_hint
    random_choice = random.choice(google_list)
    country = random_choice[0]
    capital = random_choice[1]
    capital_hint = capital[0]+"."*(len(capital)-2)+capital[-1]

def loading_animation(count=15):
    max_guesses = 3
    for i in range(count + 1):
        sys.stdout.write('\rI am thinkig up a country | ')
        time.sleep(0.1)
        sys.stdout.write('\rI am thinkig up a country /')
        time.sleep(0.1)
        sys.stdout.write('\rI am thinkig up a country -')
        time.sleep(0.1)
        sys.stdout.write('\rI am thinkig up a country \\')
        time.sleep(0.1)
    sys.stdout.write("\rEUREKA! You have %s guesses to get it.\n" %(max_guesses))
    

def main():
    game_intro()
    ask_user()
    continent_choice()
    get_random_pair()
    loading_animation() 


main()
