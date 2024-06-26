from PyQt6.QtWidgets import QDialog, QVBoxLayout, QComboBox, QSpinBox, QLabel, QDialogButtonBox

class SeleccionarAccesorioDialog(QDialog):
    def __init__(self, tipo_animal, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar Accesorio")
        layout = QVBoxLayout()

        # ComboBox para seleccionar el tipo de accesorio
        self.accesorio_combo_box = QComboBox()
        self.accesorio_combo_box.addItems(["Collar", "Correa", "Cama", "Transportadora", "Rascador"])
        layout.addWidget(QLabel("Tipo de accesorio:"))
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

    def get_accesorio_seleccionado(self):
        return self.accesorio_combo_box.currentText(), self.cantidad_spin_box.value()
