import sys
from PyQt6.QtWidgets import QApplication, QFileDialog, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QDialog, QFormLayout, QLineEdit, QMessageBox
import csv

class StockWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock de Productos")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: pink;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout principal
        self.layout = QHBoxLayout(self.central_widget)

        # Tabla de productos
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(7)  # Ajustar según el número de columnas en productos.csv
        self.layout.addWidget(self.table_widget)

        # Botones de acciones
        self.btn_agregar_nuevo = QPushButton("Agregar Producto Nuevo")
        self.btn_modificar_cantidad = QPushButton("Modificar cantidad")
        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_agregar_nuevo.clicked.connect(self.agregar_producto_nuevo)
        self.btn_modificar_cantidad.clicked.connect(self.modificar_cantidad)
        self.btn_eliminar.clicked.connect(self.eliminar_producto)

        # Layout para los botones
        self.button_layout = QVBoxLayout()
        self.button_layout.addWidget(self.btn_agregar_nuevo)
        self.button_layout.addWidget(self.btn_modificar_cantidad)
        self.button_layout.addWidget(self.btn_eliminar)
        self.layout.addLayout(self.button_layout)

        # Cargar productos desde CSV
        self.cargar_productos()

    def cargar_productos(self):
        try:
            with open('C:/Users/icede/OneDrive/Escritorio/tpa/productos.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                header = next(reader)  # Leer encabezados
                self.table_widget.setColumnCount(len(header))  # Ajustar el número de columnas
                self.table_widget.setHorizontalHeaderLabels(header)
                for row_idx, row in enumerate(reader):
                    self.table_widget.insertRow(row_idx)
                    for col_idx, col in enumerate(row):
                        item = QTableWidgetItem(col)
                        self.table_widget.setItem(row_idx, col_idx, item)
        except FileNotFoundError:
            print("No se encontró el archivo productos.csv")

    def agregar_producto_nuevo(self):
        dialog = NuevoProductoDialog()
        if dialog.exec():
            nuevo_producto = dialog.get_datos_producto()
            if nuevo_producto:
                # Añadir a la tabla
                row_idx = self.table_widget.rowCount()
                self.table_widget.insertRow(row_idx)
                for col_idx, dato in enumerate(nuevo_producto):
                    item = QTableWidgetItem(dato)
                    self.table_widget.setItem(row_idx, col_idx, item)
                QMessageBox.information(self, "Éxito", "Nuevo producto añadido exitosamente.")

                # Añadir al archivo CSV
                with open('productos.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(nuevo_producto)

    def modificar_cantidad(self):
        selected_row = self.table_widget.currentRow()
        if selected_row != -1:
            dialog = CantidadDialog("Modificar cantidad")
            if dialog.exec():
                nueva_cantidad = dialog.get_cantidad()
                self.table_widget.setItem(selected_row, 6, QTableWidgetItem(str(nueva_cantidad)))  # Suponiendo que la cantidad está en la columna 6
                QMessageBox.information(self, "Éxito", f"La cantidad del producto ha sido modificada a {nueva_cantidad}.")

                # Actualizar el archivo CSV
                productos = []
                with open('productos.csv', 'r', newline='') as file:
                    reader = csv.reader(file)
                    productos = list(reader)
                
                productos[selected_row + 1][6] = str(nueva_cantidad)  # +1 porque la primera fila es el encabezado
                
                with open('productos.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(productos)

    def eliminar_producto(self):
        selected_row = self.table_widget.currentRow()
        if selected_row != -1:
            # Eliminar la fila de la tabla
            self.table_widget.removeRow(selected_row)
            QMessageBox.information(self, "Éxito", "El producto ha sido eliminado exitosamente.")

            # Eliminar la fila correspondiente del archivo CSV
            productos = []
            with open('productos.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                productos = list(reader)
            
            del productos[selected_row + 1]  # +1 porque la primera fila es el encabezado
            
            with open('productos.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(productos)

class CantidadDialog(QDialog):
    def __init__(self, titulo):
        super().__init__()
        self.setWindowTitle(titulo)
        self.layout = QVBoxLayout()
        self.setStyleSheet("background-color: pink;")

        self.label = QLabel("Ingrese la cantidad:")
        self.layout.addWidget(self.label)

        self.cantidad_edit = QLineEdit()
        self.layout.addWidget(self.cantidad_edit)

        self.btn_aceptar = QPushButton("Aceptar")
        self.btn_aceptar.clicked.connect(self.accept)
        self.layout.addWidget(self.btn_aceptar)

        self.setLayout(self.layout)

    def get_cantidad(self):
        return int(self.cantidad_edit.text()) if self.cantidad_edit.text().isdigit() else 0

class PrecioDialog(QDialog):
    def __init__(self, titulo):
        super().__init__()
        self.setWindowTitle(titulo)
        self.layout = QVBoxLayout()

        self.label = QLabel("Ingrese el nuevo precio:")
        self.layout.addWidget(self.label)

        self.precio_edit = QLineEdit()
        self.layout.addWidget(self.precio_edit)

        self.btn_aceptar = QPushButton("Aceptar")
        self.btn_aceptar.clicked.connect(self.accept)
        self.layout.addWidget(self.btn_aceptar)

        self.setLayout(self.layout)

    def get_precio(self):
        return float(self.precio_edit.text()) if self.precio_edit.text().replace('.', '', 1).isdigit() else 0.0

class NuevoProductoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nuevo Producto")
        self.layout = QFormLayout()
        self.setStyleSheet("background-color: pink;")

        self.nombre_edit = QLineEdit()
        self.imagen_edit = QLineEdit()
        self.descripcion_edit = QLineEdit()
        self.tipo_animal_edit = QLineEdit()
        self.marca_edit = QLineEdit()
        self.tipo_edit = QLineEdit()
        self.cantidad_edit = QLineEdit()
        self.precio_edit = QLineEdit()

    # def seleccionArchivo(self):
    #     file_path,  = QFileDialog.getOpenFileName(self, 'Seleccionar archivo', '', 'Todos los archivos (*)')
    #     if file_path:
    #         self.imagen_edit.setText(file_path)

        self.layout.addRow("Nombre:", self.nombre_edit)
        self.layout.addRow("Imagen:", self.imagen_edit)
        self.layout.addRow("Descripción:", self.descripcion_edit)
        self.layout.addRow("Tipo de Animal:", self.tipo_animal_edit)
        self.layout.addRow("Marca:", self.marca_edit)
        self.layout.addRow("Tipo:", self.tipo_edit)
        self.layout.addRow("cantidad:", self.cantidad_edit)
        self.layout.addRow("Precio:", self.precio_edit)

        self.btn_aceptar = QPushButton("Aceptar")
        self.btn_aceptar.clicked.connect(self.accept)
        self.layout.addWidget(self.btn_aceptar)

        self.btn_selecimag = QPushButton("imagen")
        self.btn_selecimag.clicked.connect(self.seleccionArchivo)
        self.layout.addWidget(self.btn_selecimag)


        self.setLayout(self.layout)

    def seleccionArchivo(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Seleccionar archivo', '', 'Todos los archivos (*)')
        if file_path:
            self.imagen_edit.setText(file_path)

    def get_datos_producto(self):
        nombre = self.nombre_edit.text()
        imagen = self.imagen_edit.text()
        descripcion = self.descripcion_edit.text()
        tipo_animal = self.tipo_animal_edit.text()
        marca = self.marca_edit.text()
        tipo = self.tipo_edit.text()
        cantidad = self.cantidad_edit.text()
        precio = self.precio_edit.text()

        if all([nombre, imagen, descripcion, tipo_animal, marca, tipo, cantidad, precio]):
            return [nombre, imagen, descripcion, tipo_animal, marca, tipo, cantidad, precio]
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StockWindow()
    window.show()
    sys.exit(app.exec())
