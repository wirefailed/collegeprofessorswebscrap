import requests
from bs4 import BeautifulSoup

r = requests.get("https://viterbi.usc.edu/directory/faculty/")

print(r)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())