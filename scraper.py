import requests
from bs4 import BeautifulSoup

r = requests.get("https://viterbi.usc.edu/directory/faculty/")

#print(r)

soup = BeautifulSoup(r.content, 'html.parser')


allFaculty_div = soup.find('div', id = 'results')
allFaculty_a = allFaculty_div.find_all('a')

for href in allFaculty_a:
     print(href['href'])