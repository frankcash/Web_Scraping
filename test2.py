#makes use of Michigan Tech's Directory

from splinter import Browser
with Browser() as browser:
    url = "https://www.mtu.edu/mtuldapweb/web_lookup/"
    browser.visit(url)
    browser.fill('advtext', 'Frank')
    #find and click the 'search' button
    button = browser.find_by_name('submit')
    #interact with elements
    button.click()
    if browser.is_text_present('fjkampe'):
        print "True"
    else:
        print "False"