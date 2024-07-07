import sys
import csv
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QScrollArea, QPushButton, QApplication

class PaginaCarrito(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(300, 300, 800, 500)  # Declaramos el tamaño de la ventana
        self.setWindowTitle("Carro")  # Declaramos el nombre de la ventana

        # Crear el widget central
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: pink;")
        self.setCentralWidget(central_widget)

        # Sistema de layout para el estilo de la ventana
        layout_principal = QHBoxLayout()

        # Layouts que estarán dentro de layout_principal en orden de izquierda a derecha => |dato de compras|dato de tarjeta|
        layout_dato_de_copra = QVBoxLayout()
        layout_dato_de_tarjeta = QVBoxLayout()

        # Agregamos los layouts como segunda capa al layout principal
        layout_principal.addLayout(layout_dato_de_copra)
        layout_principal.addLayout(layout_dato_de_tarjeta)

        # Etiquetas (layout_dato_de_copra)
        tarjeta_datos_de_compra = QLabel("Datos de compra:", self)
        tarjeta_datos_de_compra.setStyleSheet("color: black;")
        layout_dato_de_copra.addWidget(tarjeta_datos_de_compra)

        # Botones y entrada de texto (layout_dato_de_compra)
        # Scroll area para mostrar productos
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_widget = QWidget()
        self.scroll_area_widget.setStyleSheet("background-color: pink;")
        self.scroll_area_layout = QVBoxLayout(self.scroll_area_widget)
        self.scroll_area.setWidget(self.scroll_area_widget)
        layout_dato_de_copra.addWidget(self.scroll_area)

        # Etiquetas (layout_dato_de_tarjeta)
        tarjeta_ingrese_DDT = QLabel("Ingrese datos de su tarjeta", self)
        tarjeta_ingrese_DDT.setStyleSheet("color: black;")
        layout_dato_de_tarjeta.addWidget(tarjeta_ingrese_DDT)

        # Botones y entrada de texto (layout_dato_de_tarjeta)
        self.entrada_N_tarjeta = QLineEdit()
        self.entrada_N_tarjeta.setPlaceholderText("Número de tarjeta")
        self.entrada_N_tarjeta.setStyleSheet("color: black;")
        layout_dato_de_tarjeta.addWidget(self.entrada_N_tarjeta)

        self.entrada_Fecha_tarjeta = QLineEdit()
        self.entrada_Fecha_tarjeta.setPlaceholderText("Fecha de expiración")
        self.entrada_Fecha_tarjeta.setStyleSheet("color: black;")
        layout_dato_de_tarjeta.addWidget(self.entrada_Fecha_tarjeta)

        self.entrada_dijito_vereficador = QLineEdit()
        self.entrada_dijito_vereficador.setPlaceholderText("Dígito verificador")
        self.entrada_dijito_vereficador.setStyleSheet("color: black;")
        layout_dato_de_tarjeta.addWidget(self.entrada_dijito_vereficador)

        # Botón para pagar
        self.boton_pagar = QPushButton("Pagar")
        self.boton_pagar.setStyleSheet("background-color: pink; color: black;")
        self.boton_pagar.clicked.connect(self.guardar_numero_tarjeta)
        layout_dato_de_tarjeta.addWidget(self.boton_pagar)

        # Etiqueta para mostrar el número de tarjeta guardado
        self.etiqueta_resultado = QLabel('')
        self.etiqueta_resultado.setStyleSheet("color: black;")
        layout_dato_de_tarjeta.addWidget(self.etiqueta_resultado)

        # Establecer el layout principal en el widget central
        central_widget.setLayout(layout_principal)

        # Llenar el scroll area con los productos del archivo CSV
        self.cargar_productos_desde_csv('carrito.csv')

    def cargar_productos_desde_csv(self, archivo_csv):
        try:
            with open(archivo_csv, mode='r', newline='') as file:
                csv_leector = csv.reader(file)
                next(csv_leector)  # Saltar el encabezado
                total_pagar = 0

                for row in csv_leector:
                    nombre = row[0].strip()
                    cantidad = int(row[1].strip())
                    precio = float(row[2].strip())
                    producto = QLabel(f"Nombre: {nombre}, Cantidad: {cantidad}, Precio: {precio}", self.scroll_area_widget)
                    producto.setStyleSheet("color: black;")
                    self.scroll_area_layout.addWidget(producto)
                    total_pagar += precio * cantidad  # Aquí se suma el precio total de los productos añadidos a la lista

                # Mostrar el total a pagar
                total_label = QLabel(f"Total a pagar: {total_pagar}", self.scroll_area_widget)
                total_label.setStyleSheet("color: black;")
                self.scroll_area_layout.addWidget(total_label)

        except FileNotFoundError:
            error_label = QLabel("Archivo CSV no encontrado.", self.scroll_area_widget)
            error_label.setStyleSheet("color: black;")
            self.scroll_area_layout.addWidget(error_label)

    def guardar_numero_tarjeta(self):
        # Guardar el texto del QLineEdit en una variable
        numero_tarjeta = self.entrada_N_tarjeta.text()
        # Mostrar si la tarjeta fue o no verificada con exito
        if self.algoritmo_de_Luhn(numero_tarjeta):
            self.etiqueta_resultado.setText("Tarjeta verificada con éxito")
        else:
            self.etiqueta_resultado.setText("Tarjeta no verificada")

    def algoritmo_de_Luhn(self, numero_tarjeta):
        # Convertir el número de tarjeta a una lista de digitos
        digitos = [int(caracter) for caracter in str(numero_tarjeta)] # convertimos cada caracter en digito entero
        # multiplicamos cada segunto termino de derecha a izquierda
        for i in range(len(digitos)-2,-1,-2):
            digitos[i] *= 2
            if digitos[i] > 9: # si el digito que se a multiplicado por dos es mayor a 9 se le resta 9
                digitos[i] -= 9
        
        # sumamos todos los digitos de la lista con la funcion suma --> sum(lista_de_elementos)
        suma_total = sum(digitos)

        return suma_total % 10 == 0 # si la sima total es igual a cero significa que la tarjeta es valida