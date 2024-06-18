import requests
from bs4 import BeautifulSoup

def education_background(id, URL):
    prof_URL = requests.get(URL)

    soup = BeautifulSoup(prof_URL.content, 'html.parser')

    # store professor's name and academic title in database
    professor_info = soup.find('div', class_ = "profileTopRight")
    professor_name = professor_info.find('h1', class_= 'facultyname').text
    professor_academic_title = professor_info.find('p', class_='faculty_academic_title').text
    # db[1] = professor_name 
    # db[2] = professor_academic_title

    # store professor's degree infos
    degree_background = soup.find_all('div', class_ ='education-piece')
    database_count = 3
    for degree in degree_background:
        degree_university = degree.li.text
        #db[database_count] = degree_university
        database_count += 1
    