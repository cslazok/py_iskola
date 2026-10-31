import urllib.request
import tkinter as tk

def pingeles():
    cim = mezo.get()
    valasz = urllib.request.urlopen(f"http://localhost:8000/ping?cim={cim}")
    szoveg = valasz.read().decode("utf-8")
    eredmeny.config(text=szoveg)

ablak = tk.Tk()
ablak.title("Hálózatfigyelő")

tk.Label(ablak, text="Cím:").grid(row=0, column=0)
mezo = tk.Entry(ablak)
mezo.grid(row=0, column=1)

gomb = tk.Button(ablak, text="Ping", command=pingeles)
gomb.grid(row=0, column=2)

eredmeny = tk.Label(ablak, text="")
eredmeny.grid(row=1, column=0, columnspan=3)

ablak.mainloop()
