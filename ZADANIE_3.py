"""
ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.
"""
from decimal import Decimal as D
def generator(a=2.0,b=5.5):

    tab=list()
    while a<= b:
        tab.append(D(a))
        a+=0.5
    return tab
print(generator())

