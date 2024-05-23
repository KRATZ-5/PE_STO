import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('company.db')

# Создаем курсор
cursor = conn.cursor()
try:
    # Создаем таблицу employees
    cursor.execute('''
    CREATE TABLE employees(
        employee_id INTEGER PRIMARY KEY,
        login TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        access_rights TEXT NOT NULL
    )
    ''')

    # Создаем таблицу cars
    cursor.execute('''
    CREATE TABLE cars(
        car_id INTEGER PRIMARY KEY,
        car_name TEXT NOT NULL,
        employee_id INTEGER,
        repair_status TEXT NOT NULL,
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    )
    ''')

    # Сохраняем изменения
    conn.commit()


except:
    print('База уже существует')
try:
    cursor.execute("INSERT INTO employees (login,email, password, access_rights) VALUES ('Viktor','Viktor@12345', '12345', 'Механик')")
    cursor.execute("INSERT INTO employees (login,email, password, access_rights) VALUES ('Viktor-Vektor','Viktor-Vektor@Q12345Q','Q12345Q', 'Старший механик')")
    cursor.execute("INSERT INTO employees (login,email, password, access_rights) VALUES ('321','321@Q123','321', 'Механик')")
    cursor.execute("INSERT INTO employees (login,email, password, access_rights) VALUES ('123','123@Q123','123', 'Старший механик')")
    cursor.execute("INSERT INTO employees (login,email, password, access_rights) VALUES ('1234','123@Q123','1234', 'Директор')")
    cursor.execute("INSERT INTO cars (car_name,employee_id, repair_status) VALUES ('BMW M3',3, 'В починке')")
    cursor.execute("INSERT INTO cars (car_name,employee_id, repair_status) VALUES ('AUDI Q7',3, 'В починке')")
    cursor.execute("INSERT INTO cars (car_name,employee_id, repair_status) VALUES ('AUDI Q7',3, 'В починке')")
    cursor.execute("INSERT INTO cars (car_name,employee_id, repair_status) VALUES ('AUDI Q5',3, 'В починке')")
    cursor.execute("INSERT INTO cars (car_name,employee_id, repair_status) VALUES ('AUDI Q3',3, 'В починке')")
except:
    print('База уже существует')
conn.commit()
# Закрываем подключение
conn.close()