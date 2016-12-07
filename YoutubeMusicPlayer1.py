import requests
import webbrowser
from bs4 import BeautifulSoup
from random import randint
from datetime import datetime
import time

#Page number 1, 2, 3 only
page_numbers = ["SADqAwA%253D", "SBTqAwA%253D", "SCjqAwA%253D"]
#type search keyword
search_terms_poll = ["Chopin", "beethoven", "Mozart"]
search_term = search_terms_poll[randint(0,len(search_terms_poll)-1)]
result_link=[]
isYoutubePlayed = False
startTime = 1
endTime = 23
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

def getPlayLink(result_link, startTime, endTime, isYoutubePlayed):
    play_link = result_link[randint(0, len(result_link) - 1)]
    ts = datetime.now().strftime('%H')
    #when not the time
    print("Not playing, current time is: ", ts)
    time.sleep(5)
    #print(startTime)
    #print(endTime)
    while int(ts) >= startTime and int(ts) <= endTime and isYoutubePlayed== False:
        #print(ts)
        time.sleep(5)
        ts = datetime.now().strftime('%H')
        webbrowser.open(play_link)
        #print(play_link)
        isYoutubePlayed = True
    getPlayLink(result_link, startTime, endTime, isYoutubePlayed)
youtubeLinkCrawler(str(search_term), 1)
getPlayLink(result_link,startTime, endTime, isYoutubePlayed)

