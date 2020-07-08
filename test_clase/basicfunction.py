# Ejemplo de funciones basico para tests unitarios

class BasicFunction(object):
    def __init__(self):
        self.state = 0
    
    def incrementState(self):
        self.state += 2

    def clearState(self):
        self.state = 0
