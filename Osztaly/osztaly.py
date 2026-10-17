

class Teglalap:
    szog = 90
    def __init__(self, szelesseg:int=5, magassag:int=10):
        self.szelesseg = szelesseg
        self.magassag = magassag

    def terulet(self):
        return self.szelesseg * self.magassag
    
    def kerulet(self):
        return 2 * (self.szelesseg + self.magassag)    

class Negyzet(Teglalap):
    def __init__(self, oldal1:int, oldal2:int=0):
        super().__init__(oldal1, oldal2)
        self.oldal1 = oldal1
        self.oldal2 = oldal1



t1 = Teglalap()
print(t1.szelesseg, t1.magassag)
print(t1.szog)
t2 = Teglalap(20, 30)
print(t2.szelesseg, t2.magassag)
print(t2.szog)
print (t1.terulet())
print (t1.kerulet())
print (t2.terulet())
print (t2.kerulet())

n1= Negyzet(5)
print(n1.terulet())
print(n1.kerulet())
print(n1.szog)
