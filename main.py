# Es obligatorio importar los codigos que se utilizaran de cada clase
#from comida import comida 
import sys
import tkinter as  tk

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget
from comida import *
from ventana1 import VentanaPrincipal



if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal
    ventana.show()
    app.exec()