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
    global user_name
    print("\nWELCOME TO CAPITALS OF THE WORLD QUIZZ")
    user_name = input("\nHi there! What's your name? \n")
    while user_name == '':
        print("\nOops! That's an empty input \n")
        user_name = input("Try again! Type your name here: \n")
    print("\nNice meeting you, " + user_name.capitalize() + emoji.emojize(":grinning_face_with_smiling_eyes:"), "\n")

    instructions = ["Let's play the game that checks how well you know the world's capital cities" + emoji.emojize(":nerd_face:") + '\n', 
            "You will have to type in the capital city for the country I randomly choose.\n", 
            "To make it easier there will be a hint with the first and last letter of the capital.\n"
            ]

    for i in instructions:
        print(i) ; sleep(1)

again = ''
def ask_user(again):
    try:
        ready = input(f"Do you want to continue {again}? (yes/no)  \n")
        if ready == 'yes':
            return True
        elif ready == 'no':
            print("That's a shame! Come back next time", emoji.emojize(":grinning_face_with_big_eyes:"), "\n")
            sys.exit()
        elif ready != 'yes' & ready != 'no':
            raise Exception
        
    except Exception as error:
        print("Hmmm... Check if you typed 'yes' to play or 'no' to exit the game. Please try again.\n")
        return ask_user(again)


def continent_choice():
    global google_list
    continents = {'1':'ASIA','2': 'AFRICA', '3': 'EUROPE', '4': 'NORTH/SOUTH AMERICAS', '5': 'AUSTRALIA/OCEANIA'}
    print("\nGo ahead and pick a number corresponding to the continent of your choice:\n\n")
    print(*[f'Enter {k} for {v}' for k,v in continents.items()], sep='\n')
    chosen_continent = input('\n'"")
    
    try:

        if chosen_continent == list(continents.keys())[0]:
            google_sheet_data = SHEET.worksheet('asian_countries').get_all_values()
            google_list = google_sheet_data
            print("\n\n"f"{list(continents.values())[0]} is a great choice!\n")
        
        
        elif chosen_continent == list(continents.keys())[1]:
            google_sheet_data = SHEET.worksheet('african_countries').get_all_values()
            google_list = google_sheet_data
            print("\n\n"f"{list(continents.values())[1]} is a great choice!\n")
            
        elif chosen_continent == list(continents.keys())[2]:
            google_sheet_data = SHEET.worksheet('european_countries').get_all_values()
            google_list = google_sheet_data
            print("\n\n"f"{list(continents.values())[2]} is a great choice!\n")

        elif chosen_continent == list(continents.keys())[3]:
            google_sheet_data = SHEET.worksheet('north_south_america_countries').get_all_values()
            google_list = google_sheet_data
            print("\n\n"f"{list(continents.values())[3]} is a great choice!\n")

        elif chosen_continent == list(continents.keys())[4]:
            google_sheet_data = SHEET.worksheet('australia_oceania_countries').get_all_values()
            google_list = google_sheet_data
            print("\n\n"f"{list(continents.values())[4]} is a great choice!\n")
        
        else:
            raise Exception (f"only the numbers from the list provided are considered")
    
    except Exception as error:
        print(f"\nThis is invalid input as {error}, please try again.\n")
        return continent_choice()
    
def loading_animation(count=15):
    for i in range(count):
        sys.stdout.write('\rI am thinking up a country | ')
        time.sleep(0.1)
        sys.stdout.write('\rI am thinking up a country /')
        time.sleep(0.1)
        sys.stdout.write('\rI am thinking up a country -')
        time.sleep(0.1)
        sys.stdout.write('\rI am thinking up a country \\')
        time.sleep(0.1)
    sys.stdout.write("\rEUREKA! I am ready for you right answer..." + "\n\n")

def play():
    global google_list, user_name
    max_guess = 3
    guess_num = 1
    user_attempt = ''
    random_choice = random.choice(google_list)
    country = random_choice[0]
    capital = random_choice[1]
    capital_hint = capital[0]+"."*(len(capital)-2)+capital[-1]

    print("You have %s guesses to get it.\n\n" %(max_guess))
    print("What is the capital of " + country.upper() + "?\n" + "Your hint is " + capital_hint.upper() + "\n")
    print(emoji.emojize(":index_pointing_up: ") + "REMEMBER" + emoji.emojize(":index_pointing_up: ") + " If capital name consists of two or more words, you have to type it as one word.\n")

    while guess_num <= max_guess or user_attempt.lower() != capital.lower():
        user_attempt = input("Type in your guess #%s below: " % (guess_num) + "\n")
        guess_num += 1
        if user_attempt.lower() == capital.lower():
            print("C'EST MAGNEFIQUE! You are a force to be reckoned with in geography")
            break
        if guess_num > max_guess:
            print("\nOH, NO! That was your last chance to get it right. The answer was %s." %(capital))
            break
        
    while True:
        another_continent = input("\nDo you want to try out another continent? (yes/no) \n")
        if another_continent == "yes":
            continent_choice()
            loading_animation()
            play()
        elif another_continent == "no":
            print(f"Okay {user_name.capitalize()}, thanks for playing, have a lovely day.")
            sys.exit()
        else:
            print("\nHmm.. That wan an invalid input. You have to select either 'yes' or 'no' \n")
            print('Please try again')    

def main():
    game_intro()
    ask_user(again)
    continent_choice()
    loading_animation()
    play()

main()