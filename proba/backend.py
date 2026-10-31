from http.server import HTTPServer, BaseHTTPRequestHandler
import meres
import adatbazis
import ping
from urllib.parse import urlparse, parse_qs


class Kezelo(BaseHTTPRequestHandler):

    def do_GET(self):
        reszek = urlparse(self.path)
        utvonal = reszek.path
        adatok = parse_qs(reszek.query)

        if utvonal == "/":
            valasz = "Ez a backend"
        elif utvonal == "/meres":
            terheles = meres.terheles_merese()
            lemez = meres.lemez_merese()
            memoria = meres.mem_merese()
            adatbazis.mentes(terheles, lemez, memoria)
            valasz = f"Terhelés: {terheles}% | Lemez: {lemez}% | Memória: {memoria}% (elmentve)" 
        elif utvonal == "/meresek":
            sorok = adatbazis.lekerdezes()
            valasz = ""
            for sor in sorok:
                valasz += f"{sor[1]} | terhelés: {sor[2]}% | lemez: {sor[3]}% | memória: {sor[4]}%\n"
        elif utvonal == "/ping":
            if "cim" in adatok:
                cim = adatok["cim"][0] 
                elerheto, ido = ping.ping(cim, 443)
                adatbazis.ping_mentes(cim, elerheto,ido)
                valasz = f"{cim}: elérhető: {elerheto}, válaszidő: {ido} ms (elmentve)"
            else:
                valasz = "Adj meg egy címet!"        
        elif utvonal == "/pingek":
            sorok = adatbazis.ping_lekerdezes()
            valasz = ""
            for sor in sorok:
                valasz += f"{sor[1]} | {sor[2]} | elérhető: {sor[3]} | {sor[4]} ms\n"
        else:
            valasz = "Nincs ilyen oldal."

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(valasz.encode("utf-8"))


szerver = HTTPServer(("localhost", 8000), Kezelo)
print("A backend fut: http://localhost:8000")
szerver.serve_forever()
