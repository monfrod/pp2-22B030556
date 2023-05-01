import psycopg2

# подключаемся к базе данных
conn = psycopg2.connect(
    host="localhost",
    database="snake",
    user="postgres",
    password="asasin00"
)

# создаем курсор
cur = conn.cursor()

# выполняем запрос на выборку уровня пользователя
cur.execute("SELECT lvl FROM users WHERE name='Wynny'")

# получаем результат
result = cur.fetchone()
lvl = result[0] # получаем значение уровня
print(lvl)

# закрываем соединение с базой данных
cur.close()
conn.close()
