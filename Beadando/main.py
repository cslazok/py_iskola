import Ping_LDC
import tkinter as tk

halozat = Ping_LDC.HalozatLDC()

def pingeles_LDC():
    cim = mezo.get()
    if cim == "":
        eredmeny.config(text="írj be egy címet", fg= "orange")
        return
    elerheto, ido = halozat.ping_LDC(cim, 443)
    halozat.mentes_LDC(cim, elerheto, ido)
    szoveg = f"{cim}: elérhető: {elerheto}, válaszidő: {ido} ms"
    if elerheto:
        eredmeny.config(text=szoveg, fg="green")
    else:
        eredmeny.config(text=szoveg, fg="red")

def listazas_LDC():
    sorok = halozat.lista_LDC()
    szoveg = ""
    for sor in sorok:
        szoveg += f"{sor[1]} | {sor[2]} | elérhető: {sor[3]} | {sor[4]} ms\n"
    lista.config(text=szoveg)


def torles_LDC():
    mezo.delete(0, tk.END)
    eredmeny.config(text="")
    lista.config(text="")


ablak = tk.Tk()
ablak.title("Hálózatfigyelő")
ablak.config(padx=10, pady=10)

tk.Label(ablak, text="Cím:").grid(row=0, column=0, padx=5, pady=5)
mezo = tk.Entry(ablak, width=30)
mezo.grid(row=0, column=1, padx=5, pady=5)

gomb = tk.Button(ablak, text="Ping", command=pingeles_LDC)
gomb.grid(row=0, column=2, padx=5, pady=5)


eredmeny = tk.Label(ablak, text="")
eredmeny.grid(row=1, column=0, columnspan=5, sticky="w")

lista_gomb = tk.Button(ablak, text="Lista", command=listazas_LDC)
lista_gomb.grid(row=0, column=3, padx=5, pady=5)

lista = tk.Label(ablak, text="", justify="left", font=("Courier", 10))
lista.grid(row=2, column=0, columnspan=5, sticky="w")

torles_gomb = tk.Button(ablak, text="Törlés", command=torles_LDC)
torles_gomb.grid(row=0, column=4, padx=5, pady=5)


ablak.mainloop()
