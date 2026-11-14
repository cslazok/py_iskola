from urllib.parse import urlparse, parse_qs

cim = "/ping?cim=index.hu"

reszek = urlparse(cim)
print("útvonal:", reszek.path)
print("adatok:", reszek.query)

adatok = parse_qs(reszek.query)
print("szótár:", adatok)
print("a cím:", adatok["cim"][0])
