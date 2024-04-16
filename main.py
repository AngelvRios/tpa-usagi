# Es obligatorio importar los codigos que se utilizaran de cada clase
#from comida import comida 
import sys
import tkinter as  tk

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget



class OtraVentana(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)

        # Establece la geometría de la ventana
        self.setGeometry(100, 100, 300, 200)  # (posición x, posición y, ancho, alto)
        self.title = comida

        capa = QGridLayout()
        
        texto = QLabel(f"Hola, estoy en la ventana: {self.title}")
        capa.addWidget(texto, 0, 0)
        self.setLayout(capa)

class comida:
    def __init__(self, marca: str, raza: str, age: str, kilogramos: int, comidaN: str):
        self.marca = marca 
        self.raza = raza
        self.age = age
        self.kilogramos = kilogramos
        self.comidaN = comidaN

    def __str__(self):
        return f"Nombre: {self.marca}, Raza: {self.raza}, Edad: {self.age}, Kilogramos: {self.kilogramos}, Comida: {self.comidaN}"

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contador = 0

        #Sección de diseño
        self.setWindowTitle("Tienda para mascotas")
        self.setFixedSize(QSize(1280,720))

        caja = QGridLayout()
        b1 = QPushButton("Adopcion")
        b2 = QPushButton("comida")
        b3 = QPushButton("Jugetes")
        b4 = QPushButton("Medicamentos")
        b5 = QPushButton("Buscar")
        b6 = QPushButton("carrito")
        b7 = QPushButton("flechaL")
        b8 = QPushButton("flechaR")
        caja.addWidget(b1, 0,0)
        caja.addWidget(b2, 0,1)
        caja.addWidget(b3, 0,2)
        caja.addWidget(b4, 0,3)
        caja.addWidget(b6, 0,4)
        caja.addWidget(b5, 0,5)
        caja.addWidget(b7, 1,0)
        caja.addWidget(b8, 1,5)

        """"
        #Ejecucion de la reacción al Click
        b1.clicked.connect(self.reaccionar_1)
        b2.clicked.connect(self.reaccionar_2)
        b3.clicked.connect(self.reaccionar_3)
        b4.clicked.connect(self.reaccionar_4)
        b5.clicked.connect(self.reaccionar_5)
        """

        #Ejecucion de la reacción al Click
        b1.clicked.connect(lambda evento: self.reaccionar(b1.text()))
        b2.clicked.connect(self.abrir_ventana_comida)
        b3.clicked.connect(lambda evento: self.reaccionar(b3.text()))
        b4.clicked.connect(lambda evento: self.reaccionar(b4.text()))
        b5.clicked.connect(lambda evento: self.reaccionar(b5.text()))

        panel = QWidget()
        panel.setLayout(caja)
        self.setCentralWidget(panel)

    
    def abrir_ventana_comida(self):
        nueva_ventana = OtraVentana("Comida")
    

    def reaccionar(self, numero):
        print(f"Boton {numero} con lambda y metodo reaccionar")

    def reaccionar_1(self):
        print(f"Boton 1")

    def reaccionar_3(self):
        print(f"Boton 3")

    def reaccionar_4(self):
        print(f"Boton 4")
    def reaccionar_5(self):
        print(f"Boton 5")

    def abrir_ventana_comida(self):
        # Crear una instancia de la clase comida con los datos que desees
        mi_comida = comida("MarcaX", "Labrador", "cachorro", 5, "Croquetas")
        nueva_ventana = OtraVentana("Informacion de comida", mi_comida)
        nueva_ventana.show()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()