class Lista:
    def __init__(self,tamanio=3):
        self.lista=[]
        self.longitud=0
        self.size=tamanio

    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud +=1
            
        else:
            print("Lista esta llena")
        
    def obtener(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            return self.lista[pos]

    def obtenerEliminando(self,pos):
        
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            eliminado=self.lista[pos]
            aux=[]
            # self.lista=self.lista[:pos] + self.lista[pos+1:]
            for ind in range(pos):
                aux=aux+[self.lista[ind]]
            for ind2 in range(pos+1,self.longitud):
                aux=aux+[self.lista[ind2]]
            self.longitud-=1
            self.lista=aux
            return (self.lista,eliminado)
            

    def mostrar(self):
        print("{:3}{:9} {}".format("","Lista","Posicion"))
        for pos,ele in enumerate(self.lista):
            print("[{:8}]  {:5}".format(ele,pos))

lista1=Lista(3)
lista1.append("Daniel")
lista1.append(52)
lista1.append(True)
lista1.append("Milagro")
lista1.mostrar()
posicion = int(input("ingrese posicion para obtener el elemento: "))
resp= lista1.obtenerEliminando(posicion)
if resp ==None:
    print("Posicion no valida, Verifique la Lista.....")
else:
    print("El elemento de la posicion: {} es: {}".format(posicion,resp))