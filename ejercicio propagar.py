def propagar(L):
    resultado = L.copy()

    for i in range(len(L)):

        if L[i] == 1:

            # hacia la izquierda
            j = i - 1
            while j >= 0 and L[j] == 0:
                resultado[j] = 1
                j -= 1

            # hacia la derecha
            j = i + 1
            while j < len(L) and L[j] == 0:
                resultado[j] = 1
                j += 1

    return resultado

print(propagar([0, 0, 0, -1, 1, 0, 0, 1]))
print(propagar([0, 0, 0, 1, 0, 0]))