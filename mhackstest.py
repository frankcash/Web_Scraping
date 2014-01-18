#main file
print "Welcome to BrowseScape.."
input = raw_input("")

if input == "weather":
	import weatherTest

elif input == "wikipedia":
	import wikipediaAPI

elif input == "exit":
	exit()