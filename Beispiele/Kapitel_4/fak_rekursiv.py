
def fakultaet(n):
    if n == 1:
        return 1
    else:
        return n * fakultaet(n-1)
        
print("Die Fakultät von 5 ist " + str(fakultaet(5)))        
