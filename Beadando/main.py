import Ping_LDC
import tkinter as tk

app = Ping_LDC.HalozatLDC()

def pingeles_LDC():
    cim = mezo.get().strip()
    if Ping_LDC.ures_LDC(cim):
        eredmeny.config(text="írj be egy címet", fg= "orange")
        return
    elerheto, ido = app.ping_LDC(cim, 443)
    app.mentes_LDC(cim, elerheto, ido)
    szoveg = f"{cim}: elérhető: {elerheto}, válaszidő: {ido} ms"
    if elerheto:
        eredmeny.config(text=f"{cim}: elérhető, válaszidő: {ido} ms", fg="green")
    else:
        eredmeny.config(text=f"{cim}: nem elérhető", fg="red")


def listazas_LDC():
    sorok = app.lista_LDC()
    szoveg = ""
    for sor in sorok:
        szoveg += Ping_LDC.sor_szoveg_LDC(sor)
    lista.config(text=szoveg)


def torles_LDC():
    mezo.delete(0, tk.END)
    eredmeny.config(text="")
    lista.config(text="")


root = tk.Tk()
root.title("PingFigyelő")
root.config(padx=10, pady=10)

tk.Label(root, text="Cím:").grid(row=0, column=0, padx=5, pady=5)
mezo = tk.Entry(root, width=30)
mezo.grid(row=0, column=1, padx=5, pady=5)

gomb = tk.Button(root, text="Ping", command=pingeles_LDC)
gomb.grid(row=0, column=2, padx=5, pady=5)


eredmeny = tk.Label(root, text="")
eredmeny.grid(row=1, column=0, columnspan=5, sticky="w")

lista_gomb = tk.Button(root, text="Lista", command=listazas_LDC)
lista_gomb.grid(row=0, column=3, padx=5, pady=5)

lista = tk.Label(root, text="", justify="left", font=("Courier", 10))
lista.grid(row=2, column=0, columnspan=5, sticky="w")

torles_gomb = tk.Button(root, text="Törlés", command=torles_LDC)
torles_gomb.grid(row=0, column=4, padx=5, pady=5)


root.mainloop()
