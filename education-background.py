import requests
from bs4 import BeautifulSoup

def education_background(id, URL):
    prof_URL = requests.get(URL)

    soup = BeautifulSoup(prof_URL.content, 'html.parser')
    degree_background = soup.find_all('div', class_ ='education-piece')
    for degree in degree_background:
        degree_university = degree.li.text