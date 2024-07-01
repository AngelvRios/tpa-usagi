import sys
from PyQt6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QLabel, QComboBox, QDialogButtonBox, 
    QWidget, QScrollArea, QHBoxLayout, QPushButton, QSpinBox
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QIcon

class SeleccionarAccesorioDialog(QDialog):
    def __init__(self, tipo_animal, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar Accesorio")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: pink;")

        self.accesorio_seleccionado = None

        # Layout principal
        layout_principal = QVBoxLayout(self)

        # ComboBox para seleccionar el tipo de accesorio
        etiqueta_tipo_accesorio = QLabel("Tipo de accesorio:")
        etiqueta_tipo_accesorio.setStyleSheet("font-size: 18px; margin: 10px;")
        layout_principal.addWidget(etiqueta_tipo_accesorio)

        self.accesorio_combo_box = QComboBox()
        self.accesorio_combo_box.addItems(["Collar", "Correa", "Cama", "Transportadora", "Rascador"])
        self.accesorio_combo_box.currentIndexChanged.connect(self.actualizar_accesorios)
        layout_principal.addWidget(self.accesorio_combo_box)

        # Área de scroll para los botones de accesorios
        self.area_scroll = QScrollArea()
        self.area_scroll.setWidgetResizable(True)

        self.contenido_scroll = QWidget()
        self.layout_scroll = QHBoxLayout(self.contenido_scroll)
        self.layout_scroll.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.area_scroll.setWidget(self.contenido_scroll)
        layout_principal.addWidget(self.area_scroll)

        # SpinBox para seleccionar la cantidad
        etiqueta_cantidad = QLabel("Cantidad:")
        etiqueta_cantidad.setStyleSheet("font-size: 18px; margin: 10px;")
        layout_principal.addWidget(etiqueta_cantidad)

        self.cantidad_spin_box = QSpinBox()
        self.cantidad_spin_box.setMinimum(1)
        self.cantidad_spin_box.setMaximum(100)
        layout_principal.addWidget(self.cantidad_spin_box)

        # Botones de aceptar y cancelar
        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        layout_principal.addWidget(botones)

        # Establecer el layout principal para la ventana
        self.setLayout(layout_principal)

        # Inicializar lista de accesorios
        self.actualizar_accesorios()

    def actualizar_accesorios(self):
        tipo_accesorio = self.accesorio_combo_box.currentText()

        # Limpiar layout anterior
        for i in reversed(range(self.layout_scroll.count())):
            widget = self.layout_scroll.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Simular diferentes accesorios basados en el tipo seleccionado
        # Aquí puedes definir tus propios datos de accesorios según el tipo seleccionado
        accesorios = []
        if tipo_accesorio == "Collar":
            accesorios = [
                {"nombre": "Collar Clásico", "imagen": "ruta/a/tu/imagen_collar.jpg", "descripcion": "Collar para mascotas", "marca": "Marca X"},
                {"nombre": "Collar Reflectante", "imagen": "ruta/a/tu/imagen_collar_reflectante.jpg", "descripcion": "Collar para visibilidad nocturna", "marca": "Marca Y"},
                {"nombre": "Collar Ajustable", "imagen": "ruta/a/tu/imagen_collar_ajustable.jpg", "descripcion": "Collar con tamaño ajustable", "marca": "Marca Z"}
            ]
        elif tipo_accesorio == "Correa":
            accesorios = [
                {"nombre": "Correa Corta", "imagen": "ruta/a/tu/imagen_correa_corta.jpg", "descripcion": "Correa resistente", "marca": "Marca A"},
                {"nombre": "Correa Extensible", "imagen": "ruta/a/tu/imagen_correa_extensible.jpg", "descripcion": "Correa para mayor libertad de movimiento", "marca": "Marca B"},
                {"nombre": "Correa Reflectante", "imagen": "ruta/a/tu/imagen_correa_reflectante.jpg", "descripcion": "Correa para visibilidad nocturna", "marca": "Marca C"}
            ]
        elif tipo_accesorio == "Cama":
            accesorios = [
                {"nombre": "Cama Ovalada", "imagen": "ruta/a/tu/imagen_cama_ovalada.jpg", "descripcion": "Cama cómoda para descanso", "marca": "Marca D"},
                {"nombre": "Cama Redonda", "imagen": "ruta/a/tu/imagen_cama_redonda.jpg", "descripcion": "Cama suave y acogedora", "marca": "Marca E"},
                {"nombre": "Cama Elevada", "imagen": "ruta/a/tu/imagen_cama_elevada.jpg", "descripcion": "Cama elevada para clima caliente", "marca": "Marca F"}
            ]
        elif tipo_accesorio == "Transportadora":
            accesorios = [
                {"nombre": "Transportadora Básica", "imagen": "ruta/a/tu/imagen_transportadora_basica.jpg", "descripcion": "Transportadora segura y práctica", "marca": "Marca G"},
                {"nombre": "Transportadora Plegable", "imagen": "ruta/a/tu/imagen_transportadora_plegable.jpg", "descripcion": "Transportadora fácil de almacenar", "marca": "Marca H"},
                {"nombre": "Transportadora de Lujo", "imagen": "ruta/a/tu/imagen_transportadora_lujo.jpg", "descripcion": "Transportadora cómoda y elegante", "marca": "Marca I"}
            ]
        elif tipo_accesorio == "Rascador":
            accesorios = [
                {"nombre": "Rascador Básico", "imagen": "ruta/a/tu/imagen_rascador_basico.jpg", "descripcion": "Rascador para gatos", "marca": "Marca J"},
                {"nombre": "Rascador de Árbol", "imagen": "ruta/a/tu/imagen_rascador_arbol.jpg", "descripcion": "Rascador con forma de árbol", "marca": "Marca K"},
                {"nombre": "Rascador de Cartón", "imagen": "ruta/a/tu/imagen_rascador_carton.jpg", "descripcion": "Rascador ecológico de cartón", "marca": "Marca L"}
            ]

        for accesorio in accesorios:
            icon = QIcon(QPixmap(accesorio["imagen"]))
            boton = QPushButton()
            boton.setIcon(icon)
            boton.setIconSize(QSize(200, 200))
            boton.setFixedSize(200, 200)
            boton.setStyleSheet("font-size: 18px;")
            boton.clicked.connect(lambda checked, a=accesorio["nombre"]: self.seleccionar_accesorio(a))
            self.layout_scroll.addWidget(boton)

        self.area_scroll.setWidget(self.contenido_scroll)

    def seleccionar_accesorio(self, accesorio):
        self.accesorio_seleccionado = accesorio
        print(f"Accesorio seleccionado: {accesorio}")

    def get_accesorio_seleccionado(self):
        return self.accesorio_seleccionado, self.cantidad_spin_box.value()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = SeleccionarAccesorioDialog(tipo_animal=None)
    if dialogo.exec() == QDialog.accepted:
        accesorio, cantidad = dialogo.get_accesorio_seleccionado()
        print(f"Accesorio: {accesorio}")
        print(f"Cantidad: {cantidad}")
    sys.exit(app.exec())
