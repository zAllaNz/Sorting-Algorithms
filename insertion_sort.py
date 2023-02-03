def insertion_sort(lista):
    for j in range(2,len(lista)):
        aux = lista[j]
        i = j - 1
        while(i>=0 and lista[i] > aux):
            lista[i+1] = lista[i]
            i = i - 1
        lista[i+1] = aux

teste = [5,3,4,2,7,8,9,12,5,3,1,5,8,4,7,6,3,1,5,8,9,0]
print("Antes:", teste)
insertion_sort(teste)
print("Resultado:", teste)
