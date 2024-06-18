from scraper import USC_scraper
from education_background import education_background

def main():
    USC_professors_infos = []
    USC_scraper(USC_professors_infos)

    # to check if it works 
    for i in USC_professors_infos:
        print(i)
    
    return 0

if __name__ == "__main__":
    main()