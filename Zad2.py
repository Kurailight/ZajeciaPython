import numpy as np

'''
Napisz klase Matrix, która reprezentuje macierz 2x2. Przeciąż operatory: dodawania i mnożenia macierzy. 
'''

class Matrix:
    def __init__(self, a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        return Matrix(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
    
    def __mul__(self, other):
        return Matrix(
                self.a * other.a + self.b * other.c, self.a * other.b + self.b * other.d,
                self.c * other.a + self.d * other.c, self.c * other.b + self.d * other.d)
    
    def __str__(self):
        return f"[{self.a}, {self.b}; \n {self.c}, {self.d}]"
    
    def __repr__(self):
        return f"Matrix({self.a}, {self.b}, {self.c}, {self.d})"
    
m1= Matrix(1,2,3,4)
m2= Matrix(2,0,1,2)
m3 = m1 + m2
print(str(m3))

m4 = m1*m2 
print(m4)
print(repr(m4))