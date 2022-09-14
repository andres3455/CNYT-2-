def llenar(cadena):
    arr = cadena.split(" ")
    for j in range(len(arr)):
        arr[i] = tuple(arr[i])
    return arr
def crear_matriz(tamaño):
    matriz =[]
    for i in range (tamaño):
        print("ingrese el vector" ,i," procure usar espacio para separar los valores")
        vector = input()
        matriz.append(llenar(vector))
    return matriz

def marbles():
    tam=int(input("Cuantos vertices desea?"))
    print("teclee el vector -estado- dejando un espacio entre cada valor")
    vector_estado=input()
    vector_estado=llenar(vector_estado)
    La_matriz=crear_matriz(tamaño)
    clicks=int(input("Ingrese el numero de clicks: "))
    while clicks>=0:
