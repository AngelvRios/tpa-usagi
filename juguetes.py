# archivo: juguetes.py
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QMessageBox

class SeleccionarJugueteDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar animal")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()

        self.btn_perro = QPushButton("Perro")
        self.btn_perro.clicked.connect(lambda: self.abrir_ventana_juguetes("perro"))
        layout.addWidget(self.btn_perro)

        self.btn_gato = QPushButton("Gato")
        self.btn_gato.clicked.connect(lambda: self.abrir_ventana_juguetes("gato"))
        layout.addWidget(self.btn_gato)

        self.btn_conejo = QPushButton("Conejo")
        self.btn_conejo.clicked.connect(lambda: self.abrir_ventana_juguetes("conejo"))
        layout.addWidget(self.btn_conejo)

        self.btn_roedores = QPushButton("Roedores")
        self.btn_roedores.clicked.connect(lambda: self.abrir_ventana_juguetes("roedores"))
        layout.addWidget(self.btn_roedores)

        self.setLayout(layout)

    def abrir_ventana_juguetes(self, tipo_animal):
        ventana_juguetes = VentanaJuguetes(tipo_animal)
        ventana_juguetes.exec()

class VentanaJuguetes(QDialog):
    def __init__(self, tipo_animal, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Juguetes Disponibles")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()

        label = QLabel(f"Juguetes disponibles para {tipo_animal.capitalize()}:")
        layout.addWidget(label)

        # Aquí podrías agregar la lógica para listar los juguetes disponibles según el tipo de animal
        # Por simplicidad, agregamos algunos juguetes ficticios
        if tipo_animal == "perro":
            juguetes = ["Pelota", "Hueso de goma", "Cuerda"]
        elif tipo_animal == "gato":
            juguetes = ["Ratón de juguete", "Pluma", "Rascador"]
        elif tipo_animal == "conejo":
            juguetes = ["Túnel", "Zanahoria de juguete", "Mordedor"]
        elif tipo_animal == "roedores":
            juguetes = ["Rueda de ejercicio", "Casita de madera", "Túnel"]

        for juguete in juguetes:
            btn_juguete = QPushButton(juguete)
            btn_juguete.clicked.connect(lambda _, j=juguete: self.comprar_juguete(j))
            layout.addWidget(btn_juguete)

        self.setLayout(layout)

    def comprar_juguete(self, juguete):
        QMessageBox.information(self, "Compra realizada", f"Has comprado el juguete: {juguete}")
