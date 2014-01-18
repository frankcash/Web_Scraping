#main file
from timeit import default_timer
start = default_timer()
duration = default_timer()-start
minutes=duration/60

print "Welcome to BrowseScape.."
print "Current commands include weather, wikipedia, search, and exit."



while minutes<1000:
	input=raw_input("")
	if input == "weather":
		import weatherTest

	elif input == "wikipedia":
		import wikipediaAPI

	elif input == "search":
		import test1

	elif input == "exit":
		exit()



