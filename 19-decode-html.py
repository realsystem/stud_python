from bs4 import BeautifulSoup
import requests


if __name__ == '__main__':
    url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, 'html.parser')
    for p in soup.find_all('p'):
        if p.string is not None:
            print p.string
