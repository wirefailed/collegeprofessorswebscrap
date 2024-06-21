from scraper import USC_scraper
from education_background import education_background
import psycopg2

def main():
    USC_professors_infos = []
    USC_scraper(USC_professors_infos)
    # sorts USC_professors_infos based off its name order
    sorted(USC_professors_infos, key=lambda x: x[0])
    
    # to check if it works 
    # for i in USC_professors_infos:
        # print(i)

    print("What is your postgres password?")
    passWord  = input()

    conn = psycopg2.connect(host="localhost", dbname="collegeprofessorinfos", user="postgres", 
                            password=passWord, port=5432)

    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS professor (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        academic_title VARCHAR(100)
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS degrees (
        id SERIAL PRIMARY KEY,
        prof_name VARCHAR(100) NOT NULL,
        degree VARCHAR(100),
        FOREIGN KEY(prof_name) REFERENCES professor(name)
    );""")

    for i in range(len(USC_professors_infos)):
        professor_name = USC_professors_infos[i][0]
        professor_academic_title = USC_professors_infos[i][1]
        cur.execute("""INSERT INTO professor(name, academic title) VALUES (%s, %s)""", 
        (professor_name, professor_academic_title))
        for j in range(len(USC_professors_infos[i][2])):
            degree = USC_professors_infos[i][2][j]
            cur.execute("""INSERT INTO degrees(prof_name, degree) VALUES(%s, %s)""",
            (professor_name, degree))

    conn.commit()

    cur.close()
    conn.close()
    return 0

if __name__ == '__main__':
    main()