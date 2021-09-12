import os 
from datetime import date
from abc import ABC,abstractmethod
from Helpers import gotoxy

class Universidad:
    def __init__(self, razonSocial, direccion, telefono, ruc):
        self.razonSocial =  razonSocial
        self.direccion = direccion
        self.telefono = telefono
        self.ruc = ruc
    
    def mostraDatos (self):
        print(""" {}
        - Ruc: {}
        - Direccion: {}
        - Teñefono: {} """. format(self.razonSocial,self.ruc, self.direccion,self.telefono))

class Carrera:
    def __init__(self,id,descripcion):
        self.__id = id
        self.descripcion = descripcion
        
    @property
    def id(self):
        return self.__id
    
    def getCarrera(self):
        return [str(self.id),self.descripcion]

class Materia:
    def __init__(self,id,descripcion):
        self.__id  = id
        self.descripcion = descripcion
        
    @property
    def id(self):
        return self.__id  
        
    def getMateria(self):
        return [str(self.id),self.descripcion]
    
class Profesor:
    def __init__(self,id,nombre,cedula,carrera,titulo,telefono):
        self._id = id
        self.nombre = nombre
        self.cedula = cedula
        self.carrera = carrera
        self.titulo = titulo
        self.telefono = telefono
        
    @property
    def id(self):
        return self._id
    
    def getProfesor(self):
        return [str(self.id),self.nombre,self.cedula, self.carrera,self.titulo, self.telefono]

class Estudiante:
    def __init__(self,id,nombre,cedula,direccion,telefono):
        self._id = id
        self.nombre = nombre
        self.cedula = cedula
        self.direccion = direccion
        self.telefono = telefono
        
    @property
    def id(self):
        return self._id
    
    def getEstudiante(self):
        return [str(self.id),self.nombre,self.cedula, self.direccion, self.telefono]

class Matricula:
    def __init__(self,id,estudiante,carrera, periodo,valor):
        self._id = id
        self.estudiante = estudiante
        self.carrera = carrera
        self.periodo = periodo
        self.valor = valor
        
    @property
    def id(self):
        return self._id
    
    def getMatricula(self):
        return [str(self.id),self.estudiante.id,self.carrera.id, self.periodo,str(self.valor)]
    
class Notas:
    def __init__(self,id,estudiante,materia,profesor,nota1, nota2):
        self._id = id
        self.estudiante = estudiante
        self.materia = materia
        self.profesor = profesor
        self.nota1 = nota1
        self.nota2 = nota2
               
    @property
    def id(self):
        return self._id
    
    def getNota(self):
        return [str(self.id),self.estudiante.id,self.materia.id, self.profesor.id,str(self.nota1),str(self.nota2)]
    
