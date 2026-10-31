import socket
import time
import adatbazis
def ping(cim, port):
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
cim = "google.com"
elerheto, ido = ping(cim, 443)
print(f"{cim}: {elerheto}, {ido} ms")
adatbazis.ping_mentes(cim=cim,elerheto=elerheto,valaszido=ido)
