from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from comida import SeleccionarComidaDialog
from adopcion1 import TiendaMascotas, VentanaAdopcion, VentanaMascotas

class VentanaPrincipal(QMainWindow):
    def __init__(self, tienda):
        super().__init__()
        self.setWindowTitle("Tienda para mascotas")
        self.setFixedSize(500, 400)
        self.tienda = tienda

        # Botón para seleccionar comida
        btn_comida = QPushButton("Seleccionar Comida", self)
        btn_comida.clicked.connect(self.abrir_ventana_comida)
        btn_comida.setGeometry(50, 50, 200, 50)

        # Botón para abrir ventana de adopción
        btn_adopcion = QPushButton("Adoptar", self)
        btn_adopcion.clicked.connect(self.abrir_ventana_adopcion)
        btn_adopcion.setGeometry(50, 120, 200, 50)

        # Botón para ver animales disponibles
        btn_ver_animales = QPushButton("Ver Animales Disponibles", self)
        btn_ver_animales.clicked.connect(self.mostrar_animales_disponibles)
        btn_ver_animales.setGeometry(50, 190, 200, 50)

    def abrir_ventana_comida(self):
        dialogo_comida = SeleccionarComidaDialog(self)
        dialogo_comida.exec()

    def abrir_ventana_adopcion(self):
        ventana_adopcion = VentanaAdopcion(self.tienda)
        ventana_adopcion.exec()

    def mostrar_animales_disponibles(self):
        ventana_mascotas = VentanaMascotas(self.tienda)
        ventana_mascotas.actualizar_mascotas_disponibles()  # Actualizar la lista de animales antes de mostrar
        ventana_mascotas.exec()

if __name__ == "__main__":
    app = QApplication([])
    tienda = TiendaMascotas()
    ventana = VentanaPrincipal(tienda)  # Pasa la tienda como argumento
    ventana.show()
    app.exec()
