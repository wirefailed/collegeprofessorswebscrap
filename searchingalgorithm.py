import psycopg2

def searching_algorithm(search_term):
    print("What is your postgres password?")
    passWord  = input()

    conn = psycopg2.connect(host="localhost", dbname="collegeprofessorinfos", user="postgres", 
                            password=passWord, port=5432)

    cur = conn.cursor()

    query = """SELECT id, name
                FROM degrees
                WHERE degree LIKE %s
            """

    cur.execute(query, ('%' + search_term + '%',))

    results = cur.fetchall()

    cur.close()
    conn.close()

    return results

search_term = input("Enter a partial academic title to search for: ")
