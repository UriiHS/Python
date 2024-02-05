## Exercise 1: Calculate the multiplication and sum of two numbers
#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def exercise1 (num1, num2):
    result = num1*num2
    if( result <= 1000):
        return result
    else:
        return num1+num2
    
final1 = exercise1(20,30)
#print("The result is ",final1)

final2 = exercise1(40,30)
#print("The result is ",final2)

##Exercise 2: Print the sum of the current number and the previous number
#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
#Mi solución (He echo un poco extra para que sea una función y puedas poner el rango que quieras.)
def exercise2 (rango):
    i = 0
    while i <= rango:
        previus_num = i-1
        if (previus_num < 0):
            previus_num = 0
        print("Current Number ",i," Previous Number ",previus_num," Sum: ",i+previus_num )
        i += 1
# print(exercise2(10))
#Solución de la página

def exercise2_2 (rango):
    previous_num = 0
    for i in range(1, rango):                  #Utiliza la funcion range()
        x_sum = previous_num + i
        print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
        previous_num = i

#print(exercise2_2(11))

## Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

#texto = input("Escribe cualquier palabra: ")

#long_texto = len(texto)
#def exercise3 (texto):
#    for i in range(0, long_texto, 2):
#        print("Index[",i,"]", texto[i])


## Exercise 4: Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old

import datetime

def exercise4 ():
    nombre = input("Como te llamas: ")
    edad = int(input("Escribe tu edad: "))
    año_actual = datetime.datetime.now().year
    print(nombre, "cumplirás los 100 años el año: ", año_actual + 100 - edad)

#exercise4()

#Vamos a hacer el ejercicio 4, pero esta vez pedirás la fecha de nacimiento y lo calculará
    
def exercise4_2():
    nombre = input("Como te llamas: ")
    fecha_nacimiento = input("Escribe la fecha de nacimiento: (DD/MM/AAAA)")
    # Tratammos lo que ha escrito el cliente
    if (fecha_nacimiento.count("/") == 2):
        fecha_val = fecha_nacimiento.split("/")
        dia_cliente = int(fecha_val[0])
        mes_cliente = int(fecha_val[1])
        año_cliente = int(fecha_val[2])
    else:
        print("Loco, sigue las instrucciones T.T")
        exercise4_2()

    #Obtenemos los valores de la fecha actual
    fecha_actual = datetime.datetime.now()
    año_actual = fecha_actual.year
    mes_actual = fecha_actual.month
    dia_actual = fecha_actual.day

    def fecha_no_valida():
        print(" Wooah, aun no has nacido, eres del futuro lol (espabila loquete)")
        exercise4_2()

    if (año_cliente > año_actual):
        fecha_no_valida()
    elif(año_cliente == año_actual):
        if (mes_cliente > mes_actual):
            fecha_no_valida()
        elif (mes_cliente == mes_actual):
            if(dia_cliente >= dia_actual):
                fecha_no_valida()
            else:
                dia_restante = 30 - dia_actual + dia_cliente
                meses_restantes = 11
                años_restantes = 99
                print("Te quedan ", dia_restante , "Dias ",meses_restantes," Meses",años_restantes," Años, para cumplir 100 años") 
        else:    
            if(dia_cliente >= dia_actual):
                dia_restante = dia_cliente- dia_actual 
                meses_restantes = 12 - mes_actual + mes_cliente
                años_restantes = 99
                print("Te quedan ", dia_restante , "Dias ",meses_restantes," Meses",años_restantes," Años, para cumplir 100 años")
            else:
                dia_restante = 30 - dia_actual + dia_cliente
                meses_restantes = 12 - mes_actual + mes_cliente
                años_restantes = 99
                print("Te quedan ", dia_restante , "Dias ",meses_restantes," Meses",años_restantes," Años, para cumplir 100 años") 
    else:
        if (mes_cliente > mes_actual):
            if (dia_cliente >= dia_actual):
                dia_restante = dia_cliente - dia_actual
                meses_restantes = mes_cliente - mes_actual
                años_restantes = año_actual - año_cliente + 100
                print("Te quedan ", dia_restante , "Dias ",meses_restantes," Meses",años_restantes," Años, para cumplir 100 años")
            else:
                dia_restante = 30 - dia_actual + dia_cliente
                meses_restantes = mes_cliente - mes_actual -1
                años_restantes = año_actual - año_cliente + 100
                print("Te quedan ", dia_restante , "Dias ",meses_restantes," Meses",años_restantes," Años, para cumplir 100 años")
        elif (mes_cliente == mes_actual):
            if(dia_cliente >= dia_actual):
                dia_restante = dia_cliente - dia_actual
                meses_restantes = mes_cliente - mes_actual
                años_restantes = año_actual - año_cliente + 99
                print("Te quedan ", dia_restante , "Dias ",meses_restantes," Meses",años_restantes," Años, para cumplir 100 años")
            else:
                dia_restante = 30 - dia_actual + dia_cliente
                meses_restantes = mes_cliente - mes_actual -1
                años_restantes = año_actual - año_cliente + 100
                print("Te quedan ", dia_restante , "Dias ",meses_restantes," Meses",años_restantes," Años, para cumplir 100 años")
        else:    
            if(dia_cliente >= dia_actual):
                dia_restante = dia_cliente - dia_actual
                meses_restantes =12 + mes_cliente - mes_actual
                años_restantes = año_actual - año_cliente + 100
                print("Te quedan ", dia_restante , "Dias ",meses_restantes," Meses",años_restantes," Años, para cumplir 100 años")
            else:
                dia_restante = 30 - dia_actual + dia_cliente
                meses_restantes =12 + mes_cliente - mes_actual
                años_restantes = año_actual - año_cliente + 100
                print("Te quedan ", dia_restante , "Dias ",meses_restantes," Meses",años_restantes," Años, para cumplir 100 años")
                

