print(True>False)   #LOL. It's True
if True<False:
    print('False is greater')
else:
    print('False is smaller')
#and we have 'elif' as 'else if' in java or JS
num = int(input('Enter a number:'))
if num!=0:
    if num > 0 and num%2==0:
        print(str(num) +' is even, positive')
    elif num<0 or num%3==0:
        print(str(num) +' is negative or divisble by 3')
    else:
        print(str(num) +' is odd')
#while loop
print('All even numbers below '+str(num))
while num>0:
    if num%2==0:
        num-=2
    else:
        num-=1
    if num==0:
        break       #py has 'continue' as well
    print(num)
        
