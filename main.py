import sqlite3

# Создание Базы
db = sqlite3.connect('repices.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS repices (
    name_rep TEXT,
    discript_rep TEXT,
    all_rep TEXT
    )""")
db.commit()

# Получение значений
# Все переведено в нижний регист, для избежание дублей в таблице
name = input('Название рецепта:\n').lower()
discript = input('Описание рецепта:\n').lower()
main_rep = input('Инструкция рецепта:\n').lower()

# Проверка имени
sql.execute(f"SELECT name_rep FROM repices WHERE name_rep = '{name}'")
if sql.fetchone() is None:
    # Если совпадений нет, добавление
    sql.execute(f'INSERT INTO repices VALUES(?,?,?)',(name,discript,main_rep))
    db.commit()
    print("Рецепт добавлен!")
else:
    # Если есть совпадения
    print('Такой рецепт уже есть!')
    for value in db.execute('SELECT * FROM repices'):
        print(value)
