import requests
from bs4 import BeautifulSoup

# store items in hashmap

query = 'https://web.archive.org/web/20190202172037/https://dnd5e.fandom.com/wiki/Category:Character'
root = 'https://web.archive.org/web/20190202172037/https://dnd5e.fandom.com/wiki/'

def dump(urlquery, urlroot):
    page = requests.get(urlquery)
    soup = BeautifulSoup(page.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        print("Found the URL:", a['href'])

dump(query, root)
