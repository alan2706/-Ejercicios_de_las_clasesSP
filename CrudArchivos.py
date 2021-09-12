class Archivo:
    def __init__(self,nombreArchivo,separador=";"):
        self._archivo = nombreArchivo
        self._separador = separador
        
    def leer(self):
        try:
            with open(self._archivos,"r", encoding="UTF-8") as file:
                lista = []
                for linea in file:
                    line = linea [:-1].split(self._separador)
                    lista.append(line)
        except IOError:
            lista = []
        return lista
    
    def buscar(self,buscado):
        resultado = []
        with open(self._archivo,mode= "r",encoding = "utf-8") as file:
            for linea in file:
                if linea[:-1].split(self._separador)[0].find(buscado) is not -1:
                    resultado = linea[:-1].split(self._separador)
        return resultado
    
    def busca2(self,buscado1,buscado2):
        resultado = []
        with open(self._archivo, mode="r",encoding= "utf-8") as file:
            for linea in file:
                registro = linea[:-1].split(self._separador)
                if registro[1] == buscado1 and registro[2] == buscado2:
                    resultado = registro
        return resultado
    
    def escribir(self,datos,modo):
        with open (self._archivo, modo, encoding = "UTF-8") as file:
            for dato in datos:
                file.write (dato+"\n")