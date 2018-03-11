#!/usr/bin/python

import sys
import requests
import ConfigParser
from twilio.rest import Client
from bs4 import BeautifulSoup

def sendText(title, url):
    environment = 'TRIAL'
    config = ConfigParser.ConfigParser()
    config.read('/home/ubuntu/project/config.ini')

    # twilio send message
    account_sid = config.get(environment,'account_sid')
    auth_token = config.get(environment,'auth_token')
    to_number = config.get(environment,'to_number')
    from_number = config.get(environment,'from_number')
    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to=to_number,
        from_=from_number,
        body="New Product from Hot Topic: \n" + title + '\n' + url)

def main():
    url = 'https://www.hottopic.com/pop-culture/shop-by-license/invader-zim/'

    try:
        page = requests.get(url)
    except:
        print 'Website is down: ' + url + "\n"
        sys.exit(1)

    # make list of already owned items.
    with open ('zimList','r') as zimListFile:
        zimList = zimListFile.readlines()
    zimListFile.close()
    zimList = [x.strip() for x in zimList]

    soup = BeautifulSoup(page.content, 'html.parser')

    items = soup.find_all('li',{'class':'grid-tile'})

    zimListFile =  open('zimList','a')
    for item in items:
        title = item.find('a',{'class':'thumb-link'})['title']
        if title not in zimList:
            print title
            link = item.find('a',{'class':'thumb-link'})['href']
            sendText(title, link)
            zimListFile.write(title + "\n")
    zimListFile.close()
    print '~fin.'



if __name__ == '__main__':
    main()




