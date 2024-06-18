import requests
from bs4 import BeautifulSoup

r = requests.get("https://viterbi.usc.edu/directory/faculty/")

print(r)

soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())

allFaculty = soup.find_all('div', class_ = 'id')

for a in allFaculty:
    print(a["href"])