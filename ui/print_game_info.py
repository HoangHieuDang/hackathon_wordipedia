"""Veronica codes here :)"""

# storing the info as constants for easier maintenance and debbuging:

welcomePath = open("database/welcome.txt", "r", encoding = "utf-8")
instructionsPath = open("database/instructions.txt", "r", encoding = "utf-8")
rulesPath = open("database/rules.txt", "r", encoding = "utf-8")


def print_welcome():
    """
    Prints welcome message from database/welcome.txt
    """
    welcome_message = welcomePath.read()
    print(welcome_message)


def print_instructions():
    """
    Prints instructions for the game from database/instructions.txt
    """
    instructions = instructionsPath.read()
    print(instructions)


def print_rules():
    """
    Prints the rules of the game from database/rules.txt
    """
    rules = rulesPath.read()
    print(rules)


def print_start_announcement(player_dict):
    """
    Prints a greeting with the player's name and designation
    """
    print(f'')


def print_winner(): # gotta finish this one
    """
    Prints the name of the winner, along with the ocurrences
    for each player sorted by high to low ocurrences
    """
    print(f'The winner of this round is {winnerName}!')
    for key in playerDict.items():
        print(f'{key} had {value} ocurrucences.')
        # this should be sorted from high to low value
    pass

def print_given_word(random_word):

    #return the given word
    pass

def print_wiki_page_name(random_article):
    #return the wiki page name
    pass