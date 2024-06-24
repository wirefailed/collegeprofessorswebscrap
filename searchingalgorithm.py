import psycopg2
from getpass import getpass

def searching_algorithm(search_term):
    print("Write your PostgresSQL password")
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

        query = """SELECT p.name, p.academic_title, d.degree
                FROM professor p
                JOIN degrees d
                ON p.id = d.professor_id
                WHERE d.degree LIKE %s
            """        

        cur.execute(query, ('%' + search_term + '%',))

        results = cur.fetchall()

        conn.commit()
    
    except psycopg2.OperationalError as e:
        print(f"An error occurred: {e}")
        conn.rollback()

    cur.close()
    conn.close()

    return results

search_term = input("Enter a partial academic title to search for: ")
results = searching_algorithm(search_term)
for row in results:
    print(f"Name: {row[0]}, Title: {row[1]}, Degree Details: {row[2]}")
