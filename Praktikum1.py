import tkinter as tk 
import sqlite3
from tkinter import ttk
from tkinter import messagebox

conn = sqlite3.connect('data_siswa1.db')
cursor = conn.cursor()

# Membuat table jika belum ada
cursor.execute('''
    CREATE TABLE IF NOT EXISTS nilai_siswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_siswa TEXT,
        biologi INTEGER,
        fisika INTEGER,
        inggris INTEGER,
        prediksi_fakultas TEXT
    )
''')
conn.commit()

def submit_nilai():
    nama_siswa = Nama.get()
    nilai_biologi = int(Bio.get())
    nilai_fisika = int(Fis.get())
    nilai_inggris = int(Bing.get())

    # Menentukan prediksi fakultas
    prediksi = ""
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi = "Teknik"
    elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
        prediksi = "Bahasa"
        
   # Memasukkan data ke SQLite
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi))
    conn.commit()
    def klikButton():
        PrediksiFakultas = Pred
    messagebox.showinfo("Prediksi Fakultas", "Kamu masuk fakultas" + prediksi)

uiApp = tk.Tk()
uiApp.configure(background='black')             #Mengatur warna background
uiApp.geometry("800x800")                       #Besar ukuran
uiApp.resizable(False,False)                    #disable pengubahan ukuran
uiApp.title("Prediksi Fakultas")                 #Memberi judul

inputFrame = tk.Frame(uiApp)                          #Make canvas
inputFrame.pack(padx=10, pady=10, fill="x", expand=True)      #Make canvas

inputLabel = ttk.Label(inputFrame, text="Prediksi Fakultas")            #Make Label
inputLabel.pack(padx=10, pady=10, fill="x",expand=True)     #Make Label

#1
Nama = ttk.Label(inputFrame, text="Nama : ")
Nama.pack(padx=10, pady=5, fill="x", expand=True)
Nama = ttk.Entry(inputFrame)
Nama.pack(padx=10, pady=5, fill="x", expand=True)

#2
Bio = ttk.Label(inputFrame, text="Biologi : ")
Bio.pack(padx=10, pady=5, fill="x", expand=True)
Bio = ttk.Entry(inputFrame)
Bio.pack(padx=10, pady=5, fill="x", expand=True)

#3
Fis = ttk.Label(inputFrame, text="Fisika : ")
Fis.pack(padx=10, pady=5, fill="x", expand=True)
Fis = ttk.Entry(inputFrame)
Fis.pack(padx=10, pady=5, fill="x", expand=True)

#4
Bing = ttk.Label(inputFrame, text="Binggris : ")
Bing.pack(padx=10, pady=5, fill="x", expand=True)
Bing = ttk.Entry(inputFrame)
Bing.pack(padx=10, pady=5, fill="x", expand=True)

buttonSubmit = ttk.Button (inputFrame, text="Prediksi Fakultas ", command= submit_nilai)
buttonSubmit.pack(padx=10, pady=10, fill="x", expand=True)

uiApp.mainloop()  

conn.close()