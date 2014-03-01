from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import requests

def countUsers():
    i=1
    foo=0
    numberOfTeams=0
    while(i<2):
        urlOne="http://registration.coded.io/events/1/teams"
        urlGen="http://registration.coded.io"
        #url="http://registration.coded.io/events/1/teams/"+str(i)
        content=urllib2.urlopen(urlOne).read()
        soup=BeautifulSoup(content)
        #temp=soup.find_all('p')
        links={}
        urlLink={}
        count=0
        for link in soup.find_all('a'): #grabs all the team ideas and stores in hash map
            links[foo]=link.get('href') #match the href with the actual text using magic
            #print links[foo]
            contentGen=urllib2.urlopen(urlGen+links[foo])
            soupGen=BeautifulSoup(contentGen)
            temp=soupGen.find_all('p')
            if (1<len(temp)):
                if (links[foo][:16]=="/events/1/teams/"): #takes a substring and compare it to a string
                    #I think I need a while loop here
                    numberOfTeams+=1
                    print numberOfTeams
                    tempLink = links[foo]
                    urlStink=urlGen+tempLink
                    urlLink[count]=urlGen+tempLink
                    count+=1
                    print urlLink #making sure the url is right
                    contentLink=urllib2.urlopen(urlStink)
                    soupLink=BeautifulSoup(contentLink)
                    tempP = soup.find_all('p')
                    #print tempLink
                   # print tempP
                    #need to follow down these links
                    #then get <p> tags that correalate to names
                foo+=1
                #print (temp)
            #end of for loop
        i+=1
        #print temp

print(countUsers())
