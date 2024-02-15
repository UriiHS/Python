""" Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum."""

#First i create a function that needs two variables to work
def exercise1 (num1, num2):
    #We calculate the value and we save that number into a new variable
    result = num1*num2
    #Quick condition to see if the numbers is higher (we show the sum) or lower (we show the product)
    if( result <= 1000):
        return result
    else:
        return num1+num2
    
final1 = exercise1(20,30)
#print("The result is ",final1)

final2 = exercise1(40,30)
#print("The result is ",final2)

"""Exercise 2: Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number."""

# The first one is my solution
def exercise2 (rango):
    # We declare a variable, that will help us in the loop
    i = 0
    #We create a loop that will loop through all the numbers in the range 
    while i <= rango:
        #Variable that will define the previous number
        previus_num = i-1
        #Quick condition, to prevent going into the negatives
        if (previus_num < 0):
            previus_num = 0
        print("Current Number ",i," Previous Number ",previus_num," Sum: ",i+previus_num )
        i += 1

#exercise2(10)

#Website solution
def exercise2_2 (rango):
    previous_num = 0
    for i in range(1, rango):                  #Utiliza la funcion range()
        x_sum = previous_num + i
        print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
        previous_num = i

#exercise2_2(11)

"""Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number."""

def exercise3 ():
    #We ask for any word using inpu()
    texto = input("Write any word: ")
    #We calculate the length of the word
    long_texto = len(texto)
    #Loop that goes through the word, with a increment of 2 in the range()
    for i in range(0, long_texto, 2):
        print("Index[",i,"]", texto[i])

#exercise3()

"""Exercise 4: Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old"""

#We import the datetime module
import datetime

def exercise4 ():
    #We ask for the name and the age
    nombre = input("What is your name? ")
    edad = int(input("How old are you? "))
    #Using the datetime module, we find the actual year
    año_actual = datetime.datetime.now().year
    #We show the name, with the operation that will tell the year that they will turn 100 years old
    print(nombre, "cumplirás los 100 años el año: ", año_actual + 100 - edad)

#exercise4()d

"""Not finish Extra 1     Make it more complex, and ask for the birth date and show exactly how many days/months/years untill turning 100"""
    
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
                
"""Exercise 5 Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user."""
                
def exercise5():
    #We ask the user for a number, and we use int() to make sure is an integer
    numero_cliente = int(input("Write a number: "))
    #We calculate if it's a odd or even number
    par_or_not = numero_cliente % 2
    #Conditional for showing the results
    if(par_or_not >= 1):
        print("The number is odd")
    else:
        print("The number is even")

#exercise5()

"""Extra 1  If the number is a multiple of 4, print out a different message."""

def exercise5_1():
    #Same as before, but with an extra operation to found the multiples of 4
    numero_cliente = int(input("Write a number: "))
    par_or_not = numero_cliente % 2
    multiple_4 = numero_cliente % 4
    #Same as before, but with the new condition 
    if(multiple_4>=1):
        if(par_or_not >= 1):
            print("The number is odd")
        else:
            print("The number is even")
    else:
        print("The number is even and a multiple of 4")
   
#exercise5_1()

