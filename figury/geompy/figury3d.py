"""Moduł zawierający klasy umożliwiające obliczenie objętości oraz pola powierzchni całkowitej dla: 
1. sześcianu 
2. prostopadłościanu 
3. kuli """

from geompy.figury2d import Kwadrat, Prostokat, Kolo

class Prostopadloscian(Prostokat):
    """Klasa child z funkcjami do obliczania pola i objetości prostopadłoscianu"""
    def __init__(self, bok_a, bok_b, wysokosc_h):
        super().__init__(bok_a, bok_b)
        self.wysokosc_h = wysokosc_h

    def pole_calkowite(self):
        """Oblicza pole powierzchni całkowitej prostopadłoscianu"""
        return 2 * (self.bok_a * self.bok_b + self.bok_b * self.wysokosc_h + self.bok_a * self.wysokosc_h)
    
    def objetosc(self):
        """Oblicza objętość prostopadłoscianu"""
        return self.bok_a * self.bok_b * self.wysokosc_h
    
class Szescian(Kwadrat):
    """Klasa child z funkcjami do obliczania pola i objetości sześcianu"""
    def __init__(self, bok_a):
        super().__init__(bok_a)
        self.wysokosc_h = bok_a

    def pole_calkowite(self):
        """Oblicza pole powierzchni całkowitej sześcianu"""
        return 6 * super().pole()
    
    def objetosc(self):
        """Oblicza objętość sześcianu"""
        return self.bok_a ** 3
    

class Kula(Kolo):
    """Klasa child z funkcjami do obliczania pola i objetości Kuli"""
    def __init__(self, promien):
        super().__init__(promien)

    def pole_calkowite(self):
        """Oblicza pole powierzchni całkowitej Kuli"""
        return 4 * Kula.pi * self.promien ** 2
    
    def objetosc(self):
        """Oblicza objętość Kuli"""
        return (4/3) * Kula.pi * self.promien ** 3