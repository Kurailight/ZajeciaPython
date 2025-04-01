def average(liczby: list[float]) -> float:
    srednia = sum(liczby)/len(liczby)
    return srednia

liczby = [2.0,3.23,45,32]
print(average(liczby))