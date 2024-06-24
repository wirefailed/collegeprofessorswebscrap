from scraper import USC_scraper
from education_background import education_background
import psycopg2
from getpass import getpass

def main():
    USC_professors_infos = []
    USC_missed_professor_infos = []
    USC_scraper(USC_professors_infos, USC_missed_professor_infos)
    print("Retrieving USC professors' informations")

    # sorts USC_professors_infos based off their first name name order
    sorted(USC_professors_infos, key=lambda x: x[0].split()[-1])
    print("Sorting Matrix in alphabethical order")

    # to check if it works 
    # for i in USC_professors_infos:
        # print(i)

    print("Connecting to data base")
    print("Write your password")
    passWord  = getpass()

    try: 
        conn = psycopg2.connect(
            host="localhost", 
            dbname="collegeprofessorinfos", 
            user="postgres", 
            password=passWord, 
            port=5432
        )
        cur = conn.cursor()

        print("Well connected, creating or checking if table exists")

        cur.execute("""
            CREATE TABLE IF NOT EXISTS professor (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                academic_title VARCHAR(255)
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS degrees (
                id SERIAL PRIMARY KEY,
                professor_id INTEGER NOT NULL,
                degree VARCHAR(255),
                FOREIGN KEY (professor_id) REFERENCES professor(id)
            );
        """)

        print("Inserting datas into the database")

        for professor_info in USC_professors_infos:
            professor_name = professor_info[0]
            professor_academic_title = professor_info[1]

            cur.execute("""INSERT INTO professor(name, academic_title) VALUES (%s, %s) RETURNING id""", 
            (professor_name, professor_academic_title))

            professor_id = cur.fetchone()[0]

            for degree_info in professor_info[2]:
                cur.execute("""INSERT INTO degrees(professor_id, degree) VALUES(%s, %s)""",
                (professor_id, degree_info))

        conn.commit()
    
    except psycopg2.OperationalError as e:
        print(f"An error occurred: {e}")
        conn.rollback()

    cur.close()
    conn.close()

    print("Everything saved")
    return 0

if __name__ == '__main__':
    main()