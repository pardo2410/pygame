a=13
binario=str(bin(a))
lista=[]
i=2
while i < len(binario):
    b = binario[i]
    lista.append(int(b))   
    i+=1

j=0
for j in lista:
    if lista[j] == lista[j+1]:
        suma = lista[j] + lista[j+1]
        print(suma)
    else:
        maximo = max(lista)
        print(maximo)    

 