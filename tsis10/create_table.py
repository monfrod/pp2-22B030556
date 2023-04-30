import psycopg2

from database import conn

def create_tables():
    command = """CREATE TABLE contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR,
            email VARCHAR
        )
        """,
        """
        CREATE TABLE phone_numbers (
            id SERIAL PRIMARY KEY,
            number VARCHAR,
            contact_id INTEGER REFERENCES contacts(id)
        )"""

    try:
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
    except (Exception, psycopg2.DatabaseError) as error:
         print(error)
    finally:
         if conn is not None:
             conn.close()




