from PyQt6.QtWidgets import QDialog, QVBoxLayout, QComboBox, QLabel, QDialogButtonBox, QApplication
import sys

class SeleccionarJugueteDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar Juguete")
        layout = QVBoxLayout()

        # ComboBox para seleccionar el tipo de animal
        self.tipo_combo_box = QComboBox()
        self.tipo_combo_box.addItems(["Perro", "Gato", "Conejo", "Roedores"])
        layout.addWidget(QLabel("Tipo de animal:"))
        layout.addWidget(self.tipo_combo_box)
        self.tipo_combo_box.currentIndexChanged.connect(self.actualizar_juguetes)

        # ComboBox para seleccionar el tipo de juguete
        self.juguetes_combo_box = QComboBox()
        layout.addWidget(QLabel("Juguetes disponibles:"))
        layout.addWidget(self.juguetes_combo_box)

        self.actualizar_juguetes()

        # Botones de aceptar y cancelar
        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        layout.addWidget(botones)

        self.setLayout(layout)

    def actualizar_juguetes(self):
        tipo_animal = self.tipo_combo_box.currentText()
        self.juguetes_combo_box.clear()

        if tipo_animal == "Perro":
            self.juguetes_combo_box.addItems(["Pelota", "Hueso de goma", "Cuerda"])
        elif tipo_animal == "Gato":
            self.juguetes_combo_box.addItems(["Ratón de juguete", "Pluma", "Rascador"])
        elif tipo_animal == "Conejo":
            self.juguetes_combo_box.addItems(["Túnel", "Zanahoria de juguete", "Mordedor"])
        elif tipo_animal == "Roedores":
            self.juguetes_combo_box.addItems(["Rueda de ejercicio", "Casita de madera", "Túnel"])

    def get_juguete_seleccionado(self):
        tipo_animal = self.tipo_combo_box.currentText()
        juguete = self.juguetes_combo_box.currentText()
        return tipo_animal, juguete


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = SeleccionarJugueteDialog()
    if dialog.exec() == QDialog.DialogCode.Accepted:
        tipo_animal, juguete = dialog.get_juguete_seleccionado()
        print(f"Tipo de animal: {tipo_animal}")
        print(f"Juguete: {juguete}")

