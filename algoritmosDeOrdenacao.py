#lista=[1,3,5,6,7,8,0,2,4,6,8]

# #coloque os elementos em ordem crescente

# # print(sorted(lista))

# #Ordenação sem utilizar a ferramenta "Sorted()"

# for numero in range(len(lista)):
# #pega os elementos em um distância equivalente ao tamanho da lista
#     for numero2 in range(len(lista)-1):
#         if lista[numero2] > lista[numero2 +1]:
#         #caso o numero no index[0] seja maior que o index[1]
#             lista[numero2], lista[numero2 +1] = lista[numero2 +1], lista[numero2]
#             #os elementos trocam de lugar.
# print(lista)

#ordenação utilizando metodo bubble sort

# lista = [3,7,5,2,1]

# def bubble_sort(lista):
#     n = len(lista)
#     for j in range(n-1):
#         for i in range(n-1):
#             if lista[i] > lista[i+1]:
#                 #troca de elementos nas posições i e i+1
#                 lista[i], lista[i+1] = lista[i+1], lista[i]


# bubble_sort(lista)

# print(lista)

#ordenação com iteração (minha versão):

# lista = [3,7,5,2,1]

# def bubble_sort(lista):
#     n = len(lista)
#     for j in range(n-1):
#         for i in range(n-1):
#             if lista[i] > lista[i+1]:
                 
#                 lista[i], lista[i+1] = lista[i+1], lista[i]
#                 print(lista)
     
# bubble_sort(lista)

# print(f"lista ordenada: {lista}")

#ordenação iteração (método do professor)


def selection_sort(lista):
    n = len(lista)
    for i in range(n-1, 0, -1):
        indice_maior= 0
        for j in range(1, i + 1):
            if lista[j]> lista[indice_maior]:
                indice_maior = j
        #coloca o maior elemento na posição correta (fim da parte não ordenada)
        lista[i], lista[indice_maior] = lista[indice_maior], lista[i]
        print(f"Lista após iteração {(i-n)*-1}", lista)


if __name__ == '__main__':
    #exemplos de uso
    valores = [3,7,5,2,1]
    print("lista inicial:", valores)
    selection_sort(valores)
    print("Lista ordenada:", valores)