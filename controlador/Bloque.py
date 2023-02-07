import hashlib
import json
import Moneda
import Usuario
from Usuario import Usuario
from Moneda import Moneda



class Bloque:
    user1 = Usuario()
    user2 = Usuario()
    Moneda1 = Moneda(2)
    monedaPropietario = {}
    data = {}
    usuarios = []
    hashAnterior = hashlib.md5()
    usuarios = list()
    monedas = list()
    hashPropio = [hashlib.new('md5')]
    def __init__(self, hashAnterior):
        self.hashAnterior = hashAnterior  
        self.LlenarMonedas(self.monedas)

    def IniciarJson(data):
       
        data['transaccion'] = ['hola']

        with open('./modelo/transacciones.json','w') as f:
        
            json.dump(data,f)
        
        
        f.close   
    def setHash (hasp):
        f = open('./modelo/transacciones.json')    # Se abre el archivo con la información
        lineas = f.readlines()    # Se leen las lineas del archivo
        h = hashlib.new('md5')    # Se crea el objeto de clase hash
        for linea in lineas:
            linea = str.encode(linea)  # Se convierte el string en un byte string
            h.update(linea)    # Se agregan las lineas del archivo al objeto hash
        hasp.insert(0, str(h.hexdigest()))
        print("El resultado en hexadecimales del hash es: " +hasp[0])
        
    def resgistrarUsuario(usuarios):
         usuarios.append(Usuario.new())
     
    def realizarTransaccion(data, usuarioPropietario = Usuario, usuarioTransferido = Usuario, monedas = Moneda):
        transaccion = str(usuarioPropietario.getSeudo()) +"transfiere" + str(monedas.getIdMoneda()) + "a  " + str(usuarioTransferido.getSeudo())
        data['transaccion'].append('nombre holmes')
        data['transaccion'].append('nombre holmes')
        data['transaccion'].append(transaccion)
        with open('./modelo/transacciones.json','w') as f:
            
            json.dump(data,f)

        
        
        f.close   
     
        
        print
    def LlenarMonedas(monedas):
        for i in range(1,50,1): 
            monedas[i-1].append(Moneda(i-1))       
    IniciarJson(data)
    #LlenarMonedas(monedas)
    setHash(hashPropio)
    realizarTransaccion(data, user1, user2, Moneda1)
    print(hashPropio[0])
    
        
pass  