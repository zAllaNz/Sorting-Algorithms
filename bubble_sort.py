def bubble_sort(lista):
    tamanho = len(lista)-1
    cont = 0
    for j in range(tamanho):
        for i in range(tamanho,j,-1):
            if lista[i] < lista[i-1]:
                aux = lista[i-1]
                lista[i-1] = lista[i]
                lista[i] = aux
                cont += 1
    print(cont)

teste = [25,15,48,35,61,14,22,11,32,9,1,23]
bubble_sort(teste)
print(teste)