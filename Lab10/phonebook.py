import psycopg2
import pandas as pd

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="eldo0619",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


# Создание таблицы
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    """)
    conn.commit()
    print("✅ Таблица создана.")


# Вставка данных через консоль
def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s);", (name, phone))
    conn.commit()
    print("✅ Контакт добавлен.")


# Вставка данных из CSV-файла
def insert_from_csv(file_path):
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s);", (row['name'], row['phone']))
    conn.commit()
    print("✅ Данные из CSV загружены.")


# Обновление данных
def update_contact(name, new_phone=None, new_name=None):
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s;", (new_phone, name))
    if new_name:
        cur.execute("UPDATE phonebook SET name = %s WHERE name = %s;", (new_name, name))
    conn.commit()
    print("✅ Контакт обновлён.")


# Запрос данных с фильтрами
def query_contacts(keyword):
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s;",
                (f"%{keyword}%", f"%{keyword}%"))
    rows = cur.fetchall()
    print("🔍 Результаты поиска:")
    for row in rows:
        print(row)


# Удаление по имени или телефону
def delete_contact(identifier):
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s;", (identifier, identifier))
    conn.commit()
    print("🗑️ Контакт удалён.")


# Пример меню
def main():
    create_table()
    while True:
        print("\n1. Добавить контакт (вручную)")
        print("2. Загрузить контакты из CSV")
        print("3. Обновить контакт")
        print("4. Найти контакты")
        print("5. Удалить контакт")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            path = input("Укажите путь к CSV-файлу: ")
            insert_from_csv(path)
        elif choice == "3":
            name = input("Имя для обновления: ")
            new_name = input("Новое имя (если не нужно — нажми Enter): ")
            new_phone = input("Новый телефон (если не нужно — нажми Enter): ")
            update_contact(name, new_phone or None, new_name or None)
        elif choice == "4":
            keyword = input("Введите имя или номер: ")
            query_contacts(keyword)
        elif choice == "5":
            ident = input("Введите имя или номер для удаления: ")
            delete_contact(ident)
        elif choice == "0":
            break
        else:
            print("⛔ Неверный выбор")


if __name__ == "__main__":
    main()
    cur.close()
    conn.close()