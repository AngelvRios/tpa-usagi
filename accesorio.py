import sys
import csv
from PyQt6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QLabel, QComboBox, QDialogButtonBox, 
    QWidget, QScrollArea, QHBoxLayout, QPushButton, QSpinBox
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QIcon

class SeleccionarAccesorioDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar Accesorio")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: pink;")

        self.accesorio_seleccionado = None

        # Layout principal
        layout_principal = QVBoxLayout(self)

        # ComboBox para seleccionar el tipo de accesorio
        etiqueta_tipo_accesorio = QLabel("Tipo de accesorio:")
        etiqueta_tipo_accesorio.setStyleSheet("font-size: 18px; margin: 10px;")
        layout_principal.addWidget(etiqueta_tipo_accesorio)

        self.accesorio_combo_box = QComboBox()
        self.accesorio_combo_box.addItems(["Collar", "Correa", "Cama", "Transportadora", "Rascador"])
        self.accesorio_combo_box.currentIndexChanged.connect(self.actualizar_accesorios)
        layout_principal.addWidget(self.accesorio_combo_box)

        # Área de scroll para los botones de accesorios
        self.area_scroll = QScrollArea()
        self.area_scroll.setWidgetResizable(True)

        self.contenido_scroll = QWidget()
        self.layout_scroll = QHBoxLayout(self.contenido_scroll)
        self.layout_scroll.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.area_scroll.setWidget(self.contenido_scroll)
        layout_principal.addWidget(self.area_scroll)

        # SpinBox para seleccionar la cantidad
        etiqueta_cantidad = QLabel("Cantidad:")
        etiqueta_cantidad.setStyleSheet("font-size: 18px; margin: 10px;")
        layout_principal.addWidget(etiqueta_cantidad)

        self.cantidad_spin_box = QSpinBox()
        self.cantidad_spin_box.setMinimum(1)
        self.cantidad_spin_box.setMaximum(100)
        layout_principal.addWidget(self.cantidad_spin_box)

        # Botones de aceptar y cancelar
        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        layout_principal.addWidget(botones)

        # Establecer el layout principal para la ventana
        self.setLayout(layout_principal)

        # Inicializar lista de accesorios
        self.actualizar_accesorios()

    def actualizar_accesorios(self):
        tipo_accesorio = self.accesorio_combo_box.currentText()

        # Limpiar layout anterior
        for i in reversed(range(self.layout_scroll.count())):
            widget = self.layout_scroll.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Cargar accesorios para el tipo de accesorio seleccionado
        productos = self.cargar_productos(tipo_accesorio)
        for producto in productos:
            icon = QIcon(QPixmap(producto['imagen']))
            boton = QPushButton()
            boton.setIcon(icon)
            boton.setIconSize(QSize(272, 272))  # Ajusta el tamaño del icono para que se ajuste al tamaño del botón
            boton.setFixedSize(272, 272)
            boton.setStyleSheet("font-size: 18px;")
            boton.clicked.connect(lambda checked, p=producto: self.seleccionar_accesorio(p))
            self.layout_scroll.addWidget(boton)

        # Verificación para asegurar que se están creando los botones
        if not productos:
            print(f"No se encontraron productos para el tipo de accesorio: {tipo_accesorio}")
        else:
            print(f"Se encontraron {len(productos)} productos para el tipo de accesorio: {tipo_accesorio}")

    def cargar_productos(self, tipo_accesorio):
        productos = []
        with open('productos.csv', mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['tipo'] == "accesorio" and row['nombre'] == tipo_accesorio:
                    productos.append(row)
        return productos

    def seleccionar_accesorio(self, accesorio):
        self.accesorio_seleccionado = accesorio
        print(f"Accesorio seleccionado: {accesorio}")

    def get_accesorio_seleccionado(self):
        return self.accesorio_seleccionado, self.cantidad_spin_box.value()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = SeleccionarAccesorioDialog()
    if dialogo.exec() == QDialog.DialogCode.Accepted:
        accesorio, cantidad = dialogo.get_accesorio_seleccionado()
        print(f"Accesorio: {accesorio}")
        print(f"Cantidad: {cantidad}")
    sys.exit(app.exec())

