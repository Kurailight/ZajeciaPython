'''
Zaimplementuj funkcję wykorzystującą iterator do zwracania kolejnych liczb ciągu Fibonacciego. Generator powinien umożliwiać iteracyjne pobieranie wartosci bez
konieczności przechowywania całej sekwencji w pamięci.
'''
class Fibonacci:
    def __init__(self, liczba_n):
        self.liczba_n = liczba_n  
        self.counter = 0          
        self.a, self.b = 0, 1   

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.liczba_n:  
            raise StopIteration

        if self.counter == 0:
            self.counter += 1
            return self.a  
        elif self.counter == 1:
            self.counter += 1
            return self.b  
        nowa_wartosc = self.a + self.b  
        self.a = self.b  
        self.b = nowa_wartosc  

        self.counter += 1  
        return nowa_wartosc 

fibonacci = Fibonacci(10)

for liczba in fibonacci:
  print(liczba)
'''
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))

'''
