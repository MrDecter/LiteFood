import sqlite3
import functions

# Создание SQL
conn = sqlite3.connect(r'sql/repices.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS repices(
   userid INT PRIMARY KEY,
   name TEXT,
   item TEXT,
   repices TEXT);
""")
conn.commit()
# Запуск
functions.start()
