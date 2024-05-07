from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QMessageBox

class Adopcion:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

class TiendaMascotas:
    def __init__(self):
        self.perros_rescatados = [Adopcion("Max", "2 años", "Labrador"), Adopcion("Luna", "3 años", "Poodle")]
        self.gatos_rescatados = [Adopcion("Simba", "1 año", "Siamés"), Adopcion("Nala", "2 años", "Persa")]

    def obtener_perros_disponibles(self):
        return self.perros_rescatados

    def obtener_gatos_disponibles(self):
        return self.gatos_rescatados

class VentanaMascotas(QDialog):
    def __init__(self, tienda, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Mascotas Disponibles")
        self.setFixedSize(500, 500)

        self.layout = QVBoxLayout()  

        self.tienda = tienda

        self.actualizar_mascotas_disponibles()

    def actualizar_mascotas_disponibles(self):
        # Limpiar el layout antes de agregar nuevos widgets
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Obtener perros y gatos disponibles
        perros = self.tienda.obtener_perros_disponibles()
        gatos = self.tienda.obtener_gatos_disponibles()

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
    def __init__(self, tienda, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Formulario de adopción")
        self.setFixedSize(500, 500)

        layout = QVBoxLayout()

        # Campos para ingresar información
        layout.addWidget(QLabel("Nombre:"))
        self.nombre_edit = QLineEdit()
        layout.addWidget(self.nombre_edit)

        layout.addWidget(QLabel("Edad:"))
        self.edad_edit = QLineEdit()
        layout.addWidget(self.edad_edit)

        layout.addWidget(QLabel("Correo electrónico:"))
        self.correo_edit = QLineEdit()
        layout.addWidget(self.correo_edit)

        layout.addWidget(QLabel("Nombre de mascota interesada:"))
        self.nombremascota_edit = QLineEdit()
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
        # Obtener el texto de los campos
        nombre = self.nombre_edit.text().strip()
        edad = self.edad_edit.text().strip()
        correo = self.correo_edit.text().strip()
        nombremascota = self.nombremascota_edit.text().strip()
        genero = self.genero_combo_box.currentText()

        # Verificar si algún campo está vacío
        if not nombre or not edad or not correo or not nombremascota:
            # Mostrar un mensaje de advertencia
            QMessageBox.warning(self, "Campos vacíos", "Por favor, llene todos los campos.")
            return
        
        # Mostrar la ventana de mensaje
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Información guardada")
        mensaje.setText("¡Tu información ha sido guardada! Nos pondremos en contacto contigo.")
        mensaje.setIcon(QMessageBox.Icon.Information)
        mensaje.exec_()
