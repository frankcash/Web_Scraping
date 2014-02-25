from bs4 import BeautifulSoup
import urllib
import urllib2
import requests
import re

urlInput = raw_input("enter the page you wish to go to\n") #this adds an option for user input
lookingFor = raw_input("what are you looking for?\n")

def runSoup(urlInput, lookingFor): #defines the function
    url = urlInput
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    print("The title of this page is "+soup.title.string+"\n") #reads the title 
    print ("\n")
    print("Your Search Returned"+ "\n")
    results=(soup.findAll(text=re.compile(lookingFor))) #will display everything inolving python
    print(results)
    return

runSoup(urlInput,lookingFor) #runs the function
