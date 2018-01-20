#Programa paraea leer desde un archivo y entregue el número de palabras y letras

def leer_archivo(archivo='archivo.txt'):
    file=open(archivo,'r')
    data=file.readlines()
    file.close()
    return data

def verificar_palabra(palabra):
    if  not palabra.isdigit():
        return True
    else:
        return False

def verificar_letra(palabra):
    letra=0
    for i in palabra:
        if not i.isdigit():
            letra += 1
    return letra
       
def numero_palabras(data):
    contador=0
    for renglon in data:
        for palabra in renglon.split(' '):
            if verificar_palabra(palabra):
                contador += 1
    print("Numero de palabras %s" %(str(contador)))

def numero_letras(data):
    letra=0
    for renglon in data:
        for palabra in renglon.split(' '):
            if verificar_palabra(palabra):
                letra += verificar_letra(palabra)
    print("Numero de letras %s" %(str(letra)))


data = leer_archivo()
numero_palabras(data)
numero_letras(data)
