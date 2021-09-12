class Texto:
    def __init__(self,nombreArchivo):
        self.archivo=nombreArchivo
    
    def read(self):
        with open(self.archivo, 'r', encoding="UTF-8") as file:
            for line in file:
                print(line[:-1])

    def write(self,datos,modo):
        with open(self.archivo, modo, encoding="UTF-8") as file:
            for dato in datos:
                file.write(dato+"\n")
                # estudiantes.write('\n')

text=Texto("estudiantes.txt")
text.write(["Marcos Vera","Ana Bohorquez","Miguel Vera"],"a")
text.read()