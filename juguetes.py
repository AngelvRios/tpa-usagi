import sys
import csv
from PyQt6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QLabel, QComboBox, QDialogButtonBox, 
    QWidget, QScrollArea, QHBoxLayout, QPushButton
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QIcon

class SeleccionarJugueteDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar Juguete")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: pink;")

        self.juguete_seleccionado = None

        # Layout principal
        layout_principal = QVBoxLayout(self)

        # ComboBox para seleccionar el tipo de animal
        etiqueta_tipo_animal = QLabel("Tipo de animal:")
        etiqueta_tipo_animal.setStyleSheet("font-size: 18px; margin: 10px;")
        layout_principal.addWidget(etiqueta_tipo_animal)

        self.tipo_combo_box = QComboBox(self)
        self.tipo_combo_box.addItems(["Perro", "Gato", "Conejo", "Roedores"])
        self.tipo_combo_box.currentIndexChanged.connect(self.actualizar_juguetes)
        layout_principal.addWidget(self.tipo_combo_box)

        # Área de scroll para los botones
        self.area_scroll = QScrollArea()
        self.area_scroll.setWidgetResizable(True)

        self.contenido_scroll = QWidget()
        self.layout_scroll = QHBoxLayout(self.contenido_scroll)
        self.layout_scroll.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.area_scroll.setWidget(self.contenido_scroll)
        layout_principal.addWidget(self.area_scroll)

        # Botones de aceptar y cancelar
        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        layout_principal.addWidget(botones)

        # Establecer el layout principal para la ventana
        self.setLayout(layout_principal)

        # Inicializar lista de juguetes
        self.actualizar_juguetes()

    def actualizar_juguetes(self):
        tipo_animal = self.tipo_combo_box.currentText()

        # Limpiar layout anterior
        for i in reversed(range(self.layout_scroll.count())):
            widget = self.layout_scroll.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        juguetes = []
        if tipo_animal == "Perro":
            juguetes = [
                {"nombre": "Pelota", "imagen": "ruta/a/tu/imagen_pelota.jpg", "descripcion": "Pelota divertida", "marca": "Marca X"},
                {"nombre": "Hueso de goma", "imagen": "ruta/a/tu/imagen_hueso.jpg", "descripcion": "Hueso duradero", "marca": "Marca Y"},
                {"nombre": "Cuerda", "imagen": "ruta/a/tu/imagen_cuerda.jpg", "descripcion": "Cuerda resistente", "marca": "Marca Z"}
            ]
        elif tipo_animal == "Gato":
            juguetes = [
                {"nombre": "Ratón de juguete", "imagen": "ruta/a/tu/imagen_raton.jpg", "descripcion": "Ratón para jugar", "marca": "Marca A"},
                {"nombre": "Pluma", "imagen": "ruta/a/tu/imagen_pluma.jpg", "descripcion": "Pluma divertida", "marca": "Marca B"},
                {"nombre": "Rascador", "imagen": "ruta/a/tu/imagen_rascador.jpg", "descripcion": "Rascador para gatos", "marca": "Marca C"}
            ]
        elif tipo_animal == "Conejo":
            juguetes = [
                {"nombre": "Túnel", "imagen": "ruta/a/tu/imagen_tunel.jpg", "descripcion": "Túnel para explorar", "marca": "Marca D"},
                {"nombre": "Zanahoria de juguete", "imagen": "ruta/a/tu/imagen_zanahoria.jpg", "descripcion": "Zanahoria divertida", "marca": "Marca E"},
                {"nombre": "Mordedor", "imagen": "ruta/a/tu/imagen_mordedor.jpg", "descripcion": "Mordedor resistente", "marca": "Marca F"}
            ]
        elif tipo_animal == "Roedores":
            juguetes = [
                {"nombre": "Rueda de ejercicio", "imagen": "ruta/a/tu/imagen_rueda.jpg", "descripcion": "Rueda para ejercitarse", "marca": "Marca G"},
                {"nombre": "Casita de madera", "imagen": "ruta/a/tu/imagen_casita.jpg", "descripcion": "Casita acogedora", "marca": "Marca H"},
                {"nombre": "Túnel", "imagen": "ruta/a/tu/imagen_tunel.jpg", "descripcion": "Túnel para roedores", "marca": "Marca I"}
            ]

        for juguete in juguetes:
            icon = QIcon(QPixmap(juguete["imagen"]))
            boton = QPushButton()
            boton.setIcon(icon)
            boton.setIconSize(QSize(200, 200))
            boton.setFixedSize(200, 200)
            boton.setStyleSheet("font-size: 18px;")
            boton.clicked.connect(lambda checked, j=juguete["nombre"]: self.seleccionar_juguete(j))
            self.layout_scroll.addWidget(boton)

        self.area_scroll.setWidget(self.contenido_scroll)

    def seleccionar_juguete(self, juguete):
        self.juguete_seleccionado = juguete
        print(f"Juguete seleccionado: {juguete}")

    def get_juguete_seleccionado(self):
        tipo_animal = self.tipo_combo_box.currentText()
        return tipo_animal, self.juguete_seleccionado

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = SeleccionarJugueteDialog()
    if dialogo.exec() == QDialog.accepted:
        tipo_animal, juguete = dialogo.get_juguete_seleccionado()
        print(f"Tipo de animal: {tipo_animal}")
        print(f"Juguete: {juguete}")
    sys.exit(app.exec())
