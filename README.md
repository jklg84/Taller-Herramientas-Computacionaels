# Taller-Herramientas-Computacionaels
## **Punto 1**
### Expliación
En el problema uno se desarrolla un algoritmo el cual se encargar de hallar el área del triangulo.
Continuando con el problema 1, este algoritmo recibe como entrada la **altura** y la **base** del triangulo. El proceso consiste en multiplicar su base por su altura y al resultado de la operación anteriormente mencionada dividirla entre 2. Por último la salida del problema es el **área del triangulo** la cual es el residuo de la división entre 2.
* La implementacion en python, puede verse en el archivo : "Herramientas.py"*
~~~
def CalcularArea ():
    print("Calcular el area de un triangulo")
    print("Ejemplo, un triangulo con base 50 y altura 30")
    altura=30
    base=50
    areaej=(basealtura)/2
    print(areaej)
    a=int(input("Escribe el primer numero "))
    b=int(input("Escribe el segundo numero "))
    area=(ab)/2
    print("Su respuesta es", area)
CalcularArea()
~~~
___
## **Punto 2**
### Expliación
El problema 2 consiste en hallar la nota final de un estudiante la cual se encuentra por medio de la suma de las notas de las tareas, 2 parciales y un proyecto, las cuales tienen tiene el valor de 20 por ciento, 25 por ciento cada parcial y 30 por ciento respectivamente.
Continuando con el problema 2, este algoritmo recibe como entrada las **todas las notas** que obtuvo el estudiante, el proceso consiste en sacarle el porcentaje respectivo a cada una de las notas y al final sumarlas para obtener la nota final. Por úlitmo la salida consiste en la **nota final** que obtuvo el estudiante. *La implementacion en python, puede verse en el archivo : "Herramientas.py"*
~~~
def CalcularNotaF():
    print("Calcular nota final")
    a=float(input("Escriba nota parcial uno " ))
    b=float(input("Escriba nota parcial dos " ))
    c=float(input("Escriba nota taller " ))
    d=float(input("Escriba nota proyecto " ))
    notafinal=((a/100)25+(b/100)25+(c/100)20+(d/100)30)
    print("Su nota final es", notafinal)
CalcularNotaF()
~~~
___
## **Punto 3**
### Explicación
En el problema número 3 se requiere un cambio de valores dentro de la temperatura, en este caso de grados celsius a farenheit , donde con una formula universal se pretende encontrar el equivalente.
La entrada de este problema consiste en digitar los **grados celsius**, que posteriormente pasarán a ser guardados en una variable en la que se desarrollara una formula correspondiente a la transformación de celsius a farenheit,la salida es  un **valor final** que será impreso con la variable anterior y será el resultado en grados farenheit. *La implementacion en python, puede verse en el archivo : "Herramientas.py"*
~~~
def transformar():
    print("Transformar grados Celsius a Farenheit")
    a=float(input("Escriba los grados Celsius "))
    farenheit=(a*9/5) + 32
    print("En Farenheit equivale a", farenheit)
transformar()
~~~
___
## **Punto 4**
### Expliación
Este problema consiste en realizar un cambio de valores, teniendo en cuenta la tasa de cambio monetaria, en la cual se va a hacer de pesos colombianos a yenes, dolares y euros, lo que pretende alcanzar el valor correspondiente de pesos colombianos en cada moneda.
La entrada recibe el valor correspondiente a **pesos colombianos**, luego, se tienen en cuenta variables con el valor actual de cambio hacia cada moneda, y con estos valores se procede a realizar la respectiva formula de cambio en cada una, para que al final, en la salida se tenga el valor correspondiente al **cambio de moneda colombiana** en dolares, yenes y euros. *La implementacion en python, puede verse en el archivo : "Herramientas.py"*
~~~
def cambio():
    print("Casa de Cambio")
    n=float(input("Digite el monto en (COP) a cambiar "))
    usd=(0.00027n)
    eur=(0.00023n)
    yen=(0.029n)
    usdg=(usd+(usd0.2))
    eurg=(eur+(eur0.2))
    yeng=(yen+(yen0.2))
    print("En dolares equivale a", (usdg))
    print("En euros equivale a", (eurg))
    print("En yenes equivale a", (yeng))
cambio()
~~~
