import shutil

def lemez():
    adat = shutil.disk_usage("/")
    foglalt = adat.used
    osszes = adat.total
    szazalek = foglalt / osszes * 100
    szazalek = round(szazalek,1)
    return szazalek

print(f"A lemez foglaltsága:{lemez()} %")