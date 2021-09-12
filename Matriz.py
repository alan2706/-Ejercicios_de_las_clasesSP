import os
class Matriz:
    def __init__(self,matriz,fila,col):
        self.matriz = matriz
        self.fila = fila
        self.col = col
        
    def ingresar(self):
        self.matriz=[]
        for fila in range(self.fila):
            columnas=[]
            for col in range(self.col):
                valor = input("Fila[{}] Col[{}]:".format(fila,col))
                columnas.append(valor)
            self.matriz.append(columnas)
    
    
    def presentar (self):
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                # print(columna[col],end=" ")
                print("[{}]".format(self.matriz[fila][col]),end=" ")
            print()



    def buscar(self,valor):
        enc= False
        for pos1,ele1 in enumerate(self.matriz):
            for pos,ele in enumerate(ele1):
                    if ele==str(valor):
                        enc=True
                        buscar=(pos1,"columna",pos)
                        break
        if enc==True:
            return buscar
        else:
            return -1
        
        
        
    def buscar2(self,valor):
        enc={}
        band=True
        fila=0
        while fila < len(self.matriz)and band:
            col=0
            while col< len(self.matriz[fila])and band:
                if self.matriz[fila][col]==str(valor):
                    enc["fila"]=fila
                    enc["col"]=col
                    band=False
                else: col+=1
            fila+=1
        return enc
                       
    def sumar(self,mat):
        matrizSuma=[]
        for fila in range(self.fila):
            columnas=[]
            for col in range(self.col):
                valor = self.matriz[fila][col] + mat[fila][col]
                columnas.append(valor)
            self.matriz.append(columnas)
        return matrizSuma
        
        
     
# numeros=[[10,20,30],[60,80,90],[25,35,55]]

numero=[]
mat = Matriz(numero,2,2)
numeros1=[]
mat1 = Matriz(numeros1,2,2)
# print(numeros[0],numeros[0][1])
mat.ingresar()
mat1.ingresar()
mat.presentar()
print()
mat1.presentar()
# res=mat.buscar("80")
# if res==-1:print("No existe valor en la matriz")
# else:print("su Fila es: {}".format(res))
# print()
# res=mat.buscar2("josue")
# if res:print("El valor se encuentra en las siguientes coordenadas: {}".format(res))
# else:print("No existe valor en la matriz")
# mat.ingresar()
print(mat.sumar(mat1.matriz))
