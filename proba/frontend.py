import urllib.request
import tkinter as tk

def pingeles():
    cim = mezo.get()
    try:
        valasz = urllib.request.urlopen(f"http://localhost:8000/ping?cim={cim}")
        szoveg = valasz.read().decode("utf-8")
        eredmeny.config(text=szoveg)
    except OSError:
        eredmeny.config(text= "A backend nem fut!")

def listazas():
    try:
        valasz = urllib.request.urlopen("http://localhost:8000/pingek")
        szoveg = valasz.read().decode("utf-8")
        lista.config(text=szoveg)
    except OSError:
        lista.config(text="A backend nem fut!")

ablak = tk.Tk()
ablak.title("Hálózatfigyelő")
ablak.config(padx=10, pady=10)

tk.Label(ablak, text="Cím:").grid(row=0, column=0, padx=5, pady=5)
mezo = tk.Entry(ablak, width=30)
mezo.grid(row=0, column=1, padx=5, pady=5)

gomb = tk.Button(ablak, text="Ping", command=pingeles)
gomb.grid(row=0, column=2, padx=5, pady=5)


eredmeny = tk.Label(ablak, text="")
eredmeny.grid(row=1, column=0, columnspan=4, sticky="w")

lista_gomb = tk.Button(ablak, text="Lista", command=listazas)
lista_gomb.grid(row=0, column=3, padx=5, pady=5)

lista = tk.Label(ablak, text="", justify="left", font=("Courier", 10))
lista.grid(row=2, column=0, columnspan=4, sticky="w")


ablak.mainloop()
