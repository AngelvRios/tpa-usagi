import sys
import csv
from PyQt6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QLabel, QComboBox, QDialogButtonBox, 
    QWidget, QScrollArea, QPushButton, QSpinBox
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

        # ComboBox para seleccionar el tipo de juguete
        etiqueta_tipo_juguete = QLabel("Tipo de juguete:")
        etiqueta_tipo_juguete.setStyleSheet("font-size: 18px; margin: 10px;")
        layout_principal.addWidget(etiqueta_tipo_juguete)

        self.juguete_combo_box = QComboBox()
        self.juguete_combo_box.addItems(["Pelota", "Cuerda", "Peluche", "Mordedor", "Lanzador"])
        self.juguete_combo_box.currentIndexChanged.connect(self.actualizar_juguetes)
        layout_principal.addWidget(self.juguete_combo_box)

        # Área de scroll para los botones de juguetes
        self.area_scroll = QScrollArea()
        self.area_scroll.setWidgetResizable(True)

        self.contenido_scroll = QWidget()
        self.layout_scroll = QVBoxLayout(self.contenido_scroll)
        self.layout_scroll.setAlignment(Qt.AlignmentFlag.AlignTop)

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

        # Inicializar lista de juguetes
        self.actualizar_juguetes()

    def actualizar_juguetes(self):
        tipo_juguete = self.juguete_combo_box.currentText()

        # Limpiar layout anterior
        for i in reversed(range(self.layout_scroll.count())):
            widget = self.layout_scroll.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Cargar juguetes para el tipo de juguete seleccionado
        productos = self.cargar_productos(tipo_juguete)
        for producto in productos:
            # Crear widget para cada juguete
            widget_juguete = QWidget()
            layout_juguete = QVBoxLayout(widget_juguete)

            icon = QIcon(QPixmap(producto['imagen']))
            boton = QPushButton()
            boton.setIcon(icon)
            boton.setIconSize(QSize(272, 272))  # Ajusta el tamaño del icono para que se ajuste al tamaño del botón
            boton.setFixedSize(272, 272)
            boton.setStyleSheet("font-size: 18px;")

            etiqueta_precio = QLabel(f"${producto['precio']}")
            etiqueta_precio.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_juguete.addWidget(etiqueta_precio)
            layout_juguete.addWidget(boton)

            # Conectar clic del botón con selección de juguete
            boton.clicked.connect(lambda checked, p=producto: self.seleccionar_juguete(p))

            self.layout_scroll.addWidget(widget_juguete)

    def cargar_productos(self, tipo_juguete):
        productos = []
        with open('productos.csv', mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['tipo'] == "juguete" and row['nombre'] == tipo_juguete:
                    productos.append(row)
        return productos

    def seleccionar_juguete(self, juguete):
        self.juguete_seleccionado = juguete
        print(f"Juguete seleccionado: {juguete}")

    def get_juguete_seleccionado(self):
        return self.juguete_seleccionado, self.cantidad_spin_box.value()

    def agregar_al_carrito(self, nombre_producto, cantidad, precio):
        with open('carrito.csv', mode='a', newline='', encoding='utf-8') as file:
            escritor = csv.writer(file)
            escritor.writerow([nombre_producto, cantidad, precio])
        print(f"Agregado {cantidad} de {nombre_producto} al carrito")

    def accept(self):
        if self.juguete_seleccionado is not None:
            juguete, cantidad = self.get_juguete_seleccionado()
            precio = self.juguete_seleccionado['precio']  # Asumiendo que 'precio' está en tu CSV
            self.agregar_al_carrito(juguete['nombre'], cantidad, precio)
        super().accept()

    def reject(self):
        super().reject()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = SeleccionarJugueteDialog()
    if dialogo.exec() == QDialog.DialogCode.Accepted:
        juguete, cantidad = dialogo.get_juguete_seleccionado()
        print(f"Juguete: {juguete}")
        print(f"Cantidad: {cantidad}")
    sys.exit(app.exec())
