# Es obligatorio importar los codigos que se utilizaran de cada clase
#from comida import comida 
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contador = 0

        #Sección de diseño
        self.setWindowTitle("La 2da aplicación con PyQt6")
        self.setFixedSize(QSize(1280,720))

        caja = QGridLayout()
        b1 = QPushButton("Adopcion")
        b2 = QPushButton("Alimentos")
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
        b2.clicked.connect(lambda evento: self.reaccionar(b2.text()))
        b3.clicked.connect(lambda evento: self.reaccionar(b3.text()))
        b4.clicked.connect(lambda evento: self.reaccionar(b4.text()))
        b5.clicked.connect(lambda evento: self.reaccionar(b5.text()))

        panel = QWidget()
        panel.setLayout(caja)
        self.setCentralWidget(panel)
    

    def reaccionar(self, numero):
        print(f"Boton {numero} con lambda y metodo reaccionar")

    def reaccionar_1(self):
        print(f"Boton 1")

    def reaccionar_2(self):
        print(f"Boton 2")
    def reaccionar_3(self):
        print(f"Boton 3")

    def reaccionar_4(self):
        print(f"Boton 4")
    def reaccionar_5(self):
        print(f"Boton 5")


    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()