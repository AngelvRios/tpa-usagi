from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from usuario import Usuario
import csv

class Ui_RegistroWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Registro")
        MainWindow.resize(700, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(700, 1000))
        MainWindow.setMaximumSize(QtCore.QSize(700, 1000))
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.marcoTextos = QtWidgets.QLabel(parent=self.centralwidget)
        self.marcoTextos.setGeometry(QtCore.QRect(140, 300, 421, 600))
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

        self.nombre = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(180, 410, 344, 62))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(14)
        self.nombre.setFont(font)
        self.nombre.setStyleSheet("border: 2px solid #000000;\n"
                                   "background-color: rgb(255, 255, 255);")
        self.nombre.setText("")
        self.nombre.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombre.setObjectName("nombre")

        self.apellido = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.apellido.setGeometry(QtCore.QRect(180, 490, 344, 62))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(14)
        self.apellido.setFont(font)
        self.apellido.setStyleSheet("border: 2px solid #000000;\n"
                                   "background-color: rgb(255, 255, 255);")
        self.apellido.setText("")
        self.apellido.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.apellido.setObjectName("apellido")

        self.emailUser = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.emailUser.setGeometry(QtCore.QRect(180, 570, 344, 62))
        self.emailUser.setFont(font)
        self.emailUser.setStyleSheet("border: 2px solid #000000;\n"
                                     "background-color: rgb(255, 255, 255);")
        self.emailUser.setText("")
        self.emailUser.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.emailUser.setObjectName("emailUser")

        self.cntUser = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.cntUser.setGeometry(QtCore.QRect(180, 650, 344, 62))
        self.cntUser.setFont(font)
        self.cntUser.setStyleSheet("border: 2px solid #000000;\n"
                                   "background-color: rgb(255, 255, 255);")
        self.cntUser.setText("")
        self.cntUser.setMaxLength(30)
        self.cntUser.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.cntUser.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cntUser.setObjectName("cntUser")

        self.cntUserConfirm = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.cntUserConfirm.setGeometry(QtCore.QRect(180, 730, 344, 62))
        self.cntUserConfirm.setFont(font)
        self.cntUserConfirm.setStyleSheet("border: 2px solid #000000;\n"
                                          "background-color: rgb(255, 255, 255);")
        self.cntUserConfirm.setText("")
        self.cntUserConfirm.setMaxLength(30)
        self.cntUserConfirm.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.cntUserConfirm.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cntUserConfirm.setObjectName("cntUserConfirm")

        self.btnRegistrar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnRegistrar.setGeometry(QtCore.QRect(260, 810, 196, 46))
        font.setPointSize(12)
        self.btnRegistrar.setFont(font)
        self.btnRegistrar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnRegistrar.setStyleSheet("border-color: black;\n"
                                        "border-radius: 10px;\n"
                                        "border-width: 2px;\n"
                                        "border-style:solid;\n"
                                        "background-color: rgb(255, 137, 224);\n"
                                        "")
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.btnRegistrar.clicked.connect(self.funcionRegistro)
        

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Registro"))
        self.nomUser.setPlaceholderText(_translate("MainWindow", "Nombre de Usuario"))
        self.nombre.setPlaceholderText(_translate("MainWindow", "Nombre"))
        self.apellido.setPlaceholderText(_translate("MainWindow", "Apellido"))
        self.emailUser.setPlaceholderText(_translate("MainWindow", "Correo Electrónico"))
        self.cntUser.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.cntUserConfirm.setPlaceholderText(_translate("MainWindow", "Confirmar Contraseña"))
        self.btnRegistrar.setText(_translate("MainWindow", "Registrar"))

    def VentanaEmergente(self, Mensaje, Titulo):
        vEmergente = QMessageBox()
        vEmergente.setText(Mensaje)
        vEmergente.setWindowTitle(Titulo)       
        vEmergente.exec()
        
    def funcionRegistro(self):
        nomuser = self.nomUser.text()
        nombre = self.nombre.text()
        apellido = self.apellido.text()
        email = self.emailUser.text()
        contrasena = self.cntUser.text()
        contrasenaConf = self.cntUserConfirm.text()
        cargo = "Cliente"
        if(nomuser.strip()== "" or nombre.strip() == "" or apellido.strip() == "" or email.strip() == ""):
            self.VentanaEmergente("Faltan datos por ingresar", "Error")
        elif (self.verificarUserRepetido(nomuser)):
            self.VentanaEmergente("El nombre de usuario indicado se encuentra en uso", "Error")
        elif (self.verificarCorreoRepetido(email)):
            self.VentanaEmergente("El correo indicado ya se encuentra en uso", "Error")
        elif (contrasena != contrasenaConf):
            self.VentanaEmergente("Las contraseñas indicadas no son iguales", "Error")
        else:
            Usuario.registrarUsuario(nomuser, nombre, apellido, email, contrasena, cargo)
            self.VentanaEmergente("El usuario "+ nomuser +" se ha registrado existosamente", "Registro")

        
    def verificarUserRepetido(self, username):
            with open('usuarios.csv', mode='r') as file:
                reader = csv.reader(file)
                for fila in reader:
                    if (username == fila[1]):
                        return True     
            return False
                    
    def verificarCorreoRepetido(self, email):
            with open('usuarios.csv', mode='r') as file:
                reader = csv.reader(file)
                for fila in reader:
                    if (email == fila[4]):
                        return True
            return False        