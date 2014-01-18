#Generates Weather conditions utilizing the Python-Weather-API
import pywapi, pprint, string, time
location = raw_input("Which ZIP code would you like to know the weather for? \n")
displayTempIn = raw_input("Would you like the Temperature to be displayed in Celsius or Fahrenheit? \n")
pp = pprint.PrettyPrinter(indent=4)
weather = pywapi.get_weather_from_yahoo(location)

displayTempIn=displayTempIn.lower()#converts to lower case to prevent any errors from occuring

    # following code converts temperature from C to F

def CtoF(weather):
    global ftemp #declares ftemp to be a global variable
    temp = weather['condition']['temp']
    FTemp=int(float(temp)) # Converting from string to int to do math
    FTemp=FTemp*9
    FTemp=FTemp/5
    Ftemp=FTemp+32
    F=Ftemp
    ftemp=str(F) #converts from int to str so it can be output
    return;

CtoF(weather)

def displayResults(ftemp, weather):
    print("Outside Conditions Appear To Be "+weather['condition']['text'])#tells current conditions
    if displayTempIn == "celsius":
        print("The Temperature Is "+weather['condition']['temp']+u"\N{DEGREE SIGN}"+"C")#tells temperature in celsius
    elif displayTempIn == "fahrenheit":
        print("The Temperature Is "+ftemp+u"\N{DEGREE SIGN}"+"F")#tells temperature in fahrenheit
    else:  #if response was incromprehensible the display will default to both fahrenheit and celsius
        print("The Temperature Is "+weather['condition']['temp']+u"\N{DEGREE SIGN}"+"C")#tells temperature in celsius
        print("The Temperature Is "+ftemp+u"\N{DEGREE SIGN}"+"F")#tells temerature in fahrenheit
    print("Last Updated At "+weather['condition']['date'])#prints when last updated
displayResults(ftemp, weather)


"""
weather_com isn't working currently, need to look into issue

#Generates Weather conditions utilizing the Python-Weather-API
import pywapi, pprint, string, time
location = raw_input("Which ZIP code would you like to know the weather for? \n")
displayTempIn = raw_input("Would you like the Temperature to be displayed in Celsius or Fahrenheit? \n")
pp = pprint.PrettyPrinter(indent=4)
weather = pywapi.get_weather_from_weather_com(location)

displayTempIn=displayTempIn.lower()#converts to lower case to prevent any errors from occuring

    # following code converts temperature from C to F



def CtoF(weather):
        global ftemp #declares ftemp to be a global variable
        temp = weather['current_conditions']['temperature']
        FTemp=int(float(temp)) # Converting from string to int to do math
        FTemp=FTemp*9
        FTemp=FTemp/5
        Ftemp=FTemp+32
        F=Ftemp
        ftemp=str(F) #converts from int to str so it can be output
        return;
CtoF(weather)


def displayResults(ftemp, weather):
    print("Outside Conditions Appear To Be "+weather['current_conditions']['text'])#tells current conditions
    if displayTempIn == "celsius":
        print("The Temperature Is "+weather['current_conditions']['temperature']+u"\N{DEGREE SIGN}"+"C")#tells temperature in celsius
    elif displayTempIn == "fahrenheit":
        print("The Temperature Is "+ftemp+u"\N{DEGREE SIGN}"+"F")#tells temperature in fahrenheit
    else: #if response was incromprehensible the display will default to both fahrenheit and celsius
        print("The Temperature Is "+weather['current_conditions']['temperature']+u"\N{DEGREE SIGN}"+"C")#tells temperature in celsius
        print("The Temperature Is "+ftemp+u"\N{DEGREE SIGN}"+"F")#tells temerature in fahrenheit
    print("Last Updated At "+weather['current_conditions']['last_updated'])#prints when last updated
displayResults(ftemp, weather)


#speed=weather['current_conditions']['wind']['speed']#gets the wind speed

#print ("The High For Tomorrow Is "+weather['forecasts'][1]['high']+u"\N{DEGREE SIGN}"+"C")#tells tomorrow's high


"""