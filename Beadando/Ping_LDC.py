import socket
import time
import sqlite3
import os
from datetime import datetime


def idopont_LDC():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def ures_LDC(cim):
    return cim == ""

def sor_szoveg_LDC(sor):
    return f"{sor[1]} | {sor[2]} | elérhető: {sor[3]} | {sor[4]} ms\n"


class HalozatLDC:

    def __init__(self):
        self.adatbazis = os.path.join(os.path.dirname(__file__), "monitor.db")
        kapcsolat = sqlite3.connect(self.adatbazis)
        kapcsolat.execute("""
            CREATE TABLE IF NOT EXISTS ellenorzesek (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                idopont TEXT,
                cim TEXT,
                elerheto INTEGER,
                valaszido REAL
            )
        """)
        kapcsolat.commit()
        kapcsolat.close()

    def ping_LDC(self, cim, port):
        try:
            kezdes = time.time()
            kapcsolat = socket.create_connection((cim, port), timeout=2)
            vege = time.time()
            kapcsolat.close()
            valaszido = (vege - kezdes) * 1000
            valaszido = round(valaszido, 1)
            return True, valaszido
        except socket.error:
            return False, None

    def mentes_LDC(self, cim, elerheto, valaszido):
        idopont = idopont_LDC()
        kapcsolat = sqlite3.connect(self.adatbazis)
        kapcsolat.execute("INSERT INTO ellenorzesek(idopont,cim,elerheto,valaszido) VALUES(?,?,?,?)", (idopont, cim, elerheto, valaszido))
        kapcsolat.commit()
        kapcsolat.close()

    def lista_LDC(self):
        kapcsolat = sqlite3.connect(self.adatbazis)
        eredmeny = kapcsolat.execute("SELECT * FROM ellenorzesek")
        sorok = eredmeny.fetchall()
        kapcsolat.close()
        return sorok
