from scraper import USC_scraper
from education_background import education_background

def main():
    USC_professors_infos = []
    USC_scraper(USC_professors_infos)
    # sorts USC_professors_infos based off its name order
    sorted(USC_professors_infos, key=lambda x: x[0])

    # to check if it works 
    for i in USC_professors_infos:
        print(i)
    
    return 0

if __name__ == '__main__':
    main()