import requests
from bs4 import BeautifulSoup
# from education_background import education_background 

def USC_scraper():
     r = requests.get("https://viterbi.usc.edu/directory/faculty/")
     list_URL = []

      
     soup = BeautifulSoup(r.content, 'html.parser')

     allFaculty_div = soup.find('div', id = 'results')
     allFaculty_a = allFaculty_div.find_all('a')

     for professor_link in allFaculty_a:
          list_URL(professor_link['href'])
          
     
     for URL in list_URL:
          print(URL)
          
         # education_background('https://viterbi.usc.edu/directory/faculty/' + URL, main_matrix)

