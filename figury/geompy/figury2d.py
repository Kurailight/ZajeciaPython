"""Moduł zawierający klasy umożliwiające obliczenie pola i obwodu dla: 
1. kwadratu 
2. prostokąta 
3. koła """


class Prostokat:
    """Klasa parent"""
    def __init__(self, bok_a, bok_b):
        self.bok_a = bok_a
        self.bok_b = bok_b
    
    def obwod(self):
        """Oblicza obwód prostokąta"""
        return 2 * self.bok_a + 2 * self.bok_b
    
    def pole(self):
        """Oblicza pole prostokąta"""
        return self.bok_a * self.bok_b
    
class Kwadrat(Prostokat):
    """Klasa child"""
    def __init__(self, bok_a):
        super().__init__(bok_a, bok_a)

    def obwod(self):
        """Oblicza obwod kwadratu"""
        return 4 * self.bok_a
    
    def pole(self):
        """Oblicza pole kwadratu"""
        return self.bok_a ** 2
    
class Kolo:
    """Klasa z funkcjami dla koła"""

    pi = 3.14
    def __init__(self, promien):
        self.promien = promien

    def pole(self):
        """Oblicza pole koła"""
        return Kolo.pi * self.promien ** 2
    
    def obwod(self):
        """Oblicza obwod koła"""
        return 2 * Kolo.pi * self.promien 