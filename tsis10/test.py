import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="postgres_db",
        user="postgres",
        password="asasin00",
        port=5432
    )
    print("Connection successful")
except Exception as e:
    print("Connection failed:", e)

try:
    cur = conn.cursor()
    print("Cursor created")
except Exception as e:
    print("Cursor creation failed:", e)
