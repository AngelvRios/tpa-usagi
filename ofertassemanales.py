import sys
import random
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem

class OfertasSemanales(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ofertas Semanales")
        self.setGeometry(100, 100, 1200, 600)
        self.setStyleSheet("background-color:pink")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout(self.central_widget)

        # Tabla de productos
        self.table_productos = QTableWidget()
        self.table_productos.setColumnCount(7)  # Ajustar según el número de columnas en productos.csv
        self.layout.addWidget(self.table_productos)

        # Botones de acciones
        self.btn_agregar = QPushButton("Agregar a Ofertas")
        self.btn_agregar.clicked.connect(self.agregar_a_ofertas)
        self.layout.addWidget(self.btn_agregar)

        self.btn_eliminar = QPushButton("Eliminar Oferta")
        self.btn_eliminar.clicked.connect(self.eliminar_oferta)
        self.layout.addWidget(self.btn_eliminar)

        # Tabla de ofertas
        self.table_ofertas = QTableWidget()
        self.table_ofertas.setColumnCount(7)  # Ajustar según el número de columnas en ofertas.csv
        self.layout.addWidget(self.table_ofertas)

        # Cargar productos desde CSV
        self.cargar_productos()
        
        # Cargar ofertas desde CSV
        self.cargar_ofertas()

    def cargar_productos(self):
        try:
            with open('productos.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                header = next(reader)  # Leer encabezados
                self.table_productos.setColumnCount(len(header))  # Ajustar el número de columnas
                self.table_productos.setHorizontalHeaderLabels(header)
                for row_idx, row in enumerate(reader):
                    self.table_productos.insertRow(row_idx)
                    for col_idx, col in enumerate(row):
                        item = QTableWidgetItem(col)
                        self.table_productos.setItem(row_idx, col_idx, item)
        except FileNotFoundError:
            print("No se encontró el archivo productos.csv")

    def cargar_ofertas(self):
        try:
            with open('ofertas.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                header = next(reader)  # Leer encabezados
                self.table_ofertas.setColumnCount(len(header))  # Ajustar el número de columnas
                self.table_ofertas.setHorizontalHeaderLabels(header)
                for row_idx, row in enumerate(reader):
                    self.table_ofertas.insertRow(row_idx)
                    for col_idx, col in enumerate(row):
                        item = QTableWidgetItem(col)
                        self.table_ofertas.setItem(row_idx, col_idx, item)
        except FileNotFoundError:
            print("No se encontró el archivo ofertas.csv")

    def agregar_a_ofertas(self):
        selected_row = self.table_productos.currentRow()
        if selected_row != -1:
            # Obtener los datos del producto seleccionado
            producto = []
            for col_idx in range(self.table_productos.columnCount()):
                producto.append(self.table_productos.item(selected_row, col_idx).text())

            # Generar descuento aleatorio entre 10% y 50%
            descuento = random.randint(10, 50)  # Descuento entero entre 10 y 50%
            descuento_decimal = descuento / 100.0  # Convertir a decimal para cálculos
            precio_original = int(producto[7])  # Obtener el precio original desde el producto seleccionado
            precio_con_descuento = precio_original * (1 - descuento_decimal)
            precio_formateado = "{:.2f}".format(precio_con_descuento).rstrip('0').rstrip('.')

            # Modificar el precio en el producto para la tabla de ofertas
            producto[7] = str(precio_formateado)  # Actualizar el precio con descuento

            # Agregar el producto a la tabla de ofertas
            row_count = self.table_ofertas.rowCount()
            self.table_ofertas.insertRow(row_count)
            for col_idx, col_value in enumerate(producto):
                item = QTableWidgetItem(col_value)
                self.table_ofertas.setItem(row_count, col_idx, item)

            # Guardar en ofertas.csv (opcional)
            with open('ofertas.csv', mode='a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(producto)

    def eliminar_oferta(self):
        selected_row = self.table_ofertas.currentRow()
        if selected_row != -1:
            self.table_ofertas.removeRow(selected_row)
            self.actualizar_csv_ofertas()

    def actualizar_csv_ofertas(self):
        # Guardar los datos actualizados de la tabla de ofertas en ofertas.csv
        with open('ofertas.csv', mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            header = [self.table_ofertas.horizontalHeaderItem(col).text() for col in range(self.table_ofertas.columnCount())]
            writer.writerow(header)
            for row in range(self.table_ofertas.rowCount()):
                row_data = []
                for col in range(self.table_ofertas.columnCount()):
                    item = self.table_ofertas.item(row, col)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                writer.writerow(row_data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_ofertas = OfertasSemanales()
    ventana_ofertas.show()
    sys.exit(app.exec())
