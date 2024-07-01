import csv

class Usuario:
    def __init__(self, username, nombre, apellido, correo, password, cargo):
        self.username = username
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = password
        self.cargo = cargo

    def get_username(self):
        return self.username
    
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_correo(self):
        return self.correo
    
    def get_password(self):
        return self.password
    
    def get_cargo(self):
        return self.cargo

    def set_username(self, username):
        self.username = username
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def set_apellido(self, apellido):
        self.apellido = apellido
        
    def set_correo(self, correo):
        self.correo = correo
        
    def set_password(self, password):
        self.password = password
    
    def set_cargo(self, cargo):
        self.cargo = cargo
    
    try:  #Crea el archivo en caso de que no exista
        with open('usuarios.csv', mode= 'x', newline='') as file:
            escritor = csv.writer(file)
            escritor.writerow(['Username', 'Nombre', 'Apellido', 'Correo', 'Contraseña', 'Cargo'])
    except FileExistsError:
        pass
    
    def registrarUsuario(username, nombre, apellido, correo, password, cargo):
        usuarios = []
        usuario = Usuario(username, nombre, apellido, correo, password, cargo)
        usuario.set_username(username)
        usuario.set_nombre(nombre)
        usuario.set_apellido(apellido)
        usuario.set_correo(correo)
        usuario.set_password(password)
        usuario.set_cargo(cargo)
        usuarios.append(usuario)
        with open('usuarios.csv', mode='a', newline='') as file:
          writer = csv.writer(file)
          for usuario in usuarios:
              writer.writerow([usuario.get_username(), usuario.get_nombre(), usuario.get_apellido(), usuario.get_correo(), usuario.get_password(), usuario.get_cargo()])
    
    def cargarUsuarios():
        try:
            with open('usuarios.csv', mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Omite la primera línea que contiene los encabezados
                for row in reader:
                    username, nombre, apellido, correo, password, cargo = row[:6]
                    usuario = Usuario(username, nombre, apellido, correo, password, cargo)
                    usuarios.append(usuario)
        except FileNotFoundError:
            print("No se encuentra el archivo CSV")
            
usuarios = []

class Administrador(Usuario):
    def __init__(self, username, nombre, apellido, correo, password):
        super().__init__(username, nombre, apellido, correo, password, "admin")
        self.es_admin = True

    def funciones_especificas(self):
        print("Funciones específicas del administrador")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un administrador
    admin = Administrador("admin1", "Oscar", "Mansilla", "Oscar@example.com", "admincontra")
    usuarios.append(admin)
    
    # Mostrar información de los usuarios
    for usuario in usuarios:
        print(f"Username: {usuario.get_username()}, Nombre: {usuario.get_nombre()}, Cargo: {usuario.get_cargo()}")
    
    # Llamar a una función específica del administrador
    admin.funciones_especificas()

    