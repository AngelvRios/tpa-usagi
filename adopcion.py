from PyQt6.QtWidgets import (
    QApplication, QDialog, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, QComboBox, QMessageBox
)
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore, QtGui
import csv
import sys

class VentanaAdopcion(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Formulario de adopción")
        self.setGeometry(600, 600, 900, 900)
        self.setMinimumSize(800, 600)
        self.setMaximumSize(1000, 800)

        layout = QVBoxLayout(self)

        self.nombre_edit = QLineEdit(self)
        self.nombre_edit.setPlaceholderText("Nombre")
        layout.addWidget(self.nombre_edit)

        self.edad_edit = QLineEdit(self)
        self.edad_edit.setPlaceholderText("Edad")
        self.edad_edit.setValidator(QtGui.QIntValidator(0, 150, self))  # Solo acepta números
        layout.addWidget(self.edad_edit)

        self.correo_edit = QLineEdit(self)
        self.correo_edit.setPlaceholderText("Correo electrónico")
        layout.addWidget(self.correo_edit)

        self.nombremascota_edit = QLineEdit(self)
        self.nombremascota_edit.setPlaceholderText("Nombre de mascota interesada")
        layout.addWidget(self.nombremascota_edit)

        genero_label = QLabel("sexo:")
        layout.addWidget(genero_label)

        genero = ["hembra", "macho"]
        self.genero_combo_box = QComboBox(self)
        self.genero_combo_box.addItems(genero)
        layout.addWidget(self.genero_combo_box)

        btn_enviar = QPushButton("Enviar Formulario", self)
        btn_enviar.clicked.connect(self.guardar_adopcion)
        layout.addWidget(btn_enviar)

    def guardar_adopcion(self):
        nombre = self.nombre_edit.text().strip()
        edad = self.edad_edit.text().strip()
        correo = self.correo_edit.text().strip()
        nombremascota = self.nombremascota_edit.text().strip()
        genero = self.genero_combo_box.currentText()

        if not nombre.isalpha():
            QMessageBox.warning(self, "Advertencia", "El nombre solo puede contener letras.")
            return

        if not nombre or not edad or not correo or not nombremascota:
            QMessageBox.warning(self, "Advertencia", "Por favor, complete todos los campos.")
            return

        try:
            self.agregar_al_formulario(nombre, edad, correo, nombremascota, genero)
            QMessageBox.information(self, "Información", "¡Formulario enviado correctamente!")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar el formulario: {e}")

    def agregar_al_formulario(self, nombre, edad, correo, nombremascota, genero):
        with open('adopciones.csv', mode='a', newline='') as file:
            escritor = csv.writer(file)
            escritor.writerow([nombre, edad, correo, nombremascota, genero])

class VentanaDetalleMascota(QDialog):
    def __init__(self, nombre_mascota, edad, genero, descripcion, imagen_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle(nombre_mascota)
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout(self)

        # Mostrar información de la mascota
        nombre_label = QLabel(f"Nombre: {nombre_mascota}")
        layout.addWidget(nombre_label)

        edad_label = QLabel(f"Edad: {edad}")
        layout.addWidget(edad_label)

        genero_label = QLabel(f"Género: {genero}")
        layout.addWidget(genero_label)

        descripcion_label = QLabel(descripcion)
        layout.addWidget(descripcion_label)

        imagen_label = QLabel()
        pixmap = QPixmap(imagen_path)
        if not pixmap.isNull():
            pixmap = pixmap.scaledToWidth(200)
            imagen_label.setPixmap(pixmap)
        layout.addWidget(imagen_label)

class AdopcionVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.animales = self.cargar_animales()
        self.crear_botones()

    def setupUi(self):
        self.setObjectName("VentanaAdopcion")
        self.resize(600, 440)
        self.setStyleSheet("background-color:pink;")
        self.setWindowTitle("Adopción")

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(309, 9, 311, 431))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 292, 1000))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.frame = QWidget(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 1000))
        self.verticalLayout_2 = QVBoxLayout(self.frame)

        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.texto_nombre = QLabel("Nombre del adoptante:", self)
        self.texto_nombre.setGeometry(QtCore.QRect(20, 10, 141, 31))
        self.Barra_bosqueda_nombre = QLineEdit(self)
        self.Barra_bosqueda_nombre.setGeometry(QtCore.QRect(20, 40, 241, 21))
        self.Barra_bosqueda_nombre.setStyleSheet("background-color: gray;")

        self.texto_edad = QLabel("Edad:", self)
        self.texto_edad.setGeometry(QtCore.QRect(20, 80, 49, 16))
        self.Barra_busqueda_edad = QLineEdit(self)
        self.Barra_busqueda_edad.setGeometry(QtCore.QRect(20, 110, 241, 21))
        self.Barra_busqueda_edad.setStyleSheet("background-color: gray")
        self.Barra_busqueda_edad.setValidator(QtGui.QIntValidator(0, 150, self))  # Solo acepta números

        self.texto_correo = QLabel("Correo electrónico:", self)
        self.texto_correo.setGeometry(QtCore.QRect(20, 150, 131, 16))
        self.Barra_busqueda_correo = QLineEdit(self)
        self.Barra_busqueda_correo.setGeometry(QtCore.QRect(20, 180, 241, 21))
        self.Barra_busqueda_correo.setStyleSheet("background-color: gray")

        self.texto_mascota = QLabel("Nombre de la mascota interesada:", self)
        self.texto_mascota.setGeometry(QtCore.QRect(20, 220, 191, 16))
        self.Barra_busqueda_mascota = QLineEdit(self)
        self.Barra_busqueda_mascota.setGeometry(QtCore.QRect(20, 250, 241, 21))
        self.Barra_busqueda_mascota.setStyleSheet("background-color: gray")

        self.texto_genero = QLabel("Género:", self)
        self.texto_genero.setGeometry(QtCore.QRect(20, 290, 191, 16))
        self.combo_genero = QComboBox(self)
        self.combo_genero.setGeometry(QtCore.QRect(20, 320, 241, 21))
        self.combo_genero.addItems(["Femenino", "Masculino", "Otro"])

        self.boton_enviar = QPushButton("Enviar Formulario", self)
        self.boton_enviar.setGeometry(QtCore.QRect(20, 400, 191, 32))
        self.boton_enviar.clicked.connect(self.mostrar_formulario)

    def mostrar_formulario(self):
        nombre = self.Barra_bosqueda_nombre.text().strip()
        edad = self.Barra_busqueda_edad.text().strip()
        correo = self.Barra_busqueda_correo.text().strip()
        nombremascota = self.Barra_busqueda_mascota.text().strip()

        if not nombre.isalpha():
            QMessageBox.warning(self, "Advertencia", "El nombre solo puede contener letras.")
            return

        if nombre == "" or edad == "" or correo == "" or nombremascota == "":
            QMessageBox.warning(self, "Advertencia", "Por favor, complete todos los campos.")
            return

        try:
            with open('adopciones.csv', mode='a', newline='') as file:
                escritor = csv.writer(file)
                escritor.writerow([nombre, edad, correo, nombremascota, self.combo_genero.currentText()])
            QMessageBox.information(self, "Información", "¡Formulario enviado correctamente!")
            self.limpiar_formulario()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar el formulario: {e}")

    def limpiar_formulario(self):
        self.Barra_bosqueda_nombre.clear()
        self.Barra_busqueda_edad.clear()
        self.Barra_busqueda_correo.clear()
        self.Barra_busqueda_mascota.clear()
        self.combo_genero.setCurrentIndex(0)

    def cargar_animales(self):
        animales = []
        try:
            with open('animales.csv', mode='r') as file:
                lector = csv.DictReader(file)
                for row in lector:
                    animal = {
                        'nombre': row.get('nombre', ''),
                        'imagen': row.get('imagen', ''),
                        'descripcion': row.get('descripcion', ''),
                        'edad': row.get('edad', ''),
                        'sexo': row.get('sexo', '')
                    }
                    animales.append(animal)
        except Exception as e:
            print(f"Error al cargar animales: {e}")
        return animales

    def crear_botones(self):
        for animal in self.animales:
            button = QPushButton(self.frame)
            button.setText(animal['nombre'])
            imagen_path = animal.get('imagen', '')
            pixmap = QPixmap(imagen_path)
            if not pixmap.isNull():
                icon = QtGui.QIcon(pixmap)
                button.setIcon(icon)
                button.setIconSize(QtCore.QSize(100, 100))
            button.setStyleSheet("background-color: pink; margin: 5px;")
            button.clicked.connect(lambda _, animal=animal: self.open_new_window(animal))
            self.verticalLayout_2.addWidget(button)

    def open_new_window(self, animal):
        detalle_mascota = VentanaDetalleMascota(
            nombre_mascota=animal.get('nombre', 'Desconocido'),
            edad=animal.get('edad', 'Desconocida'),
            genero=animal.get('sexo', 'Desconocido'),
            descripcion=animal.get('descripcion', 'Sin descripción'),
            imagen_path=animal.get('imagen', '')
        )
        detalle_mascota.exec()

def main():
    app = QApplication(sys.argv)
    ventana = AdopcionVentana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
