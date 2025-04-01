import json

'''
Napisz klasę ModelAI, która pozwala na śledzenie liczby utworzonych modeli oraz umożliwia tworzenie obiektu na podstawie pliku json


'''
class ModelAI:

    liczba_modeli = 0

    def __init__(self, nazwa_modelu, wersja):
        self.nazwa_modelu = nazwa_modelu
        self.wersja = wersja
        ModelAI.liczba_modeli += 1

    def nowy_model(self):
        ModelAI.liczba_modeli+=1 
        
    @classmethod
    def ile_modeli(cls):
        return cls.liczba_modeli
    
    @classmethod
    def z_pliku(cls, nazwa_pliku):
        with open(nazwa_pliku, "r") as f:
            dane = json.load(f)  
        return cls(dane["name"], dane["version"])
    

model1 = ModelAI.z_pliku("model.json")
print(model1.nazwa_modelu, model1.wersja)  
print(ModelAI.ile_modeli())  #1
