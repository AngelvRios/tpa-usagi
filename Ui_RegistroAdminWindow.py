from PyQt6 import QtCore, QtGui, QtWidgets
from usuario import Usuario
import csv
import re

class Ui_RegistroAdminWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("RegistroAdmin")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Registro Administrador"))
        self.nomUser.setPlaceholderText(_translate("MainWindow", "Nombre de Usuario"))
        self.nombre.setPlaceholderText(_translate("MainWindow", "Nombre"))
        self.apellido.setPlaceholderText(_translate("MainWindow", "Apellido"))
        self.emailUser.setPlaceholderText(_translate("MainWindow", "Correo Electrónico"))
        self.cntUser.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.cntUserConfirm.setPlaceholderText(_translate("MainWindow", "Confirmar Contraseña"))
        self.btnRegistrar.setText(_translate("MainWindow", "Registrar"))

    def VentanaEmergente(self, Mensaje, Titulo):
        vEmergente = QtWidgets.QMessageBox()
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
        cargo = "admin"
        
        if nomuser.strip() == "" or nombre.strip() == "" or apellido.strip() == "" or email.strip() == "":
            self.VentanaEmergente("Faltan datos por ingresar", "Error")
        elif not self.validarUsername(nomuser):
            self.VentanaEmergente("El nombre de usuario solo puede contener letras y números", "Error")
        elif not self.validarNombreApellido(nombre):
            self.VentanaEmergente("El nombre solo puede contener letras", "Error")
        elif not self.validarNombreApellido(apellido):
            self.VentanaEmergente("El apellido solo puede contener letras", "Error")
        elif not self.validarCorreo(email):
            self.VentanaEmergente("Ingrese un correo electrónico válido", "Error")
        elif self.verificarUserRepetido(nomuser):
            self.VentanaEmergente("El nombre de usuario indicado se encuentra en uso", "Error")
        elif self.verificarCorreoRepetido(email):
            self.VentanaEmergente("El correo indicado ya se encuentra en uso", "Error")
        elif not self.validarContrasena(contrasena):
            self.VentanaEmergente("La contraseña debe tener al menos 8 caracteres, incluyendo letras, números y un carácter especial", "Error")
        elif contrasena != contrasenaConf:
            self.VentanaEmergente("Las contraseñas indicadas no son iguales", "Error")
        else:
            Usuario.registrarUsuario(nomuser, nombre, apellido, email, contrasena, cargo)
            self.VentanaEmergente("Usuario registrado con éxito", "Éxito")

    def validarCorreo(self, correo):
        # Validar que el correo tenga un formato válido usando una expresión regular
        return bool(re.match(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$', correo))

    def verificarCorreoRepetido(self, email):
        # Verificar si el correo ya está registrado en el archivo CSV
        with open("usuarios.csv", "r", newline="") as archivo:
            lector = csv.reader(archivo)
            for row in lector:
                if row and row[3] == email:
                    return True
        return False
    
    def verificarUserRepetido(self, nomuser):
        with open("usuarios.csv", "r", newline="") as archivo:
            reader = csv.reader(archivo)
            for row in reader:
                if row and row[0] == nomuser:
                    return True
        return False

    def validarUsername(self, username):
        return bool(re.match("^[a-zA-Z0-9]+$", username))

    def validarNombreApellido(self, nombre):
        return bool(re.match("^[a-zA-Z]+$", nombre))
    
    def validarContrasena(self, contrasena):
        return bool(re.match("^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[@#$]).{8,}$", contrasena))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_RegistroAdminWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())