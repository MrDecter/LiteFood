import sqlite3

# Создание Базы
import time

db = sqlite3.connect('repices.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS repices (
    name_rep TEXT,
    product TEXT,
    discript_rep TEXT,
    all_rep TEXT
    )""")
db.commit()

# Функции

# Функция:Добавление рецепта
def AddRep():
    # Получение значений
    # Все переведено в нижний регист, для избежание дублей в таблице
    name = input('Название рецепта:\n').lower()
    discript = input('Описание рецепта:\n').lower()
    main_rep = input('Инструкция рецепта:\n').lower()
    prod = []
    z = True
    while z == True:
        produc = input('Какие продукты используете?\nP.S.Вводите по одному\n').lower()
        prod.append(produc)
        logis = int(input('1. Добавить еще один\n2. Закончить\n'))
        if logis == 1:
            z = True
        else:
            prod.sort()
            print('Вы добавили: ' + str(prod))
            z = False
            time.sleep(3)

    # Проверка имени
    sql.execute(f"SELECT name_rep FROM repices WHERE name_rep = '{name}'")
    if sql.fetchone() is None:
        # Если совпадений нет, добавление
        sql.execute(f'INSERT INTO repices VALUES(?,?,?,?)',(name,prod,discript,main_rep))
        db.commit()
        print("Рецепт добавлен!")
    else:
        # Если есть совпадения
        print('Такой рецепт уже есть!')
        for value in db.execute('SELECT * FROM repices'):
            print(value)

# Функция:Показать все рецепты
def AllRep():
    testing = sql.execute("SELECT * FROM repices")
    allfetch = testing.fetchall()
    q = 0
    while q != len(allfetch):
        i = 0
        print(str(q + 1) + '.Рецепт')
        while i < 4:
            if i == 0:
                print('Название: \n' + allfetch[q][i])
                i = i + 1
            elif i == 1:
                print('Продукты: \n' + allfetch[q][i])
                i = i + 1
            elif i == 2:
                print('Описание: \n' + allfetch[q][i])
                i = i + 1
            else:
                print('Рецепт: \n' + allfetch[q][i] + '\n')
                i = i + 1
        q = q + 1

# Функция:Показать рецепт по числу
def OneRep():
    Grab = sql.execute("SELECT * FROM repices")
    Grab_all = Grab.fetchall()
    One = int(input('Рецепт под каким номером будем искать? \n'))
    One = One - 1
    if One < len(Grab_all):
        print('Поиск рецепта под номером: ' + str(One + 1))
        i = 0
        while i < 3:
            if i == 0:
                print('Название: \n' + Grab_all[One][i])
                i = i + 1
            elif i == 1:
                print('Продукты: \n' + Grab_all[One][i])
                i = i + 1
            elif i == 2:
                print('Описание: \n' + Grab_all[One][i])
                i = i + 1
            else:
                print('Рецепт: \n' + Grab_all[One][i] + '\n')
                i = i + 1
    else:
        print('Рецепта с таким номером нет')
        time.sleep(2)
        menus = input('1. Вернуться \n 2. Повторить \n')
        if menus == 1:
            print('Возврат в начальное меню...')
            time.sleep(2)
            LiteFood()
        elif menus == 2:
            print('Возврат в начало поиска...')
            time.sleep(2)
            OneRep()
        else:
            print('Введеное значение не опознано, вы возвращаеться в главное меню')
            time.sleep(2)


# Функция:Выбора функции
def LiteFood():
    print('Добро пожаловать в LiteFood! \n 1. Добавить рецепт \n 2. Посмотреть рецепты \n 3. Посмотреть рецепт по номеру')
    # Проверка типа данных
    try:
        manag = int(input())
        if manag == 1:
            AddRep()
        elif manag == 2:
            AllRep()
        elif manag == 3:
            OneRep()
        else:
            print('Введено неверное значение, повторите!')
            time.sleep(2)
            LiteFood()
    except ValueError:
        print('Введеное значение не явзяеться числом, повторите попытку!')
        time.sleep(2)
        LiteFood()

# Запуск
LiteFood()