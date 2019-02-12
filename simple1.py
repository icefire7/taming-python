print('Hello World!') #Hello World!
#print(2 +'2') # unsupported operand type(s) for +: 'int' and 'str'
print('Python ' *3) #Python Python Python 
print(3 * 'Python ') #Python Python Python 
#strings can be multiplied only by int
line1 = input('Enter a number:') #input is of string type
num1 = int(line1) #type casting/conversion
num2 = int(input('Enter another number:'))
print('sum: ' + str(num1 + num2))
#print(num++) #that's a NO. py doesn't have '++' operator
num1+=1
print('num1 + 1 = '+str(num1))
