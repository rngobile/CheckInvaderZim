#!/usr/bin/python

from bs4 import BeautifulSoup
import requests

def main():
    url = 'https://www.hottopic.com/pop-culture/shop-by-license/invader-zim/'

    # make list of already owned items.
    with open ('zimList','r') as zimListFile:
        zimList = zimListFile.readlines()
    zimListFile.close()
    zimList = [x.strip() for x in zimList]

    print str(len(zimList)) + ': ' + str(zimList)

    try:
        page = requests.get(url)
    except:
        print 'Website is down: ' + url + "\n"

    soup = BeautifulSoup(page.content, 'html.parser')

    items = soup.find_all('li',{'class':'grid-tile'})

    for item in items:
        link = item.find('a',{'class':'thumb-link'})['href']
        title = item.find('a',{'class':'thumb-link'})['title']
        print title



if __name__ == '__main__':
    main()




