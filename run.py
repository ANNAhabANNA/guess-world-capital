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

print("Let's play the game that checks how well you know the world's capital cities.\n")
print("You will have to type in the capital city for the country I randomly choose.\n")
ready = input("Are you ready to play?  ")

def continent_choice():

    global google_list
    positive = 'yes'
    negative = 'no'
    continents = ['asia','africa','europe','north/south america','australia/oceania']
    play = True

    print("\nFantastic! Go ahead and pick a continent:\n\n")
    print("\n".join(str(x) for x in continents))
    chosen_continent = input('\n'"")
    print("\n\nGreat choice!\n\n")
    while play:

        if ready == positive:
           
            if chosen_continent == continents[0]:
                print("ASIA\n")
                google_sheet_data = SHEET.worksheet('asian_countries').get_all_values()
                google_list = google_sheet_data
               
            
            elif chosen_continent == continents[1]:
                print("AFRICA\n")
                google_sheet_data = SHEET.worksheet('african_countries').get_all_values()
                google_list = google_sheet_data
                
            elif chosen_continent == continents[2]:
                print("EUROPE\n")
                google_sheet_data = SHEET.worksheet('european_countries').get_all_values()
                google_list = google_sheet_data

            elif chosen_continent == continents[3]:
                print("NORTH/SOUTH AMERICA\n")
                google_sheet_data = SHEET.worksheet('north_south_america_countries').get_all_values()
                google_list = google_sheet_data

            elif chosen_continent == continents[4]:
                print("AUSTRALIA/OCEANIA\n")
                google_sheet_data = SHEET.worksheet('australia_oceania_countries').get_all_values()
                google_list = google_sheet_data
            break


def get_random_pair():
   
    random_choice = random.choice(google_list)
    print(random_choice)
    capital = random_choice[1]
    print(capital[0]+"."*(len(capital)-2)+capital[-1])


continent_choice()
get_random_pair()
