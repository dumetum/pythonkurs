# Merge-Sort: Sortierung einer Liste
#
# Idee: Hat die zu sortierende Liste nur 0 oder 1 Element ist nichts zu tun. Die Liste kann unverändert zurückgeben werden.
#  Andernfalls: 
#  - Teile die Listen in zwei gleichgroße Listen
#  - Sortiere die Listen rekursiv
#  - "Mische" die beiden sortierten Listen zu einer sortierten Liste und gebe diese zurück
#
# siehe auch: https://idea-instructions.com/merge-sort/


l = [123, 45, 67, 34, 23, 198, 263]

def merge_sort(liste):
    print("Sort: ", liste)
    # Wie sieht die Sortierung einer Liste der Groesse 0 oder 1 aus?

    # Aufspaltung in zwei Listen l1 und l2 und diese zusammenmischen
    return merge(l1, l2)

def merge(liste1, liste2):
    print("Merge ", liste1, liste2)
    ret_list = []
    # Die beiden Listen muessen durchwandert werden
    return ret_list

print(merge_sort([]))
print(merge_sort([1]))
print(merge_sort([1,2]))
print(merge_sort([2,1]))

print(l)
print(merge_sort(l))
