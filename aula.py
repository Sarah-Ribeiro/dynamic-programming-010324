def busca_binaria(array, x, low, high):
    while low <= high:
        # Forma de calcular a média
        # Só podem ser valores inteiros
        mid = low + (high - low) // 2
        # Se o valor de middle for igual de X
        if array[mid] == x:
            # O valor do middle é retornado
            return mid
        # Continua percorrendo a lista
        # Se o X for maior que o middle
        elif array[mid] < x:
            # Alterna o valor do low, já que o middle não foi encontrado
            low = mid + 1
        else:
            # Alterna o valor do high, já que o middle não foi encontrado
            high = mid - 1
    return -1

array = [3, 4, 5, 6, 7, 8 ,9]
x = 8
resultado = busca_binaria(array, x, 0, len(array)-1)
if resultado != -1:
    print('Elemento está presente no index ' + str(resultado))
else:
    print('Elemento não encontrado')

