from Helpers import borrarPantalla,gotoxy
from Componentes import Menu,Valida
from EntidadesUnemi import *
from CrudArchivos import Archivo
from datetime import date


def carreras():
    borrarPantalla()
    gotoxy(20,2);print("MANTENIMIENTO DE CARRERAS")
    gotoxy(15,4);print("Codigo: ")
    gotoxy(15,5);print("Descripcion carrera: ")
    gotoxy(35,5)
    desCarrera = input()
    archiCarrera = Archivo("./Carrera.txt",";")
    carreras = archiCarrera.leer()
    if carreras : idSig = int(carreras[-1][0])+1
    else: idSig = 1
    carrera = Carrera(idSig,desCarrera)
    datos = carrera.getCarrera()
    datos = ";".join(datos)
    archiCarrera.escribir([datos],"a")
    
def materias():
    borrarPantalla()
    gotoxy(20,2);print("MANTENIMIENTO DE MATERIAS")
    gotoxy(15,4);print("Codigo: ")
    gotoxy(15,5);print("Descripcion materia: ")
    gotoxy(35,5)
    desMaterias = input()
    archiMaterias = Archivo("./Materias.txt",";")
    materias = archiMaterias.leer()
    if materias : idSig = int(materias[-1][0])+1
    else: idSig = 1
    materias = Materia(idSig,desMaterias)
    datos = materias.getMateria()
    datos = ";".join(datos)
    archiMaterias.escribir([datos],"a")
    
#Menu Proceso Principal
opc = ""
while opc != "5":
    borrarPantalla()
    menu = Menu("Menu Principal",["1) Mantenimiento","2) Matriculación","3) Notas","4) Consultas","5) Salir"],20,5)
    opc = menu.menu()
    if opc == "1":
        opc1 = ""
        while opc1 != "6":
            borrarPantalla()
            menu1 = Menu("Menu Mantenimiento",["1)Carreras","2) Materias","3) Periodos","4) Profesores", "5) Estudiantes","6) Salir"],20,5)
            opc1 = menu1.menu()
            if opc1 == "1":
                carreras()
            elif opc1 == "2":
                materias()
            elif opc1 == "3":
                pass
            elif opc1 == "4":
                pass
    
    elif opc == "2":
            borrarPantalla()
            menu2 = Menu("Menu Matriculación",["1) Matricula","2) Salir"],20,5)
            opc2 = menu2.menu()
            if opc2 == "1":
                pass
            elif opc2 == "2":
                pass
            
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("Menu Notas",["1) Notas","2) Salir"],20,5)
            opc3 = menu3.menu()
            if opc3 == "1":
                pass
            elif opc3 == "2":
                pass
            
    elif opc == "4":
            borrarPantalla()
            menu4 = Menu("Menu Consultas",["1) Materias","2) Profesores", "3) Estudiantes","4) Cargo","5) Salir"],20,5)
            opc4 = menu4.menu()
            if opc4 == "1":
                pass
            elif opc4 == "2":
                pass
            
    elif opc == "5":
        borrarPantalla()
        print("Gracias por su visita....")
        
    else:
        print("Opcion no valida")
        
input("Presione una tecla para salir")
borrarPantalla()