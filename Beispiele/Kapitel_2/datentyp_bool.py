w1 = True
w2 = False

print("w1 and w2: ", w1 and w2) 
print("w1 or w2: ", w1 or w2) 
print("not w1: ", not w1) 

alter = int(input("Dein Alter: "))
ist_jugendlich = (alter <= 18)
ist_senior = (alter >= 65)
print("ist_jugendlich: ", ist_jugendlich)
print("ist_senior: ", ist_senior)

if ist_jugendlich:
    print("Du bekommst einen Junioren-Rabatt!")
elif ist_senior:
    print("Sie bekommen den Seniorenrabatt!")
else: 
    print("Sie muessen noch ", 65 - alter , " Jahre warten, um den Senioren-Rabatt zu bekommen.")
print("Programmende")
