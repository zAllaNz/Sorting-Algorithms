def selection_sort(lista):
    tamanho = len(lista)
    for j in range(tamanho-1):
        menor = j
        for i in range(j+1,tamanho):
            if lista[i] < lista[menor]:
                menor = i
        aux = lista[j]
        lista[j] = lista[menor]
        lista[menor] = aux
    print(lista)

teste = [5,6,3,8,9,1,525,64,254,879,31,245,1,65,97,452,3,1]
selection_sort(teste)