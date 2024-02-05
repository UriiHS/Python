### Variables
#a = "El resultado es: "                  
#b = 12                                   
#c = -1                                  
#print(a,b+c)                            Resultado para mostrar varias variables
#print(2*8)                              Se pueden hacer operaciones con los numeros sin declararlo como varaible
#print("La division es: ",round(8/3))    round() sirve para redondear decimales

### Arrays or List
#array = [a, b, "tercer valor"]          Asi se crea una array/list
#print(array)                            Asi se muestra una array
#print(array[1])                         Asi se muestra un valor en una posicion x en una array/list
#array.append("nuevo valor añadido")     El append() sirve para añadir un nuevo valor a la array/list
#array.pop()                             El pop() sirve para eliminar el último valor añadido a la array/list
#array.pop(1)                            Borra el valor que este en la posición indicada en el pop()   
#print(len(array))                       len() muestra la longitud de lo que haya dentro varaible, string, etc...

## Mini ejercicio, crea una array/list con tres nombres y guarda el segundo valor de esta lista en una variable
#lista_nombres = ["Oriol","Ganzalo","Rubia"]
#nombre_a_guardar = lista_nombres[1]
#print(nombre_a_guardar)


### Dictionaries
#dict_a = {"a":"Oro","b":"Plata","c":"Bronce"}      Crea un dictionary, es similar a las arrays/list pero con el primer puesyo es la key y el segundo es el valor.
#print(dict_a)                                      Muestra todo el dictionary
#print(dict_a["a"])                                 Ponemos la key para que nos muestre su valor

### Tuples
#tup = ("a","b")                                    Sirve para guardar valores, como las arrays/list y los dictionaries
#print(tup[1])                                      Así se muestran

### Loops
#bolsa_compra = ["pasta","arroz","carne","pescado"]
#i = 0

## Bucle FOR                                        Bucle FOR que muestra todos los objetos en una lista/array  (por cada)
#for item in bolsa_compra:                          
#    print(item)

#for item in bolsa_compra:                          Bucle FORque cuenta cuanto objetos hay en la lista/array
#    i = i + 1
#    print(i)

#for item in bolsa_compra:                          Bucle que utiliza una condicion
#    i = i + 1
#    if item == "carne":
#        print("Correcto, tenemos carne y está en la posición:", i)

##Bucle while                                       Bucle WHILE hace repeticiones de lo que haya dentro hasta que se deje de cumplir la condicion  (mientras)              
#while i <= 10:
#    print(i)
#    i = i +1

### Conditionals
a ="a"
b = "b"
## Boolean values (True or False)
## El símgolo = sirve para asiganr el valor a una variable 
## El símbolo == o escribir != o poner "is" sirve para comprar dos valores
#print(a == b)
#print(a is b)

## El not delante de una variable hace que sea negativa
#print(not a == b)
#print(a != b)

## Luego estan las valores matematicos de mas grande o mas pequeño igual que ... >,<,>=,<=
##El else if se escribe "elif" y el else es else

### Functions siempre con ()
items = ["Oriol",26,09.02,"Mataró"]
## Funcion de ordenar .sort() Sirve para Strings (entre ellas) y luego con los int y float.
#items_Str = ["Herrero","García","Sobrino","Fuentes"]
# Por defecto lo ordena de forma ascendiente
#items_Str.sort()
# también se pueden usar keys para ordenar de diferente manera
#items_Str.sort(key=str.lower, reverse=True)
#Para no modificar la la variable con la lista, podemos usar sorted()
#new_items = sorted(items_Str, key=str.lower, reverse=True)

## Funcion sum(), sirve para sumar integers y floats conjuntos
numeros = [234,2344.234,768,4.67]
#print(sum(numeros))

## Para crear una funcion utilizamos "def" para definirla
#def exercise1 (num1, num2):
#    result = num1*num2
#    if( result <= 1000):
#        return result
#    else:
#        return num1+num2
#final1 = exercise1(20,30)
#print("The result is ",final1)

#range(), sirve para establecer un rango segun el valor que le pongas
#for i in range(6):
    #print(i)

#Test with range() function
#x = range(9,23)
#for elem in x:
    #print (elem)

#input(), sirve para guardar valor que ponga el usaurio
#name = input("Enter Employee Name: ")
#print(name)



