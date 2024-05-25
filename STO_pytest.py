import tkinter
from tkinter import *                                                                                                   #Библиотека для отрисовки графического интерфейса
from tkinter import ttk                                                                                                 #Библиотека для отрисовки графического интерфейса
import sqlite3                                                                                                          #Библиотека для взаимодействия с базой данных
import hashlib                                                                                                          #Библиотека для хэширования данных
import pytest
import os
def test_passes():
    assert 4 == 4

def test2_passes():
    assert 44 == 44


def check_db(name):                                                                                                     #Функция для создания базы данных
    global conn                                                                                                         #
    global cursor                                                                                                       #
    conn = sqlite3.connect(name)                                                                                        # Создаем курсор
    cursor = conn.cursor()                                                                                              #
    try:                                                                                                                #
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
        CREATE TABLE order_car(
            car_id INTEGER PRIMARY KEY,
            license_plate TEXT NOT NULL,
            car_name TEXT NOT NULL,
            employee_id INTEGER,
            telephone TEXT NOT NULL,
            repair_status TEXT NOT NULL,
            date_repair TEXT NOT NULL DEFAULT '25.05.2024',
            FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
            )
            ''')
        # Сохраняем изменения
        conn.commit()
    except:
        print('База уже существует')
        return 'База уже существует'
    if flag_debug==True or 1==1:
        try:
            cursor.execute(
                "INSERT INTO employees (login,email, password, access_rights) VALUES ('Viktor','Viktor@12345', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 'Механик')")
            cursor.execute(
                "INSERT INTO employees (login,email, password, access_rights) VALUES ('Viktor-Vektor','Viktor-Vektor@Q12345Q','3386e3a6c561effd3d46b9eb8159ba46596264497b2e035b80734103aa02c614', 'Старший механик')")
            cursor.execute(
                "INSERT INTO employees (login,email, password, access_rights) VALUES ('321','321@Q123','8d23cf6c86e834a7aa6eded54c26ce2bb2e74903538c61bdd5d2197997ab2f72', 'Механик')")
            cursor.execute(
                "INSERT INTO employees (login,email, password, access_rights) VALUES ('123','123@Q123','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'Старший механик')")
            cursor.execute(
                "INSERT INTO employees (login,email, password, access_rights) VALUES ('1234','123@Q123','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'Директор')")
            cursor.execute(
                "INSERT INTO order_car (car_name,license_plate,telephone,employee_id, repair_status) VALUES ('BMW M3','Р309КВ','74953825327',3, 'В починке')")
            cursor.execute(
                "INSERT INTO order_car (car_name,license_plate,telephone,employee_id, repair_status) VALUES ('AUDI Q7','Р347КВ','74959458261',3, 'В починке')")
            cursor.execute(
                "INSERT INTO order_car (car_name,license_plate,telephone,employee_id, repair_status) VALUES ('BMW M7','Р309КВ','74959048821',3, 'В починке')")
            cursor.execute(
                "INSERT INTO order_car (car_name,license_plate,telephone,employee_id, repair_status) VALUES ('BMW M5','Р304КВ','74957608582',3, 'В починке')")
            cursor.execute(
                "INSERT INTO order_car (car_name,license_plate,telephone,employee_id, repair_status) VALUES ('AUDI Q3','Р339КВ','74956540819',3, 'В починке')")
        except:
            print('Параметры уже введены')
    conn.commit()
def Quit():                                                                                                             # Функция для закрытия графического интерфейса
    global app                                                                                                          #
    app.destroy()                                                                                                       #

def enter(access_rights):                                                                                               # Функция для входа пользователя с логином паролем
    global login                                                                                                        #
    global password                                                                                                     #
    global enterr                                                                                                       #
    global reg                                                                                                          #
    global quitt                                                                                                        #
    global Acc_name                                                                                                     #
    login.grid_forget()                                                                                                 #
    password.grid_forget()                                                                                              #
    enterr.grid_forget()                                                                                                #
    reg.grid_forget()                                                                                                   #
    Acc_name = Label(text=str(login.get()) , font=("Arial Bold", 20), background='#3eb489')                             #
    Acc_name.grid(row=1, column=40, padx=50, pady=5)                                                                    #
    quitt = Button(text="Выйти из аккаунта", command=quit_from_acc, font=("Arial Bold", 10))                            #
    quitt.grid(row=2, column=40, padx=50, pady=5)                                                                       #
    if access_rights=='Механик':                                                                                        #
        worker_window()                                                                                                 #
    elif access_rights=='Старший механик':                                                                              #
        manager_window()                                                                                                #
    elif access_rights=='Директор':                                                                                     #
        admin_window()                                                                                                  #
    else:                                                                                                               #
        print('UNKNOWN',access_rights)                                                                                  #

def registr():                                                                                                          # Функция для регистрации пользователя
    global enterr                                                                                                       #
    global reg                                                                                                          #
    global regis                                                                                                        #
    global login                                                                                                        #
    global email                                                                                                        #
    global password                                                                                                     #
    global repassword                                                                                                   #
    enterr.grid_forget()                                                                                                #
    reg.grid_forget()                                                                                                   #
    email = Entry(width=28)                                                                                             #
    email.grid(row=1, column=0, padx=5, pady=5)                                                                         #
    email.insert(0, 'Введите почту')                                                                                    #
    email.bind('<FocusIn>', on_entry_click_email)                                                                       #
    email.bind('<FocusOut>', on_focusout_email)                                                                         #
    repassword = Entry(width=28)                                                                                        #
    repassword.grid(row=3, column=0, padx=5, pady=5)                                                                    #
    repassword.insert(0, 'Введите пароль')                                                                              #
    repassword.bind('<FocusIn>', on_entry_click_repassword)                                                             #
    repassword.bind('<FocusOut>', on_focusout_repassword)                                                               #
    regis = Button(text="Зарегистрироваться", command=reg_check, font=("Arial Bold", 10),width=20)                      #
    regis.grid(row=4, column=0, padx=5, pady=5)                                                                         #

def reg_check():                                                                                                        # Функция проверки правильности введения логина и пароля
    global login                                                                                                        #
    global password                                                                                                     #
    global repassword                                                                                                   #
    global email                                                                                                        #
    if password.get()==repassword.get():                                                                                #
        if  not login.get()==False and login.get()!='Введите логин':                                                    #
            if not password.get()==False and password.get()!='Введите пароль':                                          #
                add_new_user()                                                                                          #

def add_new_user():                                                                                                     # Функция для добавления новго пользователя в базу данных
    global login                                                                                                        #
    global email                                                                                                        #
    global password                                                                                                     #
    global repassword                                                                                                   #
    global quitt                                                                                                        #
    global Acc_name                                                                                                     #
    login.grid_forget()                                                                                                 #
    regis.grid_forget()                                                                                                 #
    email.grid_forget()                                                                                                 #
    password.grid_forget()                                                                                              #
    repassword.grid_forget()                                                                                            #
    cursor.execute("INSERT INTO employees (login,email, password, access_rights) "                                      #
                   "VALUES ('"+str(login.get())+"', '"+str(email.get())+"','"+str(password.get())+"', 'worker')")       #
    Acc_name = Label(text=str(login.get()), width=20, font=("Arial Bold", 20), background='#3eb489')                    #
    Acc_name.grid(row=0, column=40, padx=50, pady=5)                                                                    #
    quitt = Button(text="Выйти из аккаунта", command=quit_from_acc, font=("Arial Bold", 10))                            #
    quitt.grid(row=1, column=40, padx=50, pady=5)                                                                       #
    conn.commit()                                                                                                       #


def quit_from_acc():                                                                                                    #Функция выхода из аккаунта
    for widget in app.winfo_children():                                                                                 #
        widget.grid_forget()                                                                                            #
    start()                                                                                                             #

def enter_check():                                                                                                      # Функция проверки правильности введения логина и пароля
    global login                                                                                                        #
    global password                                                                                                     #
    global flag_debug                                                                                                   #
    global employee_id                                                                                                  #
    flag=0                                                                                                              #
    cursor.execute("SELECT login,password,access_rights,employee_id FROM employees WHERE login='"+str(login.get())+"'") # Получаем данные из таблицы employees
    employees = cursor.fetchall()                                                                                       #
    for employee in employees:                                                                                          #
        if flag_debug==True:                                                                                            #
            print(employee[0],employee[1])                                                                              #
        if employee[1]==hashlib.sha256(str(password.get()).encode()).hexdigest():                                       #
            flag = 1                                                                                                    #
            employee_id=employee[3]                                                                                     #
            enter(employee[2])                                                                                          #
            break                                                                                                       #
    if flag==0:                                                                                                         #
        print('Проверьте правильность введенного логина или пароля')                                                    #

def start():                                                                                                            # Функция начала программы
    global login                                                                                                        #
    global password                                                                                                     #
    global enterr                                                                                                       #
    global reg                                                                                                          #
    login = Entry(width=28)                                                                                             #
    login.grid(row = 0, column = 0, padx=5, pady=5)                                                                     #
    login.insert(0, 'Введите логин')                                                                                    #
    login.bind('<FocusIn>', on_entry_click_user_name)                                                                   #
    login.bind('<FocusOut>', on_focusout_user_name)                                                                     #
                                                                                                                        #
    password = Entry(width=28)                                                                                          #
    password.grid(row = 2, column = 0, padx=5, pady=5)                                                                  #
    password.insert(0, 'Введите пароль')                                                                                #
    password.bind('<FocusIn>', on_entry_click_password)                                                                 #
    password.bind('<FocusOut>', on_focusout_password)                                                                   #
                                                                                                                        #
                                                                                                                        #
    enterr = Button(text="Войти", command=enter_check,font=("Arial Bold", 10), width=20)                                #
    enterr.grid(row = 3, column = 0, padx=5, pady=5)                                                                    #
    reg = Button(text="Зарегистрироваться", command=registr,font=("Arial Bold", 10), width=20)                          #
    reg.grid(row = 4, column = 0, padx=5, pady=5)                                                                       #
    btn_exit = Button(app, text="Выход", font=("Arial Bold", 10), width=14, command=Quit,background='red')              # Создание кнопки закрытия приложения
    btn_exit.grid(row=3, column=40, padx=5, pady=5)                                                                     #


def on_entry_click_user_name(event):                                                                                    #
    if login.get() == 'Введите логин':                                                                                  #
        login.delete(0, "end")                                                                                          #
        login.insert(0, '')                                                                                             #
        login.config(fg = 'black')                                                                                      #
def on_entry_click_password(event):                                                                                     #
    if password.get() == 'Введите пароль':                                                                              #
        password.delete(0, "end")                                                                                       #
        password.insert(0, '')                                                                                          #
        password.config(fg = 'black')                                                                                   #
def on_entry_click_email(event):                                                                                        #
    if email.get() == 'Введите почту':                                                                                  #
        email.delete(0, "end")                                                                                          #
        email.insert(0, '')                                                                                             #
        email.config(fg = 'black')                                                                                      #
def on_entry_click_repassword(event):                                                                                   #
    if repassword.get() == 'Введите пароль':                                                                            #
        repassword.delete(0, "end")                                                                                     #
        repassword.insert(0, '')                                                                                        #
        repassword.config(fg = 'black')                                                                                 #
def on_focusout_user_name(event):                                                                                       #
    if login.get() == '':                                                                                               #
        login.insert(0, 'Введите логин')                                                                                #
        login.config(fg = 'black')                                                                                      #
def on_focusout_password(event):                                                                                        #
    if password.get() == '':                                                                                            #
        password.insert(0, 'Введите пароль')                                                                            #
        password.config(fg = 'black')                                                                                   #
def on_focusout_email(event):                                                                                           #
    if email.get() == '':                                                                                               #
        email.insert(0, 'Введите почту')                                                                                #
        email.config(fg = 'black')                                                                                      #
def on_focusout_repassword(event):                                                                                      #
    if repassword.get() == '':                                                                                          #
        repassword.insert(0, 'Введите пароль')                                                                          #
        repassword.config(fg = 'black')                                                                                 #

def confirm_worker():                                                                                                   # Функция сохраняющая изменеия в статусе ремонта автомобиля в базу данных
    for i in range(len(statusess)):                                                                                     #
        cursor.execute("UPDATE order_car SET repair_status = ? WHERE car_id = ? ",(str(statusess[i].get()),str(id_car[i])))#
        conn.commit()                                                                                                   #

def worker_window():                                                                                                    # Функция отображающие меню для пользователей с правами рабочих
    global statusess                                                                                                    #
    global id_car                                                                                                       #
    if flag_debug == True:                                                                                              #
        print('working worker')                                                                                         #
    cursor.execute("SELECT car_name,repair_status,car_id,license_plate FROM order_car WHERE employee_id='"+str(employee_id)+"'")           # Получаем данные из таблицы car
    cars = cursor.fetchall()                                                                                            #
    label_name_car = Label(text="Название машины", font=("Arial Bold", 15), width=18)                                   #
    label_name_car.grid(row=0, column=0, padx=5, pady=5)                                                                #
    label_name_car = Label(text="Гос номер", font=("Arial Bold", 15), width=12)                                         #
    label_name_car.grid(row=0, column=1, padx=5, pady=5)                                                                #
    label_repair_status = Label(text="Статус ремонта", font=("Arial Bold", 15))                                         #
    label_repair_status.grid(row=0, column=2, padx=5, pady=5)                                                           #
                                                                                                                        #
    statuses=[['Принята','В починке','Ремонт завершен']]*len(cars)                                                      #
    statusess=[]                                                                                                        #
    id_car = []                                                                                                         #
    for i in range(len(cars)):                                                                                          #
        if flag_debug==True:                                                                                            #
            print(cars[i][0],cars[i][1])                                                                                #
        label_name_car = Label(text=str(cars[i][0]), font=("Arial Bold", 14),width=18)                                  #
        label_name_car.grid(row=0+i+1, column=0, padx=5, pady=5)                                                        #
        label_license_plate = Label(text=str(cars[i][3]), font=("Arial Bold", 14), width=12)                            #
        label_license_plate.grid(row=0 + i + 1, column=1, padx=5, pady=5)                                               #
        id_car.append(cars[i][2])                                                                                       #
        status = StringVar(app)                                                                                         #
        status.set(cars[i][1])                                                                                          # устанавливаем по умолчанию первую опцию
        om = OptionMenu(app, status, *statuses[i])                                                                      #
        om.grid(row=0+i+1, column=2, padx=5, pady=5)                                                                    # Упаковка виджета на главное окно
        om.configure(width=18)
        statusess.append(status)                                                                                        # сохраняем переменную StringVar для последующего использования
    btn_save = Button(app, text="Сохранить изменения",font=("Arial Bold", 10),command=confirm_worker, width=20,background='green')# Создание кнопки закрытия приложения
    btn_save.grid(row=0+len(cars)+2, column=0, padx=5, pady=5)                                                          # Установка расположения кнопки


def confirm_manager():                                                                                                  # Функция сохраняющая изменеия в статусе ремонта автомобиля в базу данных
    global statusess                                                                                                    #
    global id_car                                                                                                       #
    global workerss                                                                                                     #
    for i in range(len(statusess)):                                                                                     #
        cursor.execute("UPDATE order_car SET repair_status = ? WHERE car_id = ? ", (str(statusess[i].get()), str(id_car[i])))#
        conn.commit()                                                                                                   #
    for i in range(len(workerss)):                                                                                      #
        cursor.execute("SELECT employee_id FROM employees WHERE login= '"+str(workerss[i].get())+"'")                   # Получаем данные из таблицы car
        worker_id = cursor.fetchall()                                                                                   #
        cursor.execute("UPDATE order_car SET employee_id = '"+str(*worker_id[0])+"' WHERE car_id = '"+str(id_car[i])+"'")#
        conn.commit()                                                                                                   #
    cursor.execute("DELETE FROM order_car WHERE repair_status= 'Заказ завершен'")                                       #
    cursor.execute("DELETE FROM order_car WHERE repair_status= 'Заказ отменён'")                                        #
    conn.commit()                                                                                                       #
    statusess = []                                                                                                      #
    id_car = []                                                                                                         #
    workerss = []                                                                                                       #
    refresh()                                                                                                           #
    refresh_manager()                                                                                                   #
def add_avto():                                                                                                                                                         #Функция добавляющая автомобиль в базу данных
    if entry_name_car.get()!='' and entry_license_plate.get()!='' and  len(str(entry_telephone.get()))==11  and len(str(entry_date.get()))==10:                         #
        try:                                                                                                                                                            #
            print(int(str(entry_date.get())[:2]),'q',int(str(entry_date.get())[3:5]),int(str(entry_date.get())[6:]),str(entry_date.get())[2],str(entry_date.get())[5])  #
            if int(str(entry_date.get())[:1])<=31 and int(str(entry_date.get())[2:5])<=12 and int(str(entry_date.get())[6:])>2000 :                                     #
                cursor.execute("SELECT employee_id FROM employees WHERE login= '"+str(workera.get())+"'")                                                               # Получаем данные из таблицы car
                worker_id = cursor.fetchall()                                                                                                                           #
                q="'"+str(entry_name_car.get())+"','"+str(entry_license_plate.get())+"','"+str(worker_id[0][0])                                                         #
                q+="','"+str(statusa.get())+"','"+str(entry_telephone.get())+"','"+str(entry_date.get())+"'"                                                            #
                cursor.execute("INSERT INTO order_car (car_name,license_plate, employee_id, repair_status,telephone,date_repair) VALUES ("+str(q)+")")                  #
                entry_name_car.delete(0, 'end')                                                                                                                         #
                entry_license_plate.delete(0, 'end')                                                                                                                    #
                entry_telephone.delete(0, 'end')                                                                                                                        #
                entry_date.delete(0, 'end')                                                                                                                             #
                conn.commit()                                                                                                                                           #
                s=statusa                                                                                                                                               #
                w=workera                                                                                                                                               #
                statusess.append(s)                                                                                                                                     #
                workerss.append(w)                                                                                                                                      #
                id_car.append(len(cars))                                                                                                                                #
                refresh_manager()                                                                                                                                       #
        except:
            1==1
def refresh_manager():                                                                                                  # Функция для обновления отображения базы данных автомобилей
    cursor.execute("SELECT login FROM employees WHERE access_rights='Механик'")                                         # Получаем данные из таблицы car
    workersss = cursor.fetchall()                                                                                       #
    workers=[]                                                                                                          #
    for i in range(len(workersss)):                                                                                     #
        workers.append(workersss[i][0])                                                                                 #
    cursor.execute("SELECT car_name,repair_status,car_id,employee_id,license_plate,telephone,date_repair FROM order_car")# Получаем данные из таблицы car
    cars = cursor.fetchall()                                                                                            #
    statuses=[['Принята','В починке','Ремонт завершен','Заказ завершен','Заказ отменён']]*len(cars)                     #                                                                                                                                                                                                                                                                                                          #
    if flag_debug==True:                                                                                                #
        print(cars)                                                                                                     #
                                                                                                                        #
    for i in range(len(cars)):                                                                                          #
        label_name_car = Label(text=str(cars[i][0]), font=("Arial Bold", 12),width=18)                                  #
        label_name_car.grid(row=0+i+2, column=0, padx=5, pady=5)                                                        #
        label_name_car = Label(text=str(cars[i][4]), font=("Arial Bold", 12), width=14)                                 #
        label_name_car.grid(row=0 + i + 2, column=1, padx=5, pady=5)                                                    #
        label_telephone = Label(text=str(cars[i][5]), font=("Arial Bold", 12), width=14)                                #
        label_telephone.grid(row=0 + i + 2, column=3, padx=5, pady=5)                                                   #
        label_date = Label(text=str(cars[i][6]), font=("Arial Bold", 12), width=14)                                     #
        label_date.grid(row=0 + i + 2, column=4, padx=5, pady=5)                                                        #
        id_car.append(cars[i][2])                                                                                       #
        status = StringVar(app)                                                                                         #
        status.set(cars[i][1])                                                                                          # устанавливаем по умолчанию первую опцию
        om = OptionMenu(app, status, *statuses[i])                                                                      #
        om.configure(width=18)                                                                                          #
        om.grid(row=0+i+2, column=2, padx=5, pady=5)                                                                    # Упаковка виджета на главное окно
        statusess.append(status)                                                                                        # сохраняем переменную StringVar для последующего использования
        cursor.execute("SELECT login FROM employees WHERE employee_id= '"+str(cars[i][3])+"'")                          # Получаем данные из таблицы car
        worker = StringVar(app)                                                                                         #
        work=cursor.fetchall()                                                                                          #
        worker.set(*work[0])                                                                                            # устанавливаем по умолчанию первую опцию
        om1 = OptionMenu(app, worker, *workers)                                                                         #
        om1.configure(width=32)                                                                                         #
        om1.grid(row=0 + i + 2, column=5, padx=5, pady=5)                                                               # Упаковка виджета на главное окно
        workerss.append(worker)                                                                                         # сохраняем переменную StringVar для последующего использования

def refresh():                                                                                                          # Функция для обновления отображения окна менеджера
    for widget in app.winfo_children():                                                                                 #
        widget.grid_forget()                                                                                            #
    manager_window()                                                                                                    #
    btn_exit = Button(app, text="Выход", font=("Arial Bold", 10), width=14, command=Quit,background='red')              # Создание кнопки закрытия приложения
    btn_exit.grid(row=3, column=40, padx=5, pady=5)                                                                     #
    Acc_name = Label(text=str(login.get()), font=("Arial Bold", 20), background='#3eb489')                              #
    Acc_name.grid(row=1, column=40, padx=50, pady=5)                                                                    #
    quitt = Button(text="Выйти из аккаунта", command=quit_from_acc, font=("Arial Bold", 10))                            #
    quitt.grid(row=2, column=40, padx=50, pady=5)                                                                       #


def manager_window():                                                                                                   #
    global statusess                                                                                                    #
    global id_car                                                                                                       #
    global workerss                                                                                                     #
    global worker                                                                                                       #
    global entry_name_car                                                                                               #
    global entry_license_plate                                                                                          #
    global entry_telephone                                                                                              #
    global entry_date                                                                                                   #
    global workera                                                                                                      #
    global statusa                                                                                                      #
    global cars                                                                                                         #
    if flag_debug == True:                                                                                              #
        print('manager worker')                                                                                         #
    cursor.execute("SELECT login FROM employees WHERE access_rights='Механик'")                                         # Получаем данные из таблицы car
    workersss = cursor.fetchall()                                                                                       #
    workers=[]                                                                                                          #
    for i in range(len(workersss)):                                                                                     #
        workers.append(workersss[i][0])                                                                                 #
    cursor.execute("SELECT car_name,repair_status,car_id,employee_id FROM order_car")                                   # Получаем данные из таблицы car
    cars = cursor.fetchall()                                                                                            #
    statuses=[['Принята','В починке','Ремонт завершен','Заказ завершен','Отменено']]*len(cars)                          #
    statusess=[]                                                                                                        #
    id_car = []                                                                                                         #
    workerss=[]                                                                                                         #
    refresh_manager()                                                                                                   #
    label_name_car = Label(text="Название машины", font=("Arial Bold", 15))                                             #
    label_name_car.grid(row=0, column=0, padx=5, pady=5)                                                                #
    label_license_plate = Label(text="Гос Номер", font=("Arial Bold", 15), width=12)                                    #
    label_license_plate.grid(row=0, column=1, padx=5, pady=5)                                                           #
    label_repair_status = Label(text="Статус ремонта", font=("Arial Bold", 15))                                         #
    label_repair_status.grid(row=0, column=2, padx=5, pady=5)                                                           #
    label_repair_status = Label(text="Телефон клиента", font=("Arial Bold", 15))                                        #
    label_repair_status.grid(row=0, column=3, padx=5, pady=5)                                                           #
    label_date = Label(text="Дата", font=("Arial Bold", 15), width=10)                                                  #
    label_date.grid(row=0, column=4, padx=5, pady=5)                                                                    #
    label_emp = Label(text="Прикрепленный сотрудник", font=("Arial Bold", 15))                                          #
    label_emp.grid(row=0, column=5, padx=5, pady=5)                                                                     #
    btn_save = Button(app, text="Добавить автомобиль", font=("Arial Bold", 10), command=add_avto,                       # Создание кнопки закрытия приложения
                      width=20, background='green')                                                                     #




    btn_save.grid(row=1, column=6, padx=5, pady=5)                                                                      # Установка расположения кнопки
    entry_name_car = Entry(text='Поле для ввода', font=("Arial Bold", 13), width=18)                                    #
    entry_name_car.grid(row=1, column=0, padx=5, pady=5)                                                                #
    entry_license_plate = Entry(text='Поле для вводаq', font=("Arial Bold", 13), width=15)                              #
    entry_license_plate.grid(row=1, column=1, padx=5, pady=5)                                                           #
    entry_telephone = Entry(text='Поле для вводаqq', font=("Arial Bold", 13), width=15)                                 #
    entry_telephone.grid(row=1, column=3, padx=5, pady=5)                                                               #
    entry_date = Entry(text='Поле для вводаqqq', font=("Arial Bold", 13), width=15)                                     #
    entry_date.grid(row=1, column=4, padx=5, pady=5)                                                                    #
    status = StringVar(app)                                                                                             #
    status.set('Принята')                                                                                               # устанавливаем по умолчанию первую опцию
    om = OptionMenu(app, status, *statuses[i])                                                                          #
    om.configure(width=18)                                                                                              #
    om.grid(row=1, column=2, padx=5, pady=5)                                                                            # Упаковка виджета на главное окно
    statusa=status                                                                                                      #
    worker = StringVar(app)                                                                                             #
    worker.set(workers[0])                                                                                              #
    om1 = OptionMenu(app, worker, *workers)                                                                             #
    om1.configure(width=32)                                                                                             #
    om1.grid(row=1, column=5, padx=5, pady=5)                                                                           # Упаковка виджета на главное окно
    workera=worker                                                                                                      #
    label_repair_status = Label( font=("Arial Bold", 15),width=20,background='#3eb489')                                 #
    label_repair_status.grid(row=0, column=6, padx=5, pady=5)                                                           #
    btn_save = Button(app, text="Сохранить изменения", font=("Arial Bold", 10), command=confirm_manager,                # Создание кнопки закрытия приложения
                      width=20,background='green')                                                                      #
    btn_save.grid(row=0 + len(cars) + 100, column=0, padx=5, pady=5)                                                    # Установка расположения кнопки
    btn_save = Button(app, text="Обновить", font=("Arial Bold", 10), command=refresh,                                   # Создание кнопки закрытия приложения
                      width=16,background='green')                                                                      #
    btn_save.grid(row=0 + len(cars) + 100, column=1, padx=5, pady=5)                                                    # Установка расположения кнопки


def confirm_admin():                                                                                                    #Функция сохраняющая изменеия в статусе ремонта автомобиля в базу данных
    for i in range(len(rightss)):                                                                                       #
        print(str(rightss[i].get()), str(worker[i][0]))                                                                 #
        cursor.execute("UPDATE employees SET access_rights = ? WHERE login = ? ",                                       #
                       (str(rightss[i].get()), str(worker[i][0])))                                                      #
        conn.commit()                                                                                                   #
def admin_window():                                                                                                     #Функция отображающие меню для пользователей с правами рабочих
    global rightss                                                                                                      #
    global worker                                                                                                       #
    if flag_debug == True:                                                                                              #
        print('admin worker')                                                                                           #
    cursor.execute("SELECT login,access_rights,email FROM employees")                                                   # Получаем данные из таблицы car
    worker = cursor.fetchall()                                                                                          #
    label_name_worker = Label(text="Логин сотрудник", font=("Arial Bold", 15))                                          #
    label_name_worker.grid(row=0, column=0, padx=5, pady=5)                                                             #
    label_email = Label(text="Почта сотрудника", font=("Arial Bold", 15))                                               #
    label_email.grid(row=0, column=1, padx=5, pady=5)                                                                   #
    label_repair_rights = Label(text="Права сотрудника", font=("Arial Bold", 15))                                       #
    label_repair_rights.grid(row=0, column=2, padx=5, pady=5)                                                           #
    rights=[['Механик','Старший механик','Директор']]*len(worker)                                                       #
    rightss=[]                                                                                                          #
    for i in range(len(worker)):                                                                                        #
        if flag_debug==True:                                                                                            #
            print(worker[i][0],worker[i][1])                                                                            #
        label_name_worker = Label(text=str(worker[i][0]), font=("Arial Bold", 10),width=21)                             #
        label_name_worker.grid(row=0+i+1, column=0, padx=5, pady=5)                                                     #
        label_name_worker = Label(text=str(worker[i][2]), font=("Arial Bold", 10), width=21)  #
        label_name_worker.grid(row=0 + i + 1, column=1, padx=5, pady=5)  #
        right = StringVar(app)                                                                                          #
        right.set(worker[i][1])                                                                                         # устанавливаем по умолчанию первую опцию
        om = OptionMenu(app, right, *rights[i])                                                                         #
        om.grid(row=0+i+1, column=2, padx=5, pady=5)                                                                    # Упаковка виджета на главное окно
        om.configure(width=21)                                                                                          #
        rightss.append(right)                                                                                           # сохраняем переменную StringVar для последующего использования
    btn_save = Button(app, text="Сохранить изменения",font=("Arial Bold", 10),command=confirm_admin, width=20,background='green')# Создание кнопки закрытия приложения
    btn_save.grid(row=0+len(worker)+2, column=0, padx=5, pady=5)                                                        # Установка расположения кнопки

global flag_debug                                                                                                       #Создание перенной флага для режима разработчика
flag_debug=False                                                                                                        #Установка значения флагу
check_db('company.db')                                                                                                  #Подключение и создание бд в случае отсутсвия

if os.name != "nt" and os.getenv("GITHUB_ACTIONS"):
    os.system('Xvfb :1 -screen 0 1600x1200x16  &')
    os.environ["DISPLAY"] = ":1.0"
else:
    app = Tk()                                                                                                          #Создание объекта класса tkinter
    app.title("СТО")                                                                                                    #Создание заголовка для графического интерфейса
    app.geometry('1600x800')                                                                                            #Установка размера окна графичекого интерфейса
    app.configure(background='#3eb489')                                                                                 #Установка цвета заднего фона графического интерфейса
    start()                                                                                                             # Запуск основной программы
    app.mainloop()                                                                                                      #Завершение и вызов графического интерфеса tkinter


