import requests
import webbrowser
from bs4 import BeautifulSoup
from random import randint
import time

page_numbers = ["SADqAwA%253D", "SBTqAwA%253D", "SCjqAwA%253D"]
search_terms_poll = ["Chopin", "beethoven", "Mozart"]
search_term = search_terms_poll[randint(0,len(search_terms_poll)-1)]
result_link=[]
#search term check
#print(search_term)

#gives you link from the list Youtube
def youtubeLinkCrawler(search_term, max_page):
    page = 0
    while page < max_page:
        url = "https://www.youtube.com/results?search_query=" + str(search_term) + "&sp=" + page_numbers[page]
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a', {'class':'yt-uix-tile-link'}):
            href = link.get('href')
            href_url = "https://www.youtube.com/" + href
            if (len(href_url) == 44):
                result_link.append(href_url)
        page += 1

def getPlayLink(result_link):
    play_link = result_link[randint(0, len(result_link) - 1)]
    webbrowser.open(play_link)
    #print(play_link)

#youtubeLinkCrawler(str(search_term), 1)
#getPlayLink(result_link)

