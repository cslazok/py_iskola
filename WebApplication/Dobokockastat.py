import tkinter as tk
from tkinter import ttk
import random

def dobas():
    try:
        dobasok_szama = int(dobas_szam.get())
        if dobasok_szama <= 0:
            raise ValueError("A dobások számának pozitív egész számnak kell lennie.")
    except ValueError as e:
        dobas_eredmeny_cimke.config(text=f"Hiba: {e}")
        return

    eredmenyek = [0] * 6
    for _ in range(dobasok_szama):
        eredmeny = random.randint(1, 6)
        eredmenyek[eredmeny - 1] += 1

    for i in range(6):
        darab_cimkek[i].config(text=str(eredmenyek[i]))
    osszesen_cimke.config(text=str(dobasok_szama))
    dobas_eredmeny_cimke.config(text="")


root = tk.Tk()
root.title("Dobókocka statisztika")
root.geometry("800x800")
root.resizable(False, False)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

cim_cimke = ttk.Label(root, text ="Dobókocka statisztika", font=("Arial", 24))
cim_cimke.grid(row=0, column=0, columnspan=2, pady=20)
keszito_cimke = ttk.Label(root, text ="Készítette: Daniel", font=("Arial", 12))
keszito_cimke.grid(row=1, column=0, columnspan=2, pady=10)


dobas_szam = tk.StringVar(value="100")
dobas_szam_beallitas = ttk.Entry(root, textvariable=dobas_szam, width=20)
dobas_szam_beallitas.grid(row=2, column=0, columnspan=2, pady=10)


dobas_gomb = ttk.Button(root, text="Dobás", width=10, command=dobas)
dobas_gomb.grid(row=3, column=0, pady=20)

kilepes_gomb = ttk.Button(root, text="Kilépés", width=10, command=root.destroy)
kilepes_gomb.grid(row=3, column=1, pady=20)

dobas_eredmeny_cimke = ttk.Label(root, text="", font=("Arial", 12))
dobas_eredmeny_cimke.grid(row=4, column=0, columnspan=2, pady=10)

racs = ttk.Frame(root)
racs.grid(row=5, column=0, columnspan=2, pady=10)

ttk.Label(racs, text="Szám", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=20, pady=5)
ttk.Label(racs, text="Darab", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=20, pady=5)
ttk.Label(racs, text="Összesen", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=20, pady=5)

darab_cimkek = []
for i in range(6):
    ttk.Label(racs, text=str(i + 1), font=("Arial", 12)).grid(row=i + 1, column=0, padx=20, pady=5)
    cimke = ttk.Label(racs, text="-", font=("Arial", 12))
    cimke.grid(row=i + 1, column=1, padx=20, pady=5)
    darab_cimkek.append(cimke)

osszesen_cimke = ttk.Label(racs, text="-", font=("Arial", 20, "bold"))
osszesen_cimke.grid(row=1, column=2, rowspan=6, padx=20)


root.mainloop()