# exercise4_2()
                
##Exercise 5 Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#Extra 2    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
            #If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
                
def exercise5():
    numero_cliente = input("Escribe un número: ")
    numero_cliente = int(numero_cliente)
    par_or_not = numero_cliente % 2

    if(par_or_not >= 1):
        print("El número que has escrito es impar")
    else:
        print("El número que has escrito es par")

#exercise5()

#Extra 1    If the number is a multiple of 4, print out a different message.

def exercise5_1():
    numero_cliente = input("Escribe un número: ")
    numero_cliente = int(numero_cliente)
    par_or_not = numero_cliente % 2
    multiple_4 = numero_cliente % 4

  
    if(multiple_4>=1):
        if(par_or_not >= 1):
            print("El número que has escrito es impar")
        else:
            print("El número que has escrito es par")
    else:
        print("El número que has escrito es par y además es multiple de 4")
   

#exercise5_1()

#Extra 2    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
            #If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

def exercise5_2():
    numero_cliente = input("Escribe un número: ")
    numero_check = input("Escribe otro número: ")
    numero_cliente = int(numero_cliente)
    numero_check = int(numero_check)

    resultado = numero_cliente % numero_check
    total = numero_cliente / numero_check

    if(resultado >= 1):
        print("El número: ",numero_cliente," que has puesto, no es divisible por: ",numero_check)
    else:
        print("El número: ",numero_cliente," que has puesto, es divisible por: ",numero_check, " y da como resultado: ",total)

#exercise5_2()
        
## Exercise 6   Take a list and write a program that prints out all the elements of the list that are less than 5.

def exercise6(num):
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    i = 0

    while i < len(a):
        if(a[i]<num):
            print (a[i])
        i += 1

#exercise6(15)

#Extra 1       Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
def exercise6_1(num):
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    i = 0
    b = []

    while i < len(a):
        if(a[i]<num):
            b.append(a[i]) 
        i += 1

    print(b)

#exercise6_1(15)

#Extra 2       Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

def exercise6_2():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    i = 0
    b = []

    num = int(input("Escribe un valor: "))

    while i < len(a):
        if(a[i]<num):
            b.append(a[i]) 
        i += 1

    print(b)

#exercise6_2()
    
## Exercise 7   Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

def exercise7():
    num = int(input("Escribe un número: "))

    i = 1
    divisores = []
    while i <= num:
        resultado = num%i
        if (resultado==0):
            divisores.append(i)
        i += 1
    print(divisores)

"""
Solution in website
num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)
"""

#exercise7()
