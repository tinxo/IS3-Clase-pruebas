
def leerArchivoNombres(nombreArchivo):
    #Lectura del archivo de candidatos
    candidatos = []
    try:
        archivo = open(nombreArchivo, 'r')
        candidatos = archivo.readlines()
        archivo.close()
    except:
        return -1   
    return candidatos

def pedirVotos(candidatos):
    dicc = {} #clave = nombre del candidato | valor = votos obtenidos
    for unCandidato in candidatos.readlines():
        #print(unCandidato)
        votos = int(input('Ingrese los votos para el candidato ' + unCandidato + ':'))
        dicc[unCandidato] = votos

#print(dicc)
votosB = int(input('Ingrese los votos en blanco:'))
dicc['En blanco'] = votosB

suma = 0
mayor = 0
ganador = ''
for elemento in dicc:
    if (dicc[elemento] > mayor):
        mayor = dicc[elemento]  #votos
        ganador = elemento      #nombre
    suma += dicc[elemento]

for elemento in dicc:
    porcentaje = (dicc[elemento]*100)/suma
    print(elemento + ' - ' + str(dicc[elemento]) + ' votos - ' + str(porcentaje) + '%')

print('Nuevo gobernador: ' + ganador + ' con ' + str(mayor) + ' votos.')