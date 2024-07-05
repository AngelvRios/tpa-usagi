import sys
import csv
from PyQt6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QLabel, QComboBox, QDialogButtonBox, 
    QWidget, QScrollArea, QHBoxLayout, QPushButton
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QIcon

class SeleccionarJugueteDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar Juguete")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: pink;")

        self.juguete_seleccionado = None

        # Layout principal
        layout_principal = QVBoxLayout(self)

        # ComboBox para seleccionar el tipo de animal
        etiqueta_tipo_animal = QLabel("Tipo de animal:")
        etiqueta_tipo_animal.setStyleSheet("font-size: 18px; margin: 10px;")
        layout_principal.addWidget(etiqueta_tipo_animal)

        self.tipo_combo_box = QComboBox(self)
        self.tipo_combo_box.addItems(["Perro", "Gato", "Conejo", "Roedores"])
        self.tipo_combo_box.currentIndexChanged.connect(self.actualizar_juguetes)
        layout_principal.addWidget(self.tipo_combo_box)

        # Área de scroll para los botones
        self.area_scroll = QScrollArea()
        self.area_scroll.setWidgetResizable(True)

        self.contenido_scroll = QWidget()
        self.layout_scroll = QHBoxLayout(self.contenido_scroll)
        self.layout_scroll.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.area_scroll.setWidget(self.contenido_scroll)
        layout_principal.addWidget(self.area_scroll)

        # Botones de aceptar y cancelar
        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        layout_principal.addWidget(botones)

        # Establecer el layout principal para la ventana
        self.setLayout(layout_principal)

        # Inicializar lista de juguetes
        self.actualizar_juguetes()

    def actualizar_juguetes(self):
        tipo_animal = self.tipo_combo_box.currentText()

        # Limpiar layout anterior
        for i in reversed(range(self.layout_scroll.count())):
            widget = self.layout_scroll.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Cargar juguetes para el tipo de animal seleccionado
        productos = self.cargar_productos(tipo_animal)
        for producto in productos:
            icon = QIcon(QPixmap(producto['imagen']))
            boton = QPushButton()
            boton.setIcon(icon)
            boton.setIconSize(QSize(272, 272))  # Ajusta el tamaño del icono para que se ajuste al tamaño del botón
            boton.setFixedSize(272, 272)
            boton.setStyleSheet("font-size: 18px;")
            boton.clicked.connect(lambda checked, p=producto: self.seleccionar_juguete(p))
            self.layout_scroll.addWidget(boton)

    def cargar_productos(self, tipo_animal):
        productos = []
        with open('productos.csv', mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['tipo'] == "juguete" and row['tipo_animal'] == tipo_animal:
                    productos.append(row)
        return productos

    def seleccionar_juguete(self, juguete):
        self.juguete_seleccionado = juguete
        print(f"Juguete seleccionado: {juguete}")

    def get_juguete_seleccionado(self):
        tipo_animal = self.tipo_combo_box.currentText()
        return tipo_animal, self.juguete_seleccionado

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = SeleccionarJugueteDialog()
    if dialogo.exec() == QDialog.DialogCode.Accepted:
        tipo_animal, juguete = dialogo.get_juguete_seleccionado()
        print(f"Tipo de animal: {tipo_animal}")
        print(f"Juguete: {juguete}")
    sys.exit(app.exec())
