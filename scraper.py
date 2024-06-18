import requests
from bs4 import BeautifulSoup
from education_background import education_background 

def USC_scraper(mainMatrix):
    r = requests.get("https://viterbi.usc.edu/directory/faculty/")
    list_URL = []
        
    soup = BeautifulSoup(r.content, 'html.parser')

    allFaculty_div = soup.find('div', id = 'results')
    allFaculty_a = allFaculty_div.find_all('div', class_ = 'faculty-member')

    unique_URLs = set()

    for professor_link in allFaculty_a:
          href_URL = professor_link.find('div', class_ = 'faculty-text').find('a')['href']
          # hashset to only get uniquearray
          if href_URL and href_URL not in unique_URLs:
               unique_URLs.append(href_URL)
               list_URL.append(href_URL)   
          else:
               print(f"No href found or duplicate href: {href_URL}")  

    for URL in list_URL:
        mainMatrix.append(education_background('https://viterbi.usc.edu' + URL))




