class ListaB:
    def __init__(self,listas):
        self.__lista=listas  #atributo de clase
          
    @property
    def lista(self):  #getproperty
        # if self.__lista != None:
        return self.__lista   
        # else: print("Ingrese la lista") 
    # @lista.setter
    # def lista(self,value):  #setproperty
    #     self.__lista = value
    
    #busca un valor en la lista; return posicion si lo encuentra
    #y si no la encuentra return -1. 
    def busquedaLineal(self,buscado):
    
        pos = 0
        band=False
        long=len(self.__lista)
        # este metodo recorre la lista hasta que la posicion sea igual
        # a la longitud y band sea igual a True.
        while pos < long and band == False:
            if self.__lista[pos]["nombre"] == buscado:
                band=True
            else: pos+=1
        if band: return(pos) 
        else: return -1 
                          
            
    def ordenar(self,orden):
        orden = orden.lower()
        if orden == "asc":
            for pos in range(0,len(self.__lista)):
                for sig in range(pos+1,len(self.__lista)):
                    if self.__lista[pos]["nombre"]> self.__lista[sig]["nombre"]:
                        aux=self.__lista[pos]
                        self.__lista[pos]=self.__lista[sig]
                        self.__lista[sig]=aux
        else:
            for pos in range(0,len(self.__lista)):
                for sig in range(pos+1,len(self.__lista)):
                    if self.__lista[pos]["nombre"]< self.__lista[sig]["nombre"]:
                        aux=self.__lista[pos]
                        self.__lista[pos]=self.__lista[sig]
                        self.__lista[sig]=aux
                           
    def busquedaBinaria(self,buscado):
        self.ordenar("asc")
        fin=len(self.lista)-1  #gurada la posicion final del segmento lista
        inicio=0               #guarda la posicion iniciaa del segmento lista
        enc=False
        while inicio <=fin and enc==False:
            medio=(inicio+fin)//2
            if self.lista[medio]["nombre"]==buscado: enc=True
            elif self.lista[medio]["nombre"]< buscado: inicio =medio+1
            else: fin=medio-1
        if enc:return medio
        else:return -1
            
        

notas=[
    {"nombre":"Daniel","n1":20,"n2":40},
    {"nombre":"Danny","n1":30,"n2":50},
    {"nombre":"Dayana","n1":40,"n2":50},
    {"nombre":"Yady","n1":60,"n2":40},
    {"nombre":"Erick","n1":50,"n2":40},
    {"nombre":"Romina","n1":55,"n2":40},
    
]
    
bus= ListaB(notas)
# print(bus.lista)
# bus.lista = [3.5]
# print(bus.lista)
posicion=bus.busquedaBinaria("Romina") 
if posicion != -1: print(bus.lista[posicion])
else:print("no esta en la lista")
