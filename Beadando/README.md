Egy egyszerű program, amivel meg lehet nézni, hogy egy gép vagy weboldal elérhető-e a hálózaton, és mennyi a válaszideje. Az eredményeket adatbázisba menti, és vissza lehet nézni őket. Python egyetemi beadandó feladathoz készült.

Így működik:

- backend.py: a szerver (localhost:8000), ez kapja a kéréseket, pingel, ment és válaszol
- frontend.py: az ablak (tkinter), itt lehet beírni a címet és megnézni az előzőleg lekért oldalak eredményét.
- ping.py: lepingeli a megadott címet és méri a válaszidőt
- adatbazis.py: ez menti és olvassa vissza az adatokat



Indítása:

1. python backend.py - ennek kell futnia először!
2. python frontend.py - külön terminálban kell futtatni

Ha a backend nem fut, az ablak kiírja, hogy "A backend nem fut!".

Mit használ?

Nem kell semmit telepíteni, csak a Python beépített moduljait használja, ezért Windowson és Linuxon is működik.

A gyakorlas mappa:

Meghajtó és cpu mérését és kiolvasását akartam eredeti beadandónak elkészíteni, de csak linuxon futott volna, ezért más témát kerestem, de mivel elkészítettem őket feltöltöm, nincs benne semmi olyan adat ami nem lehetne publikus.

Készítette: Lázok Dániel Csaba 