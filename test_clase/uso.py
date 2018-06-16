from liquidacion import Liquidacion

print("Liquidacion de sueldos de prueba")
horas = input("Ingrese cantidad de horas trabajadas: ")
antiguedad = input("Ingrese la antiguedad del empleado: ")
liq = Liquidacion()
print("Se procede con la liquidacion: ")
basico = liq.calcularSueldoBasico(horas)
print("El sueldo basico es de: $ " + str(basico))
bruto = liq.calcularSueldoBruto(basico,antiguedad)
print("El sueldo bruto es de: $ " + str(bruto))
neto = liq.calcularSueldoNeto(bruto)
print("El sueldo a pagar es de: $ " + str(neto))