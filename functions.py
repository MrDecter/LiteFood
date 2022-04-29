# -*- coding: cp1251 -*-
import main


# Функция запуска
def start():
    print(
        "Приветствует в LiteFood. Суть программы, предоставить вам рецепты только из тех продуктов, которые у вас есть."
    )
    variant = int(input("Что выбираем? \n 1. Поиск по продуктам \n 2. Поиск по цене \n 3. Добавить рецепт \n"))
    if variant == 1:
        print('Вы выбрали поиск по продуктам')
    elif variant == 2:
        print('Вы выбрали поиск по цене')
    elif variant == 3:
        print('Вы выбрали добавление рецепта')
        addsql()
    else:
        print("Введеное значение не верно, попробуйте еще раз.")


# Добавление в sql
def addsql():
    main.cur.execute("""INSERT INTO repices(name, item, repices) 
       VALUES(name_repices, item_repices, repices_repices);""")
    main.conn.commit()
