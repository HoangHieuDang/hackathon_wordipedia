import wikipedia
import random

def get_random_article():
    """ Gets a random article from Wikipedia, its content, and linked articles.
    It returns a tuple containing the article's title, its content and a list of linked articles """
    while True: #Runs until it finds a valid article
        try:
            random_article_name = wikipedia.random() #Finds a random article and returns the name
            random_article = wikipedia.page(random_article_name) #Using the random article name, it returns the whole article 
            random_article_content = random_article.content #It gets the articles content
            random_article_links = random_article.links #It gets the articles links in a list 
        except wikipedia.exceptions.PageError: 
            raise ValueError(f"Article '{random_article_name}' not found. Trying again...")
        except wikipedia.exceptions.DisambiguationError as e:
            raise ValueError(f"'{random_article_name}' is ambiguous." 
            f"Possible options: {e.options}. Trying again with a different article...")
            random_article_name = e.options[0] #Tries to use the first option from the ambiguous list
        else:
            return random_article_name, random_article_content, random_article_links 
            #Returns a tuple, string, string, list



def get_specified_article(article_name):
    """ Gets a specified article depending on the article chosen by the user. """
    while True:
        try:
            article = wikipedia.page(article_name) #Gets the entire article using specified name (parameter)
            article_content = article.content #Gets articles content
            article_links = article.links #Gets the articles links
            return article, article_content, article_links #Returns a tuple.
        except wikipedia.exceptions.PageError:
            raise ValueError (f"Article '{random_article_name}' not found")
        except wikipedia.exceptions.DisambiguationError as e:
            raise ValueError(f"'{article}' is ambiguous. Possible options: {e.options}.")

# make indexes randomly in set
def set_random_links(article_links):
    """ Gets the links and randomly assigns them a number on the list.
    Returns a list. """
    list_of_numbers = list(range(1, len(article_links) + 1))
    random.shuffle(list_of_numbers)
    set_of_links = set()  
    for number, link in zip(list_of_numbers, article_links):
        set_of_links.add(f"{number}.{link}")
    set_of_links.sort(key = lambda x: int())
    return set_of_links

links = ["Wikipedia", "Python", "API", "Programming"]
numbered_links = set_random_links(links)
print(numbered_links)

    