"""Extra 2  Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
            If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

def exercise5_2():
    numero_cliente = int(input("Escribe un número: "))
    numero_check = int(input("Escribe otro número: "))
    #Quick maths to find the results
    resultado = numero_cliente % numero_check
    total = numero_cliente / numero_check

    if(resultado >= 1):
        print("The number: ",numero_cliente," it does not divide evenly: ",numero_check)
    else:
        print("The number: ",numero_cliente," it does divide evenly: ",numero_check, " and the result is: ",total)

#exercise5_2()
        
"""Exercise 6   Take a list and write a program that prints out all the elements of the list that are less than 5."""

def exercise6(num):
    #We declare the variables with their values
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    i = 0
    #Loop to find how many numbers are less than the number we asked the user
    while i < len(a):
        if(a[i]<num):
            print (a[i])
        i += 1

#exercise6(15)

"""Extra 1       Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list."""

def exercise6_1(num):
    #The same as before, but in this one we make a new list and has all the elements lower than the number from the user
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    i = 0
    b = []

    while i < len(a):
        if(a[i]<num):
            b.append(a[i]) 
        i += 1

    print(b)

#exercise6_1(15)

"""Extra 2       Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user."""

def exercise6_2():
    #This time, we asked the user for the number using input()
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
    
"""Exercise 7   Create a program that asks the user for a number and then prints out a list of all the divisors of that number."""

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

## Exercise 8   Take two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates)
def exercise8():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []

    for num in a:
        if num in b:
            if num not in c:
                c.append(num)
    
    print(c)

# exercise8()

## Extra 1  Randomly generate two lists to test this
import random

def exercise8_1():
    #I Create 3 list needed for this exercise
    a = []
    b = []
    c = []

    #This here, creates a random value for the lenght of the list
    long_a = random.randrange(1,101)    #Note: This one only includes the first number(1) and does not include the last number (101) <1-100>
    long_b = random.randint(1,100)     #Note: This one includes both numbers (1) and (100) <1-100>

    #I create two variables with a value of 0 that will help me in the loop
    i = 0
    e = 0
    #Two loops for adding random numbers in the a and b lists, the amount of numbers is equal to the previous numbers i generated randomly
    while i < long_a:
        a.append(random.randrange(1,101))
        i += 1
    while e < long_b:
        b.append(random.randint(1,100))
        e += 1

    #Quick loop that searches all values inside the lists and adds them into a new list (c)
    for num in a:
        if num in b:
            if num not in c:
                c.append(num)
    
    print(c)

#exercise8_1()

"""Exercise 9   Ask the user for a string and print out whether this string is a palindrome or not.
                (A palindrome is a string that reads the same forwards and backwards.)"""

def exercise9():
    phrase = str(input("Write a phrase (Careful with the MAYUS): "))
    phrase_len = len(phrase)          
    i = 0
    x = 0
    
    for i in range(0, phrase_len):
          #This compares the first letter with the last in recursive order 1 - last ,  2 - last-1, 3 - last-2, etc...
        if(phrase[i]==phrase[phrase_len-1-i]): 
            #We use this variable to help us keeping track if the letters are the same           
            x += 1   
            #If they're the same, we show that the String is a plindrome                                      
            if x == phrase_len:                             
                print("This ", phrase, " is a palindrome")
        else:
            #If not, we show that is not, and we stop the loop
            print("This ", phrase, " is not a palindrome")  
            exit()
        i += 1

#exercise9()
        
"""Exercise 10  Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
                Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it."""

def exercise10():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    #Really close as you would write it in english: Save (even) in the list for each (even) in the other list (a) if the condition is meet.   
    new_a = [even for even in a if even%2==0 ]
    print(new_a)

#exercise10()

"""Exercise 11  Make a two-player Rock-Paper-Scissors game"""

def exercise11():
    #Function that will determine players picks and who won
    def player_pick():
        player_1 = input("Player 1 Your Move: (Rock/Paper/Scissors): ")
        while (player_1 != "Rock") or (player_1 != "Paper") or (player_1 != "Scissors"):
            if(player_1 == "Rock") or (player_1 == "Paper") or (player_1 == "Scissors"):
                break
            else:
                player_1 = input("Wrong move Player 1 >:( Try again (Rock/Paper/Scissors): ")
        player_2 = input("Player 2 Yout Move: (Rock/Paper/Scissors): ")
        while (player_2 != "Rock") or (player_2 != "Paper") or (player_2 != "Scissors"):
            if(player_2 == "Rock") or (player_2 == "Paper") or (player_2 == "Scissors"):
                break
            else:
                player_2 = input("Wrong move PLayer 2 >:( Try again (Rock/Paper/Scissors): ")
        
        if(player_1=="Rock" and player_2=="Scissors") or (player_1=="Paper" and player_2=="Rock") or (player_1=="Scissors" and player_2=="Paper"):
            print("Player 1 has chosen; ",player_1," and Player 2 has chosen: ",player_2," and the Winner is Player 1 Woooooo")
        elif(player_2=="Rock" and player_1=="Scissors") or (player_2=="Paper" and player_1=="Rock") or (player_2=="Scissors" and player_1=="Paper"):
             print("Player 1 has chosen; ",player_1," and Player 2 has chosen: ",player_2," and the Winner is Player 2 Woooooo")
        else:
            print("You both manage to draw, better luck next time!")
    #Function to play again
    def play_again():
        play= input("Wanna play again ? (Yes/No)")
        while play == "Yes":
            player_pick()
            play_again()
        
        if(play=="No"):
            print("Respectable, have a nice day!")
            exit()
        else:
            print("Broskiwi, Yes or No, it's not that hard: (Yes/No)")
            play_again()

    player_pick()
    play_again()

#exercise11()
    
"""Exercise 12  Generate a random number between 1 and 9 (including 1 and 9). 
                Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
   Extra 1:     Keep the game going until the user types “exit”
   Extra 2:     Keep track of how many guesses the user has taken, and when the game ends, print this out."""

def exercise12():
    print("Let's play a game, try to find which number is this -> X")
    random_number = random.randint(1,9)            
    user_number = input("Your guess: ")
    tries = 1
    if user_number == "exit":
        exit
    else:
        user_number = int(user_number)
        if random_number == user_number:
            print("Congratulations the number was: ", user_number," and you found it in ", tries, "tries")
            exercise12()
        else:
            while random_number != user_number:
                if user_number < random_number:
                    user_number = int(input("Wrong, Try a higher number: "))
                else:
                    user_number = int(input("Wrong, Try a lower number: "))
                tries += 1
            print("Congratulations the number was: ", user_number," and you found it in ", tries, "tries")
            exercise12()

#exercise12()