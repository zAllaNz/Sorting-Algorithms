def python_sort(lista):
    nova_lista = []
    for i in range(len(lista)):
        aux = min(lista)
        lista.remove(aux)
        nova_lista += [aux]
    return nova_lista

teste = [5,3,6,2,1,9,8,12,3,84,52,16]
saida = python_sort(teste)
print(saida)