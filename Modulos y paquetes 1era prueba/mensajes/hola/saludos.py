def saludar():
    print("Hola, te saludo desde saludos.saludar()")

def prueba():
    print("Esto es una nueva prueba de la nueva version")

class Saludo:
    def __init__(self):
        print("Hola, te saludo desde Saludo.__init__()")

print(__name__)

if __name__ == '__main__':
    saludar()