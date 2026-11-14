import sqlite3
import os
from datetime import datetime

ADATBAZIS = os.path.join(os.path.dirname(__file__), "monitor.db")

def mentes(terheles, lemez, memoria):

    idopont = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    kapcsolat = sqlite3.connect(ADATBAZIS)
    kapcsolat.execute("""
        CREATE TABLE IF NOT EXISTS meresek (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            idopont TEXT,
            terheles REAL,
            lemez REAL,
            memoria REAL
        )
    """)
    kapcsolat.execute("INSERT INTO meresek(idopont,terheles,lemez,memoria) VALUES(?,?,?,?)", (idopont, terheles, lemez, memoria,))
    kapcsolat.commit()
    kapcsolat.close()

def lekerdezes():
    kapcsolat = sqlite3.connect(ADATBAZIS)
    eredmeny = kapcsolat.execute("SELECT * FROM meresek where lemez IS NOT NULL")
    sorok = eredmeny.fetchall()
    kapcsolat.close()
    return sorok

def ping_mentes(cim, elerheto, valaszido):

    idopont = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    kapcsolat = sqlite3.connect(ADATBAZIS)
    kapcsolat.execute("""
        CREATE TABLE IF NOT EXISTS ellenorzesek (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            idopont TEXT,
            cim TEXT,
            elerheto INTEGER,
            valaszido REAL
        )
    """)
    kapcsolat.execute("INSERT INTO ellenorzesek(idopont,cim,elerheto,valaszido) VALUES(?,?,?,?)", (idopont, cim, elerheto, valaszido,))
    kapcsolat.commit()
    kapcsolat.close()

def ping_lekerdezes():
    kapcsolat = sqlite3.connect(ADATBAZIS)
    eredmeny = kapcsolat.execute("SELECT * FROM ellenorzesek")
    sorok = eredmeny.fetchall()
    kapcsolat.close()
    return sorok