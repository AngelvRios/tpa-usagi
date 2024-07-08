# En principal.py

import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QDialog, QDockWidget, QScrollArea, QDialogButtonBox
import csv
from datetime import datetime
from ui_login import Ui_LoginWindow
from ui_dock_widget import Ui_DockWidget
from comida import VentanaPrincipal as VentanaComida
from juguetes import SeleccionarJugueteDialog
from accesorio import SeleccionarAccesorioDialog
from adopcion import AdopcionVentana
from Carrito import PaginaCarrito  # Asumiendo que PaginaCarrito está implementado en carrito.py

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_login = Ui_LoginWindow()
        self.ui_login.setupUi(self)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana Principal')
        self.setGeometry(100, 100, 800, 600)
        self.setMinimumSize(800, 600)
        self.setMaximumSize(1000, 800)

        # Dock widget setup
        self.dock_widget = QDockWidget("DockWidget", self)
        self.ui_dock_widget = Ui_DockWidget()
        self.ui_dock_widget.setupUi(self.dock_widget)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.RightDockWidgetArea, self.dock_widget)

        # Connect dock widget buttons
        self.ui_dock_widget.AdopcionButton.clicked.connect(self.abrir_ventana_adopcion)
        self.ui_dock_widget.AlimentosButton.clicked.connect(self.abrir_ventana_comida)
        self.ui_dock_widget.JuguetesButton.clicked.connect(self.abrir_ventana_juguetes)
        self.ui_dock_widget.AccesorioButtom.clicked.connect(lambda: self.abrir_ventana_accesorios(None))
        self.ui_dock_widget.CarritoButton.clicked.connect(self.abrir_pagina_carrito)

        # Scroll Area setup
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setGeometry(70, 150, 500, 150)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setStyleSheet("QScrollArea { background-color: pink; border: 2px solid black; }")

        self.scroll_content = QWidget()
        self.scroll_content.setStyleSheet("QWidget { background-color: pink; }")
        self.scroll_layout = QHBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)

        # Crear instancia de PaginaCarrito
        self.carrito_compras = PaginaCarrito()
        self.carrito_compras.cargar_productos_desde_csv('carrito.csv')  # Cargar productos desde el CSV

        self.load_offers()

    def load_offers(self):
        try:
            with open('ofertas.csv', 'r') as file:
                reader = csv.reader(file)
                # Saltar la primera línea (encabezado)
                next(reader)
                for row in reader:
                    producto = row[0]
                    button = QPushButton(f"Oferta: {producto}", self)
                    button.setFixedSize(100, 100)
                    button.setStyleSheet("font-size: 16px; background-color: pink; border: 1px solid black;")
                    button.clicked.connect(lambda _, producto=producto: self.agregar_al_carrito(producto))
                    self.scroll_layout.addWidget(button)
        except FileNotFoundError:
            print("El archivo 'ofertas.csv' no se encuentra.")

    def agregar_al_carrito(self, producto):
        with open('carrito.csv', mode='a', newline='') as file:
            escritor = csv.writer(file)
            escritor.writerow([producto,])
        print(f'Producto {producto} agregado al carrito.')

    def inicializar_archivo_csv(self):
        try:
            with open('registro.csv', mode='x', newline='') as file:
                escritor_csv = csv.writer(file)
                escritor_csv.writerow(["Fecha", "Operación", "Detalles"])
        except FileExistsError:
            pass

    def registrar_operacion(self, operacion, detalles):
        with open('registro.csv', "a", newline='') as file:
            escritor_csv = csv.writer(file)
            escritor_csv.writerow([datetime.now().isoformat(), operacion, detalles])

    def abrir_ventana_accesorios(self, tipo_animal):
        dialog_accesorios = SeleccionarAccesorioDialog(tipo_animal)
        if dialog_accesorios.exec() == QDialog.DialogCode.Accepted:
            accesorio, cantidad = dialog_accesorios.get_accesorio_seleccionado()
            detalles = f"Tipo de animal: {tipo_animal}, Accesorio: {accesorio}, Cantidad: {cantidad}"
            self.registrar_operacion("Compra de accesorio", detalles)

    def abrir_ventana_adopcion(self):
        self.ventana_adopcion = AdopcionVentana()
        self.ventana_adopcion.show()

    def abrir_ventana_comida(self):
        dialog_comida = VentanaComida()
        dialog_comida.show()

    def abrir_ventana_juguetes(self):
        dialog_juguetes = SeleccionarJugueteDialog()
        if dialog_juguetes.exec() == QDialog.DialogCode.Accepted:
            tipo_animal = dialog_juguetes.tipo_combo_box.currentText()
            juguete = dialog_juguetes.get_juguete_seleccionado()
            detalles = f"Tipo de animal: {tipo_animal}, Juguete: {juguete}"
            self.registrar_operacion("Compra de juguete", detalles)

    def abrir_pagina_carrito(self):
        dialogo_carrito = QDialog(self)
        dialogo_carrito.setWindowTitle('Carrito de Compras')
        layout = QVBoxLayout()

        # Agregamos la ventana PaginaCarrito al layout del QDialog
        layout.addWidget(self.carrito_compras)

        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        botones.accepted.connect(dialogo_carrito.accept)
        layout.addWidget(botones)

        dialogo_carrito.setLayout(layout)
        dialogo_carrito.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = MainApp()
    mainApp.show()
    sys.exit(app.exec())
