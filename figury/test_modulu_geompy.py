from geompy.figury2d import Kolo, Prostokat, Kwadrat
from geompy.figury3d import Kula, Prostopadloscian, Szescian

# Test dla koła
kolo = Kolo(4)
p = kolo.pole()
o = kolo.obwod()
print("Pole koła:", p, "Obwód koła:", o)

# Test dla kuli
kula = Kula(4)
p1 = kula.pole_calkowite()
o1 = kula.objetosc()
print("Pole całkowite kuli:", p1, "Objętość kuli:", o1)

# Test dla prostokąta
prostokat = Prostokat(4, 2)
p2 = prostokat.pole()
o2 = prostokat.obwod()
print("Pole prostokąta:", p2, "Obwód prostokąta:", o2)

# Test dla prostopadłościanu
prostopadloscian = Prostopadloscian(4, 1, 2)
p3 = prostopadloscian.pole_calkowite()
o3 = prostopadloscian.objetosc()
print("Pole całkowite prostopadłościanu:", p3, "Objętość prostopadłościanu:", o3)

# Test dla kwadratu
kwadrat = Kwadrat(2)
p4 = kwadrat.pole()
o4 = kwadrat.obwod()
print("Pole kwadratu:", p4, "Obwód kwadratu:", o4)

# Test dla sześcianu
szescian = Szescian(3)
p5 = szescian.pole_calkowite()
o5 = szescian.objetosc()
print("Pole całkowite sześcianu:", p5, "Objętość sześcianu:", o5)
