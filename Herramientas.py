##Esta función se encarga de calcular el área del triangulo
def CalcularArea ():
    print("Calcular el área de un triangulo")
    print("Ejemplo, un triangulo con base 50 y altura 30")
    altura=30
    base=50
    areaej=(base*altura)/2
    print(areaej)
    a=int(input("Digite el primer número "))
    b=int(input("Digite el segundo número "))
    area=(a*b)/2
    print("Su respuesta es", area)
CalcularArea()

#2
##Esta función se encarga de hallar la nota final de un estudiante
def CalcularNotaF():
    print("Calcular nota final")
    a=float(input("Digite nota parcial uno " ))
    b=float(input("Digite nota parcial dos " ))
    c=float(input("Digite nota taller " ))
    d=float(input("Digite nota proyecto " ))
    notafinal=((a/100)*25+(b/100)*25+(c/100)*20+(d/100)*30)
    print("Su nota final es", notafinal)
CalcularNotaF()
#3
##Esta función se encarga de transformar los grados de celsius a Farenheit
def transformar():
    print("Transformar grados Celsius a Farenheit")
    a=float(input("Escriba los grados Celsius "))
    farenheit=(a*9/5) + 32
    print("En Farenheit equivale a", farenheit)
transformar()
#4
#Esta función cambia el valor de los COP por diferentes monedas alrededor del mundo
def cambio():
    print("Casa de Cambio")
    n=float(input("Digite el monto en (COP) a cambiar "))
    usd=(0.00027*n)
    eur=(0.00023*n)
    yen=(0.029*n)
    usdg=(usd+(usd*0.2))
    eurg=(eur+(eur*0.2))
    yeng=(yen+(yen*0.2))
    print("En dolares equivale a", (usdg))
    print("En euros equivale a", (eurg))
    print("En yenes equivale a", (yeng))
cambio()
