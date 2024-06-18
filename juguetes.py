from PyQt6.QtWidgets import QDialog, QVBoxLayout, QComboBox, QLabel, QDialogButtonBox, QApplication, QMessageBox
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

        # Llenamos inicialmente el comboBox de juguetes
        self.actualizar_juguetes()

        # Botones de aceptar y cancelar
        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        botones.accepted.connect(self.registrar_seleccion)
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

    def registrar_seleccion(self):
        tipo_animal = self.tipo_combo_box.currentText()
        juguete = self.juguetes_combo_box.currentText()

        # Mostrar un mensaje de confirmación
        QMessageBox.information(self, "Selección Guardada", f"Tipo de animal: {tipo_animal}\nJuguete: {juguete}")
        
        # Imprimir en consola (registro)
        print(f"Tipo de animal: {tipo_animal}")
        print(f"Juguete: {juguete}")

        self.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = SeleccionarJugueteDialog()
    if dialog.exec() == QDialog.DialogCode.Accepted:
        # Las selecciones ya se imprimieron en el método registrar_seleccion
        pass
