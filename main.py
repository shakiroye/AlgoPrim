def Prim(Graphe):
    T = []
    n = len(Graphe)
    plusProche = []
    distanceMin = []

    for i in range(0, n):
        plusProche.append(0)
        distanceMin.append(0)

    for i in range(1, n):
        plusProche[i] = 0
        distanceMin[i] = Graphe[i][0]

    for i in range(0, n - 1):
        min = None
        for j in range(1, n):
            if ((min and distanceMin[j] and 0 <= distanceMin[j] < min) or (not min and 0 <= distanceMin[j])):
                min = distanceMin[j]
                k = j

        T.append((k, plusProche[k]))
        print(T)

        distanceMin[k] = -1
        distanceMin[plusProche[k]] = -1

        for j in range(1, n):
            if ((distanceMin[j] and Graphe[k][j] and Graphe[k][j] < distanceMin[j]) or not distanceMin[j]):
                distanceMin[j] = Graphe[k][j]
                distanceMin[k] = Graphe[j][k]

                plusProche[j] = k
                plusProche[k] = j

    return T


Graphe1 = [[None, 1, None, 4, None, None, None],
           [1, None, 2, 6, 4, None, None],
           [None, 2, None, None, 5, 6, None],
           [4, 6, None, None, 3, None, 4],
           [None, 4, 5, 3, None, 8, 7],
           [None, None, 6, None, 8, None, 3],
           [None, None, None, 4, 7, 3, None]]

Prim(Graphe1)