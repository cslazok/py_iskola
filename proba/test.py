import shutil
import os   

def terheles_merese():
    magok = os.cpu_count()
    terheles = os.getloadavg()[0]
    terheles_szazalek = terheles / magok  * 100
    terheles_szazalek = round(terheles_szazalek, 1)
    terheles_szazalek = min(terheles_szazalek, 100)
    return terheles_szazalek

def lemez_merese():
    lemez = shutil.disk_usage("/")
    foglalt = lemez.used
    osszes = lemez.total
    szazalek = foglalt / osszes * 100
    szazalek = round(szazalek,1)
    return szazalek

def mem_merese():
    with open ("/proc/meminfo") as f:
        for sor in f:
            if sor.startswith ("MemTotal"):
                darabok = sor.split()
                szam_szoveg = darabok[1]
                osszes_mem = int (szam_szoveg) 
            if sor.startswith ("MemAvailable"):
                darabok = sor.split()
                szam_szoveg = darabok[1]
                elerheto_mem = int (szam_szoveg) 
    foglalt_mem = osszes_mem -  elerheto_mem
    memoria_szazalek = foglalt_mem / osszes_mem * 100
    memoria_szazalek = round(memoria_szazalek, 1)
    return memoria_szazalek

print(f"A terhelés: {terheles_merese()}%")
print(f"A lemezhasználat: {lemez_merese()}%")
print(f"A memóriahasználat: {mem_merese()}%")