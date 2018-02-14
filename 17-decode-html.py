from bs4 import BeautifulSoup
import requests
import re


def main():
    url = 'http://www.bbc.com/future/story/20180126-the-100-most-nutritious-foods'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, 'html.parser')
    for link in soup.find_all(string=re.compile('(v)')):
        print link
    # for link in soup.find_all(class_='story-heading'):
    #     if link.a:
    #         a = link.a.next_element
    #         if a.name == 'span':
    #             print a.next_element
    #         else:
    #             print a.strip()

main()
