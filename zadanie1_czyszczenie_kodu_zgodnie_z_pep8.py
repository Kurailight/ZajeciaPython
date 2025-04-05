"""System do zarządzania biblioteką"""


class Ksiazka:
    """Reprezentuje książkę w systemie bibliotecznym"""

    def __init__(self, tytul, autor, dostepna=True):
        self.tytul = tytul
        self.autor = autor
        self.dostepna = dostepna


class Biblioteka:
    """Zarządza zbiorem książek i operacjami wypożyczeń"""

    def __init__(self):
        self.lista_ksiazek = []

    def dodaj_ksiazke(self, ksiazka):
        """Dodaje nową książkę do biblioteki"""
        self.lista_ksiazek.append(ksiazka)

    def wypozycz_ksiazke(self, tytul):
        """Wypożycza książkę, jeśli jest dostępna"""
        for ksiazka in self.lista_ksiazek:
            if ksiazka.Tytul == tytul:
                if ksiazka.dostepna is True:
                    ksiazka.dostepna = False
                    return f"Wypozyczono: {tytul}"
                return f"Ksiazka {tytul} niedostepna"
        return f"Brak ksiazki: {tytul}"

    def zwroc_ksiazke(self, tytul):
        """Zwraca książkę do biblioteki"""
        for ksiazka in self.lista_ksiazek:
            if ksiazka.Tytul == tytul:
                ksiazka.dostepna = True
                return f"Zwrocono: {tytul}"
        return f"Nie nalezy do biblioteki: {tytul}"

    def dostepne_ksiazki(self):
        """Wyświetla listę dostępnych książek w bibliotece"""
        dostepne = []
        for ksiazka in self.lista_ksiazek:
            if ksiazka.dostepna:
                dostepne.append(ksiazka.Tytul)
        return dostepne


def main():
    """Main"""
    biblioteka = Biblioteka()
    biblioteka.dodaj_ksiazke(Ksiazka("Wiedzmin", "Sapkowski"))
    biblioteka.dodaj_ksiazke(Ksiazka("Solaris", "Lem"))
    biblioteka.dodaj_ksiazke(Ksiazka("Lalka", "Prus", False))

    print(biblioteka.wypozycz_ksiazke("Solaris"))
    print(biblioteka.wypozycz_ksiazke("Lalka"))
    print(biblioteka.zwroc_ksiazke("Lalka"))
    print("Dostepne ksiazki: ", biblioteka.dostepne_ksiazki())


main()
