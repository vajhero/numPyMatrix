import numpy as np

liczba = int(input("Podaj dowolną liczbę"))

macierz1 = np.random.randint(100, size=(liczba,liczba))
macierz2 = np.random.randint(100, size=(liczba,liczba))

print("Macierz 1")
print (macierz1)
print ("")
print("Macierz 2")
print (macierz2)
print ("")
print("Dodawanie macierzy:")
print (macierz1+macierz2)
print ("")
print("Mnożenie macierzy:")
print (macierz1*macierz2)