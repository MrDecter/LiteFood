# -*- coding: cp1251 -*-
import main


# ������� �������
def start():
    print(
        "������������ � LiteFood. ���� ���������, ������������ ��� ������� ������ �� ��� ���������, ������� � ��� ����."
    )
    variant = int(input("��� ��������? \n 1. ����� �� ��������� \n 2. ����� �� ���� \n 3. �������� ������ \n"))
    if variant == 1:
        print('�� ������� ����� �� ���������')
    elif variant == 2:
        print('�� ������� ����� �� ����')
    elif variant == 3:
        print('�� ������� ���������� �������')
        addsql()
    else:
        print("�������� �������� �� �����, ���������� ��� ���.")


# ���������� � sql
def addsql():
    main.cur.execute("""INSERT INTO repices(name, item, repices) 
       VALUES(name_repices, item_repices, repices_repices);""")
    main.conn.commit()
