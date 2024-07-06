from PyQt6 import QtCore, QtGui, QtWidgets
from stock import StockWindow  # Importa la clase StockWindow desde el archivo stock.py
from ofertassemanales import OfertasSemanales
from Ui_RegistroAdminWindow import Ui_RegistroAdminWindow
import os

class VentanaAdmin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(265, 434)
        self.setMinimumSize(QtCore.QSize(265, 434))
        self.setMaximumSize(QtCore.QSize(265, 434))
        self.setStyleSheet("background-color: pink;")
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.setupUi()
        
    def setupUi(self):
        self.stockboton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stockboton.setGeometry(QtCore.QRect(50, 110, 171, 31))
        self.stockboton.setObjectName("stockboton")
        self.stockboton.clicked.connect(self.abrir_stock)  # Conectar el clic del botón a la función abrir_stock
        
        self.botonagregaradmin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.botonagregaradmin.setGeometry(QtCore.QRect(50, 150, 171, 31))
        self.botonagregaradmin.setObjectName("botonagregaradmin")
        self.botonagregaradmin.clicked.connect(self.nuevo_admin)
        
        self.ofertassemanales = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ofertassemanales.setGeometry(QtCore.QRect(50, 190, 171, 31))
        self.ofertassemanales.setObjectName("ofertassemanales")
        self.ofertassemanales.clicked.connect(self.abrir_ofertas)
        
        self.botonboleta = QtWidgets.QPushButton(parent=self.centralwidget)
        self.botonboleta.setGeometry(QtCore.QRect(50, 230, 171, 31))
        self.botonboleta.setObjectName("botonboleta")
        
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 100, 16))
        self.label.setObjectName("label")
        self.label.setText("Usuario:")
        
        self.nombredeusuario = QtWidgets.QLabel(parent=self.centralwidget)
        self.nombredeusuario.setGeometry(QtCore.QRect(80, 7, 142, 19))
        self.nombredeusuario.setText(self.nombre_usuario())
        self.nombredeusuario.setObjectName("nombredeusuario")
        
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(46, 295, 171, 141))
        self.label_2.setText("")
        
        # Verificar si la imagen se carga correctamente
        image_path = os.path.abspath("bienvenido.png")
        pixmap = QtGui.QPixmap(image_path)
 
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.statusbar = QtWidgets.QStatusBar(parent=self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Administrador"))
        self.stockboton.setText(_translate("MainWindow", "Stock"))
        self.botonagregaradmin.setText(_translate("MainWindow", "Agregar Administrador"))
        self.ofertassemanales.setText(_translate("MainWindow", "Ofertas Semanales"))
        self.botonboleta.setText(_translate("MainWindow", "Boletas"))

    def abrir_stock(self):
        self.stock_window = StockWindow()
        self.stock_window.show()

    def nuevo_admin(self):
        self.registeradmin = Ui_RegistroAdminWindow()
        self.ui_registeradmin = QtWidgets.QMainWindow(self)
        self.registeradmin.setupUi(self.ui_registeradmin)
        self.ui_registeradmin.show()
        
    def abrir_ofertas(self):
        self.ofertas_semanales = OfertasSemanales()
        self.ofertas_semanales.show()

    def nombre_usuario(self):
        from ui_login import user
        for nombre in user:
            return nombre

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana_admin = VentanaAdmin()
    ventana_admin.show()
    sys.exit(app.exec())
