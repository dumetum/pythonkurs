n = 5

fak = 1

# Achtung: Bei der range-Funktion ist der zweite Parameter exclusiv
for i in range(1,n+1):
    fak = fak * i
    
print("Die Fakultät von " + str(n) + " ist " + str(fak))
 
