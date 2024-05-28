from PyQt6.QtWidgets import QDialog, QVBoxLayout, QComboBox, QSpinBox, QLabel, QPushButton

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

        # Botón de aceptar
        btn_aceptar = QPushButton("Aceptar")
        btn_aceptar.clicked.connect(self.guardar_informacion)
        layout.addWidget(btn_aceptar)

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

    def guardar_informacion(self):
        marca = self.marca_combo_box.currentText()
        tipo = self.tipo_combo_box.currentText()
        edad = self.edad_combo_box.currentText()
        kilogramos = self.kilogramos_spin_box.value()

        # Aquí puedes hacer lo que necesites con la información guardada
        # por ejemplo, imprimirlo o utilizarlo en otro lugar
        print("Marca:", marca)
        print("Tipo de animal:", tipo)
        print("Edad del animal:", edad)
        print("Cantidad de comida (kilogramos):", kilogramos)

        self.close()

# Ejemplo de cómo mostrar el diálogo (esto normalmente iría en otra parte de tu aplicación)
if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    dialog = SeleccionarComidaDialog()
    dialog.exec()
