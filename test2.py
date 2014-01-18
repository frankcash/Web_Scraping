#makes use of Michigan Tech's Directory
name = raw_input("Enter the first name of the person you wish to look up: ")
from splinter import Browser
with Browser() as browser:
    url = "https://www.mtu.edu/mtuldapweb/web_lookup/"
    browser.visit(url)
    browser.fill('wuSearch.br5.ui-autocomplete-input', name)
    #find and click the 'search' button
    button = browser.find_by_name('submit')
    #interact with elements
    button.click()
    raw_input("")#gives a way for me to observe
