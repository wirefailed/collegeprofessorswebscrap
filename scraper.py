import requests
from bs4 import BeautifulSoup
from education_background import education_background 

def USC_scraper(mainMatrix):
    r = requests.get("https://viterbi.usc.edu/directory/faculty/")
    list_URL = []
        
    soup = BeautifulSoup(r.content, 'html.parser')

    allFaculty_div = soup.find('div', id = 'results')
    allFaculty_a = allFaculty_div.find_all('div', class_ = 'faculty-member')

    for professor_link in allFaculty_a:
        list_URL.append(professor_link.find('div', class_ = 'faculty-text').find('a')['href'])     

    for URL in list_URL:
        # test to see if the URL is valid
        testURL = requests.get('https://viterbi.usc.edu' + URL)
        if(testURL.ok == False):
            continue

        returnInfo = education_background('https://viterbi.usc.edu' + URL)
        
        # Used to check if the returned matrix is valid
        if(returnInfo == False):
            continue
        else:
            mainMatrix.append(returnInfo)