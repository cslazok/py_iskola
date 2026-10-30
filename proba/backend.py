from http.server import HTTPServer, BaseHTTPRequestHandler
import meres
import adatbazis

class Kezelo(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            valasz = "Ez a backend"
        elif self.path == "/meres":
            terheles = meres.terheles_merese()
            lemez = meres.lemez_merese()
            memoria = meres.mem_merese()

            adatbazis.mentes(terheles, lemez, memoria)

            valasz = f"Terhelés: {terheles}% | Lemez: {lemez}% | Memória: {memoria}% (elmentve)"

            valasz = f"Terhelés: {meres.terheles_merese()}% | Lemez:{meres.lemez_merese()}%| Memória:{meres.mem_merese()}%"    
        elif self.path == "/meresek":
            valasz = "Itt majd a mérések lesznek."
        else:
            valasz = "Nincs ilyen oldal."

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(valasz.encode("utf-8"))


szerver = HTTPServer(("localhost", 8000), Kezelo)
print("A backend fut: http://localhost:8000")
szerver.serve_forever()
