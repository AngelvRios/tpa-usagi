import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QDialog, QFormLayout, QLineEdit, QMessageBox
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
        self.btn_agregar = QPushButton("Agregar")
        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_agregar.clicked.connect(self.agregar_producto)
        self.btn_eliminar.clicked.connect(self.eliminar_producto)

        # Layout para los botones
        self.button_layout = QVBoxLayout()
        self.button_layout.addWidget(self.btn_agregar)
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
                    # Añadir columna para la cantidad
                    cantidad_item = QTableWidgetItem("0")
                    self.table_widget.setItem(row_idx, len(header), cantidad_item)  # Última columna para cantidad
        except FileNotFoundError:
            print("No se encontró el archivo productos.csv")

    def agregar_producto(self):
        selected_row = self.table_widget.currentRow()
        if selected_row != -1:
            dialog = CantidadDialog("Agregar Producto")
            if dialog.exec():
                cantidad = dialog.get_cantidad()
                # Actualizar la cantidad en la tabla
                cantidad_actual = int(self.table_widget.item(selected_row, self.table_widget.columnCount() - 1).text())
                nueva_cantidad = cantidad_actual + cantidad
                self.table_widget.item(selected_row, self.table_widget.columnCount() - 1).setText(str(nueva_cantidad))
                QMessageBox.information(self, "Éxito", f"Se han agregado {cantidad} unidades del producto.")

    def eliminar_producto(self):
        selected_row = self.table_widget.currentRow()
        if selected_row != -1:
            dialog = CantidadDialog("Eliminar Producto")
            if dialog.exec():
                cantidad = dialog.get_cantidad()
                # Actualizar la cantidad en la tabla
                cantidad_actual = int(self.table_widget.item(selected_row, self.table_widget.columnCount() - 1).text())
                if cantidad <= cantidad_actual:
                    nueva_cantidad = cantidad_actual - cantidad
                    self.table_widget.item(selected_row, self.table_widget.columnCount() - 1).setText(str(nueva_cantidad))
                    QMessageBox.information(self, "Éxito", f"Se han eliminado {cantidad} unidades del producto.")
                else:
                    QMessageBox.warning(self, "Error", "No se puede eliminar más unidades de las disponibles.")

class CantidadDialog(QDialog):
    def __init__(self, titulo):
        super().__init__()
        self.setWindowTitle(titulo)
        self.layout = QVBoxLayout()

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StockWindow()
    window.show()
    sys.exit(app.exec())
