import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="snake",
        user="postgres",
        password="asasin00",
        port=5432
    )
    print("Connection successful")
except Exception as e:
    print("Connection failed:", e)
