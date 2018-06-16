# Ejemplo un poco mas elaborado para llegar a tests de integracion

class Liquidacion(object):
    def __init__(self):
        self.valorHora = 250
        self.pctBonificacion = 8
        self.pctRetenciones = 11
        self.pctObraSocial = 3

    def calcularSueldoBasico(self, hsTrabajadas):
        # Basico = horas trabajadas * valor hora
        basico = hsTrabajadas * self.valorHora
        return basico

    def calcularSueldoBruto(self, basico, antiguedad):
        # Bruto = basico + bonificaciones + antiguedad
        bruto = basico + (basico * (self.pctBonificacion * 0.01))
        if (antiguedad < 5):
            bruto = bruto + (basico * 0.1) # 10%
        elif (antiguedad < 10):
            bruto = bruto + (basico * 0.2) # 20%
        elif (antiguedad < 20):
            bruto = bruto + (basico * 0.3) # 30%
        else:
            bruto = bruto + (basico * 0.4) # 40%
        return bruto

    def calcularSueldoNeto(self, bruto):
        # Neto = bruto - retenciones - obra social
        neto = bruto - (bruto * (self.pctRetenciones * 0.01)) - (bruto * (self.pctObraSocial * 0.01))
        return neto

    def calcularSueldoEmpleado(self, cantHorasTrabajadas, antiguedadEmpleado):
        sueldoBasico = self.calcularSueldoBasico(cantHorasTrabajadas)
        sueldoBruto = self.calcularSueldoBruto(sueldoBasico, antiguedadEmpleado)
        sueldoNeto = self.calcularSueldoNeto(sueldoBruto)
        return sueldoNeto