import socket
import time

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

