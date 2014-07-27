import urllib2
import random
import time
import os
from bs4 import BeautifulSoup as Soup

html = urllib2.urlopen("http://theodoreziras.com/lickoftheweek.htm").read()
soup = Soup(html)
table = soup.find_all('table')[-1]
entries = table.find_all('tr')[1:]

for entry in entries:
    links = map(lambda a:a['href'], entry.find_all('a'))
    youtube_link, tab_link = links[0], None
    if len(links) > 1:
        tab_link = links[1]
    print 'downloading video: ', youtube_link
    os.system('youtube-dl %s' % youtube_link)
    if tab_link != None:
        print 'downloading tab: ', tab_link
        os.system('wget %s' % tab_link)
    else:
        print 'no tab to download skipping...'
    time.sleep(random.randint(5,10))

print "Done!"
