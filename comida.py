from PyQt6.QtWidgets import QDialog, QVBoxLayout, QComboBox, QSpinBox, QLabel, QPushButton, QDialogButtonBox

class SeleccionarComidaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar Comida")
        layout = QVBoxLayout()

      
        self.tipo_combo_box = QComboBox()
        self.tipo_combo_box.addItems(["Perro", "Gato", "Tortuga", "Conejo", "Pájaro", "Hamster"])
        layout.addWidget(QLabel("Tipo de animal:"))
        layout.addWidget(self.tipo_combo_box)
        self.tipo_combo_box.currentIndexChanged.connect(self.actualizar_marcas)


        self.marca_combo_box = QComboBox()
        layout.addWidget(QLabel("Marca:"))
        layout.addWidget(self.marca_combo_box)

        self.actualizar_marcas()

    
        self.edad_combo_box = QComboBox()
        self.edad_combo_box.addItems(["Cachorro", "Adulto", "Anciano"])
        layout.addWidget(QLabel("Edad del animal:"))
        layout.addWidget(self.edad_combo_box)

       
        self.kilogramos_spin_box = QSpinBox()
        self.kilogramos_spin_box.setMinimum(1)
        self.kilogramos_spin_box.setMaximum(100)
        layout.addWidget(QLabel("Cantidad de comida (kilogramos):"))
        layout.addWidget(self.kilogramos_spin_box)
        
     
        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        layout.addWidget(botones)


        self.setLayout(layout)

    def actualizar_marcas(self):
        tipo_animal = self.tipo_combo_box.currentText()
        self.marca_combo_box.clear()

        if tipo_animal == "Perro":
            self.marca_combo_box.addItems(["Ricocan", "Mimaskot", "Dog Chow", "Pedigree"])
        elif tipo_animal == "Gato":
            self.marca_combo_box.addItems(["Whiskas", "Royal Canin", "Purina", "Mimaskot"])
        elif tipo_animal == "Tortuga":
            self.marca_combo_box.addItems(["Tetra", "Sera", "ReptoMin"])
        elif tipo_animal == "Conejo":
            self.marca_combo_box.addItems(["Vitakraft", "Kaytee", "Oxbow"])
        elif tipo_animal == "Pájaro":
            self.marca_combo_box.addItems(["Zupreem", "Kaytee", "Lafeber"])
        elif tipo_animal == "Hamster":
            self.marca_combo_box.addItems(["Vitakraft", "Kaytee", "Oxbow"])

 
if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    dialog = SeleccionarComidaDialog()
    dialog.exec()