class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}"
    

class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        super().__init__(imie, nazwisko, wiek)
        self.stanowisko = stanowisko
        self.pensja = pensja

    def info_o_pracy(self):
        return f"Pracuję jako {self.stanowisko}, zarabiam {self.pensja} zł."

class Manager(Pracownik):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja, zespol):
        super().__init__(imie, nazwisko, wiek, stanowisko, pensja)
        self.zespol = zespol
    
    def przedstaw_sie(self):
        return f"Liczba podwładnych: {len(self.zespol)}"
    
    def dodaj_do_zespolu(self, pracownik):
        self.zespol.append(pracownik)



manager1= Manager("Anna", "Kowalska", 40, "Team Leader", 18000.58, [])
pracownik1= Pracownik("Paweł", "Noga", 24, "Programista", 6500)
pracownik2= Pracownik("Grażyna", "Kwiat", 34, "Analityczka Danych", 8900)
manager1.dodaj_do_zespolu(pracownik1)
manager1.dodaj_do_zespolu(pracownik2)
print(manager1.przedstaw_sie())
print(pracownik1.info_o_pracy())

