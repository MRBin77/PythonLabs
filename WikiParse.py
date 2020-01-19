import re
import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {'Accept-Encoding': 'identity'}
    response = requests.get(url, headers=headers)
    return response.content


def parse_html(html):
    soup = BeautifulSoup(html, features="html.parser")
    links = []
    ar = []
    for link in soup.find_all('a', attrs={'href': re.compile("^(/wiki/)((?!:).)*$")}):
        try:
            if link not in links:
                link = 'https://en.wikipedia.org' + link['href']
                links.append(link)
        except KeyError:
            pass
    #for i in links:
     #   return parse_html(get_html(i))
    #print(links)
    return links

def main_link(html):
    soup = BeautifulSoup(html, features="html.parser")
    links = soup.findAll('link', rel="canonical")
    for link in links:
        link = link['href']
    return link


def main():

    article1 = main_link(get_html('https://en.wikipedia.org/wiki/Special:Random'))
    article2 = main_link(get_html('https://en.wikipedia.org/wiki/Special:Random'))
    print('article 1 ' + article1)
    print('article 2 ' + article2)
    parse_art1 = parse_html(get_html(article1))
    parse_art2 = parse_html(get_html(article2))
    print('links article 1:')
    print(parse_art1)
    print('links article 2:')
    print(parse_art2)



if __name__ == '__main__':
     main()
