# Hálózatfigyelő

- Név: Lázok Dániel Csaba
- Neptun-kód: PBXQH9
- Tárgy: Szkript nyelvek
- Tagozat: levelező
- Labor azonosító: L01

## A feladat leírása

Egy egyszerű program, amivel meg lehet nézni, hogy egy gép vagy weboldal elérhető-e a hálózaton, és mennyi a válaszideje. Az eredményeket adatbázisba menti, és vissza lehet nézni őket.

## Használat

Nem kell semmit telepíteni, csak a Python beépített moduljait használja, ezért Windowson és Linuxon is működik.

Indítás:

    python main.py

A mezőbe kell beírni egy címet (pl. index.hu), utána:

- Ping: lepingeli a címet, és kiírja, hogy elérhető-e és mennyi a válaszidő (zöld, ha elérhető, piros, ha nem)
- Lista: megmutatja az eddigi pingeket az adatbázisból
- Törlés: kiüríti a mezőt és az ablakot

Ha üresen nyomod meg a Ping gombot, kiírja, hogy írj be egy címet.

## Felépítés

- main.py: innen indul a program, itt van az ablak
  - pingeles_LDC: lepingeli a beírt címet és elmenti
  - listazas_LDC: kiírja az eddigi pingeket
  - torles_LDC: kiüríti a mezőt és az ablakot
- Ping_LDC.py: saját modul
  - HalozatLDC osztály
    - ping_LDC: megnézi, elérhető-e a cím, és mennyi a válaszidő
    - mentes_LDC: elmenti az eredményt az adatbázisba
    - lista_LDC: visszaadja az elmentett pingeket
- Használt modulok: tkinter, socket, time, sqlite3, datetime, os


## Előzmények

A korábbi változatok a `Gyakorlas/Beadando_elozmenyek` mappában vannak. Először a gép terhelését, lemezét és memóriáját mértem, de az csak Linuxon működött, ezért váltottam a pingre. Utána egy két részből álló (backend és frontend) változat készült, amiből ez az egyszerűbb, egy programos változat lett.
