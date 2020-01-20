import requests
from bs4 import BeautifulSoup
import re
from queue import Queue
import threading
import time


def get_news(url, queue):
    global time
    post_list = []
    while True:

        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        soup_find = soup.find_all('div', ['headline-list__item'])

        for i in soup_find:
            headline = i.find('div', 'headline-list__section').text
            text = i.find(['div', 'span'], 'headline-list__link-text').text
            times = i.find(['div', 'span'], 'headline-list__timestamp').text

            if headline not in post_list:
                post_list.append(headline)
                queue.put({
                    'headline-list__section': headline,
                    'headline-list__link-text': text,
                    'headline-list__timestamp': times
                })

        time.sleep(360)


queue = Queue()
url = 'https://www.boston.com/section/news'
thread = threading.Thread(target=get_news, args=(url, queue))
thread.start()
while True:
    post_list = queue.get()
    print(post_list['headline-list__section'])
    print(post_list['headline-list__link-text'])
    print(post_list['headline-list__timestamp'])
