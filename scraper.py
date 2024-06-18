import requests
from bs4 import BeautifulSoup

r = requests.get("https://viterbi.usc.edu/directory/faculty/")

print(r)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

allFaculty = soup.find_all('div', class_ = 'faculty-member')

count = 0;

for resultName in allFaculty:
     professors = resultName.h5.text
print(professors)