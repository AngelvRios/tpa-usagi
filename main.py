from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu, QDialog, QVBoxLayout, QComboBox, QSpinBox, QLabel, QDialogButtonBox
from datetime import datetime
from comida import SeleccionarComidaDialog
from adopcion1 import TiendaMascotas, VentanaAdopcion, VentanaMascotas

class SeleccionarComidaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar Comida")
        layout = QVBoxLayout()

        # ComboBox para seleccionar el tipo de animal
        self.tipo_combo_box = QComboBox()
        self.tipo_combo_box.addItems(["perro", "gato", "tortuga", "conejo", "pájaro", "hamster"])
        layout.addWidget(QLabel("Tipo de animal:"))
        layout.addWidget(self.tipo_combo_box)
        self.tipo_combo_box.currentIndexChanged.connect(self.actualizar_marcas)

        # ComboBox para seleccionar la marca
        self.marca_combo_box = QComboBox()
        layout.addWidget(QLabel("Marca:"))
        layout.addWidget(self.marca_combo_box)

        # Llenamos inicialmente el comboBox de marcas
        self.actualizar_marcas()

        # ComboBox para seleccionar la edad
        self.edad_combo_box = QComboBox()
        self.edad_combo_box.addItems(["cachorro", "adulto", "anciano"])
        layout.addWidget(QLabel("Edad del animal:"))
        layout.addWidget(self.edad_combo_box)

        # SpinBox para seleccionar los kilogramos
        self.kilogramos_spin_box = QSpinBox()
        self.kilogramos_spin_box.setMinimum(1)
        self.kilogramos_spin_box.setMaximum(100)
        layout.addWidget(QLabel("Cantidad de comida (kilogramos):"))
        layout.addWidget(self.kilogramos_spin_box)

        # Botones de aceptar y cancelar
        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        layout.addWidget(botones)

        self.setLayout(layout)

    def actualizar_marcas(self):
        tipo_animal = self.tipo_combo_box.currentText()
        self.marca_combo_box.clear()

        if tipo_animal == "perro":
            self.marca_combo_box.addItems(["Ricocan", "Mimaskot", "Dog Chow", "Pedigree"])
        elif tipo_animal == "gato":
            self.marca_combo_box.addItems(["Whiskas", "Royal Canin", "Purina", "Mimaskot"])
        elif tipo_animal == "tortuga":
            self.marca_combo_box.addItems(["Tetra", "Sera", "ReptoMin"])
        elif tipo_animal == "conejo":
            self.marca_combo_box.addItems(["Vitakraft", "Kaytee", "Oxbow"])
        elif tipo_animal == "pájaro":
            self.marca_combo_box.addItems(["Zupreem", "Kaytee", "Lafeber"])
        elif tipo_animal == "hamster":
            self.marca_combo_box.addItems(["Vitakraft", "Kaytee", "Oxbow"])

class VentanaPrincipal(QMainWindow):
    def __init__(self, tienda):
        super().__init__()
        self.setWindowTitle("Tienda para mascotas")
        self.setFixedSize(500, 400)
        self.tienda = tienda

        # Botón para seleccionar comida
        btn_comida = QPushButton("Seleccionar Comida", self)
        btn_comida.clicked.connect(self.abrir_ventana_comida)
        btn_comida.setGeometry(50, 50, 200, 50)

        # Botón para adopción con menú contextual
        btn_adopcion = QPushButton("Adopción", self)
        btn_adopcion.setGeometry(50, 120, 200, 50)
        btn_adopcion.setMenu(self.crear_menu_adopcion())

    def crear_menu_adopcion(self):
        menu_adopcion = QMenu()

        action_adoptar = menu_adopcion.addAction("Adoptar")
        action_adoptar.triggered.connect(self.abrir_ventana_adopcion)

        action_ver_animales = menu_adopcion.addAction("Ver Animales Disponibles")
        action_ver_animales.triggered.connect(self.mostrar_animales_disponibles)

        return menu_adopcion

    def abrir_ventana_comida(self):
        dialogo_comida = SeleccionarComidaDialog(self)
        dialogo_comida.accepted.connect(self.registrar_compra_comida)
        dialogo_comida.exec()

    def abrir_ventana_adopcion(self):
        ventana_adopcion = VentanaAdopcion(self.tienda)
        ventana_adopcion.accepted.connect(self.registrar_adopcion)
        ventana_adopcion.exec()

    def mostrar_animales_disponibles(self):
        ventana_mascotas = VentanaMascotas(self.tienda)
        ventana_mascotas.actualizar_mascotas_disponibles()  # Actualizar la lista de animales antes de mostrar
        ventana_mascotas.exec()

    def registrar_compra_comida(self):
        dialogo_comida = self.sender()
        marca = dialogo_comida.marca_combo_box.currentText()
        tipo = dialogo_comida.tipo_combo_box.currentText()
        edad = dialogo_comida.edad_combo_box.currentText()
        kilogramos = dialogo_comida.kilogramos_spin_box.value()

        with open("registro.txt", "a") as file:
            file.write(f"{datetime.now()}: Compra de comida - Marca: {marca}, Tipo: {tipo}, Edad: {edad}, Cantidad: {kilogramos}kg\n")

    def registrar_adopcion(self):
        ventana_adopcion = self.sender()
        # Asumimos que el método get_selected_animal() devuelve la información del animal adoptado
        animal = ventana_adopcion.get_selected_animal()

        with open("registro.txt", "a") as file:
            file.write(f"{datetime.now()}: Adopción - Animal: {animal}\n")

if __name__ == "__main__":
    app = QApplication([])
    tienda = TiendaMascotas()
    ventana = VentanaPrincipal(tienda)  # Pasa la tienda como argumento
    ventana.show()
    app.exec()


