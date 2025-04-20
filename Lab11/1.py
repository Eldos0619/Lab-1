import psycopg2
import csv
from tabulate import tabulate

conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="eldo0619",
    port=5432
)

cur = conn.cursor()

def call_insert_or_update():
    name = input("Имя: ")
    surname = input("Фамилия: ")
    phone = input("Телефон: ")
    cur.execute("CALL insert_or_update_user(%s, %s, %s)", (name, surname, phone))
    conn.commit()
    print("✅ Готово.")

def call_insert_many_from_csv():
    filepath = input("Введите путь к CSV-файлу: ")
    users = []
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            users.append(row)
    cur.execute("CALL insert_many_users(%s)", (users,))
    conn.commit()
    print("✅ Пользователи добавлены.")

def search_by_pattern():
    pattern = input("Введите шаблон для поиска: ")
    cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

def paginated_output():
    lim = int(input("Сколько записей показать: "))
    off = int(input("Пропустить сколько записей: "))
    cur.execute("SELECT * FROM get_paginated_users(%s, %s)", (lim, off))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

def delete_by_identifier():
    ident = input("Введите имя или номер для удаления: ")
    cur.execute("CALL delete_user(%s)", (ident,))
    conn.commit()
    print("🗑️ Удалено.")

def show_all():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

# Главное меню
while True:
    print("""
    📞 PhoneBook Меню:
    1. Вставить/обновить одного пользователя
    2. Вставить список пользователей из CSV
    3. Найти по шаблону (имя, фамилия, номер)
    4. Показать данные с пагинацией
    5. Удалить по имени или номеру
    6. Показать все записи
    0. Выход
    """)
    choice = input("Выберите действие: ")

    if choice == "1":
        call_insert_or_update()
    elif choice == "2":
        call_insert_many_from_csv()
    elif choice == "3":
        search_by_pattern()
    elif choice == "4":
        paginated_output()
    elif choice == "5":
        delete_by_identifier()
    elif choice == "6":
        show_all()
    elif choice == "0":
        break
    else:
        print("⛔ Неверный выбор.")

cur.close()
conn.close()
