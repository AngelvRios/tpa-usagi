from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget, QDialog, QVBoxLayout

class RazaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar Raza")
        layout = QVBoxLayout()

        # Lista de razas
        razas = ["Labrador", "Bulldog", "Poodle"]

        # Crear botón para cada raza y conectar su señal clicked a la función raza_seleccionada
        for raza in razas:
            button = QPushButton(raza)
            button.clicked.connect(lambda checked, r=raza: self.raza_seleccionada(r))
            layout.addWidget(button)

        self.setLayout(layout)

    def raza_seleccionada(self, raza):
        # Cuando se selecciona una raza, cerrar el diálogo y emitir la señal raza_seleccionada con la raza seleccionada
        self.accept()
        self.raza_seleccionada_signal.emit(raza)

class comida:
    def __init__(self, marca: str, raza: str, age: str, kilogramos: int, comidaN: str):
        self.marca = marca 
        self.raza = raza
        self.age = age
        self.kilogramos = kilogramos
        self.comidaN = comidaN

    def get_marca(self):
        return self.marca

    def get_raza(self):
        return self.raza

    def get_age(self):
        return self.age

    def get_kilogramos(self):
        return self.kilogramos

    def set_raza(self, raza: str):
        self.raza = raza

    def set_age(self, age: str):
        self.age = age

    def set_kilogramos(self, kilogramos: int):
        self.kilogramos = kilogramos

    def __str__(self):
        return f"Nombre: {self.marca}, Raza: {self.raza}, Edad: {self.age}, Kilogramos: {self.kilogramos}, Comida: {self.comidaN}"

class OtraVentana(QWidget):
    def __init__(self, title, comida_instance):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 300, 200)

        capa = QGridLayout()
        
        texto = QLabel(f"Marca: {comida_instance.get_marca()}\nRaza: {comida_instance.get_raza()}\nEdad: {comida_instance.get_age()}\nKilogramos: {comida_instance.get_kilogramos()}\nComida: {comida_instance.comidaN}")
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
        mi_comida = comida("MarcaX", "", "cachorro", 5, "Croquetas")

        # Mostrar el diálogo de selección de raza
        dialogo_raza = RazaDialog()
        if dialogo_raza.exec() == QDialog.DialogCode.Accepted:
            # Obtener la raza seleccionada del diálogo
            raza_seleccionada = dialogo_raza.raza_seleccionada
            mi_comida.set_raza(raza_seleccionada)

        # Abrir la ventana de comida con los datos actualizados
        nueva_ventana = OtraVentana("Información de comida", mi_comida)
        nueva_ventana.show()

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
