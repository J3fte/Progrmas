class LCD:
    def NumerosPrincipales(N):
        #Se crea una lista de listas que obtiene los patrones de los numeros
        Numeros = [
            [' _ ','|  |', '|_|'],#Numero 0
            ['   ', '  |', '  |'],#Numero 1
            [' _ ', ' _|', '|_ '],#Numero 2
            [' _ ', ' _|', ' _|'],#Numero 3
            ['   ', '|_|', '  |'],#Numero 4
            [' _ ', '|_ ', ' _|'],#Numero 5
            [' _ ', '|_ ', '|_|'],#Numero 6
            [' _ ', '  |', '  |'],#Numero 7
            [' _ ', '|_|', '|_|'],#Numero 8
            [' _ ', '|_|', ' _|'],#Numero 9
        ]
        #En una variavles se obtiene los patrones que se van a solicitar
        NumerosPedidos = Numeros[N]
        #se regresan los patrones
        return NumerosPedidos
    
    def MostrarNumeros(numeros):
        #La lista contiene los numeros que llegan con la funcion y se separan los valores y cada numero este en una posicion de la lista
        digitos = [int(i) for i in str(numeros)]
        #Se obtiene una lista la que contiene los patrones usando la lista digitos
        numerosLcd = [LCD.NumerosPrincipales(i) for i in digitos]
        #El for es para darle la altura de 3
        for valor in range(3):
            linea = ''
            for numeroLcd in numerosLcd:
                linea += numeroLcd[valor] + ''
            print(linea) 
            
LCD.MostrarNumeros(2)  
