#main file
print "Welcome to BrowseScrape.."
print "Current commands include weather, wikipedia, search, and exit."
x=0
i=0
while (x<20):
	i=0
	while(0<1):
		input=raw_input("")
		if input == "weather":
			import weatherTest

		elif input == "wikipedia":
			import wikipediaAPI

		elif input == "search":
			import test1
		elif input == "exit":
			exit()

		i+=1