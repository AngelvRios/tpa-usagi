from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget, QDialog, QVBoxLayout, QComboBox, QSpinBox
from datetime import datetime

class RazaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar tipo de animal")
        layout = QVBoxLayout()

        # Lista de tipos de animal
        tipos = ["perro", "gato", "tortuga","conejo", "pajaro", "hamster"]

        # Crear botón para cada tipo y conectar su señal clicked a la función tipo_seleccionado
        for tipo in tipos:
            button = QPushButton(tipo)
            button.clicked.connect(lambda checked, r=tipo: self.tipo_seleccionado(r))
            layout.addWidget(button)

        self.setLayout(layout)

    def tipo_seleccionado(self, tipo):
        # Cuando se selecciona un tipo, cerrar el diálogo y emitir la señal tipo_seleccionado con el tipo seleccionado
        self.accept()
        self.tipo_seleccionado_signal = tipo

class MarcaComidaDialog(QDialog):
    def __init__(self, tipo, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar marca de comida")
        layout = QVBoxLayout()

        # Lista de marcas de comida para el tipo seleccionado
        marcas_perro = ["Ricocan", "Mimaskot", "Dog Chow"]
        marcas_gato = ["Royal Canin", "Hill's Science Diet", "Purina Pro Plan"]
        marcas_tortuga = ["Living world", "Mazuri", "Zoo Med"]
        marcas_conejo = ["Kaytee", "oxbow","Versele-Laga"]
        marcas_pajaro = ["Beaphar","Birdola","Canary song"]
        marcas_hamster = ["Brit Super", "Tropifit", "Heno De Alfalfa"]
        # Dependiendo del tipo de animal seleccionado, se selecciona la lista de marcas de comida correspondiente
        marcas = []
        if tipo == "perro":
            marcas = marcas_perro
        elif tipo == "gato":
            marcas = marcas_gato
        elif tipo == "tortuga":
            marcas = marcas_tortuga
        elif tipo == "conejo":
            marcas = marcas_conejo
        elif tipo == "pajaro":
            marcas = marcas_pajaro
        elif tipo == "hamster":
            marcas = marcas_hamster

        # Crear un ComboBox con las opciones de marca de comida
        combo_box = QComboBox()
        combo_box.addItems(marcas)
        layout.addWidget(combo_box)

        # Botón de aceptar
        button = QPushButton("Aceptar")
        button.clicked.connect(lambda: self.accept())
        layout.addWidget(button)

        self.setLayout(layout)

class KilogramosDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar kilogramos")
        layout = QVBoxLayout()

        # Crear un QSpinBox para seleccionar la cantidad de kilogramos
        spin_box = QSpinBox()
        spin_box.setMinimum(1)  # Establecer el valor mínimo
        spin_box.setMaximum(100)  # Establecer el valor máximo
        layout.addWidget(spin_box)

        # Botón de aceptar
        button = QPushButton("Aceptar")
        button.clicked.connect(lambda: self.kilogramos_seleccionados(spin_box.value()))
        layout.addWidget(button)

        self.setLayout(layout)

    def kilogramos_seleccionados(self, kilogramos):
        # Cuando se selecciona la cantidad de kilogramos, cerrar el diálogo y emitir la señal kilogramos_seleccionados con la cantidad seleccionada
        self.accept()
        self.kilogramos_seleccionados_signal = kilogramos

class comida:
    def __init__(self, marca: str, tipo: str, age: str, kilogramos: int, comidaN: str):
        self.marca = marca 
        self.tipo = tipo
        self.age = age
        self.kilogramos = kilogramos
        self.comidaN = comidaN

    def get_marca(self):
        return self.marca

    def get_tipo(self):
        return self.tipo

    def get_age(self):
        return self.age

    def get_kilogramos(self):
        return self.kilogramos

    def set_tipo(self, tipo: str):
        self.tipo = tipo

    def set_age(self, age: str):
        self.age = age

    def set_kilogramos(self, kilogramos: int):
        self.kilogramos = kilogramos

    def __str__(self):
        return f"Nombre: {self.marca}, Tipo: {self.tipo}, Edad: {self.age}, Kilogramos: {self.kilogramos}, Comida: {self.comidaN}"

class OtraVentana(QWidget):
    def __init__(self, title, comida_instance):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 300, 200)

        capa = QGridLayout()
        
        texto = QLabel(f"Marca: {comida_instance.get_marca()}\nTipo: {comida_instance.get_tipo()}\nEdad: {comida_instance.get_age()}\nKilogramos: {comida_instance.get_kilogramos()}\nComida: {comida_instance.comidaN}")
        capa.addWidget(texto, 0,0)
        self.setLayout(capa)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contador = 0

        self.setWindowTitle("Tienda para mascotas")
        self.setFixedSize(1280, 720)

        caja = QGridLayout()
        b2 = QPushButton("comida")
        caja.addWidget(b2, 0,1)

        # Conexión del botón "comida" con la función abrir_ventana_comida
        b2.clicked.connect(lambda: self.abrir_ventana_comida())

        panel = QWidget()
        panel.setLayout(caja)
        self.setCentralWidget(panel)
    
    def abrir_ventana_comida(self):
        # Crear una instancia de la clase comida con los datos que desees
        mi_comida = comida("", "", "", 5, "")

        # Mostrar el diálogo de selección de tipo de animal
        dialogo_tipo = RazaDialog()
        if dialogo_tipo.exec() == QDialog.DialogCode.Accepted:
            # Obtener el tipo seleccionado del diálogo
            tipo_seleccionado = dialogo_tipo.tipo_seleccionado_signal
            mi_comida.set_tipo(tipo_seleccionado)

            # Mostrar el diálogo de selección de marca de comida
            dialogo_marca = MarcaComidaDialog(tipo_seleccionado)
            if dialogo_marca.exec() == QDialog.DialogCode.Accepted:
                # Obtener la marca seleccionada del diálogo
                marca_seleccionada = dialogo_marca.findChild(QComboBox).currentText()
                mi_comida.marca = marca_seleccionada

                # Mostrar el diálogo de selección de kilogramos
                dialogo_kilos = KilogramosDialog()
                if dialogo_kilos.exec() == QDialog.DialogCode.Accepted:
                    # Obtener los kilogramos seleccionados del diálogo
                    kilos_seleccionados = dialogo_kilos.kilogramos_seleccionados_signal
                    mi_comida.set_kilogramos(kilos_seleccionados)

                    # Crear una cadena con la información de la comida
                    info_comida = str(mi_comida)

                    # Guardar la información en un archivo de texto
                    try:
                        with open("informacion_comida.txt", "a") as file:
                            file.write(f"Información de comida seleccionada ({datetime.now()}):\n{info_comida}\n\n")
                        print("Información de comida guardada correctamente en 'informacion_comida.txt'")
                    except Exception as e:
                        print(f"Error al guardar la información de comida: {e}")

                    # Abrir la ventana de comida con los datos actualizados
                    nueva_ventana = OtraVentana("Información de comida", mi_comida)
                    nueva_ventana.show()

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
