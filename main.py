import requests
import os
import time


API_KEY = "TU API KEY"


def clear_console():

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main_menu():
    clear_console()
    
    print("Welcome to the Hypixel api by Al3xx_ux!")
    print("1. Win Leaderboard all time")
    print("2. Search user stats")
    print("3. Current number of users")
    print("4. Staff bans")
    print("0. Exit")

    option = input("Chose an option >>> ")
    if option.isdigit():
        option = int(option)

    match option:
        case 0:
            print("Exiting the program. minecraftiano!")
            exit()
        case 1:
            leaderboard()
        case 2:
            search_user_stats()
        case 3:
            number_of_users()
        case 4:
            staff_list()
        
        case _:
            print("Invalid option. Please try again.")
            main_menu()


def return_to_menu():
    print ("\nDo you want to return to the main menu?")
    print ("1. Yes")
    print ("2. No")
    option_return = input("Chose an option >>> ")
    if option_return.isdigit():
        option_return = int(option_return)

    match option_return:
        case 1:
            main_menu()
        case 2:
            print("Exiting the program .... bye minecraftiano!")
            exit()
        case _:
            print("Invalid option. Please try again.")
            return_to_menu()
            

def UID_to_NAME(uiid):
    url_uid_to_name = "https://api.hypixel.net/v2/player?key=" + API_KEY + "&uuid=" + uiid

    response = requests.get(url_uid_to_name)
    if response.status_code == 200:
        data = response.json()
        return data['player']['displayname']


def name_to_UID(username):
    url_name_to_UID = "https://api.mojang.com/users/profiles/minecraft/" + username
    response = requests.get(url_name_to_UID)
    if response.status_code == 200:
        data = response.json()
        return data['id']
    else:
        print("Error: Unable to retrieve UUID for the given username.")
        return None
        

def leaderboard():
    clear_console()
    print("Searching leaderboard data...")

    url_leaderboard = "https://api.hypixel.net/v2/leaderboards?key=" + API_KEY

    response = requests.get(url_leaderboard)
    
    position = 1
    
    if response.status_code == 200:
        data = response.json()
        print ("Leaderboard data retrieved successfully!")

        leaderboard_data = data['leaderboards']
        
        for mode, leaderboard_list in leaderboard_data.items():
            for leaderboard_info in leaderboard_list:
                leaders = leaderboard_info['leaders'][:10]
                
                if position >= 11:
                    return_to_menu()


                print ("TOP 10 players with most wins all time\n")
                for uiid in leaders:
                   
                    player_name = UID_to_NAME(uiid)
                    print (str(position) + ". " + player_name,)
                    position += 1
              
    else:
        print("Error al obtener leaderboard")


def search_user_stats(): 
    clear_console()
    print("Search user stats\n")

    name = input("Enter the username >>>")

    uuid_name = name_to_UID(name)

    if uuid_name == None:
        print("Invalid username. Please try again.")
        search_user_stats()
    
    url_search_user = "https://api.hypixel.net/v2/player?key=" + API_KEY + "&uuid=" + uuid_name

    response = requests.get(url_search_user, )

    if response.status_code == 200:
        data = response.json()
        if data['player'] is not None:
            player = data['player']
            stats = player.get('stats')
            bedwars = stats.get('Bedwars')

            last_logout_ms = player.get('lastLogout')
            first_login_ms = player.get('firstLogin')

            if last_logout_ms:
                last_logout_s = last_logout_ms / 1000
                diference_seconds_last_login = time.time() - last_logout_s
                days_last_logout = (diference_seconds_last_login // 86400)

            if first_login_ms:
                first_login_s = first_login_ms / 1000
                diference_seconds_first_login = time.time() - first_login_s
                days_first_login = (diference_seconds_first_login // 86400)
                
                

            print("\n Username >>> " +data['player']['displayname'])
            print ("\n UUID >>> " +data['player']['uuid'])
            print("\n First login >>> ", days_first_login, "days ago")
            print("\n Last logout >>> ", days_last_logout, "days ago")
            print("\n Bed wars stats >>> ")
            print("\t Wins >>> " + str(bedwars.get('wins_bedwars', 0)))
            print("\t Losses >>> " + str(bedwars.get('losses_bedwars', 0)))
            print("\t Kills >>> " + str(bedwars.get('kills_bedwars', 0)))

        else:
            print("\n User not found :(")
    else:
        print ("\n Status code error.")

    return_to_menu()


def number_of_users():
    clear_console()
    
    url_currentplayers = "https://api.hypixel.net/v2/counts?key=" +API_KEY

    response = requests.get(url_currentplayers)

    if response.status_code == 200:
        data = response.json()
        current_players_data = data.get('playerCount', 0)

        print("Current players >>> " + str(current_players_data))

        return_to_menu()
    else:
        print("API Error")


def staff_list():
    clear_console()
    url_punishmentstats = "https://api.hypixel.net/v2/punishmentstats?key=" + API_KEY

    response = requests.get(url_punishmentstats)

    if response.status_code == 200:
        data = response.json()
        whatchdog_total = data.get('watchdog_total', 0)
        staff_totals = data.get('staff_total', 0)
        whatchdog_daily = data.get('watchdog_rollingDaily', 0)
        staff_daily = data.get('staff_rollingDaily', 0)

        print("Hypixel punishments statics >>> ")
        print("Daily >>> ")
        print("\t Staff daily bans ", staff_daily )
        print("\t Whatch dog daily bans ", whatchdog_daily )
        print("Total >>> ")
        print("\t Staff total bans ", staff_totals)
        print("\t Whatch dog total bans ", whatchdog_total)

        return_to_menu()

    else:
        print("Error al obtener datos del API.")
        return_to_menu()

main_menu()
