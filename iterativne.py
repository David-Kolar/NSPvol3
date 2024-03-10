N = int(input())
A = input()
N2 = int(input())
B = input()


class Polovina():
    def __init__(self, znak, i, j):
        self.znak = znak
        self.i = i
        self.j = j

def iterativne4(startA, konecA, startB, konecB, polovina=1):
    delkaA = konecA - startA + 1
    delkaB = konecB - startB + 1
    predchozi = [(0, Polovina("0", 0, 0)) for i in range(delkaB)]
    for i in range(delkaA):
        aktualni = [(0, -1) for i in range(delkaB)]
        for j in range(delkaB):
            maximum = 0
            val1 = val2 = val3 = 0
            polovina1 = Polovina("0", 0, 0)
            nova_polovina = Polovina("0", 0, 0)
            if (j > 0):
                val1, polovina1 = predchozi[j-1]
                val2, polovina2 = aktualni[j-1]
                val3, polovina3 = predchozi[j]
            if (A[i+startA] == B[j+startB]):
                maximum = val1 + 1
                nova_polovina = polovina1
                if (maximum == polovina):
                    nova_polovina = Polovina(A[i+startA], i+startA, j+startB)
            if (maximum < val3):
                maximum = val3
                nova_polovina = polovina3
            if (maximum < val2):
                maximum = val2
                nova_polovina = polovina2

            aktualni[j] = maximum, nova_polovina
        predchozi = aktualni

    return predchozi[delkaB - 1]

class Interval:
    def __init__(self, startA, konecA, startB, konecB, startCesty, konecCesty):
        self.startA = startA
        self.konecA = konecA
        self.startB = startB
        self.konecB = konecB
        self.startCesty = startCesty
        self.konecCesty = konecCesty


def nalezni_cestu():
    delka_cesty = iterativne4(0, len(A)-1, 0, len(B)-1)[0]
    if (delka_cesty == 0):
        return []
    cesta = [0]*delka_cesty
    intervaly = [Interval(0, len(A)-1, 0, len(B)-1, 1, delka_cesty)]
    while(intervaly):
        nove_intervaly = []
        for interval in intervaly:
            pozice_v_ceste = (interval.startCesty + interval.konecCesty) // 2
            if (cesta[pozice_v_ceste-1] != 0):
                continue
            polovina = pozice_v_ceste - interval.startCesty + 1
            stred = iterativne4(interval.startA, interval.konecA, interval.startB, interval.konecB, polovina)[1]
            cesta[pozice_v_ceste-1] = stred.znak
            nove_intervaly.append(Interval(interval.startA, stred.i, interval.startB, stred.j, interval.startCesty, pozice_v_ceste))
            nove_intervaly.append(Interval(stred.i, interval.konecA, stred.j, interval.konecB, pozice_v_ceste, interval.konecCesty))
        intervaly = nove_intervaly
    posledni = iterativne4(0, len(A)-1, 0, len(B)-1, delka_cesty)[1].znak
    cesta[delka_cesty - 1] = posledni
    return cesta

print(nalezni_cestu())