import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QWidget, QDialog, QVBoxLayout, QLabel, QDialogButtonBox, QDockWidget, QScrollArea
import csv
from datetime import datetime
from ui_login import Ui_LoginWindow
from ui_dock_widget import Ui_DockWidget
from comida import VentanaPrincipal as VentanaComida
from juguetes import SeleccionarJugueteDialog
from accesorio import SeleccionarAccesorioDialog
from adopcion import AdopcionVentana
from Carrito import PaginaCarrito

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
        self.scroll_area.setGeometry(50, 50, 700, 500)
        self.scroll_area.setWidgetResizable(True)
        
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)

        self.load_offers()

    def load_offers(self):
        try:
            with open('ofertas.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    button = QPushButton(f"Oferta: {row[0]}", self)
                    button.setFixedSize(100, 100)
                    self.scroll_layout.addWidget(button)
        except FileNotFoundError:
            print("El archivo 'ofertas.csv' no se encuentra.")
            
    def load_data(self):
        with open('productos.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            self.tableWidget.setColumnCount(len(header))
            self.tableWidget.setHorizontalHeaderLabels(header)
            for row in reader:
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                for column, item in enumerate(row):
                    self.tableWidget.setItem(row_position, column, QTableWidgetItem(item))

    def agregar_al_carrito(self, row, column):
        nombre_producto = self.tableWidget.item(row, 0).text()
        self.carrito.agregar_producto(nombre_producto)
        print(f'Producto {nombre_producto} agregado al carrito.')

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

        # Aquí creamos una instancia de la ventana PaginaCarrito
        carrito_compras = PaginaCarrito()
        carrito_compras.cargar_productos_desde_csv('carrito.csv')  # Cargar productos desde el CSV

        # Agregamos la ventana PaginaCarrito al layout del QDialog
        layout.addWidget(carrito_compras)

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
