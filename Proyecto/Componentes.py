from Helpers import gotoxy,borrarPantalla
import time
class Menu:
    def __init__(self,titulo="",opciones= [],col=6,fil=1):
        self.titulo=titulo
        self.opciones= opciones
        self.col = col
        self.fil = fil
        
    def menu(self):
        gotoxy(self.col,self.fil);print(self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil += 1
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input("Elija opcion[1...{}]:".format(len(self.opciones)))
        return opc

class Valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True:
            gotoxy(col,fil)
            valor = input()
            try:
                if int(valor)>0:
                    break
            except: gotoxy(col,fil);print(mensajeError)
            time.sleep(1)
            gotoxy(col,fil);print(" "*len(mensajeError))
        return valor
    
    def solo_letras(self,mensaje,mensajeError):
        while True:
            valor = str(input("          ------->    I   {} ".format(mensaje)))
            if valor.isalpha():
                break
            else:
                print(("          -------><    I   {} ".format(mensajeError)))
        return valor
    
    def solo_decimales(self,mensaje, mensajeError):
        while True:
            valor = str(input("          ------->    I   {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print(("          -------><    I   {} ".format(mensajeError)))
        return valor
                
    def cedula():
        pass
    
class otra:
    pass


# borrarPantalla()
# val = Valida()
# gotoxy(10,2);print("Ingrese Año: ")
# gotoxy(12,2)
# val.solo_numeros("Error ingrese solo numeros...!!!",22,2)