class LCD:
    def Numero0(ancho,alto):
       A=["|"+(" "*(ancho)) + "|"]
       matriz=[
           [" _"],
           ["| |"],
           ["|_|"],
       ] 
       if ancho>1:
           matriz[0][0]=" "+("_"*(ancho))
           matriz[1][0]="|"+(" "*(ancho)) + "|"
           matriz[2][0]="|"+("_"*(ancho))+"|"
       if alto>1:
           matriz.insert(1 , A*(alto-2))
       return matriz
    def Numero1(ancho,alto):
        matriz=[
            ["|"],
            ["|"]
        ]
        if alto>1:
            matriz.insert(2 , "|"*(alto-1))
            matriz.insert(1 , "|"*(alto-1))
        return matriz
    def Numero2(ancho,alto):
        V1=[(" "*ancho) +" |"]
        V2=["|"]
        matriz= [[" _"],
                 [" _|"],
                 ["|_"]]
        if ancho>1:
            matriz[0][0]=" "+("_"*(ancho)) +" "
            matriz[1][0]=" "+("_"*(ancho-1)) + "_|"
            matriz[2][0]="|_"+("_"*(ancho-1)) 
        if alto>1:
            matriz.insert(2 , V2*(alto-1))
            matriz.insert(1 , V1*(alto-1))
        return matriz
    def Numero3(ancho,alto):
        V=[(" "*ancho) +"|"]
        matriz = [
            ["_"],
            ["_|"],
            ["_|"]
        ]
        if ancho >1:
            matriz[0][0]=("_"*(ancho))
            matriz[1][0]=("_"*(ancho-1)) + "_|"
            matriz[2][0]=("_"*(ancho-1)) + "_|"
        if alto >1:
            matriz.insert(2 , V*(alto-1))
            matriz.insert(1 , V*(alto-1))
        return matriz
    def Numero4(ancho,alto):
        V=[(" "*ancho) +" |"]
        V2=["|" +(" "*(ancho-1)) +" |"]
        matriz = [
            ["|_|"],
            ["  |"]
        ]
        if ancho>1:
            matriz[0][0]=("|" + "_"*(ancho)) + "|"
            matriz[1][0]=(" "*(ancho)) + " |"
        if alto>1:
          
            matriz.insert(1 , V*(alto))
            matriz.insert(0 , V2*(alto-1))
        return matriz
    def Numero5(ancho,alto):
        V=[(" "*ancho) +" |"]
        V1=["| "+(" "*ancho) ]
        matriz=[
            [" _"],
            ["|_"],
            [" _|"]
        ]
        if ancho>1:
            matriz[0][0]=(" " + "_"*(ancho)) 
            matriz[1][0]=("|"+"_"*(ancho))
            matriz[2][0]=" "+("_"*(ancho))+"|"
        if alto>1:
            matriz.insert(2 , V*(alto))
            matriz.insert(1 , V1*(alto))
        return matriz
    def Numero6(ancho,alto):
        V=[("|" + " " * ancho)+"|" ]
        V1=["| "+(" "*ancho) ]
        matriz=[
            [" _"],
            ["|_"],
            ["|_|"]
        ]
        if ancho>1:
            matriz[0][0]=(" "+ "_"*(ancho))
            matriz[1][0]=("|"+"_"*(ancho))
            matriz[2][0]=("|"+"_"*(ancho))+"|"
        if alto>1:
            matriz.insert(2 , V*(alto))
            matriz.insert(1 , "|"*(alto))
        return matriz
    def Numero7(ancho, alto):
        V =[(" "*ancho)+"|"]
        matriz=[
            ["_"],
            [" |"],
            [" |"]
        ]
        if ancho>1:
            matriz[0][0]=("_"*(ancho))
            matriz[1][0]=(" "*(ancho))+"|"
            matriz[2][0]=(" "*(ancho))+"|"
        if alto>1:
            matriz.insert(2 , V*(alto))
            matriz.insert(1 , V*(alto))
        return matriz
    def Numero8(ancho,alto):
        V=[("|" + " " * ancho)+"|" ]
        matriz=[
            [" _ "],
            ["|_|"],
            ["|_|"]
        ]
        if ancho>1:
            matriz[0][0]=" "+("_"*(ancho))
            matriz[1][0]="|"+("_"*(ancho))+"|"
            matriz[2][0]="|"+("_"*(ancho))+"|"
        if alto>1:
            matriz.insert(2 , V*(alto-1))
            matriz.insert(1 , V*(alto-1))
        return matriz
    def Numero9(ancho, alto):
        V=[("|" + " " * ancho)+"|" ]
        V1=[(" " * ancho)+" |" ]
        matriz=[
            [" _"],
            ["|_|"],
            [" _|"]
        ]
        if ancho>1:
            matriz[0][0]=" "+("_"*(ancho))
            matriz[1][0]="|"+("_"*(ancho))+"|"
            matriz[2][0]=" "+("_"*(ancho))+"|"
        if alto>1:
            matriz.insert(2,V1*(alto-1))
            matriz.insert(1,V*(alto-1))
        return matriz
    
class MostrarNumeros:
    def pedirNumeros(numeros,ancho,alto):
        digitos = [int(i) for i in str(numeros)]
        llamarClases=[
                      LCD.Numero0(ancho,alto),
                      LCD.Numero1(ancho,alto),
                      LCD.Numero2(ancho,alto),
                      LCD.Numero3(ancho,alto),
                      LCD.Numero4(ancho,alto),
                      LCD.Numero5(ancho,alto),
                      LCD.Numero6(ancho,alto),
                      LCD.Numero7(ancho,alto),
                      LCD.Numero8(ancho,alto),
                      LCD.Numero9(ancho,alto)
                    ]

        for N in digitos:
            M = llamarClases[N]
            for n in M:
                for x in n:
                    print(x)

MostrarNumeros.pedirNumeros(55,5,5)
