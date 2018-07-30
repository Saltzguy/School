import urllib.request
import os
from bs4 import BeautifulSoup


# will print somthing so long as it is not a NoneType
def remove_none_print(input):
    if input is not None:
        print(input)


url = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'

try:
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
except:
    print("failed")
    exit(0)

soup = BeautifulSoup(res, "html.parser")

#prints the title of the webpage
print() # adds some nice spacing
remove_none_print(soup.title.getText())
print()# adds some nice spacing

#finds all links in the page and print
for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None and "https" not in href:
        href = "https://en.wikipedia.org" + href
    remove_none_print(href)
    

table = soup.find('table','wikitable sortable plainrowheaders')

#for each row in the table
for row in table.find_all('tr'):
    print()
    #for each cell in the row
    s = ""
    for cell in row.find_all('td'):
        s = s + " " +cell.getText()
    print(s)


    