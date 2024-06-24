import psycopg2
from getpass import getpass

print("Write your password")
passWord  = getpass()
USC_professors_infos = ['Ali Abbas', 'Professor of Industrial and Systems Engineering and Public Policy', ['2004, Doctoral Degree, Management Science and Engineering, Stanford University', '2004, Doctoral Degree, Electrical Engineering, Stanford University', "2002, Master's Degree, Industrial Engineering, Stanford University", "1998, Master's Degree, Electrical Engineering, Stanford University"]]

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