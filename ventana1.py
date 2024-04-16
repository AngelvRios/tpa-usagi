from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget

class comida:
    def __init__(self, marca: str, raza: str, age: str, kilogramos: int, comidaN: str):
        self.marca = marca 
        self.raza = raza
        self.age = age
        self.kilogramos = kilogramos
        self.comidaN = comidaN

class OtraVentana(QWidget):
    def __init__(self, title, comida_instance):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 300, 200)

        capa = QGridLayout()
        
        texto = QLabel(f"Marca: {comida_instance.marca}\nRaza: {comida_instance.raza}\nEdad: {comida_instance.age}\nKilogramos: {comida_instance.kilogramos}\nComida: {comida_instance.comidaN}")
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

        b2.clicked.connect(lambda: self.abrir_ventana_comida())

        panel = QWidget()
        panel.setLayout(caja)
        self.setCentralWidget(panel)
    
    def abrir_ventana_comida(self):
        mi_comida = comida("MarcaX", "Labrador", "cachorro", 5, "Croquetas")
        self.nueva_ventana = OtraVentana("Información de comida", mi_comida)
        self.nueva_ventana.show()

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
