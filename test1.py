from bs4 import BeautifulSoup
import urllib
import urllib2
import requests

"""urlInput = raw_input("enter a url which you wish to find all the URLs on\n")
url = urlInput"""
url = "http://www.python.org"
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)
for link in soup.find_all('a'):
    print(link.get('href'))#reads the links
    
"""print(soup.title.string)#reads the title"""


print(soup.find_all(text="python"))


