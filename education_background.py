import requests
from bs4 import BeautifulSoup

def education_background(URL):
    
    prof_URL = requests.get(URL)

    soup = BeautifulSoup(prof_URL.content, 'html.parser')

    # store professor's name and academic title in database
    professor_info = soup.find('div', class_ = "contentDetail faculty-directory page-faculty")

    # Try-catch used to prevent one invalid URL to cause the script to crash
    try:
        professor_name = professor_info.find('h4', class_= "facultyname").text
        professor_academic_title = professor_info.find('p').text

        # store professor's degree infos
        degree_background = soup.find('div', class_ ='education-piece')
        degrees = []
        for li in degree_background.ul:
            if li.text == '':
                break
            degrees.append(li.text)
            
        professorBackground = [professor_name, professor_academic_title, degrees]
        return professorBackground
    except:
        # Could possibly append broken URLs here to repeat them back in the calling function
        return False