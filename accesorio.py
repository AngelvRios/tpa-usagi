from PyQt6.QtWidgets import QDialog, QVBoxLayout, QComboBox, QLabel, QSpinBox, QDialogButtonBox

class SeleccionarAccesorioDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar accesorios")
        layout = QVBoxLayout()

        # ComboBox para seleccionar el tipo de animal
        self.tipo_combo_box = QComboBox()
        self.tipo_combo_box.addItems(["Perro", "Gato", "Tortuga", "Conejo", "Pájaro", "Hamster"])
        layout.addWidget(QLabel("Tipo de animal:"))
        layout.addWidget(self.tipo_combo_box)
        self.tipo_combo_box.currentIndexChanged.connect(self.actualizar_accesorios)

        # ComboBox para seleccionar el accesorio
        self.accesorio_combo_box = QComboBox()
        layout.addWidget(QLabel("Accesorio:"))
        layout.addWidget(self.accesorio_combo_box)

        # SpinBox para seleccionar la cantidad
        self.cantidad_spin_box = QSpinBox()
        self.cantidad_spin_box.setMinimum(1)
        self.cantidad_spin_box.setMaximum(10)
        layout.addWidget(QLabel("Cantidad:"))
        layout.addWidget(self.cantidad_spin_box)

        # Botones de aceptar y cancelar
        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        layout.addWidget(botones)

        self.setLayout(layout)

        # Llenamos inicialmente el comboBox de accesorios
        self.actualizar_accesorios()

    def actualizar_accesorios(self):
        tipo_animal = self.tipo_combo_box.currentText()
        self.accesorio_combo_box.clear()

        if tipo_animal == "Perro":
            self.accesorio_combo_box.addItems(["Correa", "Collar", "Cama"," Transportador"])
        elif tipo_animal == "Gato":
            self.accesorio_combo_box.addItems(["Rascador", "Collar", "Cama", "Transportador"])
        elif tipo_animal == "Tortuga":
            self.accesorio_combo_box.addItems(["Terrario", "Lámpara", "Filtro"])
        elif tipo_animal == "Conejo":
            self.accesorio_combo_box.addItems(["Jaula", "Bebedero", "Pellet"])
        elif tipo_animal == "Pájaro":
            self.accesorio_combo_box.addItems(["Jaula", "Percha", ])
        elif tipo_animal == "Hamster":
            self.accesorio_combo_box.addItems(["Jaula", "Rueda", "Pellet"])

    def get_accesorio_seleccionado(self):
        accesorio = self.accesorio_combo_box.currentText()
        cantidad = self.cantidad_spin_box.value()
        return accesorio, cantidad

