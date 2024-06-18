from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu, QDialog
from datetime import datetime
from comida import SeleccionarComidaDialog
from adopcion1 import TiendaMascotas, VentanaAdopcion, VentanaMascotas
from juguetes import SeleccionarJugueteDialog
from accesorio import SeleccionarAccesorioDialog
import csv

class VentanaPrincipal(QMainWindow):
    def __init__(self, tienda):
        super().__init__()
        self.setWindowTitle("Tienda para mascotas")
        self.setFixedSize(500, 400)
        self.tienda = tienda

        # Botón para seleccionar comida
        btn_comida = QPushButton("Comida", self)
        btn_comida.clicked.connect(self.abrir_ventana_comida)
        btn_comida.setGeometry(50, 50, 200, 50)

        # Botón para adopción con menú contextual
        btn_adopcion = QPushButton("Adopción", self)
        btn_adopcion.setGeometry(50, 100, 200, 50)
        btn_adopcion.setMenu(self.crear_menu_adopcion())
        
        # Botón para seleccionar juguetes
        btn_juguetes = QPushButton("Juguetes", self)
        btn_juguetes.clicked.connect(self.abrir_ventana_juguetes)
        btn_juguetes.setGeometry(50, 150, 200, 50)
        
        # Botón para seleccionar accesorios
        btn_accesorios = QPushButton("Accesorios", self)
        btn_accesorios.clicked.connect(self.abrir_ventana_accesorios)
        btn_accesorios.setGeometry(50, 200, 200, 50)

        # Inicializar el archivo CSV con los encabezados si no existe
        self.inicializar_archivo_csv()
    
    def inicializar_archivo_csv(self):
        try:
            with open("registro.csv", mode='x', newline='') as file:
                escritor_csv = csv.writer(file)
                escritor_csv.writerow(["Fecha", "Operación", "Detalles"])
        except FileExistsError:
            pass
    
    def abrir_ventana_accesorios(self):
        dialogo_accesorio = SeleccionarAccesorioDialog(self)
        if dialogo_accesorio.exec() == QDialog.DialogCode.Accepted:
            tipo_animal = dialogo_accesorio.tipo_combo_box.currentText()
            accesorio, cantidad = dialogo_accesorio.get_accesorio_seleccionado()
            self.registrar_operacion("Compra de accesorio", f"Tipo de animal: {tipo_animal}, Accesorio: {accesorio}, Cantidad: {cantidad}")

    def crear_menu_adopcion(self):
        menu_adopcion = QMenu()

        action_adoptar = menu_adopcion.addAction("Adoptar")
        action_adoptar.triggered.connect(self.abrir_ventana_adopcion)

        action_ver_animales = menu_adopcion.addAction("Ver animales disponibles")
        action_ver_animales.triggered.connect(self.mostrar_animales_disponibles)

        return menu_adopcion

    def abrir_ventana_comida(self):
        dialogo_comida = SeleccionarComidaDialog(self)
        dialogo_comida.accepted.connect(self.registrar_compra_comida)
        dialogo_comida.exec()

    def abrir_ventana_adopcion(self):
        ventana_adopcion = VentanaAdopcion(self.tienda)
        ventana_adopcion.accepted.connect(self.registrar_adopcion)
        ventana_adopcion.exec()
        
    def abrir_ventana_juguetes(self):
        dialogo_juguetes = SeleccionarJugueteDialog(self)
        dialogo_juguetes.accepted.connect(self.registrar_compra_juguete)
        dialogo_juguetes.exec()

    def mostrar_animales_disponibles(self):
        ventana_mascotas = VentanaMascotas(self.tienda)
        ventana_mascotas.actualizar_mascotas_disponibles()  # Actualizar la lista de animales antes de mostrar
        ventana_mascotas.exec()

    def registrar_operacion(self, operacion, detalles):
        with open("registro.csv", "a", newline='') as file:
            escritor_csv = csv.writer(file)
            escritor_csv.writerow([datetime.now().isoformat(), operacion, detalles])

    def registrar_compra_comida(self):
        dialogo_comida = self.sender()
        marca = dialogo_comida.marca_combo_box.currentText()
        tipo = dialogo_comida.tipo_combo_box.currentText()
        edad = dialogo_comida.edad_combo_box.currentText()
        kilogramos = dialogo_comida.kilogramos_spin_box.value()

        detalles = f"Marca: {marca}, Tipo: {tipo}, Edad: {edad}, Cantidad: {kilogramos}kg"
        self.registrar_operacion("Compra de comida", detalles)

    def registrar_adopcion(self):
        ventana_adopcion = self.sender()
        animal = ventana_adopcion.get_selected_animal()

        detalles = f"Animal: {animal}"
        self.registrar_operacion("Adopción", detalles)

    def registrar_compra_juguete(self):
        dialogo_juguetes = self.sender()
        tipo_animal = dialogo_juguetes.tipo_combo_box.currentText()
        juguete = dialogo_juguetes.juguetes_combo_box.currentText()

        detalles = f"Tipo de animal: {tipo_animal}, Juguete: {juguete}"
        self.registrar_operacion("Compra de juguete", detalles)


if __name__ == "__main__":
    app = QApplication([])
    tienda = TiendaMascotas()
    ventana = VentanaPrincipal(tienda) 
    ventana.show()
    app.exec()
