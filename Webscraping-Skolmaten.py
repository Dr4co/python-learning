import requests
import datetime
from bs4 import BeautifulSoup

# Get the data
data = requests.get('https://skolmaten.se/brunnbyskolan/')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

weekdaysWithMeals = soup.find_all('div', {'class':'row'})

weekdays = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag"]
    
weekdayToday = datetime.datetime.today().weekday()

if weekdayToday < 5:
    print(datetime.date.today(), " - ", weekdays[weekdayToday])
    todaysElement = weekdaysWithMeals[weekdayToday].get_text().strip()
    stringArray = todaysElement.split("\n")

    # Unfortunately Beautifoulsoup interprets the DOM and includes the \n/line-breaks
    # which needs to be cleaned-up.
    # Remove dummy Beautifoulsoup line-breaks!
    while("" in stringArray) :
        stringArray.remove("")

    if stringArray != ['']:
        for i in range(len(stringArray)):
            if i > 2:
                print(stringArray[i])
else:
    print("Idag serveras ingen mat i skolan! Njut av helgen! :)")

# Example Output:
# 2021-10-06  -  Onsdag
# Köttbullar, gräddsås, potatis, lingon
# Laxpaj med spenat
# Vegobullar, gräddsås, potatis
