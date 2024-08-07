from PyQt6.QtWidgets import QApplication, QDockWidget, QPushButton, QLabel, QTextEdit, QSlider, QWidget
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu, QDialog, QVBoxLayout, QComboBox, QSpinBox, QLabel, QDialogButtonBox
from datetime import datetime
from comida import VentanaProducto
from juguetes import SeleccionarJugueteDialog
from accesorio import SeleccionarAccesorioDialog 
from PyQt6.QtWidgets import QApplication, QMainWindow, QDockWidget
from PyQt6 import QtCore
import sys

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(711, 513)
        DockWidget.setStyleSheet("background-color:pink")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.AdopcionButton = QPushButton(self.dockWidgetContents)
        self.AdopcionButton.setGeometry(QtCore.QRect(10, 10, 101, 41))
        self.AdopcionButton.setStyleSheet("background-color:rgb(170, 170, 255);\nborder-style:solid;\nborder-radius:20px;\nborder-width:2px;\nborder-color:rgb(159, 115, 255);")
        self.AdopcionButton.setObjectName("AdopcionButton")
        self.AlimentosButton = QPushButton(self.dockWidgetContents)
        self.AlimentosButton.setGeometry(QtCore.QRect(120, 10, 111, 41))
        self.AlimentosButton.setStyleSheet("background-color:rgb(170, 170, 255);\nborder-style:solid;\nborder-radius:20px;\nborder-width:2px;\nborder-color:rgb(159, 115, 255);")
        self.AlimentosButton.setObjectName("AlimentosButton")
        self.JuguetesButton = QPushButton(self.dockWidgetContents)
        self.JuguetesButton.setGeometry(QtCore.QRect(240, 10, 111, 41))
        self.JuguetesButton.setStyleSheet("background-color:rgb(170, 170, 255);\nborder-style:solid;\nborder-radius:20px;\nborder-width:2px;\nborder-color:rgb(159, 115, 255);")
        self.JuguetesButton.setObjectName("JuguetesButton")
        self.AccesorioButtom = QPushButton(self.dockWidgetContents)
        self.AccesorioButtom.setGeometry(QtCore.QRect(360, 10, 111, 41))
        self.AccesorioButtom.setStyleSheet("background-color:rgb(170, 170, 255);\nborder-style:solid;\nborder-radius:20px;\nborder-width:2px;\nborder-color:rgb(159, 115, 255);")
        self.AccesorioButtom.setObjectName("AccesorioButtom")
        self.BusquedaButton = QPushButton(self.dockWidgetContents)
        self.BusquedaButton.setGeometry(QtCore.QRect(590, 10, 111, 41))
        self.BusquedaButton.setStyleSheet("background-color:rgb(170, 170, 255);\nborder-style:solid;\nborder-radius:20px;\nborder-width:2px;\nborder-color:rgb(159, 115, 255);")
        self.BusquedaButton.setObjectName("BusquedaButton")
        # self.label = QLabel(self.dockWidgetContents)
        # self.label.setGeometry(QtCore.QRect(570, 360, 121, 111))
        # self.label.setText("")
        # self.label.setPixmap(QPixmap("C:\\Users\\denis\\Downloads\\../../../../../../../Downloads/carpeta/patitas.png"))
        # self.label.setScaledContents(True)
        # self.label.setObjectName("label")
        self.CarritoButton_2 = QPushButton(self.dockWidgetContents)
        self.CarritoButton_2.setGeometry(QtCore.QRect(480, 10, 41, 41))
        self.CarritoButton_2.setStyleSheet("background-color:rgb(170, 170, 255);\nborder-style:solid;\nborder-radius:20px;\nborder-width:2px;\nborder-color:rgb(159, 115, 255);")
        self.CarritoButton_2.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap("C:\\Users\\denis\\Downloads\\../../../../../../../Downloads/carpeta/pngwing.com.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.CarritoButton_2.setIcon(icon)
        self.CarritoButton_2.setIconSize(QtCore.QSize(35, 35))
        self.CarritoButton_2.setObjectName("CarritoButton_2")
        self.CarritoButton_3 = QPushButton(self.dockWidgetContents)
        self.CarritoButton_3.setGeometry(QtCore.QRect(540, 10, 41, 41))
        self.CarritoButton_3.setStyleSheet("background-color:rgb(170, 170, 255);\nborder-style:solid;\nborder-radius:20px;\nborder-width:2px;\nborder-color:rgb(159, 115, 255);")
        self.CarritoButton_3.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("C:\\Users\\denis\\Downloads\\../../../../../../../Downloads/carpeta/lupa.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.CarritoButton_3.setIcon(icon1)
        self.CarritoButton_3.setIconSize(QtCore.QSize(30, 30))
        self.CarritoButton_3.setObjectName("CarritoButton_3")
        self.texto_ofertas_2 = QTextEdit(self.dockWidgetContents)
        self.texto_ofertas_2.setGeometry(QtCore.QRect(50, 310, 151, 41))
        self.texto_ofertas_2.setStyleSheet("background-color: rgb(255, 178, 241);\nborder-style:solid;\nborder-radius:20px;\nborder-width:2px;\nborder-color:rgb(255, 193, 255);")
        self.texto_ofertas_2.setObjectName("texto_ofertas_2")
        self.texto_ofertas_3 = QTextEdit(self.dockWidgetContents)
        self.texto_ofertas_3.setGeometry(QtCore.QRect(50, 80, 151, 41))
        self.texto_ofertas_3.setStyleSheet("background-color: rgb(255, 178, 241);\nborder-style:solid;\nborder-radius:20px;\nborder-width:2px;\nborder-color:rgb(255, 193, 255);")
        self.texto_ofertas_3.setObjectName("texto_ofertas_3")
        self.horizontalSlider = QSlider(self.dockWidgetContents)
        self.horizontalSlider.setGeometry(QtCore.QRect(100, 210, 491, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.ContactoButton = QPushButton(self.dockWidgetContents)
        self.ContactoButton.setGeometry(QtCore.QRect(40, 450, 81, 31))
        self.ContactoButton.setStyleSheet("background-color:rgb(170, 170, 255);\nborder-style:solid;\nborder-radius:20px;\nborder-width:2px;\nborder-color:rgb(159, 115, 255);")
        self.ContactoButton.setObjectName("ContactoButton")
        self.ContactoLogo = QPushButton(self.dockWidgetContents)
        self.ContactoLogo.setGeometry(QtCore.QRect(0, 450, 41, 41))
        self.ContactoLogo.setStyleSheet("background-color:rgb(170, 170, 255);\nborder-style:solid;\nborder-radius:20px;\nborder-width:2px;\nborder-color:rgb(159, 115, 255);")
        self.ContactoLogo.setText("")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("C:\\Users\\denis\\Downloads\\../../../../../../../Downloads/pngegg.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.ContactoLogo.setIcon(icon2)
        self.ContactoLogo.setIconSize(QtCore.QSize(30, 30))
        self.ContactoLogo.setObjectName("ContactoLogo")
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        _translate = QtCore.QCoreApplication.translate
        DockWidget.setWindowTitle(_translate("DockWidget", "DockWidget"))
        self.AdopcionButton.setText(_translate("DockWidget", "Adopcion"))
        self.AlimentosButton.setText(_translate("DockWidget", "Alimentos"))
        self.JuguetesButton.setText(_translate("DockWidget", "Juguetes"))
        self.AccesorioButtom.setText(_translate("DockWidget", "Medicamentos"))
        self.BusquedaButton.setText(_translate("DockWidget", "Busqueda"))
        self.ContactoButton.setText(_translate("DockWidget", "Contacto"))
