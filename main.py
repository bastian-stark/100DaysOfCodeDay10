#Basic Calculator App

#Operations

def calculation(num1, num2, oper):
    """Use operator to determine outcome of two numbers together"""
    if oper == "+":
        return num1 + num2
    elif oper == "-":
        return num1 - num2
    elif oper == "*":
        return num1 * num2
    elif oper == "/":
        return num1 / num2
    else:
        print('Error')


#Intro
print('Welcome to Python Calculator!')
#Program loop
state = 1
while state != 0:
    #Calculation loop
    num1 = int(input("What's the first number?: "))
    status = 1
    while status != 0:
        print('+\n-\n*\n/')
        oper = input("Pick an operation from above: ")
        num2 = int(input("What's the next number?: "))
        calc = calculation(num1, num2, oper)
        print(f'{num1} {oper} {num2} = {calc}')
        cont = input(f'Type "y" to continue calculating with {calc}, or type "n" to start a new calculation: ')
        if cont == "n":
            status = 0
            if input('Type "y" if you would like to start a new calculation or "n" if you would like to quit: ') == "n":
                state = 0
            else:
                print('Beginning new calculation...')
        elif cont == "y":
            num1 = calc
        else:
            print('Error')
