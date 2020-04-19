import sys
import requests
import bs4

def wikiFun(link):
    res = requests.get(link)
    res.raise_for_status()

    wiki = bs4.BeautifulSoup(res.text,"html.parser")
    data = ''
    for i in wiki.select('p'):
        data += i.getText()
    return data
