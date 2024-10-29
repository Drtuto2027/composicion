class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"El motor {self.tipo} está encendido.")

    def apagar(self):
        self.encendido = False
        print(f"El motor {self.tipo} está apagado.")

class Coche:
    def __init__(self, marca, tipo_motor):
        self.marca = marca
        self.motor = Motor(tipo_motor)  # Se crea el motor al crear el coche

    def encender_motor(self):
        if not self.motor.encendido:
            self.motor.encender()
        else:
            print("El motor ya está encendido.")

    def apagar_motor(self):
        if self.motor.encendido:
            self.motor.apagar()
        else:
            print("El motor ya está apagado.")

# Crear un coche con un motor de tipo específico
coche1 = Coche("Toyota", "Gasolina")

# Encender el motor del coche
coche1.encender_motor()

# Intentar encender el motor nuevamente
coche1.encender_motor()

# Apagar el motor del coche
coche1.apagar_motor()

# Intentar apagar el motor nuevamente
coche1.apagar_motor()
