"""
ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
1-n = [1,2,3,4,5,...,10]
np. n=10
wejście: [2,3,7,4,9], 10
wyjście: [1,5,6,8,10]
"""
def lack(a,b):                              # a- list ,b = n
    if sorted(a)[-1] <= b:  
        return [i for i in range(1,b+1) if i not in a]
    else: 
        return 'ERROR -> n jest mniejsze od maksymalnej liczby w tablicy '
    
print(lack([2,3,7,4,9], 15))
print(lack([1,6], 4))