
def begruesse_person(person):
    if person[2] >= 18:
        print("Guten Tag Herr", person[1])
    else:
        print("Hallo " + person[0] + "! Was geht, Alter?")
        

mein_vorname = input("Geben Sie Ihren Vornamen ein: ")
mein_nachname = input("Geben Sie Ihren Nachnamen ein: ")
mein_alter = int(input("Geben Sie Ihr Alter ein: "))

ich = (mein_vorname, mein_nachname, mein_alter)

# Das folgende geht nicht:
# ich[2] = 42

begruesse_person(ich)
