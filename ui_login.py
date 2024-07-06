from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from usuario import Usuario, usuarios
from ventanaadmin import VentanaAdmin
from ui_registro import *

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        Usuario.cargarUsuarios()
        MainWindow.setObjectName("Login")
        MainWindow.resize(700, 720)
        MainWindow.setMinimumSize(QtCore.QSize(700, 720))
        MainWindow.setMaximumSize(QtCore.QSize(700, 720))
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.marcoTextos = QtWidgets.QLabel(parent=self.centralwidget)
        self.marcoTextos.setGeometry(QtCore.QRect(140, 300, 421, 370))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.marcoTextos.setFont(font)
        self.marcoTextos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border: 2px solid #000000;")
        self.marcoTextos.setText("")
        self.marcoTextos.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.marcoTextos.setObjectName("marcoTextos")

        self.nomUser = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.nomUser.setGeometry(QtCore.QRect(180, 330, 344, 62))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(14)
        self.nomUser.setFont(font)
        self.nomUser.setStyleSheet("border: 2px solid #000000;\n"
                                   "background-color: rgb(255, 255, 255);")
        self.nomUser.setText("")
        self.nomUser.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nomUser.setObjectName("nomUser")

        self.cntUser = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.cntUser.setGeometry(QtCore.QRect(180, 410, 344, 62))
        self.cntUser.setFont(font)
        self.cntUser.setStyleSheet("border: 2px solid #000000;\n"
                                   "background-color: rgb(255, 255, 255);")
        self.cntUser.setText("")
        self.cntUser.setMaxLength(30)
        self.cntUser.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.cntUser.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cntUser.setObjectName("cntUser")

        self.btnIngresar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnIngresar.setGeometry(QtCore.QRect(260, 520, 196, 46))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnIngresar.setFont(font)
        self.btnIngresar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnIngresar.setStyleSheet("border-color: black;\n"
                                       "border-radius: 10px;\n"
                                       "border-width: 2px;\n"
                                       "border-style:solid;\n"
                                       "background-color: rgb(255, 137, 224);\n"
                                       "")
        self.btnIngresar.setObjectName("btnIngresar")
        self.btnIngresar.clicked.connect(self.Inicio)

        self.btnRegistro = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnRegistro.setGeometry(QtCore.QRect(260, 580, 196, 46))
        self.btnRegistro.setFont(font)
        self.btnRegistro.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnRegistro.setStyleSheet("border-color: black;\n"
                                       "border-radius: 10px;\n"
                                       "border-width: 2px;\n"
                                       "border-style:solid;\n"
                                       "background-color: rgb(255, 137, 224);\n"
                                       "")
        self.btnRegistro.setObjectName("btnRegistro")
        self.btnRegistro.clicked.connect(self.open_register_window)

        self.Logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(270, 50, 171, 181))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("C:/Users/icede/Downloads/patitas.png"))
        self.Logo.setObjectName("Logo")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.nomUser.setPlaceholderText(_translate("MainWindow", "Nombre de Usuario"))
        self.cntUser.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.btnIngresar.setText(_translate("MainWindow", "Ingresar"))
        self.btnRegistro.setText(_translate("MainWindow", "Registro"))

    def VentanaEmergente(self, Mensaje, Titulo):
        vEmergente = QMessageBox()
        vEmergente.setText(Mensaje)
        vEmergente.setWindowTitle(Titulo)       
        vEmergente.exec()


    def Inicio(self):
        nombredeusuario = self.nomUser.text().lower()
        contrasena = self.cntUser.text()
        user.append(nombredeusuario)
        
        if nombredeusuario.strip() == "" or contrasena.strip() == "":
            self.VentanaEmergente("Hay datos que no ha ingresado", "Error")
        else:
            for usuario in usuarios:
                if nombredeusuario == usuario.get_username() and contrasena == usuario.get_password():
                    self.VentanaEmergente("Ha iniciado sesión correctamente", "Inicio de sesión")
                    if usuario.get_cargo() == "admin":
                        self.abrirVentanaAdmin()
                        return  # Salir después de abrir la ventana admin
                    else:
                        self.abrirVentanaPrincipal()
                        return  # Salir después de abrir la ventana principal
            self.VentanaEmergente("Sus datos están incorrectos", "Error")

    def open_register_window(self):
        self.ui_register = Ui_RegistroWindow()
        self.register_window = QtWidgets.QMainWindow()
        self.ui_register.setupUi(self.register_window)
        self.register_window.show()

    def abrirVentanaAdmin(self):
        self.ventanaAdmin = VentanaAdmin()
        self.ventanaAdmin.show()
        main_window = self.centralwidget.parent()
        main_window.close()

    def abrirVentanaPrincipal(self):
        from principal import VentanaPrincipal
        self.ventanaPrincipal = VentanaPrincipal()
        self.ventanaPrincipal.show()
            
        main_window = self.centralwidget.parent()
        main_window.close()

user = []