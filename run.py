import gspread
from google.oauth2.service_account import Credentials
import random
import sys
import emoji
from time import sleep
import time
from pyfiglet import Figlet
from termcolor import colored

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
    f = Figlet(font = "digital")
    print(colored(f.renderText("\nWELCOME \nTO THE WORLD CAPITALS QUIZ"), "green"))
    user_name = input("\nHI THERE! \n\nWhat's your name? \n")
    while user_name == '':
        print("\nOops! That's an empty input \n")
        user_name = input("Try again! Type your name here: \n")
    print("\nNice meeting you," + " " + user_name.upper() + " " + emoji.emojize(":grinning_face:") + "\n")
    print("Let's check how well you know the world capital cities.\n")

    instructions = [
        colored(("****************************************************************"), "green"),
        "INSTRUCTIONS\n",
        colored(("****************************************************************"), "green"),
        "You have to guess the world capital I randomly choose.\n",
        "You'll get a hint with the first and last letters of the city.\n",
        "You have 3 guesses to get it right.\n\n",
        emoji.emojize(":index_pointing_up:") + "  REMEMBER " + emoji.emojize(":index_pointing_up:") + "\n",
        colored(("****************************************************************"), "green"),
        "If capital consists of two or more words, type it as one word.\n",
        colored(("****************************************************************"), "green")
    ]

    for i in instructions:
        print(i)
        sleep(1)


def ask_user():
    try:
        ready = input("\nDO YOU WANT TO CONTINUE?" + " " + colored(("(yes/no)"), "green") + "\n")
        if ready == 'yes':
            return True
        elif ready == 'no':
            print("That's a shame! Come back next time",
                  emoji.emojize(":grinning_face_with_big_eyes:"), "\n")
            sys.exit()
        elif ready != 'yes' & ready != 'no':
            raise Exception
    except Exception as error:
        print(colored(("Invalid input! Check if you typed 'yes' or 'no'. Please try again.\n"), "red"))
        return ask_user()


def continent_choice():
    global google_list
    continents = {
        '1': 'ASIA',
        '2': 'AFRICA',
        '3': 'EUROPE',
        '4': 'NORTH/SOUTH AMERICAS',
        '5': 'AUSTRALIA/OCEANIA'
    }
    
    print(colored(("\nGO AHEAD!"), "green"))
    print(colored(("Pick the number corresponding to the continent of your choice: \n\n"), "green"))
    print(*[f'Enter {k} for {v}' for k, v in continents.items()], sep='\n')
    chosen_continent = input('\n'"")
    try:

        if chosen_continent == list(continents.keys())[0]:
            google_sheet_data = SHEET.worksheet(
                'asian_countries').get_all_values()
            google_list = google_sheet_data
            print("\n\n"f"{list(continents.values())[0]} is a great choice!\n")
        elif chosen_continent == list(continents.keys())[1]:
            google_sheet_data = SHEET.worksheet(
                'african_countries').get_all_values()
            google_list = google_sheet_data
            print("\n\n"f"{list(continents.values())[1]} is a great choice!\n")
        elif chosen_continent == list(continents.keys())[2]:
            google_sheet_data = SHEET.worksheet(
                'european_countries').get_all_values()
            google_list = google_sheet_data
            print("\n\n"f"{list(continents.values())[2]} is a great choice!\n")
        elif chosen_continent == list(continents.keys())[3]:
            google_sheet_data = SHEET.worksheet(
                'north_south_america_countries').get_all_values()
            google_list = google_sheet_data
            print("\n\n"f"{list(continents.values())[3]} is a great choice!\n")
        elif chosen_continent == list(continents.keys())[4]:
            google_sheet_data = SHEET.worksheet(
                'australia_oceania_countries').get_all_values()
            google_list = google_sheet_data
            print("\n\n"f"{list(continents.values())[4]} is a great choice!\n")
        else:
            raise Exception(
                "only the numbers from the list provided are considered")
    except Exception as e:
        print(colored((f"\nThis is invalid input as {e} Please try again.\n"), "red"))
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
    sys.stdout.write(colored(("\rEUREKA! I am all ears and ready for your answer."), "green") + "\n\n")

correct = 0
incorrect = 0

def play():
    global google_list, user_name, correct, incorrect
    max_guess = 3
    guess_num = 1
    user_attempt = ''
    random_choice = random.choice(google_list)
    country = random_choice[0]
    capital = random_choice[1]
    capital_hint = capital[0]+"."*(len(capital)-2)+capital[-1]

    print(colored(("****************************************************************"), "green"))
    print(colored(("\nWhat is the capital of " + country.upper() + "?\n" + "\nYour hint is " + capital_hint.upper() + "\n"), "yellow"))
    print(colored(("****************************************************************"), "green"))
    while guess_num <= max_guess:
        user_attempt = input("Type in your guess #%s below: " % (guess_num) + "\n")
        guess_num += 1
        if user_attempt.lower() == capital.lower():
            print(colored(("\nC'EST MAGNEFIQUE!"), "green") + " " + "You are a force to be reckoned with in geography.")
            correct += 1
            total = correct + incorrect
            print(f"\nYour correct answers score: ", colored((correct), "green"))
            print(f"\nTotal questions: ", total)
            break
        if guess_num > max_guess:
            print(colored(("\nOH, NO!"), "red") + " " + "That was your last chance to get it right. The answer was %s." %(capital))
            incorrect += 1
            total = correct + incorrect
            print(f"\nYour incorrect answers score: ", colored((incorrect), "red"))
            print(f"\nTotal questions: ", total)
            break
    
    while True:
        another_continent = input("\nDO YOU WANT TO TRY ANOTHER CONTINENT?" + " " + colored(("(yes/no)"), "green") + "\n")
        if another_continent == "yes":
            continent_choice()
            loading_animation()
            play()
        elif another_continent == "no":
            print(f"\nOkay {user_name.upper()}, thanks for playing, have a lovely day.\n")
            print(colored(("****************************************************************"), "green"))
            print(f"Your correct answers score: ", colored((correct), "green"))
            print(f"\nYour incorrect answers score: ", colored((incorrect), "red"))
            print(f"\nTotal questions: ", total)
            print(colored(("****************************************************************"), "green"))
            sys.exit()
        else:
            print(colored(("\nHmm.. That was an invalid input. You have to select either 'yes' or 'no' \n"), "red"))
            print(colored(('Please try again.') , "red"))

def main():
    game_intro()
    ask_user()
    continent_choice()
    loading_animation()
    play()


main()
