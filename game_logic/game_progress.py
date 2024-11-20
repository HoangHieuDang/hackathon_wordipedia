'''
This is where the main game loop logic is defined
'''
'''
import sys
sys.path.insert(0, '/project/workspace/database')
sys.path.insert(0, '/project/workspace/ui')
import ui.print_game_info as print_game_info
import ui.user_input as user_input
import database.game_data_info as game_data_info
'''
from ..ui.user_input import count_word
#initialize the game: reset given_word to empty string "", 
count_word()
game_data_info.given_word = ""

#reset the player_dict to empty dictionary
if not game_data_info.player_dict:
    for player in game_data_info.player_dict:
        del game_data_info.player_dict[player]    
print(f"Database after clearing: {game_data_info.player_dict}")

#ask how many players (2 players minimum and 4 players maximal)
#ask for names of the players
players_dict = user_input.players_dict() 

#this gonna return of a list of players names
#update the player_dict with players names
print (f"New players from input handle players_dict{players_dict}")
for player in players_dict:
#add the players from players_dict to our player_dict in the game_data_info
    if player not in game_data_info.player_dict:
        game_data_info.player_dict[player] = {"word_freq":0, "wiki_page":"", "stay":False}
print(f"database of players after updating: {game_data_info.player_dict[player]}")


#announce the new players on the display
#print_start_announcement(game_data_info.player_dict[player])

#Generate random word from word list database for given_word and
#store the randomized word into given_word variable in the game_data_info.py


#Generate starting wiki page, store the starting wiki page into player dictionary


#Display the given word and the starting wikipedia pages
print_game_info.print_given_word()
print_game_info.print_wiki_page_name()

'''
#main loop start
while True:
    for player in game_data_info.player_dict:
        #Check if every player wants to stay or move on to the next
        if user_input.check_input():
            print_game_info.print_linked_wiki_pages(player)

'''