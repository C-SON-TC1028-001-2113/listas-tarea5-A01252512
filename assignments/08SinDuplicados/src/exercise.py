def main():
    #escribe tu código abajo de esta línea
    lista = []
    listaSinDuplicados = []
    n = int(input())

    if n > 0:
        for i in range(n):
            valor = input()
            if valor not in lista:
                listaSinDuplicados.append(valor)
            lista.append(valor)
            
        print(lista)
        print(listaSinDuplicados)
    else:
        print("Error")
 

if __name__=='__main__':
    main()
