import sys
import csv
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea, QHBoxLayout, QDialog, QSpinBox
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QIcon

class VentanaProducto(QDialog):
    def __init__(self, nombre_producto, imagen_producto, descripcion_producto, agregar_callback):
        super().__init__()
        self.setWindowTitle(nombre_producto)
        self.setGeometry(150, 150, 600, 400)
        self.setStyleSheet("background-color: pink;")

        self.agregar_callback = agregar_callback

        # Layout principal
        layout_principal = QVBoxLayout(self)

        # Imagen del producto
        etiqueta_imagen = QLabel(self)
        pixmap = QPixmap(imagen_producto)
        etiqueta_imagen.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))
        layout_principal.addWidget(etiqueta_imagen)

        # Descripción del producto
        etiqueta_descripcion = QLabel(descripcion_producto, self)
        etiqueta_descripcion.setStyleSheet(
            "font-size: 18px; "
            "margin: 10px;"
        )
        layout_principal.addWidget(etiqueta_descripcion)

        # Cantidad y botón de agregar al carrito
        layout_cantidad = QHBoxLayout()

        etiqueta_cantidad = QLabel("Cantidad: ", self)
        etiqueta_cantidad.setStyleSheet("font-size: 18px;")
        layout_cantidad.addWidget(etiqueta_cantidad)

        self.spinbox_cantidad = QSpinBox(self)
        self.spinbox_cantidad.setRange(1, 100)
        self.spinbox_cantidad.setValue(1)
        layout_cantidad.addWidget(self.spinbox_cantidad)

        boton_agregar_carrito = QPushButton("Agregar al carrito", self)
        boton_agregar_carrito.setStyleSheet("font-size: 18px;")
        boton_agregar_carrito.clicked.connect(self.agregar_al_carrito)
        layout_cantidad.addWidget(boton_agregar_carrito)

        layout_principal.addLayout(layout_cantidad)

    def agregar_al_carrito(self):
        cantidad = self.spinbox_cantidad.value()
        self.agregar_callback(self.windowTitle(), cantidad)
        self.accept()

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alimentos")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: pink;")

        self.carrito = []

        # Widget central
        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        # Layout principal
        layout_principal = QVBoxLayout(widget_central)

        # Título
        etiqueta_titulo = QLabel("Alimentos")
        etiqueta_titulo.setAlignment(Qt.AlignmentFlag.AlignLeft)
        etiqueta_titulo.setStyleSheet(
            "font-size: 24px; "
            "font-weight: bold; "
            "margin: 10px;"
        )
        layout_principal.addWidget(etiqueta_titulo)

        # Área de scroll para los botones
        area_scroll = QScrollArea()
        area_scroll.setWidgetResizable(True)

        contenido_scroll = QWidget()
        layout_scroll = QHBoxLayout(contenido_scroll)
        layout_scroll.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Cargar productos desde CSV
        self.productos = self.cargar_productos()

        # Crear y estilizar botones
        for producto in self.productos:
            icon = QIcon(QPixmap(producto['imagen']))
            boton = QPushButton()
            boton.setIcon(icon)
            boton.setIconSize(QSize(272, 272))  # Ajusta el tamaño del icono para que se ajuste al tamaño del botón
            boton.setFixedSize(272, 272)
            boton.setStyleSheet("font-size: 18px;")
            boton.clicked.connect(lambda checked, p=producto: self.abrir_ventana_producto(p))
            layout_scroll.addWidget(boton)

        area_scroll.setWidget(contenido_scroll)
        layout_principal.addWidget(area_scroll)

    def cargar_productos(self):
        productos = []
        with open('productos.csv', mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if(row[6] == "comida"):
                    productos.append(row)
        return productos

    def abrir_ventana_producto(self, producto):
        ventana_producto = VentanaProducto(producto["nombre"], producto["imagen"], producto["descripcion", producto["tipo"]], self.agregar_al_carrito)
        ventana_producto.exec()

    def agregar_al_carrito(self, nombre_producto, cantidad):
        self.carrito.append((nombre_producto, cantidad))
        print(f"Agregado {cantidad} de {nombre_producto} al carrito")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
