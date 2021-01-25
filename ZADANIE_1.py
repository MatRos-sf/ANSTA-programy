"""
ZADANIE 1. GENERATOR KODow POCZTOWYCH
przyjmuje 2 stringi: "79-900" i "80-155" i zwraca liste kodow pomiedzy nimi
"""
# sposob 1
def view_postcode(a):
    
    if a>=10000:
        return str(a)
    else:
        zero= 5-len(str(a))
        return '0'*zero+str(a)

def postCodes(a,b):

   tab=list()
   x =  lambda y: int(y.replace('-',''))
   a,b = x(a),x(b)

   for i in range(a+1,b):
        pc=view_postcode(i)                         #post codes
        tab.append('%s-%s' %(pc[:2],pc[2:]))
   return tab

#print(postCodes("79-900" , "80-155"))

# sposob 2 
def postCodesII(a,b):
    
    c = lambda y: int(y.replace('-',''))
    a, b = c(a), c(b)
    
    tab = [str(i).zfill(5) for i in range(a+1,b)]
    return ['%s-%s' %( i[:2] , i[2:]) for i in tab ]
    
print(postCodesII("79-900" , "80-155"))

