

@author: Mathias Sandvik
"""
class Quiz():
    def __init__(self, spm, fv, svar):
        self.spørsmål = spm
        self.flervalg = fv
        self.svar = svar
        
    def __str__(self):
        return self.spørsmål + "\n" + "\n".join([" ".join([str(x+1), y]) for x, y in enumerate(self.flervalg)]) + "\n"
    
    def sjekk_svar(self, brukerSvar):
        return brukerSvar == self.svar
    
    def korrekt_svar_tekst(self):
        return self.flervalg[self.svar]
    
def les():
    with open("sporsmaalsfil.txt", encoding = "UTF-8") as fil:
        liste = []
        for i, e in enumerate(fil):
            e = e.split(":")
            globals()["spørsmål%s" % i] = Quiz(e[0], e[2].strip("[]\n ").split(", "), int(e[1]))
            liste.append(eval("spørsmål%s" % i))
        return liste
    


if __name__ == "__main__":
    liste = les()
    poeng1 = 0 
    poeng2 = 0
    for i in liste:
        print(i)
        svar1 = int(input("Hva svarer spiller nr1?: "))
        svar2 = int(input("Hva svarer spiller nr2?: "))

        print("Korrekt svar: " , i.korrekt_svar_tekst() )
        if svar1==i.svar+1:
            poeng1 = poeng1+1
        if svar2==i.svar+1:
            poeng2 = poeng2+1
        print ("Spiller 1: ", "Korrekt" if svar1 == i.svar+1 else "Feil")
        print ("Spiller 2: ", "Korrekt" if svar2 == i.svar+1 else "Feil")

print ("Spiller 1 fikk", poeng1, "riktige svar!")
print ("Spiller 2 fikk", poeng2, "riktige svar!")
