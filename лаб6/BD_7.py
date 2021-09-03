# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 12:22:06 2021

@author: DashaEfimova
"""

import pyodbc
import tkinter as tk
import tkinter.ttk as ttk

# Установление соединения с базой данной
conn = pyodbc.connect(driver = '{SQL Server}',server = '192.168.112.103' , database = 'db22205', user = 'User052', password = 'User052>#26')

cursor = conn.cursor()
root = tk.Tk()   
table1 = ttk.Treeview(root, show="headings", selectmode="browse")


def main():
    root.title("Доктора")
    root.geometry("700x400")
    lbox = tk.Label(height = 5, pady = 5)
    text1 = tk.Label(text = "Информация о докторах:", justify = tk.RIGHT, padx = 2, pady = 5, font=("Comic Sans MS", 16))
    
    lbox.pack(side=tk.TOP)
    text1.place(relx = 0.03, rely = 0.1)
    
    fr = tk.Frame()
    fr2 = tk.Frame()
    fr.pack(side=tk.LEFT, padx=10)
    fr2.pack(side=tk.RIGHT, padx=10)
    
    textBotton = tk.Label(pady = 20).place(relx = 0.85, rely = 0.1)
    tk.Button(textBotton, text="Добавить доктора", font=("Comic Sans MS", 12), border="4").place(relx = 0.73, rely = 0.1)    
    
    # Заполнение списка деталей из базы данных
    # выполнение команды SQL
    cursor.execute("Select txtDoctorName, txtSpecialist, datDoctorWork from tblDoctor")
    row = cursor.fetchone()   # получение данных записи

    headings=('ФИО доктора', 'Специальность', 'Дата приема на работу')
    
    table1["columns"] = headings
    table1["displaycolumns"] = headings
    
    for head in headings:
        table1.heading(head, text=head, anchor=tk.CENTER)
        table1.column(head, anchor=tk.CENTER)
        
    # for row in rows:
    #     table1.insert('', tk.END, values=tuple(row))
    
        
    scrolltable = tk.Scrollbar(command=table1.yview)
    table1.configure(yscrollcommand=scrolltable.set)
    scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
    table1.pack(expand=tk.YES, fill=tk.X)
    
    while row: 
        table1.insert('', 'end', values=(row[0], row[1], row[2]))
        row = cursor.fetchone()   # получение данных одной записи

    # Передача управления пользователю
    root.mainloop()
    
    # Закрытие курсора и соединения с базой данной
    cursor.close()
    conn.close()

if __name__=="__main__":
    main()