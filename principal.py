import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QDockWidget, QDialog
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

        self.dock_widget = QDockWidget("DockWidget", self)
        self.ui_dock_widget = Ui_DockWidget()
        self.ui_dock_widget.setupUi(self.dock_widget)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.RightDockWidgetArea, self.dock_widget)

        self.ui_dock_widget.AdopcionButton.clicked.connect(self.abrir_ventana_adopcion)
        self.ui_dock_widget.AlimentosButton.clicked.connect(self.abrir_ventana_comida)
        self.ui_dock_widget.JuguetesButton.clicked.connect(self.abrir_ventana_juguetes)
        self.ui_dock_widget.AccesorioButtom.clicked.connect(lambda: self.abrir_ventana_accesorios(None))

        self.inicializar_archivo_csv()

    def inicializar_archivo_csv(self):
        try:
            with open("registro.csv", mode='x', newline='') as file:
                escritor_csv = csv.writer(file)
                escritor_csv.writerow(["Fecha", "Operación", "Detalles"])
        except FileExistsError:
            pass

    def registrar_operacion(self, operacion, detalles):
        with open("registro.csv", "a", newline='') as file:
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
            juguete = dialog_juguetes.juguetes_combo_box.currentText()
            detalles = f"Tipo de animal: {tipo_animal}, Juguete: {juguete}"
            self.registrar_operacion("Compra de juguete", detalles)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = MainApp()
    mainApp.show()
    sys.exit(app.exec())