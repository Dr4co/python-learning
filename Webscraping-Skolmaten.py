import requests
from bs4 import BeautifulSoup

# Get the data
data = requests.get('https://skolmaten.se/brunnbyskolan/')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

weekdaysWithMeals = soup.find_all('div', {'class':'row'})

for daystructure in weekdaysWithMeals:
    daystructure
    stringElement = daystructure.get_text().strip()
    stringArray = stringElement.split("\n")
    if stringArray != ['']:
        # Unfortunately Beautifoulsoup interprets the DOM and includes the \n/line-breaks
        # which needs to be cleaned-up.
        for string in stringArray:
            if string != '':
                print(string)

# Example Output:
# Måndag
# Mån
# 2021-10-04
# Stekt fisk, dressing, potatismos
# Biff Lindström, gräddsås, potatis
# Morotsbiff, dressing, potatis
