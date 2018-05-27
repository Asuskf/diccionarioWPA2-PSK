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
        if inicioCedula[:1] == '0':
            while inicio <= final:
                total = 0
                numeroLetras = str(inicio)
                tipo = int(numeroLetras[2])
                if tipo >= 0 and tipo <= 6:
                    base = 10
                    digitoVerificador = int(numeroLetras[-1])
                    proceso = (2, 1, 2, 1, 2, 1, 2, 1, 2)
                elif (tipo == 6):
                    base = 11
                    digitoVerificador = int(numeroLetras[-1])
                    proceso = (4, 3, 2, 7, 6, 5, 4, 3, 3)
                for i in range(0, len(proceso)):
                    calcular = int(numeroLetras[i]) * proceso[i]
                    if (tipo >= 0 and tipo <= 6) or tipo == 9:
                        total += calcular if calcular < 10 else int(str(calcular)[0]) + int(str(calcular)[1])
                    else:
                        total += calcular
                modulo = total % base
                val = base - modulo if modulo != 0 else 0
                validar = val == digitoVerificador
                if validar == True:
                    archivo.write('0'+numeroLetras + '\n')
                    archivo.write('0'+numeroLetras + '001\n')
                inicio += 1
        else:
            while inicio <= final:
                total = 0
                numeroLetras = str(inicio)
                tipo = int(numeroLetras[2])
                if tipo >= 0 and tipo <= 6:
                    base = 10
                    digitoVerificador = int(numeroLetras[-1])
                    proceso = (2, 1, 2, 1, 2, 1, 2, 1, 2)
                elif (tipo == 6):
                    base = 11
                    digitoVerificador = int(numeroLetras[-1])
                    proceso = (4, 3, 2, 7, 6, 5, 4, 3, 3)
                for i in range(0, len(proceso)):
                    calcular = int(numeroLetras[i]) * proceso[i]
                    if (tipo >= 0 and tipo <= 6) or tipo == 9:
                        total += calcular if calcular < 10 else int(str(calcular)[0]) + int(str(calcular)[1])
                    else:
                        total += calcular
                modulo = total % base
                val = base - modulo if modulo != 0 else 0
                validar = val == digitoVerificador
                if validar == True:
                    archivo.write(numeroLetras + '\n')
                    archivo.write(numeroLetras + '001\n')
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
