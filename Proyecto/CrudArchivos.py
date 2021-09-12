class Archivo:
    def __init__(self,nombreArchivo,separador=";"):
        self.__archivo = nombreArchivo
        self.__separador = separador
        
    def leer(self):
        try:
            with open(self.__archivo,"r", encoding="UTF-8") as file:
                lista = []
                for linea in file:
                    line = linea [:-1].split(self.__separador)
                    lista.append(line)
        except IOError:
            lista = []
        return lista
    
    def buscar(self,buscado):
        resultado = []
        with open(self.__archivo,mode= "r",encoding = "UTF-8") as file:
            for linea in file:
                if linea[:-1].split(self.__separador)[0].find(buscado) is not -1:
                    resultado = linea[:-1].split(self.__separador)
        return resultado
    
    def busca2(self,buscado1,buscado2):
        resultado = []
        with open(self.__archivo, mode="r",encoding= "UTF-8") as file:
            for linea in file:
                registro = linea[:-1].split(self.__separador)
                if registro[1] == buscado1 and registro[2] == buscado2:
                    resultado = registro
        return resultado
    
    def escribir(self,datos,modo):
        with open (self.__archivo, modo, encoding = "UTF-8") as file:
            for dato in datos:
                file.write (dato+"\n")