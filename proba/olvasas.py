import sqlite3

kapcsolat = sqlite3.connect("monitor.db")
eredmeny = kapcsolat.execute("SELECT * FROM meresek where lemez IS NOT NULL")
sorok = eredmeny.fetchall()
for sor in sorok:
    print(f"{sor[1]}| terhelés: {sor[2]}|lemez: {sor[3]}|memoria: {sor[4]}") 

eredmeny = kapcsolat.execute("Select COUNT(*), AVG(memoria), MAX(terheles) FROM meresek where lemez is not null")
stat = eredmeny.fetchone()
print(f"Mérések száma:{stat[0]}, Átlag:{stat[1]}, Max:{stat[2]}    ")
kapcsolat.close()