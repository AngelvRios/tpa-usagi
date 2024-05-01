from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget, QDialog, QVBoxLayout, QComboBox, QLineEdit, QMessageBox

class adopcion:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

class TiendaMascotas:
    def __init__(self):
        self.perros_rescatados = []
        self.gatos_rescatados = []

    def adoptar_perro(self, nombre, edad, raza):
        perro = adopcion(nombre, edad, raza)
        self.perros_rescatados.append(perro)

    def adoptar_gato(self, nombre, edad, raza):
        gato = adopcion(nombre, edad, raza)
        self.gatos_rescatados.append(gato)

    def obtener_perros_disponibles(self):
        return self.perros_rescatados

    def obtener_gatos_disponibles(self):
        return self.gatos_rescatados

class VentanaPrincipal(QMainWindow):
    def __init__(self, tienda):
        super().__init__()
        self.tienda = tienda
        self.ventana_mascotas = None  # Inicializa la ventana de mascotas 

        self.setWindowTitle("Tienda para mascotas")
        self.setFixedSize(400, 200)

        layout = QVBoxLayout()

        # Botón para mostrar mascotas disponibles
        btn_mostrar_mascotas = QPushButton("Mostrar mascotas disponibles")
        btn_mostrar_mascotas.clicked.connect(self.mostrar_mascotas)
        layout.addWidget(btn_mostrar_mascotas)

        # Botón para abrir ventana de adopción
        btn_adopcion = QPushButton("Adoptar")
        btn_adopcion.clicked.connect(self.abrir_ventana_adopcion)
        layout.addWidget(btn_adopcion)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def mostrar_mascotas(self):
        if not self.ventana_mascotas:
            self.ventana_mascotas = VentanaMascotas(self.tienda)
        self.ventana_mascotas.show()

    def abrir_ventana_adopcion(self):
        ventana_adopcion = VentanaAdopcion(self.tienda)
        ventana_adopcion.exec()

class VentanaMascotas(QDialog):
    def __init__(self, tienda, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Mascotas Disponibles")
        self.setFixedSize(500, 500)

        self.layout = QVBoxLayout()  

        #  perros y gatos disponibles
        perros = tienda.obtener_perros_disponibles()
        gatos = tienda.obtener_gatos_disponibles()

        # Mostrar perros disponibles
        self.layout.addWidget(QLabel("Perros disponibles para adopción:"))
        for perro in perros:
            perro_info = QLabel(f"Nombre: {perro.nombre}, Edad: {perro.edad}, Raza: {perro.raza}")
            self.layout.addWidget(perro_info)

        # Mostrar gatos disponibles
        self.layout.addWidget(QLabel("Gatos disponibles para adopción:"))
        for gato in gatos:
            gato_info = QLabel(f"Nombre: {gato.nombre}, Edad: {gato.edad}, Raza: {gato.raza}")
            self.layout.addWidget(gato_info)

        self.setLayout(self.layout)  

class VentanaAdopcion(QDialog):
    def __init__(self, tienda, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Formulario de adopción")
        self.setFixedSize(500, 500)

        layout = QVBoxLayout()

        # Campos para ingresar información
        self.nombre_edit = QLineEdit()
        layout.addWidget(QLabel("Nombre:"))
        layout.addWidget(self.nombre_edit)

        self.edad_edit = QLineEdit()
        layout.addWidget(QLabel("Edad:"))
        layout.addWidget(self.edad_edit)

        self.correo_edit = QLineEdit()
        layout.addWidget(QLabel("Correo electrónico:"))
        layout.addWidget(self.correo_edit)

        self.nombremascota_edit = QLineEdit()
        layout.addWidget(QLabel("Nombre de mascota interesada:"))
        layout.addWidget(self.nombremascota_edit)

        genero = ["Femenino", "Masculino", "Otro"]
        self.genero_combo_box = QComboBox()
        self.genero_combo_box.addItems(genero)
        layout.addWidget(QLabel("Género:"))
        layout.addWidget(self.genero_combo_box)

        # Botón de aceptar
        btn_aceptar = QPushButton("Aceptar")
        btn_aceptar.clicked.connect(self.guardar_adopcion)
        layout.addWidget(btn_aceptar)

        self.setLayout(layout)

        self.tienda = tienda

    def guardar_adopcion(self):
        nombre = self.nombre_edit.text()
        edad = self.edad_edit.text()
        correo = self.correo_edit.text()
        genero = self.genero_combo_box.currentText()


        # Mostrar la ventana de mensaje
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Información guardada")
        mensaje.setText("¡Tu información ha sido guardada! Nos pondremos en contacto contigo.")
        mensaje.setIcon(QMessageBox.Icon.Information)  # Aquí está el cambio
        mensaje.exec()

# Ejemplo de uso
tienda = TiendaMascotas()

# Agregar algunos perros y gatos rescatados
tienda.adoptar_perro("corxea", "3 años", "Labrador Retriever")
tienda.adoptar_perro("perejil","2 años" , "desconocido")
tienda.adoptar_gato("wisin", "1 años", "negro")
tienda.adoptar_gato("yandel", "4 años", "naranjo")

if __name__ == "__main__":
    app = QApplication([])
    ventana_principal = VentanaPrincipal(tienda)
    ventana_principal.show()
    app.exec()
