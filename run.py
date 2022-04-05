import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('world_capital_cities')

country_capital = SHEET.worksheet('country_capital')

user_name = input("\nHi there! What's your name? ")
while user_name == '':
    print("\nOops! That's an empty input")
    user_name = input("Try again! Type your name here: ")
print("\nNice meeting you, " + user_name.capitalize() + "\n")

print("Let's play the game that checks how well you know the world's capital cities.")
print("You will have to type in the capital city for the country I randomly choose.")
print("Let's start")

def get_random_pair():
    country_capital= SHEET.worksheet('country_capital').get_all_values()
    random_choice = random.choice(country_capital)
    capital = random_choice[1]
    print(capital[0]+"."*(len(capital)-2)+capital[-1])

get_random_pair()




